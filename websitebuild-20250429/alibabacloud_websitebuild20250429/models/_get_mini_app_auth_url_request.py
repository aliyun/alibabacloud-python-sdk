# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMiniAppAuthUrlRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        channel: str = None,
        redirect_uri: str = None,
    ):
        # Site ID
        self.biz_id = biz_id
        # Channel information
        self.channel = channel
        # Hyperlink URL
        self.redirect_uri = redirect_uri

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

        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')

        return self

