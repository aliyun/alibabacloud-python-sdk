# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyOfficeSiteBridgeInfoRequest(DaraModel):
    def __init__(
        self,
        bridge_id: str = None,
        bridge_level: str = None,
        bridge_type: str = None,
        enable_bridge: bool = None,
        license: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The virtual bridge ID.
        self.bridge_id = bridge_id
        # The virtual bridge specifications.
        self.bridge_level = bridge_level
        # The third-party plugin type of the virtual bridge.
        self.bridge_type = bridge_type
        # Specifies whether to enable the bridge.
        self.enable_bridge = enable_bridge
        # The activation code object.
        self.license = license
        # The office network ID.
        self.office_site_id = office_site_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bridge_id is not None:
            result['BridgeId'] = self.bridge_id

        if self.bridge_level is not None:
            result['BridgeLevel'] = self.bridge_level

        if self.bridge_type is not None:
            result['BridgeType'] = self.bridge_type

        if self.enable_bridge is not None:
            result['EnableBridge'] = self.enable_bridge

        if self.license is not None:
            result['License'] = self.license

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BridgeId') is not None:
            self.bridge_id = m.get('BridgeId')

        if m.get('BridgeLevel') is not None:
            self.bridge_level = m.get('BridgeLevel')

        if m.get('BridgeType') is not None:
            self.bridge_type = m.get('BridgeType')

        if m.get('EnableBridge') is not None:
            self.enable_bridge = m.get('EnableBridge')

        if m.get('License') is not None:
            self.license = m.get('License')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

