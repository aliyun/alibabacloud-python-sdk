# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class GetOssStorageAndAccByBucketsResponseBody(DaraModel):
    def __init__(
        self,
        bucket_list: List[main_models.GetOssStorageAndAccByBucketsResponseBodyBucketList] = None,
        request_id: str = None,
    ):
        # The information about the bucket.
        self.bucket_list = bucket_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.bucket_list:
            for v1 in self.bucket_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BucketList'] = []
        if self.bucket_list is not None:
            for k1 in self.bucket_list:
                result['BucketList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bucket_list = []
        if m.get('BucketList') is not None:
            for k1 in m.get('BucketList'):
                temp_model = main_models.GetOssStorageAndAccByBucketsResponseBodyBucketList()
                self.bucket_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetOssStorageAndAccByBucketsResponseBodyBucketList(DaraModel):
    def __init__(
        self,
        acc: int = None,
        bucket: str = None,
        storage_usage_byte: int = None,
    ):
        # The number of times that the bucket is accessed.
        self.acc = acc
        # The name of the bucket.
        self.bucket = bucket
        # The storage usage of the bucket. Unit: bytes.
        self.storage_usage_byte = storage_usage_byte

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.storage_usage_byte is not None:
            result['StorageUsageByte'] = self.storage_usage_byte

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('StorageUsageByte') is not None:
            self.storage_usage_byte = m.get('StorageUsageByte')

        return self

