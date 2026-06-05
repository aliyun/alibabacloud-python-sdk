# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMiniAppBindingRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        channel: str = None,
        setting_key: str = None,
        setting_value: str = None,
    ):
        self.biz_id = biz_id
        self.channel = channel
        self.setting_key = setting_key
        self.setting_value = setting_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.setting_key is not None:
            result['SettingKey'] = self.setting_key

        if self.setting_value is not None:
            result['SettingValue'] = self.setting_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('SettingKey') is not None:
            self.setting_key = m.get('SettingKey')

        if m.get('SettingValue') is not None:
            self.setting_value = m.get('SettingValue')

        return self

