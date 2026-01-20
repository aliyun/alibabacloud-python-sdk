# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListResourceShareInvitationsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_share_ids: List[str] = None,
        resource_share_invitation_ids: List[str] = None,
    ):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token
        # The IDs of the resource shares.
        self.resource_share_ids = resource_share_ids
        # The IDs of the resource sharing invitations.
        self.resource_share_invitation_ids = resource_share_invitation_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids

        if self.resource_share_invitation_ids is not None:
            result['ResourceShareInvitationIds'] = self.resource_share_invitation_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')

        if m.get('ResourceShareInvitationIds') is not None:
            self.resource_share_invitation_ids = m.get('ResourceShareInvitationIds')

        return self

