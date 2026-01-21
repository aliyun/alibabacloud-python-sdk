# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListHostGroupsForUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        host_groups: List[main_models.ListHostGroupsForUserGroupResponseBodyHostGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The host groups returned.
        self.host_groups = host_groups
        # The ID of the request.
        self.request_id = request_id
        # The total number of host groups returned.
        self.total_count = total_count

    def validate(self):
        if self.host_groups:
            for v1 in self.host_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k1 in self.host_groups:
                result['HostGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k1 in m.get('HostGroups'):
                temp_model = main_models.ListHostGroupsForUserGroupResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHostGroupsForUserGroupResponseBodyHostGroups(DaraModel):
    def __init__(
        self,
        comment: str = None,
        host_group_id: str = None,
        host_group_name: str = None,
    ):
        # The description of the host group.
        self.comment = comment
        # The ID of the host group.
        self.host_group_id = host_group_id
        # The name of the host group.
        self.host_group_name = host_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id

        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')

        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')

        return self

