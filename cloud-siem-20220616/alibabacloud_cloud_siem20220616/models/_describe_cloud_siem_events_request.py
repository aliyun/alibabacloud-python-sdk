# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeCloudSiemEventsRequest(DaraModel):
    def __init__(
        self,
        asset_id: str = None,
        current_page: int = None,
        end_time: int = None,
        entity_uuid: str = None,
        event_name: str = None,
        incident_uuid: str = None,
        order: str = None,
        order_field: str = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
        status: int = None,
        thread_level: List[str] = None,
    ):
        # The ID of the asset that is associated with the event.
        self.asset_id = asset_id
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        self.entity_uuid = entity_uuid
        # The name of the event.
        self.event_name = event_name
        # The ID of the event.
        self.incident_uuid = incident_uuid
        # The sort order. Valid values:
        # 
        # *   desc: descending order
        # *   asc: ascending order
        self.order = order
        # The sort field. Valid values:
        # 
        # *   GmtModified: sorts the events by creation time. This is the default value.
        # *   ThreatScore: sorts the events by risk score.
        self.order_field = order_field
        # The number of entries per page. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the regions in which your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
        self.role_type = role_type
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time
        # The status of the event. Valid values:
        # 
        # *   0: unhandled
        # *   1: handling
        # *   5: handling failed
        # *   10: handled
        self.status = status
        # The risk levels of the events. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.thread_level = thread_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.order is not None:
            result['Order'] = self.order

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.thread_level is not None:
            result['ThreadLevel'] = self.thread_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThreadLevel') is not None:
            self.thread_level = m.get('ThreadLevel')

        return self

