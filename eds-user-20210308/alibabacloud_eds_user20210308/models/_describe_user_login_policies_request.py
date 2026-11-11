# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeUserLoginPoliciesRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        name: str = None,
        policy_ids: List[str] = None,
    ):
        # The channel.
        self.business_channel = business_channel
        # The policy name.
        self.name = name
        # The list of policy IDs. This is a filter condition for the query.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        return self

