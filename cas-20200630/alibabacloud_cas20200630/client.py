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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_client_certificate_with_options(
        self,
        request: cas_20200630_models.CreateClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateClientCertificateResponse:
        """
        @summary Issues a client certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](~~CreateRootCACertificate~~) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](~~CreateRootCACertificate~~) operation. Only intermediate CA certificates can issue client certificates.
        ## QPS limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientCertificateResponse
        """
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
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
            action='CreateClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a client certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](~~CreateRootCACertificate~~) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](~~CreateRootCACertificate~~) operation. Only intermediate CA certificates can issue client certificates.
        ## QPS limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientCertificateResponse
        """
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
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
            action='CreateClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a client certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](~~CreateRootCACertificate~~) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](~~CreateRootCACertificate~~) operation. Only intermediate CA certificates can issue client certificates.
        ## QPS limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateRequest
        @return: CreateClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_client_certificate_with_options(request, runtime)

    async def create_client_certificate_async(
        self,
        request: cas_20200630_models.CreateClientCertificateRequest,
    ) -> cas_20200630_models.CreateClientCertificateResponse:
        """
        @summary Issues a client certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](~~CreateRootCACertificate~~) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](~~CreateRootCACertificate~~) operation. Only intermediate CA certificates can issue client certificates.
        ## QPS limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateRequest
        @return: CreateClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_client_certificate_with_options_async(request, runtime)

    def create_client_certificate_with_csr_with_options(
        self,
        request: cas_20200630_models.CreateClientCertificateWithCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateClientCertificateWithCsrResponse:
        """
        @summary Issues a client certificate by using a custom certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue client certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateWithCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientCertificateWithCsrResponse
        """
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
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
            action='CreateClientCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a client certificate by using a custom certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue client certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateWithCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClientCertificateWithCsrResponse
        """
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
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
            action='CreateClientCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a client certificate by using a custom certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue client certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateWithCsrRequest
        @return: CreateClientCertificateWithCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_client_certificate_with_csr_with_options(request, runtime)

    async def create_client_certificate_with_csr_async(
        self,
        request: cas_20200630_models.CreateClientCertificateWithCsrRequest,
    ) -> cas_20200630_models.CreateClientCertificateWithCsrResponse:
        """
        @summary Issues a client certificate by using a custom certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue client certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateClientCertificateWithCsrRequest
        @return: CreateClientCertificateWithCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_client_certificate_with_csr_with_options_async(request, runtime)

    def create_custom_certificate_with_options(
        self,
        request: cas_20200630_models.CreateCustomCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateCustomCertificateResponse:
        """
        @summary Issues a certificate based on the specified key usage, extended key usage, and name and alias of the entity that uses the certificate.
        
        @description By default, the name of the entity is obtained from the certificate signing request (CSR) of the certificate that you want to issue. If you specify a different name for the entity, the name of the entity in the CSR becomes invalid. The specified name is used to issue the certificate.
        You must specify the key usage and extended key usage based on the certificate type. The following list describes common certificate types:
        Server certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth
        Client certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: clientAuth
        Mutual Transport Layer Security (TLS) authentication certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth or clientAuth
        Email certificate
        Key usage: digitalSignature or contentCommitment
        Extended key usage: emailProtection
        Note: Compliant certificate authorities (CAs) are managed by third-party authorities. This operation is not supported for compliant CAs.
        
        @param request: CreateCustomCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_passthrough):
            query['ApiPassthrough'] = request.api_passthrough
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.validity):
            query['Validity'] = request.validity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateCustomCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_certificate_with_options_async(
        self,
        request: cas_20200630_models.CreateCustomCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateCustomCertificateResponse:
        """
        @summary Issues a certificate based on the specified key usage, extended key usage, and name and alias of the entity that uses the certificate.
        
        @description By default, the name of the entity is obtained from the certificate signing request (CSR) of the certificate that you want to issue. If you specify a different name for the entity, the name of the entity in the CSR becomes invalid. The specified name is used to issue the certificate.
        You must specify the key usage and extended key usage based on the certificate type. The following list describes common certificate types:
        Server certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth
        Client certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: clientAuth
        Mutual Transport Layer Security (TLS) authentication certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth or clientAuth
        Email certificate
        Key usage: digitalSignature or contentCommitment
        Extended key usage: emailProtection
        Note: Compliant certificate authorities (CAs) are managed by third-party authorities. This operation is not supported for compliant CAs.
        
        @param request: CreateCustomCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_passthrough):
            query['ApiPassthrough'] = request.api_passthrough
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not UtilClient.is_unset(request.immediately):
            query['Immediately'] = request.immediately
        if not UtilClient.is_unset(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.validity):
            query['Validity'] = request.validity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.CreateCustomCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_certificate(
        self,
        request: cas_20200630_models.CreateCustomCertificateRequest,
    ) -> cas_20200630_models.CreateCustomCertificateResponse:
        """
        @summary Issues a certificate based on the specified key usage, extended key usage, and name and alias of the entity that uses the certificate.
        
        @description By default, the name of the entity is obtained from the certificate signing request (CSR) of the certificate that you want to issue. If you specify a different name for the entity, the name of the entity in the CSR becomes invalid. The specified name is used to issue the certificate.
        You must specify the key usage and extended key usage based on the certificate type. The following list describes common certificate types:
        Server certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth
        Client certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: clientAuth
        Mutual Transport Layer Security (TLS) authentication certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth or clientAuth
        Email certificate
        Key usage: digitalSignature or contentCommitment
        Extended key usage: emailProtection
        Note: Compliant certificate authorities (CAs) are managed by third-party authorities. This operation is not supported for compliant CAs.
        
        @param request: CreateCustomCertificateRequest
        @return: CreateCustomCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_certificate_with_options(request, runtime)

    async def create_custom_certificate_async(
        self,
        request: cas_20200630_models.CreateCustomCertificateRequest,
    ) -> cas_20200630_models.CreateCustomCertificateResponse:
        """
        @summary Issues a certificate based on the specified key usage, extended key usage, and name and alias of the entity that uses the certificate.
        
        @description By default, the name of the entity is obtained from the certificate signing request (CSR) of the certificate that you want to issue. If you specify a different name for the entity, the name of the entity in the CSR becomes invalid. The specified name is used to issue the certificate.
        You must specify the key usage and extended key usage based on the certificate type. The following list describes common certificate types:
        Server certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth
        Client certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: clientAuth
        Mutual Transport Layer Security (TLS) authentication certificate
        Key usage: digitalSignature or keyEncipherment
        Extended key usage: serverAuth or clientAuth
        Email certificate
        Key usage: digitalSignature or contentCommitment
        Extended key usage: emailProtection
        Note: Compliant certificate authorities (CAs) are managed by third-party authorities. This operation is not supported for compliant CAs.
        
        @param request: CreateCustomCertificateRequest
        @return: CreateCustomCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_certificate_with_options_async(request, runtime)

    def create_revoke_client_certificate_with_options(
        self,
        request: cas_20200630_models.CreateRevokeClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateRevokeClientCertificateResponse:
        """
        @summary Revokes a client certificate or a server certificate.
        
        @description After a client certificate or a server certificate is revoked, the client or the server on which the certificate is installed cannot establish HTTPS connections with other devices.
        After a client certificate or a server certificate is revoked, you can call the [DeleteClientCertificate](https://help.aliyun.com/document_detail/330880.html) operation to permanently delete the certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRevokeClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRevokeClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRevokeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Revokes a client certificate or a server certificate.
        
        @description After a client certificate or a server certificate is revoked, the client or the server on which the certificate is installed cannot establish HTTPS connections with other devices.
        After a client certificate or a server certificate is revoked, you can call the [DeleteClientCertificate](https://help.aliyun.com/document_detail/330880.html) operation to permanently delete the certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRevokeClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRevokeClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRevokeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Revokes a client certificate or a server certificate.
        
        @description After a client certificate or a server certificate is revoked, the client or the server on which the certificate is installed cannot establish HTTPS connections with other devices.
        After a client certificate or a server certificate is revoked, you can call the [DeleteClientCertificate](https://help.aliyun.com/document_detail/330880.html) operation to permanently delete the certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRevokeClientCertificateRequest
        @return: CreateRevokeClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_revoke_client_certificate_with_options(request, runtime)

    async def create_revoke_client_certificate_async(
        self,
        request: cas_20200630_models.CreateRevokeClientCertificateRequest,
    ) -> cas_20200630_models.CreateRevokeClientCertificateResponse:
        """
        @summary Revokes a client certificate or a server certificate.
        
        @description After a client certificate or a server certificate is revoked, the client or the server on which the certificate is installed cannot establish HTTPS connections with other devices.
        After a client certificate or a server certificate is revoked, you can call the [DeleteClientCertificate](https://help.aliyun.com/document_detail/330880.html) operation to permanently delete the certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRevokeClientCertificateRequest
        @return: CreateRevokeClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_revoke_client_certificate_with_options_async(request, runtime)

    def create_root_cacertificate_with_options(
        self,
        request: cas_20200630_models.CreateRootCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateRootCACertificateResponse:
        """
        @summary Creates a root certificate authority (CA) certificate.
        
        @description You can call the CreateRootCACertificate operation to create a self-signed root CA certificate. A root CA certificate is the trust anchor in a chain of trust for private certificates that are used within an enterprise. You must create a root CA certificate before you can use the root CA certificate to issue intermediate CA certificates. Then, you can use the intermediate CA certificates to issue client certificates and server certificates.
        Before you call this operation, make sure that you have purchased a private root CA instance by using the [Certificate Management Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRootCACertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRootCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRootCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a root certificate authority (CA) certificate.
        
        @description You can call the CreateRootCACertificate operation to create a self-signed root CA certificate. A root CA certificate is the trust anchor in a chain of trust for private certificates that are used within an enterprise. You must create a root CA certificate before you can use the root CA certificate to issue intermediate CA certificates. Then, you can use the intermediate CA certificates to issue client certificates and server certificates.
        Before you call this operation, make sure that you have purchased a private root CA instance by using the [Certificate Management Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRootCACertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRootCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRootCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates a root certificate authority (CA) certificate.
        
        @description You can call the CreateRootCACertificate operation to create a self-signed root CA certificate. A root CA certificate is the trust anchor in a chain of trust for private certificates that are used within an enterprise. You must create a root CA certificate before you can use the root CA certificate to issue intermediate CA certificates. Then, you can use the intermediate CA certificates to issue client certificates and server certificates.
        Before you call this operation, make sure that you have purchased a private root CA instance by using the [Certificate Management Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRootCACertificateRequest
        @return: CreateRootCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_root_cacertificate_with_options(request, runtime)

    async def create_root_cacertificate_async(
        self,
        request: cas_20200630_models.CreateRootCACertificateRequest,
    ) -> cas_20200630_models.CreateRootCACertificateResponse:
        """
        @summary Creates a root certificate authority (CA) certificate.
        
        @description You can call the CreateRootCACertificate operation to create a self-signed root CA certificate. A root CA certificate is the trust anchor in a chain of trust for private certificates that are used within an enterprise. You must create a root CA certificate before you can use the root CA certificate to issue intermediate CA certificates. Then, you can use the intermediate CA certificates to issue client certificates and server certificates.
        Before you call this operation, make sure that you have purchased a private root CA instance by using the [Certificate Management Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateRootCACertificateRequest
        @return: CreateRootCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_root_cacertificate_with_options_async(request, runtime)

    def create_server_certificate_with_options(
        self,
        request: cas_20200630_models.CreateServerCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateServerCertificateResponse:
        """
        @summary Issues a server certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateServerCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerCertificateResponse
        """
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
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a server certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateServerCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerCertificateResponse
        """
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
        if not UtilClient.is_unset(request.days):
            query['Days'] = request.days
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a server certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateServerCertificateRequest
        @return: CreateServerCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_server_certificate_with_options(request, runtime)

    async def create_server_certificate_async(
        self,
        request: cas_20200630_models.CreateServerCertificateRequest,
    ) -> cas_20200630_models.CreateServerCertificateResponse:
        """
        @summary Issues a server certificate by using a system-generated certificate signing request (CSR) file.
        
        @description Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateServerCertificateRequest
        @return: CreateServerCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_server_certificate_with_options_async(request, runtime)

    def create_server_certificate_with_csr_with_options(
        self,
        request: cas_20200630_models.CreateServerCertificateWithCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateServerCertificateWithCsrResponse:
        """
        @summary Issues a server certificate by using a custom certificate signing request (CSR) file.
        
        @description ## Usage notes
        Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        
        @param request: CreateServerCertificateWithCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerCertificateWithCsrResponse
        """
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
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a server certificate by using a custom certificate signing request (CSR) file.
        
        @description ## Usage notes
        Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        
        @param request: CreateServerCertificateWithCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServerCertificateWithCsrResponse
        """
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
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
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
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServerCertificateWithCsr',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Issues a server certificate by using a custom certificate signing request (CSR) file.
        
        @description ## Usage notes
        Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        
        @param request: CreateServerCertificateWithCsrRequest
        @return: CreateServerCertificateWithCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_server_certificate_with_csr_with_options(request, runtime)

    async def create_server_certificate_with_csr_async(
        self,
        request: cas_20200630_models.CreateServerCertificateWithCsrRequest,
    ) -> cas_20200630_models.CreateServerCertificateWithCsrResponse:
        """
        @summary Issues a server certificate by using a custom certificate signing request (CSR) file.
        
        @description ## Usage notes
        Before you call this operation, make sure that you have created a root certificate authority (CA) certificate by calling the [CreateRootCACertificate](https://help.aliyun.com/document_detail/328093.html) operation and an intermediate CA certificate by calling the [CreateSubCACertificate](https://help.aliyun.com/document_detail/328094.html) operation. Only intermediate CA certificates can be used to issue server certificates.
        
        @param request: CreateServerCertificateWithCsrRequest
        @return: CreateServerCertificateWithCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_server_certificate_with_csr_with_options_async(request, runtime)

    def create_sub_cacertificate_with_options(
        self,
        request: cas_20200630_models.CreateSubCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.CreateSubCACertificateResponse:
        """
        @summary Creates an intermediate certificate authority (CA) certificate.
        
        @description You can call this operation to issue an intermediate certificate authority (CA) certificate by using an existing root CA certificate. Intermediate CA certificates can be used to issue client certificates and server certificates.
        Before you call this operation, make sure that you have issued a root CA certificate by calling the [CreateRootCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSubCACertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.crl_day):
            query['CrlDay'] = request.crl_day
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not UtilClient.is_unset(request.extended_key_usages):
            query['ExtendedKeyUsages'] = request.extended_key_usages
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.path_len_constraint):
            query['PathLenConstraint'] = request.path_len_constraint
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates an intermediate certificate authority (CA) certificate.
        
        @description You can call this operation to issue an intermediate certificate authority (CA) certificate by using an existing root CA certificate. Intermediate CA certificates can be used to issue client certificates and server certificates.
        Before you call this operation, make sure that you have issued a root CA certificate by calling the [CreateRootCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSubCACertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSubCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.crl_day):
            query['CrlDay'] = request.crl_day
        if not UtilClient.is_unset(request.enable_crl):
            query['EnableCrl'] = request.enable_crl
        if not UtilClient.is_unset(request.extended_key_usages):
            query['ExtendedKeyUsages'] = request.extended_key_usages
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.organization):
            query['Organization'] = request.organization
        if not UtilClient.is_unset(request.organization_unit):
            query['OrganizationUnit'] = request.organization_unit
        if not UtilClient.is_unset(request.parent_identifier):
            query['ParentIdentifier'] = request.parent_identifier
        if not UtilClient.is_unset(request.path_len_constraint):
            query['PathLenConstraint'] = request.path_len_constraint
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.years):
            query['Years'] = request.years
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Creates an intermediate certificate authority (CA) certificate.
        
        @description You can call this operation to issue an intermediate certificate authority (CA) certificate by using an existing root CA certificate. Intermediate CA certificates can be used to issue client certificates and server certificates.
        Before you call this operation, make sure that you have issued a root CA certificate by calling the [CreateRootCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSubCACertificateRequest
        @return: CreateSubCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_sub_cacertificate_with_options(request, runtime)

    async def create_sub_cacertificate_async(
        self,
        request: cas_20200630_models.CreateSubCACertificateRequest,
    ) -> cas_20200630_models.CreateSubCACertificateResponse:
        """
        @summary Creates an intermediate certificate authority (CA) certificate.
        
        @description You can call this operation to issue an intermediate certificate authority (CA) certificate by using an existing root CA certificate. Intermediate CA certificates can be used to issue client certificates and server certificates.
        Before you call this operation, make sure that you have issued a root CA certificate by calling the [CreateRootCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: CreateSubCACertificateRequest
        @return: CreateSubCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_sub_cacertificate_with_options_async(request, runtime)

    def delete_client_certificate_with_options(
        self,
        request: cas_20200630_models.DeleteClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DeleteClientCertificateResponse:
        """
        @summary Deletes a client certificate or a server certificate that is revoked.
        
        @description Before you call this operation, you must call the [CreateRevokeClientCertificate](https://help.aliyun.com/document_detail/330876.html) operation to revoke a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a client certificate or a server certificate that is revoked.
        
        @description Before you call this operation, you must call the [CreateRevokeClientCertificate](https://help.aliyun.com/document_detail/330876.html) operation to revoke a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Deletes a client certificate or a server certificate that is revoked.
        
        @description Before you call this operation, you must call the [CreateRevokeClientCertificate](https://help.aliyun.com/document_detail/330876.html) operation to revoke a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteClientCertificateRequest
        @return: DeleteClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_client_certificate_with_options(request, runtime)

    async def delete_client_certificate_async(
        self,
        request: cas_20200630_models.DeleteClientCertificateRequest,
    ) -> cas_20200630_models.DeleteClientCertificateResponse:
        """
        @summary Deletes a client certificate or a server certificate that is revoked.
        
        @description Before you call this operation, you must call the [CreateRevokeClientCertificate](https://help.aliyun.com/document_detail/330876.html) operation to revoke a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteClientCertificateRequest
        @return: DeleteClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_client_certificate_with_options_async(request, runtime)

    def describe_cacertificate_with_options(
        self,
        request: cas_20200630_models.DescribeCACertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateResponse:
        """
        @summary Queries the details about a root certificate authority (CA) certificate or an intermediate CA certificate.
        
        @description You can call the DescribeCACertificate operation to query the details about a root CA certificate or an intermediate CA certificate by using the unique identifier of the root CA certificate or intermediate CA certificate. The details include the serial number, user information, and content of a CA certificate.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about a root certificate authority (CA) certificate or an intermediate CA certificate.
        
        @description You can call the DescribeCACertificate operation to query the details about a root CA certificate or an intermediate CA certificate by using the unique identifier of the root CA certificate or intermediate CA certificate. The details include the serial number, user information, and content of a CA certificate.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about a root certificate authority (CA) certificate or an intermediate CA certificate.
        
        @description You can call the DescribeCACertificate operation to query the details about a root CA certificate or an intermediate CA certificate by using the unique identifier of the root CA certificate or intermediate CA certificate. The details include the serial number, user information, and content of a CA certificate.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateRequest
        @return: DescribeCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_with_options(request, runtime)

    async def describe_cacertificate_async(
        self,
        request: cas_20200630_models.DescribeCACertificateRequest,
    ) -> cas_20200630_models.DescribeCACertificateResponse:
        """
        @summary Queries the details about a root certificate authority (CA) certificate or an intermediate CA certificate.
        
        @description You can call the DescribeCACertificate operation to query the details about a root CA certificate or an intermediate CA certificate by using the unique identifier of the root CA certificate or intermediate CA certificate. The details include the serial number, user information, and content of a CA certificate.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateRequest
        @return: DescribeCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cacertificate_with_options_async(request, runtime)

    def describe_cacertificate_count_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateCountResponse:
        """
        @summary Queries the number of certificate authority (CA) certificates that you create.
        
        @description You can call the DescribeCACertificateCount operation to query the number of created CA certificates, which includes root CA certificates and intermediate CA certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCACertificateCountResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCACertificateCount',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the number of certificate authority (CA) certificates that you create.
        
        @description You can call the DescribeCACertificateCount operation to query the number of created CA certificates, which includes root CA certificates and intermediate CA certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateCountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCACertificateCountResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCACertificateCount',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.DescribeCACertificateCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cacertificate_count(self) -> cas_20200630_models.DescribeCACertificateCountResponse:
        """
        @summary Queries the number of certificate authority (CA) certificates that you create.
        
        @description You can call the DescribeCACertificateCount operation to query the number of created CA certificates, which includes root CA certificates and intermediate CA certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @return: DescribeCACertificateCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_count_with_options(runtime)

    async def describe_cacertificate_count_async(self) -> cas_20200630_models.DescribeCACertificateCountResponse:
        """
        @summary Queries the number of certificate authority (CA) certificates that you create.
        
        @description You can call the DescribeCACertificateCount operation to query the number of created CA certificates, which includes root CA certificates and intermediate CA certificates.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @return: DescribeCACertificateCountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cacertificate_count_with_options_async(runtime)

    def describe_cacertificate_list_with_options(
        self,
        request: cas_20200630_models.DescribeCACertificateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCACertificateListResponse:
        """
        @summary Queries the details about all root certificate authority (CA) certificates and intermediate CA certificates.
        
        @description You can call the DescribeCACertificateList operation to perform a paged query of the details about all CA certificates that you create. The details include the unique identifier, serial number, user information, and content of each root CA certificate or intermediate CA certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCACertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_status):
            query['CaStatus'] = request.ca_status
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.issuer_type):
            query['IssuerType'] = request.issuer_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.valid_status):
            query['ValidStatus'] = request.valid_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificateList',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about all root certificate authority (CA) certificates and intermediate CA certificates.
        
        @description You can call the DescribeCACertificateList operation to perform a paged query of the details about all CA certificates that you create. The details include the unique identifier, serial number, user information, and content of each root CA certificate or intermediate CA certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCACertificateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ca_status):
            query['CaStatus'] = request.ca_status
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.issuer_type):
            query['IssuerType'] = request.issuer_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.valid_status):
            query['ValidStatus'] = request.valid_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificateList',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about all root certificate authority (CA) certificates and intermediate CA certificates.
        
        @description You can call the DescribeCACertificateList operation to perform a paged query of the details about all CA certificates that you create. The details include the unique identifier, serial number, user information, and content of each root CA certificate or intermediate CA certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateListRequest
        @return: DescribeCACertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificate_list_with_options(request, runtime)

    async def describe_cacertificate_list_async(
        self,
        request: cas_20200630_models.DescribeCACertificateListRequest,
    ) -> cas_20200630_models.DescribeCACertificateListResponse:
        """
        @summary Queries the details about all root certificate authority (CA) certificates and intermediate CA certificates.
        
        @description You can call the DescribeCACertificateList operation to perform a paged query of the details about all CA certificates that you create. The details include the unique identifier, serial number, user information, and content of each root CA certificate or intermediate CA certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCACertificateListRequest
        @return: DescribeCACertificateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cacertificate_list_with_options_async(request, runtime)

    def describe_certificate_private_key_with_options(
        self,
        request: cas_20200630_models.DescribeCertificatePrivateKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeCertificatePrivateKeyResponse:
        """
        @summary Queries the encrypted private key of a client certificate or a server certificate.
        
        @description ## Usage notes
        You can call the DescribeCertificatePrivateKey operation to obtain the encrypted private key of a client certificate or a server certificate. The certificate is issued based on a system-generated certificate signing request (CSR). Before you call this operation, make sure that you have issued a client certificate or a server certificate by calling the following operation:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        To ensure the security of private key transmission, the DescribeCertificatePrivateKey operation encrypts the private key by using the private key password that you specify and returns the encrypted private key. The private key password is a string that is used to encrypt the private key. After you obtain the encrypted private key of the certificate, you can use the following methods to decrypt the private key:
        If the encryption algorithm of the certificate is RSA, you must run the `openssl rsa -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is ECC, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is SM2, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        >  You can call the [DescribeClientCertificate] operation to query the encryption algorithm type of a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCertificatePrivateKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificatePrivateKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypted_code):
            query['EncryptedCode'] = request.encrypted_code
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificatePrivateKey',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the encrypted private key of a client certificate or a server certificate.
        
        @description ## Usage notes
        You can call the DescribeCertificatePrivateKey operation to obtain the encrypted private key of a client certificate or a server certificate. The certificate is issued based on a system-generated certificate signing request (CSR). Before you call this operation, make sure that you have issued a client certificate or a server certificate by calling the following operation:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        To ensure the security of private key transmission, the DescribeCertificatePrivateKey operation encrypts the private key by using the private key password that you specify and returns the encrypted private key. The private key password is a string that is used to encrypt the private key. After you obtain the encrypted private key of the certificate, you can use the following methods to decrypt the private key:
        If the encryption algorithm of the certificate is RSA, you must run the `openssl rsa -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is ECC, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is SM2, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        >  You can call the [DescribeClientCertificate] operation to query the encryption algorithm type of a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCertificatePrivateKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificatePrivateKeyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypted_code):
            query['EncryptedCode'] = request.encrypted_code
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificatePrivateKey',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the encrypted private key of a client certificate or a server certificate.
        
        @description ## Usage notes
        You can call the DescribeCertificatePrivateKey operation to obtain the encrypted private key of a client certificate or a server certificate. The certificate is issued based on a system-generated certificate signing request (CSR). Before you call this operation, make sure that you have issued a client certificate or a server certificate by calling the following operation:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        To ensure the security of private key transmission, the DescribeCertificatePrivateKey operation encrypts the private key by using the private key password that you specify and returns the encrypted private key. The private key password is a string that is used to encrypt the private key. After you obtain the encrypted private key of the certificate, you can use the following methods to decrypt the private key:
        If the encryption algorithm of the certificate is RSA, you must run the `openssl rsa -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is ECC, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is SM2, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        >  You can call the [DescribeClientCertificate] operation to query the encryption algorithm type of a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCertificatePrivateKeyRequest
        @return: DescribeCertificatePrivateKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_private_key_with_options(request, runtime)

    async def describe_certificate_private_key_async(
        self,
        request: cas_20200630_models.DescribeCertificatePrivateKeyRequest,
    ) -> cas_20200630_models.DescribeCertificatePrivateKeyResponse:
        """
        @summary Queries the encrypted private key of a client certificate or a server certificate.
        
        @description ## Usage notes
        You can call the DescribeCertificatePrivateKey operation to obtain the encrypted private key of a client certificate or a server certificate. The certificate is issued based on a system-generated certificate signing request (CSR). Before you call this operation, make sure that you have issued a client certificate or a server certificate by calling the following operation:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        To ensure the security of private key transmission, the DescribeCertificatePrivateKey operation encrypts the private key by using the private key password that you specify and returns the encrypted private key. The private key password is a string that is used to encrypt the private key. After you obtain the encrypted private key of the certificate, you can use the following methods to decrypt the private key:
        If the encryption algorithm of the certificate is RSA, you must run the `openssl rsa -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is ECC, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [OpenSSL](https://www.openssl.org/source/) or [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        If the encryption algorithm of the certificate is SM2, you must run the `openssl ec -in <Encrypted private key file> -passin pass:<Private key password> -out <Decrypted private key file>` command in the computer on which [BabaSSL](https://github.com/BabaSSL/BabaSSL) is installed.
        >  You can call the [DescribeClientCertificate] operation to query the encryption algorithm type of a client certificate or a server certificate.
        ## Limits
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeCertificatePrivateKeyRequest
        @return: DescribeCertificatePrivateKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_private_key_with_options_async(request, runtime)

    def describe_client_certificate_with_options(
        self,
        request: cas_20200630_models.DescribeClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateResponse:
        """
        @summary Queries the details about a client certificate or a server certificate by using the unique identifier of the certificate.
        
        @description You can call the DescribeClientCertificate operation to query the details about a client certificate or a server certificate by using the unique identifier of the certificate. The details include the serial number, user information, content, and status of each certificate.
        Before you call this operation, make sure that you have created a client certificate or a server certificate.
        For more information about how to call an operation to create a client certificate, see the following topics:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateClientCertificateWithCsr](https://help.aliyun.com/document_detail/330875.html)
        For more information about how to call an operation to create a server certificate, see the following topics:
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        [CreateServerCertificateWithCsr](https://help.aliyun.com/document_detail/330878.html)
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about a client certificate or a server certificate by using the unique identifier of the certificate.
        
        @description You can call the DescribeClientCertificate operation to query the details about a client certificate or a server certificate by using the unique identifier of the certificate. The details include the serial number, user information, content, and status of each certificate.
        Before you call this operation, make sure that you have created a client certificate or a server certificate.
        For more information about how to call an operation to create a client certificate, see the following topics:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateClientCertificateWithCsr](https://help.aliyun.com/document_detail/330875.html)
        For more information about how to call an operation to create a server certificate, see the following topics:
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        [CreateServerCertificateWithCsr](https://help.aliyun.com/document_detail/330878.html)
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about a client certificate or a server certificate by using the unique identifier of the certificate.
        
        @description You can call the DescribeClientCertificate operation to query the details about a client certificate or a server certificate by using the unique identifier of the certificate. The details include the serial number, user information, content, and status of each certificate.
        Before you call this operation, make sure that you have created a client certificate or a server certificate.
        For more information about how to call an operation to create a client certificate, see the following topics:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateClientCertificateWithCsr](https://help.aliyun.com/document_detail/330875.html)
        For more information about how to call an operation to create a server certificate, see the following topics:
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        [CreateServerCertificateWithCsr](https://help.aliyun.com/document_detail/330878.html)
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateRequest
        @return: DescribeClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_with_options(request, runtime)

    async def describe_client_certificate_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateRequest,
    ) -> cas_20200630_models.DescribeClientCertificateResponse:
        """
        @summary Queries the details about a client certificate or a server certificate by using the unique identifier of the certificate.
        
        @description You can call the DescribeClientCertificate operation to query the details about a client certificate or a server certificate by using the unique identifier of the certificate. The details include the serial number, user information, content, and status of each certificate.
        Before you call this operation, make sure that you have created a client certificate or a server certificate.
        For more information about how to call an operation to create a client certificate, see the following topics:
        [CreateClientCertificate](https://help.aliyun.com/document_detail/330873.html)
        [CreateClientCertificateWithCsr](https://help.aliyun.com/document_detail/330875.html)
        For more information about how to call an operation to create a server certificate, see the following topics:
        [CreateServerCertificate](https://help.aliyun.com/document_detail/330877.html)
        [CreateServerCertificateWithCsr](https://help.aliyun.com/document_detail/330878.html)
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateRequest
        @return: DescribeClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_certificate_with_options_async(request, runtime)

    def describe_client_certificate_status_with_options(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.DescribeClientCertificateStatusResponse:
        """
        @summary Queries the status information about client certificates and server certificates by using the unique identifiers of the certificates.
        
        @description You can call the DescribeClientCertificateStatus operation to query the status information about multiple client certificates or server certificates at a time by using the unique identifiers of the certificates. For example, you can check whether a certificate is revoked.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClientCertificateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status information about client certificates and server certificates by using the unique identifiers of the certificates.
        
        @description You can call the DescribeClientCertificateStatus operation to query the status information about multiple client certificates or server certificates at a time by using the unique identifiers of the certificates. For example, you can check whether a certificate is revoked.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClientCertificateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClientCertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status information about client certificates and server certificates by using the unique identifiers of the certificates.
        
        @description You can call the DescribeClientCertificateStatus operation to query the status information about multiple client certificates or server certificates at a time by using the unique identifiers of the certificates. For example, you can check whether a certificate is revoked.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateStatusRequest
        @return: DescribeClientCertificateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_client_certificate_status_with_options(request, runtime)

    async def describe_client_certificate_status_async(
        self,
        request: cas_20200630_models.DescribeClientCertificateStatusRequest,
    ) -> cas_20200630_models.DescribeClientCertificateStatusResponse:
        """
        @summary Queries the status information about client certificates and server certificates by using the unique identifiers of the certificates.
        
        @description You can call the DescribeClientCertificateStatus operation to query the status information about multiple client certificates or server certificates at a time by using the unique identifiers of the certificates. For example, you can check whether a certificate is revoked.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DescribeClientCertificateStatusRequest
        @return: DescribeClientCertificateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_client_certificate_status_with_options_async(request, runtime)

    def get_cainstance_status_with_options(
        self,
        request: cas_20200630_models.GetCAInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.GetCAInstanceStatusResponse:
        """
        @summary Queries the status information about a private root certificate authority (CA) instance or a private intermediate CA instance that you purchase by using the Certificate Management Service console.
        
        @description ## Usage notes
        You can call the GetCAInstanceStatus operation to query the status information of a private CA instance by using the ID of the instance. The instance is purchased by using the SSL Certificates Service console. The status information includes the status of the private CA instance, the number of certificates that can be issued by using the private CA instance, and the number of issued certificates.
        Before you call this operation, make sure that you have purchased a private CA by using the [SSL Certificates Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        
        @param request: GetCAInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCAInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCAInstanceStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status information about a private root certificate authority (CA) instance or a private intermediate CA instance that you purchase by using the Certificate Management Service console.
        
        @description ## Usage notes
        You can call the GetCAInstanceStatus operation to query the status information of a private CA instance by using the ID of the instance. The instance is purchased by using the SSL Certificates Service console. The status information includes the status of the private CA instance, the number of certificates that can be issued by using the private CA instance, and the number of issued certificates.
        Before you call this operation, make sure that you have purchased a private CA by using the [SSL Certificates Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        
        @param request: GetCAInstanceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCAInstanceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCAInstanceStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the status information about a private root certificate authority (CA) instance or a private intermediate CA instance that you purchase by using the Certificate Management Service console.
        
        @description ## Usage notes
        You can call the GetCAInstanceStatus operation to query the status information of a private CA instance by using the ID of the instance. The instance is purchased by using the SSL Certificates Service console. The status information includes the status of the private CA instance, the number of certificates that can be issued by using the private CA instance, and the number of issued certificates.
        Before you call this operation, make sure that you have purchased a private CA by using the [SSL Certificates Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        
        @param request: GetCAInstanceStatusRequest
        @return: GetCAInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cainstance_status_with_options(request, runtime)

    async def get_cainstance_status_async(
        self,
        request: cas_20200630_models.GetCAInstanceStatusRequest,
    ) -> cas_20200630_models.GetCAInstanceStatusResponse:
        """
        @summary Queries the status information about a private root certificate authority (CA) instance or a private intermediate CA instance that you purchase by using the Certificate Management Service console.
        
        @description ## Usage notes
        You can call the GetCAInstanceStatus operation to query the status information of a private CA instance by using the ID of the instance. The instance is purchased by using the SSL Certificates Service console. The status information includes the status of the private CA instance, the number of certificates that can be issued by using the private CA instance, and the number of issued certificates.
        Before you call this operation, make sure that you have purchased a private CA by using the [SSL Certificates Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist). For more information, see [Create a private CA](https://help.aliyun.com/document_detail/208553.html).
        
        @param request: GetCAInstanceStatusRequest
        @return: GetCAInstanceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cainstance_status_with_options_async(request, runtime)

    def list_cert_with_options(
        self,
        request: cas_20200630_models.ListCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListCertResponse:
        """
        @summary 获取证书列表
        
        @param request: ListCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_uuid):
            query['InstanceUuid'] = request.instance_uuid
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCert',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cert_with_options_async(
        self,
        request: cas_20200630_models.ListCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListCertResponse:
        """
        @summary 获取证书列表
        
        @param request: ListCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after_date):
            query['AfterDate'] = request.after_date
        if not UtilClient.is_unset(request.before_date):
            query['BeforeDate'] = request.before_date
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_uuid):
            query['InstanceUuid'] = request.instance_uuid
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCert',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.ListCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cert(
        self,
        request: cas_20200630_models.ListCertRequest,
    ) -> cas_20200630_models.ListCertResponse:
        """
        @summary 获取证书列表
        
        @param request: ListCertRequest
        @return: ListCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cert_with_options(request, runtime)

    async def list_cert_async(
        self,
        request: cas_20200630_models.ListCertRequest,
    ) -> cas_20200630_models.ListCertResponse:
        """
        @summary 获取证书列表
        
        @param request: ListCertRequest
        @return: ListCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cert_with_options_async(request, runtime)

    def list_client_certificate_with_options(
        self,
        request: cas_20200630_models.ListClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListClientCertificateResponse:
        """
        @summary Queries the details about all client certificates and server certificates.
        
        @description You can call the ListClientCertificate operation to perform a paged query of the details about all client certificates and server certificates that you create. The details include the unique identifier, serial number, user information, content, and status of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about all client certificates and server certificates.
        
        @description You can call the ListClientCertificate operation to perform a paged query of the details about all client certificates and server certificates that you create. The details include the unique identifier, serial number, user information, content, and status of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about all client certificates and server certificates.
        
        @description You can call the ListClientCertificate operation to perform a paged query of the details about all client certificates and server certificates that you create. The details include the unique identifier, serial number, user information, content, and status of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListClientCertificateRequest
        @return: ListClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_client_certificate_with_options(request, runtime)

    async def list_client_certificate_async(
        self,
        request: cas_20200630_models.ListClientCertificateRequest,
    ) -> cas_20200630_models.ListClientCertificateResponse:
        """
        @summary Queries the details about all client certificates and server certificates.
        
        @description You can call the ListClientCertificate operation to perform a paged query of the details about all client certificates and server certificates that you create. The details include the unique identifier, serial number, user information, content, and status of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListClientCertificateRequest
        @return: ListClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_client_certificate_with_options_async(request, runtime)

    def list_revoke_certificate_with_options(
        self,
        request: cas_20200630_models.ListRevokeCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.ListRevokeCertificateResponse:
        """
        @summary Queries the details about all client certificates and server certificates that are revoked.
        
        @description You can call the ListRevokeCertificate operation to perform a paged query of the details about all revoked client certificates and server certificates. The details include the unique identifier, serial number, and revocation date of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListRevokeCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRevokeCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRevokeCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about all client certificates and server certificates that are revoked.
        
        @description You can call the ListRevokeCertificate operation to perform a paged query of the details about all revoked client certificates and server certificates. The details include the unique identifier, serial number, and revocation date of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListRevokeCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRevokeCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRevokeCertificate',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Queries the details about all client certificates and server certificates that are revoked.
        
        @description You can call the ListRevokeCertificate operation to perform a paged query of the details about all revoked client certificates and server certificates. The details include the unique identifier, serial number, and revocation date of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListRevokeCertificateRequest
        @return: ListRevokeCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_revoke_certificate_with_options(request, runtime)

    async def list_revoke_certificate_async(
        self,
        request: cas_20200630_models.ListRevokeCertificateRequest,
    ) -> cas_20200630_models.ListRevokeCertificateResponse:
        """
        @summary Queries the details about all client certificates and server certificates that are revoked.
        
        @description You can call the ListRevokeCertificate operation to perform a paged query of the details about all revoked client certificates and server certificates. The details include the unique identifier, serial number, and revocation date of each certificate.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListRevokeCertificateRequest
        @return: ListRevokeCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_revoke_certificate_with_options_async(request, runtime)

    def update_cacertificate_status_with_options(
        self,
        request: cas_20200630_models.UpdateCACertificateStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.UpdateCACertificateStatusResponse:
        """
        @summary Changes the status of a root certificate authority (CA) certificate or an intermediate CA certificate from ISSUE to REVOKE.
        
        @description After a CA certificate is created, the CA certificate is in the ISSUE state by default. You can call the UpdateCACertificateStatus operation to change the status of a CA certificate from ISSUE to REVOKE. If a CA certificate is in the ISSUE state, the CA certificate can be used to issue certificates. If a CA certificate is in the REVOKE state, the CA certificate cannot be used to issue certificates, and the certificates that are issued from the CA certificate become invalid.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCACertificateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCACertificateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCACertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the status of a root certificate authority (CA) certificate or an intermediate CA certificate from ISSUE to REVOKE.
        
        @description After a CA certificate is created, the CA certificate is in the ISSUE state by default. You can call the UpdateCACertificateStatus operation to change the status of a CA certificate from ISSUE to REVOKE. If a CA certificate is in the ISSUE state, the CA certificate can be used to issue certificates. If a CA certificate is in the REVOKE state, the CA certificate cannot be used to issue certificates, and the certificates that are issued from the CA certificate become invalid.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCACertificateStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCACertificateStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCACertificateStatus',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
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
        """
        @summary Changes the status of a root certificate authority (CA) certificate or an intermediate CA certificate from ISSUE to REVOKE.
        
        @description After a CA certificate is created, the CA certificate is in the ISSUE state by default. You can call the UpdateCACertificateStatus operation to change the status of a CA certificate from ISSUE to REVOKE. If a CA certificate is in the ISSUE state, the CA certificate can be used to issue certificates. If a CA certificate is in the REVOKE state, the CA certificate cannot be used to issue certificates, and the certificates that are issued from the CA certificate become invalid.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCACertificateStatusRequest
        @return: UpdateCACertificateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_cacertificate_status_with_options(request, runtime)

    async def update_cacertificate_status_async(
        self,
        request: cas_20200630_models.UpdateCACertificateStatusRequest,
    ) -> cas_20200630_models.UpdateCACertificateStatusResponse:
        """
        @summary Changes the status of a root certificate authority (CA) certificate or an intermediate CA certificate from ISSUE to REVOKE.
        
        @description After a CA certificate is created, the CA certificate is in the ISSUE state by default. You can call the UpdateCACertificateStatus operation to change the status of a CA certificate from ISSUE to REVOKE. If a CA certificate is in the ISSUE state, the CA certificate can be used to issue certificates. If a CA certificate is in the REVOKE state, the CA certificate cannot be used to issue certificates, and the certificates that are issued from the CA certificate become invalid.
        Before you call this operation, make sure that you have created a root CA by calling the [CreateRootCACertificate] operation or an intermediate CA certificate by calling the [CreateSubCACertificate] operation.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UpdateCACertificateStatusRequest
        @return: UpdateCACertificateStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_cacertificate_status_with_options_async(request, runtime)

    def upload_pca_cert_to_cas_with_options(
        self,
        request: cas_20200630_models.UploadPcaCertToCasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.UploadPcaCertToCasResponse:
        """
        @summary 上传pca证书到SSL上传证书
        
        @param request: UploadPcaCertToCasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadPcaCertToCasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPcaCertToCas',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.UploadPcaCertToCasResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_pca_cert_to_cas_with_options_async(
        self,
        request: cas_20200630_models.UploadPcaCertToCasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200630_models.UploadPcaCertToCasResponse:
        """
        @summary 上传pca证书到SSL上传证书
        
        @param request: UploadPcaCertToCasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadPcaCertToCasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadPcaCertToCas',
            version='2020-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cas_20200630_models.UploadPcaCertToCasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_pca_cert_to_cas(
        self,
        request: cas_20200630_models.UploadPcaCertToCasRequest,
    ) -> cas_20200630_models.UploadPcaCertToCasResponse:
        """
        @summary 上传pca证书到SSL上传证书
        
        @param request: UploadPcaCertToCasRequest
        @return: UploadPcaCertToCasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_pca_cert_to_cas_with_options(request, runtime)

    async def upload_pca_cert_to_cas_async(
        self,
        request: cas_20200630_models.UploadPcaCertToCasRequest,
    ) -> cas_20200630_models.UploadPcaCertToCasResponse:
        """
        @summary 上传pca证书到SSL上传证书
        
        @param request: UploadPcaCertToCasRequest
        @return: UploadPcaCertToCasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_pca_cert_to_cas_with_options_async(request, runtime)
