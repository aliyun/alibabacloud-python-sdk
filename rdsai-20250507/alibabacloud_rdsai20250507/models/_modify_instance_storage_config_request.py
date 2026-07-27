# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceStorageConfigRequest(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        client_token: str = None,
        config_list: List[main_models.ModifyInstanceStorageConfigRequestConfigList] = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.branch_name = branch_name
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, which ensures that the request is not repeated.
        self.client_token = client_token
        # The list of storage configurations.
        self.config_list = config_list
        # The instance ID of the AI application.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The region ID.
        self.region_id = region_id

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
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.ModifyInstanceStorageConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyInstanceStorageConfigRequestConfigList(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the configuration item. Valid values:
        # 
        # - **AWS_SESSION_TOKEN** (optional): the temporary access token (Session Token) for OSS. If this parameter is not specified, AccessKey ID and AccessKey Secret are used for authentication.
        # - **AWS_ACCESS_KEY_ID**: the AccessKey ID for OSS.
        # - **AWS_SECRET_ACCESS_KEY**: the AccessKey Secret for OSS.
        # - **GLOBAL_S3_BUCKET**: the bucket name of OSS.
        # - **TENANT_ID**: the OSS directory name. You do not need to create it in advance.
        # - **GLOBAL_S3_ENDPOINT**: the endpoint of OSS.
        # - **REGION**: the region of OSS.
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

