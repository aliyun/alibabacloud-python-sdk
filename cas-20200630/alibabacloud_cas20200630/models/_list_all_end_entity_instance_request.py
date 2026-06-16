# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAllEndEntityInstanceRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        max_results: int = None,
        next_token: str = None,
        parent_id: int = None,
        recursive_children: int = None,
        show_size: int = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The maximum number of entries to return for this call.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. You can get this token from the \\`NextToken\\` response parameter of the previous query.
        self.next_token = next_token
        # The ID of the parent instance.
        self.parent_id = parent_id
        # Specifies whether to return information about the billing type in the response. Valid values: -**0**: The information is not returned. -**1**: The information is returned.
        self.recursive_children = recursive_children
        # The number of entries to return on each page. Default value: 20.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.recursive_children is not None:
            result['RecursiveChildren'] = self.recursive_children

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RecursiveChildren') is not None:
            self.recursive_children = m.get('RecursiveChildren')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self

