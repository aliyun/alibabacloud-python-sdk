# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListIncidentsShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_uuid: str = None,
        end_time: int = None,
        incident_name: str = None,
        incident_status: int = None,
        incident_status_list: List[str] = None,
        incident_tags: str = None,
        incident_uuids_shrink: str = None,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        order_direction: str = None,
        order_field_name: str = None,
        owners: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        relate_asset_id: str = None,
        relate_entity_id: str = None,
        role_for: int = None,
        role_type: int = None,
        start_time: int = None,
        threat_level: List[str] = None,
    ):
        # The alert ID.
        self.alert_uuid = alert_uuid
        # The end time as a UNIX timestamp in milliseconds (ms).
        self.end_time = end_time
        # The event name.
        self.incident_name = incident_name
        # The event status. Valid values:
        # - 0: Unhandled.
        # - 1: Handling.
        # - 5: Handling failed.
        # - 10: Handled.
        self.incident_status = incident_status
        self.incident_status_list = incident_status_list
        # The event tags.
        self.incident_tags = incident_tags
        # The list of event UUIDs, separated by commas (,).
        self.incident_uuids_shrink = incident_uuids_shrink
        # The language type of the response messages. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return.
        self.max_results = max_results
        # The pagination token for the next query. Leave this parameter empty for the first query or if no more results exist. If a next page exists, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The sort direction. Valid values:
        # - **desc** (default): Descending order.
        # - **asc**: Ascending order.
        self.order_direction = order_direction
        # The name of the field used to sort the list.
        # - GmtModified: Event update time (default).
        # - ThreatScore: Threat score.
        self.order_field_name = order_field_name
        # The UID of the account responsible for the event.
        self.owners = owners
        # The page number.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the threat analysis data management center is located. Select the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets are located in the Chinese mainland.
        # - ap-southeast-1: Your assets are located outside China.
        self.region_id = region_id
        # The ID of the asset associated with the event.
        self.relate_asset_id = relate_asset_id
        # The ID of the entity associated with the event.
        self.relate_entity_id = relate_entity_id
        # The user ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: The view of the current Alibaba Cloud account.
        # - 1: The view of all accounts in the enterprise.
        self.role_type = role_type
        # The start time as a UNIX timestamp in milliseconds (ms).
        self.start_time = start_time
        # The threat level. Valid values:
        # - 5: Critical.
        # - 4: High.
        # - 3: Medium.
        # - 2: Low.
        # - 1: Informational.
        self.threat_level = threat_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name

        if self.incident_status is not None:
            result['IncidentStatus'] = self.incident_status

        if self.incident_status_list is not None:
            result['IncidentStatusList'] = self.incident_status_list

        if self.incident_tags is not None:
            result['IncidentTags'] = self.incident_tags

        if self.incident_uuids_shrink is not None:
            result['IncidentUuids'] = self.incident_uuids_shrink

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction

        if self.order_field_name is not None:
            result['OrderFieldName'] = self.order_field_name

        if self.owners is not None:
            result['Owners'] = self.owners

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relate_asset_id is not None:
            result['RelateAssetId'] = self.relate_asset_id

        if self.relate_entity_id is not None:
            result['RelateEntityId'] = self.relate_entity_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')

        if m.get('IncidentStatus') is not None:
            self.incident_status = m.get('IncidentStatus')

        if m.get('IncidentStatusList') is not None:
            self.incident_status_list = m.get('IncidentStatusList')

        if m.get('IncidentTags') is not None:
            self.incident_tags = m.get('IncidentTags')

        if m.get('IncidentUuids') is not None:
            self.incident_uuids_shrink = m.get('IncidentUuids')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')

        if m.get('OrderFieldName') is not None:
            self.order_field_name = m.get('OrderFieldName')

        if m.get('Owners') is not None:
            self.owners = m.get('Owners')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelateAssetId') is not None:
            self.relate_asset_id = m.get('RelateAssetId')

        if m.get('RelateEntityId') is not None:
            self.relate_entity_id = m.get('RelateEntityId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')

        return self

