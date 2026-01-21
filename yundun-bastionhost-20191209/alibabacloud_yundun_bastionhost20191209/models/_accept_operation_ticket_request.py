# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AcceptOperationTicketRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        effect_count: str = None,
        effect_end_time: str = None,
        effect_start_time: str = None,
        instance_id: str = None,
        operation_ticket_id: str = None,
        region_id: str = None,
    ):
        # The review description.
        self.comment = comment
        # The maximum number of logons allowed. Valid values:
        # 
        # *   **0**: The number of logons is unlimited. The O\\&M engineer can log on to the specified asset for unlimited times during the validity period.
        # *   **1**: The O\\&M engineer can log on to the specified asset only once during the validity period.
        # 
        # > *   You can set this parameter only to 0 if you review an O\\&M application on a database.
        # > *   If you do not specify this parameter, the default value 0 is used.
        self.effect_count = effect_count
        # The end time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_end_time = effect_end_time
        # The start time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_start_time = effect_start_time
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the O\\&M application that you want to approve. You can call the ListOperationTickets operation to query the IDs of all O\\&M applications that require review.
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

        if self.effect_count is not None:
            result['EffectCount'] = self.effect_count

        if self.effect_end_time is not None:
            result['EffectEndTime'] = self.effect_end_time

        if self.effect_start_time is not None:
            result['EffectStartTime'] = self.effect_start_time

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

        if m.get('EffectCount') is not None:
            self.effect_count = m.get('EffectCount')

        if m.get('EffectEndTime') is not None:
            self.effect_end_time = m.get('EffectEndTime')

        if m.get('EffectStartTime') is not None:
            self.effect_start_time = m.get('EffectStartTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

