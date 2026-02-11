# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListRdUsersResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListRdUsersResponseBodyData] = None,
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
                temp_model = main_models.ListRdUsersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRdUsersResponseBodyData(DaraModel):
    def __init__(
        self,
        delegated_or_not: bool = None,
        joined: bool = None,
        joined_time: str = None,
        main_user_id: int = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        # Indicates whether the account can be used to view the logs and alerts within the account.
        self.delegated_or_not = delegated_or_not
        # Indicates whether the account is added to the threat analysis feature for centralized management. Valid values:
        # 
        # *   true
        # *   false
        self.joined = joined
        # The time when the account was added to the threat analysis feature.
        self.joined_time = joined_time
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id
        # The ID of the Alibaba Cloud account that is used to perform operations supported by the threat analysis feature.
        self.sub_user_id = sub_user_id
        # The username of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delegated_or_not is not None:
            result['DelegatedOrNot'] = self.delegated_or_not

        if self.joined is not None:
            result['Joined'] = self.joined

        if self.joined_time is not None:
            result['JoinedTime'] = self.joined_time

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelegatedOrNot') is not None:
            self.delegated_or_not = m.get('DelegatedOrNot')

        if m.get('Joined') is not None:
            self.joined = m.get('Joined')

        if m.get('JoinedTime') is not None:
            self.joined_time = m.get('JoinedTime')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')

        return self

