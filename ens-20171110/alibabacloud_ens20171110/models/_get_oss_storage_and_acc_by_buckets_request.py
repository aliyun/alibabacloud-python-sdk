# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOssStorageAndAccByBucketsRequest(DaraModel):
    def __init__(
        self,
        bucket_list: str = None,
    ):
        # The information about the bucket.
        self.bucket_list = bucket_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_list is not None:
            result['BucketList'] = self.bucket_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketList') is not None:
            self.bucket_list = m.get('BucketList')

        return self

