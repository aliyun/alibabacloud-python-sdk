# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefenseResourceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.DescribeDefenseResourceGroupsResponseBodyGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of protected object groups.
        self.groups = groups
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeDefenseResourceGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDefenseResourceGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_name: str = None,
        resource_list: str = None,
    ):
        # The description of the protected object group.
        self.description = description
        # The time when the protected object group was created. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The most recent time when the protected object group was modified. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The name of the protected object group.
        self.group_name = group_name
        # The names of the protected objects that are added to the protected object group. Separate multiple protected objects with commas (,).
        self.resource_list = resource_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.resource_list is not None:
            result['ResourceList'] = self.resource_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ResourceList') is not None:
            self.resource_list = m.get('ResourceList')

        return self

