# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutBucketRequest(DaraModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
        comment: str = None,
        dispatch_scope: str = None,
        ens_region_id: str = None,
        logical_bucket_type: str = None,
    ):
        # Bucket permission type: private (default). public-read-write: Allows public read and write access. public-read: Allows public read access.
        self.bucket_acl = bucket_acl
        # Bucket name. Must be 3 to 50 characters long. Use only lowercase letters, numbers, and hyphens (-). Cannot start or end with a hyphen.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # Comment. Up to 128 characters, including letters, digits, Chinese characters, and emojis.
        self.comment = comment
        # Scheduling scope. Valid values:
        # 
        # - domestic (within China)
        # 
        # - outside China
        # 
        # > You must specify this parameter when creating a global bucket.
        self.dispatch_scope = dispatch_scope
        # Edge zone ID. If not specified, the global default edge zone is used.
        self.ens_region_id = ens_region_id
        # The logical type of the bucket. Valid values: sink: A sink bucket on a specified node. standard: A standard global bucket. This is the default value.
        self.logical_bucket_type = logical_bucket_type

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

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.dispatch_scope is not None:
            result['DispatchScope'] = self.dispatch_scope

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.logical_bucket_type is not None:
            result['LogicalBucketType'] = self.logical_bucket_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DispatchScope') is not None:
            self.dispatch_scope = m.get('DispatchScope')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('LogicalBucketType') is not None:
            self.logical_bucket_type = m.get('LogicalBucketType')

        return self

