# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataSourcePropertiesRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        ds_id: str = None,
        quick_biowner_id: str = None,
        show_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.ds_id = ds_id
        self.quick_biowner_id = quick_biowner_id
        self.show_name = show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.quick_biowner_id is not None:
            result['QuickBIOwnerId'] = self.quick_biowner_id

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('QuickBIOwnerId') is not None:
            self.quick_biowner_id = m.get('QuickBIOwnerId')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        return self

