# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAllGroupsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        groups: List[main_models.DescribeAllGroupsResponseBodyGroups] = None,
        request_id: str = None,
    ):
        # The total number of server groups.
        self.count = count
        # The grouping information about the servers.
        self.groups = groups
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeAllGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAllGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group_flag: int = None,
        group_id: int = None,
        group_name: str = None,
    ):
        # The type of the server group. Valid values:
        # 
        # *   **0**: default group
        # *   **1**: other groups
        self.group_flag = group_flag
        # The ID of the server group.
        self.group_id = group_id
        # The name of the server group.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_flag is not None:
            result['GroupFlag'] = self.group_flag

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupFlag') is not None:
            self.group_flag = m.get('GroupFlag')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

