# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstancesRequest(DaraModel):
    def __init__(
        self,
        db_version: str = None,
        description: str = None,
        instance_id: str = None,
        must_has_cdc: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        series: str = None,
        tags: str = None,
    ):
        self.db_version = db_version
        self.description = description
        self.instance_id = instance_id
        self.must_has_cdc = must_has_cdc
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.series = series
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_version is not None:
            result['DbVersion'] = self.db_version

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.must_has_cdc is not None:
            result['MustHasCdc'] = self.must_has_cdc

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.series is not None:
            result['Series'] = self.series

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbVersion') is not None:
            self.db_version = m.get('DbVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MustHasCdc') is not None:
            self.must_has_cdc = m.get('MustHasCdc')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Series') is not None:
            self.series = m.get('Series')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

