# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListCustomDomainOutput(DaraModel):
    def __init__(
        self,
        custom_domains: List[main_models.CustomDomain] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.custom_domains = custom_domains
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.custom_domains:
            for v1 in self.custom_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['customDomains'] = []
        if self.custom_domains is not None:
            for k1 in self.custom_domains:
                result['customDomains'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_domains = []
        if m.get('customDomains') is not None:
            for k1 in m.get('customDomains'):
                temp_model = main_models.CustomDomain()
                self.custom_domains.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

