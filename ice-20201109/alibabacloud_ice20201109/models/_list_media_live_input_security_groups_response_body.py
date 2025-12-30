# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListMediaLiveInputSecurityGroupsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        security_groups: List[main_models.ListMediaLiveInputSecurityGroupsResponseBodySecurityGroups] = None,
        total_count: int = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The security groups.
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
                temp_model = main_models.ListMediaLiveInputSecurityGroupsResponseBodySecurityGroups()
                self.security_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMediaLiveInputSecurityGroupsResponseBodySecurityGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        input_ids: List[str] = None,
        name: str = None,
        security_group_id: str = None,
        whitelist_rules: List[str] = None,
    ):
        # The time when the security group was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The IDs of the inputs associated with the security group.
        self.input_ids = input_ids
        # The security group name.
        self.name = name
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The security group rules.
        self.whitelist_rules = whitelist_rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.input_ids is not None:
            result['InputIds'] = self.input_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.whitelist_rules is not None:
            result['WhitelistRules'] = self.whitelist_rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InputIds') is not None:
            self.input_ids = m.get('InputIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('WhitelistRules') is not None:
            self.whitelist_rules = m.get('WhitelistRules')

        return self

