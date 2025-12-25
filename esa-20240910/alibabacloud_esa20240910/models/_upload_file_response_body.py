# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadFileResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        upload_id: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the file upload task. You can use this ID for task submission or query subsequently.
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.upload_id is not None:
            result['UploadId'] = self.upload_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UploadId') is not None:
            self.upload_id = m.get('UploadId')

        return self

