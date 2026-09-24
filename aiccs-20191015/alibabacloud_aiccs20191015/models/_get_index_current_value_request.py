# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIndexCurrentValueRequest(DaraModel):
    def __init__(
        self,
        dep_ids: str = None,
        group_ids: str = None,
        instance_id: str = None,
    ):
        # The list of department IDs. Separate multiple IDs with commas (,).
        # 
        # Call the [GetAllDepartment](https://help.aliyun.com/document_detail/2717975.html) operation and check the **DepartmentId** parameter in the response to obtain the department ID.
        # 
        # > When this parameter is not empty:
        # > - If GroupIds is not empty, the query is performed based on the skill group list corresponding to GroupIds.
        # > - If GroupIds is empty, the query is performed based on the department list corresponding to this parameter.
        self.dep_ids = dep_ids
        # The list of skill group IDs. Separate multiple IDs with commas (,).
        # 
        # Call the [QuerySkillGroups](https://help.aliyun.com/document_detail/2717970.html) operation and check the **SkillGroupId** parameter in the response to obtain the skill group ID.
        # 
        # > When this parameter is not empty, the query is performed based on the skill group list corresponding to this parameter.
        self.group_ids = group_ids
        # The AICCS instance ID. You can obtain the instance ID from <b>Instance Management</b> in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # > The AICCS instance ID is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dep_ids is not None:
            result['DepIds'] = self.dep_ids

        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepIds') is not None:
            self.dep_ids = m.get('DepIds')

        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

