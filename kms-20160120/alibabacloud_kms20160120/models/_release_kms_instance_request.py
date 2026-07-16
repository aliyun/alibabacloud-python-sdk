# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseKmsInstanceRequest(DaraModel):
    def __init__(
        self,
        force_delete_without_backup: str = None,
        kms_instance_id: str = None,
    ):
        # Specifies whether to forcibly release the KMS instance if it has not been backed up.
        # 
        # - true: forcibly releases the instance.
        # 
        # - false (default): does not release the instance.
        self.force_delete_without_backup = force_delete_without_backup
        # The ID of the KMS instance.
        # 
        # This parameter is required.
        self.kms_instance_id = kms_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_delete_without_backup is not None:
            result['ForceDeleteWithoutBackup'] = self.force_delete_without_backup

        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDeleteWithoutBackup') is not None:
            self.force_delete_without_backup = m.get('ForceDeleteWithoutBackup')

        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')

        return self

