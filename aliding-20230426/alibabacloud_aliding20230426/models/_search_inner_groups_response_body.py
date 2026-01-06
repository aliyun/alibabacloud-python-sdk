# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class SearchInnerGroupsResponseBody(DaraModel):
    def __init__(
        self,
        group_infos: List[main_models.SearchInnerGroupsResponseBodyGroupInfos] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.group_infos = group_infos
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.group_infos:
            for v1 in self.group_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['groupInfos'] = []
        if self.group_infos is not None:
            for k1 in self.group_infos:
                result['groupInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_infos = []
        if m.get('groupInfos') is not None:
            for k1 in m.get('groupInfos'):
                temp_model = main_models.SearchInnerGroupsResponseBodyGroupInfos()
                self.group_infos.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class SearchInnerGroupsResponseBodyGroupInfos(DaraModel):
    def __init__(
        self,
        icon: str = None,
        member_amount: str = None,
        open_conversation_id: str = None,
        title: str = None,
    ):
        self.icon = icon
        self.member_amount = member_amount
        self.open_conversation_id = open_conversation_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icon is not None:
            result['Icon'] = self.icon

        if self.member_amount is not None:
            result['MemberAmount'] = self.member_amount

        if self.open_conversation_id is not None:
            result['OpenConversationId'] = self.open_conversation_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('MemberAmount') is not None:
            self.member_amount = m.get('MemberAmount')

        if m.get('OpenConversationId') is not None:
            self.open_conversation_id = m.get('OpenConversationId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

