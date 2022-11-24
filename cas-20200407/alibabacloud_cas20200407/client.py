# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cas20200407 import models as cas_20200407_models
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
        self._endpoint_map = {
            'cn-hangzhou': 'cas.aliyuncs.com',
            'ap-northeast-2-pop': 'cas.aliyuncs.com',
            'ap-southeast-1': 'cas.aliyuncs.com',
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
            'cn-yushanfang': 'cas.aliyuncs.com',
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_certificate_for_package_request_with_options(
        self,
        request: cas_20200407_models.CancelCertificateForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CancelCertificateForPackageRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCertificateForPackageRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CancelCertificateForPackageRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_certificate_for_package_request_with_options_async(
        self,
        request: cas_20200407_models.CancelCertificateForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CancelCertificateForPackageRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCertificateForPackageRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CancelCertificateForPackageRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_certificate_for_package_request(
        self,
        request: cas_20200407_models.CancelCertificateForPackageRequestRequest,
    ) -> cas_20200407_models.CancelCertificateForPackageRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_certificate_for_package_request_with_options(request, runtime)

    async def cancel_certificate_for_package_request_async(
        self,
        request: cas_20200407_models.CancelCertificateForPackageRequestRequest,
    ) -> cas_20200407_models.CancelCertificateForPackageRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_certificate_for_package_request_with_options_async(request, runtime)

    def cancel_order_request_with_options(
        self,
        request: cas_20200407_models.CancelOrderRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CancelOrderRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrderRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CancelOrderRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_request_with_options_async(
        self,
        request: cas_20200407_models.CancelOrderRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CancelOrderRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrderRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CancelOrderRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order_request(
        self,
        request: cas_20200407_models.CancelOrderRequestRequest,
    ) -> cas_20200407_models.CancelOrderRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_request_with_options(request, runtime)

    async def cancel_order_request_async(
        self,
        request: cas_20200407_models.CancelOrderRequestRequest,
    ) -> cas_20200407_models.CancelOrderRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_request_with_options_async(request, runtime)

    def create_certificate_for_package_request_with_options(
        self,
        request: cas_20200407_models.CreateCertificateForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateForPackageRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateForPackageRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateCertificateForPackageRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_for_package_request_with_options_async(
        self,
        request: cas_20200407_models.CreateCertificateForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateForPackageRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.company_name):
            query['CompanyName'] = request.company_name
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateForPackageRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateCertificateForPackageRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_for_package_request(
        self,
        request: cas_20200407_models.CreateCertificateForPackageRequestRequest,
    ) -> cas_20200407_models.CreateCertificateForPackageRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_for_package_request_with_options(request, runtime)

    async def create_certificate_for_package_request_async(
        self,
        request: cas_20200407_models.CreateCertificateForPackageRequestRequest,
    ) -> cas_20200407_models.CreateCertificateForPackageRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_for_package_request_with_options_async(request, runtime)

    def create_certificate_request_with_options(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateCertificateRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_request_with_options_async(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateCertificateRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_request(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_request_with_options(request, runtime)

    async def create_certificate_request_async(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_request_with_options_async(request, runtime)

    def create_certificate_with_csr_request_with_options(
        self,
        request: cas_20200407_models.CreateCertificateWithCsrRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateWithCsrRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateWithCsrRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateCertificateWithCsrRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_with_csr_request_with_options_async(
        self,
        request: cas_20200407_models.CreateCertificateWithCsrRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateWithCsrRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateWithCsrRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateCertificateWithCsrRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_with_csr_request(
        self,
        request: cas_20200407_models.CreateCertificateWithCsrRequestRequest,
    ) -> cas_20200407_models.CreateCertificateWithCsrRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_csr_request_with_options(request, runtime)

    async def create_certificate_with_csr_request_async(
        self,
        request: cas_20200407_models.CreateCertificateWithCsrRequestRequest,
    ) -> cas_20200407_models.CreateCertificateWithCsrRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_with_csr_request_with_options_async(request, runtime)

    def create_whclient_certificate_with_options(
        self,
        request: cas_20200407_models.CreateWHClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateWHClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after_time):
            query['AfterTime'] = request.after_time
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.before_time):
            query['BeforeTime'] = request.before_time
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.months):
            query['Months'] = request.months
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.san_type):
            query['SanType'] = request.san_type
        if not UtilClient.is_unset(request.san_value):
            query['SanValue'] = request.san_value
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWHClientCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateWHClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_whclient_certificate_with_options_async(
        self,
        request: cas_20200407_models.CreateWHClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateWHClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after_time):
            query['AfterTime'] = request.after_time
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.before_time):
            query['BeforeTime'] = request.before_time
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country):
            query['Country'] = request.country
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.months):
            query['Months'] = request.months
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.san_type):
            query['SanType'] = request.san_type
        if not UtilClient.is_unset(request.san_value):
            query['SanValue'] = request.san_value
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWHClientCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.CreateWHClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_whclient_certificate(
        self,
        request: cas_20200407_models.CreateWHClientCertificateRequest,
    ) -> cas_20200407_models.CreateWHClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_whclient_certificate_with_options(request, runtime)

    async def create_whclient_certificate_async(
        self,
        request: cas_20200407_models.CreateWHClientCertificateRequest,
    ) -> cas_20200407_models.CreateWHClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_whclient_certificate_with_options_async(request, runtime)

    def decrypt_with_options(
        self,
        request: cas_20200407_models.DecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DecryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Decrypt',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DecryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrypt_with_options_async(
        self,
        request: cas_20200407_models.DecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DecryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Decrypt',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DecryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrypt(
        self,
        request: cas_20200407_models.DecryptRequest,
    ) -> cas_20200407_models.DecryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    async def decrypt_async(
        self,
        request: cas_20200407_models.DecryptRequest,
    ) -> cas_20200407_models.DecryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decrypt_with_options_async(request, runtime)

    def delete_certificate_request_with_options(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCertificateRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DeleteCertificateRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_certificate_request_with_options_async(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCertificateRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DeleteCertificateRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_certificate_request(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_certificate_request_with_options(request, runtime)

    async def delete_certificate_request_async(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_certificate_request_with_options_async(request, runtime)

    def delete_pcacert_with_options(
        self,
        request: cas_20200407_models.DeletePCACertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeletePCACertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePCACert',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DeletePCACertResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pcacert_with_options_async(
        self,
        request: cas_20200407_models.DeletePCACertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeletePCACertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePCACert',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DeletePCACertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pcacert(
        self,
        request: cas_20200407_models.DeletePCACertRequest,
    ) -> cas_20200407_models.DeletePCACertResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pcacert_with_options(request, runtime)

    async def delete_pcacert_async(
        self,
        request: cas_20200407_models.DeletePCACertRequest,
    ) -> cas_20200407_models.DeletePCACertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pcacert_with_options_async(request, runtime)

    def delete_user_certificate_with_options(
        self,
        request: cas_20200407_models.DeleteUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteUserCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DeleteUserCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_certificate_with_options_async(
        self,
        request: cas_20200407_models.DeleteUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteUserCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DeleteUserCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_certificate(
        self,
        request: cas_20200407_models.DeleteUserCertificateRequest,
    ) -> cas_20200407_models.DeleteUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_certificate_with_options(request, runtime)

    async def delete_user_certificate_async(
        self,
        request: cas_20200407_models.DeleteUserCertificateRequest,
    ) -> cas_20200407_models.DeleteUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_certificate_with_options_async(request, runtime)

    def describe_certificate_state_with_options(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificateState',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DescribeCertificateStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificate_state_with_options_async(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificateState',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DescribeCertificateStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificate_state(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_state_with_options(request, runtime)

    async def describe_certificate_state_async(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_state_with_options_async(request, runtime)

    def describe_package_state_with_options(
        self,
        request: cas_20200407_models.DescribePackageStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribePackageStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageState',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DescribePackageStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_package_state_with_options_async(
        self,
        request: cas_20200407_models.DescribePackageStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribePackageStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePackageState',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.DescribePackageStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_package_state(
        self,
        request: cas_20200407_models.DescribePackageStateRequest,
    ) -> cas_20200407_models.DescribePackageStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_package_state_with_options(request, runtime)

    async def describe_package_state_async(
        self,
        request: cas_20200407_models.DescribePackageStateRequest,
    ) -> cas_20200407_models.DescribePackageStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_package_state_with_options_async(request, runtime)

    def encrypt_with_options(
        self,
        request: cas_20200407_models.EncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.EncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Encrypt',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.EncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_with_options_async(
        self,
        request: cas_20200407_models.EncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.EncryptResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.plaintext):
            query['Plaintext'] = request.plaintext
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Encrypt',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.EncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt(
        self,
        request: cas_20200407_models.EncryptRequest,
    ) -> cas_20200407_models.EncryptResponse:
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    async def encrypt_async(
        self,
        request: cas_20200407_models.EncryptRequest,
    ) -> cas_20200407_models.EncryptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.encrypt_with_options_async(request, runtime)

    def get_cert_warehouse_quota_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetCertWarehouseQuotaResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCertWarehouseQuota',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.GetCertWarehouseQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cert_warehouse_quota_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetCertWarehouseQuotaResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCertWarehouseQuota',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.GetCertWarehouseQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cert_warehouse_quota(self) -> cas_20200407_models.GetCertWarehouseQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cert_warehouse_quota_with_options(runtime)

    async def get_cert_warehouse_quota_async(self) -> cas_20200407_models.GetCertWarehouseQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cert_warehouse_quota_with_options_async(runtime)

    def get_user_certificate_detail_with_options(
        self,
        request: cas_20200407_models.GetUserCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetUserCertificateDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserCertificateDetail',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.GetUserCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_certificate_detail_with_options_async(
        self,
        request: cas_20200407_models.GetUserCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetUserCertificateDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserCertificateDetail',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.GetUserCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_certificate_detail(
        self,
        request: cas_20200407_models.GetUserCertificateDetailRequest,
    ) -> cas_20200407_models.GetUserCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_certificate_detail_with_options(request, runtime)

    async def get_user_certificate_detail_async(
        self,
        request: cas_20200407_models.GetUserCertificateDetailRequest,
    ) -> cas_20200407_models.GetUserCertificateDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_certificate_detail_with_options_async(request, runtime)

    def list_cert_with_options(
        self,
        request: cas_20200407_models.ListCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCert',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.ListCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cert_with_options_async(
        self,
        request: cas_20200407_models.ListCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCert',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.ListCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cert(
        self,
        request: cas_20200407_models.ListCertRequest,
    ) -> cas_20200407_models.ListCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cert_with_options(request, runtime)

    async def list_cert_async(
        self,
        request: cas_20200407_models.ListCertRequest,
    ) -> cas_20200407_models.ListCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cert_with_options_async(request, runtime)

    def list_cert_warehouse_with_options(
        self,
        request: cas_20200407_models.ListCertWarehouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCertWarehouseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCertWarehouse',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.ListCertWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cert_warehouse_with_options_async(
        self,
        request: cas_20200407_models.ListCertWarehouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCertWarehouseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCertWarehouse',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.ListCertWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cert_warehouse(
        self,
        request: cas_20200407_models.ListCertWarehouseRequest,
    ) -> cas_20200407_models.ListCertWarehouseResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cert_warehouse_with_options(request, runtime)

    async def list_cert_warehouse_async(
        self,
        request: cas_20200407_models.ListCertWarehouseRequest,
    ) -> cas_20200407_models.ListCertWarehouseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cert_warehouse_with_options_async(request, runtime)

    def list_user_certificate_order_with_options(
        self,
        request: cas_20200407_models.ListUserCertificateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListUserCertificateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserCertificateOrder',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.ListUserCertificateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_certificate_order_with_options_async(
        self,
        request: cas_20200407_models.ListUserCertificateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListUserCertificateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserCertificateOrder',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.ListUserCertificateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_certificate_order(
        self,
        request: cas_20200407_models.ListUserCertificateOrderRequest,
    ) -> cas_20200407_models.ListUserCertificateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_certificate_order_with_options(request, runtime)

    async def list_user_certificate_order_async(
        self,
        request: cas_20200407_models.ListUserCertificateOrderRequest,
    ) -> cas_20200407_models.ListUserCertificateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_certificate_order_with_options_async(request, runtime)

    def renew_certificate_order_for_package_request_with_options(
        self,
        request: cas_20200407_models.RenewCertificateOrderForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.RenewCertificateOrderForPackageRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewCertificateOrderForPackageRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.RenewCertificateOrderForPackageRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_certificate_order_for_package_request_with_options_async(
        self,
        request: cas_20200407_models.RenewCertificateOrderForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.RenewCertificateOrderForPackageRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewCertificateOrderForPackageRequest',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.RenewCertificateOrderForPackageRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_certificate_order_for_package_request(
        self,
        request: cas_20200407_models.RenewCertificateOrderForPackageRequestRequest,
    ) -> cas_20200407_models.RenewCertificateOrderForPackageRequestResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_certificate_order_for_package_request_with_options(request, runtime)

    async def renew_certificate_order_for_package_request_async(
        self,
        request: cas_20200407_models.RenewCertificateOrderForPackageRequestRequest,
    ) -> cas_20200407_models.RenewCertificateOrderForPackageRequestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_certificate_order_for_package_request_with_options_async(request, runtime)

    def revoke_whclient_certificate_with_options(
        self,
        request: cas_20200407_models.RevokeWHClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.RevokeWHClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeWHClientCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.RevokeWHClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_whclient_certificate_with_options_async(
        self,
        request: cas_20200407_models.RevokeWHClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.RevokeWHClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevokeWHClientCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.RevokeWHClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_whclient_certificate(
        self,
        request: cas_20200407_models.RevokeWHClientCertificateRequest,
    ) -> cas_20200407_models.RevokeWHClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_whclient_certificate_with_options(request, runtime)

    async def revoke_whclient_certificate_async(
        self,
        request: cas_20200407_models.RevokeWHClientCertificateRequest,
    ) -> cas_20200407_models.RevokeWHClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_whclient_certificate_with_options_async(request, runtime)

    def sign_with_options(
        self,
        request: cas_20200407_models.SignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.SignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Sign',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.SignResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_with_options_async(
        self,
        request: cas_20200407_models.SignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.SignResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Sign',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.SignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign(
        self,
        request: cas_20200407_models.SignRequest,
    ) -> cas_20200407_models.SignResponse:
        runtime = util_models.RuntimeOptions()
        return self.sign_with_options(request, runtime)

    async def sign_async(
        self,
        request: cas_20200407_models.SignRequest,
    ) -> cas_20200407_models.SignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sign_with_options_async(request, runtime)

    def upload_pcacert_with_options(
        self,
        request: cas_20200407_models.UploadPCACertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadPCACertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPCACert',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.UploadPCACertResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_pcacert_with_options_async(
        self,
        request: cas_20200407_models.UploadPCACertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadPCACertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPCACert',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.UploadPCACertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_pcacert(
        self,
        request: cas_20200407_models.UploadPCACertRequest,
    ) -> cas_20200407_models.UploadPCACertResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_pcacert_with_options(request, runtime)

    async def upload_pcacert_async(
        self,
        request: cas_20200407_models.UploadPCACertRequest,
    ) -> cas_20200407_models.UploadPCACertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_pcacert_with_options_async(request, runtime)

    def upload_user_certificate_with_options(
        self,
        request: cas_20200407_models.UploadUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadUserCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.encrypt_cert):
            query['EncryptCert'] = request.encrypt_cert
        if not UtilClient.is_unset(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.sign_cert):
            query['SignCert'] = request.sign_cert
        if not UtilClient.is_unset(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadUserCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.UploadUserCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_user_certificate_with_options_async(
        self,
        request: cas_20200407_models.UploadUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadUserCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert):
            query['Cert'] = request.cert
        if not UtilClient.is_unset(request.encrypt_cert):
            query['EncryptCert'] = request.encrypt_cert
        if not UtilClient.is_unset(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.sign_cert):
            query['SignCert'] = request.sign_cert
        if not UtilClient.is_unset(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadUserCertificate',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.UploadUserCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_user_certificate(
        self,
        request: cas_20200407_models.UploadUserCertificateRequest,
    ) -> cas_20200407_models.UploadUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_user_certificate_with_options(request, runtime)

    async def upload_user_certificate_async(
        self,
        request: cas_20200407_models.UploadUserCertificateRequest,
    ) -> cas_20200407_models.UploadUserCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_user_certificate_with_options_async(request, runtime)

    def verify_with_options(
        self,
        request: cas_20200407_models.VerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.VerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.signature_value):
            query['SignatureValue'] = request.signature_value
        if not UtilClient.is_unset(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Verify',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.VerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_with_options_async(
        self,
        request: cas_20200407_models.VerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.VerifyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.message_type):
            query['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.signature_value):
            query['SignatureValue'] = request.signature_value
        if not UtilClient.is_unset(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Verify',
            version='2020-04-07',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200407_models.VerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify(
        self,
        request: cas_20200407_models.VerifyRequest,
    ) -> cas_20200407_models.VerifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_with_options(request, runtime)

    async def verify_async(
        self,
        request: cas_20200407_models.VerifyRequest,
    ) -> cas_20200407_models.VerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_with_options_async(request, runtime)
