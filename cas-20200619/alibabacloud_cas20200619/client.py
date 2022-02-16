# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cas20200619 import models as cas_20200619_models
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

    def create_sslcertificate_with_options(
        self,
        request: cas_20200619_models.CreateSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.CreateSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSSLCertificate',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.CreateSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sslcertificate_with_options_async(
        self,
        request: cas_20200619_models.CreateSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.CreateSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSSLCertificate',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.CreateSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sslcertificate(
        self,
        request: cas_20200619_models.CreateSSLCertificateRequest,
    ) -> cas_20200619_models.CreateSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sslcertificate_with_options(request, runtime)

    async def create_sslcertificate_async(
        self,
        request: cas_20200619_models.CreateSSLCertificateRequest,
    ) -> cas_20200619_models.CreateSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sslcertificate_with_options_async(request, runtime)

    def create_sslcertificate_with_name_with_options(
        self,
        request: cas_20200619_models.CreateSSLCertificateWithNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.CreateSSLCertificateWithNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSSLCertificateWithName',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.CreateSSLCertificateWithNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sslcertificate_with_name_with_options_async(
        self,
        request: cas_20200619_models.CreateSSLCertificateWithNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.CreateSSLCertificateWithNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSSLCertificateWithName',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.CreateSSLCertificateWithNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sslcertificate_with_name(
        self,
        request: cas_20200619_models.CreateSSLCertificateWithNameRequest,
    ) -> cas_20200619_models.CreateSSLCertificateWithNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sslcertificate_with_name_with_options(request, runtime)

    async def create_sslcertificate_with_name_async(
        self,
        request: cas_20200619_models.CreateSSLCertificateWithNameRequest,
    ) -> cas_20200619_models.CreateSSLCertificateWithNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sslcertificate_with_name_with_options_async(request, runtime)

    def delete_sslcertificate_with_options(
        self,
        request: cas_20200619_models.DeleteSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DeleteSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSSLCertificate',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DeleteSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sslcertificate_with_options_async(
        self,
        request: cas_20200619_models.DeleteSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DeleteSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSSLCertificate',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DeleteSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sslcertificate(
        self,
        request: cas_20200619_models.DeleteSSLCertificateRequest,
    ) -> cas_20200619_models.DeleteSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sslcertificate_with_options(request, runtime)

    async def delete_sslcertificate_async(
        self,
        request: cas_20200619_models.DeleteSSLCertificateRequest,
    ) -> cas_20200619_models.DeleteSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sslcertificate_with_options_async(request, runtime)

    def describe_sslcertificate_count_with_options(
        self,
        request: cas_20200619_models.DescribeSSLCertificateCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificateCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificateCount',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificateCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sslcertificate_count_with_options_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificateCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificateCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificateCount',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificateCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sslcertificate_count(
        self,
        request: cas_20200619_models.DescribeSSLCertificateCountRequest,
    ) -> cas_20200619_models.DescribeSSLCertificateCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sslcertificate_count_with_options(request, runtime)

    async def describe_sslcertificate_count_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificateCountRequest,
    ) -> cas_20200619_models.DescribeSSLCertificateCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sslcertificate_count_with_options_async(request, runtime)

    def describe_sslcertificate_list_with_options(
        self,
        request: cas_20200619_models.DescribeSSLCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificateList',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sslcertificate_list_with_options_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.search_value):
            query['SearchValue'] = request.search_value
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificateList',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sslcertificate_list(
        self,
        request: cas_20200619_models.DescribeSSLCertificateListRequest,
    ) -> cas_20200619_models.DescribeSSLCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sslcertificate_list_with_options(request, runtime)

    async def describe_sslcertificate_list_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificateListRequest,
    ) -> cas_20200619_models.DescribeSSLCertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sslcertificate_list_with_options_async(request, runtime)

    def describe_sslcertificate_match_domain_list_with_options(
        self,
        request: cas_20200619_models.DescribeSSLCertificateMatchDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificateMatchDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificateMatchDomainList',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificateMatchDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sslcertificate_match_domain_list_with_options_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificateMatchDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificateMatchDomainListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.match_type):
            query['MatchType'] = request.match_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificateMatchDomainList',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificateMatchDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sslcertificate_match_domain_list(
        self,
        request: cas_20200619_models.DescribeSSLCertificateMatchDomainListRequest,
    ) -> cas_20200619_models.DescribeSSLCertificateMatchDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sslcertificate_match_domain_list_with_options(request, runtime)

    async def describe_sslcertificate_match_domain_list_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificateMatchDomainListRequest,
    ) -> cas_20200619_models.DescribeSSLCertificateMatchDomainListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sslcertificate_match_domain_list_with_options_async(request, runtime)

    def describe_sslcertificate_private_key_with_options(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePrivateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificatePrivateKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.encrypted_code):
            query['EncryptedCode'] = request.encrypted_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificatePrivateKey',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificatePrivateKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sslcertificate_private_key_with_options_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePrivateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificatePrivateKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        if not UtilClient.is_unset(request.encrypted_code):
            query['EncryptedCode'] = request.encrypted_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificatePrivateKey',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificatePrivateKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sslcertificate_private_key(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePrivateKeyRequest,
    ) -> cas_20200619_models.DescribeSSLCertificatePrivateKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sslcertificate_private_key_with_options(request, runtime)

    async def describe_sslcertificate_private_key_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePrivateKeyRequest,
    ) -> cas_20200619_models.DescribeSSLCertificatePrivateKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sslcertificate_private_key_with_options_async(request, runtime)

    def describe_sslcertificate_public_key_detail_with_options(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePublicKeyDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificatePublicKeyDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificatePublicKeyDetail',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificatePublicKeyDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sslcertificate_public_key_detail_with_options_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePublicKeyDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.DescribeSSLCertificatePublicKeyDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_identifier):
            query['CertIdentifier'] = request.cert_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSSLCertificatePublicKeyDetail',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.DescribeSSLCertificatePublicKeyDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sslcertificate_public_key_detail(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePublicKeyDetailRequest,
    ) -> cas_20200619_models.DescribeSSLCertificatePublicKeyDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sslcertificate_public_key_detail_with_options(request, runtime)

    async def describe_sslcertificate_public_key_detail_async(
        self,
        request: cas_20200619_models.DescribeSSLCertificatePublicKeyDetailRequest,
    ) -> cas_20200619_models.DescribeSSLCertificatePublicKeyDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sslcertificate_public_key_detail_with_options_async(request, runtime)

    def upload_sslcertificate_with_options(
        self,
        request: cas_20200619_models.UploadSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.UploadSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.encrypt_certificate):
            query['EncryptCertificate'] = request.encrypt_certificate
        if not UtilClient.is_unset(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.sign_certificate):
            query['SignCertificate'] = request.sign_certificate
        if not UtilClient.is_unset(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadSSLCertificate',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.UploadSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_sslcertificate_with_options_async(
        self,
        request: cas_20200619_models.UploadSSLCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200619_models.UploadSSLCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.encrypt_certificate):
            query['EncryptCertificate'] = request.encrypt_certificate
        if not UtilClient.is_unset(request.encrypt_private_key):
            query['EncryptPrivateKey'] = request.encrypt_private_key
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.sign_certificate):
            query['SignCertificate'] = request.sign_certificate
        if not UtilClient.is_unset(request.sign_private_key):
            query['SignPrivateKey'] = request.sign_private_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadSSLCertificate',
            version='2020-06-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200619_models.UploadSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_sslcertificate(
        self,
        request: cas_20200619_models.UploadSSLCertificateRequest,
    ) -> cas_20200619_models.UploadSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_sslcertificate_with_options(request, runtime)

    async def upload_sslcertificate_async(
        self,
        request: cas_20200619_models.UploadSSLCertificateRequest,
    ) -> cas_20200619_models.UploadSSLCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_sslcertificate_with_options_async(request, runtime)
