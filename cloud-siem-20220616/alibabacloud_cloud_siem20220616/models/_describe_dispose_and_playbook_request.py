# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDisposeAndPlaybookRequest(DaraModel):
    def __init__(
        self,
        available_only: bool = None,
        current_page: int = None,
        entity_type: str = None,
        entity_uuid: str = None,
        entity_uuid_list: str = None,
        incident_uuid: str = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        self.available_only = available_only
        # The current page number. The value must be greater than or equal to 1.
        self.current_page = current_page
        # The entity type. Valid values:
        self.entity_type = entity_type
        # The entity UUID.
        self.entity_uuid = entity_uuid
        self.entity_uuid_list = entity_uuid_list
        # The incident UUID.
        self.incident_uuid = incident_uuid
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size
        # The region where the threat analysis data management center is located. Specify the management center region based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets are located in the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: Your assets are located outside China.
        self.region_id = region_id
        # The user ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_only is not None:
            result['AvailableOnly'] = self.available_only

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.entity_uuid_list is not None:
            result['EntityUuidList'] = self.entity_uuid_list

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableOnly') is not None:
            self.available_only = m.get('AvailableOnly')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('EntityUuidList') is not None:
            self.entity_uuid_list = m.get('EntityUuidList')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

