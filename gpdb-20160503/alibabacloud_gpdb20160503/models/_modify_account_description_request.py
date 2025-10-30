# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountDescriptionRequest(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        client_token: str = None,
        dbinstance_id: str = None,
    ):
        # The new description of the database account.
        # 
        # *   The description must start with a letter.
        # *   The description cannot start with `http://` or `https://`.
        # *   The description can contain letters, underscores (_), hyphens (-), and digits.
        # *   The description must be 2 to 256 characters in length.
        self.account_description = account_description
        # The name of the database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Idempotence check. For more information, see [How to Ensure Idempotence](https://help.aliyun.com/document_detail/327176.html).
        self.client_token = client_token
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances within a region.
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
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        return self

