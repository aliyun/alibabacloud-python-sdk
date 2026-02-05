# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateInstanceRequest(DaraModel):
    def __init__(
        self,
        calling_number: List[str] = None,
        instance_description: str = None,
        instance_name: str = None,
        max_concurrent_conversation: int = None,
        nlu_service_type: str = None,
        resource_group_id: str = None,
    ):
        self.calling_number = calling_number
        self.instance_description = instance_description
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.max_concurrent_conversation = max_concurrent_conversation
        self.nlu_service_type = nlu_service_type
        self.resource_group_id = resource_group_id

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

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation

        if self.nlu_service_type is not None:
            result['NluServiceType'] = self.nlu_service_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')

        if m.get('NluServiceType') is not None:
            self.nlu_service_type = m.get('NluServiceType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

