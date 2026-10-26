# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListMembersNotForProjectResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        members: List[main_models.ListMembersNotForProjectResponseBodyMembers] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries to return. If a valid value is specified for the MaxResults request parameter, the value of the parameter is returned. Otherwise, the default value is returned.
        self.max_results = max_results
        # The list of member accounts.
        self.members = members
        # The token for the next request, which is used for paging. Specify this token in the NextToken request parameter for the next paged query. If this field is empty in the response, no more data is available.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.ListMembersNotForProjectResponseBodyMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMembersNotForProjectResponseBodyMembers(DaraModel):
    def __init__(
        self,
        member_id: int = None,
    ):
        # The UID of the member accounts.
        self.member_id = member_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_id is not None:
            result['MemberId'] = self.member_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        return self

