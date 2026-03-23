# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EditApgroupThirdAppRequest(DaraModel):
    def __init__(
        self,
        apgroup_id: int = None,
        app_code: str = None,
        app_data: str = None,
        app_name: str = None,
        apply_to_sub_group: int = None,
        category: int = None,
        config_type: str = None,
        id: int = None,
        inherit_parent_group: int = None,
        third_app_name: str = None,
    ):
        # This parameter is required.
        self.apgroup_id = apgroup_id
        # This parameter is required.
        self.app_code = app_code
        self.app_data = app_data
        # This parameter is required.
        self.app_name = app_name
        self.apply_to_sub_group = apply_to_sub_group
        self.category = category
        self.config_type = config_type
        self.id = id
        self.inherit_parent_group = inherit_parent_group
        self.third_app_name = third_app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_data is not None:
            result['AppData'] = self.app_data

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.apply_to_sub_group is not None:
            result['ApplyToSubGroup'] = self.apply_to_sub_group

        if self.category is not None:
            result['Category'] = self.category

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.id is not None:
            result['Id'] = self.id

        if self.inherit_parent_group is not None:
            result['InheritParentGroup'] = self.inherit_parent_group

        if self.third_app_name is not None:
            result['ThirdAppName'] = self.third_app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppData') is not None:
            self.app_data = m.get('AppData')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ApplyToSubGroup') is not None:
            self.apply_to_sub_group = m.get('ApplyToSubGroup')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InheritParentGroup') is not None:
            self.inherit_parent_group = m.get('InheritParentGroup')

        if m.get('ThirdAppName') is not None:
            self.third_app_name = m.get('ThirdAppName')

        return self

