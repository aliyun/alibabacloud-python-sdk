# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaLiveInputSecurityGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_group: main_models.GetMediaLiveInputSecurityGroupResponseBodySecurityGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The security group information.
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            self.security_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroup') is not None:
            temp_model = main_models.GetMediaLiveInputSecurityGroupResponseBodySecurityGroup()
            self.security_group = temp_model.from_map(m.get('SecurityGroup'))

        return self

class GetMediaLiveInputSecurityGroupResponseBodySecurityGroup(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        input_ids: List[str] = None,
        name: str = None,
        security_group_id: str = None,
        whitelist_rules: List[str] = None,
    ):
        # The time when the security group was created. It follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The IDs of the inputs associated with the security group.
        self.input_ids = input_ids
        # The name of the security group.
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

