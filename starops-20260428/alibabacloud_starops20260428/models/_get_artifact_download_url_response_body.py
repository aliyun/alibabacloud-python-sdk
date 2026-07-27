# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetArtifactDownloadUrlResponseBody(DaraModel):
    def __init__(
        self,
        expire: int = None,
        request_id: str = None,
        url: str = None,
    ):
        self.expire = expire
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire is not None:
            result['expire'] = self.expire

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire') is not None:
            self.expire = m.get('expire')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

