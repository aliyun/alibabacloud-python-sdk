# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_list: List[main_models.ListInstancesResponseBodyInstanceList] = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The current page number in a paged query.
        self.current_page = current_page
        # The list of instances.
        self.instance_list = instance_list
        # The request ID.
        self.request_id = request_id
        # The number of records per page.
        self.show_size = show_size
        # The total number of instances.
        self.total_count = total_count

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.ListInstancesResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        auto_reissue: str = None,
        brand: str = None,
        cert_identifier: str = None,
        certificate_domain: str = None,
        certificate_id: int = None,
        certificate_name: str = None,
        certificate_not_after: int = None,
        certificate_not_before: int = None,
        certificate_revoke_time: int = None,
        certificate_status: str = None,
        certificate_type: str = None,
        domain: str = None,
        full_domain_count: int = None,
        instance_end_time: int = None,
        instance_id: str = None,
        instance_start_time: int = None,
        instance_type: str = None,
        key_algorithm: str = None,
        order_end_time: int = None,
        order_start_time: int = None,
        pending_result: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        using_product_list: List[str] = None,
        wildcard_domain_count: int = None,
    ):
        # Indicates whether automatic managed renewal is enabled. Valid values:
        # - enable: enabled.
        # - disable: disabled.
        self.auto_reissue = auto_reissue
        # The CA brand. Valid values: WoSign, CFCA, DigiCert, GeoTrust, GlobalSign, vTrus, and Alibaba.
        self.brand = brand
        # The global certificate ID, in the format of certificate ID + "-" + site region ID. This ID is commonly used across Alibaba Cloud services.
        # - For the China site: certificate ID + "-cn-hangzhou"
        # - For the China site: certificate ID + "-ap-southeast-1"
        # 
        # For example, if the certificate ID is 123, the CertIdentifier on the China site is "123-cn-hangzhou", and the CertIdentifier on the International site is "123-ap-southeast-1".
        self.cert_identifier = cert_identifier
        # The domain name of the latest issued certificate.
        self.certificate_domain = certificate_domain
        # The certificate ID.
        self.certificate_id = certificate_id
        # The certificate name.
        self.certificate_name = certificate_name
        # The end time of the latest certificate, in timestamp format. If no certificate has been issued, this field is empty.
        self.certificate_not_after = certificate_not_after
        # The start time of the latest certificate, in timestamp format. If no certificate has been issued, this field is empty.
        self.certificate_not_before = certificate_not_before
        # The revocation time of the latest certificate, in timestamp format.
        self.certificate_revoke_time = certificate_revoke_time
        # The status of the certificate. Valid values:
        # - **issued**: Issued.
        # - **revoked**: Revoked.
        # - **willExpire**: About to expire.
        # - **expired**: Expired.
        self.certificate_status = certificate_status
        # The type of the certificate. Valid values: DV, OV, and EV.
        self.certificate_type = certificate_type
        # The domain name bound to the certificate.
        self.domain = domain
        # The number of exact-match domain names.
        self.full_domain_count = full_domain_count
        # The expiration time of the instance, in timestamp format. If no certificate has been issued, this field is empty.
        self.instance_end_time = instance_end_time
        # The instance ID.
        self.instance_id = instance_id
        # The start time of the instance, in timestamp format. If no certificate has been issued, this field is empty.
        self.instance_start_time = instance_start_time
        # The instance type. Valid values:
        # - BUY: official certificate.
        # - TEST: test certificate.
        self.instance_type = instance_type
        # The certificate algorithm. Default value: RSA_2048. Valid values:
        # - **RSA_2048**
        # - **RSA_3072**
        # - **RSA_4096**
        # - **ECC_256**
        # - **SM2**
        self.key_algorithm = key_algorithm
        # The end time of the instance purchase, in timestamp format. Used to determine the purchase duration of the instance.
        self.order_end_time = order_end_time
        # The start time of the instance purchase, in timestamp format. Used to determine the refund time limit.
        self.order_start_time = order_start_time
        # The result returned by the CA during the last certificate operation.
        self.pending_result = pending_result
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The purchased instance specification.
        self.spec = spec
        # The instance status. Valid values:
        # - **inactive**: pending use.
        # - **pending**: under review. The latest certificate is being reviewed.
        # - **willExpire**: about to expire.
        # - **expired**: expired.
        # - **refund**: refunded.
        # - **normal**: normal.
        # - **closed**: closed and unavailable.
        self.status = status
        # The list of cloud services to which the latest certificate is deployed.
        self.using_product_list = using_product_list
        # The number of wildcard domain names.
        self.wildcard_domain_count = wildcard_domain_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_reissue is not None:
            result['AutoReissue'] = self.auto_reissue

        if self.brand is not None:
            result['Brand'] = self.brand

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.certificate_domain is not None:
            result['CertificateDomain'] = self.certificate_domain

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.certificate_not_after is not None:
            result['CertificateNotAfter'] = self.certificate_not_after

        if self.certificate_not_before is not None:
            result['CertificateNotBefore'] = self.certificate_not_before

        if self.certificate_revoke_time is not None:
            result['CertificateRevokeTime'] = self.certificate_revoke_time

        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.full_domain_count is not None:
            result['FullDomainCount'] = self.full_domain_count

        if self.instance_end_time is not None:
            result['InstanceEndTime'] = self.instance_end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_start_time is not None:
            result['InstanceStartTime'] = self.instance_start_time

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.key_algorithm is not None:
            result['KeyAlgorithm'] = self.key_algorithm

        if self.order_end_time is not None:
            result['OrderEndTime'] = self.order_end_time

        if self.order_start_time is not None:
            result['OrderStartTime'] = self.order_start_time

        if self.pending_result is not None:
            result['PendingResult'] = self.pending_result

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.using_product_list is not None:
            result['UsingProductList'] = self.using_product_list

        if self.wildcard_domain_count is not None:
            result['WildcardDomainCount'] = self.wildcard_domain_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReissue') is not None:
            self.auto_reissue = m.get('AutoReissue')

        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertificateDomain') is not None:
            self.certificate_domain = m.get('CertificateDomain')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('CertificateNotAfter') is not None:
            self.certificate_not_after = m.get('CertificateNotAfter')

        if m.get('CertificateNotBefore') is not None:
            self.certificate_not_before = m.get('CertificateNotBefore')

        if m.get('CertificateRevokeTime') is not None:
            self.certificate_revoke_time = m.get('CertificateRevokeTime')

        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('FullDomainCount') is not None:
            self.full_domain_count = m.get('FullDomainCount')

        if m.get('InstanceEndTime') is not None:
            self.instance_end_time = m.get('InstanceEndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStartTime') is not None:
            self.instance_start_time = m.get('InstanceStartTime')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('KeyAlgorithm') is not None:
            self.key_algorithm = m.get('KeyAlgorithm')

        if m.get('OrderEndTime') is not None:
            self.order_end_time = m.get('OrderEndTime')

        if m.get('OrderStartTime') is not None:
            self.order_start_time = m.get('OrderStartTime')

        if m.get('PendingResult') is not None:
            self.pending_result = m.get('PendingResult')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UsingProductList') is not None:
            self.using_product_list = m.get('UsingProductList')

        if m.get('WildcardDomainCount') is not None:
            self.wildcard_domain_count = m.get('WildcardDomainCount')

        return self

