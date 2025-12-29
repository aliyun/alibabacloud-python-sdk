# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportRoomControlDevicesShrinkRequest(DaraModel):
    def __init__(
        self,
        enable_infrared_device_import: str = None,
        enable_mesh_device_import: str = None,
        hotel_id: str = None,
        location_devices_shrink: str = None,
        room_no: str = None,
    ):
        self.enable_infrared_device_import = enable_infrared_device_import
        self.enable_mesh_device_import = enable_mesh_device_import
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.location_devices_shrink = location_devices_shrink
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_infrared_device_import is not None:
            result['EnableInfraredDeviceImport'] = self.enable_infrared_device_import

        if self.enable_mesh_device_import is not None:
            result['EnableMeshDeviceImport'] = self.enable_mesh_device_import

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.location_devices_shrink is not None:
            result['LocationDevices'] = self.location_devices_shrink

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInfraredDeviceImport') is not None:
            self.enable_infrared_device_import = m.get('EnableInfraredDeviceImport')

        if m.get('EnableMeshDeviceImport') is not None:
            self.enable_mesh_device_import = m.get('EnableMeshDeviceImport')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('LocationDevices') is not None:
            self.location_devices_shrink = m.get('LocationDevices')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

