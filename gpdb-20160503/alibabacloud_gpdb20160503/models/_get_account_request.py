# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccountRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        dbinstance_id: str = None,
    ):
        # The name of the initial account. The name must meet the following requirements:
        # 
        # - The name can contain lowercase letters, digits, and underscores (_).
        # - The name must start with a lowercase letter and end with a lowercase letter or digit.
        # - The name cannot start with gp.
        # - The name must be 2 to 16 characters in length.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The instance ID.
        # >You can specify up to 30 instance IDs for batch operations. Separate multiple instance IDs with commas (,).
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

