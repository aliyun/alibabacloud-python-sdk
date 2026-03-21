# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribePackageDeductionsRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_ids: List[str] = None,
        package_ids: List[str] = None,
        page_num: int = None,
        page_size: int = None,
        resource_type: str = None,
        resource_types: List[str] = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_ids = instance_ids
        self.package_ids = package_ids
        self.page_num = page_num
        self.page_size = page_size
        self.resource_type = resource_type
        self.resource_types = resource_types
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.package_ids is not None:
            result['PackageIds'] = self.package_ids

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PackageIds') is not None:
            self.package_ids = m.get('PackageIds')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

