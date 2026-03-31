# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeMemberAccountsResponseBody(DaraModel):
    def __init__(
        self,
        account_infos: List[main_models.DescribeMemberAccountsResponseBodyAccountInfos] = None,
        request_id: str = None,
    ):
        # The information about the member.
        self.account_infos = account_infos
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.account_infos:
            for v1 in self.account_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountInfos'] = []
        if self.account_infos is not None:
            for k1 in self.account_infos:
                result['AccountInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_infos = []
        if m.get('AccountInfos') is not None:
            for k1 in m.get('AccountInfos'):
                temp_model = main_models.DescribeMemberAccountsResponseBodyAccountInfos()
                self.account_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMemberAccountsResponseBodyAccountInfos(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        account_status: str = None,
        description: str = None,
        gmt_create: int = None,
    ):
        # The ID of the member.
        self.account_id = account_id
        # The name of the member.
        self.account_name = account_name
        # The status of the member.
        # 
        # *   **enabled**: managed.
        # *   **disabled**: not managed.
        # *   **disabling**: being deleted.
        self.account_status = account_status
        # The description of the member.
        self.description = description
        # The time when the member was added.
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        return self

