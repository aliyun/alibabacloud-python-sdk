# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAxb700Request(DaraModel):
    def __init__(
        self,
        asr_model_id: str = None,
        audio: str = None,
        call_restrict: str = None,
        call_timeout: int = None,
        dtmf_config: str = None,
        expiration: str = None,
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
        tel_a: str = None,
        tel_b: str = None,
        tel_x: str = None,
    ):
        # Optional. The ASR model ID. Valid values:
        # 
        # - General-Phone-Mandarin model ID: 7ee372834d2f4cc7ac0d0ab2d0ae1aac
        # - General-Phone-Cantonese model ID: 9b4afe3d224e4fa3bf963697113e2f77
        # - General-Phone-Regional Accent model ID: 3655a6cb94764145a1f9a38a3c3b3b4b.
        self.asr_model_id = asr_model_id
        # The audio prompt encoding.
        # 
        # - ACallX_Apre: The audio prompt encoding played to A before the call is connected when A calls X.
        # - ACallX_Ain: The audio prompt encoding played to A after the call is connected when A calls X.
        # - ACallX_Bin: The audio prompt encoding played to B after the call is connected when A calls X.
        # - BCallX_Bpre: The audio prompt encoding played to B before the call is connected when B calls X.
        # - BCallX_Ain: The audio prompt encoding played to A after the call is connected when B calls X.
        # - BCallX_Bin: The audio prompt encoding played to B after the call is connected when B calls X.
        self.audio = audio
        # The one-way call restriction logic. Valid values:
        # 
        # - CONTROL_AX_DISABLE: Number A cannot call number X.
        # 
        # - CONTROL_BX_DISABLE: Number B cannot call number X.
        self.call_restrict = call_restrict
        # The sequential ringing duration. Unit: seconds. Valid values: 5 to 20.
        self.call_timeout = call_timeout
        # Optional. The DTMF key configuration for 700AXB number binding. The following items can be configured:
        # 
        # - endCallIvrPhoneNo: The audio playback target, A or B.
        # - waitingDtmfTime: The maximum wait time after the first audio file is played. Maximum value: 30 seconds.
        # - maxLoop dtmf: The maximum number of times the first audio file is replayed when a key press does not match. Maximum value: 5.
        # - step1File: The name of the first audio file.
        # - step2File: The name of the second audio file.
        # - validKey: The valid key values, such as 1,2. Only two valid key values can be configured, separated by commas (,).
        # - waitingEndCall: The carrier hang-up wait time. Maximum value: 10 seconds.
        self.dtmf_config = dtmf_config
        # The expiration time of the number binding.
        # 
        # > - The expiration time must be at least 1 minute later than the current binding time, accurate to the second.
        # >- You can manually unbind the number at any time before the binding expires.
        # >- If you unbind a number that is in an active call, the current call is not affected.
        # 
        # This parameter is required.
        self.expiration = expiration
        # The industrial Internet identifier code, which has a one-to-one mapping with OrderId.
        # 
        # The code supports characters such as "." and "/" as domain separators. The code must not contain non-printable characters such as spaces or line breaks.
        # 
        # This field is required when the caller generates the industrial Internet identifier code independently.
        # 
        # > 
        # > - Either OrderId or IndustrialId is required depending on the business scenario.
        self.industrial_id = industrial_id
        # Specifies whether to enable the ASR service. Valid values:
        # 
        # - false: Disable (default).
        # 
        # - true: Enable.
        self.need_asr = need_asr
        # Specifies whether call recording files are required for all calls made through this number binding. Valid values:
        # 
        # - true: Enable recording.
        # 
        # - false: Disable recording (default).
        self.need_record = need_record
        # The business order code.
        # 
        # - This code has a one-to-one mapping with the actual business order and must be unique.
        # 
        # - The code supports characters such as "." and "/" as domain separators. The code must not contain non-printable characters such as spaces or line breaks.
        # 
        # - This field is required when the caller submits a business order code and the platform generates an industrial Internet identifier code.
        # > 
        # > - Either OrderId or IndustrialId is required depending on the business scenario.
        self.order_id = order_id
        # The external business extension field. This parameter is returned in the call record receipt message.
        self.out_id = out_id
        # The external business ID.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # The key of the China 700 number pool.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        # The recording file format. Valid values: mp3 and wav.
        self.rec_type = rec_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The phone number of user A.
        # 
        # This parameter is required.
        self.tel_a = tel_a
        # The phone number of user B.
        # 
        # This parameter is required.
        self.tel_b = tel_b
        # Optional. The intermediate number X.
        # > - If the caller does not specify an X number,
        # > - the platform assigns a number from the number pool as the X number.
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

        if self.dtmf_config is not None:
            result['DtmfConfig'] = self.dtmf_config

        if self.expiration is not None:
            result['Expiration'] = self.expiration

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

        if self.tel_a is not None:
            result['TelA'] = self.tel_a

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

        if m.get('DtmfConfig') is not None:
            self.dtmf_config = m.get('DtmfConfig')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

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

        if m.get('TelA') is not None:
            self.tel_a = m.get('TelA')

        if m.get('TelB') is not None:
            self.tel_b = m.get('TelB')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        return self

