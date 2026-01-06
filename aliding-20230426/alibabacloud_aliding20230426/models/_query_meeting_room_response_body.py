# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryMeetingRoomResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.QueryMeetingRoomResponseBodyResult = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        # requestId
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
            temp_model = main_models.QueryMeetingRoomResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class QueryMeetingRoomResponseBodyResult(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        device_union_ids: List[str] = None,
        enable_cycle_reservation: bool = None,
        isv_room_id: str = None,
        reservation_authority: main_models.QueryMeetingRoomResponseBodyResultReservationAuthority = None,
        room_capacity: int = None,
        room_group: main_models.QueryMeetingRoomResponseBodyResultRoomGroup = None,
        room_id: str = None,
        room_labels: List[main_models.QueryMeetingRoomResponseBodyResultRoomLabels] = None,
        room_location: main_models.QueryMeetingRoomResponseBodyResultRoomLocation = None,
        room_name: str = None,
        room_picture: str = None,
        room_staff_id: str = None,
        room_status: int = None,
        room_union_id: str = None,
    ):
        self.corp_id = corp_id
        self.device_union_ids = device_union_ids
        self.enable_cycle_reservation = enable_cycle_reservation
        self.isv_room_id = isv_room_id
        self.reservation_authority = reservation_authority
        self.room_capacity = room_capacity
        self.room_group = room_group
        self.room_id = room_id
        self.room_labels = room_labels
        self.room_location = room_location
        self.room_name = room_name
        self.room_picture = room_picture
        self.room_staff_id = room_staff_id
        self.room_status = room_status
        self.room_union_id = room_union_id

    def validate(self):
        if self.reservation_authority:
            self.reservation_authority.validate()
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

        if self.device_union_ids is not None:
            result['DeviceUnionIds'] = self.device_union_ids

        if self.enable_cycle_reservation is not None:
            result['EnableCycleReservation'] = self.enable_cycle_reservation

        if self.isv_room_id is not None:
            result['IsvRoomId'] = self.isv_room_id

        if self.reservation_authority is not None:
            result['ReservationAuthority'] = self.reservation_authority.to_map()

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

        if self.room_union_id is not None:
            result['RoomUnionId'] = self.room_union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('DeviceUnionIds') is not None:
            self.device_union_ids = m.get('DeviceUnionIds')

        if m.get('EnableCycleReservation') is not None:
            self.enable_cycle_reservation = m.get('EnableCycleReservation')

        if m.get('IsvRoomId') is not None:
            self.isv_room_id = m.get('IsvRoomId')

        if m.get('ReservationAuthority') is not None:
            temp_model = main_models.QueryMeetingRoomResponseBodyResultReservationAuthority()
            self.reservation_authority = temp_model.from_map(m.get('ReservationAuthority'))

        if m.get('RoomCapacity') is not None:
            self.room_capacity = m.get('RoomCapacity')

        if m.get('RoomGroup') is not None:
            temp_model = main_models.QueryMeetingRoomResponseBodyResultRoomGroup()
            self.room_group = temp_model.from_map(m.get('RoomGroup'))

        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')

        self.room_labels = []
        if m.get('RoomLabels') is not None:
            for k1 in m.get('RoomLabels'):
                temp_model = main_models.QueryMeetingRoomResponseBodyResultRoomLabels()
                self.room_labels.append(temp_model.from_map(k1))

        if m.get('RoomLocation') is not None:
            temp_model = main_models.QueryMeetingRoomResponseBodyResultRoomLocation()
            self.room_location = temp_model.from_map(m.get('RoomLocation'))

        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')

        if m.get('RoomPicture') is not None:
            self.room_picture = m.get('RoomPicture')

        if m.get('RoomStaffId') is not None:
            self.room_staff_id = m.get('RoomStaffId')

        if m.get('RoomStatus') is not None:
            self.room_status = m.get('RoomStatus')

        if m.get('RoomUnionId') is not None:
            self.room_union_id = m.get('RoomUnionId')

        return self

class QueryMeetingRoomResponseBodyResultRoomLocation(DaraModel):
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

class QueryMeetingRoomResponseBodyResultRoomLabels(DaraModel):
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

class QueryMeetingRoomResponseBodyResultRoomGroup(DaraModel):
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

class QueryMeetingRoomResponseBodyResultReservationAuthority(DaraModel):
    def __init__(
        self,
        authorized_members: List[main_models.QueryMeetingRoomResponseBodyResultReservationAuthorityAuthorizedMembers] = None,
    ):
        self.authorized_members = authorized_members

    def validate(self):
        if self.authorized_members:
            for v1 in self.authorized_members:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthorizedMembers'] = []
        if self.authorized_members is not None:
            for k1 in self.authorized_members:
                result['AuthorizedMembers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_members = []
        if m.get('AuthorizedMembers') is not None:
            for k1 in m.get('AuthorizedMembers'):
                temp_model = main_models.QueryMeetingRoomResponseBodyResultReservationAuthorityAuthorizedMembers()
                self.authorized_members.append(temp_model.from_map(k1))

        return self

class QueryMeetingRoomResponseBodyResultReservationAuthorityAuthorizedMembers(DaraModel):
    def __init__(
        self,
        member_id: str = None,
        member_name: str = None,
        member_type: str = None,
    ):
        self.member_id = member_id
        self.member_name = member_name
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.member_name is not None:
            result['MemberName'] = self.member_name

        if self.member_type is not None:
            result['MemberType'] = self.member_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('MemberName') is not None:
            self.member_name = m.get('MemberName')

        if m.get('MemberType') is not None:
            self.member_type = m.get('MemberType')

        return self

