# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableSqlAuditRequest(DaraModel):
    def __init__(
        self,
        audit_account_name: str = None,
        audit_account_password: str = None,
        dbinstance_id: str = None,
        expire_after_days: int = None,
        region_id: str = None,
    ):
        self.audit_account_name = audit_account_name
        self.audit_account_password = audit_account_password
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.expire_after_days = expire_after_days
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_account_name is not None:
            result['AuditAccountName'] = self.audit_account_name

        if self.audit_account_password is not None:
            result['AuditAccountPassword'] = self.audit_account_password

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.expire_after_days is not None:
            result['ExpireAfterDays'] = self.expire_after_days

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditAccountName') is not None:
            self.audit_account_name = m.get('AuditAccountName')

        if m.get('AuditAccountPassword') is not None:
            self.audit_account_password = m.get('AuditAccountPassword')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ExpireAfterDays') is not None:
            self.expire_after_days = m.get('ExpireAfterDays')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

