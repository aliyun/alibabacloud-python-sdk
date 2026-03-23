# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAttachmentUrlResponseBody(DaraModel):
    def __init__(
        self,
        access_file_url: str = None,
        request_id: str = None,
    ):
        self.access_file_url = access_file_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_file_url is not None:
            result['AccessFileUrl'] = self.access_file_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessFileUrl') is not None:
            self.access_file_url = m.get('AccessFileUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

