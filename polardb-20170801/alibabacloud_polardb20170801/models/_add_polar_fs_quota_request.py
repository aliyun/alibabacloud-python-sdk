# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class AddPolarFsQuotaRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        polar_fs_instance_id: str = None,
        quotas: List[main_models.AddPolarFsQuotaRequestQuotas] = None,
    ):
        # The ID of the PolarDB instance on which the application depends.
        self.dbcluster_id = dbcluster_id
        # The ID of the Polarlakebase instance.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id
        # The details of the quota rules.
        # 
        # This parameter is required.
        self.quotas = quotas

    def validate(self):
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.AddPolarFsQuotaRequestQuotas()
                self.quotas.append(temp_model.from_map(k1))

        return self

class AddPolarFsQuotaRequestQuotas(DaraModel):
    def __init__(
        self,
        access_ttl: int = None,
        change_ttl: int = None,
        description: str = None,
        enabled: bool = None,
        exclude: str = None,
        file_count_limit: int = None,
        include: str = None,
        name: str = None,
        priority: int = None,
        size_limit: int = None,
    ):
        # The time to live (TTL) for the access time. Unit: seconds.
        self.access_ttl = access_ttl
        # The TTL for the change time. Unit: seconds.
        self.change_ttl = change_ttl
        # The description of the resource quota.
        self.description = description
        # Specifies whether to enable the rule. Valid values:
        # 
        # - **True**: The rule immediately applies to new items. This is the default value.
        # 
        # - **False**: The rule does not apply to new items.
        self.enabled = enabled
        # The rule to exclude specific paths from matching.
        # 
        # - A path pattern that starts with a forward slash (/). Supports glob syntax, including `*`, `?`, and `**`.
        self.exclude = exclude
        # The limit on the number of files for a user in the directory.
        self.file_count_limit = file_count_limit
        # The wildcard pattern to match paths.
        # 
        # - A path pattern that starts with a forward slash (/). Supports glob syntax, including `*`, `?`, and `**`.
        # 
        # This parameter is required.
        self.include = include
        # The name of the rule.
        # 
        # This parameter is required.
        self.name = name
        # The priority of the quota rule.
        self.priority = priority
        # The total size limit for files in the directory. Unit: GB.
        # 
        # - Note: The value must be at least 1 GB.
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

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

