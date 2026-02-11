# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAlertsRequest(DaraModel):
    def __init__(
        self,
        alert_name: str = None,
        alert_status: List[str] = None,
        alert_title: str = None,
        alert_type: str = None,
        alert_uuid: str = None,
        asset_id: str = None,
        asset_name: str = None,
        current_page: int = None,
        end_time: int = None,
        entity_id: str = None,
        entity_name: str = None,
        is_defend: str = None,
        label_type: str = None,
        level: List[str] = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        source: str = None,
        start_time: int = None,
        sub_user_id: str = None,
    ):
        self.alert_name = alert_name
        self.alert_status = alert_status
        # The title of the alert.
        self.alert_title = alert_title
        self.alert_type = alert_type
        # The UUID of the alert.
        self.alert_uuid = alert_uuid
        self.asset_id = asset_id
        self.asset_name = asset_name
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. Unit: milliseconds.
        self.end_time = end_time
        self.entity_id = entity_id
        self.entity_name = entity_name
        # Specifies whether an attack is defended. Valid values:
        # 
        # *   0: detected.
        # *   1: blocked.
        self.is_defend = is_defend
        self.label_type = label_type
        # The risk level. The value is a JSON array. Valid values:
        # 
        # *   serious: high
        # *   suspicious: medium
        # *   remind: low
        self.level = level
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
        # The source of the alert.
        self.source = source
        # The beginning of the time range to query. Unit: milliseconds.
        self.start_time = start_time
        # The ID of the Alibaba Cloud account within which the alert is generated.
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name

        if self.alert_status is not None:
            result['AlertStatus'] = self.alert_status

        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title

        if self.alert_type is not None:
            result['AlertType'] = self.alert_type

        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.is_defend is not None:
            result['IsDefend'] = self.is_defend

        if self.label_type is not None:
            result['LabelType'] = self.label_type

        if self.level is not None:
            result['Level'] = self.level

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')

        if m.get('AlertStatus') is not None:
            self.alert_status = m.get('AlertStatus')

        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')

        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')

        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('IsDefend') is not None:
            self.is_defend = m.get('IsDefend')

        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

