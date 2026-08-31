# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MiguSourceDownloadDTO(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        expires_at: str = None,
        method: str = None,
        source_id: str = None,
    ):
        # The OSS pre-signed download URL.
        self.download_url = download_url
        # The expiration time of the download URL, in RFC 3339 format.
        self.expires_at = expires_at
        # The download request method. The value is fixed to GET.
        self.method = method
        # The unique identifier of the source file.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.expires_at is not None:
            result['expiresAt'] = self.expires_at

        if self.method is not None:
            result['method'] = self.method

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('expiresAt') is not None:
            self.expires_at = m.get('expiresAt')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        return self

