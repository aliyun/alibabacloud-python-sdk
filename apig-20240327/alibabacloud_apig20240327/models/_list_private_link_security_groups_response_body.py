# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListPrivateLinkSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPrivateLinkSecurityGroupsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListPrivateLinkSecurityGroupsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListPrivateLinkSecurityGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListPrivateLinkSecurityGroupsResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The source information.
        self.items = items
        # The maximum number of entries returned in this query.
        self.max_results = max_results
        # The next token.
        self.next_token = next_token

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListPrivateLinkSecurityGroupsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

class ListPrivateLinkSecurityGroupsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        security_group_name: str = None,
        service_managed: bool = None,
        vpc_id: str = None,
    ):
        # The security group ID.
        self.security_group_id = security_group_id
        # The security group name.
        self.security_group_name = security_group_name
        # Specifies whether the resource is created by a service account. Valid values:
        # 
        # - 0: Not created by a service account.
        # - 1: Created by a service account.
        self.service_managed = service_managed
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id

        if self.security_group_name is not None:
            result['securityGroupName'] = self.security_group_name

        if self.service_managed is not None:
            result['serviceManaged'] = self.service_managed

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')

        if m.get('securityGroupName') is not None:
            self.security_group_name = m.get('securityGroupName')

        if m.get('serviceManaged') is not None:
            self.service_managed = m.get('serviceManaged')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

