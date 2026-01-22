# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableRightsSeparationRequest(DaraModel):
    def __init__(
        self,
        audit_account_description: str = None,
        audit_account_name: str = None,
        audit_account_password: str = None,
        dbinstance_name: str = None,
        region_id: str = None,
        security_account_description: str = None,
        security_account_name: str = None,
        security_account_password: str = None,
    ):
        self.audit_account_description = audit_account_description
        # This parameter is required.
        self.audit_account_name = audit_account_name
        # This parameter is required.
        self.audit_account_password = audit_account_password
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.region_id = region_id
        self.security_account_description = security_account_description
        # This parameter is required.
        self.security_account_name = security_account_name
        # This parameter is required.
        self.security_account_password = security_account_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_account_description is not None:
            result['AuditAccountDescription'] = self.audit_account_description

        if self.audit_account_name is not None:
            result['AuditAccountName'] = self.audit_account_name

        if self.audit_account_password is not None:
            result['AuditAccountPassword'] = self.audit_account_password

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_account_description is not None:
            result['SecurityAccountDescription'] = self.security_account_description

        if self.security_account_name is not None:
            result['SecurityAccountName'] = self.security_account_name

        if self.security_account_password is not None:
            result['SecurityAccountPassword'] = self.security_account_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditAccountDescription') is not None:
            self.audit_account_description = m.get('AuditAccountDescription')

        if m.get('AuditAccountName') is not None:
            self.audit_account_name = m.get('AuditAccountName')

        if m.get('AuditAccountPassword') is not None:
            self.audit_account_password = m.get('AuditAccountPassword')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityAccountDescription') is not None:
            self.security_account_description = m.get('SecurityAccountDescription')

        if m.get('SecurityAccountName') is not None:
            self.security_account_name = m.get('SecurityAccountName')

        if m.get('SecurityAccountPassword') is not None:
            self.security_account_password = m.get('SecurityAccountPassword')

        return self

