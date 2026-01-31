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
        self.current_page = current_page
        self.instance_list = instance_list
        self.request_id = request_id
        self.show_size = show_size
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
        certificate_id: int = None,
        certificate_name: str = None,
        certificate_not_after: int = None,
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
        spec: str = None,
        status: str = None,
        wildcard_domain_count: int = None,
    ):
        self.auto_reissue = auto_reissue
        self.brand = brand
        self.cert_identifier = cert_identifier
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.certificate_not_after = certificate_not_after
        self.certificate_revoke_time = certificate_revoke_time
        self.certificate_status = certificate_status
        self.certificate_type = certificate_type
        self.domain = domain
        self.full_domain_count = full_domain_count
        self.instance_end_time = instance_end_time
        self.instance_id = instance_id
        self.instance_start_time = instance_start_time
        self.instance_type = instance_type
        self.key_algorithm = key_algorithm
        self.order_end_time = order_end_time
        self.order_start_time = order_start_time
        self.pending_result = pending_result
        self.spec = spec
        self.status = status
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

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.certificate_not_after is not None:
            result['CertificateNotAfter'] = self.certificate_not_after

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

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('CertificateNotAfter') is not None:
            self.certificate_not_after = m.get('CertificateNotAfter')

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

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WildcardDomainCount') is not None:
            self.wildcard_domain_count = m.get('WildcardDomainCount')

        return self

