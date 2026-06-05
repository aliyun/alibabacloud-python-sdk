# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMiniAppBindingShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        channel: str = None,
        setting_keys_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.channel = channel
        self.setting_keys_shrink = setting_keys_shrink

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

        if self.setting_keys_shrink is not None:
            result['SettingKeys'] = self.setting_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('SettingKeys') is not None:
            self.setting_keys_shrink = m.get('SettingKeys')

        return self

