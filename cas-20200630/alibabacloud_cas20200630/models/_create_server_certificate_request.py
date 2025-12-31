# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateServerCertificateRequest(DaraModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
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
        tags: List[main_models.CreateServerCertificateRequestTags] = None,
        years: int = None,
    ):
        # The expiration time of the server certificate. This value is a UNIX timestamp. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.after_time = after_time
        # The key algorithm of the server certificate. The key algorithm is in the `<Encryption algorithm>_<Key length>` format. Valid values:
        # 
        # *   **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # *   **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # *   **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # *   **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # *   **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the server certificate must be the same as the encryption algorithm of the intermediate CA certificate. The key length can be different. For example, if the key algorithm of the intermediate CA certificate is RSA_2048, the key algorithm of the server certificate must be RSA_1024, RSA_2048, or RSA_4096.
        # 
        # >  You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the key algorithm of an intermediate CA certificate.
        # 
        # This parameter is required.
        self.algorithm = algorithm
        # The issuance time of the server certificate. This value is a UNIX timestamp. The default value is the time when you call this operation. Unit: seconds.
        # 
        # >  The **BeforeTime** and **AfterTime** parameters must be both empty or both specified.
        self.before_time = before_time
        # The name of the certificate user. The user of a server certificate is a server. We recommend that you enter the domain name or IP address of the server.
        # 
        # This parameter is required.
        self.common_name = common_name
        # The code of the country in which the organization is located, such as CN or US.
        self.country = country
        self.custom_identifier = custom_identifier
        # The validity period of the server certificate. Unit: days. You must specify at least one of the **Days**, **BeforeTime**, and **AfterTime** parameters. The **BeforeTime** and **AfterTime** parameters must be both empty or both specified. The following list describes how to specify these parameters:
        # 
        # *   If you specify the **Days** parameter, you can specify both the **BeforeTime** and **AfterTime** parameters or leave them both empty.
        # *   If you do not specify the **Days** parameter, you must specify both the **BeforeTime** and **AfterTime** parameters.
        # 
        # > 
        # 
        # *   If you specify the **Days**, **BeforeTime**, and **AfterTime** parameters together, the validity period of the server certificate is determined by the value of the **Days** parameter.
        # 
        # *   The validity period of the server certificate cannot exceed the validity period of the intermediate CA certificate. You can call the [DescribeCACertificate](https://help.aliyun.com/document_detail/328096.html) operation to query the validity period of an intermediate CA certificate.
        self.days = days
        # The additional domain names and additional IP addresses of the server certificate. After you add additional domain names and additional IP addresses to a certificate, you can apply the certificate to the domain names and IP addresses.
        # 
        # Separate multiple domain names and multiple IP addresses with commas (,).
        self.domain = domain
        # include the CRL address.
        # 
        # - 0- No
        # - 1- Yes
        self.enable_crl = enable_crl
        # Specifies whether to return the certificate. Valid values:
        # 
        # *   **0**: does not return the certificate. This is the default value.
        # *   **1**: returns the certificate.
        # *   **2**: returns the certificate and the certificate chain of the certificate.
        self.immediately = immediately
        # The name of the city in which the organization is located. The value can contain letters. The default value is the name of the city in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.locality = locality
        # The validity period of the server certificate. Unit: months.
        self.months = months
        # The name of the organization. Default value: Alibaba Inc.
        self.organization = organization
        # The name of the department. Default value: Aliyun CDN.
        self.organization_unit = organization_unit
        # The unique identifier of the intermediate CA certificate from which the server certificate is issued.
        # 
        # >  You can call the [DescribeCACertificateList](https://help.aliyun.com/document_detail/328095.html) operation to query the unique identifier of an intermediate CA certificate.
        # 
        # This parameter is required.
        self.parent_identifier = parent_identifier
        self.resource_group_id = resource_group_id
        # The province, municipality, or autonomous region in which the organization is located. The value can contain letters. The default value is the name of the province, municipality, or autonomous region in which the organization is located. The organization is associated with the intermediate CA certificate from which the certificate is issued.
        self.state = state
        self.tags = tags
        # The validity period of the server certificate. Unit: years.
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
                temp_model = main_models.CreateServerCertificateRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

class CreateServerCertificateRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

