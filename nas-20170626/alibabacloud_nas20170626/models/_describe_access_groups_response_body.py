# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessGroupsResponseBody(DaraModel):
    def __init__(
        self,
        access_groups: main_models.DescribeAccessGroupsResponseBodyAccessGroups = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried permission groups.
        self.access_groups = access_groups
        # The page number.
        self.page_number = page_number
        # The number of permission groups returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of permission groups.
        self.total_count = total_count

    def validate(self):
        if self.access_groups:
            self.access_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_groups is not None:
            result['AccessGroups'] = self.access_groups.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroups') is not None:
            temp_model = main_models.DescribeAccessGroupsResponseBodyAccessGroups()
            self.access_groups = temp_model.from_map(m.get('AccessGroups'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccessGroupsResponseBodyAccessGroups(DaraModel):
    def __init__(
        self,
        access_group: List[main_models.DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup] = None,
    ):
        self.access_group = access_group

    def validate(self):
        if self.access_group:
            for v1 in self.access_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessGroup'] = []
        if self.access_group is not None:
            for k1 in self.access_group:
                result['AccessGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_group = []
        if m.get('AccessGroup') is not None:
            for k1 in m.get('AccessGroup'):
                temp_model = main_models.DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup()
                self.access_group.append(temp_model.from_map(k1))

        return self

class DescribeAccessGroupsResponseBodyAccessGroupsAccessGroup(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_group_type: str = None,
        create_time: str = None,
        description: str = None,
        file_system_type: str = None,
        mount_target_count: int = None,
        region_id: str = None,
        rule_count: int = None,
    ):
        # The name of the permission group.
        self.access_group_name = access_group_name
        # The network type of the permission group. Valid value: **Vpc**.
        self.access_group_type = access_group_type
        # The time when the permission group was created.
        self.create_time = create_time
        # The description of the permission group.
        self.description = description
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard: General-purpose Apsara File Storage NAS (NAS) file system
        # *   extreme: Extreme NAS file system.
        # *   cpfs: CPFS file system.
        self.file_system_type = file_system_type
        # The number of mount targets to which the permission group is attached.
        self.mount_target_count = mount_target_count
        # The region ID.
        self.region_id = region_id
        # The total number of rules in the permission group.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        if self.mount_target_count is not None:
            result['MountTargetCount'] = self.mount_target_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        if m.get('MountTargetCount') is not None:
            self.mount_target_count = m.get('MountTargetCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

