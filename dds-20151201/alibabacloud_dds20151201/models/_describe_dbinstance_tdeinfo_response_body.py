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
        # The custom key of the instance.
        # 
        # Currently, only the following regions support Bring Your Own Key (BYOK), which allows you to manage and own encryption keys:
        # - China (Hangzhou)
        # - China (Shanghai)
        # - China (Beijing)
        # - China (Shenzhen)
        # - Hong Kong (China)
        # - Singapore
        # - Malaysia (Kuala Lumpur)
        # 
        # > If BYOK is supported, you can manage and own the key, and the system returns your custom key. If BYOK is not supported, you cannot manage the key, and the system returns the string `NoActiveBYOK`.
        self.encryption_key = encryption_key
        # The encryption algorithm.
        self.encryptor_name = encryptor_name
        # The request ID.
        self.request_id = request_id
        # The global resource descriptor ARN (Alibaba Cloud Resource Name) of the role pending authorization.
        self.role_arn = role_arn
        # The TDE enabling status. Valid values:
        # - **enabled**: TDE is enabled.
        # - **disabled**: TDE is disabled.
        # 
        # > If the TDE status is disabled, the **RoleARN**, **EncryptionKey**, and **EncryptorName** parameters are not returned.
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

