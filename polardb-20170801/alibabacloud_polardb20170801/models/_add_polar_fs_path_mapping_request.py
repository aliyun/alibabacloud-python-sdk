# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class AddPolarFsPathMappingRequest(DaraModel):
    def __init__(
        self,
        custom_bucket_path_list: List[main_models.AddPolarFsPathMappingRequestCustomBucketPathList] = None,
        dbcluster_id: str = None,
        polar_fs_instance_id: str = None,
    ):
        # The bucket and corresponding path information.
        self.custom_bucket_path_list = custom_bucket_path_list
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The PolarFS instance ID.
        # 
        # This parameter is required.
        self.polar_fs_instance_id = polar_fs_instance_id

    def validate(self):
        if self.custom_bucket_path_list:
            for v1 in self.custom_bucket_path_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomBucketPathList'] = []
        if self.custom_bucket_path_list is not None:
            for k1 in self.custom_bucket_path_list:
                result['CustomBucketPathList'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.polar_fs_instance_id is not None:
            result['PolarFsInstanceId'] = self.polar_fs_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_bucket_path_list = []
        if m.get('CustomBucketPathList') is not None:
            for k1 in m.get('CustomBucketPathList'):
                temp_model = main_models.AddPolarFsPathMappingRequestCustomBucketPathList()
                self.custom_bucket_path_list.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PolarFsInstanceId') is not None:
            self.polar_fs_instance_id = m.get('PolarFsInstanceId')

        return self



class AddPolarFsPathMappingRequestCustomBucketPathList(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        bucket_access_key_id: str = None,
        bucket_access_key_secret: str = None,
        path: str = None,
    ):
        # The bucket name.
        self.bucket = bucket
        self.bucket_access_key_id = bucket_access_key_id
        self.bucket_access_key_secret = bucket_access_key_secret
        # The custom storage path.
        self.path = path

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

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BucketAccessKeyId') is not None:
            self.bucket_access_key_id = m.get('BucketAccessKeyId')

        if m.get('BucketAccessKeySecret') is not None:
            self.bucket_access_key_secret = m.get('BucketAccessKeySecret')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

