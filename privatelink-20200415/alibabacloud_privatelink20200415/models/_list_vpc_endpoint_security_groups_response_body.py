# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_privatelink20200415 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        security_groups: List[main_models.ListVpcEndpointSecurityGroupsResponseBodySecurityGroups] = None,
        total_count: int = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the security groups.
        self.security_groups = security_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.security_groups:
            for v1 in self.security_groups:
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

        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k1 in self.security_groups:
                result['SecurityGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k1 in m.get('SecurityGroups'):
                temp_model = main_models.ListVpcEndpointSecurityGroupsResponseBodySecurityGroups()
                self.security_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListVpcEndpointSecurityGroupsResponseBodySecurityGroups(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        security_group_status: str = None,
    ):
        # The ID of the security group that is associated with the endpoint.
        self.security_group_id = security_group_id
        # The associate status of the security group, valid values:
        # - Attaching: The security group is being attached.
        # - Attached: The security group is attached.
        # - Detaching: The security group is being detached.
        self.security_group_status = security_group_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_status is not None:
            result['SecurityGroupStatus'] = self.security_group_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupStatus') is not None:
            self.security_group_status = m.get('SecurityGroupStatus')

        return self

