# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cas20200630 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'cas.aliyuncs.com',
            'ap-northeast-2-pop': 'cas.aliyuncs.com',
            'ap-southeast-3': 'cas.aliyuncs.com',
            'ap-southeast-5': 'cas.aliyuncs.com',
            'cn-beijing': 'cas.aliyuncs.com',
            'cn-beijing-finance-1': 'cas.aliyuncs.com',
            'cn-beijing-finance-pop': 'cas.aliyuncs.com',
            'cn-beijing-gov-1': 'cas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cas.aliyuncs.com',
            'cn-chengdu': 'cas.aliyuncs.com',
            'cn-edge-1': 'cas.aliyuncs.com',
            'cn-fujian': 'cas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cas.aliyuncs.com',
            'cn-hangzhou-finance': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cas.aliyuncs.com',
            'cn-hangzhou-test-306': 'cas.aliyuncs.com',
            'cn-hongkong': 'cas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cas.aliyuncs.com',
            'cn-huhehaote': 'cas.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'cas.aliyuncs.com',
            'cn-north-2-gov-1': 'cas.aliyuncs.com',
            'cn-qingdao': 'cas.aliyuncs.com',
            'cn-qingdao-nebula': 'cas.aliyuncs.com',
            'cn-shanghai': 'cas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cas.aliyuncs.com',
            'cn-shanghai-finance-1': 'cas.aliyuncs.com',
            'cn-shanghai-inner': 'cas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cas.aliyuncs.com',
            'cn-shenzhen': 'cas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'cas.aliyuncs.com',
            'cn-shenzhen-inner': 'cas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cas.aliyuncs.com',
            'cn-wuhan': 'cas.aliyuncs.com',
            'cn-wulanchabu': 'cas.aliyuncs.com',
            'cn-yushanfang': 'cas.aliyuncs.com',
            'cn-zhangbei': 'cas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cas.aliyuncs.com',
            'cn-zhangjiakou': 'cas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cas.aliyuncs.com',
            'eu-west-1': 'cas.aliyuncs.com',
            'eu-west-1-oxs': 'cas.aliyuncs.com',
            'rus-west-1-pop': 'cas.aliyuncs.com',
            'us-east-1': 'cas.aliyuncs.com',
            'us-west-1': 'cas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assign_certificate_count_with_options(
        self,
        request: main_models.AssignCertificateCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignCertificateCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_total_count):
            query['CertTotalCount'] = request.cert_total_count
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignCertificateCount',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignCertificateCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_certificate_count_with_options_async(
        self,
        request: main_models.AssignCertificateCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignCertificateCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_total_count):
            query['CertTotalCount'] = request.cert_total_count
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignCertificateCount',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignCertificateCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_certificate_count(
        self,
        request: main_models.AssignCertificateCountRequest,
    ) -> main_models.AssignCertificateCountResponse:
        runtime = RuntimeOptions()
        return self.assign_certificate_count_with_options(request, runtime)

    async def assign_certificate_count_async(
        self,
        request: main_models.AssignCertificateCountRequest,
    ) -> main_models.AssignCertificateCountResponse:
        runtime = RuntimeOptions()
        return await self.assign_certificate_count_with_options_async(request, runtime)

    def create_client_certificate_with_options(
        self,
        request: main_models.CreateClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.san_type):
            query['SanType'] = request.san_type
        if not DaraCore.is_null(request.san_value):
            query['SanValue'] = request.san_value
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_certificate_with_options_async(
        self,
        request: main_models.CreateClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.san_type):
            query['SanType'] = request.san_type
        if not DaraCore.is_null(request.san_value):
            query['SanValue'] = request.san_value
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_certificate(
        self,
        request: main_models.CreateClientCertificateRequest,
    ) -> main_models.CreateClientCertificateResponse:
        runtime = RuntimeOptions()
        return self.create_client_certificate_with_options(request, runtime)

    async def create_client_certificate_async(
        self,
        request: main_models.CreateClientCertificateRequest,
    ) -> main_models.CreateClientCertificateResponse:
        runtime = RuntimeOptions()
        return await self.create_client_certificate_with_options_async(request, runtime)

    def create_client_certificate_with_csr_with_options(
        self,
        request: main_models.CreateClientCertificateWithCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientCertificateWithCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.san_type):
            query['SanType'] = request.san_type
        if not DaraCore.is_null(request.san_value):
            query['SanValue'] = request.san_value
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientCertificateWithCsr',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientCertificateWithCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_certificate_with_csr_with_options_async(
        self,
        request: main_models.CreateClientCertificateWithCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientCertificateWithCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.san_type):
            query['SanType'] = request.san_type
        if not DaraCore.is_null(request.san_value):
            query['SanValue'] = request.san_value
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClientCertificateWithCsr',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientCertificateWithCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_certificate_with_csr(
        self,
        request: main_models.CreateClientCertificateWithCsrRequest,
    ) -> main_models.CreateClientCertificateWithCsrResponse:
        runtime = RuntimeOptions()
        return self.create_client_certificate_with_csr_with_options(request, runtime)

    async def create_client_certificate_with_csr_async(
        self,
        request: main_models.CreateClientCertificateWithCsrRequest,
    ) -> main_models.CreateClientCertificateWithCsrResponse:
        runtime = RuntimeOptions()
        return await self.create_client_certificate_with_csr_with_options_async(request, runtime)

    def create_custom_certificate_with_options(
        self,
        request: main_models.CreateCustomCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_passthrough):
            query['ApiPassthrough'] = request.api_passthrough
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.validity):
            query['Validity'] = request.validity
        if not DaraCore.is_null(request.custom_identifier):
            query['customIdentifier'] = request.custom_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_certificate_with_options_async(
        self,
        request: main_models.CreateCustomCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_passthrough):
            query['ApiPassthrough'] = request.api_passthrough
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.validity):
            query['Validity'] = request.validity
        if not DaraCore.is_null(request.custom_identifier):
            query['customIdentifier'] = request.custom_identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_certificate(
        self,
        request: main_models.CreateCustomCertificateRequest,
    ) -> main_models.CreateCustomCertificateResponse:
        runtime = RuntimeOptions()
        return self.create_custom_certificate_with_options(request, runtime)

    async def create_custom_certificate_async(
        self,
        request: main_models.CreateCustomCertificateRequest,
    ) -> main_models.CreateCustomCertificateResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_certificate_with_options_async(request, runtime)

    def create_external_cacertificate_with_options(
        self,
        tmp_req: main_models.CreateExternalCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalCACertificateResponse:
        tmp_req.validate()
        request = main_models.CreateExternalCACertificateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_passthrough):
            request.api_passthrough_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_passthrough, 'ApiPassthrough', 'json')
        query = {}
        if not DaraCore.is_null(request.api_passthrough_shrink):
            query['ApiPassthrough'] = request.api_passthrough_shrink
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.validity):
            query['Validity'] = request.validity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_external_cacertificate_with_options_async(
        self,
        tmp_req: main_models.CreateExternalCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateExternalCACertificateResponse:
        tmp_req.validate()
        request = main_models.CreateExternalCACertificateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.api_passthrough):
            request.api_passthrough_shrink = Utils.array_to_string_with_specified_style(tmp_req.api_passthrough, 'ApiPassthrough', 'json')
        query = {}
        if not DaraCore.is_null(request.api_passthrough_shrink):
            query['ApiPassthrough'] = request.api_passthrough_shrink
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.validity):
            query['Validity'] = request.validity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateExternalCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateExternalCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_external_cacertificate(
        self,
        request: main_models.CreateExternalCACertificateRequest,
    ) -> main_models.CreateExternalCACertificateResponse:
        runtime = RuntimeOptions()
        return self.create_external_cacertificate_with_options(request, runtime)

    async def create_external_cacertificate_async(
        self,
        request: main_models.CreateExternalCACertificateRequest,
    ) -> main_models.CreateExternalCACertificateResponse:
        runtime = RuntimeOptions()
        return await self.create_external_cacertificate_with_options_async(request, runtime)

    def create_revoke_client_certificate_with_options(
        self,
        request: main_models.CreateRevokeClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRevokeClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRevokeClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRevokeClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_revoke_client_certificate_with_options_async(
        self,
        request: main_models.CreateRevokeClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRevokeClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRevokeClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRevokeClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_revoke_client_certificate(
        self,
        request: main_models.CreateRevokeClientCertificateRequest,
    ) -> main_models.CreateRevokeClientCertificateResponse:
        runtime = RuntimeOptions()
        return self.create_revoke_client_certificate_with_options(request, runtime)

    async def create_revoke_client_certificate_async(
        self,
        request: main_models.CreateRevokeClientCertificateRequest,
    ) -> main_models.CreateRevokeClientCertificateResponse:
        runtime = RuntimeOptions()
        return await self.create_revoke_client_certificate_with_options_async(request, runtime)

    def create_root_cacertificate_with_options(
        self,
        request: main_models.CreateRootCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRootCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRootCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRootCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_root_cacertificate_with_options_async(
        self,
        request: main_models.CreateRootCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRootCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRootCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRootCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_root_cacertificate(
        self,
        request: main_models.CreateRootCACertificateRequest,
    ) -> main_models.CreateRootCACertificateResponse:
        runtime = RuntimeOptions()
        return self.create_root_cacertificate_with_options(request, runtime)

    async def create_root_cacertificate_async(
        self,
        request: main_models.CreateRootCACertificateRequest,
    ) -> main_models.CreateRootCACertificateResponse:
        runtime = RuntimeOptions()
        return await self.create_root_cacertificate_with_options_async(request, runtime)

    def create_server_certificate_with_options(
        self,
        request: main_models.CreateServerCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_certificate_with_options_async(
        self,
        request: main_models.CreateServerCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_certificate(
        self,
        request: main_models.CreateServerCertificateRequest,
    ) -> main_models.CreateServerCertificateResponse:
        runtime = RuntimeOptions()
        return self.create_server_certificate_with_options(request, runtime)

    async def create_server_certificate_async(
        self,
        request: main_models.CreateServerCertificateRequest,
    ) -> main_models.CreateServerCertificateResponse:
        runtime = RuntimeOptions()
        return await self.create_server_certificate_with_options_async(request, runtime)

    def create_server_certificate_with_csr_with_options(
        self,
        request: main_models.CreateServerCertificateWithCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerCertificateWithCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerCertificateWithCsr',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerCertificateWithCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_certificate_with_csr_with_options_async(
        self,
        request: main_models.CreateServerCertificateWithCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerCertificateWithCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_time):
            query['AfterTime'] = request.after_time
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.before_time):
            query['BeforeTime'] = request.before_time
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country):
            query['Country'] = request.country
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.days):
            query['Days'] = request.days
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.immediately):
            query['Immediately'] = request.immediately
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.months):
            query['Months'] = request.months
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServerCertificateWithCsr',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerCertificateWithCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_certificate_with_csr(
        self,
        request: main_models.CreateServerCertificateWithCsrRequest,
    ) -> main_models.CreateServerCertificateWithCsrResponse:
        runtime = RuntimeOptions()
        return self.create_server_certificate_with_csr_with_options(request, runtime)

    async def create_server_certificate_with_csr_async(
        self,
        request: main_models.CreateServerCertificateWithCsrRequest,
    ) -> main_models.CreateServerCertificateWithCsrResponse:
        runtime = RuntimeOptions()
        return await self.create_server_certificate_with_csr_with_options_async(request, runtime)

    def create_sub_cacertificate_with_options(
        self,
        request: main_models.CreateSubCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.crl_day):
            query['CrlDay'] = request.crl_day
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.extended_key_usages):
            query['ExtendedKeyUsages'] = request.extended_key_usages
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.path_len_constraint):
            query['PathLenConstraint'] = request.path_len_constraint
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sub_cacertificate_with_options_async(
        self,
        request: main_models.CreateSubCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSubCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.crl_day):
            query['CrlDay'] = request.crl_day
        if not DaraCore.is_null(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not DaraCore.is_null(request.extended_key_usages):
            query['ExtendedKeyUsages'] = request.extended_key_usages
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.path_len_constraint):
            query['PathLenConstraint'] = request.path_len_constraint
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.years):
            query['Years'] = request.years
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSubCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSubCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sub_cacertificate(
        self,
        request: main_models.CreateSubCACertificateRequest,
    ) -> main_models.CreateSubCACertificateResponse:
        runtime = RuntimeOptions()
        return self.create_sub_cacertificate_with_options(request, runtime)

    async def create_sub_cacertificate_async(
        self,
        request: main_models.CreateSubCACertificateRequest,
    ) -> main_models.CreateSubCACertificateResponse:
        runtime = RuntimeOptions()
        return await self.create_sub_cacertificate_with_options_async(request, runtime)

    def delete_client_certificate_with_options(
        self,
        request: main_models.DeleteClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_certificate_with_options_async(
        self,
        request: main_models.DeleteClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_certificate(
        self,
        request: main_models.DeleteClientCertificateRequest,
    ) -> main_models.DeleteClientCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_client_certificate_with_options(request, runtime)

    async def delete_client_certificate_async(
        self,
        request: main_models.DeleteClientCertificateRequest,
    ) -> main_models.DeleteClientCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_client_certificate_with_options_async(request, runtime)

    def describe_cacertificate_with_options(
        self,
        request: main_models.DescribeCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificate_with_options_async(
        self,
        request: main_models.DescribeCACertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCACertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificate(
        self,
        request: main_models.DescribeCACertificateRequest,
    ) -> main_models.DescribeCACertificateResponse:
        runtime = RuntimeOptions()
        return self.describe_cacertificate_with_options(request, runtime)

    async def describe_cacertificate_async(
        self,
        request: main_models.DescribeCACertificateRequest,
    ) -> main_models.DescribeCACertificateResponse:
        runtime = RuntimeOptions()
        return await self.describe_cacertificate_with_options_async(request, runtime)

    def describe_cacertificate_count_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificateCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCACertificateCount',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificateCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificate_count_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificateCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeCACertificateCount',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificateCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificate_count(self) -> main_models.DescribeCACertificateCountResponse:
        runtime = RuntimeOptions()
        return self.describe_cacertificate_count_with_options(runtime)

    async def describe_cacertificate_count_async(self) -> main_models.DescribeCACertificateCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_cacertificate_count_with_options_async(runtime)

    def describe_cacertificate_list_with_options(
        self,
        request: main_models.DescribeCACertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_status):
            query['CaStatus'] = request.ca_status
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.issuer_type):
            query['IssuerType'] = request.issuer_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.valid_status):
            query['ValidStatus'] = request.valid_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCACertificateList',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificate_list_with_options_async(
        self,
        request: main_models.DescribeCACertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCACertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ca_status):
            query['CaStatus'] = request.ca_status
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.issuer_type):
            query['IssuerType'] = request.issuer_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.valid_status):
            query['ValidStatus'] = request.valid_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCACertificateList',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCACertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificate_list(
        self,
        request: main_models.DescribeCACertificateListRequest,
    ) -> main_models.DescribeCACertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_cacertificate_list_with_options(request, runtime)

    async def describe_cacertificate_list_async(
        self,
        request: main_models.DescribeCACertificateListRequest,
    ) -> main_models.DescribeCACertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cacertificate_list_with_options_async(request, runtime)

    def describe_certificate_private_key_with_options(
        self,
        request: main_models.DescribeCertificatePrivateKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertificatePrivateKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypted_code):
            query['EncryptedCode'] = request.encrypted_code
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertificatePrivateKey',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertificatePrivateKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificate_private_key_with_options_async(
        self,
        request: main_models.DescribeCertificatePrivateKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertificatePrivateKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypted_code):
            query['EncryptedCode'] = request.encrypted_code
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertificatePrivateKey',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertificatePrivateKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificate_private_key(
        self,
        request: main_models.DescribeCertificatePrivateKeyRequest,
    ) -> main_models.DescribeCertificatePrivateKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_certificate_private_key_with_options(request, runtime)

    async def describe_certificate_private_key_async(
        self,
        request: main_models.DescribeCertificatePrivateKeyRequest,
    ) -> main_models.DescribeCertificatePrivateKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_certificate_private_key_with_options_async(request, runtime)

    def describe_client_certificate_with_options(
        self,
        request: main_models.DescribeClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_with_options_async(
        self,
        request: main_models.DescribeClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate(
        self,
        request: main_models.DescribeClientCertificateRequest,
    ) -> main_models.DescribeClientCertificateResponse:
        runtime = RuntimeOptions()
        return self.describe_client_certificate_with_options(request, runtime)

    async def describe_client_certificate_async(
        self,
        request: main_models.DescribeClientCertificateRequest,
    ) -> main_models.DescribeClientCertificateResponse:
        runtime = RuntimeOptions()
        return await self.describe_client_certificate_with_options_async(request, runtime)

    def describe_client_certificate_for_serial_number_with_options(
        self,
        request: main_models.DescribeClientCertificateForSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateForSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificateForSerialNumber',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateForSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_for_serial_number_with_options_async(
        self,
        request: main_models.DescribeClientCertificateForSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateForSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificateForSerialNumber',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateForSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate_for_serial_number(
        self,
        request: main_models.DescribeClientCertificateForSerialNumberRequest,
    ) -> main_models.DescribeClientCertificateForSerialNumberResponse:
        runtime = RuntimeOptions()
        return self.describe_client_certificate_for_serial_number_with_options(request, runtime)

    async def describe_client_certificate_for_serial_number_async(
        self,
        request: main_models.DescribeClientCertificateForSerialNumberRequest,
    ) -> main_models.DescribeClientCertificateForSerialNumberResponse:
        runtime = RuntimeOptions()
        return await self.describe_client_certificate_for_serial_number_with_options_async(request, runtime)

    def describe_client_certificate_status_with_options(
        self,
        request: main_models.DescribeClientCertificateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificateStatus',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_status_with_options_async(
        self,
        request: main_models.DescribeClientCertificateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificateStatus',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate_status(
        self,
        request: main_models.DescribeClientCertificateStatusRequest,
    ) -> main_models.DescribeClientCertificateStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_client_certificate_status_with_options(request, runtime)

    async def describe_client_certificate_status_async(
        self,
        request: main_models.DescribeClientCertificateStatusRequest,
    ) -> main_models.DescribeClientCertificateStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_client_certificate_status_with_options_async(request, runtime)

    def describe_client_certificate_status_for_serial_number_with_options(
        self,
        request: main_models.DescribeClientCertificateStatusForSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateStatusForSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificateStatusForSerialNumber',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateStatusForSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_status_for_serial_number_with_options_async(
        self,
        request: main_models.DescribeClientCertificateStatusForSerialNumberRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientCertificateStatusForSerialNumberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClientCertificateStatusForSerialNumber',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientCertificateStatusForSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate_status_for_serial_number(
        self,
        request: main_models.DescribeClientCertificateStatusForSerialNumberRequest,
    ) -> main_models.DescribeClientCertificateStatusForSerialNumberResponse:
        runtime = RuntimeOptions()
        return self.describe_client_certificate_status_for_serial_number_with_options(request, runtime)

    async def describe_client_certificate_status_for_serial_number_async(
        self,
        request: main_models.DescribeClientCertificateStatusForSerialNumberRequest,
    ) -> main_models.DescribeClientCertificateStatusForSerialNumberResponse:
        runtime = RuntimeOptions()
        return await self.describe_client_certificate_status_for_serial_number_with_options_async(request, runtime)

    def describe_pca_and_external_cacertificate_list_with_options(
        self,
        request: main_models.DescribePcaAndExternalCACertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePcaAndExternalCACertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePcaAndExternalCACertificateList',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePcaAndExternalCACertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pca_and_external_cacertificate_list_with_options_async(
        self,
        request: main_models.DescribePcaAndExternalCACertificateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePcaAndExternalCACertificateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePcaAndExternalCACertificateList',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePcaAndExternalCACertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pca_and_external_cacertificate_list(
        self,
        request: main_models.DescribePcaAndExternalCACertificateListRequest,
    ) -> main_models.DescribePcaAndExternalCACertificateListResponse:
        runtime = RuntimeOptions()
        return self.describe_pca_and_external_cacertificate_list_with_options(request, runtime)

    async def describe_pca_and_external_cacertificate_list_async(
        self,
        request: main_models.DescribePcaAndExternalCACertificateListRequest,
    ) -> main_models.DescribePcaAndExternalCACertificateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_pca_and_external_cacertificate_list_with_options_async(request, runtime)

    def get_cainstance_status_with_options(
        self,
        request: main_models.GetCAInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCAInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCAInstanceStatus',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCAInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cainstance_status_with_options_async(
        self,
        request: main_models.GetCAInstanceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCAInstanceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCAInstanceStatus',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCAInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cainstance_status(
        self,
        request: main_models.GetCAInstanceStatusRequest,
    ) -> main_models.GetCAInstanceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_cainstance_status_with_options(request, runtime)

    async def get_cainstance_status_async(
        self,
        request: main_models.GetCAInstanceStatusRequest,
    ) -> main_models.GetCAInstanceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_cainstance_status_with_options_async(request, runtime)

    def list_all_end_entity_instance_with_options(
        self,
        request: main_models.ListAllEndEntityInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllEndEntityInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.recursive_children):
            query['RecursiveChildren'] = request.recursive_children
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllEndEntityInstance',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllEndEntityInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_end_entity_instance_with_options_async(
        self,
        request: main_models.ListAllEndEntityInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAllEndEntityInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.recursive_children):
            query['RecursiveChildren'] = request.recursive_children
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAllEndEntityInstance',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAllEndEntityInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_end_entity_instance(
        self,
        request: main_models.ListAllEndEntityInstanceRequest,
    ) -> main_models.ListAllEndEntityInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_all_end_entity_instance_with_options(request, runtime)

    async def list_all_end_entity_instance_async(
        self,
        request: main_models.ListAllEndEntityInstanceRequest,
    ) -> main_models.ListAllEndEntityInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_all_end_entity_instance_with_options_async(request, runtime)

    def list_cacertificate_log_with_options(
        self,
        request: main_models.ListCACertificateLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCACertificateLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCACertificateLog',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCACertificateLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cacertificate_log_with_options_async(
        self,
        request: main_models.ListCACertificateLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCACertificateLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCACertificateLog',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCACertificateLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cacertificate_log(
        self,
        request: main_models.ListCACertificateLogRequest,
    ) -> main_models.ListCACertificateLogResponse:
        runtime = RuntimeOptions()
        return self.list_cacertificate_log_with_options(request, runtime)

    async def list_cacertificate_log_async(
        self,
        request: main_models.ListCACertificateLogRequest,
    ) -> main_models.ListCACertificateLogResponse:
        runtime = RuntimeOptions()
        return await self.list_cacertificate_log_with_options_async(request, runtime)

    def list_cert_with_options(
        self,
        request: main_models.ListCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_date):
            query['AfterDate'] = request.after_date
        if not DaraCore.is_null(request.before_date):
            query['BeforeDate'] = request.before_date
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_uuid):
            query['InstanceUuid'] = request.instance_uuid
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCert',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cert_with_options_async(
        self,
        request: main_models.ListCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.after_date):
            query['AfterDate'] = request.after_date
        if not DaraCore.is_null(request.before_date):
            query['BeforeDate'] = request.before_date
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_uuid):
            query['InstanceUuid'] = request.instance_uuid
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCert',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cert(
        self,
        request: main_models.ListCertRequest,
    ) -> main_models.ListCertResponse:
        runtime = RuntimeOptions()
        return self.list_cert_with_options(request, runtime)

    async def list_cert_async(
        self,
        request: main_models.ListCertRequest,
    ) -> main_models.ListCertResponse:
        runtime = RuntimeOptions()
        return await self.list_cert_with_options_async(request, runtime)

    def list_client_certificate_with_options(
        self,
        request: main_models.ListClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_certificate_with_options_async(
        self,
        request: main_models.ListClientCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClientCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClientCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_certificate(
        self,
        request: main_models.ListClientCertificateRequest,
    ) -> main_models.ListClientCertificateResponse:
        runtime = RuntimeOptions()
        return self.list_client_certificate_with_options(request, runtime)

    async def list_client_certificate_async(
        self,
        request: main_models.ListClientCertificateRequest,
    ) -> main_models.ListClientCertificateResponse:
        runtime = RuntimeOptions()
        return await self.list_client_certificate_with_options_async(request, runtime)

    def list_pca_ca_certificate_with_options(
        self,
        request: main_models.ListPcaCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPcaCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPcaCaCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPcaCaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pca_ca_certificate_with_options_async(
        self,
        request: main_models.ListPcaCaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPcaCaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPcaCaCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPcaCaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pca_ca_certificate(
        self,
        request: main_models.ListPcaCaCertificateRequest,
    ) -> main_models.ListPcaCaCertificateResponse:
        runtime = RuntimeOptions()
        return self.list_pca_ca_certificate_with_options(request, runtime)

    async def list_pca_ca_certificate_async(
        self,
        request: main_models.ListPcaCaCertificateRequest,
    ) -> main_models.ListPcaCaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.list_pca_ca_certificate_with_options_async(request, runtime)

    def list_revoke_certificate_with_options(
        self,
        request: main_models.ListRevokeCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRevokeCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRevokeCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRevokeCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_revoke_certificate_with_options_async(
        self,
        request: main_models.ListRevokeCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRevokeCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRevokeCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRevokeCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_revoke_certificate(
        self,
        request: main_models.ListRevokeCertificateRequest,
    ) -> main_models.ListRevokeCertificateResponse:
        runtime = RuntimeOptions()
        return self.list_revoke_certificate_with_options(request, runtime)

    async def list_revoke_certificate_async(
        self,
        request: main_models.ListRevokeCertificateRequest,
    ) -> main_models.ListRevokeCertificateResponse:
        runtime = RuntimeOptions()
        return await self.list_revoke_certificate_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_cacertificate_status_with_options(
        self,
        request: main_models.UpdateCACertificateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCACertificateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCACertificateStatus',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCACertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cacertificate_status_with_options_async(
        self,
        request: main_models.UpdateCACertificateStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCACertificateStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCACertificateStatus',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCACertificateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cacertificate_status(
        self,
        request: main_models.UpdateCACertificateStatusRequest,
    ) -> main_models.UpdateCACertificateStatusResponse:
        runtime = RuntimeOptions()
        return self.update_cacertificate_status_with_options(request, runtime)

    async def update_cacertificate_status_async(
        self,
        request: main_models.UpdateCACertificateStatusRequest,
    ) -> main_models.UpdateCACertificateStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_cacertificate_status_with_options_async(request, runtime)

    def update_pca_certificate_with_options(
        self,
        request: main_models.UpdatePcaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePcaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePcaCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePcaCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pca_certificate_with_options_async(
        self,
        request: main_models.UpdatePcaCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePcaCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alias_name):
            query['AliasName'] = request.alias_name
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePcaCertificate',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePcaCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pca_certificate(
        self,
        request: main_models.UpdatePcaCertificateRequest,
    ) -> main_models.UpdatePcaCertificateResponse:
        runtime = RuntimeOptions()
        return self.update_pca_certificate_with_options(request, runtime)

    async def update_pca_certificate_async(
        self,
        request: main_models.UpdatePcaCertificateRequest,
    ) -> main_models.UpdatePcaCertificateResponse:
        runtime = RuntimeOptions()
        return await self.update_pca_certificate_with_options_async(request, runtime)

    def upload_pca_cert_to_cas_with_options(
        self,
        request: main_models.UploadPcaCertToCasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadPcaCertToCasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadPcaCertToCas',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadPcaCertToCasResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_pca_cert_to_cas_with_options_async(
        self,
        request: main_models.UploadPcaCertToCasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadPcaCertToCasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadPcaCertToCas',
            version = '2020-06-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadPcaCertToCasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_pca_cert_to_cas(
        self,
        request: main_models.UploadPcaCertToCasRequest,
    ) -> main_models.UploadPcaCertToCasResponse:
        runtime = RuntimeOptions()
        return self.upload_pca_cert_to_cas_with_options(request, runtime)

    async def upload_pca_cert_to_cas_async(
        self,
        request: main_models.UploadPcaCertToCasRequest,
    ) -> main_models.UploadPcaCertToCasResponse:
        runtime = RuntimeOptions()
        return await self.upload_pca_cert_to_cas_with_options_async(request, runtime)
