# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetGroupLiveListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetGroupLiveListResponseBodyResult = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.request_id = request_id
        self.result = result
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GetGroupLiveListResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetGroupLiveListResponseBodyResult(DaraModel):
    def __init__(
        self,
        group_live_list: List[main_models.GetGroupLiveListResponseBodyResultGroupLiveList] = None,
    ):
        self.group_live_list = group_live_list

    def validate(self):
        if self.group_live_list:
            for v1 in self.group_live_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupLiveList'] = []
        if self.group_live_list is not None:
            for k1 in self.group_live_list:
                result['GroupLiveList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_live_list = []
        if m.get('GroupLiveList') is not None:
            for k1 in m.get('GroupLiveList'):
                temp_model = main_models.GetGroupLiveListResponseBodyResultGroupLiveList()
                self.group_live_list.append(temp_model.from_map(k1))

        return self

class GetGroupLiveListResponseBodyResultGroupLiveList(DaraModel):
    def __init__(
        self,
        anchor_nickname: str = None,
        anchor_union_id: str = None,
        live_end_time: int = None,
        live_start_time: int = None,
        live_uuid: str = None,
        title: str = None,
    ):
        self.anchor_nickname = anchor_nickname
        self.anchor_union_id = anchor_union_id
        self.live_end_time = live_end_time
        self.live_start_time = live_start_time
        self.live_uuid = live_uuid
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_nickname is not None:
            result['AnchorNickname'] = self.anchor_nickname

        if self.anchor_union_id is not None:
            result['AnchorUnionId'] = self.anchor_union_id

        if self.live_end_time is not None:
            result['LiveEndTime'] = self.live_end_time

        if self.live_start_time is not None:
            result['LiveStartTime'] = self.live_start_time

        if self.live_uuid is not None:
            result['LiveUuid'] = self.live_uuid

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorNickname') is not None:
            self.anchor_nickname = m.get('AnchorNickname')

        if m.get('AnchorUnionId') is not None:
            self.anchor_union_id = m.get('AnchorUnionId')

        if m.get('LiveEndTime') is not None:
            self.live_end_time = m.get('LiveEndTime')

        if m.get('LiveStartTime') is not None:
            self.live_start_time = m.get('LiveStartTime')

        if m.get('LiveUuid') is not None:
            self.live_uuid = m.get('LiveUuid')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

