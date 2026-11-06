# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPrivateLinkSecurityGroupsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        vpc_id: str = None,
    ):
        # The maximum number of entries to return.
        self.max_results = max_results
        # The token for the next page.
        self.next_token = next_token
        # The ID of the VPC owned by the authorized user. The candidate security groups must belong to this VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

