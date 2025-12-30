# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDefaultStorageLocationRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        path: str = None,
        storage_type: str = None,
    ):
        self.bucket = bucket
        self.path = path
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.path is not None:
            result['Path'] = self.path

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

