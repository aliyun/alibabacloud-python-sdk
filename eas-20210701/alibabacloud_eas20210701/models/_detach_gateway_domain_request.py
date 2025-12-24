# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DetachGatewayDomainRequest(DaraModel):
    def __init__(
        self,
        custom_domain: main_models.DetachGatewayDomainRequestCustomDomain = None,
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
            temp_model = main_models.DetachGatewayDomainRequestCustomDomain()
            self.custom_domain = temp_model.from_map(m.get('CustomDomain'))

        return self

class DetachGatewayDomainRequestCustomDomain(DaraModel):
    def __init__(
        self,
        domain: str = None,
        type: str = None,
    ):
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
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

