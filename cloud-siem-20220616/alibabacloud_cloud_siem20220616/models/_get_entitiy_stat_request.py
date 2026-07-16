# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEntitiyStatRequest(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        asset_uuid: str = None,
        entity_name: str = None,
        entity_type: str = None,
        entity_uuid: str = None,
        incident_uuid: str = None,
        is_asset: str = None,
        is_malware_entity: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
        tags: str = None,
    ):
        # The asset ID associated with the incident.
        self.asset_name = asset_name
        # The asset ID associated with the incident.
        self.asset_uuid = asset_uuid
        # The asset ID associated with the incident.
        self.entity_name = entity_name
        # The asset ID associated with the incident.
        self.entity_type = entity_type
        # The asset ID associated with the incident.
        self.entity_uuid = entity_uuid
        # The incident ID.
        # 
        # This parameter is required.
        self.incident_uuid = incident_uuid
        # The asset ID associated with the incident.
        self.is_asset = is_asset
        # The sort order of the incident list. Valid values:
        # 
        # - desc: descending order.
        # - asc: ascending order.
        self.is_malware_entity = is_malware_entity
        # The region where the threat detection and response data management center resides. Select the management center based on the region of your assets. Valid values:
        # 
        # - cn-hangzhou: the asset belongs to the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: the asset belongs to a region outside the Chinese mainland.
        self.region_id = region_id
        # The user ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type. Valid values:
        # 
        # - 0: single-account logon.
        # - 1: global view.
        # - 2: switched view.
        # - 3: partial view.
        self.role_type = role_type
        # The entity tags. The value is a JSON array string in the following format: \\"[{\\"tagKey1\\":\\"tagValue1\\"},{\\"tagKey2\\":\\"tagValue2\\"}]\\"
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_uuid is not None:
            result['AssetUuid'] = self.asset_uuid

        if self.entity_name is not None:
            result['EntityName'] = self.entity_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_uuid is not None:
            result['EntityUuid'] = self.entity_uuid

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.is_asset is not None:
            result['IsAsset'] = self.is_asset

        if self.is_malware_entity is not None:
            result['IsMalwareEntity'] = self.is_malware_entity

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
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetUuid') is not None:
            self.asset_uuid = m.get('AssetUuid')

        if m.get('EntityName') is not None:
            self.entity_name = m.get('EntityName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityUuid') is not None:
            self.entity_uuid = m.get('EntityUuid')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('IsAsset') is not None:
            self.is_asset = m.get('IsAsset')

        if m.get('IsMalwareEntity') is not None:
            self.is_malware_entity = m.get('IsMalwareEntity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

