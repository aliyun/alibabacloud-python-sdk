# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateBackupPolicyResponseBody(DaraModel):
    def __init__(
        self,
        backup_policy: main_models.CreateBackupPolicyResponseBodyBackupPolicy = None,
        request_id: str = None,
    ):
        # The information about the anti-ransomware policy.
        self.backup_policy = backup_policy
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.backup_policy:
            self.backup_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_policy is not None:
            result['BackupPolicy'] = self.backup_policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPolicy') is not None:
            temp_model = main_models.CreateBackupPolicyResponseBodyBackupPolicy()
            self.backup_policy = temp_model.from_map(m.get('BackupPolicy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateBackupPolicyResponseBodyBackupPolicy(DaraModel):
    def __init__(
        self,
        id: str = None,
        status: str = None,
    ):
        # The ID of the anti-ransomware policy.
        self.id = id
        # The status of the anti-ransomware policy. Valid values:
        # 
        # *   **enabled**
        # *   **disabled**
        # 
        # >  After you create an anti-ransomware policy, the policy is enabled by default.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

