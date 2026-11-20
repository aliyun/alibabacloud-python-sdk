# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAxbBindFixedLineShrinkRequest(DaraModel):
    def __init__(
        self,
        anucode: str = None,
        anucodecalled: str = None,
        app_id: str = None,
        expiration: str = None,
        extra_shrink: str = None,
        order_id: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sub_id: str = None,
        subts: str = None,
        tanucode_connect: str = None,
        tel_a: str = None,
        tel_b: str = None,
        ts: str = None,
    ):
        # The caller-side audio playback code. This parameter is required for the AXB privacy number service for landlines. The audio playback code must include codes for three scenarios. Specify the codes in the order of "B->X, A->X, and other numbers->X", and separate the codes with commas.
        # 
        # > "1,2,3" indicates that the audio playback code for B->X is 1, the code for A->X is 2, and the code for other numbers->X is 3.
        self.anucode = anucode
        # The callee-side audio playback code after the call is connected. The callee-side audio playback code must include codes for two scenarios. Specify the codes in the order of "A as the callee and B as the callee", and separate the codes with commas.
        # 
        # > "1,2" indicates that the audio playback code when Number A answers as the callee is 1, and the code when Number B answers as the callee is 2.
        self.anucodecalled = anucodecalled
        # The ID of the number pool.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The expiration time. Unit: seconds. Valid values:
        # 
        # - 0: The binding never expires.
        # 
        # - Other values: If you specify another value, such as 60, the binding is valid for 60 seconds after Number X is allocated. After 60 seconds, the binding is automatically unbound.
        self.expiration = expiration
        # The extension parameters.
        self.extra_shrink = extra_shrink
        # The unique identifier of the message request.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id
        # The external business extension field. This parameter is returned in the call record receipt message. The value cannot exceed 100 characters in length.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The binding ID.
        # 
        # This parameter is required.
        self.sub_id = sub_id
        # The binding time. The format is yyyyMMddHHmmss. The time is in UTC+8 and uses the 24-hour format.
        # 
        # This parameter is required.
        self.subts = subts
        # The caller-side audio playback code after the call is connected. The caller-side audio playback code after connection must include codes for two scenarios. Specify the codes in the order of "A as the callee and B as the callee", and separate the codes with commas.
        # 
        # > "1,2" indicates that the caller-side audio playback code when Number A is the callee is 1, and the caller-side audio playback code when Number B is the callee is 2.
        self.tanucode_connect = tanucode_connect
        # Sets Number A in the binding relationship.
        # 
        # 
        # > - Number A can be set to a mobile phone number or a landline number. If it is a landline number, you must add the area code. No hyphen is required between the area code and the number.
        # > - You cannot update TelA and TelB at the same time.
        self.tel_a = tel_a
        # Sets Number B in the binding relationship.
        # 
        # 
        # > - Number B can be set to a mobile phone number or a landline number. If it is a landline number, you must add the area code. No hyphen is required between the area code and the number.
        # > - You cannot update TelA and TelB at the same time.
        self.tel_b = tel_b
        # The business timestamp. The format is yyyyMMddHHmmssSSS. The time is in UTC+8 and uses the 24-hour format. The precision is accurate to milliseconds.
        # 
        # This parameter is required.
        self.ts = ts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anucode is not None:
            result['Anucode'] = self.anucode

        if self.anucodecalled is not None:
            result['Anucodecalled'] = self.anucodecalled

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sub_id is not None:
            result['SubId'] = self.sub_id

        if self.subts is not None:
            result['Subts'] = self.subts

        if self.tanucode_connect is not None:
            result['TAnucodeConnect'] = self.tanucode_connect

        if self.tel_a is not None:
            result['TelA'] = self.tel_a

        if self.tel_b is not None:
            result['TelB'] = self.tel_b

        if self.ts is not None:
            result['Ts'] = self.ts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Anucode') is not None:
            self.anucode = m.get('Anucode')

        if m.get('Anucodecalled') is not None:
            self.anucodecalled = m.get('Anucodecalled')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Extra') is not None:
            self.extra_shrink = m.get('Extra')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')

        if m.get('Subts') is not None:
            self.subts = m.get('Subts')

        if m.get('TAnucodeConnect') is not None:
            self.tanucode_connect = m.get('TAnucodeConnect')

        if m.get('TelA') is not None:
            self.tel_a = m.get('TelA')

        if m.get('TelB') is not None:
            self.tel_b = m.get('TelB')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

