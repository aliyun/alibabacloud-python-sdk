# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceStorageConfigResponseBody(DaraModel):
    def __init__(
        self,
        config_list: List[main_models.DescribeInstanceStorageConfigResponseBodyConfigList] = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        # The storage configurations.
        self.config_list = config_list
        # The ID of the RDS Supabase instance.
        self.instance_name = instance_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.DescribeInstanceStorageConfigResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceStorageConfigResponseBodyConfigList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The configuration item name. Valid values:
        # 
        # *   **AWS_SESSION_TOKEN**: temporary OSS access token (session token).
        # *   **AWS_ACCESS_KEY_ID**: the AccessKey ID of OSS.
        # *   **AWS_SECRET_ACCESS_KEY**: the AccessKey secret of OSS.
        # *   **GLOBAL_S3_BUCKET**: the name of the OSS bucket.
        # *   **TENANT_ID**: the tenant ID of the OSS Prefix (prefix or directory).
        # *   **GLOBAL_S3_ENDPOINT**: the endpoint of OSS.
        # *   **REGION**: the region of OSS.
        self.name = name
        # The value of the configuration item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

