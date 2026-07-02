# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDeletionProtectionRequest(DaraModel):
    def __init__(
        self,
        deletion_protection_description: str = None,
        enable_deletion_protection: bool = None,
        key_id: str = None,
        kms_instance_id: str = None,
        protected_resource_arn: str = None,
    ):
        # The description of deletion protection.
        # 
        # > This parameter is available only when EnableDeletionProtection is set to true.
        self.deletion_protection_description = deletion_protection_description
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # - true: enables deletion protection.
        # 
        # - false: disables deletion protection. This is the default value.
        # 
        # This parameter is required.
        self.enable_deletion_protection = enable_deletion_protection
        # The ID of the key.
        self.key_id = key_id
        self.kms_instance_id = kms_instance_id
        # The ARN of the CMK for which you want to configure deletion protection.<br>
        # You can call the [DescribeKey](https://help.aliyun.com/document_detail/28952.html) operation to query the ARN of the CMK.<br><br>
        self.protected_resource_arn = protected_resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deletion_protection_description is not None:
            result['DeletionProtectionDescription'] = self.deletion_protection_description

        if self.enable_deletion_protection is not None:
            result['EnableDeletionProtection'] = self.enable_deletion_protection

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id

        if self.protected_resource_arn is not None:
            result['ProtectedResourceArn'] = self.protected_resource_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeletionProtectionDescription') is not None:
            self.deletion_protection_description = m.get('DeletionProtectionDescription')

        if m.get('EnableDeletionProtection') is not None:
            self.enable_deletion_protection = m.get('EnableDeletionProtection')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')

        if m.get('ProtectedResourceArn') is not None:
            self.protected_resource_arn = m.get('ProtectedResourceArn')

        return self

