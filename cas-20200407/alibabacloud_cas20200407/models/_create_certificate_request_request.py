# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200407 import models as main_models
from darabonba.model import DaraModel

class CreateCertificateRequestRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        email: str = None,
        phone: str = None,
        product_code: str = None,
        tags: List[main_models.CreateCertificateRequestRequestTags] = None,
        username: str = None,
        validate_type: str = None,
    ):
        # The domain name that you want to bind to the certificate. You can specify only one domain name.
        # 
        # >  The domain name must match the certificate specifications that you specify for the **ProductCode** parameter. If you apply for a single-domain certificate, you must specify a single domain name for this parameter. If you apply for a wildcard certificate, you must specify a wildcard domain name such as `*.aliyundoc.com` for this parameter.
        # 
        # This parameter is required.
        self.domain = domain
        # The contact email address of the applicant.
        # 
        # This parameter is required.
        self.email = email
        # The phone number of the applicant.
        # 
        # This parameter is required.
        self.phone = phone
        # The specifications of the certificate. Valid values:
        # 
        # *   **digicert-free-1-free** (default): DigiCert single-domain DV certificate, which is free and valid for 3 months.
        # *   **symantec-free-1-free**: DigiCert single-domain DV certificate, which is free and valid for 1 year. This value is available only on the China site (aliyun.com).
        # *   **symantec-dv-1-starter**: DigiCert wildcard DV certificate.
        # *   **geotrust-dv-1-starter**: GeoTrust single-domain DV certificate.
        # *   **geotrust-dv-w-starter**: GeoTrust wildcard DV certificate.
        # *   **globalsign-dv-1-personal**: GlobalSign single-domain DV certificate.
        # *   **globalsign-dv-w-advanced**: GlobalSign wildcard DV certificate.
        self.product_code = product_code
        # The tags.
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
        if self.domain is not None:
            result['Domain'] = self.domain

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
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateCertificateRequestRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('ValidateType') is not None:
            self.validate_type = m.get('ValidateType')

        return self

class CreateCertificateRequestRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. You cannot specify empty strings as tag keys.
        # 
        # The key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        # 
        # >  You must specify at least one of **Tag.N** (**Tag.N.Key** and **Tag.N.Value**).
        self.key = key
        # The tag value. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value cannot exceed 128 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
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

