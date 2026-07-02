# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecretRequest(DaraModel):
    def __init__(
        self,
        force_delete_without_recovery: str = None,
        recovery_window_in_days: str = None,
        secret_name: str = None,
    ):
        # Specifies whether to forcibly delete the secret. If this parameter is set to true, the secret cannot be recovered.
        # 
        # Valid values:
        # 
        # *   **true**
        # *   **false** (default value)
        self.force_delete_without_recovery = force_delete_without_recovery
        # Specifies the recovery period of the secret if you do not forcibly delete it. Default value: 30. Unit: Days.
        self.recovery_window_in_days = recovery_window_in_days
        # The name of the secret.
        # 
        # This parameter is required.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_delete_without_recovery is not None:
            result['ForceDeleteWithoutRecovery'] = self.force_delete_without_recovery

        if self.recovery_window_in_days is not None:
            result['RecoveryWindowInDays'] = self.recovery_window_in_days

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForceDeleteWithoutRecovery') is not None:
            self.force_delete_without_recovery = m.get('ForceDeleteWithoutRecovery')

        if m.get('RecoveryWindowInDays') is not None:
            self.recovery_window_in_days = m.get('RecoveryWindowInDays')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

