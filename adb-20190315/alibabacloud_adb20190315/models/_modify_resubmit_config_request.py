# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class ModifyResubmitConfigRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rules: List[main_models.ModifyResubmitConfigRequestRules] = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The job resubmission rules.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ModifyResubmitConfigRequestRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ModifyResubmitConfigRequestRules(DaraModel):
    def __init__(
        self,
        exceed_memory_exception: bool = None,
        group_name: str = None,
        peak_memory: str = None,
        query_time: str = None,
        target_group_name: str = None,
    ):
        # Specifies whether to configure out-of-memory (OOM) check.
        self.exceed_memory_exception = exceed_memory_exception
        # The name of the source resource group.
        self.group_name = group_name
        # The peak memory usage.
        self.peak_memory = peak_memory
        # The duration of the SQL statement. Unit: milliseconds.
        self.query_time = query_time
        # The name of the destination resource group.
        self.target_group_name = target_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exceed_memory_exception is not None:
            result['ExceedMemoryException'] = self.exceed_memory_exception

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.peak_memory is not None:
            result['PeakMemory'] = self.peak_memory

        if self.query_time is not None:
            result['QueryTime'] = self.query_time

        if self.target_group_name is not None:
            result['TargetGroupName'] = self.target_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceedMemoryException') is not None:
            self.exceed_memory_exception = m.get('ExceedMemoryException')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('PeakMemory') is not None:
            self.peak_memory = m.get('PeakMemory')

        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')

        if m.get('TargetGroupName') is not None:
            self.target_group_name = m.get('TargetGroupName')

        return self

