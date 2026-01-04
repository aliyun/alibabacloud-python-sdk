# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListApplicationAccountsResponseBody(DaraModel):
    def __init__(
        self,
        application_accounts: List[main_models.ListApplicationAccountsResponseBodyApplicationAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.application_accounts = application_accounts
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.application_accounts:
            for v1 in self.application_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationAccounts'] = []
        if self.application_accounts is not None:
            for k1 in self.application_accounts:
                result['ApplicationAccounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_accounts = []
        if m.get('ApplicationAccounts') is not None:
            for k1 in m.get('ApplicationAccounts'):
                temp_model = main_models.ListApplicationAccountsResponseBodyApplicationAccounts()
                self.application_accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationAccountsResponseBodyApplicationAccounts(DaraModel):
    def __init__(
        self,
        application_account_id: str = None,
        application_id: str = None,
        application_username: str = None,
        create_time: int = None,
        instance_id: str = None,
        user_id: str = None,
    ):
        # IDaaS EIAM 应用账号Id
        self.application_account_id = application_account_id
        # IDaaS EIAM 应用Id
        self.application_id = application_id
        # IDaaS EIAM 应用账号名称
        self.application_username = application_username
        # 创建时间
        self.create_time = create_time
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        # IDaaS EIAM 用户Id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_account_id is not None:
            result['ApplicationAccountId'] = self.application_account_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_username is not None:
            result['ApplicationUsername'] = self.application_username

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationAccountId') is not None:
            self.application_account_id = m.get('ApplicationAccountId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationUsername') is not None:
            self.application_username = m.get('ApplicationUsername')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

