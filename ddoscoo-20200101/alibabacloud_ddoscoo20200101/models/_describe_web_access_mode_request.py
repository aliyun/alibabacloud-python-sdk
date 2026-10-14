# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeWebAccessModeRequest(DaraModel):
    def __init__(
        self,
        domains: List[str] = None,
    ):
        # The domain names of website businesses.
        # 
        # > The domain names must have website forwarding rules configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        # 
        # This parameter is required.
        self.domains = domains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        return self

