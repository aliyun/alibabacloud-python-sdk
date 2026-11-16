# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        biz_config: str = None,
        input_url: str = None,
        media_id: str = None,
    ):
        # Specifies the validity period, in seconds, of the file URL that requires authentication for access.
        self.auth_timeout = auth_timeout
        self.biz_config = biz_config
        # This parameter is currently unavailable.
        self.input_url = input_url
        # The ID of the media asset. If this parameter is specified, the query is performed based on this ID and the system verifies whether it is a valid media asset ID.
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.biz_config is not None:
            result['BizConfig'] = self.biz_config

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('BizConfig') is not None:
            self.biz_config = m.get('BizConfig')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

