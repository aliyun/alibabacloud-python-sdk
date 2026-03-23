# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAttachmentUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        access_file_url: str = None,
        object_key: str = None,
        put_object_url: str = None,
        request_id: str = None,
    ):
        self.access_file_url = access_file_url
        self.object_key = object_key
        self.put_object_url = put_object_url
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

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.put_object_url is not None:
            result['PutObjectUrl'] = self.put_object_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessFileUrl') is not None:
            self.access_file_url = m.get('AccessFileUrl')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('PutObjectUrl') is not None:
            self.put_object_url = m.get('PutObjectUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

