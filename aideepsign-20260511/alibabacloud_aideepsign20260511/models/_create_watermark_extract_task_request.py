# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWatermarkExtractTaskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        file_type: str = None,
        file_url: str = None,
        reserved: str = None,
    ):
        # A reserved idempotency field. Idempotency is not supported. Passing in a value does not cause an error, but it does not produce an idempotency effect.
        self.client_token = client_token
        # The file type. Valid values: `image` and `video`. The value must be the same as the `FileType` used when the watermark was embedded.
        # 
        # This parameter is required.
        self.file_type = file_type
        # The URL of the file from which the watermark is to be extracted. Images and videos are supported. Only the `http/https` protocol is supported. Videos must be no longer than 10 minutes and no larger than 100 MB.
        self.file_url = file_url
        # A reserved field. No valid values are available. Do not pass in this parameter.
        self.reserved = reserved

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        return self

