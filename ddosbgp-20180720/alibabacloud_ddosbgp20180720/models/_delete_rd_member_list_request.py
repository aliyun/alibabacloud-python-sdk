# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DeleteRdMemberListRequest(DaraModel):
    def __init__(
        self,
        member_list: List[main_models.DeleteRdMemberListRequestMemberList] = None,
    ):
        # The list of the members.
        # 
        # This parameter is required.
        self.member_list = member_list

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.DeleteRdMemberListRequestMemberList()
                self.member_list.append(temp_model.from_map(k1))

        return self

class DeleteRdMemberListRequestMemberList(DaraModel):
    def __init__(
        self,
        uid: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

