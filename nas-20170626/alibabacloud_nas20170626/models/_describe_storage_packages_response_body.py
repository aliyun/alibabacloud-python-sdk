# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeStoragePackagesResponseBody(DaraModel):
    def __init__(
        self,
        packages: main_models.DescribeStoragePackagesResponseBodyPackages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of storage plans.
        self.packages = packages
        # The page number of the returned page.
        self.page_number = page_number
        # The number of storage plans returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of storage plans.
        self.total_count = total_count

    def validate(self):
        if self.packages:
            self.packages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.packages is not None:
            result['Packages'] = self.packages.to_map()

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
        if m.get('Packages') is not None:
            temp_model = main_models.DescribeStoragePackagesResponseBodyPackages()
            self.packages = temp_model.from_map(m.get('Packages'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStoragePackagesResponseBodyPackages(DaraModel):
    def __init__(
        self,
        package: List[main_models.DescribeStoragePackagesResponseBodyPackagesPackage] = None,
    ):
        self.package = package

    def validate(self):
        if self.package:
            for v1 in self.package:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Package'] = []
        if self.package is not None:
            for k1 in self.package:
                result['Package'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.package = []
        if m.get('Package') is not None:
            for k1 in m.get('Package'):
                temp_model = main_models.DescribeStoragePackagesResponseBodyPackagesPackage()
                self.package.append(temp_model.from_map(k1))

        return self

class DescribeStoragePackagesResponseBodyPackagesPackage(DaraModel):
    def __init__(
        self,
        expired_time: str = None,
        file_system_id: str = None,
        package_id: str = None,
        size: int = None,
        start_time: str = None,
        status: str = None,
        storage_type: str = None,
    ):
        # The end time of the validity period for the storage plan.
        self.expired_time = expired_time
        # The ID of the file system that is bound to the storage plan.
        self.file_system_id = file_system_id
        # The ID of the storage plan.
        self.package_id = package_id
        # The capacity of the storage plan.
        # 
        # Unit: bytes.
        self.size = size
        # The start time of the validity period for the storage plan.
        self.start_time = start_time
        # The status of the storage plan.
        # 
        # Valid values:
        # 
        # *   free: The storage plan is not bound to a file system. You can bind the storage plan to a file system of the same storage type.
        # *   bound: The storage plan is bound to a file system.
        self.status = status
        # The type of the storage plan.
        # 
        # Valid values:
        # 
        # *   Performance
        # *   Capacity
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.package_id is not None:
            result['PackageId'] = self.package_id

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('PackageId') is not None:
            self.package_id = m.get('PackageId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

