# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotPackageResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshot_packages: main_models.DescribeSnapshotPackageResponseBodySnapshotPackages = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Details about the OSS storage plans.
        self.snapshot_packages = snapshot_packages
        # The total number of OSS storage plans.
        self.total_count = total_count

    def validate(self):
        if self.snapshot_packages:
            self.snapshot_packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_packages is not None:
            result['SnapshotPackages'] = self.snapshot_packages.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotPackages') is not None:
            temp_model = main_models.DescribeSnapshotPackageResponseBodySnapshotPackages()
            self.snapshot_packages = temp_model.from_map(m.get('SnapshotPackages'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSnapshotPackageResponseBodySnapshotPackages(DaraModel):
    def __init__(
        self,
        snapshot_package: List[main_models.DescribeSnapshotPackageResponseBodySnapshotPackagesSnapshotPackage] = None,
    ):
        self.snapshot_package = snapshot_package

    def validate(self):
        if self.snapshot_package:
            for v1 in self.snapshot_package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnapshotPackage'] = []
        if self.snapshot_package is not None:
            for k1 in self.snapshot_package:
                result['SnapshotPackage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot_package = []
        if m.get('SnapshotPackage') is not None:
            for k1 in m.get('SnapshotPackage'):
                temp_model = main_models.DescribeSnapshotPackageResponseBodySnapshotPackagesSnapshotPackage()
                self.snapshot_package.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotPackageResponseBodySnapshotPackagesSnapshotPackage(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        end_time: str = None,
        init_capacity: int = None,
        start_time: str = None,
    ):
        # The name of the OSS storage plan.
        self.display_name = display_name
        # The time when the OSS storage plan expires. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The maximum storage capacity offered by the OSS storage plan.
        self.init_capacity = init_capacity
        # The time when the OSS storage plan was purchased. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

