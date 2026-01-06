# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListUserCertificateOrderResponseBody(DaraModel):
    def __init__(
        self,
        certificate_order_list: List[main_models.ListUserCertificateOrderResponseBodyCertificateOrderList] = None,
        current_page: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The certificates and orders.
        self.certificate_order_list = certificate_order_list
        # The page number of the returned page.
        self.current_page = current_page
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The number of entries returned per page.
        self.show_size = show_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.certificate_order_list:
            for v1 in self.certificate_order_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertificateOrderList'] = []
        if self.certificate_order_list is not None:
            for k1 in self.certificate_order_list:
                result['CertificateOrderList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_order_list = []
        if m.get('CertificateOrderList') is not None:
            for k1 in m.get('CertificateOrderList'):
                temp_model = main_models.ListUserCertificateOrderResponseBodyCertificateOrderList()
                self.certificate_order_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListUserCertificateOrderResponseBodyCertificateOrderList(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        aliyun_order_id: int = None,
        buy_date: int = None,
        cert_end_time: int = None,
        cert_start_time: int = None,
        cert_type: str = None,
        certificate_id: int = None,
        city: str = None,
        common_name: str = None,
        country: str = None,
        domain: str = None,
        domain_count: int = None,
        domain_type: str = None,
        end_date: str = None,
        expired: bool = None,
        fingerprint: str = None,
        instance_id: str = None,
        issuer: str = None,
        name: str = None,
        order_id: int = None,
        org_name: str = None,
        partner_order_id: str = None,
        product_code: str = None,
        product_name: str = None,
        province: str = None,
        resource_group_id: str = None,
        root_brand: str = None,
        sans: str = None,
        serial_no: str = None,
        sha_2: str = None,
        source_type: str = None,
        start_date: str = None,
        status: str = None,
        trustee_status: str = None,
        upload: bool = None,
        wild_domain_count: int = None,
    ):
        # The algorithm. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.algorithm = algorithm
        # The ID of the Alibaba Cloud order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.aliyun_order_id = aliyun_order_id
        # The time at which the order was placed. Unit: milliseconds. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.buy_date = buy_date
        # The time at which the certificate expires. Unit: milliseconds. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.cert_end_time = cert_end_time
        # The time at which the certificate starts to take effect. Unit: milliseconds. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.cert_start_time = cert_start_time
        # The type of the certificate. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **DV**: domain validated (DV) certificate
        # *   **EV**: extended validation (EV) certificate
        # *   **OV**: organization validated (OV) certificate **FREE**: free certificate, available only on the China site (aliyun.com)
        self.cert_type = cert_type
        # The ID of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.certificate_id = certificate_id
        # The city in which the organization is located. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.city = city
        # The parent domain name of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.common_name = common_name
        # The code of the country in which the organization is located. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.country = country
        # The domain name. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.domain = domain
        # The total number of domain names that can be bound to the certificate. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.domain_count = domain_count
        # The type of the domain name. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **ONE**: single domain name
        # *   **MULTIPLE**: multiple domain names
        # *   **WILDCARD**: single wildcard domain name
        # *   **M_WILDCARD**: multiple wildcard domain names
        # *   **MIX**: hybrid domain name
        self.domain_type = domain_type
        # The time at which the certificate expires. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.end_date = end_date
        # Indicates whether the certificate expires. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.expired = expired
        # The fingerprint of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.fingerprint = fingerprint
        # The ID of the resource.
        self.instance_id = instance_id
        # The issuer of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.issuer = issuer
        # The name of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.name = name
        # The order ID. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.order_id = order_id
        # The name of the organization that is associated with the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.org_name = org_name
        # The ID of the third-party certificate authority (CA) order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.partner_order_id = partner_order_id
        # The specification ID of the order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.product_code = product_code
        # The specification name of the order. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.product_name = product_name
        # The province or autonomous region in which the organization is located. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.province = province
        # The ID of the resource group. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.resource_group_id = resource_group_id
        # The brand of the certificate. Valid values: WoSign, CFCA, DigiCert, and vTrus. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.root_brand = root_brand
        # All domain names that are bound to the certificate. Multiple domain names are separated by commas (,). This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.sans = sans
        # The serial number of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.serial_no = serial_no
        # The SHA-2 value of the certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.sha_2 = sha_2
        # The type of the order. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **cpack**: virtual resource order
        # *   **buy**: purchase order
        self.source_type = source_type
        # The time at which the certificate starts to take effect. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.start_date = start_date
        # The certificate status of the order. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **PAYED**: pending application
        # *   **CHECKING**: reviewing
        # *   **CHECKED_FAIL**: review failed
        # *   **ISSUED**: issued
        # *   **WILLEXPIRED**: about to expire
        # *   **EXPIRED**: expired
        # *   **NOTACTIVATED**: not activated
        # *   **REVOKED**: revoked
        self.status = status
        # The hosting status of the certificate. This parameter is returned only if OrderType is set to CPACK or BUY. Valid values:
        # 
        # *   **unTrustee**: not hosted
        # *   **trustee**: hosted
        self.trustee_status = trustee_status
        # Indicates whether the certificate is an uploaded certificate. This parameter is returned only if OrderType is set to CERT or UPLOAD.
        self.upload = upload
        # The number of wildcard domain names that can be bound to the certificate. This parameter is returned only if OrderType is set to CPACK or BUY.
        self.wild_domain_count = wild_domain_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.aliyun_order_id is not None:
            result['AliyunOrderId'] = self.aliyun_order_id

        if self.buy_date is not None:
            result['BuyDate'] = self.buy_date

        if self.cert_end_time is not None:
            result['CertEndTime'] = self.cert_end_time

        if self.cert_start_time is not None:
            result['CertStartTime'] = self.cert_start_time

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.city is not None:
            result['City'] = self.city

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country is not None:
            result['Country'] = self.country

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.name is not None:
            result['Name'] = self.name

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        if self.partner_order_id is not None:
            result['PartnerOrderId'] = self.partner_order_id

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.province is not None:
            result['Province'] = self.province

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.root_brand is not None:
            result['RootBrand'] = self.root_brand

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no

        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.trustee_status is not None:
            result['TrusteeStatus'] = self.trustee_status

        if self.upload is not None:
            result['Upload'] = self.upload

        if self.wild_domain_count is not None:
            result['WildDomainCount'] = self.wild_domain_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('AliyunOrderId') is not None:
            self.aliyun_order_id = m.get('AliyunOrderId')

        if m.get('BuyDate') is not None:
            self.buy_date = m.get('BuyDate')

        if m.get('CertEndTime') is not None:
            self.cert_end_time = m.get('CertEndTime')

        if m.get('CertStartTime') is not None:
            self.cert_start_time = m.get('CertStartTime')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        if m.get('PartnerOrderId') is not None:
            self.partner_order_id = m.get('PartnerOrderId')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RootBrand') is not None:
            self.root_brand = m.get('RootBrand')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')

        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrusteeStatus') is not None:
            self.trustee_status = m.get('TrusteeStatus')

        if m.get('Upload') is not None:
            self.upload = m.get('Upload')

        if m.get('WildDomainCount') is not None:
            self.wild_domain_count = m.get('WildDomainCount')

        return self

