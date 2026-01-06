# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMeetingRoomShrinkRequest(DaraModel):
    def __init__(
        self,
        enable_cycle_reservation: bool = None,
        group_id: int = None,
        isv_room_id: str = None,
        reservation_authority_shrink: str = None,
        room_capacity: int = None,
        room_id: str = None,
        room_label_ids_shrink: str = None,
        room_location_shrink: str = None,
        room_name: str = None,
        room_picture: str = None,
        room_status: int = None,
        tenant_context_shrink: str = None,
    ):
        self.enable_cycle_reservation = enable_cycle_reservation
        self.group_id = group_id
        self.isv_room_id = isv_room_id
        self.reservation_authority_shrink = reservation_authority_shrink
        self.room_capacity = room_capacity
        self.room_id = room_id
        self.room_label_ids_shrink = room_label_ids_shrink
        self.room_location_shrink = room_location_shrink
        self.room_name = room_name
        self.room_picture = room_picture
        self.room_status = room_status
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

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

        if self.reservation_authority_shrink is not None:
            result['ReservationAuthority'] = self.reservation_authority_shrink

        if self.room_capacity is not None:
            result['RoomCapacity'] = self.room_capacity

        if self.room_id is not None:
            result['RoomId'] = self.room_id

        if self.room_label_ids_shrink is not None:
            result['RoomLabelIds'] = self.room_label_ids_shrink

        if self.room_location_shrink is not None:
            result['RoomLocation'] = self.room_location_shrink

        if self.room_name is not None:
            result['RoomName'] = self.room_name

        if self.room_picture is not None:
            result['RoomPicture'] = self.room_picture

        if self.room_status is not None:
            result['RoomStatus'] = self.room_status

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

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
            self.reservation_authority_shrink = m.get('ReservationAuthority')

        if m.get('RoomCapacity') is not None:
            self.room_capacity = m.get('RoomCapacity')

        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')

        if m.get('RoomLabelIds') is not None:
            self.room_label_ids_shrink = m.get('RoomLabelIds')

        if m.get('RoomLocation') is not None:
            self.room_location_shrink = m.get('RoomLocation')

        if m.get('RoomName') is not None:
            self.room_name = m.get('RoomName')

        if m.get('RoomPicture') is not None:
            self.room_picture = m.get('RoomPicture')

        if m.get('RoomStatus') is not None:
            self.room_status = m.get('RoomStatus')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

