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
        auto_reissue_flag: int = None,
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
        deployment_resource_count: int = None,
        deployment_use_count: int = None,
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
        monitor_expand_flag: int = None,
        monitor_use_count: int = None,
        order_end_time: int = None,
        order_progress: str = None,
        order_start_time: int = None,
        pending_result: str = None,
        province: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        spec: str = None,
        status: str = None,
        tags: List[main_models.GetInstanceDetailResponseBodyTags] = None,
        total_deployment_count: int = None,
        total_monitor_count: int = None,
        upgrade_status: str = None,
        validation_method: str = None,
        version_type: str = None,
        wildcard_domain_count: int = None,
    ):
        # Specifies whether automatic hosting is enabled. Valid values:
        # - enable: Enabled.
        # - disable: Disabled.
        self.auto_reissue = auto_reissue
        # Specifies whether the current version includes automatic hosting. Valid values:
        # - 1: Included.
        # - 0: Not included.
        self.auto_reissue_flag = auto_reissue_flag
        # The average waiting time for issuing a certificate of this specification, in seconds.
        self.average_waiting_time = average_waiting_time
        # The CA brand. Valid values: WoSign, CFCA, DigiCert, GeoTrust, GlobalSign, vTrus, and Alibaba.
        self.brand = brand
        # The global certificate ID. The format is Certificate ID + "-" + Site region ID. This ID is commonly used across Alibaba Cloud services.
        # - For the Chinese site, the format is Certificate ID + "-cn-hangzhou".
        # - For the international site, the format is Certificate ID + "-ap-southeast-1".
        # For example, if the certificate ID is 123, the CertIdentifier for the Chinese site is "123-cn-hangzhou", and for the international site, it is "123-ap-southeast-1".
        self.cert_identifier = cert_identifier
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The name of the instance. When a certificate is issued, this name is used as the default name of the certificate.
        self.certificate_name = certificate_name
        # The expiration time of the latest certificate. The value is a UNIX timestamp accurate to seconds. If no certificate is issued, this parameter is empty.
        self.certificate_not_after = certificate_not_after
        # The start time of the latest certificate. The value is a UNIX timestamp accurate to seconds. If no certificate is issued, this parameter is empty.
        self.certificate_not_before = certificate_not_before
        # The revocation time of the latest certificate. The value is a UNIX timestamp accurate to seconds.
        self.certificate_revoke_time = certificate_revoke_time
        # The status of the certificate. Valid values:
        # - **issued**: Issued.
        # - **revoked**: Revoked.
        # - **willExpire**: Expiring soon.
        # - **expired**: Expired.
        self.certificate_status = certificate_status
        # The type of the certificate. Valid values: DV, OV, and EV.
        self.certificate_type = certificate_type
        # The city where the company or organization of the user who purchased the certificate is located. This field is required when generating a CSR. Default value: Beijing.
        self.city = city
        # The ID of the company information.
        self.company_id = company_id
        # The list of contact IDs.
        self.contact_id_list = contact_id_list
        # The code of the country or region where the organization specified in the certificate is located. For example, CN indicates China, and US indicates the United States. This field is required when generating a CSR. Default value: CN.
        self.country_code = country_code
        # The certificate signing request in PEM format.
        self.csr = csr
        # The number of deployed cloud service resources.
        self.deployment_resource_count = deployment_resource_count
        # The used quota for deployment to cloud servers.
        self.deployment_use_count = deployment_use_count
        # The list of associated DingTalk groups for expert services.
        self.ding_group_list = ding_group_list
        # The domain name bound to the certificate.
        self.domain = domain
        # The list of domain names to be validated.
        self.domain_validation_list = domain_validation_list
        # The number of exact domain names.
        self.full_domain_count = full_domain_count
        # The method used to generate the CSR. Valid values:
        # - online: Generated by the system. The Csr field is ignored.
        # - upload: Uploaded by the user. The Csr field is required.
        self.generate_csr_method = generate_csr_method
        # The expiration time of the instance. The value is a UNIX timestamp accurate to seconds. If no certificate has been issued, this parameter is empty.
        self.instance_end_time = instance_end_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The start time of the instance. The value is a UNIX timestamp accurate to seconds. If no certificate has been issued, this parameter is empty.
        self.instance_start_time = instance_start_time
        # The type of the instance. Valid values:
        # - BUY: Official certificate.
        # - TEST: Test certificate.
        self.instance_type = instance_type
        # The algorithm of the certificate. Valid values:
        # - **RSA_2048**
        # - **RSA_3072**
        # - **RSA_4096**
        # - **ECC_256**
        # - **SM2**
        self.key_algorithm = key_algorithm
        # Specifies whether the quota for domain name monitoring can be expanded. Valid values:
        # - 1: Yes.
        # - 0: No.
        self.monitor_expand_flag = monitor_expand_flag
        # The used quota for domain name monitoring.
        self.monitor_use_count = monitor_use_count
        # The end time of the instance purchase. The value is a UNIX timestamp used to determine the purchase duration of the instance.
        self.order_end_time = order_end_time
        # The progress of the order.
        self.order_progress = order_progress
        # The start time of the instance purchase. The value is a UNIX timestamp accurate to seconds, used to determine the time limit for refunds.
        self.order_start_time = order_start_time
        # The result returned by the CA during the last operation on the certificate.
        self.pending_result = pending_result
        # The province or region where the company is located. This field is required when generating a CSR. Default value: Beijing.
        self.province = province
        # The ID of the request. It is a unique identifier generated by Alibaba Cloud for the request and can be used for troubleshooting.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The specifications of the purchased instance.
        self.spec = spec
        # The instance status. Valid values:
        # - **inactive**: Pending use.
        # - **pending**: Under review. The latest certificate is committed for review.
        # - **willExpire**: Expiring soon.
        # - **expired**: Expired.
        # - **refund**: Refunded.
        # - **normal**: Normal.
        # - **closed**: Shutdown and unavailable.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The total quota for deployment to cloud servers.
        self.total_deployment_count = total_deployment_count
        # The total quota for domain name monitoring.
        self.total_monitor_count = total_monitor_count
        # The upgrade status of the instance. Valid values:
        # - none: The instance is not upgraded.
        # - payed: The instance upgrade is paid.
        # - issued: The latest certificate is issued for the instance upgrade.
        self.upgrade_status = upgrade_status
        # The validation method for the certificate application. Valid values:
        # - DNS: DNS validation, using TXT or CNAME records.
        # - HTTP: File validation.
        self.validation_method = validation_method
        # The version type. Valid values:
        # - FOTA: System upgrade.
        # - APP: Application upgrade.
        self.version_type = version_type
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

        if self.auto_reissue_flag is not None:
            result['AutoReissueFlag'] = self.auto_reissue_flag

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

        if self.deployment_resource_count is not None:
            result['DeploymentResourceCount'] = self.deployment_resource_count

        if self.deployment_use_count is not None:
            result['DeploymentUseCount'] = self.deployment_use_count

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

        if self.monitor_expand_flag is not None:
            result['MonitorExpandFlag'] = self.monitor_expand_flag

        if self.monitor_use_count is not None:
            result['MonitorUseCount'] = self.monitor_use_count

        if self.order_end_time is not None:
            result['OrderEndTime'] = self.order_end_time

        if self.order_progress is not None:
            result['OrderProgress'] = self.order_progress

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

        if self.total_deployment_count is not None:
            result['TotalDeploymentCount'] = self.total_deployment_count

        if self.total_monitor_count is not None:
            result['TotalMonitorCount'] = self.total_monitor_count

        if self.upgrade_status is not None:
            result['UpgradeStatus'] = self.upgrade_status

        if self.validation_method is not None:
            result['ValidationMethod'] = self.validation_method

        if self.version_type is not None:
            result['VersionType'] = self.version_type

        if self.wildcard_domain_count is not None:
            result['WildcardDomainCount'] = self.wildcard_domain_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoReissue') is not None:
            self.auto_reissue = m.get('AutoReissue')

        if m.get('AutoReissueFlag') is not None:
            self.auto_reissue_flag = m.get('AutoReissueFlag')

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

        if m.get('DeploymentResourceCount') is not None:
            self.deployment_resource_count = m.get('DeploymentResourceCount')

        if m.get('DeploymentUseCount') is not None:
            self.deployment_use_count = m.get('DeploymentUseCount')

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

        if m.get('MonitorExpandFlag') is not None:
            self.monitor_expand_flag = m.get('MonitorExpandFlag')

        if m.get('MonitorUseCount') is not None:
            self.monitor_use_count = m.get('MonitorUseCount')

        if m.get('OrderEndTime') is not None:
            self.order_end_time = m.get('OrderEndTime')

        if m.get('OrderProgress') is not None:
            self.order_progress = m.get('OrderProgress')

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

        if m.get('TotalDeploymentCount') is not None:
            self.total_deployment_count = m.get('TotalDeploymentCount')

        if m.get('TotalMonitorCount') is not None:
            self.total_monitor_count = m.get('TotalMonitorCount')

        if m.get('UpgradeStatus') is not None:
            self.upgrade_status = m.get('UpgradeStatus')

        if m.get('ValidationMethod') is not None:
            self.validation_method = m.get('ValidationMethod')

        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')

        if m.get('WildcardDomainCount') is not None:
            self.wildcard_domain_count = m.get('WildcardDomainCount')

        return self

class GetInstanceDetailResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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
        # The CNAME record value for verification-free authorization. This parameter may be empty.
        self.cname = cname
        # The prefix used for CNAME validation.
        self.cname_key = cname_key
        # The domain name to be validated.
        self.domain = domain
        # The root domain name.
        self.root_domain = root_domain
        # The host record.
        self.validation_key = validation_key
        # The validation type. Valid values: TXT, HTTP, and CNAME.
        self.validation_type = validation_type
        # The value of the host record for validation.
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
        # The instance ID of the DingTalk group for expert services.
        self.ding_group_instance_id = ding_group_instance_id
        # The name of the DingTalk group for expert services.
        self.ding_group_name = ding_group_name
        # The type of the DingTalk group for expert services. Valid values:
        # - expedite: Application assistance.
        # - remote: Offline deployment.
        self.ding_group_type = ding_group_type
        # The link to join the DingTalk group for expert services.
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

