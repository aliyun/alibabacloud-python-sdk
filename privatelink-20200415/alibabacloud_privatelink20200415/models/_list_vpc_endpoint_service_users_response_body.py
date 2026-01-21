# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointServiceUsersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
        user_arns: List[main_models.ListVpcEndpointServiceUsersResponseBodyUserARNs] = None,
        users: List[main_models.ListVpcEndpointServiceUsersResponseBodyUsers] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The whitelists in the format of Aliyun Resource Name (ARN).
        self.user_arns = user_arns
        # The Alibaba Cloud accounts in the whitelist of the endpoint service.
        self.users = users

    def validate(self):
        if self.user_arns:
            for v1 in self.user_arns:
                 if v1:
                    v1.validate()
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UserARNs'] = []
        if self.user_arns is not None:
            for k1 in self.user_arns:
                result['UserARNs'].append(k1.to_map() if k1 else None)

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.user_arns = []
        if m.get('UserARNs') is not None:
            for k1 in m.get('UserARNs'):
                temp_model = main_models.ListVpcEndpointServiceUsersResponseBodyUserARNs()
                self.user_arns.append(temp_model.from_map(k1))

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListVpcEndpointServiceUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListVpcEndpointServiceUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        user_id: int = None,
    ):
        # The ID of the Alibaba Cloud account in the whitelist of the endpoint service.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListVpcEndpointServiceUsersResponseBodyUserARNs(DaraModel):
    def __init__(
        self,
        user_arn: str = None,
    ):
        # The whitelist in the format of ARN.
        self.user_arn = user_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_arn is not None:
            result['UserARN'] = self.user_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserARN') is not None:
            self.user_arn = m.get('UserARN')

        return self

