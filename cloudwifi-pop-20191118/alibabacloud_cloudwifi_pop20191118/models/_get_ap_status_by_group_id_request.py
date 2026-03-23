# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApStatusByGroupIdRequest(DaraModel):
    def __init__(
        self,
        apgroup_id: str = None,
        app_code: str = None,
        app_name: str = None,
        cursor: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.apgroup_id = apgroup_id
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cursor = cursor
        # This parameter is required.
        self.page_size = page_size

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

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cursor is not None:
            result['Cursor'] = self.cursor

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

