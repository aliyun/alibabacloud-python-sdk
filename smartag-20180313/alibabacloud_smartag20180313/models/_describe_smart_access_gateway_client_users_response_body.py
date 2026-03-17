# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSmartAccessGatewayClientUsersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        users: main_models.DescribeSmartAccessGatewayClientUsersResponseBodyUsers = None,
    ):
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.users is not None:
            result['Users'] = self.users.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Users') is not None:
            temp_model = main_models.DescribeSmartAccessGatewayClientUsersResponseBodyUsers()
            self.users = temp_model.from_map(m.get('Users'))

        return self

class DescribeSmartAccessGatewayClientUsersResponseBodyUsers(DaraModel):
    def __init__(
        self,
        user: List[main_models.DescribeSmartAccessGatewayClientUsersResponseBodyUsersUser] = None,
    ):
        self.user = user

    def validate(self):
        if self.user:
            for v1 in self.user:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['User'] = []
        if self.user is not None:
            for k1 in self.user:
                result['User'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user = []
        if m.get('User') is not None:
            for k1 in m.get('User'):
                temp_model = main_models.DescribeSmartAccessGatewayClientUsersResponseBodyUsersUser()
                self.user.append(temp_model.from_map(k1))

        return self

class DescribeSmartAccessGatewayClientUsersResponseBodyUsersUser(DaraModel):
    def __init__(
        self,
        accelerate_bandwidth: int = None,
        bandwidth: int = None,
        client_ip: str = None,
        is_static_ip: int = None,
        state: int = None,
        user_mail: str = None,
        user_name: str = None,
    ):
        self.accelerate_bandwidth = accelerate_bandwidth
        self.bandwidth = bandwidth
        self.client_ip = client_ip
        self.is_static_ip = is_static_ip
        self.state = state
        self.user_mail = user_mail
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_bandwidth is not None:
            result['AccelerateBandwidth'] = self.accelerate_bandwidth

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.is_static_ip is not None:
            result['IsStaticIp'] = self.is_static_ip

        if self.state is not None:
            result['State'] = self.state

        if self.user_mail is not None:
            result['UserMail'] = self.user_mail

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateBandwidth') is not None:
            self.accelerate_bandwidth = m.get('AccelerateBandwidth')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('IsStaticIp') is not None:
            self.is_static_ip = m.get('IsStaticIp')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UserMail') is not None:
            self.user_mail = m.get('UserMail')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

