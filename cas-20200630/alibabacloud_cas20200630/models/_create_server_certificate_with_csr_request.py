# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateServerCertificateWithCsrRequest(DaraModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        csr: str = None,
        custom_identifier: str = None,
        days: int = None,
        domain: str = None,
        enable_crl: int = None,
        immediately: int = None,
        locality: str = None,
        months: int = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        resource_group_id: str = None,
        state: str = None,
        tags: List[main_models.CreateServerCertificateWithCsrRequestTags] = None,
        years: int = None,
    ):
        # Expiration time of the server-side certificate, in UNIX timestamp format. Unit: seconds.
        # 
        # > The **BeforeTime** and **AfterTime** parameters must both be empty or both configured.
        self.after_time = after_time
        # Key algorithm for the server-side certificate. Use the format `<encryption algorithm>_<key length>`. Valid values:
        # 
        # - **RSA_1024**: Signature algorithm is Sha256WithRSA.
        # 
        # - **RSA_2048**: Signature algorithm is Sha256WithRSA.
        # 
        # - **RSA_4096**: Signature algorithm is Sha256WithRSA.
        # 
        # - **ECC_256**: Signature algorithm is Sha256WithECDSA.
        # 
        # - **ECC_384**: Signature algorithm is Sha256WithECDSA.
        # 
        # - **ECC_512**: Signature algorithm is Sha256WithECDSA.
        # 
        # - **SM2_256**: Signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the server-side certificate must match that of the sub-CA certificate. The key length can differ. For example, if the sub-CA certificate uses RSA_2048, the server-side certificate must use RSA_1024, RSA_2048, or RSA_4096.
        # 
        # > Call [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) to check the key algorithm of the sub-CA certificate.
        self.algorithm = algorithm
        # Issue time of the server-side certificate, in UNIX timestamp format. Default: current time when you call this API. Unit: seconds.
        # 
        # > The **BeforeTime** and **AfterTime** parameters must both be empty or both configured.
        self.before_time = before_time
        # Set the common name for the certificate. Supports Chinese, English, and other characters.
        # 
        # > If you set the **Csr** parameter, the value of **CommonName** comes from the corresponding field in the **Csr** parameter.
        self.common_name = common_name
        # The country code. For example, CN or US.
        self.country = country
        # You can generate a CSR using OpenSSL or Keytool. For more information, see [How to create a CSR file](https://help.aliyun.com/document_detail/42218.html).
        # 
        # <props="china">
        # 
        # You can also create a CSR in the SSL Certificate console. For more information, see [Create a CSR](https://help.aliyun.com/document_detail/313297.html).
        # 
        # This parameter is required.
        self.csr = csr
        # A custom identifier. This is a unique key.
        self.custom_identifier = custom_identifier
        # The **Days**, **BeforeTime**, and **AfterTime** parameters cannot all be empty. The **BeforeTime** and **AfterTime** parameters must both be empty or both set. Follow these rules:
        # 
        # - If you set **Days**, you can optionally set **BeforeTime** and **AfterTime**.
        # 
        # - If you do not set **Days**, you must set both **BeforeTime** and **AfterTime**.
        # 
        # > * If you set **Days**, **BeforeTime**, and **AfterTime** together, the validity period uses the value of **Days**.
        # 
        # - The server-side certificate validity period cannot exceed that of the sub-CA certificate. Call [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) to check the sub-CA certificate validity period.
        self.days = days
        # Additional domain names or IP addresses for the server-side certificate. Adding this information lets you apply the certificate to multiple domains or IP addresses.
        # 
        # You can enter multiple domain names and IP addresses. Separate them with commas (,).
        self.domain = domain
        # Specifies whether to include the certificate revocation list (CRL) address.
        # 
        # 0 - No
        # 
        # 1 - Yes
        self.enable_crl = enable_crl
        # Specifies whether to return the digital certificate immediately.
        # 
        # - **0**: Do not return. Default.
        # 
        # - **1**: Return the certificate.
        # 
        # - **2**: Return the certificate and its certificate chain.
        self.immediately = immediately
        # The city where the organization for the certificate is located. The name can contain both Chinese and English characters. By default, this parameter is set to the city of the organization for the issuing subordinate Certificate Authority (CA).
        self.locality = locality
        # The validity period of the certificate, in months.
        self.months = months
        # The name of the organization. Default value: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default value: Alibaba Cloud CDN.
        self.organization_unit = organization_unit
        # Unique identifier of the sub-CA certificate that issues this certificate.
        # 
        # > Call [DescribeCACertificateList](https://help.aliyun.com/document_detail/465957.html) to query the unique identifier of the sub-CA certificate.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # <props="china">Set the name of the province, municipality, or autonomous region where the organization is located. Supports Chinese, English, and other characters. Defaults to the province, municipality, or autonomous region of the issuing sub-CA certificate\\"s organization.
        # <props="intl">Set the name of the state or province where the organization is located. Supports Chinese, English, and other characters. Defaults to the state or province of the issuing sub-CA certificate\\"s organization.
        self.state = state
        # A list of tags.
        self.tags = tags
        # The validity period of the certificate, in years.
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
        if self.after_time is not None:
            result['AfterTime'] = self.after_time

        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.before_time is not None:
            result['BeforeTime'] = self.before_time

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country is not None:
            result['Country'] = self.country

        if self.csr is not None:
            result['Csr'] = self.csr

        if self.custom_identifier is not None:
            result['CustomIdentifier'] = self.custom_identifier

        if self.days is not None:
            result['Days'] = self.days

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable_crl is not None:
            result['EnableCrl'] = self.enable_crl

        if self.immediately is not None:
            result['Immediately'] = self.immediately

        if self.locality is not None:
            result['Locality'] = self.locality

        if self.months is not None:
            result['Months'] = self.months

        if self.organization is not None:
            result['Organization'] = self.organization

        if self.organization_unit is not None:
            result['OrganizationUnit'] = self.organization_unit

        if self.parent_identifier is not None:
            result['ParentIdentifier'] = self.parent_identifier

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.state is not None:
            result['State'] = self.state

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.years is not None:
            result['Years'] = self.years

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterTime') is not None:
            self.after_time = m.get('AfterTime')

        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('CustomIdentifier') is not None:
            self.custom_identifier = m.get('CustomIdentifier')

        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EnableCrl') is not None:
            self.enable_crl = m.get('EnableCrl')

        if m.get('Immediately') is not None:
            self.immediately = m.get('Immediately')

        if m.get('Locality') is not None:
            self.locality = m.get('Locality')

        if m.get('Months') is not None:
            self.months = m.get('Months')

        if m.get('Organization') is not None:
            self.organization = m.get('Organization')

        if m.get('OrganizationUnit') is not None:
            self.organization_unit = m.get('OrganizationUnit')

        if m.get('ParentIdentifier') is not None:
            self.parent_identifier = m.get('ParentIdentifier')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateServerCertificateWithCsrRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

class CreateServerCertificateWithCsrRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

