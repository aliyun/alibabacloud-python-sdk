# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApgroupSsidConfigRequest(DaraModel):
    def __init__(
        self,
        ap_group_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        # This parameter is required.
        self.ap_group_uuid = ap_group_uuid
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

