# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteObjectRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        object_key: str = None,
    ):
        # The name of the bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The name of the file.
        # 
        # This parameter is required.
        self.object_key = object_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        return self

