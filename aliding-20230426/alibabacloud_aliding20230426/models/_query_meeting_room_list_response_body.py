# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryMeetingRoomListResponseBody(DaraModel):
    def __init__(
        self,
        has_more: bool = None,
        next_token: int = None,
        request_id: str = None,
        result: List[main_models.QueryMeetingRoomListResponseBodyResult] = None,
    ):
        self.has_more = has_more
        self.next_token = next_token
        # requestId
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_more is not None:
            result['hasMore'] = self.has_more

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.QueryMeetingRoomListResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class QueryMeetingRoomListResponseBodyResult(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        isv_room_id: str = None,
        room_capacity: int = None,
        room_group: main_models.QueryMeetingRoomListResponseBodyResultRoomGroup = None,
        room_id: str = None,
        room_labels: List[main_models.QueryMeetingRoomListResponseBodyResultRoomLabels] = None,
        room_location: main_models.QueryMeetingRoomListResponseBodyResultRoomLocation = None,
        room_name: str = None,
        room_picture: str = None,
        room_staff_id: str = None,
        room_status: int = None,
    ):
        self.corp_id = corp_id
        self.isv_room_id = isv_room_id
        self.room_capacity = room_capacity
        self.room_group = room_group
        self.room_id = room_id
        self.room_labels = room_labels
        self.room_location = room_location
        self.room_name = room_name
        self.room_picture = room_picture
        self.room_staff_id = room_staff_id
        self.room_status = room_status

    def validate(self):
        if self.room_group:
            self.room_group.validate()
        if self.room_labels:
            for v1 in self.room_labels:
                 if v1:
                    v1.validate()
        if self.room_location:
            self.room_location.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.isv_room_id is not None:
            result['IsvRoomId'] = self.isv_room_id

        if self.room_capacity is not None:
            result['RoomCapacity'] = self.room_capacity

        if self.room_group is not None:
            result['RoomGroup'] = self.room_group.to_map()

        if self.room_id is not None:
            result['RoomId'] = self.room_id

        result['RoomLabels'] = []
        if self.room_labels is not None:
            for k1 in self.room_labels:
                result['RoomLabels'].append(k1.to_map() if k1 else None)

        if self.room_location is not None:
            result['RoomLocation'] = self.room_location.to_map()

        if self.room_name is not None:
            result['RoomName'] = self.room_name

        if self.room_picture is not None:
            result['RoomPicture'] = self.room_picture

        if self.room_staff_id is not None:
            result['RoomStaffId'] = self.room_staff_id

        if self.room_status is not None:
            result['RoomStatus'] = self.room_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('IsvRoomId') is not None:
            self.isv_room_id = m.get('IsvRoomId')

        if m.get('RoomCapacity') is not None:
            self.room_capacity = m.get('RoomCapacity')

        if m.get('RoomGroup') is not None:
            temp_model = main_models.QueryMeetingRoomListResponseBodyResultRoomGroup()
            self.room_group = temp_model.from_map(m.get('RoomGroup'))

        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')

        self.room_labels = []
        if m.get('RoomLabels') is not None:
            for k1 in m.get('RoomLabels'):
                temp_model = main_models.QueryMeetingRoomListResponseBodyResultRoomLabels()
                self.room_labels.append(temp_model.from_map(k1))

        if m.get('RoomLocation') is not None:
            temp_model = main_models.QueryMeetingRoomListResponseBodyResultRoomLocation()
            self.room_location = temp_model.from_map(m.get('RoomLocation'))

        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')

        if m.get('RoomPicture') is not None:
            self.room_picture = m.get('RoomPicture')

        if m.get('RoomStaffId') is not None:
            self.room_staff_id = m.get('RoomStaffId')

        if m.get('RoomStatus') is not None:
            self.room_status = m.get('RoomStatus')

        return self

class QueryMeetingRoomListResponseBodyResultRoomLocation(DaraModel):
    def __init__(
        self,
        desc: str = None,
        title: str = None,
    ):
        self.desc = desc
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class QueryMeetingRoomListResponseBodyResultRoomLabels(DaraModel):
    def __init__(
        self,
        label_id: int = None,
        label_name: str = None,
    ):
        self.label_id = label_id
        self.label_name = label_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_id is not None:
            result['LabelId'] = self.label_id

        if self.label_name is not None:
            result['LabelName'] = self.label_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')

        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')

        return self

class QueryMeetingRoomListResponseBodyResultRoomGroup(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        group_name: str = None,
        parent_id: int = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

