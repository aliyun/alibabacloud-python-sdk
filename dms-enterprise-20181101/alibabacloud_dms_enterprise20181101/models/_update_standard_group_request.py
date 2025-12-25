# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateStandardGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: int = None,
        group_name: str = None,
        tid: int = None,
    ):
        # The description of the security rule set.
        # 
        # This parameter is required.
        self.description = description
        # The security rule set ID. You can call the [ListStandardGroups](https://help.aliyun.com/document_detail/465940.html) operation to obtain the ID of the security rule set.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the security rule set.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The tenant ID.
        # 
        # >  To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

