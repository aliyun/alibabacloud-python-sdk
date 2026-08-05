# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolarFsMappingAuthRequest(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        bucket_access_key_id: str = None,
        bucket_access_key_secret: str = None,
        dbcluster_id: str = None,
        path: str = None,
        polar_fs_instance_id: str = None,
    ):
        # The bucket name.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The AccessKey ID for the storage bucket.
        # 
        # This parameter is required.
        self.bucket_access_key_id = bucket_access_key_id
        # The AccessKey secret for the storage bucket.
        # 
        # This parameter is required.
        self.bucket_access_key_secret = bucket_access_key_secret
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query information about all clusters in a specified region, including the cluster ID.
        self.dbcluster_id = dbcluster_id
        # The destination path.
        # 
        # This parameter is required.
        self.path = path
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.bucket_access_key_id is not None:
            result['BucketAccessKeyId'] = self.bucket_access_key_id

        if self.bucket_access_key_secret is not None:
            result['BucketAccessKeySecret'] = self.bucket_access_key_secret

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.path is not None:
            result['Path'] = self.path

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BucketAccessKeyId') is not None:
            self.bucket_access_key_id = m.get('BucketAccessKeyId')

        if m.get('BucketAccessKeySecret') is not None:
            self.bucket_access_key_secret = m.get('BucketAccessKeySecret')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self

