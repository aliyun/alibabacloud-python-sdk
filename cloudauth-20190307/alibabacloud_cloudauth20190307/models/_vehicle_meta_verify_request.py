# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VehicleMetaVerifyRequest(DaraModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
        vehicle_num: str = None,
        vehicle_type: str = None,
        verify_meta_type: str = None,
    ):
        # ID number.
        # 
        # This is a required field when VerifyMetaType is set to VEHICLE_3_META.
        # > 
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, enter the first 6 digits in plain text + the birth date encrypted with MD5 (32 lowercase characters) + the last 4 digits in plain text.
        self.identify_num = identify_num
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: Encrypted with MD5.
        self.param_type = param_type
        # Name
        # 
        # > This is an explanation
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, encrypt the first character of the name with MD5 (32 lowercase characters) + the rest of the name in plain text.
        self.user_name = user_name
        # Vehicle license plate
        # 
        # > 
        # > - When paramType is set to normal, enter the plain text.
        # > - When paramType is set to md5, enter the part of the license plate except for the last two characters in plain text + the last two characters of the license plate encrypted with MD5 (32 lowercase characters).
        self.vehicle_num = vehicle_num
        # Vehicle type
        self.vehicle_type = vehicle_type
        # Verification type
        # 
        # > 
        # > - VEHICLE_2_META: Two-element verification, name + vehicle license plate verification;
        # > - VEHICLE_3_META: Three-element verification, name + vehicle license plate + ID number verification;
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

