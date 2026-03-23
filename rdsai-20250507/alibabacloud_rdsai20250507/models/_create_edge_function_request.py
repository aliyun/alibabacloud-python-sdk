# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class CreateEdgeFunctionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        code: main_models.CreateEdgeFunctionRequestCode = None,
        custom_config: Dict[str, int] = None,
        edge_function_name: str = None,
        envs: Dict[str, str] = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The code parameters.
        self.code = code
        # The configuration parameters of the edge function.
        self.custom_config = custom_config
        # The name of the function.
        self.edge_function_name = edge_function_name
        # The environment variables.
        self.envs = envs
        # The ID of the RDS Supabase instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.code:
            self.code.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.code is not None:
            result['Code'] = self.code.to_map()

        if self.custom_config is not None:
            result['CustomConfig'] = self.custom_config

        if self.edge_function_name is not None:
            result['EdgeFunctionName'] = self.edge_function_name

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Code') is not None:
            temp_model = main_models.CreateEdgeFunctionRequestCode()
            self.code = temp_model.from_map(m.get('Code'))

        if m.get('CustomConfig') is not None:
            self.custom_config = m.get('CustomConfig')

        if m.get('EdgeFunctionName') is not None:
            self.edge_function_name = m.get('EdgeFunctionName')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateEdgeFunctionRequestCode(DaraModel):
    def __init__(
        self,
        download_url: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        oss_type: str = None,
    ):
        self.download_url = download_url
        # The name of the OSS bucket.
        self.oss_bucket_name = oss_bucket_name
        # The OSS path of a code file.
        self.oss_object_name = oss_object_name
        # The storage class of the OSS bucket.
        self.oss_type = oss_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_object_name is not None:
            result['OssObjectName'] = self.oss_object_name

        if self.oss_type is not None:
            result['OssType'] = self.oss_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssObjectName') is not None:
            self.oss_object_name = m.get('OssObjectName')

        if m.get('OssType') is not None:
            self.oss_type = m.get('OssType')

        return self

