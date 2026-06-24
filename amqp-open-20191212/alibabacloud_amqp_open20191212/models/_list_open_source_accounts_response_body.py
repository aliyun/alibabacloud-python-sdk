# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp_open20191212 import models as main_models
from darabonba.model import DaraModel

class ListOpenSourceAccountsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListOpenSourceAccountsResponseBodyData] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
        self.data = data
        # The maximum number of entries to return.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # The token that marks the end of the current query. This token is passed as a parameter in the next call to continue pagination. Set this parameter to an empty string for the first call or when the last page is returned.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListOpenSourceAccountsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListOpenSourceAccountsResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_user_id: int = None,
        cinstance_id: str = None,
        create_time: str = None,
        extra_json: str = None,
        hashing_algorithm: str = None,
        limits: str = None,
        name: str = None,
        password_hash: str = None,
        tags: str = None,
        weak_password: bool = None,
    ):
        # The Alibaba Cloud UID.
        self.aliyun_user_id = aliyun_user_id
        # The instance ID.
        self.cinstance_id = cinstance_id
        # The time when the user was created.
        self.create_time = create_time
        # The description.
        self.extra_json = extra_json
        # The hash algorithm.
        self.hashing_algorithm = hashing_algorithm
        # The quota configuration.
        self.limits = limits
        # The username.
        self.name = name
        # The password hash.
        self.password_hash = password_hash
        # The tags.
        self.tags = tags
        # Indicates whether the password is a weak password. Valid values:
        # - 0: No.
        # - 1: Yes.
        self.weak_password = weak_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_user_id is not None:
            result['AliyunUserId'] = self.aliyun_user_id

        if self.cinstance_id is not None:
            result['CInstanceId'] = self.cinstance_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extra_json is not None:
            result['ExtraJson'] = self.extra_json

        if self.hashing_algorithm is not None:
            result['HashingAlgorithm'] = self.hashing_algorithm

        if self.limits is not None:
            result['Limits'] = self.limits

        if self.name is not None:
            result['Name'] = self.name

        if self.password_hash is not None:
            result['PasswordHash'] = self.password_hash

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.weak_password is not None:
            result['WeakPassword'] = self.weak_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunUserId') is not None:
            self.aliyun_user_id = m.get('AliyunUserId')

        if m.get('CInstanceId') is not None:
            self.cinstance_id = m.get('CInstanceId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExtraJson') is not None:
            self.extra_json = m.get('ExtraJson')

        if m.get('HashingAlgorithm') is not None:
            self.hashing_algorithm = m.get('HashingAlgorithm')

        if m.get('Limits') is not None:
            self.limits = m.get('Limits')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PasswordHash') is not None:
            self.password_hash = m.get('PasswordHash')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('WeakPassword') is not None:
            self.weak_password = m.get('WeakPassword')

        return self

