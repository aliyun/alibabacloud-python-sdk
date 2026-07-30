# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetMediasRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        media_ids: str = None,
    ):
        # The validity period of the signed file access URL. Unit: seconds.
        self.auth_timeout = auth_timeout
        # The IDs of the media assets to query, separated by commas.
        self.media_ids = media_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_timeout is not None:
            result['AuthTimeout'] = self.auth_timeout

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        return self

