# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterApAssetRequest(DaraModel):
    def __init__(
        self,
        ap_group_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
        id: int = None,
        mac: str = None,
        serial_no: str = None,
    ):
        # This parameter is required.
        self.ap_group_uuid = ap_group_uuid
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        self.id = id
        # This parameter is required.
        self.mac = mac
        # This parameter is required.
        self.serial_no = serial_no

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

        if self.id is not None:
            result['Id'] = self.id

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')

        return self

