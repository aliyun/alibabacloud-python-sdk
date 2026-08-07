# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOutboundCallRestrictionShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        outbound_call_restriction_shrink: str = None,
        policy: int = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The outbound call restriction.
        self.outbound_call_restriction_shrink = outbound_call_restriction_shrink
        # The policy. Valid values:
        # 0: blacklist.
        # 1: whitelist.
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.outbound_call_restriction_shrink is not None:
            result['OutboundCallRestriction'] = self.outbound_call_restriction_shrink

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OutboundCallRestriction') is not None:
            self.outbound_call_restriction_shrink = m.get('OutboundCallRestriction')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

