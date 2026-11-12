# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ResetSystemRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        image_id: str = None,
        instance_id: str = None,
        login_credentials: main_models.ResetSystemRequestLoginCredentials = None,
        region_id: str = None,
    ):
        # The client token that you want to use to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The ID of the destination image. If you do not specify this parameter, the current image is reset.
        self.image_id = image_id
        # The ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The information about the logon credentials.
        self.login_credentials = login_credentials
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.login_credentials:
            self.login_credentials.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.login_credentials is not None:
            result['LoginCredentials'] = self.login_credentials.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LoginCredentials') is not None:
            temp_model = main_models.ResetSystemRequestLoginCredentials()
            self.login_credentials = temp_model.from_map(m.get('LoginCredentials'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ResetSystemRequestLoginCredentials(DaraModel):
    def __init__(
        self,
        key_pair_name: str = None,
        password: str = None,
    ):
        # The name of the key pair that you want to bind to the simple application server. Only Linux simple application servers support key pairs.
        self.key_pair_name = key_pair_name
        # The password that corresponds to the administrator.
        # 
        # - For Windows servers, the default administrator account is Administrator.
        # 
        # - Linux servers, the default administrator account is root.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.password is not None:
            result['Password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        return self

