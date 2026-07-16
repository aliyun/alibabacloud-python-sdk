# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class DescribeOrgsRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        include_org_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        org_name: str = None,
        parent_org_id: str = None,
        show_extras: Dict[str, Any] = None,
    ):
        # The channel.
        self.business_channel = business_channel
        self.include_org_ids = include_org_ids
        # The maximum number of entries to return. Valid values: 1 to 100.<br>
        # Default value: 100.<br>
        self.max_results = max_results
        # The pagination token. To retrieve the next page of results, set this parameter to the `NextToken` value that was returned from a previous request.
        self.next_token = next_token
        # The organization name.
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

        if self.include_org_ids is not None:
            result['IncludeOrgIds'] = self.include_org_ids

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

        if m.get('IncludeOrgIds') is not None:
            self.include_org_ids = m.get('IncludeOrgIds')

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

