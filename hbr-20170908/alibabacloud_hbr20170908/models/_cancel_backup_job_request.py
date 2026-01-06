# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelBackupJobRequest(DaraModel):
    def __init__(
        self,
        edition: str = None,
        job_id: str = None,
        vault_id: str = None,
    ):
        self.edition = edition
        # The ID of the backup job.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

