# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEncryptionKeyResponseBody(DaraModel):
    def __init__(
        self,
        creator: str = None,
        delete_date: str = None,
        description: str = None,
        encryption_key: str = None,
        encryption_key_status: str = None,
        encryption_name: str = None,
        key_usage: str = None,
        material_expire_time: str = None,
        origin: str = None,
        request_id: str = None,
        role_arn: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to create the custom key.
        self.creator = creator
        # The time when the custom key is expected to be deleted. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > If the return value is an empty string, the custom key cannot be automatically deleted.
        self.delete_date = delete_date
        # The description of the custom key. By default, an empty string is returned.
        self.description = description
        # The ID of the custom key.
        self.encryption_key = encryption_key
        # The state of the custom key. Valid values:
        # 
        # *   **Enabled**: The custom key is available.
        # *   **Disabled**: The custom key is unavailable.
        self.encryption_key_status = encryption_key_status
        # The encryption algorithm.
        self.encryption_name = encryption_name
        # The purpose of the custom key. A value of `ENCRYPT/DECRYPT` indicates encryption and decryption.
        self.key_usage = key_usage
        # The time when the custom key expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > If the return value is an empty string, the custom key does not expire.
        self.material_expire_time = material_expire_time
        # The source of the custom key. A value of **Aliyun_KMS** indicates [Key Management Service (KMS)](https://help.aliyun.com/document_detail/28935.html) of Alibaba Cloud.
        self.origin = origin
        # The ID of the request.
        self.request_id = request_id
        # The Alibaba Cloud Resource Name (ARN) of the Resource Access Management (RAM) role to which you want to grant permissions.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.delete_date is not None:
            result['DeleteDate'] = self.delete_date

        if self.description is not None:
            result['Description'] = self.description

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_key_status is not None:
            result['EncryptionKeyStatus'] = self.encryption_key_status

        if self.encryption_name is not None:
            result['EncryptionName'] = self.encryption_name

        if self.key_usage is not None:
            result['KeyUsage'] = self.key_usage

        if self.material_expire_time is not None:
            result['MaterialExpireTime'] = self.material_expire_time

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeleteDate') is not None:
            self.delete_date = m.get('DeleteDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionKeyStatus') is not None:
            self.encryption_key_status = m.get('EncryptionKeyStatus')

        if m.get('EncryptionName') is not None:
            self.encryption_name = m.get('EncryptionName')

        if m.get('KeyUsage') is not None:
            self.key_usage = m.get('KeyUsage')

        if m.get('MaterialExpireTime') is not None:
            self.material_expire_time = m.get('MaterialExpireTime')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

