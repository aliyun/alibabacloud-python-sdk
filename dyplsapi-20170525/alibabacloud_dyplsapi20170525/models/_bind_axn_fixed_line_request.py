# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class BindAxnFixedLineRequest(DaraModel):
    def __init__(
        self,
        anucode: str = None,
        anucodecalled: str = None,
        app_id: str = None,
        areacode: str = None,
        bind_type: str = None,
        expiration: str = None,
        extra: main_models.BindAxnFixedLineRequestExtra = None,
        order_id: str = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subts: str = None,
        tanucode_connect: str = None,
        tel_a: str = None,
        tel_b: str = None,
        tel_x: str = None,
        ts: str = None,
    ):
        # The audio prompt codes for the caller side. The value must include codes for three scenarios. Specify the codes in the order of B->X, A->X, and other numbers->X, separated by commas.
        # 
        # > For example, 1,2,3 indicates that the audio prompt code for B->X is 1, the code for A->X is 2, and the code for other numbers->X is 3.
        # 
        # This parameter is required.
        self.anucode = anucode
        # The audio prompt codes for the callee side. The value must include codes for two scenarios. Specify the codes in the order of A as the callee and other numbers as the callee, separated by commas.
        # 
        # > For example, 1,2 indicates that the audio prompt code when number A answers as the callee is 1, and the code when other numbers answer as the callee is 2.
        self.anucodecalled = anucodecalled
        # The ID of the number pool.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The area code. You can specify the location of number X (specified city -> provincial capital -> national routing). If you do not specify the location, a number is randomly assigned nationwide.
        self.areacode = areacode
        # The binding type. Valid values:
        # 
        # - mode101: The customer specifies number X.
        # 
        # - mode102: The platform assigns number X.
        # 
        # This parameter is required.
        self.bind_type = bind_type
        # The expiration time. Unit: seconds. Valid values:
        # 
        # - 0: The binding never expires.
        # 
        # - Other values: If you specify another value, such as 60, the binding is valid for 60 seconds after number X is successfully assigned. After 60 seconds, the binding is automatically unbound.
        # 
        # This parameter is required.
        self.expiration = expiration
        # The extended parameters.
        self.extra = extra
        # The unique identifier of the message request.
        # 
        # This parameter is required.
        self.order_id = order_id
        self.owner_id = owner_id
        # The external business extension field. This parameter is returned in the call record receipt message. The value cannot exceed 100 characters in length.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The binding time. The format is yyyyMMddHHmmss. The time is in UTC+8 and uses the 24-hour clock.
        # 
        # This parameter is required.
        self.subts = subts
        # The audio prompt codes for the caller side after the call is connected. The value must include codes for two scenarios. Specify the codes in the order of A as the callee and other numbers as the callee, separated by commas.
        # 
        # > For example, 1,2 indicates that the audio prompt code for the caller side when number A is the callee is 1, and the code for the caller side when other numbers are the callee is 2.
        self.tanucode_connect = tanucode_connect
        # Number A of the fixed-line AXN privacy number.
        # 
        # 
        # > - Number A can be a mobile phone number or a fixed-line number. A fixed-line number must include the area code, and no hyphen is required between the area code and the number.
        # > - If your business requires modifying a bound number, you can call the [UpdateAxnBindFixedLine](https://api.aliyun.com/document/Dyplsapi/2017-05-25/UpdateAxnBindFixedLine) operation to modify it.
        # 
        # This parameter is required.
        self.tel_a = tel_a
        # Number N of the fixed-line AXN privacy number.
        self.tel_b = tel_b
        # Number X of the fixed-line AXN privacy number. Number X is the privacy number that you have purchased in the console.
        # 
        # > This parameter is required in the mode where the customer specifies number X (that is, the BindType parameter is set to mode101).
        self.tel_x = tel_x
        # The business timestamp. The format is yyyyMMddHHmmssSSS. The time is in UTC+8 and uses the 24-hour clock, accurate to milliseconds.
        # 
        # This parameter is required.
        self.ts = ts

    def validate(self):
        if self.extra:
            self.extra.validate()

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

        if self.extra is not None:
            result['Extra'] = self.extra.to_map()

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

        if self.tel_b is not None:
            result['TelB'] = self.tel_b

        if self.tel_x is not None:
            result['TelX'] = self.tel_x

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

        if m.get('Extra') is not None:
            temp_model = main_models.BindAxnFixedLineRequestExtra()
            self.extra = temp_model.from_map(m.get('Extra'))

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

        if m.get('TelB') is not None:
            self.tel_b = m.get('TelB')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        if m.get('Ts') is not None:
            self.ts = m.get('Ts')

        return self

class BindAxnFixedLineRequestExtra(DaraModel):
    def __init__(
        self,
        callback: str = None,
        callrecording: str = None,
    ):
        # The callback control. This applies when User A makes a call through number X, meaning User A calls number X. Valid values:
        # 
        # - 0 (default): Outbound calls are not allowed.
        # 
        # - 1: Connects to the most recent number N.
        # 
        # - 2: Calls back the fixed number TelB.
        self.callback = callback
        # The call recording control. Valid values:
        # 
        # - 0 (default): Call recording is disabled.
        # 
        # - 1: Call recording is enabled.
        # 
        # > After you enable call recording, you can play and download audio files in the call records. Audio files are billed at CNY 0.010 per minute.
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

