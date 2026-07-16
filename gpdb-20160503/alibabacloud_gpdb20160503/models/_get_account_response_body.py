# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccountResponseBody(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        dbinstance_id: str = None,
        request_id: str = None,
    ):
        # The modified account description. The description must meet the following requirements:
        # 
        # - The description must start with a Chinese character or an English letter.
        # - The description cannot start with `http://` or `https://`.
        # - The description can contain Chinese characters, English characters, underscores (_), hyphens (-), and digits.
        # - The description must be 2 to 256 characters in length.
        self.account_description = account_description
        # The name of the initial account. The name must meet the following requirements:
        # 
        # - The name can contain lowercase letters, digits, and underscores (_).
        # - The name must start with a lowercase letter and end with a lowercase letter or digit.
        # - The name cannot start with gp.
        # - The name must be 2 to 16 characters in length.
        self.account_name = account_name
        # The status of the database account. Valid values:
        # 
        # - **0**: Being created.
        # - **1**: In use.
        # - **3**: Being deleted.
        self.account_status = account_status
        # The type of the host account. Valid values:
        # - **Normal**: standard account.
        # - **Admin**: administrator account.
        # 
        # For more information about the permissions of host accounts, see [Host account permissions](https://help.aliyun.com/document_detail/176240.html).
        self.account_type = account_type
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a region, including instance IDs.
        self.dbinstance_id = dbinstance_id
        # Id of the request
        self.request_id = request_id

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

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

