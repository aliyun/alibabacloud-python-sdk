# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDevelopersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        portal_id: str = None,
        status: str = None,
        username: str = None,
    ):
        # The maximum number of entries per page. The default value and valid values are not specified in the API definition.
        self.max_results = max_results
        # The pagination cursor. Pass the nextToken value returned in the previous response to retrieve the next page. Do not pass this parameter for the first query.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The ID of the portal used to filter developers.
        self.portal_id = portal_id
        # The status of the developer used to filter developers. Valid values: PENDING, APPROVED, and REJECTED.
        self.status = status
        # The logon username of the developer used to filter developers.
        self.username = username

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

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        if self.status is not None:
            result['status'] = self.status

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

