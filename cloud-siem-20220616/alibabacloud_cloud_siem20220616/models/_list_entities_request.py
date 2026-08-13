# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEntitiesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        entity_uuids: str = None,
        incident_uuid: str = None,
        is_malware_entity: str = None,
        malware_type: str = None,
        page_size: int = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        tags: str = None,
    ):
        # The current page number, which must be greater than or equal to 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The entity name.
        self.entity_name = entity_name
        # The entity type. Valid values:
        self.entity_type = entity_type
        # The entity UUID.
        self.entity_uuid = entity_uuid
        # The list of entity UUIDs.
        self.entity_uuids = entity_uuids
        # The incident ID.
        # 
        # This parameter is required.
        self.incident_uuid = incident_uuid
        # Specifies whether the entity is malicious. Valid values:
        self.is_malware_entity = is_malware_entity
        # The malware entity type.
        self.malware_type = malware_type
        # The number of entries per page, up to a maximum of 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region where the data management center of threat analysis is located. Select the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: Your assets reside in regions outside the Chinese mainland.
        self.region_id = region_id
        # The user ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type.
        self.role_type = role_type
        # The entity tags. The value is a JSON array string:
        # 
        # `"[{"tagKey1":"tagValue1"},{"tagKey2":"tagValue2"}]"`
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.entity_uuids is not None:
            result['EntityUuids'] = self.entity_uuids

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.is_malware_entity is not None:
            result['IsMalwareEntity'] = self.is_malware_entity

        if self.malware_type is not None:
            result['MalwareType'] = self.malware_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('EntityUuids') is not None:
            self.entity_uuids = m.get('EntityUuids')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('IsMalwareEntity') is not None:
            self.is_malware_entity = m.get('IsMalwareEntity')

        if m.get('MalwareType') is not None:
            self.malware_type = m.get('MalwareType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

