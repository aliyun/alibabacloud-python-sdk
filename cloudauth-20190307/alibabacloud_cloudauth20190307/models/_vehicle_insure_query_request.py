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
        # The parameter type. Valid values:
        # - **normal**: No encryption.
        # - **md5**: MD5 encryption.
        self.param_type = param_type
        # The license plate number.
        # > 
        # > - If paramType is set to normal, enter the plaintext.
        # > - If paramType is set to md5, enter the plaintext of the license plate number excluding the last two characters, followed by the MD5 hash (32-character lowercase) of the last two characters.
        self.vehicle_num = vehicle_num
        # The permitted vehicle type of the driver\\"s license.
        self.vehicle_type = vehicle_type
        # The vehicle identification number (VIN).
        # > 
        # > - If paramType is set to normal, enter the plaintext.
        # > - If paramType is set to md5, enter the plaintext of the VIN excluding the last four characters, followed by the MD5 hash (32-character lowercase) of the last four characters.
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

