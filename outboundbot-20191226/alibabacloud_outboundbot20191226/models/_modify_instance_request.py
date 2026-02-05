# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyInstanceRequest(DaraModel):
    def __init__(
        self,
        calling_number: List[str] = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_name: str = None,
        max_concurrent_conversation: int = None,
    ):
        self.calling_number = calling_number
        self.instance_description = instance_description
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_name = instance_name
        # This parameter is required.
        self.max_concurrent_conversation = max_concurrent_conversation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')

        return self

