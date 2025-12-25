# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindAliasRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        app_key: int = None,
        device_id: str = None,
        unbind_all: bool = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id
        self.unbind_all = unbind_all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.unbind_all is not None:
            result['UnbindAll'] = self.unbind_all

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('UnbindAll') is not None:
            self.unbind_all = m.get('UnbindAll')

        return self

