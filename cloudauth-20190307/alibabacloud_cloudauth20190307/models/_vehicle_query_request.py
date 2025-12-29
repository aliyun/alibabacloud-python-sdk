# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VehicleQueryRequest(DaraModel):
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
        # > - When paramType is set to md5, enter the unencrypted part of the license plate number except for the last two characters + the MD5 (32 lowercase) encryption of the last two characters of the license plate.
        self.vehicle_num = vehicle_num
        # Vehicle type
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

