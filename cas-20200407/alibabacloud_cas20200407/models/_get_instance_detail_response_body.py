# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class GetInstanceDetailResponseBody(DaraModel):
    def __init__(
        self,
        auto_reissue: str = None,
        average_waiting_time: str = None,
        brand: str = None,
        cert_identifier: str = None,
        certificate_id: int = None,
        certificate_name: str = None,
        certificate_not_after: int = None,
        certificate_revoke_time: int = None,
        certificate_status: str = None,
        certificate_type: str = None,
        city: str = None,
        company_id: int = None,
        contact_id_list: List[int] = None,
        country_code: str = None,
        csr: str = None,
        ding_group_list: List[main_models.GetInstanceDetailResponseBodyDingGroupList] = None,
        domain: str = None,
        domain_validation_list: List[main_models.GetInstanceDetailResponseBodyDomainValidationList] = None,
        full_domain_count: int = None,
        generate_csr_method: str = None,
        instance_end_time: int = None,
        instance_id: str = None,
        instance_start_time: int = None,
        instance_type: str = None,
        key_algorithm: str = None,
        order_end_time: int = None,
        order_start_time: int = None,
        pending_result: str = None,
        province: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[main_models.GetInstanceDetailResponseBodyTags] = None,
        validation_method: str = None,
        wildcard_domain_count: int = None,
    ):
        self.auto_reissue = auto_reissue
        self.average_waiting_time = average_waiting_time
        self.brand = brand
        self.cert_identifier = cert_identifier
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.certificate_not_after = certificate_not_after
        self.certificate_revoke_time = certificate_revoke_time
        self.certificate_status = certificate_status
        self.certificate_type = certificate_type
        self.city = city
        self.company_id = company_id
        self.contact_id_list = contact_id_list
        self.country_code = country_code
        self.csr = csr
        self.ding_group_list = ding_group_list
        self.domain = domain
        self.domain_validation_list = domain_validation_list
        self.full_domain_count = full_domain_count
        self.generate_csr_method = generate_csr_method
        self.instance_end_time = instance_end_time
        self.instance_id = instance_id
        self.instance_start_time = instance_start_time
        self.instance_type = instance_type
        self.key_algorithm = key_algorithm
        self.order_end_time = order_end_time
        self.order_start_time = order_start_time
        self.pending_result = pending_result
        self.province = province
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.spec = spec
        self.status = status
        self.tags = tags
        self.validation_method = validation_method
        self.wildcard_domain_count = wildcard_domain_count

    def validate(self):
        if self.ding_group_list:
            for v1 in self.ding_group_list:
                 if v1:
                    v1.validate()
        if self.domain_validation_list:
            for v1 in self.domain_validation_list:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_reissue is not None:
            result['AutoReissue'] = self.auto_reissue

        if self.average_waiting_time is not None:
            result['AverageWaitingTime'] = self.average_waiting_time

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

        if self.city is not None:
            result['City'] = self.city

        if self.company_id is not None:
            result['CompanyId'] = self.company_id

        if self.contact_id_list is not None:
            result['ContactIdList'] = self.contact_id_list

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.csr is not None:
            result['Csr'] = self.csr

        result['DingGroupList'] = []
        if self.ding_group_list is not None:
            for k1 in self.ding_group_list:
                result['DingGroupList'].append(k1.to_map() if k1 else None)

        if self.domain is not None:
            result['Domain'] = self.domain

        result['DomainValidationList'] = []
        if self.domain_validation_list is not None:
            for k1 in self.domain_validation_list:
                result['DomainValidationList'].append(k1.to_map() if k1 else None)

        if self.full_domain_count is not None:
            result['FullDomainCount'] = self.full_domain_count

        if self.generate_csr_method is not None:
            result['GenerateCsrMethod'] = self.generate_csr_method

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

        if self.province is not None:
            result['Province'] = self.province

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.validation_method is not None:
            result['ValidationMethod'] = self.validation_method

        if self.wildcard_domain_count is not None:
            result['WildcardDomainCount'] = self.wildcard_domain_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReissue') is not None:
            self.auto_reissue = m.get('AutoReissue')

        if m.get('AverageWaitingTime') is not None:
            self.average_waiting_time = m.get('AverageWaitingTime')

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

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')

        if m.get('ContactIdList') is not None:
            self.contact_id_list = m.get('ContactIdList')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        self.ding_group_list = []
        if m.get('DingGroupList') is not None:
            for k1 in m.get('DingGroupList'):
                temp_model = main_models.GetInstanceDetailResponseBodyDingGroupList()
                self.ding_group_list.append(temp_model.from_map(k1))

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        self.domain_validation_list = []
        if m.get('DomainValidationList') is not None:
            for k1 in m.get('DomainValidationList'):
                temp_model = main_models.GetInstanceDetailResponseBodyDomainValidationList()
                self.domain_validation_list.append(temp_model.from_map(k1))

        if m.get('FullDomainCount') is not None:
            self.full_domain_count = m.get('FullDomainCount')

        if m.get('GenerateCsrMethod') is not None:
            self.generate_csr_method = m.get('GenerateCsrMethod')

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

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetInstanceDetailResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ValidationMethod') is not None:
            self.validation_method = m.get('ValidationMethod')

        if m.get('WildcardDomainCount') is not None:
            self.wildcard_domain_count = m.get('WildcardDomainCount')

        return self

class GetInstanceDetailResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class GetInstanceDetailResponseBodyDomainValidationList(DaraModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        root_domain: str = None,
        validation_key: str = None,
        validation_type: str = None,
        validation_value: str = None,
    ):
        self.cname = cname
        self.domain = domain
        self.root_domain = root_domain
        self.validation_key = validation_key
        self.validation_type = validation_type
        self.validation_value = validation_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.root_domain is not None:
            result['RootDomain'] = self.root_domain

        if self.validation_key is not None:
            result['ValidationKey'] = self.validation_key

        if self.validation_type is not None:
            result['ValidationType'] = self.validation_type

        if self.validation_value is not None:
            result['ValidationValue'] = self.validation_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('RootDomain') is not None:
            self.root_domain = m.get('RootDomain')

        if m.get('ValidationKey') is not None:
            self.validation_key = m.get('ValidationKey')

        if m.get('ValidationType') is not None:
            self.validation_type = m.get('ValidationType')

        if m.get('ValidationValue') is not None:
            self.validation_value = m.get('ValidationValue')

        return self

class GetInstanceDetailResponseBodyDingGroupList(DaraModel):
    def __init__(
        self,
        ding_group_instance_id: str = None,
        ding_group_name: str = None,
        ding_group_type: str = None,
        ding_group_url: str = None,
    ):
        self.ding_group_instance_id = ding_group_instance_id
        self.ding_group_name = ding_group_name
        self.ding_group_type = ding_group_type
        self.ding_group_url = ding_group_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ding_group_instance_id is not None:
            result['DingGroupInstanceId'] = self.ding_group_instance_id

        if self.ding_group_name is not None:
            result['DingGroupName'] = self.ding_group_name

        if self.ding_group_type is not None:
            result['DingGroupType'] = self.ding_group_type

        if self.ding_group_url is not None:
            result['DingGroupUrl'] = self.ding_group_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingGroupInstanceId') is not None:
            self.ding_group_instance_id = m.get('DingGroupInstanceId')

        if m.get('DingGroupName') is not None:
            self.ding_group_name = m.get('DingGroupName')

        if m.get('DingGroupType') is not None:
            self.ding_group_type = m.get('DingGroupType')

        if m.get('DingGroupUrl') is not None:
            self.ding_group_url = m.get('DingGroupUrl')

        return self

