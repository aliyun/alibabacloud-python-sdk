# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeLogBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        advanced_log_policies: main_models.DescribeLogBackupPolicyResponseBodyAdvancedLogPolicies = None,
        enable_backup_log: int = None,
        log_backup_another_region_region: str = None,
        log_backup_another_region_retention_period: str = None,
        log_backup_retention_period: int = None,
        request_id: str = None,
    ):
        self.advanced_log_policies = advanced_log_policies
        # Indicates whether the log backup feature is enabled. Valid values:
        # 
        # *   0: The log backup feature is disabled.
        # *   1: The log backup feature is enabled. By default, the log backup feature is enabled and cannot be disabled.
        self.enable_backup_log = enable_backup_log
        # The region in which you want to store cross-region log backups. For more information about regions that support the cross-region backup feature, see [Overview](https://help.aliyun.com/document_detail/72672.html).
        self.log_backup_another_region_region = log_backup_another_region_region
        # The retention period of cross-region log backups. Valid values:
        # 
        # *   **0**: The cross-region backup feature is disabled.
        # *   **30 to 7300**: Cross-region log backups are retained for 30 to 7,300 days.
        # *   **-1**: The log backups are permanently retained.
        # 
        # >  When you create a cluster, the default value of this parameter is **0**.
        self.log_backup_another_region_retention_period = log_backup_another_region_retention_period
        # The retention period of the log backups. Valid values:
        # 
        # *   3 to 7300: The log backups are retained for 3 to 7,300 days.
        # *   \\-1: The log backups are permanently retained.
        self.log_backup_retention_period = log_backup_retention_period
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.advanced_log_policies:
            self.advanced_log_policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_log_policies is not None:
            result['AdvancedLogPolicies'] = self.advanced_log_policies.to_map()

        if self.enable_backup_log is not None:
            result['EnableBackupLog'] = self.enable_backup_log

        if self.log_backup_another_region_region is not None:
            result['LogBackupAnotherRegionRegion'] = self.log_backup_another_region_region

        if self.log_backup_another_region_retention_period is not None:
            result['LogBackupAnotherRegionRetentionPeriod'] = self.log_backup_another_region_retention_period

        if self.log_backup_retention_period is not None:
            result['LogBackupRetentionPeriod'] = self.log_backup_retention_period

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedLogPolicies') is not None:
            temp_model = main_models.DescribeLogBackupPolicyResponseBodyAdvancedLogPolicies()
            self.advanced_log_policies = temp_model.from_map(m.get('AdvancedLogPolicies'))

        if m.get('EnableBackupLog') is not None:
            self.enable_backup_log = m.get('EnableBackupLog')

        if m.get('LogBackupAnotherRegionRegion') is not None:
            self.log_backup_another_region_region = m.get('LogBackupAnotherRegionRegion')

        if m.get('LogBackupAnotherRegionRetentionPeriod') is not None:
            self.log_backup_another_region_retention_period = m.get('LogBackupAnotherRegionRetentionPeriod')

        if m.get('LogBackupRetentionPeriod') is not None:
            self.log_backup_retention_period = m.get('LogBackupRetentionPeriod')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLogBackupPolicyResponseBodyAdvancedLogPolicies(DaraModel):
    def __init__(
        self,
        advanced_log_policy: List[main_models.DescribeLogBackupPolicyResponseBodyAdvancedLogPoliciesAdvancedLogPolicy] = None,
    ):
        self.advanced_log_policy = advanced_log_policy

    def validate(self):
        if self.advanced_log_policy:
            for v1 in self.advanced_log_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvancedLogPolicy'] = []
        if self.advanced_log_policy is not None:
            for k1 in self.advanced_log_policy:
                result['AdvancedLogPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advanced_log_policy = []
        if m.get('AdvancedLogPolicy') is not None:
            for k1 in m.get('AdvancedLogPolicy'):
                temp_model = main_models.DescribeLogBackupPolicyResponseBodyAdvancedLogPoliciesAdvancedLogPolicy()
                self.advanced_log_policy.append(temp_model.from_map(k1))

        return self

class DescribeLogBackupPolicyResponseBodyAdvancedLogPoliciesAdvancedLogPolicy(DaraModel):
    def __init__(
        self,
        dest_region: str = None,
        dest_type: str = None,
        enable_log_backup: int = None,
        log_retention_type: str = None,
        log_retention_value: str = None,
        policy_id: str = None,
        src_region: str = None,
        src_type: str = None,
    ):
        self.dest_region = dest_region
        self.dest_type = dest_type
        self.enable_log_backup = enable_log_backup
        self.log_retention_type = log_retention_type
        self.log_retention_value = log_retention_value
        self.policy_id = policy_id
        self.src_region = src_region
        self.src_type = src_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.dest_type is not None:
            result['DestType'] = self.dest_type

        if self.enable_log_backup is not None:
            result['EnableLogBackup'] = self.enable_log_backup

        if self.log_retention_type is not None:
            result['LogRetentionType'] = self.log_retention_type

        if self.log_retention_value is not None:
            result['LogRetentionValue'] = self.log_retention_value

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.src_region is not None:
            result['SrcRegion'] = self.src_region

        if self.src_type is not None:
            result['SrcType'] = self.src_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('DestType') is not None:
            self.dest_type = m.get('DestType')

        if m.get('EnableLogBackup') is not None:
            self.enable_log_backup = m.get('EnableLogBackup')

        if m.get('LogRetentionType') is not None:
            self.log_retention_type = m.get('LogRetentionType')

        if m.get('LogRetentionValue') is not None:
            self.log_retention_value = m.get('LogRetentionValue')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('SrcRegion') is not None:
            self.src_region = m.get('SrcRegion')

        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')

        return self

