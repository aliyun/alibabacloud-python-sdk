# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceIpWhitelistRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        group_name: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.branch_name = branch_name
        # The group name.
        self.group_name = group_name
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

