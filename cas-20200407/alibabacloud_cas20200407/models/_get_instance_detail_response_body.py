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
        certificate_not_before: int = None,
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
        upgrade_status: str = None,
        validation_method: str = None,
        wildcard_domain_count: int = None,
    ):
        # Specifies whether automatic managed renewal is enabled. Valid values:
        # - enable: Enabled.
        # - disable: Disabled.
        self.auto_reissue = auto_reissue
        # The average waiting time for issuing a certificate of this specification. Unit: seconds.
        self.average_waiting_time = average_waiting_time
        # The CA brand. Valid values: WoSign, CFCA, DigiCert, GeoTrust, GlobalSign, vTrus, and Alibaba.
        self.brand = brand
        # The global certificate ID, in the format of certificate ID + "-" + site region ID. This ID is commonly used across Alibaba Cloud services.
        #   --For the China site, the format is certificate ID + "-cn-hangzhou".
        # For the China site, the format is certificate ID + "-ap-southeast-1".
        # For example, if the certificate ID is 123, the CertIdentifier on the China site is "123-cn-hangzhou", and the CertIdentifier on the China site is "123-ap-southeast-1".
        self.cert_identifier = cert_identifier
        # The certificate ID.
        self.certificate_id = certificate_id
        # The name of the instance. When a certificate is issued, this name is used as the default certificate name.
        self.certificate_name = certificate_name
        # The end time of the latest certificate. The value is a UNIX timestamp. This field is empty if no certificate has been issued.
        self.certificate_not_after = certificate_not_after
        self.certificate_not_before = certificate_not_before
        # The revocation time of the latest certificate. The value is a UNIX timestamp.
        self.certificate_revoke_time = certificate_revoke_time
        # The status of the certificate. Valid values:
        # - **issued**: issued.
        # - **revoked**: revoked.
        # - **willExpire**: about to expire.
        # - **expired**: expired.
        self.certificate_status = certificate_status
        # The type of the certificate. Valid values: DV, OV, and EV.
        self.certificate_type = certificate_type
        # The city where the company or organization of the certificate purchaser is located. This field is required when generating a certificate signing request. Default value: Beijing.
        self.city = city
        # The company information ID.
        self.company_id = company_id
        # The list of contact IDs.
        self.contact_id_list = contact_id_list
        # The code of the country or region where the certificate organization is located. For example, CN indicates China, and US indicates the United States. This field is required when generating a certificate signing request. Default value: CN.
        self.country_code = country_code
        # The certificate signing request in PEM format.
        self.csr = csr
        # The list of associated expert service DingTalk groups.
        self.ding_group_list = ding_group_list
        # The domain name bound to the certificate.
        self.domain = domain
        # The list of domain names to be validated.
        self.domain_validation_list = domain_validation_list
        # The number of exact-match domain names.
        self.full_domain_count = full_domain_count
        # The CSR generation method. Valid values:
        # - online: system-generated. The Csr field is ignored.
        # - upload: user-uploaded. The Csr field is required.
        self.generate_csr_method = generate_csr_method
        # The expiration time of the instance. The value is a UNIX timestamp. If no certificate has been issued, this field is empty.
        self.instance_end_time = instance_end_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The start time of the instance. The value is a UNIX timestamp. If no certificate has been issued, this field is empty.
        self.instance_start_time = instance_start_time
        # The instance type. Valid values:
        # - **BUY**: formal certificate.
        # - **TEST**: test certificate.
        self.instance_type = instance_type
        # The certificate algorithm. Valid values:
        # - **RSA_2048**
        # - **RSA_3072**
        # - **RSA_4096**
        # - **ECC_256**
        # - **SM2**.
        self.key_algorithm = key_algorithm
        # The end time of the instance purchase. The value is a UNIX timestamp. You can use this value to determine the purchase duration of the instance.
        self.order_end_time = order_end_time
        # The start time of the instance purchase. The value is a UNIX timestamp. You can use this value to determine the refund time limit.
        self.order_start_time = order_start_time
        # The result returned by the certification authority (CA) during the last certificate operation.
        self.pending_result = pending_result
        # The province or region where the company is located. This field is required when generating a certificate signing request. Default value: Beijing.
        self.province = province
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use the request ID to troubleshoot issues.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The purchased instance specification.
        self.spec = spec
        # The instance status. Valid values:
        # - **inactive**: pending use.
        # - **pending**: under review. The latest certificate is being reviewed.
        # - **willExpire**: the instance is about to expire.
        # - **expired**: the instance has expired.
        # - **refund**: refunded.
        # - **normal**: normal.
        # - **closed**: closed and unavailable.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The upgrade status of the instance. Valid values:
        # 
        # - none: the instance has not been upgraded.
        # 
        # - payed: the instance upgrade has been paid.
        # 
        # - issued: the latest certificate has been issued after the instance upgrade.
        self.upgrade_status = upgrade_status
        # The validation method for the certificate application. Valid values:
        # - DNS: DNS validation, using TXT or CNAME.
        # - HTTP: file-based validation.
        self.validation_method = validation_method
        # The number of wildcard domain names.
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

        if self.certificate_not_before is not None:
            result['CertificateNotBefore'] = self.certificate_not_before

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

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

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

        if m.get('CertificateNotBefore') is not None:
            self.certificate_not_before = m.get('CertificateNotBefore')

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

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

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
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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
        cname_key: str = None,
        domain: str = None,
        root_domain: str = None,
        validation_key: str = None,
        validation_type: str = None,
        validation_value: str = None,
    ):
        # The CNAME record value for verification-free authorization. This field may be empty.
        self.cname = cname
        # The prefix for CNAME validation.
        self.cname_key = cname_key
        # The domain name to be validated.
        self.domain = domain
        # The root domain name.
        self.root_domain = root_domain
        # The host record.
        self.validation_key = validation_key
        # The validation type. Valid values: TXT, HTTP, and CNAME.
        self.validation_type = validation_type
        # The host record value for validation.
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

        if self.cname_key is not None:
            result['CnameKey'] = self.cname_key

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

        if m.get('CnameKey') is not None:
            self.cname_key = m.get('CnameKey')

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
        # The instance ID of the expert service DingTalk group.
        self.ding_group_instance_id = ding_group_instance_id
        # The name of the expert service DingTalk group.
        self.ding_group_name = ding_group_name
        # The type of the expert service DingTalk group. Valid values:
        # - expedite: application assistance.
        # - remote: offline deployment.
        self.ding_group_type = ding_group_type
        # The link to join the expert service DingTalk group.
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

