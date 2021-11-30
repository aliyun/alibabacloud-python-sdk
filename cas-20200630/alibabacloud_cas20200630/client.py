# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cas20200630 import models as cas_20200630_models
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

    def create_certificate_with_extension_with_options(
        self,
        request: cas_20200630_models.CreateCertificateWithExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateCertificateWithExtensionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['AlgorithmKeySize'] = request.algorithm_key_size
        query['AliasName'] = request.alias_name
        query['AppendCrl'] = request.append_crl
        query['BasicConstraintsCritical'] = request.basic_constraints_critical
        query['BeforeTime'] = request.before_time
        query['CertType'] = request.cert_type
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['CsrPemString'] = request.csr_pem_string
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['ParentIdentifier'] = request.parent_identifier
        query['Sans'] = request.sans
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCertificateWithExtension',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateCertificateWithExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_with_extension_with_options_async(
        self,
        request: cas_20200630_models.CreateCertificateWithExtensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateCertificateWithExtensionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['AlgorithmKeySize'] = request.algorithm_key_size
        query['AliasName'] = request.alias_name
        query['AppendCrl'] = request.append_crl
        query['BasicConstraintsCritical'] = request.basic_constraints_critical
        query['BeforeTime'] = request.before_time
        query['CertType'] = request.cert_type
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['CsrPemString'] = request.csr_pem_string
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['ParentIdentifier'] = request.parent_identifier
        query['Sans'] = request.sans
        query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCertificateWithExtension',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateCertificateWithExtensionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_with_extension(
        self,
        request: cas_20200630_models.CreateCertificateWithExtensionRequest,
    ) -> cas_20200630_models.CreateCertificateWithExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_extension_with_options(request, runtime)

    async def create_certificate_with_extension_async(
        self,
        request: cas_20200630_models.CreateCertificateWithExtensionRequest,
    ) -> cas_20200630_models.CreateCertificateWithExtensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_with_extension_with_options_async(request, runtime)

    def create_client_certificate_with_options(
        self,
        request: cas_20200630_models.CreateClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['Algorithm'] = request.algorithm
        query['BeforeTime'] = request.before_time
        query['CommonName'] = request.common_name
        query['Days'] = request.days
        query['ParentIdentifier'] = request.parent_identifier
        query['SanType'] = request.san_type
        query['SanValue'] = request.san_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_certificate_with_options_async(
        self,
        request: cas_20200630_models.CreateClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['Algorithm'] = request.algorithm
        query['BeforeTime'] = request.before_time
        query['CommonName'] = request.common_name
        query['Days'] = request.days
        query['ParentIdentifier'] = request.parent_identifier
        query['SanType'] = request.san_type
        query['SanValue'] = request.san_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_certificate(
        self,
        request: cas_20200630_models.CreateClientCertificateRequest,
    ) -> cas_20200630_models.CreateClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_client_certificate_with_options(request, runtime)

    async def create_client_certificate_async(
        self,
        request: cas_20200630_models.CreateClientCertificateRequest,
    ) -> cas_20200630_models.CreateClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_client_certificate_with_options_async(request, runtime)

    def create_client_certificate_with_csr_with_options(
        self,
        request: cas_20200630_models.CreateClientCertificateWithCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateClientCertificateWithCsrResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['BeforeTime'] = request.before_time
        query['Csr'] = request.csr
        query['Days'] = request.days
        query['ParentIdentifier'] = request.parent_identifier
        query['SanType'] = request.san_type
        query['SanValue'] = request.san_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClientCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateClientCertificateWithCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_client_certificate_with_csr_with_options_async(
        self,
        request: cas_20200630_models.CreateClientCertificateWithCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateClientCertificateWithCsrResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['BeforeTime'] = request.before_time
        query['Csr'] = request.csr
        query['Days'] = request.days
        query['ParentIdentifier'] = request.parent_identifier
        query['SanType'] = request.san_type
        query['SanValue'] = request.san_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClientCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateClientCertificateWithCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_client_certificate_with_csr(
        self,
        request: cas_20200630_models.CreateClientCertificateWithCsrRequest,
    ) -> cas_20200630_models.CreateClientCertificateWithCsrResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_client_certificate_with_csr_with_options(request, runtime)

    async def create_client_certificate_with_csr_async(
        self,
        request: cas_20200630_models.CreateClientCertificateWithCsrRequest,
    ) -> cas_20200630_models.CreateClientCertificateWithCsrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_client_certificate_with_csr_with_options_async(request, runtime)

    def create_revoke_client_certificate_with_options(
        self,
        request: cas_20200630_models.CreateRevokeClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateRevokeClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRevokeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateRevokeClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_revoke_client_certificate_with_options_async(
        self,
        request: cas_20200630_models.CreateRevokeClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateRevokeClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRevokeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateRevokeClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_revoke_client_certificate(
        self,
        request: cas_20200630_models.CreateRevokeClientCertificateRequest,
    ) -> cas_20200630_models.CreateRevokeClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_revoke_client_certificate_with_options(request, runtime)

    async def create_revoke_client_certificate_async(
        self,
        request: cas_20200630_models.CreateRevokeClientCertificateRequest,
    ) -> cas_20200630_models.CreateRevokeClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_revoke_client_certificate_with_options_async(request, runtime)

    def create_root_cacertificate_with_options(
        self,
        request: cas_20200630_models.CreateRootCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateRootCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Algorithm'] = request.algorithm
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['State'] = request.state
        query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRootCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateRootCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_root_cacertificate_with_options_async(
        self,
        request: cas_20200630_models.CreateRootCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateRootCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Algorithm'] = request.algorithm
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['State'] = request.state
        query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRootCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateRootCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_root_cacertificate(
        self,
        request: cas_20200630_models.CreateRootCACertificateRequest,
    ) -> cas_20200630_models.CreateRootCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_root_cacertificate_with_options(request, runtime)

    async def create_root_cacertificate_async(
        self,
        request: cas_20200630_models.CreateRootCACertificateRequest,
    ) -> cas_20200630_models.CreateRootCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_root_cacertificate_with_options_async(request, runtime)

    def create_server_certificate_with_options(
        self,
        request: cas_20200630_models.CreateServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateServerCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['Algorithm'] = request.algorithm
        query['BeforeTime'] = request.before_time
        query['CommonName'] = request.common_name
        query['Days'] = request.days
        query['Domain'] = request.domain
        query['ParentIdentifier'] = request.parent_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateServerCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_certificate_with_options_async(
        self,
        request: cas_20200630_models.CreateServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateServerCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['Algorithm'] = request.algorithm
        query['BeforeTime'] = request.before_time
        query['CommonName'] = request.common_name
        query['Days'] = request.days
        query['Domain'] = request.domain
        query['ParentIdentifier'] = request.parent_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateServerCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateServerCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_certificate(
        self,
        request: cas_20200630_models.CreateServerCertificateRequest,
    ) -> cas_20200630_models.CreateServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_server_certificate_with_options(request, runtime)

    async def create_server_certificate_async(
        self,
        request: cas_20200630_models.CreateServerCertificateRequest,
    ) -> cas_20200630_models.CreateServerCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_server_certificate_with_options_async(request, runtime)

    def create_server_certificate_with_csr_with_options(
        self,
        request: cas_20200630_models.CreateServerCertificateWithCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateServerCertificateWithCsrResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['BeforeTime'] = request.before_time
        query['Csr'] = request.csr
        query['Days'] = request.days
        query['Domain'] = request.domain
        query['ParentIdentifier'] = request.parent_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateServerCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateServerCertificateWithCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_server_certificate_with_csr_with_options_async(
        self,
        request: cas_20200630_models.CreateServerCertificateWithCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateServerCertificateWithCsrResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AfterTime'] = request.after_time
        query['BeforeTime'] = request.before_time
        query['Csr'] = request.csr
        query['Days'] = request.days
        query['Domain'] = request.domain
        query['ParentIdentifier'] = request.parent_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateServerCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateServerCertificateWithCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_server_certificate_with_csr(
        self,
        request: cas_20200630_models.CreateServerCertificateWithCsrRequest,
    ) -> cas_20200630_models.CreateServerCertificateWithCsrResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_server_certificate_with_csr_with_options(request, runtime)

    async def create_server_certificate_with_csr_async(
        self,
        request: cas_20200630_models.CreateServerCertificateWithCsrRequest,
    ) -> cas_20200630_models.CreateServerCertificateWithCsrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_server_certificate_with_csr_with_options_async(request, runtime)

    def create_sub_cacertificate_with_options(
        self,
        request: cas_20200630_models.CreateSubCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateSubCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Algorithm'] = request.algorithm
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['ParentIdentifier'] = request.parent_identifier
        query['State'] = request.state
        query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSubCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateSubCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sub_cacertificate_with_options_async(
        self,
        request: cas_20200630_models.CreateSubCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateSubCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Algorithm'] = request.algorithm
        query['CommonName'] = request.common_name
        query['CountryCode'] = request.country_code
        query['Locality'] = request.locality
        query['Organization'] = request.organization
        query['OrganizationUnit'] = request.organization_unit
        query['ParentIdentifier'] = request.parent_identifier
        query['State'] = request.state
        query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSubCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateSubCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sub_cacertificate(
        self,
        request: cas_20200630_models.CreateSubCACertificateRequest,
    ) -> cas_20200630_models.CreateSubCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_sub_cacertificate_with_options(request, runtime)

    async def create_sub_cacertificate_async(
        self,
        request: cas_20200630_models.CreateSubCACertificateRequest,
    ) -> cas_20200630_models.CreateSubCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_sub_cacertificate_with_options_async(request, runtime)

    def delete_client_certificate_with_options(
        self,
        request: cas_20200630_models.DeleteClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DeleteClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DeleteClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_certificate_with_options_async(
        self,
        request: cas_20200630_models.DeleteClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DeleteClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DeleteClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client_certificate(
        self,
        request: cas_20200630_models.DeleteClientCertificateRequest,
    ) -> cas_20200630_models.DeleteClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_client_certificate_with_options(request, runtime)

    async def delete_client_certificate_async(
        self,
        request: cas_20200630_models.DeleteClientCertificateRequest,
    ) -> cas_20200630_models.DeleteClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_client_certificate_with_options_async(request, runtime)

    def describe_cacertificate_with_options(
        self,
        request: cas_20200630_models.DescribeCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificate_with_options_async(
        self,
        request: cas_20200630_models.DescribeCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificate(
        self,
        request: cas_20200630_models.DescribeCACertificateRequest,
    ) -> cas_20200630_models.DescribeCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_with_options(request, runtime)

    async def describe_cacertificate_async(
        self,
        request: cas_20200630_models.DescribeCACertificateRequest,
    ) -> cas_20200630_models.DescribeCACertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cacertificate_with_options_async(request, runtime)

    def describe_cacertificate_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCACertificateCount',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificate_count_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateCountResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCACertificateCount',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificate_count(self) -> cas_20200630_models.DescribeCACertificateCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_count_with_options(runtime)

    async def describe_cacertificate_count_async(self) -> cas_20200630_models.DescribeCACertificateCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cacertificate_count_with_options_async(runtime)

    def describe_cacertificate_list_with_options(
        self,
        request: cas_20200630_models.DescribeCACertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCACertificateList',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cacertificate_list_with_options_async(
        self,
        request: cas_20200630_models.DescribeCACertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCACertificateList',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificate_list(
        self,
        request: cas_20200630_models.DescribeCACertificateListRequest,
    ) -> cas_20200630_models.DescribeCACertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_list_with_options(request, runtime)

    async def describe_cacertificate_list_async(
        self,
        request: cas_20200630_models.DescribeCACertificateListRequest,
    ) -> cas_20200630_models.DescribeCACertificateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cacertificate_list_with_options_async(request, runtime)

    def describe_certificate_private_key_with_options(
        self,
        request: cas_20200630_models.DescribeCertificatePrivateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCertificatePrivateKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EncryptedCode'] = request.encrypted_code
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCertificatePrivateKey',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCertificatePrivateKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificate_private_key_with_options_async(
        self,
        request: cas_20200630_models.DescribeCertificatePrivateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCertificatePrivateKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EncryptedCode'] = request.encrypted_code
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeCertificatePrivateKey',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCertificatePrivateKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificate_private_key(
        self,
        request: cas_20200630_models.DescribeCertificatePrivateKeyRequest,
    ) -> cas_20200630_models.DescribeCertificatePrivateKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_private_key_with_options(request, runtime)

    async def describe_certificate_private_key_async(
        self,
        request: cas_20200630_models.DescribeCertificatePrivateKeyRequest,
    ) -> cas_20200630_models.DescribeCertificatePrivateKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_private_key_with_options_async(request, runtime)

    def describe_client_certificate_with_options(
        self,
        request: cas_20200630_models.DescribeClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_with_options_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate(
        self,
        request: cas_20200630_models.DescribeClientCertificateRequest,
    ) -> cas_20200630_models.DescribeClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_with_options(request, runtime)

    async def describe_client_certificate_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateRequest,
    ) -> cas_20200630_models.DescribeClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_certificate_with_options_async(request, runtime)

    def describe_client_certificate_for_serial_number_with_options(
        self,
        request: cas_20200630_models.DescribeClientCertificateForSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateForSerialNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateForSerialNumber',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateForSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_for_serial_number_with_options_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateForSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateForSerialNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateForSerialNumber',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateForSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate_for_serial_number(
        self,
        request: cas_20200630_models.DescribeClientCertificateForSerialNumberRequest,
    ) -> cas_20200630_models.DescribeClientCertificateForSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_for_serial_number_with_options(request, runtime)

    async def describe_client_certificate_for_serial_number_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateForSerialNumberRequest,
    ) -> cas_20200630_models.DescribeClientCertificateForSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_certificate_for_serial_number_with_options_async(request, runtime)

    def describe_client_certificate_status_with_options(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_status_with_options_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate_status(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusRequest,
    ) -> cas_20200630_models.DescribeClientCertificateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_status_with_options(request, runtime)

    async def describe_client_certificate_status_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusRequest,
    ) -> cas_20200630_models.DescribeClientCertificateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_certificate_status_with_options_async(request, runtime)

    def describe_client_certificate_status_for_serial_number_with_options(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusForSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateStatusForSerialNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatusForSerialNumber',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateStatusForSerialNumberResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_client_certificate_status_for_serial_number_with_options_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusForSerialNumberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateStatusForSerialNumberResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatusForSerialNumber',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeClientCertificateStatusForSerialNumberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_client_certificate_status_for_serial_number(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusForSerialNumberRequest,
    ) -> cas_20200630_models.DescribeClientCertificateStatusForSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_status_for_serial_number_with_options(request, runtime)

    async def describe_client_certificate_status_for_serial_number_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusForSerialNumberRequest,
    ) -> cas_20200630_models.DescribeClientCertificateStatusForSerialNumberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_certificate_status_for_serial_number_with_options_async(request, runtime)

    def get_cainstance_status_with_options(
        self,
        request: cas_20200630_models.GetCAInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.GetCAInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetCAInstanceStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.GetCAInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cainstance_status_with_options_async(
        self,
        request: cas_20200630_models.GetCAInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.GetCAInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetCAInstanceStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.GetCAInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cainstance_status(
        self,
        request: cas_20200630_models.GetCAInstanceStatusRequest,
    ) -> cas_20200630_models.GetCAInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cainstance_status_with_options(request, runtime)

    async def get_cainstance_status_async(
        self,
        request: cas_20200630_models.GetCAInstanceStatusRequest,
    ) -> cas_20200630_models.GetCAInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cainstance_status_with_options_async(request, runtime)

    def list_cacertificate_log_with_options(
        self,
        request: cas_20200630_models.ListCACertificateLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListCACertificateLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCACertificateLog',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListCACertificateLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cacertificate_log_with_options_async(
        self,
        request: cas_20200630_models.ListCACertificateLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListCACertificateLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListCACertificateLog',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListCACertificateLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cacertificate_log(
        self,
        request: cas_20200630_models.ListCACertificateLogRequest,
    ) -> cas_20200630_models.ListCACertificateLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cacertificate_log_with_options(request, runtime)

    async def list_cacertificate_log_async(
        self,
        request: cas_20200630_models.ListCACertificateLogRequest,
    ) -> cas_20200630_models.ListCACertificateLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cacertificate_log_with_options_async(request, runtime)

    def list_client_certificate_with_options(
        self,
        request: cas_20200630_models.ListClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_certificate_with_options_async(
        self,
        request: cas_20200630_models.ListClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListClientCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_certificate(
        self,
        request: cas_20200630_models.ListClientCertificateRequest,
    ) -> cas_20200630_models.ListClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_client_certificate_with_options(request, runtime)

    async def list_client_certificate_async(
        self,
        request: cas_20200630_models.ListClientCertificateRequest,
    ) -> cas_20200630_models.ListClientCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_client_certificate_with_options_async(request, runtime)

    def list_revoke_certificate_with_options(
        self,
        request: cas_20200630_models.ListRevokeCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListRevokeCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRevokeCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListRevokeCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_revoke_certificate_with_options_async(
        self,
        request: cas_20200630_models.ListRevokeCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListRevokeCertificateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentPage'] = request.current_page
        query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRevokeCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListRevokeCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_revoke_certificate(
        self,
        request: cas_20200630_models.ListRevokeCertificateRequest,
    ) -> cas_20200630_models.ListRevokeCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_revoke_certificate_with_options(request, runtime)

    async def list_revoke_certificate_async(
        self,
        request: cas_20200630_models.ListRevokeCertificateRequest,
    ) -> cas_20200630_models.ListRevokeCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_revoke_certificate_with_options_async(request, runtime)

    def update_cacertificate_status_with_options(
        self,
        request: cas_20200630_models.UpdateCACertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.UpdateCACertificateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCACertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.UpdateCACertificateStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cacertificate_status_with_options_async(
        self,
        request: cas_20200630_models.UpdateCACertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.UpdateCACertificateStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Identifier'] = request.identifier
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCACertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.UpdateCACertificateStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cacertificate_status(
        self,
        request: cas_20200630_models.UpdateCACertificateStatusRequest,
    ) -> cas_20200630_models.UpdateCACertificateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cacertificate_status_with_options(request, runtime)

    async def update_cacertificate_status_async(
        self,
        request: cas_20200630_models.UpdateCACertificateStatusRequest,
    ) -> cas_20200630_models.UpdateCACertificateStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cacertificate_status_with_options_async(request, runtime)
