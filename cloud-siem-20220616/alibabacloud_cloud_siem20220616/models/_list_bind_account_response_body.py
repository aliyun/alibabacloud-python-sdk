# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListBindAccountResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListBindAccountResponseBodyData] = None,
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
                temp_model = main_models.ListBindAccountResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBindAccountResponseBodyData(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        account_id: str = None,
        account_name: str = None,
        bind_id: int = None,
        cloud_code: str = None,
        create_user: str = None,
        data_source_count: int = None,
        modify_time: str = None,
    ):
        # The AccessKey ID of the cloud account.
        self.access_id = access_id
        # The ID of the cloud account.
        self.account_id = account_id
        # The username of the cloud account.
        self.account_name = account_name
        # The ID that is generated when the cloud account is added.
        self.bind_id = bind_id
        # The code of the cloud service provider. Valid values:
        # 
        # *   qcloud: Tencent Cloud
        # *   aliyun: Alibaba Cloud
        # *   hcloud: Huawei Cloud
        self.cloud_code = cloud_code
        # The ID of the account that is used to add the cloud account.
        self.create_user = create_user
        # The number of data sources that are added to the threat analysis feature within the cloud account.
        self.data_source_count = data_source_count
        # The modification time.
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.bind_id is not None:
            result['BindId'] = self.bind_id

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_source_count is not None:
            result['DataSourceCount'] = self.data_source_count

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSourceCount') is not None:
            self.data_source_count = m.get('DataSourceCount')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        return self

