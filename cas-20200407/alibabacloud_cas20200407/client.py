# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cas20200407 import models as main_models
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

    def cancel_certificate_for_package_request_with_options(
        self,
        request: main_models.CancelCertificateForPackageRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCertificateForPackageRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCertificateForPackageRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCertificateForPackageRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_certificate_for_package_request_with_options_async(
        self,
        request: main_models.CancelCertificateForPackageRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCertificateForPackageRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCertificateForPackageRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCertificateForPackageRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_certificate_for_package_request(
        self,
        request: main_models.CancelCertificateForPackageRequestRequest,
    ) -> main_models.CancelCertificateForPackageRequestResponse:
        runtime = RuntimeOptions()
        return self.cancel_certificate_for_package_request_with_options(request, runtime)

    async def cancel_certificate_for_package_request_async(
        self,
        request: main_models.CancelCertificateForPackageRequestRequest,
    ) -> main_models.CancelCertificateForPackageRequestResponse:
        runtime = RuntimeOptions()
        return await self.cancel_certificate_for_package_request_with_options_async(request, runtime)

    def cancel_order_request_with_options(
        self,
        request: main_models.CancelOrderRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOrderRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_request_with_options_async(
        self,
        request: main_models.CancelOrderRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOrderRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order_request(
        self,
        request: main_models.CancelOrderRequestRequest,
    ) -> main_models.CancelOrderRequestResponse:
        runtime = RuntimeOptions()
        return self.cancel_order_request_with_options(request, runtime)

    async def cancel_order_request_async(
        self,
        request: main_models.CancelOrderRequestRequest,
    ) -> main_models.CancelOrderRequestResponse:
        runtime = RuntimeOptions()
        return await self.cancel_order_request_with_options_async(request, runtime)

    def create_certificate_for_package_request_with_options(
        self,
        request: main_models.CreateCertificateForPackageRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertificateForPackageRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCertificateForPackageRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertificateForPackageRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_for_package_request_with_options_async(
        self,
        request: main_models.CreateCertificateForPackageRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertificateForPackageRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_name):
            query['CompanyName'] = request.company_name
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCertificateForPackageRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertificateForPackageRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_for_package_request(
        self,
        request: main_models.CreateCertificateForPackageRequestRequest,
    ) -> main_models.CreateCertificateForPackageRequestResponse:
        runtime = RuntimeOptions()
        return self.create_certificate_for_package_request_with_options(request, runtime)

    async def create_certificate_for_package_request_async(
        self,
        request: main_models.CreateCertificateForPackageRequestRequest,
    ) -> main_models.CreateCertificateForPackageRequestResponse:
        runtime = RuntimeOptions()
        return await self.create_certificate_for_package_request_with_options_async(request, runtime)

    def create_certificate_request_with_options(
        self,
        request: main_models.CreateCertificateRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertificateRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCertificateRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertificateRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_request_with_options_async(
        self,
        request: main_models.CreateCertificateRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertificateRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCertificateRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertificateRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_request(
        self,
        request: main_models.CreateCertificateRequestRequest,
    ) -> main_models.CreateCertificateRequestResponse:
        runtime = RuntimeOptions()
        return self.create_certificate_request_with_options(request, runtime)

    async def create_certificate_request_async(
        self,
        request: main_models.CreateCertificateRequestRequest,
    ) -> main_models.CreateCertificateRequestResponse:
        runtime = RuntimeOptions()
        return await self.create_certificate_request_with_options_async(request, runtime)

    def create_certificate_with_csr_request_with_options(
        self,
        request: main_models.CreateCertificateWithCsrRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertificateWithCsrRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCertificateWithCsrRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertificateWithCsrRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_with_csr_request_with_options_async(
        self,
        request: main_models.CreateCertificateWithCsrRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCertificateWithCsrRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        if not DaraCore.is_null(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCertificateWithCsrRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCertificateWithCsrRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_with_csr_request(
        self,
        request: main_models.CreateCertificateWithCsrRequestRequest,
    ) -> main_models.CreateCertificateWithCsrRequestResponse:
        runtime = RuntimeOptions()
        return self.create_certificate_with_csr_request_with_options(request, runtime)

    async def create_certificate_with_csr_request_async(
        self,
        request: main_models.CreateCertificateWithCsrRequestRequest,
    ) -> main_models.CreateCertificateWithCsrRequestResponse:
        runtime = RuntimeOptions()
        return await self.create_certificate_with_csr_request_with_options_async(request, runtime)

    def create_csr_with_options(
        self,
        request: main_models.CreateCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.key_size):
            query['KeySize'] = request.key_size
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.sans):
            query['Sans'] = request.sans
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_csr_with_options_async(
        self,
        request: main_models.CreateCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.common_name):
            query['CommonName'] = request.common_name
        if not DaraCore.is_null(request.corp_name):
            query['CorpName'] = request.corp_name
        if not DaraCore.is_null(request.country_code):
            query['CountryCode'] = request.country_code
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.key_size):
            query['KeySize'] = request.key_size
        if not DaraCore.is_null(request.locality):
            query['Locality'] = request.locality
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.province):
            query['Province'] = request.province
        if not DaraCore.is_null(request.sans):
            query['Sans'] = request.sans
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_csr(
        self,
        request: main_models.CreateCsrRequest,
    ) -> main_models.CreateCsrResponse:
        runtime = RuntimeOptions()
        return self.create_csr_with_options(request, runtime)

    async def create_csr_async(
        self,
        request: main_models.CreateCsrRequest,
    ) -> main_models.CreateCsrResponse:
        runtime = RuntimeOptions()
        return await self.create_csr_with_options_async(request, runtime)

    def create_deployment_job_with_options(
        self,
        request: main_models.CreateDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_job_with_options_async(
        self,
        request: main_models.CreateDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_job(
        self,
        request: main_models.CreateDeploymentJobRequest,
    ) -> main_models.CreateDeploymentJobResponse:
        runtime = RuntimeOptions()
        return self.create_deployment_job_with_options(request, runtime)

    async def create_deployment_job_async(
        self,
        request: main_models.CreateDeploymentJobRequest,
    ) -> main_models.CreateDeploymentJobResponse:
        runtime = RuntimeOptions()
        return await self.create_deployment_job_with_options_async(request, runtime)

    def decrypt_with_options(
        self,
        request: main_models.DecryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Decrypt',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrypt_with_options_async(
        self,
        request: main_models.DecryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.ciphertext_blob):
            query['CiphertextBlob'] = request.ciphertext_blob
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Decrypt',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrypt(
        self,
        request: main_models.DecryptRequest,
    ) -> main_models.DecryptResponse:
        runtime = RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    async def decrypt_async(
        self,
        request: main_models.DecryptRequest,
    ) -> main_models.DecryptResponse:
        runtime = RuntimeOptions()
        return await self.decrypt_with_options_async(request, runtime)

    def delete_certificate_request_with_options(
        self,
        request: main_models.DeleteCertificateRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCertificateRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCertificateRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCertificateRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_certificate_request_with_options_async(
        self,
        request: main_models.DeleteCertificateRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCertificateRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCertificateRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCertificateRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_certificate_request(
        self,
        request: main_models.DeleteCertificateRequestRequest,
    ) -> main_models.DeleteCertificateRequestResponse:
        runtime = RuntimeOptions()
        return self.delete_certificate_request_with_options(request, runtime)

    async def delete_certificate_request_async(
        self,
        request: main_models.DeleteCertificateRequestRequest,
    ) -> main_models.DeleteCertificateRequestResponse:
        runtime = RuntimeOptions()
        return await self.delete_certificate_request_with_options_async(request, runtime)

    def delete_csr_with_options(
        self,
        request: main_models.DeleteCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_csr_with_options_async(
        self,
        request: main_models.DeleteCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_csr(
        self,
        request: main_models.DeleteCsrRequest,
    ) -> main_models.DeleteCsrResponse:
        runtime = RuntimeOptions()
        return self.delete_csr_with_options(request, runtime)

    async def delete_csr_async(
        self,
        request: main_models.DeleteCsrRequest,
    ) -> main_models.DeleteCsrResponse:
        runtime = RuntimeOptions()
        return await self.delete_csr_with_options_async(request, runtime)

    def delete_deployment_job_with_options(
        self,
        request: main_models.DeleteDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_job_with_options_async(
        self,
        request: main_models.DeleteDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment_job(
        self,
        request: main_models.DeleteDeploymentJobRequest,
    ) -> main_models.DeleteDeploymentJobResponse:
        runtime = RuntimeOptions()
        return self.delete_deployment_job_with_options(request, runtime)

    async def delete_deployment_job_async(
        self,
        request: main_models.DeleteDeploymentJobRequest,
    ) -> main_models.DeleteDeploymentJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_deployment_job_with_options_async(request, runtime)

    def delete_pcacert_with_options(
        self,
        request: main_models.DeletePCACertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePCACertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePCACert',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePCACertResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pcacert_with_options_async(
        self,
        request: main_models.DeletePCACertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePCACertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePCACert',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePCACertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pcacert(
        self,
        request: main_models.DeletePCACertRequest,
    ) -> main_models.DeletePCACertResponse:
        runtime = RuntimeOptions()
        return self.delete_pcacert_with_options(request, runtime)

    async def delete_pcacert_async(
        self,
        request: main_models.DeletePCACertRequest,
    ) -> main_models.DeletePCACertResponse:
        runtime = RuntimeOptions()
        return await self.delete_pcacert_with_options_async(request, runtime)

    def delete_user_certificate_with_options(
        self,
        request: main_models.DeleteUserCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserCertificate',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_certificate_with_options_async(
        self,
        request: main_models.DeleteUserCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserCertificate',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_certificate(
        self,
        request: main_models.DeleteUserCertificateRequest,
    ) -> main_models.DeleteUserCertificateResponse:
        runtime = RuntimeOptions()
        return self.delete_user_certificate_with_options(request, runtime)

    async def delete_user_certificate_async(
        self,
        request: main_models.DeleteUserCertificateRequest,
    ) -> main_models.DeleteUserCertificateResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_certificate_with_options_async(request, runtime)

    def delete_worker_resource_with_options(
        self,
        request: main_models.DeleteWorkerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkerResource',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_worker_resource_with_options_async(
        self,
        request: main_models.DeleteWorkerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWorkerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWorkerResource',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWorkerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_worker_resource(
        self,
        request: main_models.DeleteWorkerResourceRequest,
    ) -> main_models.DeleteWorkerResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_worker_resource_with_options(request, runtime)

    async def delete_worker_resource_async(
        self,
        request: main_models.DeleteWorkerResourceRequest,
    ) -> main_models.DeleteWorkerResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_worker_resource_with_options_async(request, runtime)

    def describe_certificate_state_with_options(
        self,
        request: main_models.DescribeCertificateStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertificateStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertificateState',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertificateStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificate_state_with_options_async(
        self,
        request: main_models.DescribeCertificateStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCertificateStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCertificateState',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCertificateStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificate_state(
        self,
        request: main_models.DescribeCertificateStateRequest,
    ) -> main_models.DescribeCertificateStateResponse:
        runtime = RuntimeOptions()
        return self.describe_certificate_state_with_options(request, runtime)

    async def describe_certificate_state_async(
        self,
        request: main_models.DescribeCertificateStateRequest,
    ) -> main_models.DescribeCertificateStateResponse:
        runtime = RuntimeOptions()
        return await self.describe_certificate_state_with_options_async(request, runtime)

    def describe_cloud_resource_status_with_options(
        self,
        request: main_models.DescribeCloudResourceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResourceStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_resource_status_with_options_async(
        self,
        request: main_models.DescribeCloudResourceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCloudResourceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCloudResourceStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCloudResourceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_resource_status(
        self,
        request: main_models.DescribeCloudResourceStatusRequest,
    ) -> main_models.DescribeCloudResourceStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_cloud_resource_status_with_options(request, runtime)

    async def describe_cloud_resource_status_async(
        self,
        request: main_models.DescribeCloudResourceStatusRequest,
    ) -> main_models.DescribeCloudResourceStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_cloud_resource_status_with_options_async(request, runtime)

    def describe_deployment_job_with_options(
        self,
        request: main_models.DescribeDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployment_job_with_options_async(
        self,
        request: main_models.DescribeDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployment_job(
        self,
        request: main_models.DescribeDeploymentJobRequest,
    ) -> main_models.DescribeDeploymentJobResponse:
        runtime = RuntimeOptions()
        return self.describe_deployment_job_with_options(request, runtime)

    async def describe_deployment_job_async(
        self,
        request: main_models.DescribeDeploymentJobRequest,
    ) -> main_models.DescribeDeploymentJobResponse:
        runtime = RuntimeOptions()
        return await self.describe_deployment_job_with_options_async(request, runtime)

    def describe_deployment_job_status_with_options(
        self,
        request: main_models.DescribeDeploymentJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeploymentJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeploymentJobStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeploymentJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployment_job_status_with_options_async(
        self,
        request: main_models.DescribeDeploymentJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeploymentJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDeploymentJobStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeploymentJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployment_job_status(
        self,
        request: main_models.DescribeDeploymentJobStatusRequest,
    ) -> main_models.DescribeDeploymentJobStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_deployment_job_status_with_options(request, runtime)

    async def describe_deployment_job_status_async(
        self,
        request: main_models.DescribeDeploymentJobStatusRequest,
    ) -> main_models.DescribeDeploymentJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_deployment_job_status_with_options_async(request, runtime)

    def describe_package_state_with_options(
        self,
        request: main_models.DescribePackageStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackageStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackageState',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackageStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_package_state_with_options_async(
        self,
        request: main_models.DescribePackageStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePackageStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePackageState',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePackageStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_package_state(
        self,
        request: main_models.DescribePackageStateRequest,
    ) -> main_models.DescribePackageStateResponse:
        runtime = RuntimeOptions()
        return self.describe_package_state_with_options(request, runtime)

    async def describe_package_state_async(
        self,
        request: main_models.DescribePackageStateRequest,
    ) -> main_models.DescribePackageStateResponse:
        runtime = RuntimeOptions()
        return await self.describe_package_state_with_options_async(request, runtime)

    def encrypt_with_options(
        self,
        request: main_models.EncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.plaintext):
            query['Plaintext'] = request.plaintext
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Encrypt',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptResponse(),
            self.call_api(params, req, runtime)
        )

    async def encrypt_with_options_async(
        self,
        request: main_models.EncryptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncryptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.plaintext):
            query['Plaintext'] = request.plaintext
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Encrypt',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncryptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encrypt(
        self,
        request: main_models.EncryptRequest,
    ) -> main_models.EncryptResponse:
        runtime = RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    async def encrypt_async(
        self,
        request: main_models.EncryptRequest,
    ) -> main_models.EncryptResponse:
        runtime = RuntimeOptions()
        return await self.encrypt_with_options_async(request, runtime)

    def get_cert_warehouse_quota_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetCertWarehouseQuotaResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetCertWarehouseQuota',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCertWarehouseQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cert_warehouse_quota_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetCertWarehouseQuotaResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetCertWarehouseQuota',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCertWarehouseQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cert_warehouse_quota(self) -> main_models.GetCertWarehouseQuotaResponse:
        runtime = RuntimeOptions()
        return self.get_cert_warehouse_quota_with_options(runtime)

    async def get_cert_warehouse_quota_async(self) -> main_models.GetCertWarehouseQuotaResponse:
        runtime = RuntimeOptions()
        return await self.get_cert_warehouse_quota_with_options_async(runtime)

    def get_csr_detail_with_options(
        self,
        request: main_models.GetCsrDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCsrDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCsrDetail',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCsrDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_csr_detail_with_options_async(
        self,
        request: main_models.GetCsrDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCsrDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCsrDetail',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCsrDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_csr_detail(
        self,
        request: main_models.GetCsrDetailRequest,
    ) -> main_models.GetCsrDetailResponse:
        runtime = RuntimeOptions()
        return self.get_csr_detail_with_options(request, runtime)

    async def get_csr_detail_async(
        self,
        request: main_models.GetCsrDetailRequest,
    ) -> main_models.GetCsrDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_csr_detail_with_options_async(request, runtime)

    def get_user_certificate_detail_with_options(
        self,
        request: main_models.GetUserCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_filter):
            query['CertFilter'] = request.cert_filter
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserCertificateDetail',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_certificate_detail_with_options_async(
        self,
        request: main_models.GetUserCertificateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserCertificateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_filter):
            query['CertFilter'] = request.cert_filter
        if not DaraCore.is_null(request.cert_id):
            query['CertId'] = request.cert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserCertificateDetail',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserCertificateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_certificate_detail(
        self,
        request: main_models.GetUserCertificateDetailRequest,
    ) -> main_models.GetUserCertificateDetailResponse:
        runtime = RuntimeOptions()
        return self.get_user_certificate_detail_with_options(request, runtime)

    async def get_user_certificate_detail_async(
        self,
        request: main_models.GetUserCertificateDetailRequest,
    ) -> main_models.GetUserCertificateDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_user_certificate_detail_with_options_async(request, runtime)

    def list_cert_with_options(
        self,
        request: main_models.ListCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCert',
            version = '2020-04-07',
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
        if not DaraCore.is_null(request.cert_type):
            query['CertType'] = request.cert_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCert',
            version = '2020-04-07',
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

    def list_cert_warehouse_with_options(
        self,
        request: main_models.ListCertWarehouseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertWarehouseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCertWarehouse',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cert_warehouse_with_options_async(
        self,
        request: main_models.ListCertWarehouseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCertWarehouseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCertWarehouse',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCertWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cert_warehouse(
        self,
        request: main_models.ListCertWarehouseRequest,
    ) -> main_models.ListCertWarehouseResponse:
        runtime = RuntimeOptions()
        return self.list_cert_warehouse_with_options(request, runtime)

    async def list_cert_warehouse_async(
        self,
        request: main_models.ListCertWarehouseRequest,
    ) -> main_models.ListCertWarehouseResponse:
        runtime = RuntimeOptions()
        return await self.list_cert_warehouse_with_options_async(request, runtime)

    def list_cloud_access_with_options(
        self,
        request: main_models.ListCloudAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAccess',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_access_with_options_async(
        self,
        request: main_models.ListCloudAccessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudAccess',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_access(
        self,
        request: main_models.ListCloudAccessRequest,
    ) -> main_models.ListCloudAccessResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_access_with_options(request, runtime)

    async def list_cloud_access_async(
        self,
        request: main_models.ListCloudAccessRequest,
    ) -> main_models.ListCloudAccessResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_access_with_options_async(request, runtime)

    def list_cloud_resources_with_options(
        self,
        tmp_req: main_models.ListCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudResourcesResponse:
        tmp_req.validate()
        request = main_models.ListCloudResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cert_ids):
            request.cert_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.cert_ids, 'CertIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cert_ids_shrink):
            query['CertIds'] = request.cert_ids_shrink
        if not DaraCore.is_null(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not DaraCore.is_null(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudResources',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_resources_with_options_async(
        self,
        tmp_req: main_models.ListCloudResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCloudResourcesResponse:
        tmp_req.validate()
        request = main_models.ListCloudResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cert_ids):
            request.cert_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.cert_ids, 'CertIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cert_ids_shrink):
            query['CertIds'] = request.cert_ids_shrink
        if not DaraCore.is_null(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not DaraCore.is_null(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.secret_id):
            query['SecretId'] = request.secret_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCloudResources',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_resources(
        self,
        request: main_models.ListCloudResourcesRequest,
    ) -> main_models.ListCloudResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_cloud_resources_with_options(request, runtime)

    async def list_cloud_resources_async(
        self,
        request: main_models.ListCloudResourcesRequest,
    ) -> main_models.ListCloudResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_cloud_resources_with_options_async(request, runtime)

    def list_contact_with_options(
        self,
        request: main_models.ListContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContact',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contact_with_options_async(
        self,
        request: main_models.ListContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListContact',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contact(
        self,
        request: main_models.ListContactRequest,
    ) -> main_models.ListContactResponse:
        runtime = RuntimeOptions()
        return self.list_contact_with_options(request, runtime)

    async def list_contact_async(
        self,
        request: main_models.ListContactRequest,
    ) -> main_models.ListContactResponse:
        runtime = RuntimeOptions()
        return await self.list_contact_with_options_async(request, runtime)

    def list_csr_with_options(
        self,
        request: main_models.ListCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_csr_with_options_async(
        self,
        request: main_models.ListCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_csr(
        self,
        request: main_models.ListCsrRequest,
    ) -> main_models.ListCsrResponse:
        runtime = RuntimeOptions()
        return self.list_csr_with_options(request, runtime)

    async def list_csr_async(
        self,
        request: main_models.ListCsrRequest,
    ) -> main_models.ListCsrResponse:
        runtime = RuntimeOptions()
        return await self.list_csr_with_options_async(request, runtime)

    def list_deployment_job_with_options(
        self,
        request: main_models.ListDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_job_with_options_async(
        self,
        request: main_models.ListDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_type):
            query['JobType'] = request.job_type
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_job(
        self,
        request: main_models.ListDeploymentJobRequest,
    ) -> main_models.ListDeploymentJobResponse:
        runtime = RuntimeOptions()
        return self.list_deployment_job_with_options(request, runtime)

    async def list_deployment_job_async(
        self,
        request: main_models.ListDeploymentJobRequest,
    ) -> main_models.ListDeploymentJobResponse:
        runtime = RuntimeOptions()
        return await self.list_deployment_job_with_options_async(request, runtime)

    def list_deployment_job_cert_with_options(
        self,
        request: main_models.ListDeploymentJobCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentJobCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentJobCert',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentJobCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_job_cert_with_options_async(
        self,
        request: main_models.ListDeploymentJobCertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentJobCertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentJobCert',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentJobCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_job_cert(
        self,
        request: main_models.ListDeploymentJobCertRequest,
    ) -> main_models.ListDeploymentJobCertResponse:
        runtime = RuntimeOptions()
        return self.list_deployment_job_cert_with_options(request, runtime)

    async def list_deployment_job_cert_async(
        self,
        request: main_models.ListDeploymentJobCertRequest,
    ) -> main_models.ListDeploymentJobCertResponse:
        runtime = RuntimeOptions()
        return await self.list_deployment_job_cert_with_options_async(request, runtime)

    def list_deployment_job_resource_with_options(
        self,
        request: main_models.ListDeploymentJobResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentJobResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentJobResource',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentJobResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_job_resource_with_options_async(
        self,
        request: main_models.ListDeploymentJobResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentJobResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeploymentJobResource',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentJobResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_job_resource(
        self,
        request: main_models.ListDeploymentJobResourceRequest,
    ) -> main_models.ListDeploymentJobResourceResponse:
        runtime = RuntimeOptions()
        return self.list_deployment_job_resource_with_options(request, runtime)

    async def list_deployment_job_resource_async(
        self,
        request: main_models.ListDeploymentJobResourceRequest,
    ) -> main_models.ListDeploymentJobResourceResponse:
        runtime = RuntimeOptions()
        return await self.list_deployment_job_resource_with_options_async(request, runtime)

    def list_user_certificate_order_with_options(
        self,
        request: main_models.ListUserCertificateOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserCertificateOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserCertificateOrder',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserCertificateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_certificate_order_with_options_async(
        self,
        request: main_models.ListUserCertificateOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserCertificateOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserCertificateOrder',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserCertificateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_certificate_order(
        self,
        request: main_models.ListUserCertificateOrderRequest,
    ) -> main_models.ListUserCertificateOrderResponse:
        runtime = RuntimeOptions()
        return self.list_user_certificate_order_with_options(request, runtime)

    async def list_user_certificate_order_async(
        self,
        request: main_models.ListUserCertificateOrderRequest,
    ) -> main_models.ListUserCertificateOrderResponse:
        runtime = RuntimeOptions()
        return await self.list_user_certificate_order_with_options_async(request, runtime)

    def list_worker_resource_with_options(
        self,
        request: main_models.ListWorkerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkerResource',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_worker_resource_with_options_async(
        self,
        request: main_models.ListWorkerResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWorkerResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.show_size):
            query['ShowSize'] = request.show_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWorkerResource',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWorkerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_worker_resource(
        self,
        request: main_models.ListWorkerResourceRequest,
    ) -> main_models.ListWorkerResourceResponse:
        runtime = RuntimeOptions()
        return self.list_worker_resource_with_options(request, runtime)

    async def list_worker_resource_async(
        self,
        request: main_models.ListWorkerResourceRequest,
    ) -> main_models.ListWorkerResourceResponse:
        runtime = RuntimeOptions()
        return await self.list_worker_resource_with_options_async(request, runtime)

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
            version = '2020-04-07',
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
            version = '2020-04-07',
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

    def renew_certificate_order_for_package_request_with_options(
        self,
        request: main_models.RenewCertificateOrderForPackageRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewCertificateOrderForPackageRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewCertificateOrderForPackageRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewCertificateOrderForPackageRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_certificate_order_for_package_request_with_options_async(
        self,
        request: main_models.RenewCertificateOrderForPackageRequestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewCertificateOrderForPackageRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewCertificateOrderForPackageRequest',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewCertificateOrderForPackageRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_certificate_order_for_package_request(
        self,
        request: main_models.RenewCertificateOrderForPackageRequestRequest,
    ) -> main_models.RenewCertificateOrderForPackageRequestResponse:
        runtime = RuntimeOptions()
        return self.renew_certificate_order_for_package_request_with_options(request, runtime)

    async def renew_certificate_order_for_package_request_async(
        self,
        request: main_models.RenewCertificateOrderForPackageRequestRequest,
    ) -> main_models.RenewCertificateOrderForPackageRequestResponse:
        runtime = RuntimeOptions()
        return await self.renew_certificate_order_for_package_request_with_options_async(request, runtime)

    def sign_with_options(
        self,
        request: main_models.SignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Sign',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignResponse(),
            self.call_api(params, req, runtime)
        )

    async def sign_with_options_async(
        self,
        request: main_models.SignRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Sign',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sign(
        self,
        request: main_models.SignRequest,
    ) -> main_models.SignResponse:
        runtime = RuntimeOptions()
        return self.sign_with_options(request, runtime)

    async def sign_async(
        self,
        request: main_models.SignRequest,
    ) -> main_models.SignResponse:
        runtime = RuntimeOptions()
        return await self.sign_with_options_async(request, runtime)

    def update_csr_with_options(
        self,
        request: main_models.UpdateCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr_id):
            query['CsrId'] = request.csr_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_csr_with_options_async(
        self,
        request: main_models.UpdateCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr_id):
            query['CsrId'] = request.csr_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_csr(
        self,
        request: main_models.UpdateCsrRequest,
    ) -> main_models.UpdateCsrResponse:
        runtime = RuntimeOptions()
        return self.update_csr_with_options(request, runtime)

    async def update_csr_async(
        self,
        request: main_models.UpdateCsrRequest,
    ) -> main_models.UpdateCsrResponse:
        runtime = RuntimeOptions()
        return await self.update_csr_with_options_async(request, runtime)

    def update_deployment_job_with_options(
        self,
        request: main_models.UpdateDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_job_with_options_async(
        self,
        request: main_models.UpdateDeploymentJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentJob',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_job(
        self,
        request: main_models.UpdateDeploymentJobRequest,
    ) -> main_models.UpdateDeploymentJobResponse:
        runtime = RuntimeOptions()
        return self.update_deployment_job_with_options(request, runtime)

    async def update_deployment_job_async(
        self,
        request: main_models.UpdateDeploymentJobRequest,
    ) -> main_models.UpdateDeploymentJobResponse:
        runtime = RuntimeOptions()
        return await self.update_deployment_job_with_options_async(request, runtime)

    def update_deployment_job_status_with_options(
        self,
        request: main_models.UpdateDeploymentJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentJobStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_job_status_with_options_async(
        self,
        request: main_models.UpdateDeploymentJobStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeploymentJobStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeploymentJobStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeploymentJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_job_status(
        self,
        request: main_models.UpdateDeploymentJobStatusRequest,
    ) -> main_models.UpdateDeploymentJobStatusResponse:
        runtime = RuntimeOptions()
        return self.update_deployment_job_status_with_options(request, runtime)

    async def update_deployment_job_status_async(
        self,
        request: main_models.UpdateDeploymentJobStatusRequest,
    ) -> main_models.UpdateDeploymentJobStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_deployment_job_status_with_options_async(request, runtime)

    def update_worker_resource_status_with_options(
        self,
        request: main_models.UpdateWorkerResourceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkerResourceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkerResourceStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkerResourceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_worker_resource_status_with_options_async(
        self,
        request: main_models.UpdateWorkerResourceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWorkerResourceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWorkerResourceStatus',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWorkerResourceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_worker_resource_status(
        self,
        request: main_models.UpdateWorkerResourceStatusRequest,
    ) -> main_models.UpdateWorkerResourceStatusResponse:
        runtime = RuntimeOptions()
        return self.update_worker_resource_status_with_options(request, runtime)

    async def update_worker_resource_status_async(
        self,
        request: main_models.UpdateWorkerResourceStatusRequest,
    ) -> main_models.UpdateWorkerResourceStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_worker_resource_status_with_options_async(request, runtime)

    def upload_csr_with_options(
        self,
        request: main_models.UploadCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_csr_with_options_async(
        self,
        request: main_models.UploadCsrRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadCsrResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.csr):
            query['Csr'] = request.csr
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadCsr',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_csr(
        self,
        request: main_models.UploadCsrRequest,
    ) -> main_models.UploadCsrResponse:
        runtime = RuntimeOptions()
        return self.upload_csr_with_options(request, runtime)

    async def upload_csr_async(
        self,
        request: main_models.UploadCsrRequest,
    ) -> main_models.UploadCsrResponse:
        runtime = RuntimeOptions()
        return await self.upload_csr_with_options_async(request, runtime)

    def upload_user_certificate_with_options(
        self,
        request: main_models.UploadUserCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadUserCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert):
            query['Cert'] = request.cert
        if not DaraCore.is_null(request.encrypt_cert):
            query['EncryptCert'] = request.encrypt_cert
        if not DaraCore.is_null(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sign_cert):
            query['SignCert'] = request.sign_cert
        if not DaraCore.is_null(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadUserCertificate',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadUserCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_user_certificate_with_options_async(
        self,
        request: main_models.UploadUserCertificateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadUserCertificateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert):
            query['Cert'] = request.cert
        if not DaraCore.is_null(request.encrypt_cert):
            query['EncryptCert'] = request.encrypt_cert
        if not DaraCore.is_null(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sign_cert):
            query['SignCert'] = request.sign_cert
        if not DaraCore.is_null(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadUserCertificate',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadUserCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_user_certificate(
        self,
        request: main_models.UploadUserCertificateRequest,
    ) -> main_models.UploadUserCertificateResponse:
        runtime = RuntimeOptions()
        return self.upload_user_certificate_with_options(request, runtime)

    async def upload_user_certificate_async(
        self,
        request: main_models.UploadUserCertificateRequest,
    ) -> main_models.UploadUserCertificateResponse:
        runtime = RuntimeOptions()
        return await self.upload_user_certificate_with_options_async(request, runtime)

    def verify_with_options(
        self,
        request: main_models.VerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.signature_value):
            query['SignatureValue'] = request.signature_value
        if not DaraCore.is_null(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Verify',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_with_options_async(
        self,
        request: main_models.VerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not DaraCore.is_null(request.custom_identifier):
            query['CustomIdentifier'] = request.custom_identifier
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.signature_value):
            query['SignatureValue'] = request.signature_value
        if not DaraCore.is_null(request.signing_algorithm):
            query['SigningAlgorithm'] = request.signing_algorithm
        if not DaraCore.is_null(request.warehouse_id):
            query['WarehouseId'] = request.warehouse_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Verify',
            version = '2020-04-07',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify(
        self,
        request: main_models.VerifyRequest,
    ) -> main_models.VerifyResponse:
        runtime = RuntimeOptions()
        return self.verify_with_options(request, runtime)

    async def verify_async(
        self,
        request: main_models.VerifyRequest,
    ) -> main_models.VerifyResponse:
        runtime = RuntimeOptions()
        return await self.verify_with_options_async(request, runtime)
