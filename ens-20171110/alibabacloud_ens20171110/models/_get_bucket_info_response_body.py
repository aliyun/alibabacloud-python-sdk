# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class GetBucketInfoResponseBody(DaraModel):
    def __init__(
        self,
        bucket_info: main_models.GetBucketInfoResponseBodyBucketInfo = None,
        request_id: str = None,
    ):
        # The list of bucket information.
        self.bucket_info = bucket_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.bucket_info:
            self.bucket_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_info is not None:
            result['BucketInfo'] = self.bucket_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketInfo') is not None:
            temp_model = main_models.GetBucketInfoResponseBodyBucketInfo()
            self.bucket_info = temp_model.from_map(m.get('BucketInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetBucketInfoResponseBodyBucketInfo(DaraModel):
    def __init__(
        self,
        bucket_acl: str = None,
        bucket_name: str = None,
        comment: str = None,
        create_time: str = None,
        logical_bucket_type: str = None,
        modify_time: str = None,
    ):
        # The ACL of the bucket.
        # 
        # *   **public-read-write**
        # *   **public-read**
        # *   **private** (default)
        self.bucket_acl = bucket_acl
        # The name of the bucket.
        self.bucket_name = bucket_name
        # The remarks.
        self.comment = comment
        # The time when the bucket was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # Single-node storage. Set the value to sink.
        self.logical_bucket_type = logical_bucket_type
        # The time when the bucket was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modify_time = modify_time

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.logical_bucket_type is not None:
            result['LogicalBucketType'] = self.logical_bucket_type

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketAcl') is not None:
            self.bucket_acl = m.get('BucketAcl')

        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LogicalBucketType') is not None:
            self.logical_bucket_type = m.get('LogicalBucketType')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        return self

