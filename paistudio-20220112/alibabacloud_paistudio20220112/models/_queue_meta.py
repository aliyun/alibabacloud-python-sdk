# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class QueueMeta(DaraModel):
    def __init__(
        self,
        gmt_dequeued_time: str = None,
        gmt_enqueued_time: str = None,
        gmt_position_modified_time: str = None,
        name: str = None,
        position: str = None,
        queue_strategy: str = None,
        quota_id: str = None,
        resource: main_models.ResourceAmount = None,
        scheduled_resource: str = None,
        status: str = None,
        use_oversold_resource: bool = None,
    ):
        self.gmt_dequeued_time = gmt_dequeued_time
        self.gmt_enqueued_time = gmt_enqueued_time
        self.gmt_position_modified_time = gmt_position_modified_time
        self.name = name
        self.position = position
        self.queue_strategy = queue_strategy
        self.quota_id = quota_id
        self.resource = resource
        self.scheduled_resource = scheduled_resource
        self.status = status
        self.use_oversold_resource = use_oversold_resource

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_dequeued_time is not None:
            result['GmtDequeuedTime'] = self.gmt_dequeued_time

        if self.gmt_enqueued_time is not None:
            result['GmtEnqueuedTime'] = self.gmt_enqueued_time

        if self.gmt_position_modified_time is not None:
            result['GmtPositionModifiedTime'] = self.gmt_position_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.position is not None:
            result['Position'] = self.position

        if self.queue_strategy is not None:
            result['QueueStrategy'] = self.queue_strategy

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.scheduled_resource is not None:
            result['ScheduledResource'] = self.scheduled_resource

        if self.status is not None:
            result['Status'] = self.status

        if self.use_oversold_resource is not None:
            result['UseOversoldResource'] = self.use_oversold_resource

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtDequeuedTime') is not None:
            self.gmt_dequeued_time = m.get('GmtDequeuedTime')

        if m.get('GmtEnqueuedTime') is not None:
            self.gmt_enqueued_time = m.get('GmtEnqueuedTime')

        if m.get('GmtPositionModifiedTime') is not None:
            self.gmt_position_modified_time = m.get('GmtPositionModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('QueueStrategy') is not None:
            self.queue_strategy = m.get('QueueStrategy')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('Resource') is not None:
            temp_model = main_models.ResourceAmount()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('ScheduledResource') is not None:
            self.scheduled_resource = m.get('ScheduledResource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UseOversoldResource') is not None:
            self.use_oversold_resource = m.get('UseOversoldResource')

        return self

