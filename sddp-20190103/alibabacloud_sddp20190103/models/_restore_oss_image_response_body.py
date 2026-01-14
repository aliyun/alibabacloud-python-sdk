# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreOssImageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        restored_image_key: str = None,
    ):
        self.request_id = request_id
        self.restored_image_key = restored_image_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.restored_image_key is not None:
            result['RestoredImageKey'] = self.restored_image_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RestoredImageKey') is not None:
            self.restored_image_key = m.get('RestoredImageKey')

        return self

