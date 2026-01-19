# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DissociateInstanceWithPrivateDNSShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        intranet_domains_shrink: str = None,
        security_token: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The internal domain names included in the resolution.
        # 
        # This parameter is required.
        self.intranet_domains_shrink = intranet_domains_shrink
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intranet_domains_shrink is not None:
            result['IntranetDomains'] = self.intranet_domains_shrink

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntranetDomains') is not None:
            self.intranet_domains_shrink = m.get('IntranetDomains')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

