# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPhoneNumberRequest(DaraModel):
    def __init__(
        self,
        contact_flow_id: str = None,
        instance_id: str = None,
        number: str = None,
        usage: str = None,
    ):
        # The IVR contact flow ID attached to the number. This field is valid only when the number usage is Inbound or Bidirection.
        self.contact_flow_id = contact_flow_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Phone number.
        # 
        # This parameter is required.
        self.number = number
        # Number usage.
        # 
        # This parameter is required.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_flow_id is not None:
            result['ContactFlowId'] = self.contact_flow_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number is not None:
            result['Number'] = self.number

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

