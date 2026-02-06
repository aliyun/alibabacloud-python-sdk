# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDownloadSecretKeyResponseBody(DaraModel):
    def __init__(
        self,
        app_encrypt_key: str = None,
        request_id: str = None,
    ):
        # The key file for secure download.
        self.app_encrypt_key = app_encrypt_key
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_encrypt_key is not None:
            result['AppEncryptKey'] = self.app_encrypt_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppEncryptKey') is not None:
            self.app_encrypt_key = m.get('AppEncryptKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

