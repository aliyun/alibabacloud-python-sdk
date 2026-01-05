# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeResourcePackagesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_package_list: List[main_models.DescribeResourcePackagesResponseBodyResourcePackageList] = None,
    ):
        self.request_id = request_id
        self.resource_package_list = resource_package_list

    def validate(self):
        if self.resource_package_list:
            for v1 in self.resource_package_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourcePackageList'] = []
        if self.resource_package_list is not None:
            for k1 in self.resource_package_list:
                result['ResourcePackageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_package_list = []
        if m.get('ResourcePackageList') is not None:
            for k1 in m.get('ResourcePackageList'):
                temp_model = main_models.DescribeResourcePackagesResponseBodyResourcePackageList()
                self.resource_package_list.append(temp_model.from_map(k1))

        return self

class DescribeResourcePackagesResponseBodyResourcePackageList(DaraModel):
    def __init__(
        self,
        auto_quota: bool = None,
        create_time: int = None,
        expire_time: int = None,
        resource_package_id: str = None,
        resource_package_quota_list: List[main_models.DescribeResourcePackagesResponseBodyResourcePackageListResourcePackageQuotaList] = None,
        resource_package_type: str = None,
        status: str = None,
        tags: List[main_models.DescribeResourcePackagesResponseBodyResourcePackageListTags] = None,
        total_capacity: int = None,
        used_capacity: int = None,
    ):
        self.auto_quota = auto_quota
        self.create_time = create_time
        self.expire_time = expire_time
        self.resource_package_id = resource_package_id
        self.resource_package_quota_list = resource_package_quota_list
        self.resource_package_type = resource_package_type
        self.status = status
        self.tags = tags
        self.total_capacity = total_capacity
        self.used_capacity = used_capacity

    def validate(self):
        if self.resource_package_quota_list:
            for v1 in self.resource_package_quota_list:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_quota is not None:
            result['AutoQuota'] = self.auto_quota

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.resource_package_id is not None:
            result['ResourcePackageId'] = self.resource_package_id

        result['ResourcePackageQuotaList'] = []
        if self.resource_package_quota_list is not None:
            for k1 in self.resource_package_quota_list:
                result['ResourcePackageQuotaList'].append(k1.to_map() if k1 else None)

        if self.resource_package_type is not None:
            result['ResourcePackageType'] = self.resource_package_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoQuota') is not None:
            self.auto_quota = m.get('AutoQuota')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('ResourcePackageId') is not None:
            self.resource_package_id = m.get('ResourcePackageId')

        self.resource_package_quota_list = []
        if m.get('ResourcePackageQuotaList') is not None:
            for k1 in m.get('ResourcePackageQuotaList'):
                temp_model = main_models.DescribeResourcePackagesResponseBodyResourcePackageListResourcePackageQuotaList()
                self.resource_package_quota_list.append(temp_model.from_map(k1))

        if m.get('ResourcePackageType') is not None:
            self.resource_package_type = m.get('ResourcePackageType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeResourcePackagesResponseBodyResourcePackageListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

class DescribeResourcePackagesResponseBodyResourcePackageListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeResourcePackagesResponseBodyResourcePackageListResourcePackageQuotaList(DaraModel):
    def __init__(
        self,
        allocated_capacity: int = None,
        project_id: str = None,
        used_capacity: int = None,
    ):
        self.allocated_capacity = allocated_capacity
        self.project_id = project_id
        self.used_capacity = used_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated_capacity is not None:
            result['AllocatedCapacity'] = self.allocated_capacity

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocatedCapacity') is not None:
            self.allocated_capacity = m.get('AllocatedCapacity')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

