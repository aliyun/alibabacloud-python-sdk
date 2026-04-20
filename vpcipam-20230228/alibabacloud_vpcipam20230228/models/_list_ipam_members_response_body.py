# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamMembersResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        member_infos: List[main_models.ListIpamMembersResponseBodyMemberInfos] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.count = count
        self.max_results = max_results
        self.member_infos = member_infos
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.member_infos:
            for v1 in self.member_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['MemberInfos'] = []
        if self.member_infos is not None:
            for k1 in self.member_infos:
                result['MemberInfos'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.member_infos = []
        if m.get('MemberInfos') is not None:
            for k1 in m.get('MemberInfos'):
                temp_model = main_models.ListIpamMembersResponseBodyMemberInfos()
                self.member_infos.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamMembersResponseBodyMemberInfos(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        member_id: str = None,
        member_type: str = None,
        status: str = None,
    ):
        self.creation_time = creation_time
        self.member_id = member_id
        self.member_type = member_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_type is not None:
            result['MemberType'] = self.member_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

