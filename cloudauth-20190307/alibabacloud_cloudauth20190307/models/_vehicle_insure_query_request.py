# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VehicleInsureQueryRequest(DaraModel):
    def __init__(
        self,
        param_type: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
        vin: str = None,
    ):
        # Parameter type:
        # 
        # - **normal**: Unencrypted.
        # - **md5**: MD5 encrypted.
        self.param_type = param_type
        # License plate number
        # > 
        # > - When `paramType` is set to `normal`, enter the plain text.
        # > - When `paramType` is set to `md5`, enter the plain text of all but the last two characters of the license plate + the MD5 encryption (32 lowercase characters) of the last two characters of the license plate.
        self.vehicle_num = vehicle_num
        # Driver\\"s license vehicle type.
        self.vehicle_type = vehicle_type
        # Vehicle identification code, i.e., the vehicle VIN
        # 
        # 
        # > 
        # > - When `paramType` is set to `normal`, enter the plain text.
        # > - When `paramType` is set to `md5`, enter the plain text of all but the last four characters of the VIN + the MD5 encryption (32 lowercase characters) of the last four characters of the VIN.
        self.vin = vin

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

        if self.vin is not None:
            result['Vin'] = self.vin

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')

        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')

        if m.get('Vin') is not None:
            self.vin = m.get('Vin')

        return self

