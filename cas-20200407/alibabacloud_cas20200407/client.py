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

    def cancel_certificate_for_package_request_with_options(
        self,
        request: cas_20200407_models.CancelCertificateForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CancelCertificateForPackageRequestResponse:
        """
        @summary You can call the CancelCertificateForPackageRequest operation to cancel a certificate application order and revoke the issued certificate in the order. You can call this operation only when the certificate application order is in the *issued** state.
        >  You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        If a certificate is revoked within 30 calendar days after the issuance date, the consumed certificate quota is returned to you. Otherwise, the consumed certificate quota is not returned.
        
        @description Revokes an issued certificate and cancels the application order of the certificate.
        
        @param request: CancelCertificateForPackageRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCertificateForPackageRequestResponse
        """
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
        """
        @summary You can call the CancelCertificateForPackageRequest operation to cancel a certificate application order and revoke the issued certificate in the order. You can call this operation only when the certificate application order is in the *issued** state.
        >  You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        If a certificate is revoked within 30 calendar days after the issuance date, the consumed certificate quota is returned to you. Otherwise, the consumed certificate quota is not returned.
        
        @description Revokes an issued certificate and cancels the application order of the certificate.
        
        @param request: CancelCertificateForPackageRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelCertificateForPackageRequestResponse
        """
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
        """
        @summary You can call the CancelCertificateForPackageRequest operation to cancel a certificate application order and revoke the issued certificate in the order. You can call this operation only when the certificate application order is in the *issued** state.
        >  You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        If a certificate is revoked within 30 calendar days after the issuance date, the consumed certificate quota is returned to you. Otherwise, the consumed certificate quota is not returned.
        
        @description Revokes an issued certificate and cancels the application order of the certificate.
        
        @param request: CancelCertificateForPackageRequestRequest
        @return: CancelCertificateForPackageRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_certificate_for_package_request_with_options(request, runtime)

    async def cancel_certificate_for_package_request_async(
        self,
        request: cas_20200407_models.CancelCertificateForPackageRequestRequest,
    ) -> cas_20200407_models.CancelCertificateForPackageRequestResponse:
        """
        @summary You can call the CancelCertificateForPackageRequest operation to cancel a certificate application order and revoke the issued certificate in the order. You can call this operation only when the certificate application order is in the *issued** state.
        >  You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        If a certificate is revoked within 30 calendar days after the issuance date, the consumed certificate quota is returned to you. Otherwise, the consumed certificate quota is not returned.
        
        @description Revokes an issued certificate and cancels the application order of the certificate.
        
        @param request: CancelCertificateForPackageRequestRequest
        @return: CancelCertificateForPackageRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_certificate_for_package_request_with_options_async(request, runtime)

    def cancel_order_request_with_options(
        self,
        request: cas_20200407_models.CancelOrderRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CancelOrderRequestResponse:
        """
        @summary Cancels a certificate application order that is in the pending validation or being reviewed state.
        
        @description You can call the CancelOrderRequest operation to cancel a certificate application order only in the following scenarios:
        The order is in the **pending validation** state. You have submitted a certificate application but the verification of the domain name ownership is not complete.
        The order is in the **being reviewed** state. You have submitted a certificate application and the verification of the domain name ownership is complete, but the certificate authority (CA) does not complete the review of the certificate application.
        After a certificate application order is canceled, the status of the order changes to the *pending application** state. In this case, you can call the [DeleteCertificateRequest](https://help.aliyun.com/document_detail/164109.html) operation to delete the certificate application order. Then, the consumed certificate quota is returned to you.
        
        @param request: CancelOrderRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelOrderRequestResponse
        """
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
        """
        @summary Cancels a certificate application order that is in the pending validation or being reviewed state.
        
        @description You can call the CancelOrderRequest operation to cancel a certificate application order only in the following scenarios:
        The order is in the **pending validation** state. You have submitted a certificate application but the verification of the domain name ownership is not complete.
        The order is in the **being reviewed** state. You have submitted a certificate application and the verification of the domain name ownership is complete, but the certificate authority (CA) does not complete the review of the certificate application.
        After a certificate application order is canceled, the status of the order changes to the *pending application** state. In this case, you can call the [DeleteCertificateRequest](https://help.aliyun.com/document_detail/164109.html) operation to delete the certificate application order. Then, the consumed certificate quota is returned to you.
        
        @param request: CancelOrderRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelOrderRequestResponse
        """
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
        """
        @summary Cancels a certificate application order that is in the pending validation or being reviewed state.
        
        @description You can call the CancelOrderRequest operation to cancel a certificate application order only in the following scenarios:
        The order is in the **pending validation** state. You have submitted a certificate application but the verification of the domain name ownership is not complete.
        The order is in the **being reviewed** state. You have submitted a certificate application and the verification of the domain name ownership is complete, but the certificate authority (CA) does not complete the review of the certificate application.
        After a certificate application order is canceled, the status of the order changes to the *pending application** state. In this case, you can call the [DeleteCertificateRequest](https://help.aliyun.com/document_detail/164109.html) operation to delete the certificate application order. Then, the consumed certificate quota is returned to you.
        
        @param request: CancelOrderRequestRequest
        @return: CancelOrderRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_request_with_options(request, runtime)

    async def cancel_order_request_async(
        self,
        request: cas_20200407_models.CancelOrderRequestRequest,
    ) -> cas_20200407_models.CancelOrderRequestResponse:
        """
        @summary Cancels a certificate application order that is in the pending validation or being reviewed state.
        
        @description You can call the CancelOrderRequest operation to cancel a certificate application order only in the following scenarios:
        The order is in the **pending validation** state. You have submitted a certificate application but the verification of the domain name ownership is not complete.
        The order is in the **being reviewed** state. You have submitted a certificate application and the verification of the domain name ownership is complete, but the certificate authority (CA) does not complete the review of the certificate application.
        After a certificate application order is canceled, the status of the order changes to the *pending application** state. In this case, you can call the [DeleteCertificateRequest](https://help.aliyun.com/document_detail/164109.html) operation to delete the certificate application order. Then, the consumed certificate quota is returned to you.
        
        @param request: CancelOrderRequestRequest
        @return: CancelOrderRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_request_with_options_async(request, runtime)

    def create_certificate_for_package_request_with_options(
        self,
        request: cas_20200407_models.CreateCertificateForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateForPackageRequestResponse:
        """
        @summary Submits a certificate application.
        
        @description    Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455800.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of certificate resource plans that you purchase, the number of certificate applications that are submitted, and the number of certificates that are issued.
        After you call this operation to submit a certificate application and the certificate is issued, the certificate quota provided by the resource plan that you purchased is consumed. When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate that you want to apply for.
        After you call this operation to submit a certificate application, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete the verification of the domain name ownership, and complete the verification. If you use the DNS verification method, you must complete the verification in the management platform of the domain name. If you use the file verification method, you must complete the verification in the DNS server. Then, the certificate application order will be reviewed by the certificate authority (CA).
        
        @param request: CreateCertificateForPackageRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateForPackageRequestResponse
        """
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
        """
        @summary Submits a certificate application.
        
        @description    Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455800.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of certificate resource plans that you purchase, the number of certificate applications that are submitted, and the number of certificates that are issued.
        After you call this operation to submit a certificate application and the certificate is issued, the certificate quota provided by the resource plan that you purchased is consumed. When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate that you want to apply for.
        After you call this operation to submit a certificate application, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete the verification of the domain name ownership, and complete the verification. If you use the DNS verification method, you must complete the verification in the management platform of the domain name. If you use the file verification method, you must complete the verification in the DNS server. Then, the certificate application order will be reviewed by the certificate authority (CA).
        
        @param request: CreateCertificateForPackageRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateForPackageRequestResponse
        """
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
        """
        @summary Submits a certificate application.
        
        @description    Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455800.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of certificate resource plans that you purchase, the number of certificate applications that are submitted, and the number of certificates that are issued.
        After you call this operation to submit a certificate application and the certificate is issued, the certificate quota provided by the resource plan that you purchased is consumed. When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate that you want to apply for.
        After you call this operation to submit a certificate application, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete the verification of the domain name ownership, and complete the verification. If you use the DNS verification method, you must complete the verification in the management platform of the domain name. If you use the file verification method, you must complete the verification in the DNS server. Then, the certificate application order will be reviewed by the certificate authority (CA).
        
        @param request: CreateCertificateForPackageRequestRequest
        @return: CreateCertificateForPackageRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_for_package_request_with_options(request, runtime)

    async def create_certificate_for_package_request_async(
        self,
        request: cas_20200407_models.CreateCertificateForPackageRequestRequest,
    ) -> cas_20200407_models.CreateCertificateForPackageRequestResponse:
        """
        @summary Submits a certificate application.
        
        @description    Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455800.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of certificate resource plans that you purchase, the number of certificate applications that are submitted, and the number of certificates that are issued.
        After you call this operation to submit a certificate application and the certificate is issued, the certificate quota provided by the resource plan that you purchased is consumed. When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate that you want to apply for.
        After you call this operation to submit a certificate application, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete the verification of the domain name ownership, and complete the verification. If you use the DNS verification method, you must complete the verification in the management platform of the domain name. If you use the file verification method, you must complete the verification in the DNS server. Then, the certificate application order will be reviewed by the certificate authority (CA).
        
        @param request: CreateCertificateForPackageRequestRequest
        @return: CreateCertificateForPackageRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_for_package_request_with_options_async(request, runtime)

    def create_certificate_request_with_options(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using extended certificate services.
        
        @description    You can call this operation to apply for only DV certificates. If you want to apply for an organization validated (OV) or extended validation (EV) certificate, we recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation. This operation allows you to apply for certificates of all specifications and specify the method to generate a certificate signing request (CSR) file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455803.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications have been submitted, and the number of times that certificates have been issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, Certificate Management Service automatically creates a CSR file for your application and consumes the certificate quota in the certificate resource plans of the specified specifications that you purchased. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. Then, the certificate authority (CA) will review your certificate application.
        
        @param request: CreateCertificateRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateRequestResponse
        """
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
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using extended certificate services.
        
        @description    You can call this operation to apply for only DV certificates. If you want to apply for an organization validated (OV) or extended validation (EV) certificate, we recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation. This operation allows you to apply for certificates of all specifications and specify the method to generate a certificate signing request (CSR) file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455803.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications have been submitted, and the number of times that certificates have been issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, Certificate Management Service automatically creates a CSR file for your application and consumes the certificate quota in the certificate resource plans of the specified specifications that you purchased. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. Then, the certificate authority (CA) will review your certificate application.
        
        @param request: CreateCertificateRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateRequestResponse
        """
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
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using extended certificate services.
        
        @description    You can call this operation to apply for only DV certificates. If you want to apply for an organization validated (OV) or extended validation (EV) certificate, we recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation. This operation allows you to apply for certificates of all specifications and specify the method to generate a certificate signing request (CSR) file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455803.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications have been submitted, and the number of times that certificates have been issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, Certificate Management Service automatically creates a CSR file for your application and consumes the certificate quota in the certificate resource plans of the specified specifications that you purchased. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. Then, the certificate authority (CA) will review your certificate application.
        
        @param request: CreateCertificateRequestRequest
        @return: CreateCertificateRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_request_with_options(request, runtime)

    async def create_certificate_request_async(
        self,
        request: cas_20200407_models.CreateCertificateRequestRequest,
    ) -> cas_20200407_models.CreateCertificateRequestResponse:
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using extended certificate services.
        
        @description    You can call this operation to apply for only DV certificates. If you want to apply for an organization validated (OV) or extended validation (EV) certificate, we recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation. This operation allows you to apply for certificates of all specifications and specify the method to generate a certificate signing request (CSR) file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/455803.html) operation to query the usage of certificate resource plans of specified specifications, including the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications have been submitted, and the number of times that certificates have been issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, Certificate Management Service automatically creates a CSR file for your application and consumes the certificate quota in the certificate resource plans of the specified specifications that you purchased. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. Then, the certificate authority (CA) will review your certificate application.
        
        @param request: CreateCertificateRequestRequest
        @return: CreateCertificateRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_request_with_options_async(request, runtime)

    def create_certificate_with_csr_request_with_options(
        self,
        request: cas_20200407_models.CreateCertificateWithCsrRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCertificateWithCsrRequestResponse:
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using a custom certificate signing request (CSR) file. You can use extended certificate services to purchase and apply for a DV certificate with a few clicks.
        
        @description    You can call the CreateCertificateWithCsrRequest operation to apply only for DV certificates. We recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation to submit a certificate application. This operation allows you to apply for certificates of all specifications and specify the method to generate a CSR file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/164110.html) operation to query the usage of certificate resource plans of specified specifications. The usage information includes the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications are submitted, and the number of times that certificates are issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, the certificate quota of the required specifications that you purchased is consumed. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. The certificate authority (CA) starts to review your certificate application only after the domain name verification is complete.
        
        @param request: CreateCertificateWithCsrRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateWithCsrRequestResponse
        """
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
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using a custom certificate signing request (CSR) file. You can use extended certificate services to purchase and apply for a DV certificate with a few clicks.
        
        @description    You can call the CreateCertificateWithCsrRequest operation to apply only for DV certificates. We recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation to submit a certificate application. This operation allows you to apply for certificates of all specifications and specify the method to generate a CSR file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/164110.html) operation to query the usage of certificate resource plans of specified specifications. The usage information includes the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications are submitted, and the number of times that certificates are issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, the certificate quota of the required specifications that you purchased is consumed. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. The certificate authority (CA) starts to review your certificate application only after the domain name verification is complete.
        
        @param request: CreateCertificateWithCsrRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateWithCsrRequestResponse
        """
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
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using a custom certificate signing request (CSR) file. You can use extended certificate services to purchase and apply for a DV certificate with a few clicks.
        
        @description    You can call the CreateCertificateWithCsrRequest operation to apply only for DV certificates. We recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation to submit a certificate application. This operation allows you to apply for certificates of all specifications and specify the method to generate a CSR file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/164110.html) operation to query the usage of certificate resource plans of specified specifications. The usage information includes the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications are submitted, and the number of times that certificates are issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, the certificate quota of the required specifications that you purchased is consumed. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. The certificate authority (CA) starts to review your certificate application only after the domain name verification is complete.
        
        @param request: CreateCertificateWithCsrRequestRequest
        @return: CreateCertificateWithCsrRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_csr_request_with_options(request, runtime)

    async def create_certificate_with_csr_request_async(
        self,
        request: cas_20200407_models.CreateCertificateWithCsrRequestRequest,
    ) -> cas_20200407_models.CreateCertificateWithCsrRequestResponse:
        """
        @summary Purchases, applies for, and issues a domain validated (DV) certificate by using a custom certificate signing request (CSR) file. You can use extended certificate services to purchase and apply for a DV certificate with a few clicks.
        
        @description    You can call the CreateCertificateWithCsrRequest operation to apply only for DV certificates. We recommend that you call the [CreateCertificateForPackageRequest](https://help.aliyun.com/document_detail/455296.html) operation to submit a certificate application. This operation allows you to apply for certificates of all specifications and specify the method to generate a CSR file.
        Before you call this operation, make sure that you have purchased a certificate resource plan of the required specifications. For more information about how to purchase a certificate resource plan, see [Purchase a certificate resource plan](https://help.aliyun.com/document_detail/28542.html). You can call the [DescribePackageState](https://help.aliyun.com/document_detail/164110.html) operation to query the usage of certificate resource plans of specified specifications. The usage information includes the total number of purchased certificate resource plans of the specified specifications, the number of times that certificate applications are submitted, and the number of times that certificates are issued.
        When you call this operation, you can use the **ProductCode** parameter to specify the specifications of the certificate.
        After you call this operation to submit a certificate application, the certificate quota of the required specifications that you purchased is consumed. After you call this operation, you also need to call the [DescribeCertificateState](https://help.aliyun.com/document_detail/164111.html) operation to obtain the information that is required to complete domain name verification, and manually complete the verification. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on your DNS server. The certificate authority (CA) starts to review your certificate application only after the domain name verification is complete.
        
        @param request: CreateCertificateWithCsrRequestRequest
        @return: CreateCertificateWithCsrRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_with_csr_request_with_options_async(request, runtime)

    def create_csr_with_options(
        self,
        request: cas_20200407_models.CreateCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCsrResponse:
        """
        @param request: CreateCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.corp_name):
            query['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.department):
            query['Department'] = request.department
        if not UtilClient.is_unset(request.key_size):
            query['KeySize'] = request.key_size
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.sans):
            query['Sans'] = request.sans
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCsr',
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
            cas_20200407_models.CreateCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_csr_with_options_async(
        self,
        request: cas_20200407_models.CreateCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateCsrResponse:
        """
        @param request: CreateCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.common_name):
            query['CommonName'] = request.common_name
        if not UtilClient.is_unset(request.corp_name):
            query['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.department):
            query['Department'] = request.department
        if not UtilClient.is_unset(request.key_size):
            query['KeySize'] = request.key_size
        if not UtilClient.is_unset(request.locality):
            query['Locality'] = request.locality
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.province):
            query['Province'] = request.province
        if not UtilClient.is_unset(request.sans):
            query['Sans'] = request.sans
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCsr',
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
            cas_20200407_models.CreateCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_csr(
        self,
        request: cas_20200407_models.CreateCsrRequest,
    ) -> cas_20200407_models.CreateCsrResponse:
        """
        @param request: CreateCsrRequest
        @return: CreateCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_csr_with_options(request, runtime)

    async def create_csr_async(
        self,
        request: cas_20200407_models.CreateCsrRequest,
    ) -> cas_20200407_models.CreateCsrResponse:
        """
        @param request: CreateCsrRequest
        @return: CreateCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_csr_with_options_async(request, runtime)

    def create_deployment_job_with_options(
        self,
        request: cas_20200407_models.CreateDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateDeploymentJobResponse:
        """
        @summary 创建部署任务
        
        @param request: CreateDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeploymentJob',
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
            cas_20200407_models.CreateDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deployment_job_with_options_async(
        self,
        request: cas_20200407_models.CreateDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateDeploymentJobResponse:
        """
        @summary 创建部署任务
        
        @param request: CreateDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeploymentJob',
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
            cas_20200407_models.CreateDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deployment_job(
        self,
        request: cas_20200407_models.CreateDeploymentJobRequest,
    ) -> cas_20200407_models.CreateDeploymentJobResponse:
        """
        @summary 创建部署任务
        
        @param request: CreateDeploymentJobRequest
        @return: CreateDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_deployment_job_with_options(request, runtime)

    async def create_deployment_job_async(
        self,
        request: cas_20200407_models.CreateDeploymentJobRequest,
    ) -> cas_20200407_models.CreateDeploymentJobResponse:
        """
        @summary 创建部署任务
        
        @param request: CreateDeploymentJobRequest
        @return: CreateDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_deployment_job_with_options_async(request, runtime)

    def create_whclient_certificate_with_options(
        self,
        request: cas_20200407_models.CreateWHClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.CreateWHClientCertificateResponse:
        """
        @param request: CreateWHClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWHClientCertificateResponse
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
        """
        @param request: CreateWHClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWHClientCertificateResponse
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
        """
        @param request: CreateWHClientCertificateRequest
        @return: CreateWHClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_whclient_certificate_with_options(request, runtime)

    async def create_whclient_certificate_async(
        self,
        request: cas_20200407_models.CreateWHClientCertificateRequest,
    ) -> cas_20200407_models.CreateWHClientCertificateResponse:
        """
        @param request: CreateWHClientCertificateRequest
        @return: CreateWHClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_whclient_certificate_with_options_async(request, runtime)

    def decrypt_with_options(
        self,
        request: cas_20200407_models.DecryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DecryptResponse:
        """
        @param request: DecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecryptResponse
        """
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
        """
        @param request: DecryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecryptResponse
        """
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
        """
        @param request: DecryptRequest
        @return: DecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.decrypt_with_options(request, runtime)

    async def decrypt_async(
        self,
        request: cas_20200407_models.DecryptRequest,
    ) -> cas_20200407_models.DecryptResponse:
        """
        @param request: DecryptRequest
        @return: DecryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.decrypt_with_options_async(request, runtime)

    def delete_certificate_request_with_options(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        """
        @summary Deletes an order in which the application for a domain validated (DV) certificate failed.
        
        @description You can call this operation to delete a certificate application order only in the following scenarios:
        The status of the order is review failed. You have called the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html)  operation to query the status of the certificate application order and the value of the **Type** parameter is **verify_fail**.
        The status of the order is **pending application**. You have called the [CancelOrderRequest](https://help.aliyun.com/document_detail/455299.html) operation to cancel a certificate application order whose status is pending review or being reviewed. The status of the certificate application order that is canceled in this case changes to **pending application**.
        
        @param request: DeleteCertificateRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCertificateRequestResponse
        """
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
        """
        @summary Deletes an order in which the application for a domain validated (DV) certificate failed.
        
        @description You can call this operation to delete a certificate application order only in the following scenarios:
        The status of the order is review failed. You have called the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html)  operation to query the status of the certificate application order and the value of the **Type** parameter is **verify_fail**.
        The status of the order is **pending application**. You have called the [CancelOrderRequest](https://help.aliyun.com/document_detail/455299.html) operation to cancel a certificate application order whose status is pending review or being reviewed. The status of the certificate application order that is canceled in this case changes to **pending application**.
        
        @param request: DeleteCertificateRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCertificateRequestResponse
        """
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
        """
        @summary Deletes an order in which the application for a domain validated (DV) certificate failed.
        
        @description You can call this operation to delete a certificate application order only in the following scenarios:
        The status of the order is review failed. You have called the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html)  operation to query the status of the certificate application order and the value of the **Type** parameter is **verify_fail**.
        The status of the order is **pending application**. You have called the [CancelOrderRequest](https://help.aliyun.com/document_detail/455299.html) operation to cancel a certificate application order whose status is pending review or being reviewed. The status of the certificate application order that is canceled in this case changes to **pending application**.
        
        @param request: DeleteCertificateRequestRequest
        @return: DeleteCertificateRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_certificate_request_with_options(request, runtime)

    async def delete_certificate_request_async(
        self,
        request: cas_20200407_models.DeleteCertificateRequestRequest,
    ) -> cas_20200407_models.DeleteCertificateRequestResponse:
        """
        @summary Deletes an order in which the application for a domain validated (DV) certificate failed.
        
        @description You can call this operation to delete a certificate application order only in the following scenarios:
        The status of the order is review failed. You have called the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html)  operation to query the status of the certificate application order and the value of the **Type** parameter is **verify_fail**.
        The status of the order is **pending application**. You have called the [CancelOrderRequest](https://help.aliyun.com/document_detail/455299.html) operation to cancel a certificate application order whose status is pending review or being reviewed. The status of the certificate application order that is canceled in this case changes to **pending application**.
        
        @param request: DeleteCertificateRequestRequest
        @return: DeleteCertificateRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_certificate_request_with_options_async(request, runtime)

    def delete_csr_with_options(
        self,
        request: cas_20200407_models.DeleteCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteCsrResponse:
        """
        @param request: DeleteCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCsr',
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
            cas_20200407_models.DeleteCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_csr_with_options_async(
        self,
        request: cas_20200407_models.DeleteCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteCsrResponse:
        """
        @param request: DeleteCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCsr',
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
            cas_20200407_models.DeleteCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_csr(
        self,
        request: cas_20200407_models.DeleteCsrRequest,
    ) -> cas_20200407_models.DeleteCsrResponse:
        """
        @param request: DeleteCsrRequest
        @return: DeleteCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_csr_with_options(request, runtime)

    async def delete_csr_async(
        self,
        request: cas_20200407_models.DeleteCsrRequest,
    ) -> cas_20200407_models.DeleteCsrResponse:
        """
        @param request: DeleteCsrRequest
        @return: DeleteCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_csr_with_options_async(request, runtime)

    def delete_deployment_job_with_options(
        self,
        request: cas_20200407_models.DeleteDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteDeploymentJobResponse:
        """
        @summary 删除部署任务
        
        @param request: DeleteDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeploymentJob',
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
            cas_20200407_models.DeleteDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deployment_job_with_options_async(
        self,
        request: cas_20200407_models.DeleteDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteDeploymentJobResponse:
        """
        @summary 删除部署任务
        
        @param request: DeleteDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeploymentJob',
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
            cas_20200407_models.DeleteDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deployment_job(
        self,
        request: cas_20200407_models.DeleteDeploymentJobRequest,
    ) -> cas_20200407_models.DeleteDeploymentJobResponse:
        """
        @summary 删除部署任务
        
        @param request: DeleteDeploymentJobRequest
        @return: DeleteDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_deployment_job_with_options(request, runtime)

    async def delete_deployment_job_async(
        self,
        request: cas_20200407_models.DeleteDeploymentJobRequest,
    ) -> cas_20200407_models.DeleteDeploymentJobResponse:
        """
        @summary 删除部署任务
        
        @param request: DeleteDeploymentJobRequest
        @return: DeleteDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_deployment_job_with_options_async(request, runtime)

    def delete_pcacert_with_options(
        self,
        request: cas_20200407_models.DeletePCACertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeletePCACertResponse:
        """
        @param request: DeletePCACertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePCACertResponse
        """
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
        """
        @param request: DeletePCACertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePCACertResponse
        """
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
        """
        @param request: DeletePCACertRequest
        @return: DeletePCACertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_pcacert_with_options(request, runtime)

    async def delete_pcacert_async(
        self,
        request: cas_20200407_models.DeletePCACertRequest,
    ) -> cas_20200407_models.DeletePCACertResponse:
        """
        @param request: DeletePCACertRequest
        @return: DeletePCACertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_pcacert_with_options_async(request, runtime)

    def delete_user_certificate_with_options(
        self,
        request: cas_20200407_models.DeleteUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteUserCertificateResponse:
        """
        @summary Deletes an expired or uploaded certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteUserCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserCertificateResponse
        """
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
        """
        @summary Deletes an expired or uploaded certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteUserCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserCertificateResponse
        """
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
        """
        @summary Deletes an expired or uploaded certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteUserCertificateRequest
        @return: DeleteUserCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_certificate_with_options(request, runtime)

    async def delete_user_certificate_async(
        self,
        request: cas_20200407_models.DeleteUserCertificateRequest,
    ) -> cas_20200407_models.DeleteUserCertificateResponse:
        """
        @summary Deletes an expired or uploaded certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: DeleteUserCertificateRequest
        @return: DeleteUserCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_certificate_with_options_async(request, runtime)

    def delete_worker_resource_with_options(
        self,
        request: cas_20200407_models.DeleteWorkerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteWorkerResourceResponse:
        """
        @summary 删除部署任务worker
        
        @param request: DeleteWorkerResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkerResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkerResource',
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
            cas_20200407_models.DeleteWorkerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_worker_resource_with_options_async(
        self,
        request: cas_20200407_models.DeleteWorkerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DeleteWorkerResourceResponse:
        """
        @summary 删除部署任务worker
        
        @param request: DeleteWorkerResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkerResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkerResource',
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
            cas_20200407_models.DeleteWorkerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_worker_resource(
        self,
        request: cas_20200407_models.DeleteWorkerResourceRequest,
    ) -> cas_20200407_models.DeleteWorkerResourceResponse:
        """
        @summary 删除部署任务worker
        
        @param request: DeleteWorkerResourceRequest
        @return: DeleteWorkerResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_worker_resource_with_options(request, runtime)

    async def delete_worker_resource_async(
        self,
        request: cas_20200407_models.DeleteWorkerResourceRequest,
    ) -> cas_20200407_models.DeleteWorkerResourceResponse:
        """
        @summary 删除部署任务worker
        
        @param request: DeleteWorkerResourceRequest
        @return: DeleteWorkerResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_worker_resource_with_options_async(request, runtime)

    def describe_certificate_state_with_options(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        """
        @summary Queries the status of a specified certificate application order.
        
        @description If you do not complete the verification of the domain name ownership after you submit a certificate application, you can call this operation to obtain the information that is required to complete the verification. You can complete the verification of the domain name ownership based on the data returned. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on the DNS server.
        The certificate authority (CA) reviews your certificate application only after you complete the verification of the domain name ownership. After the CA approves your certificate application, the CA issues the certificate. If a certificate is issued, you can call this operation to obtain the CA certificate and private key of the certificate.
        
        @param request: DescribeCertificateStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificateStateResponse
        """
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
        """
        @summary Queries the status of a specified certificate application order.
        
        @description If you do not complete the verification of the domain name ownership after you submit a certificate application, you can call this operation to obtain the information that is required to complete the verification. You can complete the verification of the domain name ownership based on the data returned. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on the DNS server.
        The certificate authority (CA) reviews your certificate application only after you complete the verification of the domain name ownership. After the CA approves your certificate application, the CA issues the certificate. If a certificate is issued, you can call this operation to obtain the CA certificate and private key of the certificate.
        
        @param request: DescribeCertificateStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificateStateResponse
        """
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
        """
        @summary Queries the status of a specified certificate application order.
        
        @description If you do not complete the verification of the domain name ownership after you submit a certificate application, you can call this operation to obtain the information that is required to complete the verification. You can complete the verification of the domain name ownership based on the data returned. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on the DNS server.
        The certificate authority (CA) reviews your certificate application only after you complete the verification of the domain name ownership. After the CA approves your certificate application, the CA issues the certificate. If a certificate is issued, you can call this operation to obtain the CA certificate and private key of the certificate.
        
        @param request: DescribeCertificateStateRequest
        @return: DescribeCertificateStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certificate_state_with_options(request, runtime)

    async def describe_certificate_state_async(
        self,
        request: cas_20200407_models.DescribeCertificateStateRequest,
    ) -> cas_20200407_models.DescribeCertificateStateResponse:
        """
        @summary Queries the status of a specified certificate application order.
        
        @description If you do not complete the verification of the domain name ownership after you submit a certificate application, you can call this operation to obtain the information that is required to complete the verification. You can complete the verification of the domain name ownership based on the data returned. If you use the DNS verification method, you must complete the verification on the management platform of the domain name. If you use the file verification method, you must complete the verification on the DNS server.
        The certificate authority (CA) reviews your certificate application only after you complete the verification of the domain name ownership. After the CA approves your certificate application, the CA issues the certificate. If a certificate is issued, you can call this operation to obtain the CA certificate and private key of the certificate.
        
        @param request: DescribeCertificateStateRequest
        @return: DescribeCertificateStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificate_state_with_options_async(request, runtime)

    def describe_cloud_resource_status_with_options(
        self,
        request: cas_20200407_models.DescribeCloudResourceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeCloudResourceStatusResponse:
        """
        @summary 云产品分组-获取用户资源计数
        
        @param request: DescribeCloudResourceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudResourceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudResourceStatus',
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
            cas_20200407_models.DescribeCloudResourceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cloud_resource_status_with_options_async(
        self,
        request: cas_20200407_models.DescribeCloudResourceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeCloudResourceStatusResponse:
        """
        @summary 云产品分组-获取用户资源计数
        
        @param request: DescribeCloudResourceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCloudResourceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCloudResourceStatus',
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
            cas_20200407_models.DescribeCloudResourceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cloud_resource_status(
        self,
        request: cas_20200407_models.DescribeCloudResourceStatusRequest,
    ) -> cas_20200407_models.DescribeCloudResourceStatusResponse:
        """
        @summary 云产品分组-获取用户资源计数
        
        @param request: DescribeCloudResourceStatusRequest
        @return: DescribeCloudResourceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_resource_status_with_options(request, runtime)

    async def describe_cloud_resource_status_async(
        self,
        request: cas_20200407_models.DescribeCloudResourceStatusRequest,
    ) -> cas_20200407_models.DescribeCloudResourceStatusResponse:
        """
        @summary 云产品分组-获取用户资源计数
        
        @param request: DescribeCloudResourceStatusRequest
        @return: DescribeCloudResourceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_resource_status_with_options_async(request, runtime)

    def describe_deployment_job_with_options(
        self,
        request: cas_20200407_models.DescribeDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeDeploymentJobResponse:
        """
        @summary 获取部署任务详情
        
        @param request: DescribeDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeploymentJob',
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
            cas_20200407_models.DescribeDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployment_job_with_options_async(
        self,
        request: cas_20200407_models.DescribeDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeDeploymentJobResponse:
        """
        @summary 获取部署任务详情
        
        @param request: DescribeDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeploymentJob',
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
            cas_20200407_models.DescribeDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployment_job(
        self,
        request: cas_20200407_models.DescribeDeploymentJobRequest,
    ) -> cas_20200407_models.DescribeDeploymentJobResponse:
        """
        @summary 获取部署任务详情
        
        @param request: DescribeDeploymentJobRequest
        @return: DescribeDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_job_with_options(request, runtime)

    async def describe_deployment_job_async(
        self,
        request: cas_20200407_models.DescribeDeploymentJobRequest,
    ) -> cas_20200407_models.DescribeDeploymentJobResponse:
        """
        @summary 获取部署任务详情
        
        @param request: DescribeDeploymentJobRequest
        @return: DescribeDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployment_job_with_options_async(request, runtime)

    def describe_deployment_job_status_with_options(
        self,
        request: cas_20200407_models.DescribeDeploymentJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeDeploymentJobStatusResponse:
        """
        @summary 查询任务状态
        
        @param request: DescribeDeploymentJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeploymentJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeploymentJobStatus',
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
            cas_20200407_models.DescribeDeploymentJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deployment_job_status_with_options_async(
        self,
        request: cas_20200407_models.DescribeDeploymentJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribeDeploymentJobStatusResponse:
        """
        @summary 查询任务状态
        
        @param request: DescribeDeploymentJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDeploymentJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeploymentJobStatus',
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
            cas_20200407_models.DescribeDeploymentJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deployment_job_status(
        self,
        request: cas_20200407_models.DescribeDeploymentJobStatusRequest,
    ) -> cas_20200407_models.DescribeDeploymentJobStatusResponse:
        """
        @summary 查询任务状态
        
        @param request: DescribeDeploymentJobStatusRequest
        @return: DescribeDeploymentJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_job_status_with_options(request, runtime)

    async def describe_deployment_job_status_async(
        self,
        request: cas_20200407_models.DescribeDeploymentJobStatusRequest,
    ) -> cas_20200407_models.DescribeDeploymentJobStatusResponse:
        """
        @summary 查询任务状态
        
        @param request: DescribeDeploymentJobStatusRequest
        @return: DescribeDeploymentJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployment_job_status_with_options_async(request, runtime)

    def describe_package_state_with_options(
        self,
        request: cas_20200407_models.DescribePackageStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.DescribePackageStateResponse:
        """
        @summary Queries the number and usage of purchased domain validated (DV) certificates.
        
        @param request: DescribePackageStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageStateResponse
        """
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
        """
        @summary Queries the number and usage of purchased domain validated (DV) certificates.
        
        @param request: DescribePackageStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePackageStateResponse
        """
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
        """
        @summary Queries the number and usage of purchased domain validated (DV) certificates.
        
        @param request: DescribePackageStateRequest
        @return: DescribePackageStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_package_state_with_options(request, runtime)

    async def describe_package_state_async(
        self,
        request: cas_20200407_models.DescribePackageStateRequest,
    ) -> cas_20200407_models.DescribePackageStateResponse:
        """
        @summary Queries the number and usage of purchased domain validated (DV) certificates.
        
        @param request: DescribePackageStateRequest
        @return: DescribePackageStateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_package_state_with_options_async(request, runtime)

    def encrypt_with_options(
        self,
        request: cas_20200407_models.EncryptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.EncryptResponse:
        """
        @param request: EncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptResponse
        """
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
        """
        @param request: EncryptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncryptResponse
        """
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
        """
        @param request: EncryptRequest
        @return: EncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.encrypt_with_options(request, runtime)

    async def encrypt_async(
        self,
        request: cas_20200407_models.EncryptRequest,
    ) -> cas_20200407_models.EncryptResponse:
        """
        @param request: EncryptRequest
        @return: EncryptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.encrypt_with_options_async(request, runtime)

    def get_cert_warehouse_quota_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetCertWarehouseQuotaResponse:
        """
        @param request: GetCertWarehouseQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCertWarehouseQuotaResponse
        """
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
        """
        @param request: GetCertWarehouseQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCertWarehouseQuotaResponse
        """
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
        """
        @return: GetCertWarehouseQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cert_warehouse_quota_with_options(runtime)

    async def get_cert_warehouse_quota_async(self) -> cas_20200407_models.GetCertWarehouseQuotaResponse:
        """
        @return: GetCertWarehouseQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cert_warehouse_quota_with_options_async(runtime)

    def get_csr_detail_with_options(
        self,
        request: cas_20200407_models.GetCsrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetCsrDetailResponse:
        """
        @param request: GetCsrDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCsrDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCsrDetail',
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
            cas_20200407_models.GetCsrDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_csr_detail_with_options_async(
        self,
        request: cas_20200407_models.GetCsrDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetCsrDetailResponse:
        """
        @param request: GetCsrDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCsrDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr_id):
            query['CsrId'] = request.csr_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCsrDetail',
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
            cas_20200407_models.GetCsrDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_csr_detail(
        self,
        request: cas_20200407_models.GetCsrDetailRequest,
    ) -> cas_20200407_models.GetCsrDetailResponse:
        """
        @param request: GetCsrDetailRequest
        @return: GetCsrDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_csr_detail_with_options(request, runtime)

    async def get_csr_detail_async(
        self,
        request: cas_20200407_models.GetCsrDetailRequest,
    ) -> cas_20200407_models.GetCsrDetailResponse:
        """
        @param request: GetCsrDetailRequest
        @return: GetCsrDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_csr_detail_with_options_async(request, runtime)

    def get_user_certificate_detail_with_options(
        self,
        request: cas_20200407_models.GetUserCertificateDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.GetUserCertificateDetailResponse:
        """
        @summary Queries the details of a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetUserCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_filter):
            query['CertFilter'] = request.cert_filter
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
        """
        @summary Queries the details of a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetUserCertificateDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserCertificateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_filter):
            query['CertFilter'] = request.cert_filter
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
        """
        @summary Queries the details of a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetUserCertificateDetailRequest
        @return: GetUserCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_certificate_detail_with_options(request, runtime)

    async def get_user_certificate_detail_async(
        self,
        request: cas_20200407_models.GetUserCertificateDetailRequest,
    ) -> cas_20200407_models.GetUserCertificateDetailResponse:
        """
        @summary Queries the details of a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: GetUserCertificateDetailRequest
        @return: GetUserCertificateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_certificate_detail_with_options_async(request, runtime)

    def list_cert_with_options(
        self,
        request: cas_20200407_models.ListCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCertResponse:
        """
        @summary Queries the certificates in a certificate repository.
        
        @description You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
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
        """
        @summary Queries the certificates in a certificate repository.
        
        @description You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
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
        """
        @summary Queries the certificates in a certificate repository.
        
        @description You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListCertRequest
        @return: ListCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cert_with_options(request, runtime)

    async def list_cert_async(
        self,
        request: cas_20200407_models.ListCertRequest,
    ) -> cas_20200407_models.ListCertResponse:
        """
        @summary Queries the certificates in a certificate repository.
        
        @description You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListCertRequest
        @return: ListCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cert_with_options_async(request, runtime)

    def list_cert_warehouse_with_options(
        self,
        request: cas_20200407_models.ListCertWarehouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCertWarehouseResponse:
        """
        @param request: ListCertWarehouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCertWarehouseResponse
        """
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
        """
        @param request: ListCertWarehouseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCertWarehouseResponse
        """
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
        """
        @param request: ListCertWarehouseRequest
        @return: ListCertWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cert_warehouse_with_options(request, runtime)

    async def list_cert_warehouse_async(
        self,
        request: cas_20200407_models.ListCertWarehouseRequest,
    ) -> cas_20200407_models.ListCertWarehouseResponse:
        """
        @param request: ListCertWarehouseRequest
        @return: ListCertWarehouseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cert_warehouse_with_options_async(request, runtime)

    def list_cloud_access_with_options(
        self,
        request: cas_20200407_models.ListCloudAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCloudAccessResponse:
        """
        @summary 云授权ak查询
        
        @param request: ListCloudAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudAccess',
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
            cas_20200407_models.ListCloudAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_access_with_options_async(
        self,
        request: cas_20200407_models.ListCloudAccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCloudAccessResponse:
        """
        @summary 云授权ak查询
        
        @param request: ListCloudAccessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudAccessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudAccess',
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
            cas_20200407_models.ListCloudAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_access(
        self,
        request: cas_20200407_models.ListCloudAccessRequest,
    ) -> cas_20200407_models.ListCloudAccessResponse:
        """
        @summary 云授权ak查询
        
        @param request: ListCloudAccessRequest
        @return: ListCloudAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_access_with_options(request, runtime)

    async def list_cloud_access_async(
        self,
        request: cas_20200407_models.ListCloudAccessRequest,
    ) -> cas_20200407_models.ListCloudAccessResponse:
        """
        @summary 云授权ak查询
        
        @param request: ListCloudAccessRequest
        @return: ListCloudAccessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_access_with_options_async(request, runtime)

    def list_cloud_resources_with_options(
        self,
        request: cas_20200407_models.ListCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCloudResourcesResponse:
        """
        @summary 可选择的资源-查询云资源列表
        
        @param request: ListCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not UtilClient.is_unset(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudResources',
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
            cas_20200407_models.ListCloudResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cloud_resources_with_options_async(
        self,
        request: cas_20200407_models.ListCloudResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCloudResourcesResponse:
        """
        @summary 可选择的资源-查询云资源列表
        
        @param request: ListCloudResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCloudResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_name):
            query['CloudName'] = request.cloud_name
        if not UtilClient.is_unset(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.secret_id):
            query['SecretId'] = request.secret_id
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCloudResources',
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
            cas_20200407_models.ListCloudResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cloud_resources(
        self,
        request: cas_20200407_models.ListCloudResourcesRequest,
    ) -> cas_20200407_models.ListCloudResourcesResponse:
        """
        @summary 可选择的资源-查询云资源列表
        
        @param request: ListCloudResourcesRequest
        @return: ListCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cloud_resources_with_options(request, runtime)

    async def list_cloud_resources_async(
        self,
        request: cas_20200407_models.ListCloudResourcesRequest,
    ) -> cas_20200407_models.ListCloudResourcesResponse:
        """
        @summary 可选择的资源-查询云资源列表
        
        @param request: ListCloudResourcesRequest
        @return: ListCloudResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cloud_resources_with_options_async(request, runtime)

    def list_contact_with_options(
        self,
        request: cas_20200407_models.ListContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListContactResponse:
        """
        @summary 获取联系人列表
        
        @param request: ListContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContact',
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
            cas_20200407_models.ListContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_contact_with_options_async(
        self,
        request: cas_20200407_models.ListContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListContactResponse:
        """
        @summary 获取联系人列表
        
        @param request: ListContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListContact',
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
            cas_20200407_models.ListContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_contact(
        self,
        request: cas_20200407_models.ListContactRequest,
    ) -> cas_20200407_models.ListContactResponse:
        """
        @summary 获取联系人列表
        
        @param request: ListContactRequest
        @return: ListContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_contact_with_options(request, runtime)

    async def list_contact_async(
        self,
        request: cas_20200407_models.ListContactRequest,
    ) -> cas_20200407_models.ListContactResponse:
        """
        @summary 获取联系人列表
        
        @param request: ListContactRequest
        @return: ListContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_contact_with_options_async(request, runtime)

    def list_csr_with_options(
        self,
        request: cas_20200407_models.ListCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCsrResponse:
        """
        @param request: ListCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCsr',
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
            cas_20200407_models.ListCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_csr_with_options_async(
        self,
        request: cas_20200407_models.ListCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListCsrResponse:
        """
        @param request: ListCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algorithm):
            query['Algorithm'] = request.algorithm
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCsr',
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
            cas_20200407_models.ListCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_csr(
        self,
        request: cas_20200407_models.ListCsrRequest,
    ) -> cas_20200407_models.ListCsrResponse:
        """
        @param request: ListCsrRequest
        @return: ListCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_csr_with_options(request, runtime)

    async def list_csr_async(
        self,
        request: cas_20200407_models.ListCsrRequest,
    ) -> cas_20200407_models.ListCsrResponse:
        """
        @param request: ListCsrRequest
        @return: ListCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_csr_with_options_async(request, runtime)

    def list_deployment_job_with_options(
        self,
        request: cas_20200407_models.ListDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListDeploymentJobResponse:
        """
        @summary 获取部署任务列表
        
        @param request: ListDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentJob',
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
            cas_20200407_models.ListDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_job_with_options_async(
        self,
        request: cas_20200407_models.ListDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListDeploymentJobResponse:
        """
        @summary 获取部署任务列表
        
        @param request: ListDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentJob',
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
            cas_20200407_models.ListDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_job(
        self,
        request: cas_20200407_models.ListDeploymentJobRequest,
    ) -> cas_20200407_models.ListDeploymentJobResponse:
        """
        @summary 获取部署任务列表
        
        @param request: ListDeploymentJobRequest
        @return: ListDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_deployment_job_with_options(request, runtime)

    async def list_deployment_job_async(
        self,
        request: cas_20200407_models.ListDeploymentJobRequest,
    ) -> cas_20200407_models.ListDeploymentJobResponse:
        """
        @summary 获取部署任务列表
        
        @param request: ListDeploymentJobRequest
        @return: ListDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_deployment_job_with_options_async(request, runtime)

    def list_deployment_job_cert_with_options(
        self,
        request: cas_20200407_models.ListDeploymentJobCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListDeploymentJobCertResponse:
        """
        @summary 获取部署任务的证书列表
        
        @param request: ListDeploymentJobCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentJobCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentJobCert',
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
            cas_20200407_models.ListDeploymentJobCertResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_job_cert_with_options_async(
        self,
        request: cas_20200407_models.ListDeploymentJobCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListDeploymentJobCertResponse:
        """
        @summary 获取部署任务的证书列表
        
        @param request: ListDeploymentJobCertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentJobCertResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentJobCert',
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
            cas_20200407_models.ListDeploymentJobCertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_job_cert(
        self,
        request: cas_20200407_models.ListDeploymentJobCertRequest,
    ) -> cas_20200407_models.ListDeploymentJobCertResponse:
        """
        @summary 获取部署任务的证书列表
        
        @param request: ListDeploymentJobCertRequest
        @return: ListDeploymentJobCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_deployment_job_cert_with_options(request, runtime)

    async def list_deployment_job_cert_async(
        self,
        request: cas_20200407_models.ListDeploymentJobCertRequest,
    ) -> cas_20200407_models.ListDeploymentJobCertResponse:
        """
        @summary 获取部署任务的证书列表
        
        @param request: ListDeploymentJobCertRequest
        @return: ListDeploymentJobCertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_deployment_job_cert_with_options_async(request, runtime)

    def list_deployment_job_resource_with_options(
        self,
        request: cas_20200407_models.ListDeploymentJobResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListDeploymentJobResourceResponse:
        """
        @summary 部署任务的资源列表
        
        @param request: ListDeploymentJobResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentJobResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentJobResource',
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
            cas_20200407_models.ListDeploymentJobResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployment_job_resource_with_options_async(
        self,
        request: cas_20200407_models.ListDeploymentJobResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListDeploymentJobResourceResponse:
        """
        @summary 部署任务的资源列表
        
        @param request: ListDeploymentJobResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDeploymentJobResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeploymentJobResource',
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
            cas_20200407_models.ListDeploymentJobResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployment_job_resource(
        self,
        request: cas_20200407_models.ListDeploymentJobResourceRequest,
    ) -> cas_20200407_models.ListDeploymentJobResourceResponse:
        """
        @summary 部署任务的资源列表
        
        @param request: ListDeploymentJobResourceRequest
        @return: ListDeploymentJobResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_deployment_job_resource_with_options(request, runtime)

    async def list_deployment_job_resource_async(
        self,
        request: cas_20200407_models.ListDeploymentJobResourceRequest,
    ) -> cas_20200407_models.ListDeploymentJobResourceResponse:
        """
        @summary 部署任务的资源列表
        
        @param request: ListDeploymentJobResourceRequest
        @return: ListDeploymentJobResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_deployment_job_resource_with_options_async(request, runtime)

    def list_user_certificate_order_with_options(
        self,
        request: cas_20200407_models.ListUserCertificateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListUserCertificateOrderResponse:
        """
        @summary Queries the certificates or certificate orders of users.
        
        @description You can call the ListUserCertificateOrder operation to query the certificates or certificate orders of users. If you set OrderType to CERT or UPLOAD, certificates are returned. If you set OrderType to CPACK or BUY, certificate orders are returned.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListUserCertificateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserCertificateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Queries the certificates or certificate orders of users.
        
        @description You can call the ListUserCertificateOrder operation to query the certificates or certificate orders of users. If you set OrderType to CERT or UPLOAD, certificates are returned. If you set OrderType to CPACK or BUY, certificate orders are returned.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListUserCertificateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserCertificateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Queries the certificates or certificate orders of users.
        
        @description You can call the ListUserCertificateOrder operation to query the certificates or certificate orders of users. If you set OrderType to CERT or UPLOAD, certificates are returned. If you set OrderType to CPACK or BUY, certificate orders are returned.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListUserCertificateOrderRequest
        @return: ListUserCertificateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_certificate_order_with_options(request, runtime)

    async def list_user_certificate_order_async(
        self,
        request: cas_20200407_models.ListUserCertificateOrderRequest,
    ) -> cas_20200407_models.ListUserCertificateOrderResponse:
        """
        @summary Queries the certificates or certificate orders of users.
        
        @description You can call the ListUserCertificateOrder operation to query the certificates or certificate orders of users. If you set OrderType to CERT or UPLOAD, certificates are returned. If you set OrderType to CPACK or BUY, certificate orders are returned.
        ## Limits
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: ListUserCertificateOrderRequest
        @return: ListUserCertificateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_certificate_order_with_options_async(request, runtime)

    def list_worker_resource_with_options(
        self,
        request: cas_20200407_models.ListWorkerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListWorkerResourceResponse:
        """
        @summary 查询部署任务worker
        
        @param request: ListWorkerResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkerResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkerResource',
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
            cas_20200407_models.ListWorkerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_worker_resource_with_options_async(
        self,
        request: cas_20200407_models.ListWorkerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.ListWorkerResourceResponse:
        """
        @summary 查询部署任务worker
        
        @param request: ListWorkerResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkerResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cloud_product):
            query['CloudProduct'] = request.cloud_product
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.show_size):
            query['ShowSize'] = request.show_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkerResource',
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
            cas_20200407_models.ListWorkerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_worker_resource(
        self,
        request: cas_20200407_models.ListWorkerResourceRequest,
    ) -> cas_20200407_models.ListWorkerResourceResponse:
        """
        @summary 查询部署任务worker
        
        @param request: ListWorkerResourceRequest
        @return: ListWorkerResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_worker_resource_with_options(request, runtime)

    async def list_worker_resource_async(
        self,
        request: cas_20200407_models.ListWorkerResourceRequest,
    ) -> cas_20200407_models.ListWorkerResourceResponse:
        """
        @summary 查询部署任务worker
        
        @param request: ListWorkerResourceRequest
        @return: ListWorkerResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_worker_resource_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: cas_20200407_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.MoveResourceGroupResponse:
        """
        @summary Move Resource Group
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
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
            cas_20200407_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: cas_20200407_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.MoveResourceGroupResponse:
        """
        @summary Move Resource Group
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
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
            cas_20200407_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: cas_20200407_models.MoveResourceGroupRequest,
    ) -> cas_20200407_models.MoveResourceGroupResponse:
        """
        @summary Move Resource Group
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: cas_20200407_models.MoveResourceGroupRequest,
    ) -> cas_20200407_models.MoveResourceGroupResponse:
        """
        @summary Move Resource Group
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def renew_certificate_order_for_package_request_with_options(
        self,
        request: cas_20200407_models.RenewCertificateOrderForPackageRequestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.RenewCertificateOrderForPackageRequestResponse:
        """
        @summary Submits a renewal application for the certificate order of an issued certificate.
        
        @description You can call this operation to submit a renewal application for a certificate only when the order of the certificate is in the expiring state. After the renewal is complete, a new certificate order whose status is pending application is generated. You must submit a certificate application for the new certificate order and install the new certificate after the new certificate is issued.
        > You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        
        @param request: RenewCertificateOrderForPackageRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewCertificateOrderForPackageRequestResponse
        """
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
        """
        @summary Submits a renewal application for the certificate order of an issued certificate.
        
        @description You can call this operation to submit a renewal application for a certificate only when the order of the certificate is in the expiring state. After the renewal is complete, a new certificate order whose status is pending application is generated. You must submit a certificate application for the new certificate order and install the new certificate after the new certificate is issued.
        > You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        
        @param request: RenewCertificateOrderForPackageRequestRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewCertificateOrderForPackageRequestResponse
        """
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
        """
        @summary Submits a renewal application for the certificate order of an issued certificate.
        
        @description You can call this operation to submit a renewal application for a certificate only when the order of the certificate is in the expiring state. After the renewal is complete, a new certificate order whose status is pending application is generated. You must submit a certificate application for the new certificate order and install the new certificate after the new certificate is issued.
        > You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        
        @param request: RenewCertificateOrderForPackageRequestRequest
        @return: RenewCertificateOrderForPackageRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_certificate_order_for_package_request_with_options(request, runtime)

    async def renew_certificate_order_for_package_request_async(
        self,
        request: cas_20200407_models.RenewCertificateOrderForPackageRequestRequest,
    ) -> cas_20200407_models.RenewCertificateOrderForPackageRequestResponse:
        """
        @summary Submits a renewal application for the certificate order of an issued certificate.
        
        @description You can call this operation to submit a renewal application for a certificate only when the order of the certificate is in the expiring state. After the renewal is complete, a new certificate order whose status is pending application is generated. You must submit a certificate application for the new certificate order and install the new certificate after the new certificate is issued.
        > You can call the [DescribeCertificateState](https://help.aliyun.com/document_detail/455800.html) operation to query the status of a certificate application order. If the value of the *Type** response parameter is **certificate**, the certificate is issued.
        
        @param request: RenewCertificateOrderForPackageRequestRequest
        @return: RenewCertificateOrderForPackageRequestResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_certificate_order_for_package_request_with_options_async(request, runtime)

    def revoke_whclient_certificate_with_options(
        self,
        request: cas_20200407_models.RevokeWHClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.RevokeWHClientCertificateResponse:
        """
        @param request: RevokeWHClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeWHClientCertificateResponse
        """
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
        """
        @param request: RevokeWHClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevokeWHClientCertificateResponse
        """
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
        """
        @param request: RevokeWHClientCertificateRequest
        @return: RevokeWHClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revoke_whclient_certificate_with_options(request, runtime)

    async def revoke_whclient_certificate_async(
        self,
        request: cas_20200407_models.RevokeWHClientCertificateRequest,
    ) -> cas_20200407_models.RevokeWHClientCertificateResponse:
        """
        @param request: RevokeWHClientCertificateRequest
        @return: RevokeWHClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revoke_whclient_certificate_with_options_async(request, runtime)

    def sign_with_options(
        self,
        request: cas_20200407_models.SignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.SignResponse:
        """
        @param request: SignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignResponse
        """
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
        """
        @param request: SignRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SignResponse
        """
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
        """
        @param request: SignRequest
        @return: SignResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sign_with_options(request, runtime)

    async def sign_async(
        self,
        request: cas_20200407_models.SignRequest,
    ) -> cas_20200407_models.SignResponse:
        """
        @param request: SignRequest
        @return: SignResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sign_with_options_async(request, runtime)

    def update_csr_with_options(
        self,
        request: cas_20200407_models.UpdateCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateCsrResponse:
        """
        @param request: UpdateCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr_id):
            query['CsrId'] = request.csr_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCsr',
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
            cas_20200407_models.UpdateCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_csr_with_options_async(
        self,
        request: cas_20200407_models.UpdateCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateCsrResponse:
        """
        @param request: UpdateCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr_id):
            query['CsrId'] = request.csr_id
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCsr',
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
            cas_20200407_models.UpdateCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_csr(
        self,
        request: cas_20200407_models.UpdateCsrRequest,
    ) -> cas_20200407_models.UpdateCsrResponse:
        """
        @param request: UpdateCsrRequest
        @return: UpdateCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_csr_with_options(request, runtime)

    async def update_csr_async(
        self,
        request: cas_20200407_models.UpdateCsrRequest,
    ) -> cas_20200407_models.UpdateCsrResponse:
        """
        @param request: UpdateCsrRequest
        @return: UpdateCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_csr_with_options_async(request, runtime)

    def update_deployment_job_with_options(
        self,
        request: cas_20200407_models.UpdateDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateDeploymentJobResponse:
        """
        @summary 更新部署任务
        
        @param request: UpdateDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentJob',
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
            cas_20200407_models.UpdateDeploymentJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_job_with_options_async(
        self,
        request: cas_20200407_models.UpdateDeploymentJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateDeploymentJobResponse:
        """
        @summary 更新部署任务
        
        @param request: UpdateDeploymentJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_ids):
            query['CertIds'] = request.cert_ids
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentJob',
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
            cas_20200407_models.UpdateDeploymentJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_job(
        self,
        request: cas_20200407_models.UpdateDeploymentJobRequest,
    ) -> cas_20200407_models.UpdateDeploymentJobResponse:
        """
        @summary 更新部署任务
        
        @param request: UpdateDeploymentJobRequest
        @return: UpdateDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_deployment_job_with_options(request, runtime)

    async def update_deployment_job_async(
        self,
        request: cas_20200407_models.UpdateDeploymentJobRequest,
    ) -> cas_20200407_models.UpdateDeploymentJobResponse:
        """
        @summary 更新部署任务
        
        @param request: UpdateDeploymentJobRequest
        @return: UpdateDeploymentJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_deployment_job_with_options_async(request, runtime)

    def update_deployment_job_status_with_options(
        self,
        request: cas_20200407_models.UpdateDeploymentJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateDeploymentJobStatusResponse:
        """
        @summary 更新任务部署任务状态
        
        @param request: UpdateDeploymentJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentJobStatus',
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
            cas_20200407_models.UpdateDeploymentJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deployment_job_status_with_options_async(
        self,
        request: cas_20200407_models.UpdateDeploymentJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateDeploymentJobStatusResponse:
        """
        @summary 更新任务部署任务状态
        
        @param request: UpdateDeploymentJobStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDeploymentJobStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDeploymentJobStatus',
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
            cas_20200407_models.UpdateDeploymentJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deployment_job_status(
        self,
        request: cas_20200407_models.UpdateDeploymentJobStatusRequest,
    ) -> cas_20200407_models.UpdateDeploymentJobStatusResponse:
        """
        @summary 更新任务部署任务状态
        
        @param request: UpdateDeploymentJobStatusRequest
        @return: UpdateDeploymentJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_deployment_job_status_with_options(request, runtime)

    async def update_deployment_job_status_async(
        self,
        request: cas_20200407_models.UpdateDeploymentJobStatusRequest,
    ) -> cas_20200407_models.UpdateDeploymentJobStatusResponse:
        """
        @summary 更新任务部署任务状态
        
        @param request: UpdateDeploymentJobStatusRequest
        @return: UpdateDeploymentJobStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_deployment_job_status_with_options_async(request, runtime)

    def update_worker_resource_status_with_options(
        self,
        request: cas_20200407_models.UpdateWorkerResourceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateWorkerResourceStatusResponse:
        """
        @summary 更新部署任务worker状态
        
        @param request: UpdateWorkerResourceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkerResourceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkerResourceStatus',
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
            cas_20200407_models.UpdateWorkerResourceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_worker_resource_status_with_options_async(
        self,
        request: cas_20200407_models.UpdateWorkerResourceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UpdateWorkerResourceStatusResponse:
        """
        @summary 更新部署任务worker状态
        
        @param request: UpdateWorkerResourceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkerResourceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.worker_id):
            query['WorkerId'] = request.worker_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWorkerResourceStatus',
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
            cas_20200407_models.UpdateWorkerResourceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_worker_resource_status(
        self,
        request: cas_20200407_models.UpdateWorkerResourceStatusRequest,
    ) -> cas_20200407_models.UpdateWorkerResourceStatusResponse:
        """
        @summary 更新部署任务worker状态
        
        @param request: UpdateWorkerResourceStatusRequest
        @return: UpdateWorkerResourceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_worker_resource_status_with_options(request, runtime)

    async def update_worker_resource_status_async(
        self,
        request: cas_20200407_models.UpdateWorkerResourceStatusRequest,
    ) -> cas_20200407_models.UpdateWorkerResourceStatusResponse:
        """
        @summary 更新部署任务worker状态
        
        @param request: UpdateWorkerResourceStatusRequest
        @return: UpdateWorkerResourceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_worker_resource_status_with_options_async(request, runtime)

    def upload_csr_with_options(
        self,
        request: cas_20200407_models.UploadCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadCsrResponse:
        """
        @param request: UploadCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCsr',
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
            cas_20200407_models.UploadCsrResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_csr_with_options_async(
        self,
        request: cas_20200407_models.UploadCsrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadCsrResponse:
        """
        @param request: UploadCsrRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCsrResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.csr):
            query['Csr'] = request.csr
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCsr',
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
            cas_20200407_models.UploadCsrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_csr(
        self,
        request: cas_20200407_models.UploadCsrRequest,
    ) -> cas_20200407_models.UploadCsrResponse:
        """
        @param request: UploadCsrRequest
        @return: UploadCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_csr_with_options(request, runtime)

    async def upload_csr_async(
        self,
        request: cas_20200407_models.UploadCsrRequest,
    ) -> cas_20200407_models.UploadCsrResponse:
        """
        @param request: UploadCsrRequest
        @return: UploadCsrResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_csr_with_options_async(request, runtime)

    def upload_pcacert_with_options(
        self,
        request: cas_20200407_models.UploadPCACertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadPCACertResponse:
        """
        @summary The private key of the certificate.
        
        @description The unique identifier of the certificate.
        
        @param request: UploadPCACertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadPCACertResponse
        """
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
        """
        @summary The private key of the certificate.
        
        @description The unique identifier of the certificate.
        
        @param request: UploadPCACertRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadPCACertResponse
        """
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
        """
        @summary The private key of the certificate.
        
        @description The unique identifier of the certificate.
        
        @param request: UploadPCACertRequest
        @return: UploadPCACertResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_pcacert_with_options(request, runtime)

    async def upload_pcacert_async(
        self,
        request: cas_20200407_models.UploadPCACertRequest,
    ) -> cas_20200407_models.UploadPCACertResponse:
        """
        @summary The private key of the certificate.
        
        @description The unique identifier of the certificate.
        
        @param request: UploadPCACertRequest
        @return: UploadPCACertResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_pcacert_with_options_async(request, runtime)

    def upload_user_certificate_with_options(
        self,
        request: cas_20200407_models.UploadUserCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.UploadUserCertificateResponse:
        """
        @summary Uploads a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UploadUserCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadUserCertificateResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Uploads a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UploadUserCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadUserCertificateResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        @summary Uploads a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UploadUserCertificateRequest
        @return: UploadUserCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_user_certificate_with_options(request, runtime)

    async def upload_user_certificate_async(
        self,
        request: cas_20200407_models.UploadUserCertificateRequest,
    ) -> cas_20200407_models.UploadUserCertificateResponse:
        """
        @summary Uploads a certificate.
        
        @description You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        
        @param request: UploadUserCertificateRequest
        @return: UploadUserCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_user_certificate_with_options_async(request, runtime)

    def verify_with_options(
        self,
        request: cas_20200407_models.VerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cas_20200407_models.VerifyResponse:
        """
        @param request: VerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyResponse
        """
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
        """
        @param request: VerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyResponse
        """
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
        """
        @param request: VerifyRequest
        @return: VerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_with_options(request, runtime)

    async def verify_async(
        self,
        request: cas_20200407_models.VerifyRequest,
    ) -> cas_20200407_models.VerifyResponse:
        """
        @param request: VerifyRequest
        @return: VerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_with_options_async(request, runtime)
