# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceCLSResponseBody(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        encryption_key: str = None,
        encryption_key_mode: str = None,
        request_id: str = None,
        white_list_mode: bool = None,
    ):
        self.algorithm = algorithm
        self.encryption_key = encryption_key
        self.encryption_key_mode = encryption_key_mode
        self.request_id = request_id
        self.white_list_mode = white_list_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_mode is not None:
            result['EncryptionKeyMode'] = self.encryption_key_mode

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.white_list_mode is not None:
            result['WhiteListMode'] = self.white_list_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyMode') is not None:
            self.encryption_key_mode = m.get('EncryptionKeyMode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WhiteListMode') is not None:
            self.white_list_mode = m.get('WhiteListMode')

        return self

