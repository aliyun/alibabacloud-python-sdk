# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class DescribeOrgsRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        max_results: int = None,
        next_token: str = None,
        org_name: str = None,
        parent_org_id: str = None,
        show_extras: Dict[str, Any] = None,
    ):
        self.business_channel = business_channel
        # The maximum number of entries to return. Valid values: 1 to 100.\\
        # Default value: 100.
        self.max_results = max_results
        # The token that determines the start point of the query. The return value is the value of the NextToken response parameter that was returned last time the DescribeOrgs operation was called.
        self.next_token = next_token
        # The name of the organization.
        self.org_name = org_name
        # The parent organization ID.
        self.parent_org_id = parent_org_id
        self.show_extras = show_extras

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.org_name is not None:
            result['OrgName'] = self.org_name

        if self.parent_org_id is not None:
            result['ParentOrgId'] = self.parent_org_id

        if self.show_extras is not None:
            result['ShowExtras'] = self.show_extras

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')

        if m.get('ParentOrgId') is not None:
            self.parent_org_id = m.get('ParentOrgId')

        if m.get('ShowExtras') is not None:
            self.show_extras = m.get('ShowExtras')

        return self

