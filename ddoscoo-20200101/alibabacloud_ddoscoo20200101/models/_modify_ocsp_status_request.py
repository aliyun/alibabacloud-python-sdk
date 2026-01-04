# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOcspStatusRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enable: int = None,
    ):
        # The domain name for which you want to configure the Static Page Caching policy.
        # 
        # > You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all the domain names that are added to Anti-DDoS Pro or Anti-DDoS Premium.
        # 
        # This parameter is required.
        self.domain = domain
        # Specifies whether to enable the OCSP feature. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        # 
        # This parameter is required.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable is not None:
            result['Enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        return self

