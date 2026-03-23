# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AddApListToApgroupRequest(DaraModel):
    def __init__(
        self,
        ap_group_id: str = None,
        ap_mac_list: Dict[str, Any] = None,
        app_code: str = None,
        app_name: str = None,
    ):
        # This parameter is required.
        self.ap_group_id = ap_group_id
        # This parameter is required.
        self.ap_mac_list = ap_mac_list
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
        if self.ap_group_id is not None:
            result['ApGroupId'] = self.ap_group_id

        if self.ap_mac_list is not None:
            result['ApMacList'] = self.ap_mac_list

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupId') is not None:
            self.ap_group_id = m.get('ApGroupId')

        if m.get('ApMacList') is not None:
            self.ap_mac_list = m.get('ApMacList')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        return self

