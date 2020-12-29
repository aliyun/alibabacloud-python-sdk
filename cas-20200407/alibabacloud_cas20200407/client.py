# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cas20200407 import models as cas_20200407_models
from alibabacloud_tea_util import models as util_models


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

    def create_certificate_request_with_options(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.CreateCertificateRequestResponse().from_map(
            self.do_rpcrequest('CreateCertificateRequest', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_certificate_request_with_options_async(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.CreateCertificateRequestResponse().from_map(
            await self.do_rpcrequest_async('CreateCertificateRequest', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.CreateCertificateWithCsrRequestResponse().from_map(
            self.do_rpcrequest('CreateCertificateWithCsrRequest', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_certificate_with_csr_request_with_options_async(
        self,
        request: cas_20200407_models.CreateCertificateWithCsrRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateWithCsrRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.CreateCertificateWithCsrRequestResponse().from_map(
            await self.do_rpcrequest_async('CreateCertificateWithCsrRequest', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.DeleteCertificateRequestResponse().from_map(
            self.do_rpcrequest('DeleteCertificateRequest', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_certificate_request_with_options_async(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.DeleteCertificateRequestResponse().from_map(
            await self.do_rpcrequest_async('DeleteCertificateRequest', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.DescribeCertificateStateResponse().from_map(
            self.do_rpcrequest('DescribeCertificateState', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_certificate_state_with_options_async(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.DescribeCertificateStateResponse().from_map(
            await self.do_rpcrequest_async('DescribeCertificateState', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.DescribePackageStateResponse().from_map(
            self.do_rpcrequest('DescribePackageState', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_package_state_with_options_async(
        self,
        request: cas_20200407_models.DescribePackageStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribePackageStateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return cas_20200407_models.DescribePackageStateResponse().from_map(
            await self.do_rpcrequest_async('DescribePackageState', '2020-04-07', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
