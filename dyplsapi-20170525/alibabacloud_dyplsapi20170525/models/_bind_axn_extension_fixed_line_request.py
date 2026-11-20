# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class BindAxnExtensionFixedLineRequest(DaraModel):
    def __init__(
        self,
        anucode: str = None,
        anucodecalled: str = None,
        app_id: str = None,
        areacode: str = None,
        bind_type: str = None,
        expiration: str = None,
        extraaxx: main_models.BindAxnExtensionFixedLineRequestExtraaxx = None,
        order_id: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subts: str = None,
        tanucode_connect: str = None,
        tel_a: str = None,
        tel_x: str = None,
        tel_xext: str = None,
        ts: str = None,
    ):
        # Caller-side ringtone code. This parameter is required for AXB scenarios. Must contain codes for 3 scenarios. Enter the codes in the order of "B->X, A->X, other numbers->X", separated by commas.
        # 
        # > "1,2,3" indicates that the ringtone code for B->X is 1, for A->X is 2, and for other numbers->X is 3.
        # 
        # This parameter is required.
        self.anucode = anucode
        # Called-side ringtone code after connection. Must contain codes for 2 scenarios. Enter the codes in the order of "A as called party, B as called party", separated by commas.
        # 
        # > "1,2" indicates that the ringtone code when A is the called party is 1, and the ringtone code when B is the called party is 2.
        self.anucodecalled = anucodecalled
        # Number pool ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Area code. Supports specifying the home location of the X number (specified city -> provincial capital -> nationwide routing). If no home location is specified, a number is randomly assigned nationwide.
        self.areacode = areacode
        # Binding type. Valid values:
        # 
        # - mode101: Customer specifies the X number.
        # 
        # - mode102: Platform assigns the X number.
        # 
        # This parameter is required.
        self.bind_type = bind_type
        # Expiration time. Unit: seconds. Valid values:
        # 
        # - 0: Never expires.
        # 
        # - Other values: When other values are specified, such as 60, the binding is valid for 60 seconds after the X number is successfully assigned. After 60 seconds, the binding is automatically released.
        # 
        # This parameter is required.
        self.expiration = expiration
        # Extension parameters.
        self.extraaxx = extraaxx
        # Unique identifier of the message request.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id
        # External business extension field. This parameter is returned in call record receipt messages. Must not exceed 100 characters.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Binding time. Format: yyyyMMddHHmmss. Uses Beijing time, 24-hour clock.
        # 
        # This parameter is required.
        self.subts = subts
        # Caller-side ringtone code after connection. Must contain codes for 2 scenarios. Enter the codes in the order of "A as called party, B as called party", separated by commas.
        # 
        # > "1,2" indicates that the caller-side ringtone code when A is the called party is 1, and the caller-side ringtone code when B is the called party is 2.
        self.tanucode_connect = tanucode_connect
        # The A number for the fixed-line AXN extension number.
        # 
        # > The A number can be set to a mobile number or a fixed-line number. Fixed-line numbers must include the area code, and no hyphen is needed between the area code and the number.
        # 
        # This parameter is required.
        self.tel_a = tel_a
        # The X number for the fixed-line AXN extension number. The X number is a privacy number that you have [purchased](https://dyplsnext.console.aliyun.com/numberbuy) in the console.
        self.tel_x = tel_x
        # Extension number. This parameter is required when the BindType parameter is set to mode101.
        self.tel_xext = tel_xext
        # Business timestamp. Format: yyyyMMddHHmmssSSS. Uses Beijing time, 24-hour clock, accurate to milliseconds.
        # 
        # This parameter is required.
        self.ts = ts

    def validate(self):
        if self.extraaxx:
            self.extraaxx.validate()

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

        if self.areacode is not None:
            result['Areacode'] = self.areacode

        if self.bind_type is not None:
            result['BindType'] = self.bind_type

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.extraaxx is not None:
            result['Extraaxx'] = self.extraaxx.to_map()

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

        if self.subts is not None:
            result['Subts'] = self.subts

        if self.tanucode_connect is not None:
            result['TAnucodeConnect'] = self.tanucode_connect

        if self.tel_a is not None:
            result['TelA'] = self.tel_a

        if self.tel_x is not None:
            result['TelX'] = self.tel_x

        if self.tel_xext is not None:
            result['TelXext'] = self.tel_xext

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

        if m.get('Areacode') is not None:
            self.areacode = m.get('Areacode')

        if m.get('BindType') is not None:
            self.bind_type = m.get('BindType')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Extraaxx') is not None:
            temp_model = main_models.BindAxnExtensionFixedLineRequestExtraaxx()
            self.extraaxx = temp_model.from_map(m.get('Extraaxx'))

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

        if m.get('Subts') is not None:
            self.subts = m.get('Subts')

        if m.get('TAnucodeConnect') is not None:
            self.tanucode_connect = m.get('TAnucodeConnect')

        if m.get('TelA') is not None:
            self.tel_a = m.get('TelA')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        if m.get('TelXext') is not None:
            self.tel_xext = m.get('TelXext')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

class BindAxnExtensionFixedLineRequestExtraaxx(DaraModel):
    def __init__(
        self,
        callback: str = None,
        callrecording: str = None,
    ):
        # Callback control. When A calls through X, that is, A dials X as the caller. Valid values:
        # 
        # - 0 (default): Cannot make outbound calls.
        # 
        # - 1: Connect to the most recent N number.
        # 
        # - 2: Call back the fixed number TelB.
        self.callback = callback
        # Recording control. Valid values:
        # 
        # - 0 (default): No recording.
        # 
        # - 1: Recording.
        # 
        # > After you enable the call recording feature, you can play and download audio files in the call records. Recording files are billed at CNY 0.010/minute.
        self.callrecording = callrecording

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback is not None:
            result['Callback'] = self.callback

        if self.callrecording is not None:
            result['Callrecording'] = self.callrecording

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('Callrecording') is not None:
            self.callrecording = m.get('Callrecording')

        return self

