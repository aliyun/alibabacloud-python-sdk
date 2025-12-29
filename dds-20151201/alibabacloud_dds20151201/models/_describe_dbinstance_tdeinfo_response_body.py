# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBInstanceTDEInfoResponseBody(DaraModel):
    def __init__(
        self,
        encryption_key: str = None,
        encryptor_name: str = None,
        request_id: str = None,
        role_arn: str = None,
        tdestatus: str = None,
    ):
        # 实例的自定义密钥。
        # 
        # 目前仅以下地域支持BYOK（Bring Your Own Key，用户可以自行管理和拥有加密密钥）：
        # - 华东1（杭州）
        # - 华东2（上海）
        # - 华北2（北京）
        # - 华南1（深圳）
        # - 中国（香港）
        # - 新加坡
        # - 马来西亚（吉隆坡）
        # 
        # > 支持BYOK，用户可以管理且拥有密钥，系统将返回用户的自定义密钥；不支持BYOK，用户不可管理密钥，系统将返回字符串`NoActiveBYOK`。
        self.encryption_key = encryption_key
        # 加密算法。
        self.encryptor_name = encryptor_name
        # The request ID.
        self.request_id = request_id
        # 指定待授权角色的全局资源描述符ARN（Alibaba Cloud Resource Name）信息。
        self.role_arn = role_arn
        # The TDE status. Valid values:
        # 
        # *   **enabled**
        # *   **disabled**
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryptor_name is not None:
            result['EncryptorName'] = self.encryptor_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_arn is not None:
            result['RoleARN'] = self.role_arn

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptorName') is not None:
            self.encryptor_name = m.get('EncryptorName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleARN') is not None:
            self.role_arn = m.get('RoleARN')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

