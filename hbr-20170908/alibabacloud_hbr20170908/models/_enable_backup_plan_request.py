# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableBackupPlanRequest(DaraModel):
    def __init__(
        self,
        edition: str = None,
        plan_id: str = None,
        source_type: str = None,
        vault_id: str = None,
    ):
        self.edition = edition
        # The ID of the backup plan.
        # 
        # This parameter is required.
        self.plan_id = plan_id
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS (NAS) file systems
        self.source_type = source_type
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

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

