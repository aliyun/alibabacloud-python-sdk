# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeRdMemberListResponseBody(DaraModel):
    def __init__(
        self,
        member_list: List[main_models.DescribeRdMemberListResponseBodyMemberList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The information about the members.
        self.member_list = member_list
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.member_list:
            for v1 in self.member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MemberList'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['MemberList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.DescribeRdMemberListResponseBodyMemberList()
                self.member_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeRdMemberListResponseBodyMemberList(DaraModel):
    def __init__(
        self,
        gmt_create: int = None,
        name: str = None,
        uid: str = None,
    ):
        # The creation time.
        self.gmt_create = gmt_create
        # The name of the member.
        self.name = name
        # The Alibaba Cloud account ID of the member.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.name is not None:
            result['Name'] = self.name

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

