# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class GetSecretValueResponseBody(DaraModel):
    def __init__(
        self,
        automatic_rotation: str = None,
        create_time: str = None,
        extended_config: str = None,
        last_rotation_date: str = None,
        next_rotation_date: str = None,
        request_id: str = None,
        rotation_interval: str = None,
        secret_data: str = None,
        secret_data_type: str = None,
        secret_name: str = None,
        secret_type: str = None,
        version_id: str = None,
        version_stages: main_models.GetSecretValueResponseBodyVersionStages = None,
    ):
        # Indicates whether automatic rotation is enabled. Valid values:  
        # - Enabled: Automatic rotation is enabled.  
        # - Disabled: Automatic rotation is disabled.  
        # - Invalid: The rotation status is abnormal, and KMS cannot automatically rotate the credential for you.  
        # 
        # > This parameter is returned only for RDS credentials, PolarDB credentials, Redis/Tair credentials, RAM credentials, or ECS credentials.
        self.automatic_rotation = automatic_rotation
        # The time when the credential was created.
        self.create_time = create_time
        # The extended configuration of the credential.  
        # 
        # > This parameter is returned only for RDS credentials, PolarDB credentials, Redis/Tair credentials, RAM credentials, or ECS credentials when FetchExtendedConfig is set to true.
        self.extended_config = extended_config
        # The time of the most recent rotation.  
        # 
        # > This parameter is returned only if the credential has been rotated.
        self.last_rotation_date = last_rotation_date
        # The time of the next rotation.  
        # 
        # > This parameter is returned only when automatic rotation is enabled.
        self.next_rotation_date = next_rotation_date
        # The ID of the current request. Alibaba Cloud generates a unique identifier for each request, which can be used for troubleshooting and issue tracking.
        self.request_id = request_id
        # The epoch for automatic credential rotation.    
        # The format is `integer[unit]`, where `integer` indicates the time duration and `unit` indicates the time unit. Valid value for `unit`: s (seconds). For example, a 7-day rotation epoch is 604800s.
        # 
        # > This parameter is returned only when automatic rotation is enabled.
        self.rotation_interval = rotation_interval
        # The value of the credential. KMS decrypts the stored ciphertext and returns this parameter.  
        # 
        # - For generic secrets, the credential value you specified is returned.  
        # 
        # - For RDS credentials and Redis/Tair credentials, the credential value is in the format: `{"AccountName":"","AccountPassword":""}`.  
        # 
        # - For RAM credentials, the credential value is in the format: `{"AccessKeyId":"Adfdsfd","AccessKeySecret":"fdsfdsf","GenerateTimestamp": "2023-03-25T10:42:40Z"}`.  
        # 
        # - For ECS credentials, the credential value is in one of the following formats:  
        #   - Security token type: `{"UserName":"ecs-user","Password":"H5asdasdsads****"}`.  
        #   - Public-private key pair type (private key in PEM format): `{"UserName":"ecs-user","PublicKey":"ssh-rsa ****mKwnVix9YTFY9Rs= imported-openssh-key","PrivateKey": "d6bee1cb-2e14-4277-ba6b-73786b21****"}`.  
        # 
        # - For PolarDB credentials, the credential value is in the format: `{"AccountName":"","AccountPassword":""}`.
        self.secret_data = secret_data
        # The value type of the credential. Valid values:
        # - text
        # - binary
        self.secret_data_type = secret_data_type
        # The name of the credential.
        self.secret_name = secret_name
        # The type of the credential. Valid values:
        # - Generic: generic secret.  
        # - Rds: RDS credential.  
        # - Redis: Redis/Tair credential.
        # - RAMCredentials: RAM credential.  
        # - ECS: ECS credential.
        # - PolarDB: PolarDB credential.
        self.secret_type = secret_type
        # The version number of the credential.
        self.version_id = version_id
        self.version_stages = version_stages

    def validate(self):
        if self.version_stages:
            self.version_stages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.automatic_rotation is not None:
            result['AutomaticRotation'] = self.automatic_rotation

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extended_config is not None:
            result['ExtendedConfig'] = self.extended_config

        if self.last_rotation_date is not None:
            result['LastRotationDate'] = self.last_rotation_date

        if self.next_rotation_date is not None:
            result['NextRotationDate'] = self.next_rotation_date

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval

        if self.secret_data is not None:
            result['SecretData'] = self.secret_data

        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.secret_type is not None:
            result['SecretType'] = self.secret_type

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_stages is not None:
            result['VersionStages'] = self.version_stages.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutomaticRotation') is not None:
            self.automatic_rotation = m.get('AutomaticRotation')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExtendedConfig') is not None:
            self.extended_config = m.get('ExtendedConfig')

        if m.get('LastRotationDate') is not None:
            self.last_rotation_date = m.get('LastRotationDate')

        if m.get('NextRotationDate') is not None:
            self.next_rotation_date = m.get('NextRotationDate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')

        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')

        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionStages') is not None:
            temp_model = main_models.GetSecretValueResponseBodyVersionStages()
            self.version_stages = temp_model.from_map(m.get('VersionStages'))

        return self

class GetSecretValueResponseBodyVersionStages(DaraModel):
    def __init__(
        self,
        version_stage: List[str] = None,
    ):
        self.version_stage = version_stage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version_stage is not None:
            result['VersionStage'] = self.version_stage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionStage') is not None:
            self.version_stage = m.get('VersionStage')

        return self

