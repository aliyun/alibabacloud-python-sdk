# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindGxb700Request(DaraModel):
    def __init__(
        self,
        asr_model_id: str = None,
        audio: str = None,
        call_restrict: str = None,
        call_timeout: int = None,
        default_a: str = None,
        dtmf_config: str = None,
        expiration: str = None,
        group_id: str = None,
        industrial_id: str = None,
        need_asr: bool = None,
        need_record: bool = None,
        order_id: str = None,
        out_id: str = None,
        out_order_id: str = None,
        owner_id: int = None,
        pool_key: str = None,
        rec_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tel_b: str = None,
        tel_x: str = None,
    ):
        # The ASR model ID. Valid values: 
        # 
        # - General-Phone-Chinese Mandarin model ID: 7ee372834d2f4cc7ac0d0ab2d0ae1aac 
        # - General-Phone-Chinese Cantonese model ID: 9b4afe3d224e4fa3bf963697113e2f77 
        # - General-Phone-Regional Accent model ID: 3655a6cb94764145a1f9a38a3c3b3b4b.
        self.asr_model_id = asr_model_id
        # The audio prompt code.
        # 
        # 
        # - GCallX_Gpre: the audio prompt code played to the caller before the call is connected when a number in group G calls number X.
        # - GCallX_Gin: the audio prompt code played to the caller after the call is connected when a number in group G calls number X.
        # - GCallX_Bin: the audio prompt code played to user B after the call is connected when a number in group G calls number X.
        # - BCallX_Bpre: the audio prompt code played to user B before the call is connected when user B calls number X.
        # - BCallX_Gin: the audio prompt code played to the callee after the call is connected when number X is called.
        # - BCallX_Bin: the audio prompt code played to user B after the call is connected when user B calls number X.
        self.audio = audio
        # The one-way call restriction logic. Valid values:
        # 
        # - CONTROL_BX_DISABLE: number B cannot call number X.
        # - CONTROL_GX_DISABLE: numbers in number group G cannot call number X.
        self.call_restrict = call_restrict
        # The sequential ringing duration. Unit: seconds. Valid values: 5 to 20.
        self.call_timeout = call_timeout
        # Phone number A.
        # The DefaultA number for the GXB private number.
        # 
        # > Note
        # The callback mode can be configured at the number pool level. When the callback mode is set to default, this field takes effect. When user B calls number X, the call is forwarded to this A number by default. If number A is not configured, the call cannot be connected.
        # To update number A, call the number binding modification operation.
        self.default_a = default_a
        # The DTMF key configuration, used when setting up AXB intermediate number binding. The following items can be configured:
        # 
        # - endCallIvrPhoneNo: the party to play the audio prompt to, A or B. 
        # - waitingDtmfTime: the maximum wait time after the first audio prompt is played. Maximum value: 30 seconds. 
        # - maxLoop dtmf: the maximum number of times the first audio file is played in a loop when the key input does not match. Maximum value: 5. 
        # - step1File: the name of the first audio file. 
        # - step2File: the name of the second audio file.
        # - validKey: the valid key values, such as 1,2. Only two valid key values can be configured, separated by ",". 
        # - waitingEndCall: the carrier hang-up wait time. Maximum value: 10 seconds.
        self.dtmf_config = dtmf_config
        # The expiration time of the number binding.
        # 
        # > Note
        # The expiration time must be at least 1 minute later than the current binding time, accurate to the second.
        # You can manually unbind the number at any time before the binding expires.
        # If you unbind a number that is in an active call, the current call is not affected.
        # 
        # This parameter is required.
        self.expiration = expiration
        # The ID of number group G.
        # 
        # Number group G is created by using the "Create G Number Group" message.
        self.group_id = group_id
        # - The Industrial Internet identifier code, which has a one-to-one mapping with OrderID.
        # 
        # - The code supports characters such as "." and "/" as domain separators. The code must not contain non-printable characters such as spaces or line breaks.
        # 
        # - This field is required when the business user generates the Industrial Internet identifier code independently.
        self.industrial_id = industrial_id
        # Specifies whether to enable the ASR service. Valid values: 
        # 
        # - false: Disabled (default value).
        # 
        # - true: Enabled.
        self.need_asr = need_asr
        # Specifies whether the business user requires all call media files generated by this number binding relationship. Valid values:
        # 
        # - true: Enable recording.
        # - false: Disable recording (default value).
        self.need_record = need_record
        # The business order code.
        # 
        # - This code has a one-to-one mapping with the actual business order and must be unique.
        # 
        # - The code supports characters such as "." and "/" as domain separators. The code must not contain non-printable characters such as spaces or line breaks.
        # 
        # - This field is required when the business user submits a business order code and the platform generates an Industrial Internet identifier code.
        self.order_id = order_id
        # An external business extension field. This parameter is returned in the call record receipt message.
        self.out_id = out_id
        # The external business ID.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # The key of the China 700 number pool.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        # The recording type. Valid values: mp3 and wav.
        self.rec_type = rec_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Phone number of user B.
        # 
        # This parameter is required.
        self.tel_b = tel_b
        # The intermediate number X. If the business user does not specify an X number, the platform assigns a number from the number pool as the X number.
        self.tel_x = tel_x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id

        if self.audio is not None:
            result['Audio'] = self.audio

        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict

        if self.call_timeout is not None:
            result['CallTimeout'] = self.call_timeout

        if self.default_a is not None:
            result['DefaultA'] = self.default_a

        if self.dtmf_config is not None:
            result['DtmfConfig'] = self.dtmf_config

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.industrial_id is not None:
            result['IndustrialId'] = self.industrial_id

        if self.need_asr is not None:
            result['NeedAsr'] = self.need_asr

        if self.need_record is not None:
            result['NeedRecord'] = self.need_record

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.rec_type is not None:
            result['RecType'] = self.rec_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tel_b is not None:
            result['TelB'] = self.tel_b

        if self.tel_x is not None:
            result['TelX'] = self.tel_x

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')

        if m.get('Audio') is not None:
            self.audio = m.get('Audio')

        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')

        if m.get('CallTimeout') is not None:
            self.call_timeout = m.get('CallTimeout')

        if m.get('DefaultA') is not None:
            self.default_a = m.get('DefaultA')

        if m.get('DtmfConfig') is not None:
            self.dtmf_config = m.get('DtmfConfig')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IndustrialId') is not None:
            self.industrial_id = m.get('IndustrialId')

        if m.get('NeedAsr') is not None:
            self.need_asr = m.get('NeedAsr')

        if m.get('NeedRecord') is not None:
            self.need_record = m.get('NeedRecord')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('RecType') is not None:
            self.rec_type = m.get('RecType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TelB') is not None:
            self.tel_b = m.get('TelB')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        return self

