# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20250903 import models as main_models
from darabonba.model import DaraModel

class CreateComponentAssetRequest(DaraModel):
    def __init__(
        self,
        component_asset_name: str = None,
        component_asset_values: List[main_models.CreateComponentAssetRequestComponentAssetValues] = None,
        component_name: str = None,
        lang: str = None,
        role_for: int = None,
    ):
        # The name of the asset.
        # 
        # This parameter is required.
        self.component_asset_name = component_asset_name
        # Configuration information of the asset.
        # 
        # This parameter is required.
        self.component_asset_values = component_asset_values
        # The name of the component.
        # 
        # This parameter is required.
        self.component_name = component_name
        # The language type for receiving messages. Values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # Resource directory member account ID.
        self.role_for = role_for

    def validate(self):
        if self.component_asset_values:
            for v1 in self.component_asset_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_asset_name is not None:
            result['ComponentAssetName'] = self.component_asset_name

        result['ComponentAssetValues'] = []
        if self.component_asset_values is not None:
            for k1 in self.component_asset_values:
                result['ComponentAssetValues'].append(k1.to_map() if k1 else None)

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentAssetName') is not None:
            self.component_asset_name = m.get('ComponentAssetName')

        self.component_asset_values = []
        if m.get('ComponentAssetValues') is not None:
            for k1 in m.get('ComponentAssetValues'):
                temp_model = main_models.CreateComponentAssetRequestComponentAssetValues()
                self.component_asset_values.append(temp_model.from_map(k1))

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self



class CreateComponentAssetRequestComponentAssetValues(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        field_value: str = None,
    ):
        # Field name.
        # 
        # This parameter is required.
        self.field_name = field_name
        # Field value.
        # 
        # This parameter is required.
        self.field_value = field_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.field_value is not None:
            result['FieldValue'] = self.field_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')

        return self

