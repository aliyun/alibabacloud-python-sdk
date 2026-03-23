# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NewApgroupConfigRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        name: str = None,
        parent_apgroup_id: str = None,
    ):
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.parent_apgroup_id = parent_apgroup_id

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

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_apgroup_id is not None:
            result['ParentApgroupId'] = self.parent_apgroup_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentApgroupId') is not None:
            self.parent_apgroup_id = m.get('ParentApgroupId')

        return self

