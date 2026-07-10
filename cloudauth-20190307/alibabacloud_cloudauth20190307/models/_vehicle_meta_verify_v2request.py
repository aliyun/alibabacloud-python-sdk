# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VehicleMetaVerifyV2Request(DaraModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
        verify_meta_type: str = None,
    ):
        # The ID card number.
        # 
        # This parameter is required when VerifyMetaType is set to VEHICLE_3_META.
        # 
        # > 
        # > - If ParamType is set to normal, enter the plaintext value.
        # > - If ParamType is set to md5, enter the first 6 digits of the ID card number in plaintext + the MD5-encrypted date of birth (32-bit lowercase MD5) + the last 4 digits of the ID card number.
        self.identify_num = identify_num
        # The parameter type. Valid values:
        # 
        # - normal: not encrypted.
        # - md5: MD5-encrypted.
        self.param_type = param_type
        # The name.
        # > 
        # > - If ParamType is set to normal, enter the plaintext value.
        # > - If ParamType is set to md5, enter the MD5-encrypted first character of the name (32-bit lowercase MD5) + the remaining characters of the name in plaintext.
        self.user_name = user_name
        # The license plate number.
        # 
        # > 
        # > - If ParamType is set to normal, enter the plaintext value.
        # > - If ParamType is set to md5, enter the license plate number excluding the last two characters in plaintext + the MD5-encrypted last two characters (32-bit lowercase MD5).
        self.vehicle_num = vehicle_num
        # The vehicle type.
        self.vehicle_type = vehicle_type
        # The verification type.
        # 
        # > 
        # > - VEHICLE_2_META: two-element verification. Verifies the name and license plate number.
        # > - VEHICLE_3_META: three-element verification. Verifies the name, license plate number, and ID card number.
        self.verify_meta_type = verify_meta_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.vehicle_num is not None:
            result['VehicleNum'] = self.vehicle_num

        if self.vehicle_type is not None:
            result['VehicleType'] = self.vehicle_type

        if self.verify_meta_type is not None:
            result['VerifyMetaType'] = self.verify_meta_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VehicleNum') is not None:
            self.vehicle_num = m.get('VehicleNum')

        if m.get('VehicleType') is not None:
            self.vehicle_type = m.get('VehicleType')

        if m.get('VerifyMetaType') is not None:
            self.verify_meta_type = m.get('VerifyMetaType')

        return self

