# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompleteCodeBundleRequest(DaraModel):
    def __init__(
        self,
        byte_size: int = None,
        content_type: str = None,
    ):
        # The declared size of the uploaded object. This value must match the OSS Content-Length.
        # 
        # This parameter is required.
        self.byte_size = byte_size
        # The MIME type of the stored code bundle. This is typically application/octet-stream for pre-signed PUT operations.
        # 
        # This parameter is required.
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.byte_size is not None:
            result['byteSize'] = self.byte_size

        if self.content_type is not None:
            result['contentType'] = self.content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('byteSize') is not None:
            self.byte_size = m.get('byteSize')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        return self

