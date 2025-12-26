# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class UserVpc(DaraModel):
    def __init__(
        self,
        default_forward_info: main_models.ForwardInfo = None,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        role_arn: str = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        self.default_forward_info = default_forward_info
        self.default_route = default_route
        self.extended_cidrs = extended_cidrs
        self.role_arn = role_arn
        self.security_group_id = security_group_id
        self.switch_id = switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.default_forward_info:
            self.default_forward_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_forward_info is not None:
            result['DefaultForwardInfo'] = self.default_forward_info.to_map()

        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route

        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultForwardInfo') is not None:
            temp_model = main_models.ForwardInfo()
            self.default_forward_info = temp_model.from_map(m.get('DefaultForwardInfo'))

        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')

        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

