# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class CreateMeetingRoomRequest(DaraModel):
    def __init__(
        self,
        enable_cycle_reservation: bool = None,
        group_id: int = None,
        isv_room_id: str = None,
        reservation_authority: main_models.CreateMeetingRoomRequestReservationAuthority = None,
        room_capacity: int = None,
        room_label_ids: List[int] = None,
        room_location: main_models.CreateMeetingRoomRequestRoomLocation = None,
        room_name: str = None,
        room_picture: str = None,
        room_status: int = None,
        tenant_context: main_models.CreateMeetingRoomRequestTenantContext = None,
    ):
        self.enable_cycle_reservation = enable_cycle_reservation
        self.group_id = group_id
        self.isv_room_id = isv_room_id
        self.reservation_authority = reservation_authority
        self.room_capacity = room_capacity
        self.room_label_ids = room_label_ids
        self.room_location = room_location
        self.room_name = room_name
        self.room_picture = room_picture
        self.room_status = room_status
        self.tenant_context = tenant_context

    def validate(self):
        if self.reservation_authority:
            self.reservation_authority.validate()
        if self.room_location:
            self.room_location.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_cycle_reservation is not None:
            result['EnableCycleReservation'] = self.enable_cycle_reservation

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.isv_room_id is not None:
            result['IsvRoomId'] = self.isv_room_id

        if self.reservation_authority is not None:
            result['ReservationAuthority'] = self.reservation_authority.to_map()

        if self.room_capacity is not None:
            result['RoomCapacity'] = self.room_capacity

        if self.room_label_ids is not None:
            result['RoomLabelIds'] = self.room_label_ids

        if self.room_location is not None:
            result['RoomLocation'] = self.room_location.to_map()

        if self.room_name is not None:
            result['RoomName'] = self.room_name

        if self.room_picture is not None:
            result['RoomPicture'] = self.room_picture

        if self.room_status is not None:
            result['RoomStatus'] = self.room_status

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableCycleReservation') is not None:
            self.enable_cycle_reservation = m.get('EnableCycleReservation')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsvRoomId') is not None:
            self.isv_room_id = m.get('IsvRoomId')

        if m.get('ReservationAuthority') is not None:
            temp_model = main_models.CreateMeetingRoomRequestReservationAuthority()
            self.reservation_authority = temp_model.from_map(m.get('ReservationAuthority'))

        if m.get('RoomCapacity') is not None:
            self.room_capacity = m.get('RoomCapacity')

        if m.get('RoomLabelIds') is not None:
            self.room_label_ids = m.get('RoomLabelIds')

        if m.get('RoomLocation') is not None:
            temp_model = main_models.CreateMeetingRoomRequestRoomLocation()
            self.room_location = temp_model.from_map(m.get('RoomLocation'))

        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')

        if m.get('RoomPicture') is not None:
            self.room_picture = m.get('RoomPicture')

        if m.get('RoomStatus') is not None:
            self.room_status = m.get('RoomStatus')

        if m.get('TenantContext') is not None:
            temp_model = main_models.CreateMeetingRoomRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class CreateMeetingRoomRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class CreateMeetingRoomRequestRoomLocation(DaraModel):
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

class CreateMeetingRoomRequestReservationAuthority(DaraModel):
    def __init__(
        self,
        authorized_members: List[main_models.CreateMeetingRoomRequestReservationAuthorityAuthorizedMembers] = None,
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
                temp_model = main_models.CreateMeetingRoomRequestReservationAuthorityAuthorizedMembers()
                self.authorized_members.append(temp_model.from_map(k1))

        return self

class CreateMeetingRoomRequestReservationAuthorityAuthorizedMembers(DaraModel):
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

