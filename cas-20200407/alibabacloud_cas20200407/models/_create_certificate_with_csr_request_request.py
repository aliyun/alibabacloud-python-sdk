# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class CreateCertificateWithCsrRequestRequest(DaraModel):
    def __init__(
        self,
        csr: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        tags: List[main_models.CreateCertificateWithCsrRequestRequestTags] = None,
        username: str = None,
        validate_type: str = None,
    ):
        # The content of the CSR file.\\
        # The key algorithm in the CSR file must be Rivest-Shamir-Adleman (RSA) or elliptic-curve cryptography (ECC), and the key length of the RSA algorithm must be greater than or equal to 2,048 characters. For more information about how to create a CSR file, see [How do I create a CSR file?](https://help.aliyun.com/document_detail/42218.html)\\
        # A CSR file contains the information about your server and company. When you apply for a certificate, you must submit the CSR file to the CA. The CA signs the CSR file by using the private key of the root certificate and generates a public key file to issue your certificate.
        # 
        # >  The **CN** field in the CSR file specifies the domain name that is bound to the certificate.
        # 
        # This parameter is required.
        self.csr = csr
        # The contact email address of the applicant.
        # 
        # This parameter is required.
        self.email = email
        # The phone number of the applicant.
        # 
        # This parameter is required.
        self.phone = phone
        # The specifications of the certificate that you want to apply for. Valid values:
        # 
        # *   **digicert-free-1-free** (default): DigiCert single-domain DV certificate in a three-month free trial, available only on the China site (aliyun.com).
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate in a one-year free trial, available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        self.product_code = product_code
        # The tag list.
        self.tags = tags
        # The name of the applicant.
        # 
        # This parameter is required.
        self.username = username
        # The method to verify the ownership of a domain name. Valid values:
        # 
        # *   **DNS**: DNS verification. If you use this method, you must add a TXT record to the DNS records of the domain name in the management platform of the domain name. You must have operation permissions on domain name resolution to verify the ownership of the domain name.
        # *   **FILE**: file verification. If you use this method, you must create a specified file on the DNS server. You must have administrative rights on the DNS server to verify the ownership of the domain name.
        # 
        # For more information about the verification methods, see [Verify the ownership of a domain name](https://help.aliyun.com/document_detail/48016.html).
        # 
        # This parameter is required.
        self.validate_type = validate_type

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
        if self.csr is not None:
            result['Csr'] = self.csr

        if self.email is not None:
            result['Email'] = self.email

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.username is not None:
            result['Username'] = self.username

        if self.validate_type is not None:
            result['ValidateType'] = self.validate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Csr') is not None:
            self.csr = m.get('Csr')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateCertificateWithCsrRequestRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')

        return self

class CreateCertificateWithCsrRequestRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag.
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

