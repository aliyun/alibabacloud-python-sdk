# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetOrgLiveListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetOrgLiveListResponseBodyResult = None,
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
            temp_model = main_models.GetOrgLiveListResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class GetOrgLiveListResponseBodyResult(DaraModel):
    def __init__(
        self,
        new_live: main_models.GetOrgLiveListResponseBodyResultNewLive = None,
        update_live: main_models.GetOrgLiveListResponseBodyResultUpdateLive = None,
    ):
        self.new_live = new_live
        self.update_live = update_live

    def validate(self):
        if self.new_live:
            self.new_live.validate()
        if self.update_live:
            self.update_live.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_live is not None:
            result['NewLive'] = self.new_live.to_map()

        if self.update_live is not None:
            result['UpdateLive'] = self.update_live.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewLive') is not None:
            temp_model = main_models.GetOrgLiveListResponseBodyResultNewLive()
            self.new_live = temp_model.from_map(m.get('NewLive'))

        if m.get('UpdateLive') is not None:
            temp_model = main_models.GetOrgLiveListResponseBodyResultUpdateLive()
            self.update_live = temp_model.from_map(m.get('UpdateLive'))

        return self

class GetOrgLiveListResponseBodyResultUpdateLive(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        live_list: List[main_models.GetOrgLiveListResponseBodyResultUpdateLiveLiveList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.live_list = live_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.live_list:
            for v1 in self.live_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['LiveList'] = []
        if self.live_list is not None:
            for k1 in self.live_list:
                result['LiveList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.live_list = []
        if m.get('LiveList') is not None:
            for k1 in m.get('LiveList'):
                temp_model = main_models.GetOrgLiveListResponseBodyResultUpdateLiveLiveList()
                self.live_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetOrgLiveListResponseBodyResultUpdateLiveLiveList(DaraModel):
    def __init__(
        self,
        anchor_nickname: str = None,
        anchor_union_id: str = None,
        anchor_union_id_in_alibaba: str = None,
        anchor_user_id: str = None,
        live_end_time: int = None,
        live_start_time: int = None,
        live_uuid: str = None,
        title: str = None,
    ):
        self.anchor_nickname = anchor_nickname
        self.anchor_union_id = anchor_union_id
        self.anchor_union_id_in_alibaba = anchor_union_id_in_alibaba
        self.anchor_user_id = anchor_user_id
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

        if self.anchor_union_id_in_alibaba is not None:
            result['AnchorUnionIdInAlibaba'] = self.anchor_union_id_in_alibaba

        if self.anchor_user_id is not None:
            result['AnchorUserId'] = self.anchor_user_id

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

        if m.get('AnchorUnionIdInAlibaba') is not None:
            self.anchor_union_id_in_alibaba = m.get('AnchorUnionIdInAlibaba')

        if m.get('AnchorUserId') is not None:
            self.anchor_user_id = m.get('AnchorUserId')

        if m.get('LiveEndTime') is not None:
            self.live_end_time = m.get('LiveEndTime')

        if m.get('LiveStartTime') is not None:
            self.live_start_time = m.get('LiveStartTime')

        if m.get('LiveUuid') is not None:
            self.live_uuid = m.get('LiveUuid')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetOrgLiveListResponseBodyResultNewLive(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        live_list: List[main_models.GetOrgLiveListResponseBodyResultNewLiveLiveList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.live_list = live_list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.live_list:
            for v1 in self.live_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['LiveList'] = []
        if self.live_list is not None:
            for k1 in self.live_list:
                result['LiveList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.live_list = []
        if m.get('LiveList') is not None:
            for k1 in m.get('LiveList'):
                temp_model = main_models.GetOrgLiveListResponseBodyResultNewLiveLiveList()
                self.live_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetOrgLiveListResponseBodyResultNewLiveLiveList(DaraModel):
    def __init__(
        self,
        anchor_nickname: str = None,
        anchor_union_id: str = None,
        anchor_union_id_in_alibaba: str = None,
        anchor_user_id: str = None,
        live_end_time: int = None,
        live_start_time: int = None,
        live_uuid: str = None,
        share_open_conversation_ids: List[str] = None,
        title: str = None,
    ):
        self.anchor_nickname = anchor_nickname
        self.anchor_union_id = anchor_union_id
        self.anchor_union_id_in_alibaba = anchor_union_id_in_alibaba
        self.anchor_user_id = anchor_user_id
        self.live_end_time = live_end_time
        self.live_start_time = live_start_time
        self.live_uuid = live_uuid
        self.share_open_conversation_ids = share_open_conversation_ids
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

        if self.anchor_union_id_in_alibaba is not None:
            result['AnchorUnionIdInAlibaba'] = self.anchor_union_id_in_alibaba

        if self.anchor_user_id is not None:
            result['AnchorUserId'] = self.anchor_user_id

        if self.live_end_time is not None:
            result['LiveEndTime'] = self.live_end_time

        if self.live_start_time is not None:
            result['LiveStartTime'] = self.live_start_time

        if self.live_uuid is not None:
            result['LiveUuid'] = self.live_uuid

        if self.share_open_conversation_ids is not None:
            result['ShareOpenConversationIds'] = self.share_open_conversation_ids

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorNickname') is not None:
            self.anchor_nickname = m.get('AnchorNickname')

        if m.get('AnchorUnionId') is not None:
            self.anchor_union_id = m.get('AnchorUnionId')

        if m.get('AnchorUnionIdInAlibaba') is not None:
            self.anchor_union_id_in_alibaba = m.get('AnchorUnionIdInAlibaba')

        if m.get('AnchorUserId') is not None:
            self.anchor_user_id = m.get('AnchorUserId')

        if m.get('LiveEndTime') is not None:
            self.live_end_time = m.get('LiveEndTime')

        if m.get('LiveStartTime') is not None:
            self.live_start_time = m.get('LiveStartTime')

        if m.get('LiveUuid') is not None:
            self.live_uuid = m.get('LiveUuid')

        if m.get('ShareOpenConversationIds') is not None:
            self.share_open_conversation_ids = m.get('ShareOpenConversationIds')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

