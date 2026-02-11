# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListAccountsByLogResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAccountsByLogResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAccountsByLogResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAccountsByLogResponseBodyData(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        account_name: str = None,
        imported: int = None,
        log_code: str = None,
        main_user_id: int = None,
        prod_code: str = None,
        sub_user_id: int = None,
    ):
        # The ID of the cloud account.
        self.account_id = account_id
        # The name of the cloud account.
        self.account_name = account_name
        # Indicates whether the account is added. Valid values: -1: yes -0: no
        self.imported = imported
        # The code of the log.
        self.log_code = log_code
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id
        # The code of the service.
        self.prod_code = prod_code
        # The ID of the Alibaba Cloud account for which the threat analysis feature is enabled.
        self.sub_user_id = sub_user_id

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

        if self.imported is not None:
            result['Imported'] = self.imported

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Imported') is not None:
            self.imported = m.get('Imported')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

