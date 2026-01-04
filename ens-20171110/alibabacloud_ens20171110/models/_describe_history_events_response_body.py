# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeHistoryEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.DescribeHistoryEventsResponseBodyEvents] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried events.
        self.events = events
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.DescribeHistoryEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHistoryEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        event_id: str = None,
        event_level: str = None,
        event_status: str = None,
        event_type: str = None,
        extended_attribute: str = None,
        not_before: int = None,
        publish_time: int = None,
        reason: str = None,
        resource_id: str = None,
    ):
        # The ID of the event.
        self.event_id = event_id
        # The level of the specific event. Valid values:
        # 
        # *   CRITICAL
        # *   WARN
        # *   INFO
        self.event_level = event_level
        # The status of the event. Valid values:
        # 
        # *   Inquiring
        # *   Scheduled
        # *   Executing
        # *   Executed
        # *   Failed
        # *   Canceled
        # *   Avoided
        self.event_status = event_status
        # The type of the event. Description:
        # 
        # *   Instance:SystemFailure.Redeploy: The instance is redeployed due to system issues.
        # *   Instance:SystemFailure.Reboot: The instance is restarted due to a system error.
        # *   Instance:RegionNetworkDown: The node network is interrupted.
        # *   Disk:Stalled: The disk performance is impaired.
        # *   EnsRegion:NetworkMigration: The instance is migrated due to a system error.
        # *   IP:SafeRisk: IP alerts.
        # *   IP:SafeBan: IP blocking.
        # *   Instance:SystemUpgrade.Migrate: The instance needs to be migrated due to underlying upgrades.
        # *   Instance:SystemMaintenance.Redeploy: The instance is redeployed due to system maintenance.
        self.event_type = event_type
        # The extended attributes.
        self.extended_attribute = extended_attribute
        # The scheduled execution time of the event in milliseconds.
        self.not_before = not_before
        # The release time in milliseconds.
        self.publish_time = publish_time
        # The event cause.
        self.reason = reason
        # The ID of the associated resources.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.extended_attribute is not None:
            result['ExtendedAttribute'] = self.extended_attribute

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('ExtendedAttribute') is not None:
            self.extended_attribute = m.get('ExtendedAttribute')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

