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
        project_id: int = None,
        region_id: str = None,
    ):
        # The approval remarks.
        self.comment = comment
        # The limit on the number of logons allowed. Valid values:
        # 
        # - **0**: No limit on the number of logons. The O&M engineer can log on an unlimited number of times during the validity period.
        # 
        # - **1**: The O&M engineer can log on only once during the validity period.
        # > - The logon limit for database asset O&M approval can only be set to no limit on the number of logons in Settings.
        # > - If an empty character string is passed, the default value is no limit on the number of logons.
        self.effect_count = effect_count
        # The end time of the validity period for logon (in seconds, UNIX timestamp format).
        self.effect_end_time = effect_end_time
        # The start time of the validity period for logon (in seconds, UNIX timestamp format).
        self.effect_start_time = effect_start_time
        # The ID of the bastion host instance.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the O&M request to approve.
        # > You can call the [ListOperationTickets](https://help.aliyun.com/document_detail/2584313.html) operation to query all OperationTicketId values that require approval.
        # 
        # This parameter is required.
        self.operation_ticket_id = operation_ticket_id
        # The project ID.
        self.project_id = project_id
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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

