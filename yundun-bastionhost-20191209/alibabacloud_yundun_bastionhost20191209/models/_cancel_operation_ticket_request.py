# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelOperationTicketRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        operation_ticket_id: str = None,
        region_id: str = None,
    ):
        # The instance ID of the Bastionhost instance.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the O&M request to be withdrawn.
        # > You can only withdraw O&M requests that have not been fully approved.
        # 
        # This parameter is required.
        self.operation_ticket_id = operation_ticket_id
        # The region ID of the Bastionhost instance.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

