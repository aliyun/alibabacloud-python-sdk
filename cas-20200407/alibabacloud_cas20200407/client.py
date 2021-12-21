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
        query['CompanyName'] = request.company_name
        query['Csr'] = request.csr
        query['Domain'] = request.domain
        query['Email'] = request.email
        query['Phone'] = request.phone
        query['ProductCode'] = request.product_code
        query['Username'] = request.username
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
        query['CompanyName'] = request.company_name
        query['Csr'] = request.csr
        query['Domain'] = request.domain
        query['Email'] = request.email
        query['Phone'] = request.phone
        query['ProductCode'] = request.product_code
        query['Username'] = request.username
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
        query['Domain'] = request.domain
        query['Email'] = request.email
        query['Phone'] = request.phone
        query['ProductCode'] = request.product_code
        query['Username'] = request.username
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
        query['Domain'] = request.domain
        query['Email'] = request.email
        query['Phone'] = request.phone
        query['ProductCode'] = request.product_code
        query['Username'] = request.username
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
        query['Csr'] = request.csr
        query['Email'] = request.email
        query['Phone'] = request.phone
        query['ProductCode'] = request.product_code
        query['Username'] = request.username
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
        query['Csr'] = request.csr
        query['Email'] = request.email
        query['Phone'] = request.phone
        query['ProductCode'] = request.product_code
        query['Username'] = request.username
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

    def delete_certificate_request_with_options(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        UtilClient.validate_model(request)
        query = {}
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

    def describe_certificate_state_with_options(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        UtilClient.validate_model(request)
        query = {}
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

    def renew_certificate_order_for_package_request_with_options(
        self,
        request: cas_20200407_models.RenewCertificateOrderForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.RenewCertificateOrderForPackageRequestResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Csr'] = request.csr
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
        query['Csr'] = request.csr
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
