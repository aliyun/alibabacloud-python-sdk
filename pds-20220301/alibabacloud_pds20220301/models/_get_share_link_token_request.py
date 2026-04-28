# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetShareLinkTokenRequest(DaraModel):
    def __init__(
        self,
        expire_sec: int = None,
        share_id: str = None,
        share_pwd: str = None,
    ):
        # The validity period of the token. Valid values: (0,7200]. Default value: 7200. Unit: seconds.
        self.expire_sec = expire_sec
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id
        # The access code.
        self.share_pwd = share_pwd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec

        if self.share_id is not None:
            result['share_id'] = self.share_id

        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')

        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')

        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')

        return self

