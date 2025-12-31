# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class DescribeCACertificateListResponseBody(DaraModel):
    def __init__(
        self,
        certificate_list: List[main_models.DescribeCACertificateListResponseBodyCertificateList] = None,
        current_page: int = None,
        page_count: int = None,
        request_id: str = None,
        show_size: int = None,
        total_count: int = None,
    ):
        # The details about the CA certificates.
        self.certificate_list = certificate_list
        # The page number of the returned page.
        self.current_page = current_page
        # The number of returned pages.
        self.page_count = page_count
        # The ID of the request.
        self.request_id = request_id
        # The number of CA certificates returned per page.
        self.show_size = show_size
        # The total number of root CA certificates and intermediate CA certificates that are returned.
        self.total_count = total_count

    def validate(self):
        if self.certificate_list:
            for v1 in self.certificate_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertificateList'] = []
        if self.certificate_list is not None:
            for k1 in self.certificate_list:
                result['CertificateList'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_list = []
        if m.get('CertificateList') is not None:
            for k1 in m.get('CertificateList'):
                temp_model = main_models.DescribeCACertificateListResponseBodyCertificateList()
                self.certificate_list.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCACertificateListResponseBodyCertificateList(DaraModel):
    def __init__(
        self,
        after_date: int = None,
        algorithm: str = None,
        alias: str = None,
        before_date: int = None,
        certificate_type: str = None,
        common_name: str = None,
        country_code: str = None,
        gift: int = None,
        identifier: str = None,
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
        trial: int = None,
        x_509certificate: str = None,
        years: int = None,
    ):
        # The expiration date of the CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.after_date = after_date
        # The encryption algorithm of the CA certificate. Valid values:
        # 
        # *   **RSA**: the Rivest-Shamir-Adleman (RSA) algorithm.
        # *   **ECC**: the elliptic curve cryptography (ECC) algorithm.
        # *   **SM2**: the SM2 algorithm, which is developed and approved by the State Cryptography Administration of China.
        self.algorithm = algorithm
        # The alias of the CA.
        self.alias = alias
        # The issuance date of the CA certificate. This value is a UNIX timestamp. Unit: milliseconds.
        self.before_date = before_date
        # The type of the CA certificate. Valid values:
        # 
        # *   **ROOT**: a root CA certificate.
        # *   **SUB_ROOT**: an intermediate CA certificate.
        self.certificate_type = certificate_type
        # The common name or abbreviation of the organization that is associated with the CA certificate.
        self.common_name = common_name
        # The code of the country in which the organization is located.
        # 
        # For more information about country codes, see the **"Country codes"** section of the [Manage company profiles](https://help.aliyun.com/document_detail/198289.html) topic.
        self.country_code = country_code
        self.gift = gift
        # The unique identifier of the CA certificate.
        self.identifier = identifier
        # The key length of the CA certificate.
        self.key_size = key_size
        # The name of the city in which the organization is located.
        self.locality = locality
        # The MD5 fingerprint of the CA certificate.
        self.md_5 = md_5
        # The name of the organization that is associated with the CA certificate.
        self.organization = organization
        # The name of the department or branch in the organization that is associated with the CA certificate.
        self.organization_unit = organization_unit
        # The unique identifier of the root CA certificate from which the CA certificate is issued.
        # 
        # >  This parameter is returned only if the value of the **CertificateType** parameter is **SUB_ROOT**. The value SUB_ROOT indicates an intermediate CA certificate.
        self.parent_identifier = parent_identifier
        self.resource_group_id = resource_group_id
        # This parameter is deprecated.
        self.sans = sans
        # The serial number of the CA certificate.
        self.serial_number = serial_number
        # The SHA-256 fingerprint of the CA certificate.
        self.sha_2 = sha_2
        # The signature algorithm of the CA certificate.
        self.sign_algorithm = sign_algorithm
        # The name of the province, municipality, or autonomous region in which the organization is located.
        self.state = state
        # The status of the CA certificate. Valid values:
        # 
        # *   **ISSUE**: The CA certificate is issued.
        # *   **REVOKE**: The CA certificate is revoked.
        self.status = status
        # The Distinguished Name (DN) attribute of the CA certificate, which indicates the user information of the certificate. The DN attribute contains the following information:
        # 
        # *   **C**: the code of the country in which the organization is located.
        # *   **O**: the name of the organization.
        # *   **OU**: the name of the department or branch in the organization.
        # *   **L**: the name of the city in which the organization is located.
        # *   **CN**: the common name or abbreviation of the organization.
        self.subject_dn = subject_dn
        self.trial = trial
        # The content of the CA certificate.
        self.x_509certificate = x_509certificate
        # The validity period of the CA certificate. Unit: years.
        self.years = years

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_date is not None:
            result['AfterDate'] = self.after_date

        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.alias is not None:
            result['Alias'] = self.alias

        if self.before_date is not None:
            result['BeforeDate'] = self.before_date

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.gift is not None:
            result['Gift'] = self.gift

        if self.identifier is not None:
            result['Identifier'] = self.identifier

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

        if self.trial is not None:
            result['Trial'] = self.trial

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

        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('Gift') is not None:
            self.gift = m.get('Gift')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

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

        if m.get('Trial') is not None:
            self.trial = m.get('Trial')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

