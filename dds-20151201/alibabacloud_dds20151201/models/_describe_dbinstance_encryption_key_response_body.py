# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceEncryptionKeyResponseBody(DaraModel):
    def __init__(
        self,
        creator: str = None,
        delete_date: str = None,
        description: str = None,
        encryption_key: str = None,
        encryption_key_status: str = None,
        key_usage: str = None,
        material_expire_time: str = None,
        origin: str = None,
        request_id: str = None,
    ):
        # The UID of the key creator.
        self.creator = creator
        # The scheduled time when the key for the instance will be deleted. If the parameter is left empty, the key will not be deleted.
        self.delete_date = delete_date
        # The description of the key for the instance.
        self.description = description
        # The key for the instance.
        self.encryption_key = encryption_key
        # Indicates whether the key for the instance is enabled. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.encryption_key_status = encryption_key_status
        # The purpose of the key for the instance.
        self.key_usage = key_usage
        # The expiration time of the key for the instance. The time is displayed in UTC. If the parameter is left empty, the key for the instance will not expire.
        self.material_expire_time = material_expire_time
        # The source of the key for the instance.
        self.origin = origin
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date

        if self.description is not None:
            result['Description'] = self.description

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status

        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage

        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')

        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')

        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

