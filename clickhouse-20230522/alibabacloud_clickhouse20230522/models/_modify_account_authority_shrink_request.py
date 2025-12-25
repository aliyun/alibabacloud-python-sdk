# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountAuthorityShrinkRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        dbinstance_id: str = None,
        dml_auth_setting_shrink: str = None,
        region_id: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account = account
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The information about permissions.
        # 
        # This parameter is required.
        self.dml_auth_setting_shrink = dml_auth_setting_shrink
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dml_auth_setting_shrink is not None:
            result['DmlAuthSetting'] = self.dml_auth_setting_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DmlAuthSetting') is not None:
            self.dml_auth_setting_shrink = m.get('DmlAuthSetting')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

