# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class CreateOutboundCallRestrictionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        outbound_call_restriction: List[main_models.CreateOutboundCallRestrictionRequestOutboundCallRestriction] = None,
        policy: int = None,
    ):
        # The instance ID.
        self.instance_id = instance_id
        # The outbound call restriction.
        self.outbound_call_restriction = outbound_call_restriction
        # The policy. Valid values:
        # 0: blacklist.
        # 1: whitelist.
        self.policy = policy

    def validate(self):
        if self.outbound_call_restriction:
            for v1 in self.outbound_call_restriction:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['OutboundCallRestriction'] = []
        if self.outbound_call_restriction is not None:
            for k1 in self.outbound_call_restriction:
                result['OutboundCallRestriction'].append(k1.to_map() if k1 else None)

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.outbound_call_restriction = []
        if m.get('OutboundCallRestriction') is not None:
            for k1 in m.get('OutboundCallRestriction'):
                temp_model = main_models.CreateOutboundCallRestrictionRequestOutboundCallRestriction()
                self.outbound_call_restriction.append(temp_model.from_map(k1))

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

class CreateOutboundCallRestrictionRequestOutboundCallRestriction(DaraModel):
    def __init__(
        self,
        number: str = None,
        remark: str = None,
    ):
        # The phone number.
        self.number = number
        # The remarks.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number is not None:
            result['Number'] = self.number

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

