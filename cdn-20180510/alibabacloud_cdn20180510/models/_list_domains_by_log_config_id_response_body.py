# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class ListDomainsByLogConfigIdResponseBody(DaraModel):
    def __init__(
        self,
        domains: main_models.ListDomainsByLogConfigIdResponseBodyDomains = None,
        request_id: str = None,
    ):
        self.domains = domains
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            temp_model = main_models.ListDomainsByLogConfigIdResponseBodyDomains()
            self.domains = temp_model.from_map(m.get('Domains'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDomainsByLogConfigIdResponseBodyDomains(DaraModel):
    def __init__(
        self,
        domain: List[str] = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

