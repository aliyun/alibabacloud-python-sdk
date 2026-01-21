# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RejectOperationTicketRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        instance_id: str = None,
        operation_ticket_id: str = None,
        region_id: str = None,
    ):
        # The review remarks.
        self.comment = comment
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the O\\&M application that you want to reject.
        # 
        # >  You can call the [ListOperationTickets](https://help.aliyun.com/document_detail/2584313.html) operation to query the IDs of all O\\&M applications that require review.
        # 
        # This parameter is required.
        self.operation_ticket_id = operation_ticket_id
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
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

