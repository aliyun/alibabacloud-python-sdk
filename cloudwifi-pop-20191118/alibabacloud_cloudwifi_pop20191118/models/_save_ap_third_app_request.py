# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveApThirdAppRequest(DaraModel):
    def __init__(
        self,
        add_style: int = None,
        ap_asset_id: int = None,
        app_code: str = None,
        app_data: str = None,
        app_name: str = None,
        category: int = None,
        id: int = None,
        mac: str = None,
        third_app_name: str = None,
        version: str = None,
    ):
        self.add_style = add_style
        self.ap_asset_id = ap_asset_id
        # This parameter is required.
        self.app_code = app_code
        self.app_data = app_data
        # This parameter is required.
        self.app_name = app_name
        self.category = category
        self.id = id
        # This parameter is required.
        self.mac = mac
        self.third_app_name = third_app_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_style is not None:
            result['AddStyle'] = self.add_style

        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_data is not None:
            result['AppData'] = self.app_data

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.category is not None:
            result['Category'] = self.category

        if self.id is not None:
            result['Id'] = self.id

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.third_app_name is not None:
            result['ThirdAppName'] = self.third_app_name

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddStyle') is not None:
            self.add_style = m.get('AddStyle')

        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppData') is not None:
            self.app_data = m.get('AppData')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('ThirdAppName') is not None:
            self.third_app_name = m.get('ThirdAppName')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

