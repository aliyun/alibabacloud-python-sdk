# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutBucketAclRequest(DaraModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
    ):
        # The access control list (ACL) of the bucket.
        # 
        # *   **public-read-write**
        # *   **public-read**
        # *   **private** (default)
        # 
        # This parameter is required.
        self.bucket_acl = bucket_acl
        # The name of the bucket.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_acl is not None:
            result['BucketAcl'] = self.bucket_acl

        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        return self

