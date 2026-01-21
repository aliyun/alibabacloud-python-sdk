# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class SetPolicyCommandConfigRequest(DaraModel):
    def __init__(
        self,
        command_config: main_models.SetPolicyCommandConfigRequestCommandConfig = None,
        instance_id: str = None,
        policy_id: str = None,
        region_id: str = None,
    ):
        # The command control settings.
        # 
        # > This parameter applies only to Linux hosts.
        # 
        # This parameter is required.
        self.command_config = command_config
        # The bastion host ID.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the bastion host ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the control policy that you want to modify.
        # 
        # > You can call the [ListPolicies](https://help.aliyun.com/document_detail/2758876.html) operation to query the control policy ID.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        if self.command_config:
            self.command_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_config is not None:
            result['CommandConfig'] = self.command_config.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandConfig') is not None:
            temp_model = main_models.SetPolicyCommandConfigRequestCommandConfig()
            self.command_config = temp_model.from_map(m.get('CommandConfig'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class SetPolicyCommandConfigRequestCommandConfig(DaraModel):
    def __init__(
        self,
        approval: main_models.SetPolicyCommandConfigRequestCommandConfigApproval = None,
        deny: main_models.SetPolicyCommandConfigRequestCommandConfigDeny = None,
    ):
        # The command approval settings.
        # 
        # > A command approval policy is used to approve the commands that are excluded from a whitelist or blacklist specified in a command control policy. The command control policy takes precedence over the command approval policy in validation.
        self.approval = approval
        # The command control settings.
        # 
        # This parameter is required.
        self.deny = deny

    def validate(self):
        if self.approval:
            self.approval.validate()
        if self.deny:
            self.deny.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval is not None:
            result['Approval'] = self.approval.to_map()

        if self.deny is not None:
            result['Deny'] = self.deny.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Approval') is not None:
            temp_model = main_models.SetPolicyCommandConfigRequestCommandConfigApproval()
            self.approval = temp_model.from_map(m.get('Approval'))

        if m.get('Deny') is not None:
            temp_model = main_models.SetPolicyCommandConfigRequestCommandConfigDeny()
            self.deny = temp_model.from_map(m.get('Deny'))

        return self

class SetPolicyCommandConfigRequestCommandConfigDeny(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        commands: List[str] = None,
    ):
        # The type of command control. Valid values:
        # 
        # *   **black**: blacklist mode.
        # *   **white**: whitelist mode.
        # 
        # This parameter is required.
        self.acl_type = acl_type
        # The commands to be controlled.
        # 
        # > This parameter is required if AclType is set to white.
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.commands is not None:
            result['Commands'] = self.commands

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        return self

class SetPolicyCommandConfigRequestCommandConfigApproval(DaraModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        # The commands that can be run only after approval.
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands is not None:
            result['Commands'] = self.commands

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        return self

