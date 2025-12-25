# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class CreateDomainResponseBody(DaraModel):
    def __init__(
        self,
        domain_info: main_models.CreateDomainResponseBodyDomainInfo = None,
        request_id: str = None,
    ):
        # The information about the domain name that is added.
        self.domain_info = domain_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domain_info:
            self.domain_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_info is not None:
            result['DomainInfo'] = self.domain_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainInfo') is not None:
            temp_model = main_models.CreateDomainResponseBodyDomainInfo()
            self.domain_info = temp_model.from_map(m.get('DomainInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateDomainResponseBodyDomainInfo(DaraModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        domain_id: str = None,
    ):
        # The CNAME that is assigned by WAF to the domain name.
        self.cname = cname
        # The domain name that you added to WAF.
        self.domain = domain
        # The name of the protected object that is generated.
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        return self

