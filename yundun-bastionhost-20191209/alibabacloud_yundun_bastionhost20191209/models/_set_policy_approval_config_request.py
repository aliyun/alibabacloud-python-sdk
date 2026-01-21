# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class SetPolicyApprovalConfigRequest(DaraModel):
    def __init__(
        self,
        approval_config: main_models.SetPolicyApprovalConfigRequestApprovalConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        # The O&M approval setting in the control policy.
        # 
        # This parameter is required.
        self.approval_config = approval_config
        # The bastion host ID.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # 
        # >  You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to query the control policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        if self.approval_config:
            self.approval_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_config is not None:
            result['ApprovalConfig'] = self.approval_config.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalConfig') is not None:
            temp_model = main_models.SetPolicyApprovalConfigRequestApprovalConfig()
            self.approval_config = temp_model.from_map(m.get('ApprovalConfig'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class SetPolicyApprovalConfigRequestApprovalConfig(DaraModel):
    def __init__(
        self,
        switch_status: str = None,
    ):
        # Specifies whether to enable O&M approval in the control policy. Valid values:
        # 
        # * **On**: enables O&M approval.
        # * **Off**: disables O&M approval.
        # 
        # This parameter is required.
        self.switch_status = switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        return self

