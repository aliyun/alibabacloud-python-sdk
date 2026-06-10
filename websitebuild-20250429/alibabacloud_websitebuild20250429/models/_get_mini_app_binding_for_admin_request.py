# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMiniAppBindingForAdminRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        channel: str = None,
        platform_appid: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Channel
        self.channel = channel
        # Miniapp ID
        self.platform_appid = platform_appid

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

        if self.platform_appid is not None:
            result['PlatformAppid'] = self.platform_appid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('PlatformAppid') is not None:
            self.platform_appid = m.get('PlatformAppid')

        return self

