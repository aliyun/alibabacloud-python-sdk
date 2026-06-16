# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateClientCertificateRequest(DaraModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        alias_name: str = None,
        before_time: int = None,
        client_token: str = None,
        common_name: str = None,
        country: str = None,
        custom_identifier: str = None,
        days: int = None,
        enable_crl: int = None,
        immediately: int = None,
        locality: str = None,
        months: int = None,
        organization: str = None,
        organization_unit: str = None,
        parent_identifier: str = None,
        resource_group_id: str = None,
        san_type: int = None,
        san_value: str = None,
        state: str = None,
        tags: List[main_models.CreateClientCertificateRequestTags] = None,
        years: int = None,
    ):
        # The expiration time of the client certificate in UNIX timestamp format. The unit is seconds.
        # 
        # > **BeforeTime** and **AfterTime** must be specified together or left empty together.
        self.after_time = after_time
        # The key algorithm for the client certificate. The format is `<encryption algorithm>_<key length>`. Valid values:
        # 
        # - **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # 
        # - **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # 
        # - **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # 
        # - **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # 
        # - **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # 
        # - **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # 
        # - **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the client certificate must be the same as the subordinate CA certificate. The key length can be different. For example, if the subordinate CA certificate uses the RSA_2048 key algorithm, the client certificate must use RSA_1024, RSA_2048, or RSA_4096.
        # 
        # > Call [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) to find the key algorithm of the subordinate CA certificate.
        self.algorithm = algorithm
        # Set the name of the issued certificate.
        self.alias_name = alias_name
        # The issuance time of the client certificate in UNIX timestamp format. The unit is seconds. The default value is the time when you call this operation.
        # 
        # > **BeforeTime** and **AfterTime** must be specified together or left empty together.
        self.before_time = before_time
        # Used to ensure request idempotence. The client generates this parameter value, which must be unique across different requests. It can contain a maximum of 64 ASCII characters and must not include any non-ASCII characters.
        self.client_token = client_token
        # The name of the certificate user. For a client authentication (ClientAuth) certificate, the user is typically an individual, a company, an organization, or an application. Specify the common name of the user, such as John Doe, Alibaba, Alibaba Cloud Cryptography Platform, or Tmall Genie.
        self.common_name = common_name
        # The country code. Default: CN.
        self.country = country
        # A custom identifier. This is a unique key.
        self.custom_identifier = custom_identifier
        # The validity period of the client certificate in days. The **Days**, **BeforeTime**, or **AfterTime** parameters cannot all be empty. The **BeforeTime** and **AfterTime** parameters must be set together or left empty. The parameters are configured as follows:
        # 
        # - If you set the **Days** parameter, the **BeforeTime** and **AfterTime** parameters are optional.
        # 
        # - If you do not set the **Days** parameter, you must set both the **BeforeTime** and **AfterTime** parameters.
        # 
        # > * If you set the **Days**, **BeforeTime**, and **AfterTime** parameters, the value of the **Days** parameter takes precedence.
        # 
        # - The validity period of the client certificate cannot exceed the validity period of the subordinate CA certificate. To view the validity period of the subordinate CA certificate, you can call [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html).
        self.days = days
        # Specifies whether to include the Certificate Revocation List (CRL) address.
        # 
        # Valid values: 0 (No) and 1 (Yes).
        self.enable_crl = enable_crl
        # Specifies whether to return the digital certificate immediately.
        # 
        # - **0**: No. This is the default value.
        # 
        # - **1**: Yes, return the certificate.
        # 
        # - **2**: Yes, return the certificate and its certificate chain.
        self.immediately = immediately
        # The name of the city where the organization is located. The default value is the city of the subordinate CA that issues the certificate.
        self.locality = locality
        # The validity period of the certificate in months.
        self.months = months
        # The name of the organization. Default: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default: Alibaba Cloud CDN.
        self.organization_unit = organization_unit
        # The unique identifier of the subordinate CA certificate that issues this certificate.
        # 
        # > Call DescribeCACertificateList to query the unique identifier of the subordinate CA certificate.
        self.parent_identifier = parent_identifier
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of Subject Alternative Name (SAN) extension for the client certificate. Valid values:
        # 
        # - **1**: Email
        # 
        # - **6**: Uniform Resource Identifier (URI)
        self.san_type = san_type
        # The extension information for the client certificate. To enter multiple extensions, separate them with commas (,).
        self.san_value = san_value
        # Specify the province or state of the certificate organization. The value can contain letters. The default value is the province or state of the organization for the intermediate CA that issued the certificate.
        self.state = state
        # A list of tags.
        self.tags = tags
        # The validity period of the certificate in years.
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

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.before_time is not None:
            result['BeforeTime'] = self.before_time

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.country is not None:
            result['Country'] = self.country

        if self.custom_identifier is not None:
            result['CustomIdentifier'] = self.custom_identifier

        if self.days is not None:
            result['Days'] = self.days

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

        if self.san_type is not None:
            result['SanType'] = self.san_type

        if self.san_value is not None:
            result['SanValue'] = self.san_value

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

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('CustomIdentifier') is not None:
            self.custom_identifier = m.get('CustomIdentifier')

        if m.get('Days') is not None:
            self.days = m.get('Days')

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

        if m.get('SanType') is not None:
            self.san_type = m.get('SanType')

        if m.get('SanValue') is not None:
            self.san_value = m.get('SanValue')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateClientCertificateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self



class CreateClientCertificateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

