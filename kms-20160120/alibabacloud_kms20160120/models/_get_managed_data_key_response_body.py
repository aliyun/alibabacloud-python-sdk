# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetManagedDataKeyResponseBody(DaraModel):
    def __init__(
        self,
        data_key_name: str = None,
        data_key_version_id: str = None,
        data_key_version_name: str = None,
        plaintext: str = None,
        request_id: str = None,
    ):
        # The name of the managed data key (DK).
        self.data_key_name = data_key_name
        # The version number of the returned managed data key (DK).
        self.data_key_version_id = data_key_version_id
        # The credential name that stores the key material of the returned managed data key (DK) version.
        self.data_key_version_name = data_key_version_name
        # The Base64-encoding plaintext value of the data key (DK).
        self.plaintext = plaintext
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use the request ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_key_name is not None:
            result['DataKeyName'] = self.data_key_name

        if self.data_key_version_id is not None:
            result['DataKeyVersionId'] = self.data_key_version_id

        if self.data_key_version_name is not None:
            result['DataKeyVersionName'] = self.data_key_version_name

        if self.plaintext is not None:
            result['Plaintext'] = self.plaintext

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataKeyName') is not None:
            self.data_key_name = m.get('DataKeyName')

        if m.get('DataKeyVersionId') is not None:
            self.data_key_version_id = m.get('DataKeyVersionId')

        if m.get('DataKeyVersionName') is not None:
            self.data_key_version_name = m.get('DataKeyVersionName')

        if m.get('Plaintext') is not None:
            self.plaintext = m.get('Plaintext')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

