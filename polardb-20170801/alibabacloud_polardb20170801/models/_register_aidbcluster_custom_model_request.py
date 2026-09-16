# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterAIDBClusterCustomModelRequest(DaraModel):
    def __init__(
        self,
        custom_oss_bucket_name: str = None,
        custom_oss_bucket_path: str = None,
        dbcluster_id: str = None,
        display_model_name: str = None,
        model_name: str = None,
        region_id: str = None,
    ):
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.custom_oss_bucket_name = custom_oss_bucket_name
        # The model path within the OSS bucket.
        # 
        # This parameter is required.
        self.custom_oss_bucket_path = custom_oss_bucket_path
        # The ID of the PolarDB AI 3.0 logical instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The display name shown in the candidate list and the initial client-facing invocation name.
        self.display_model_name = display_model_name
        # The custom model registration key and model directory name.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_oss_bucket_name is not None:
            result['CustomOssBucketName'] = self.custom_oss_bucket_name

        if self.custom_oss_bucket_path is not None:
            result['CustomOssBucketPath'] = self.custom_oss_bucket_path

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.display_model_name is not None:
            result['DisplayModelName'] = self.display_model_name

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomOssBucketName') is not None:
            self.custom_oss_bucket_name = m.get('CustomOssBucketName')

        if m.get('CustomOssBucketPath') is not None:
            self.custom_oss_bucket_path = m.get('CustomOssBucketPath')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DisplayModelName') is not None:
            self.display_model_name = m.get('DisplayModelName')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

