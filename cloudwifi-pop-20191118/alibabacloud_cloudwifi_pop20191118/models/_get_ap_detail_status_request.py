# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApDetailStatusRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        mac: str = None,
        need_apgroup_info: bool = None,
        need_radio_status: bool = None,
    ):
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.mac = mac
        # This parameter is required.
        self.need_apgroup_info = need_apgroup_info
        # This parameter is required.
        self.need_radio_status = need_radio_status

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

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.need_apgroup_info is not None:
            result['NeedApgroupInfo'] = self.need_apgroup_info

        if self.need_radio_status is not None:
            result['NeedRadioStatus'] = self.need_radio_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('NeedApgroupInfo') is not None:
            self.need_apgroup_info = m.get('NeedApgroupInfo')

        if m.get('NeedRadioStatus') is not None:
            self.need_radio_status = m.get('NeedRadioStatus')

        return self

