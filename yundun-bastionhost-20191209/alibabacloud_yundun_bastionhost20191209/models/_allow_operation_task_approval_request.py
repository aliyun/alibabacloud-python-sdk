# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllowOperationTaskApprovalRequest(DaraModel):
    def __init__(
        self,
        approve_id: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The ID of the O&M task approval.
        # > You can call the ListTodoOpsTaskApprovals operation to query this parameter.
        # 
        # This parameter is required.
        self.approve_id = approve_id
        # The instance ID of the bastion host.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve_id is not None:
            result['ApproveId'] = self.approve_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveId') is not None:
            self.approve_id = m.get('ApproveId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

