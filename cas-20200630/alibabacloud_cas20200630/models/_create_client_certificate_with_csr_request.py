# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class CreateClientCertificateWithCsrRequest(DaraModel):
    def __init__(
        self,
        after_time: int = None,
        algorithm: str = None,
        asynchronous_flag: bool = None,
        before_time: int = None,
        common_name: str = None,
        country: str = None,
        csr: str = None,
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
        tags: List[main_models.CreateClientCertificateWithCsrRequestTags] = None,
        years: int = None,
    ):
        # The expiration time of the client certificate in UNIX timestamp format. Unit: seconds.
        # >The **BeforeTime** and **AfterTime** parameters must both be empty or both be specified.
        self.after_time = after_time
        # The key algorithm of the client certificate. The key algorithm is in the `<encryption algorithm>_<key length>` format. Valid values:
        # 
        # - **RSA_1024**: The signature algorithm is Sha256WithRSA.
        # - **RSA_2048**: The signature algorithm is Sha256WithRSA.
        # - **RSA_4096**: The signature algorithm is Sha256WithRSA.
        # - **ECC_256**: The signature algorithm is Sha256WithECDSA.
        # - **ECC_384**: The signature algorithm is Sha256WithECDSA.
        # - **ECC_512**: The signature algorithm is Sha256WithECDSA.
        # - **SM2_256**: The signature algorithm is SM3WithSM2.
        # 
        # The encryption algorithm of the client certificate must be the same as that of the sub-CA certificate, but the key length can be different. For example, if the key algorithm of the sub-CA certificate is RSA_2048, the key algorithm of the client certificate must be RSA_1024, RSA_2048, or RSA_4096.
        # 
        # >You can call [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) to query the key algorithm of the sub-CA certificate.
        self.algorithm = algorithm
        # The asynchronous processing flag. If the value is "true", the backend service issues the certificate asynchronously.
        # After the request is submitted, you can call the ListClientCertificate operation to obtain the latest certificate.
        self.asynchronous_flag = asynchronous_flag
        # The issuance time of the client certificate in UNIX timestamp format. Default value: the time when you call this operation. Unit: seconds.
        # 
        # >The **BeforeTime** and **AfterTime** parameters must both be empty or both be specified.
        self.before_time = before_time
        # The common name of the certificate. Chinese characters, English characters, and other characters are supported.
        # >If you set the **CsrPemString** parameter, the value of the **CommonName** parameter is determined by the corresponding information in the **CsrPemString** parameter.
        self.common_name = common_name
        # The country code. Example: **CN** or **US**.
        self.country = country
        # The CSR content. You can use OpenSSL or Keytool to generate a CSR. For more information, see [How to create a CSR file](https://help.aliyun.com/document_detail/42218.html).
        # <props="china">You can also create a CSR in the SSL Certificates Service console. For more information, see [Create a CSR](https://help.aliyun.com/document_detail/313297.html).
        self.csr = csr
        # The custom identifier, which serves as a unique key.
        self.custom_identifier = custom_identifier
        # The validity period of the client certificate. Unit: days.
        # The **Days**, **BeforeTime**, and **AfterTime** parameters cannot all be empty. The **BeforeTime** and **AfterTime** parameters must both be empty or both be specified. The following rules apply:
        # 
        # - If you set the **Days** parameter, you can choose to set or not set the **BeforeTime** and **AfterTime** parameters.
        # - If you do not set the **Days** parameter, you must set the **BeforeTime** and **AfterTime** parameters.
        # 
        # >- If you set the **Days**, **BeforeTime**, and **AfterTime** parameters at the same time, the validity period of the client certificate is determined by the value of the **Days** parameter.
        # - The validity period of the client certificate cannot exceed the validity period of the sub-CA certificate. You can call [DescribeCACertificate](https://help.aliyun.com/document_detail/465954.html) to view the validity period of the sub-CA certificate.
        self.days = days
        # Specifies whether to include the Certificate Revocation List (CRL) address. Valid values:
        # 
        # - 0: No.
        # - 1: Yes.
        self.enable_crl = enable_crl
        # Specifies whether to immediately return the digital certificate. Valid values:
        # - **0**: does not return the certificate. This is the default value.
        # - **1**: returns the certificate.
        # - **2**: returns the certificate and its certificate chain.
        self.immediately = immediately
        # The name of the city where the certificate organization is located. Chinese characters, English characters, and other characters are supported.
        # Default value: the name of the city where the sub-CA certificate organization that issues this certificate is located.
        self.locality = locality
        # The certificate validity period. Unit: months.
        self.months = months
        # The organization name. Default value: Alibaba Inc.
        self.organization = organization
        # The organizational unit name. Default value: Aliyun CDN.
        self.organization_unit = organization_unit
        # The unique identifier of the sub-CA certificate that issues this certificate.
        # >You can call [DescribeCACertificateList](https://help.aliyun.com/document_detail/465957.html) to query the unique identifier of the sub-CA certificate.
        self.parent_identifier = parent_identifier
        # The ID of the resource group to which the certificate belongs.
        self.resource_group_id = resource_group_id
        # The type of the Subject Alternative Name (SAN) extension of the client certificate. Valid values:
        # 
        # - **0**: otherName (0): other name.
        # - **1**: rfc822Name (1): RFC 822 name, which is typically an email address.
        # - **2**: dNSName (2): DNS name (domain name).
        # - **3**: x400Address (3): X.400 address, an early email standard address.
        # - **4**: directoryName (4): directory name, which is typically an X.500 distinguished name (DN).
        # - **5**: ediPartyName (5): Electronic Data Interchange (EDI) party name.
        # - **6**: uniformResourceIdentifier (6): Uniform Resource Identifier (URI).
        # - **7**: iPAddress (7): IP address.
        # - **8**: registeredID (8): registered ID (object identifier OID).
        self.san_type = san_type
        # The specific SAN extension information of the client certificate. You can enter multiple values separated by commas (,).
        # 
        # 1. otherName (0): other name
        # 
        # - Example: 1.3.6.1.4.1.311.20.2.3 (OID) + user@domain.com (UPN - User Principal Name)
        # - Description: A custom extension type that typically consists of a specific OID (object identifier) and a corresponding value. In Windows environments, it is commonly used to store UPN (User Principal Name), such as zhangsan@company.com for smart card logon.
        # 
        # 2. rfc822Name (1): RFC 822 name (email address)
        # 
        # - Example: admin@example.com,support@company.cn
        # - Description: An Internet email address that complies with the RFC 822 standard. It is commonly used in S/MIME email signing and encryption certificates to identify the sender or recipient of an email.
        # - dNSName (2): DNS name (domain name)
        # - Example: www.example.com,api.test.cn,*.mydomain.com (wildcard domain name)
        # - Description: The most commonly used type in HTTPS website SSL/TLS certificates. A certificate can contain multiple DNS names through the SAN extension, allowing a single certificate to protect multiple subdomains or completely different domain names.
        # 3. x400Address (3): X.400 address
        # - Example: G=Zhang; S=San; O=Company; PRMD=IT; ADMD=Telecom; C=CN
        # - Description: An early email system address standard with a complex structure that includes attributes such as country (C), administration domain (ADMD), organization (O), surname (S), and given name (G). It is rarely used in modern Internet HTTPS certificates and is mostly found in traditional European government, enterprise, or military communication systems.
        # 4. directoryName (4): directory name
        # - Example: CN=IT Department, OU=Tech, O=Company Ltd, L=Beijing, ST=Beijing, C=CN
        # - Description: A standard X.500 distinguished name (DN). It is typically used to explicitly identify the complete hierarchical information of an organization, department, or entity in a certificate. It is commonly found in enterprise internal root certificates or specific government digital certificates.
        # 5. ediPartyName (5): EDI party name
        # - Example: nameAssigner=GlobalTradeOrg, partyName=SupplierA
        # - Description: Used specifically in the Electronic Data Interchange (EDI) domain. It identifies a specific party in business message exchanges (such as order and invoice transmissions) and typically includes the assigning organization (nameAssigner) and the party name (partyName).
        # 6. uniformResourceIdentifier (6): Uniform Resource Identifier (URI)
        # - Example: http://www.example.com/verify,https://api.test.cn/status
        # - Description: A standard URL format that must include a protocol prefix (such as http:// or https://). It can point to a specific network resource address.
        # 7. iPAddress (7): IP address
        # - Example: 192.168.1.100 (IPv4), 2001:0db8:85a3::8a2e:0370:7334 (IPv6)
        # - Description: Directly binds to a server IP address. It is commonly used for internal systems without domain names, API servers, or specific services that can only be accessed through a public IP address. Note: Public IP certificates typically require strict Organization Validation (OV).
        # 8. registeredID (8): registered ID (object identifier OID)
        # - Example: 1.2.3.4.55.6.5.99, 2.5.29.17
        # - Description: A unique numeric identifier assigned by international standards organizations. It is rarely used directly as a subject name in certificates and is more commonly used as a unique identity code or policy identifier within systems.
        self.san_value = san_value
        # <props="china">The name of the province, municipality, or autonomous region where the certificate organization is located. Chinese characters, English characters, and other characters are supported. Default value: the name of the province, municipality, or autonomous region where the sub-CA certificate organization that issues this certificate is located.
        # <props="intl">The name of the province or state where the certificate organization is located. Chinese characters, English characters, and other characters are supported. Default value: the name of the province or state where the sub-CA certificate organization that issues this certificate is located.
        self.state = state
        # The tag list.
        self.tags = tags
        # The certificate validity period. Unit: years.
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

        if self.asynchronous_flag is not None:
            result['AsynchronousFlag'] = self.asynchronous_flag

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

        if m.get('AsynchronousFlag') is not None:
            self.asynchronous_flag = m.get('AsynchronousFlag')

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
                temp_model = main_models.CreateClientCertificateWithCsrRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Years') is not None:
            self.years = m.get('Years')

        return self

class CreateClientCertificateWithCsrRequestTags(DaraModel):
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

