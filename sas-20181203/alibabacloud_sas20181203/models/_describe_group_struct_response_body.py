# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeGroupStructResponseBody(DaraModel):
    def __init__(
        self,
        group_father: int = None,
        group_flag: int = None,
        group_id: int = None,
        group_index: int = None,
        group_level: int = None,
        group_name: str = None,
        groups: List[str] = None,
        machine_num: int = None,
        request_id: str = None,
    ):
        # The parent node of the group.
        self.group_father = group_father
        # The type of the server group. Valid values:
        # 
        # *   **0**: the default group
        # *   **1**: other groups
        self.group_flag = group_flag
        # The ID of the server group.
        self.group_id = group_id
        # The sequence number.
        self.group_index = group_index
        # The level of the application group.
        self.group_level = group_level
        # The name of the server group.
        self.group_name = group_name
        # An array that consists of child groups.
        self.groups = groups
        # The number of servers in the group.
        self.machine_num = machine_num
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_father is not None:
            result['GroupFather'] = self.group_father

        if self.group_flag is not None:
            result['GroupFlag'] = self.group_flag

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_index is not None:
            result['GroupIndex'] = self.group_index

        if self.group_level is not None:
            result['GroupLevel'] = self.group_level

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.groups is not None:
            result['Groups'] = self.groups

        if self.machine_num is not None:
            result['MachineNum'] = self.machine_num

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupFather') is not None:
            self.group_father = m.get('GroupFather')

        if m.get('GroupFlag') is not None:
            self.group_flag = m.get('GroupFlag')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupIndex') is not None:
            self.group_index = m.get('GroupIndex')

        if m.get('GroupLevel') is not None:
            self.group_level = m.get('GroupLevel')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Groups') is not None:
            self.groups = m.get('Groups')

        if m.get('MachineNum') is not None:
            self.machine_num = m.get('MachineNum')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

