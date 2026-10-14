# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebAccessModeRequest(DaraModel):
    def __init__(
        self,
        access_mode: int = None,
        domain: str = None,
    ):
        # The access mode for website services. Valid values:
        # - **0**: A record
        # - **1**: Anti-DDoS Pro mode
        # - **2**: Back-to-origin mode
        # 
        # This parameter is required.
        self.access_mode = access_mode
        # The domain name of the website service.
        # > The domain name must have forwarding rules configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

