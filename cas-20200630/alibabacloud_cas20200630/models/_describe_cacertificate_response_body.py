# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class DescribeCACertificateResponseBody(DaraModel):
    def __init__(
        self,
        certificate: main_models.DescribeCACertificateResponseBodyCertificate = None,
        request_id: str = None,
        years: int = None,
    ):
        # The details of the CA certificate.
        self.certificate = certificate
        # The ID of the request.
        self.request_id = request_id
        # The validity period of the CA certificate. Unit: years.
        self.years = years

    def validate(self):
        if self.certificate:
            self.certificate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.years is not None:
            result['Years'] = self.years

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = main_models.DescribeCACertificateResponseBodyCertificate()
            self.certificate = temp_model.from_map(m.get('Certificate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

class DescribeCACertificateResponseBodyCertificate(DaraModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        before_date: int = None,
        ca_cert_chain: str = None,
        cert_issued_count: int = None,
        cert_max_time: int = None,
        cert_remaining_count: int = None,
        cert_total_count: int = None,
        certificate_type: str = None,
        cluster_id: str = None,
        common_name: str = None,
        country_code: str = None,
        crl_day: int = None,
        crl_status: str = None,
        crl_url: str = None,
        full_algorithm: str = None,
        identifier: str = None,
        issuer_type: str = None,
        key_index: int = None,
        key_size: int = None,
        locality: str = None,
        md_5: str = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        resource_group_id: str = None,
        sans: str = None,
        serial_number: str = None,
        sha_2: str = None,
        sign_algorithm: str = None,
        state: str = None,
        status: str = None,
        subject_dn: str = None,
        tags: List[main_models.DescribeCACertificateResponseBodyCertificateTags] = None,
        x_509certificate: str = None,
        years: int = None,
    ):
        # The date when the CA certificate expires. This is a UNIX timestamp. Unit: milliseconds.
        self.after_date = after_date
        # The type of the encryption algorithm of the CA certificate. Valid values:
        # 
        # - **RSA**: The RSA algorithm.
        # 
        # - **ECC**: The ECC algorithm.
        # 
        # - **SM2**: The SM2 algorithm.
        self.algorithm = algorithm
        # The date when the CA certificate was issued. This is a UNIX timestamp. Unit: milliseconds.
        self.before_date = before_date
        # The complete certificate chain.
        self.ca_cert_chain = ca_cert_chain
        # The number of certificates that the private CA instance has issued.
        self.cert_issued_count = cert_issued_count
        self.cert_max_time = cert_max_time
        # The number of remaining certificates that can be issued.
        self.cert_remaining_count = cert_remaining_count
        # The total certificate quota you purchased.
        self.cert_total_count = cert_total_count
        # The type of the CA certificate. Valid values:
        # 
        # - **ROOT**: A root CA certificate.
        # 
        # - **SUB_ROOT**: A subordinate CA certificate.
        self.certificate_type = certificate_type
        # The ID of the hardware security module (HSM) cluster. This parameter is available when the CA is enabled using an HSM.
        self.cluster_id = cluster_id
        # The common name or abbreviation of the organization that is associated with the CA certificate.
        self.common_name = common_name
        # The country code of the organization that is associated with the CA certificate.
        # 
        # For more information about country codes, see the **International codes** section in [Manage company information](https://help.aliyun.com/document_detail/198289.html).
        self.country_code = country_code
        # The validity period of the CRL. Valid values: 1 to 365. Unit: days.
        self.crl_day = crl_day
        # The status of the Certificate Revocation List (CRL).
        self.crl_status = crl_status
        # The CRL URL.
        self.crl_url = crl_url
        # The algorithm and its key length.
        self.full_algorithm = full_algorithm
        # The unique identifier of the CA certificate.
        self.identifier = identifier
        # The issuer of the CA. Valid values:
        # 
        # - local: A private certificate.
        # 
        # - iTrusChina: A compliance CA.
        # 
        # - external: An imported certificate.
        self.issuer_type = issuer_type
        # The index of the key in the HSM. This parameter is available when the CA is enabled using an HSM.
        self.key_index = key_index
        # The key length of the CA certificate.
        self.key_size = key_size
        # The name of the city where the organization associated with the CA certificate is located.
        self.locality = locality
        # The MD5 fingerprint of the CA certificate.
        self.md_5 = md_5
        # The name of the organization that is associated with the CA certificate.
        self.organization = organization
        # The name of the department in the organization that is associated with the CA certificate.
        self.organization_unit = organization_unit
        # The unique identifier of the root CA certificate that issued the CA certificate.
        # 
        # > This parameter is returned only when **CertificateType** is **SUB_ROOT**, which indicates a subordinate CA certificate.
        self.parent_identifier = parent_identifier
        # The ID of the resource group to which the certificate belongs.
        self.resource_group_id = resource_group_id
        # This parameter is deprecated.
        self.sans = sans
        # The serial number of the CA certificate.
        self.serial_number = serial_number
        # The SHA-256 fingerprint of the CA certificate.
        self.sha_2 = sha_2
        # The signature algorithm of the CA certificate.
        self.sign_algorithm = sign_algorithm
        # <props="china">The name of the province, municipality, or autonomous region where the organization associated with the CA certificate is located.
        # <props="intl">The name of the province or state where the organization associated with the CA certificate is located.
        self.state = state
        # The status of the CA certificate. Valid values:
        # 
        # - **ISSUE**: The certificate is issued.
        # 
        # - **REVOKE**: The certificate is revoked.
        self.status = status
        # The subject of the CA certificate. It contains the following information:
        # 
        # - **C**: The country code of the organization.
        # 
        # - **O**: The name of the organization.
        # 
        # - **OU**: The department of the organization.
        # 
        # - **L**: The city where the organization is located.
        # 
        # <props="china">
        # 
        # - **ST**: The province, municipality, or autonomous region where the organization is located.
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # - **ST**: The province or state where the organization is located.
        # 
        # 
        # 
        # 
        # - **CN**: The common name or abbreviation of the organization.
        self.subject_dn = subject_dn
        # The list of tags.
        self.tags = tags
        # The content of the CA certificate.
        self.x_509certificate = x_509certificate
        # The validity period of the CA certificate. Unit: years.
        self.years = years

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_date is not None:
            result['AfterDate'] = self.after_date

        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.before_date is not None:
            result['BeforeDate'] = self.before_date

        if self.ca_cert_chain is not None:
            result['CaCertChain'] = self.ca_cert_chain

        if self.cert_issued_count is not None:
            result['CertIssuedCount'] = self.cert_issued_count

        if self.cert_max_time is not None:
            result['CertMaxTime'] = self.cert_max_time

        if self.cert_remaining_count is not None:
            result['CertRemainingCount'] = self.cert_remaining_count

        if self.cert_total_count is not None:
            result['CertTotalCount'] = self.cert_total_count

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.crl_day is not None:
            result['CrlDay'] = self.crl_day

        if self.crl_status is not None:
            result['CrlStatus'] = self.crl_status

        if self.crl_url is not None:
            result['CrlUrl'] = self.crl_url

        if self.full_algorithm is not None:
            result['FullAlgorithm'] = self.full_algorithm

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.issuer_type is not None:
            result['IssuerType'] = self.issuer_type

        if self.key_index is not None:
            result['KeyIndex'] = self.key_index

        if self.key_size is not None:
            result['KeySize'] = self.key_size

        if self.locality is not None:
            result['Locality'] = self.locality

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.sha_2 is not None:
            result['Sha2'] = self.sha_2

        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.subject_dn is not None:
            result['SubjectDN'] = self.subject_dn

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        if self.years is not None:
            result['Years'] = self.years

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')

        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')

        if m.get('CaCertChain') is not None:
            self.ca_cert_chain = m.get('CaCertChain')

        if m.get('CertIssuedCount') is not None:
            self.cert_issued_count = m.get('CertIssuedCount')

        if m.get('CertMaxTime') is not None:
            self.cert_max_time = m.get('CertMaxTime')

        if m.get('CertRemainingCount') is not None:
            self.cert_remaining_count = m.get('CertRemainingCount')

        if m.get('CertTotalCount') is not None:
            self.cert_total_count = m.get('CertTotalCount')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CrlDay') is not None:
            self.crl_day = m.get('CrlDay')

        if m.get('CrlStatus') is not None:
            self.crl_status = m.get('CrlStatus')

        if m.get('CrlUrl') is not None:
            self.crl_url = m.get('CrlUrl')

        if m.get('FullAlgorithm') is not None:
            self.full_algorithm = m.get('FullAlgorithm')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('IssuerType') is not None:
            self.issuer_type = m.get('IssuerType')

        if m.get('KeyIndex') is not None:
            self.key_index = m.get('KeyIndex')

        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')

        if m.get('Locality') is not None:
            self.locality = m.get('Locality')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Sha2') is not None:
            self.sha_2 = m.get('Sha2')

        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubjectDN') is not None:
            self.subject_dn = m.get('SubjectDN')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeCACertificateResponseBodyCertificateTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

class DescribeCACertificateResponseBodyCertificateTags(DaraModel):
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

