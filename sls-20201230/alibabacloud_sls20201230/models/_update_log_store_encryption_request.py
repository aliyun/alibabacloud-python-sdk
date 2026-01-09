# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class UpdateLogStoreEncryptionRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        encrypt_type: str = None,
        user_cmk_info: main_models.UpdateLogStoreEncryptionRequestUserCmkInfo = None,
    ):
        # Specifies whether to enable the encryption feature. After you update the encryption configuration of the Logstore, you can modify only the enable parameter in subsequent update requests. You cannot modify the encryptType or userCmkInfo parameters.
        # 
        # This parameter is required.
        self.enable = enable
        # The encryption algorithm. Valid values: default, m4, sm4_ecb, sm4_cbc, sm4_gcm, aes_ecb, aes_cbc, aes_cfb, aes_ofb, and aes_gcm.
        self.encrypt_type = encrypt_type
        # Optional. If you use a BYOK key to encrypt logs, you must specify this parameter. If you use the service key of Simple Log Service to encrypt logs, you do not need to specify this parameter.
        self.user_cmk_info = user_cmk_info

    def validate(self):
        if self.user_cmk_info:
            self.user_cmk_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.encrypt_type is not None:
            result['encryptType'] = self.encrypt_type

        if self.user_cmk_info is not None:
            result['userCmkInfo'] = self.user_cmk_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('encryptType') is not None:
            self.encrypt_type = m.get('encryptType')

        if m.get('userCmkInfo') is not None:
            temp_model = main_models.UpdateLogStoreEncryptionRequestUserCmkInfo()
            self.user_cmk_info = temp_model.from_map(m.get('userCmkInfo'))

        return self

class UpdateLogStoreEncryptionRequestUserCmkInfo(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        region_id: str = None,
        role_arn: str = None,
    ):
        # The ID of the CMK to which the BYOK key belongs. You can create a CMK in KMS. The CMK must be in the same region as the endpoint of Simple Log Service.
        self.key_id = key_id
        # The region ID. Example: cn-hangzhou.
        self.region_id = region_id
        # The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role.The value is in the acs:ram::12344\\*\\*\\*:role/xxxxx format. To use a BYOK key to encrypt logs, you must create a RAM role and grant the AliyunKMSReadOnlyAccess and AliyunKMSCryptoUserAccess permissions to the RAM role. You must grant the API caller the PassRole permission on the RAM role.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['keyId'] = self.key_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyId') is not None:
            self.key_id = m.get('keyId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        return self

