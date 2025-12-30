# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPlayInfoRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        input_url: str = None,
        media_id: str = None,
    ):
        self.auth_timeout = auth_timeout
        # The input URL that you specified for the media asset when you registered the media asset. For more information, see [RegisterMediaInfo](https://help.aliyun.com/document_detail/441152.html).
        # 
        # >  You must specify at least one of the MediaId and InputURL parameters.
        self.input_url = input_url
        # The ID of the media asset.
        # 
        # >  You must specify at least one of the MediaId and InputURL parameters.
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

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

