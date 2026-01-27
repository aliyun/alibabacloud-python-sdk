# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEnterpriseSnapshotPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        cross_region_copy_info_shrink: str = None,
        desc: str = None,
        name: str = None,
        policy_id: str = None,
        region_id: str = None,
        retain_rule_shrink: str = None,
        schedule_shrink: str = None,
        special_retain_rules_shrink: str = None,
        state: str = None,
        storage_rule_shrink: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Snapshot replication destination information.
        self.cross_region_copy_info_shrink = cross_region_copy_info_shrink
        # The description of the policy.
        self.desc = desc
        # The name of the policy.
        self.name = name
        # The id of the policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID . You can call the [DescribeRegions](https://help.aliyun.com/document_detail/354276.html) operation to query the most recent list of regions in which snapshot policy is supported.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Snapshot retention rule.
        self.retain_rule_shrink = retain_rule_shrink
        # The rule for scheduling.
        self.schedule_shrink = schedule_shrink
        # The special snapshot retention rules.
        self.special_retain_rules_shrink = special_retain_rules_shrink
        # The status of the policy. Valid values:
        # 
        # *   **ENABLED**: Enable snapshot policy execution.
        # *   **DISABLED**: Disable snapshot policy execution.
        self.state = state
        # Advanced snapshot features.
        self.storage_rule_shrink = storage_rule_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cross_region_copy_info_shrink is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info_shrink

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retain_rule_shrink is not None:
            result['RetainRule'] = self.retain_rule_shrink

        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink

        if self.special_retain_rules_shrink is not None:
            result['SpecialRetainRules'] = self.special_retain_rules_shrink

        if self.state is not None:
            result['State'] = self.state

        if self.storage_rule_shrink is not None:
            result['StorageRule'] = self.storage_rule_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CrossRegionCopyInfo') is not None:
            self.cross_region_copy_info_shrink = m.get('CrossRegionCopyInfo')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetainRule') is not None:
            self.retain_rule_shrink = m.get('RetainRule')

        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')

        if m.get('SpecialRetainRules') is not None:
            self.special_retain_rules_shrink = m.get('SpecialRetainRules')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StorageRule') is not None:
            self.storage_rule_shrink = m.get('StorageRule')

        return self

