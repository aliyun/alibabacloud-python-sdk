# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Vehicle5ItemQueryRequest(DaraModel):
    def __init__(
        self,
        param_type: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
    ):
        # Parameter type:
        # 
        # - **normal**: Unencrypted.
        # - **md5**: MD5 encrypted.
        self.param_type = param_type
        # License plate number
        # 
        # > 
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, enter the plain text of all but the last two characters of the license plate + MD5 encryption (32-bit lowercase MD5) of the last two characters.
        self.vehicle_num = vehicle_num
        # Vehicle type
        # 
        # > 
        # > - 02: Ordinary passenger car
        # > - 52: New energy passenger car
        self.vehicle_type = vehicle_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num

        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')

        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')

        return self

