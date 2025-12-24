# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class AttachGatewayDomainRequest(DaraModel):
    def __init__(
        self,
        custom_domain: main_models.AttachGatewayDomainRequestCustomDomain = None,
    ):
        # The custom domain name information.
        # 
        # This parameter is required.
        self.custom_domain = custom_domain

    def validate(self):
        if self.custom_domain:
            self.custom_domain.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            temp_model = main_models.AttachGatewayDomainRequestCustomDomain()
            self.custom_domain = temp_model.from_map(m.get('CustomDomain'))

        return self

class AttachGatewayDomainRequestCustomDomain(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        domain: str = None,
        type: str = None,
    ):
        # The ID of the SSL certificate bound to the domain name. Obtain the certificate ID after you upload or purchase a certificate in the [Certificate Management Service](https://yundunnext.console.aliyun.com/?spm=5176.2020520163.console-base_help.2.4b3baJixaJixOc\\&p=cas) console.
        self.certificate_id = certificate_id
        # The custom domain name.
        # 
        # This parameter is required.
        self.domain = domain
        # The domain name type.
        # 
        # Valid value:
        # 
        # *   intranet: internal network.
        # *   internet: public network.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

