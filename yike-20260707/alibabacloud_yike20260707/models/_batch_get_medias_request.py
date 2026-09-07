# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchGetMediasRequest(DaraModel):
    def __init__(
        self,
        auth_timeout: int = None,
        biz_config: str = None,
        media_ids: str = None,
        return_dynamic_meta: bool = None,
    ):
        # The validity period of the signed file access URL. Unit: seconds.
        self.auth_timeout = auth_timeout
        self.biz_config = biz_config
        # The IDs of the media assets to query, separated by commas.
        self.media_ids = media_ids
        self.return_dynamic_meta = return_dynamic_meta

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

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.return_dynamic_meta is not None:
            result['ReturnDynamicMeta'] = self.return_dynamic_meta

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthTimeout') is not None:
            self.auth_timeout = m.get('AuthTimeout')

        if m.get('BizConfig') is not None:
            self.biz_config = m.get('BizConfig')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('ReturnDynamicMeta') is not None:
            self.return_dynamic_meta = m.get('ReturnDynamicMeta')

        return self

