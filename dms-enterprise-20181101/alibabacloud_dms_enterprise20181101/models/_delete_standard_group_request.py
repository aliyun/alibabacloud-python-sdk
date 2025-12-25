# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteStandardGroupRequest(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        tid: int = None,
    ):
        # The security rule set ID. You can call the [ListStandardGroups](https://help.aliyun.com/document_detail/465940.html) operation to obtain the ID of the security rule set.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

