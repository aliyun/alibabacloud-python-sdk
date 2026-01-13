# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GrantRoleToUsersRequest(DaraModel):
    def __init__(
        self,
        role_arn: str = None,
        user_arns: List[str] = None,
        region_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.role_arn = role_arn
        # The user ARNs.
        self.user_arns = user_arns
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.user_arns is not None:
            result['userArns'] = self.user_arns

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('userArns') is not None:
            self.user_arns = m.get('userArns')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

