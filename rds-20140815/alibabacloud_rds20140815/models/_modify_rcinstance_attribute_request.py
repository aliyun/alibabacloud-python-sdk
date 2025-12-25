# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyRCInstanceAttributeRequest(DaraModel):
    def __init__(
        self,
        deletion_protection: bool = None,
        host_name: str = None,
        instance_id: str = None,
        instance_ids: List[str] = None,
        instance_name: str = None,
        password: str = None,
        reboot: bool = None,
        region_id: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
    ):
        # Specifies whether to enable the release protection feature for the instance. Valid values:
        # 
        # - **true**: enables the release protection feature.
        # - **false** (default): does not enable the release protection feature.
        self.deletion_protection = deletion_protection
        # The hostname of the instance.
        self.host_name = host_name
        # The instance ID.
        self.instance_id = instance_id
        self.instance_ids = instance_ids
        self.instance_name = instance_name
        # The new password of the instance.
        # 
        # *   The value must be 8 to 30 characters in length.
        # *   The value must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include `()` ~ ! @ # $ % ^ & \\* - _ + = \\`
        self.password = password
        # Specifies whether to restart the instance. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.reboot = reboot
        # The region ID of the instance. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the security group to which the instance is added.
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.password is not None:
            result['Password'] = self.password

        if self.reboot is not None:
            result['Reboot'] = self.reboot

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Reboot') is not None:
            self.reboot = m.get('Reboot')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        return self

