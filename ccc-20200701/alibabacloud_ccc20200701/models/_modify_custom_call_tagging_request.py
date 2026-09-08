# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCustomCallTaggingRequest(DaraModel):
    def __init__(
        self,
        call_tag_name_list: str = None,
        description: str = None,
        instance_id: str = None,
        number: str = None,
    ):
        # A list of number tag names. You must provide the complete list of number tags to be modified, and ensure that these number tags have already been created.
        self.call_tag_name_list = call_tag_name_list
        # The new description for the inbound number mark. This parameter is optional. The default value is empty, which indicates that the description will not be modified.
        self.description = description
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number associated with the inbound number mark. The system matches the inbound number mark to be modified based on this number.
        # 
        # This parameter is required.
        self.number = number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_tag_name_list is not None:
            result['CallTagNameList'] = self.call_tag_name_list

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.number is not None:
            result['Number'] = self.number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallTagNameList') is not None:
            self.call_tag_name_list = m.get('CallTagNameList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        return self

