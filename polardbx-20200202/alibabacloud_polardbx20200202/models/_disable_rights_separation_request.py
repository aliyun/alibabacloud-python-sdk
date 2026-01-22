# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableRightsSeparationRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        dba_account_name: str = None,
        dba_account_password: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.dba_account_name = dba_account_name
        # This parameter is required.
        self.dba_account_password = dba_account_password
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dba_account_name is not None:
            result['DbaAccountName'] = self.dba_account_name

        if self.dba_account_password is not None:
            result['DbaAccountPassword'] = self.dba_account_password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DbaAccountName') is not None:
            self.dba_account_name = m.get('DbaAccountName')

        if m.get('DbaAccountPassword') is not None:
            self.dba_account_password = m.get('DbaAccountPassword')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

