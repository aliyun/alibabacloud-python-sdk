# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateWebCertRequest(DaraModel):
    def __init__(
        self,
        cert: str = None,
        cert_id: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        cert_region: str = None,
        domain: str = None,
        key: str = None,
    ):
        # The public key of the certificate that you want to associate. This parameter must be used together with the CertName and Key parameters.
        # 
        # >  If you specify a value for the CertName, Cert, and Key parameters, you do not need to specify a value for the CertId parameter.
        self.cert = cert
        # The ID of the certificate.
        # 
        # >  If you specify a certificate ID, you do not need to specify a value for the CertName, Cert, and Key parameters. You can specify only one of this parameter and the CertIdentifier parameter.
        self.cert_id = cert_id
        # The globally unique ID of the certificate. The value is in the "Certificate ID-cn-hangzhou" format. For example, if the ID of the certificate is 123, the value of the CertIdentifier parameter is 123-cn-hangzhou.
        # 
        # >  You can specify only one of this parameter and the CertId parameter.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        # 
        # >  You can specify the name of the certificate that you want to associate. This parameter must be used together with the Cert and Key parameters.
        self.cert_name = cert_name
        # The region of the certificate. Valid values: **cn-hangzhou** and **ap-southeast-1**. Default value: **cn-hangzhou**.
        self.cert_region = cert_region
        # The domain name of the website.
        # 
        # >  A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain
        # The private key of the certificate that you want to associate. This parameter must be used together with the CertName and Cert parameters.
        # 
        # >  If you specify a value for the CertName, Cert, and Key parameters, you do not need to specify a value for the CertId parameter.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert is not None:
            result['Cert'] = self.cert

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_region is not None:
            result['CertRegion'] = self.cert_region

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertRegion') is not None:
            self.cert_region = m.get('CertRegion')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

