# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsQuotaResponseBody(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_record_count: str = None,
        page_size: str = None,
        path: str = None,
        polar_fs_instance_id: str = None,
        policy_items: List[main_models.DescribePolarFsQuotaResponseBodyPolicyItems] = None,
        quota_items: List[main_models.DescribePolarFsQuotaResponseBodyQuotaItems] = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The number of entries per page. Valid values: 5 to 50. Default value: 10.
        self.page_size = page_size
        # The path of the directory.
        self.path = path
        # The PolarFS instance ID.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The details of the rules.
        self.policy_items = policy_items
        # The quota information.
        self.quota_items = quota_items
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.policy_items:
            for v1 in self.policy_items:
                 if v1:
                    v1.validate()
        if self.quota_items:
            for v1 in self.quota_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        result['PolicyItems'] = []
        if self.policy_items is not None:
            for k1 in self.policy_items:
                result['PolicyItems'].append(k1.to_map() if k1 else None)

        result['QuotaItems'] = []
        if self.quota_items is not None:
            for k1 in self.quota_items:
                result['QuotaItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        self.policy_items = []
        if m.get('PolicyItems') is not None:
            for k1 in m.get('PolicyItems'):
                temp_model = main_models.DescribePolarFsQuotaResponseBodyPolicyItems()
                self.policy_items.append(temp_model.from_map(k1))

        self.quota_items = []
        if m.get('QuotaItems') is not None:
            for k1 in m.get('QuotaItems'):
                temp_model = main_models.DescribePolarFsQuotaResponseBodyQuotaItems()
                self.quota_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePolarFsQuotaResponseBodyQuotaItems(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        inodes: int = None,
        path: str = None,
        used_capacity: int = None,
        used_inodes: int = None,
    ):
        # The capacity. Unit: bytes.
        self.capacity = capacity
        # The total number of inodes.
        self.inodes = inodes
        # The directory path.
        self.path = path
        # The used capacity. Unit: bytes.
        self.used_capacity = used_capacity
        # The number of used inodes.
        self.used_inodes = used_inodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.inodes is not None:
            result['Inodes'] = self.inodes

        if self.path is not None:
            result['Path'] = self.path

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        if self.used_inodes is not None:
            result['UsedInodes'] = self.used_inodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('Inodes') is not None:
            self.inodes = m.get('Inodes')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        if m.get('UsedInodes') is not None:
            self.used_inodes = m.get('UsedInodes')

        return self

class DescribePolarFsQuotaResponseBodyPolicyItems(DaraModel):
    def __init__(
        self,
        access_ttl: int = None,
        change_ttl: int = None,
        description: str = None,
        enabled: bool = None,
        exclude: str = None,
        file_count_limit: int = None,
        id: int = None,
        include: str = None,
        name: str = None,
        priority: int = None,
        size_limit: int = None,
    ):
        # The TTL of the access time. Unit: seconds.
        self.access_ttl = access_ttl
        # The TTL of the change time. Unit: seconds.
        self.change_ttl = change_ttl
        # The rule description.
        self.description = description
        # Indicates whether the rule is enabled. Valid values:
        # 
        # - **true**: The rule takes effect immediately for new events. This is the default value.
        # 
        # - **false**: The rule does not take effect for new events.
        self.enabled = enabled
        # The glob pattern of paths to exclude.
        # 
        # - The pattern must start with `/` and supports glob syntax, including `*`, `?`, and `**`.
        self.exclude = exclude
        # The maximum number of files in the directory.
        self.file_count_limit = file_count_limit
        # The rule ID.
        self.id = id
        # The glob pattern for paths to include.
        # 
        # - The pattern must start with `/` and supports glob syntax, including `*`, `?`, and `**`.
        self.include = include
        # The rule name.
        self.name = name
        # The priority of the quota rule.
        self.priority = priority
        # The maximum total size of files in the directory. Unit: GB.
        # 
        # - The value must be greater than or equal to 1.
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ttl is not None:
            result['AccessTTL'] = self.access_ttl

        if self.change_ttl is not None:
            result['ChangeTTL'] = self.change_ttl

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.id is not None:
            result['Id'] = self.id

        if self.include is not None:
            result['Include'] = self.include

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTTL') is not None:
            self.access_ttl = m.get('AccessTTL')

        if m.get('ChangeTTL') is not None:
            self.change_ttl = m.get('ChangeTTL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

