# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachGatewayDomainShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_domain_shrink: str = None,
    ):
        # The custom domain name information.
        # 
        # This parameter is required.
        self.custom_domain_shrink = custom_domain_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_domain_shrink is not None:
            result['CustomDomain'] = self.custom_domain_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomDomain') is not None:
            self.custom_domain_shrink = m.get('CustomDomain')

        return self

