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
        # The name of the OSS bucket you created.
        self.bucket = bucket
        # - When storageType is set to user_oss_bucket, temporary files are stored under this path. If path is empty or set to /, files are stored in the root directory.
        # 
        # - This field does not take effect for VOD storage.
        self.path = path
        # Storage type:
        # 
        # - **vod_oss_bucket**: VOD-managed bucket.<br>
        #   Supports adding buckets managed by the VOD system or OSS buckets added within the VOD system. If no active buckets are available, you can add a new bucket in the ApsaraVideo VOD console. After activating ApsaraVideo VOD, the system assigns a storage address in each storage region. You must enable this address before use. For details, see [Manage Storage Buckets](https://help.aliyun.com/document_detail/86097.html).
        # 
        # - **user_oss_bucket**: User private bucket. Before adding an Object Storage address, you must activate Object Storage Service (OSS) and create a bucket. For details, see [Create a Bucket in the Console](https://help.aliyun.com/document_detail/31885.html).
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

