# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AcceptApproveCommandRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the command that you want to approve.
        # 
        # >  You can call the [ListApproveCommands](https://help.aliyun.com/document_detail/2584310.html) operation to query the IDs of all commands that need to be reviewed.
        # 
        # This parameter is required.
        self.command_id = command_id
        # The ID of the bastion host.
        # 
        # >  You can call the DescribeInstances operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

