# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEncryptionDBSecretResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        encryption_dbregion: str = None,
        encryption_dbstatus: str = None,
        encryption_key: str = None,
        encryption_key_status: str = None,
        request_id: str = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.encryption_dbregion = encryption_dbregion
        self.encryption_dbstatus = encryption_dbstatus
        self.encryption_key = encryption_key
        self.encryption_key_status = encryption_key_status
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.encryption_dbregion is not None:
            result['EncryptionDBRegion'] = self.encryption_dbregion

        if self.encryption_dbstatus is not None:
            result['EncryptionDBStatus'] = self.encryption_dbstatus

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EncryptionDBRegion') is not None:
            self.encryption_dbregion = m.get('EncryptionDBRegion')

        if m.get('EncryptionDBStatus') is not None:
            self.encryption_dbstatus = m.get('EncryptionDBStatus')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

