# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTempDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        oss_key: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The OSS object key.
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        return self

