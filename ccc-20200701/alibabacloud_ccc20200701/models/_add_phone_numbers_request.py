# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPhoneNumbersRequest(DaraModel):
    def __init__(
        self,
        contact_flow_id: str = None,
        instance_id: str = None,
        number_group_id: str = None,
        number_list: str = None,
        usage: str = None,
    ):
        # ID of the IVR contact flow to attach. This parameter is valid only when the number usage includes inbound calls. It is optional and defaults to empty.
        self.contact_flow_id = contact_flow_id
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Number group ID. You can view number grouping information in the Cloud Contact Center console. This parameter is optional and defaults to empty.
        self.number_group_id = number_group_id
        # List of phone numbers to add.
        self.number_list = number_list
        # Usage of the phone number. Note: If the provided number is a 400 number, the usage must be set to Inbound.
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

        if self.number_group_id is not None:
            result['NumberGroupId'] = self.number_group_id

        if self.number_list is not None:
            result['NumberList'] = self.number_list

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactFlowId') is not None:
            self.contact_flow_id = m.get('ContactFlowId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NumberGroupId') is not None:
            self.number_group_id = m.get('NumberGroupId')

        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

