# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnRegisterApAssetRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        asset_apgroup_id: int = None,
        category: int = None,
        id: int = None,
        mac: str = None,
        serial_no: str = None,
        use_for: int = None,
    ):
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        self.asset_apgroup_id = asset_apgroup_id
        self.category = category
        self.id = id
        # This parameter is required.
        self.mac = mac
        self.serial_no = serial_no
        self.use_for = use_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.asset_apgroup_id is not None:
            result['AssetApgroupId'] = self.asset_apgroup_id

        if self.category is not None:
            result['Category'] = self.category

        if self.id is not None:
            result['Id'] = self.id

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no

        if self.use_for is not None:
            result['UseFor'] = self.use_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AssetApgroupId') is not None:
            self.asset_apgroup_id = m.get('AssetApgroupId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')

        if m.get('UseFor') is not None:
            self.use_for = m.get('UseFor')

        return self

