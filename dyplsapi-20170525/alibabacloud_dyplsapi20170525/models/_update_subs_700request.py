# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubs700Request(DaraModel):
    def __init__(
        self,
        asr_model_id: str = None,
        audio: str = None,
        call_restrict: str = None,
        default_a: str = None,
        expiration: str = None,
        group_id: str = None,
        industrial_id: str = None,
        need_asr: bool = None,
        need_record: bool = None,
        operate_type: str = None,
        order_id: str = None,
        out_id: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subs_id: int = None,
        tel_a: str = None,
        tel_b: str = None,
        tel_x: str = None,
    ):
        # The ASR model ID. Valid values:
        # - General-telephone-Mandarin Chinese model ID: 7ee372834d2f4cc7ac0d0ab2d0ae1aac.
        # - General-telephone-Cantonese model ID: 9b4afe3d224e4fa3bf963697113e2f77.
        # - General-telephone-regional accent model ID: 3655a6cb94764145a1f9a38a3c3b3b4b.
        self.asr_model_id = asr_model_id
        # Optional. The audio playback code.
        # - AXB mode:
        # ACallX_Apre: The audio playback code for the voice prompt played to Number A before the call is connected when Number A calls Number X.
        # ACallX_Ain: The audio playback code for the voice prompt played to Number A after the call is connected when Number A calls Number X.
        # ACallX_Bin: The audio playback code for the voice prompt played to Number B after the call is connected when Number A calls Number X.
        # BCallX_Bpre: The audio playback code for the voice prompt played to Number B before the call is connected when Number B calls Number X.
        # BCallX_Ain: The audio playback code for the voice prompt played to Number A after the call is connected when Number B calls Number X.
        # BCallX_Bin: The audio playback code for the voice prompt played to Number B after the call is connected when Number B calls Number X.
        # - GXB mode:
        # GCallX_Gpre: The audio playback code for the voice prompt played to the caller before the call is connected when a number in Group G calls Number X.
        # GCallX_Gin: The audio playback code for the voice prompt played to the caller after the call is connected when a number in Group G calls Number X.
        # GCallX_Bin: The audio playback code for the voice prompt played to Number B after the call is connected when a number in Group G calls Number X.
        # BCallX_Bpre: The audio playback code for the voice prompt played to Number B before the call is connected when Number B calls Number X.
        # BCallX_Gin: The audio playback code for the voice prompt played to the callee after the call is connected when Number B calls Number X.
        # BCallX_Bin: The audio playback code for the voice prompt played to Number B after the call is connected when Number B calls Number X.
        self.audio = audio
        # The new single-call restriction logic.
        self.call_restrict = call_restrict
        # The default Number A for the GXB private number. Note: The callback mode can be set at the number pool level. When the callback mode is set to the default mode, this field takes effect. When Number B calls Number X, the call is forwarded to this Number A by default. If Number A is not set, the call cannot be connected. To update Number A, call the number binding modification API.
        self.default_a = default_a
        # The new expiration time of the binding relationship.
        self.expiration = expiration
        # The new group ID in the binding relationship.
        self.group_id = group_id
        # Optional. The Industrial Internet identification code, which has a one-to-one mapping with the OrderId. The code supports characters such as periods (.) and forward slashes (/) to separate code domains. The code must not contain non-printable characters, such as spaces and line breaks. This field is required when the business user generates the Industrial Internet identification code.
        self.industrial_id = industrial_id
        # Specifies whether to enable the ASR feature. Valid values:
        # - false: Disables the feature. This is the default value.
        # - true: Enables the feature.
        self.need_asr = need_asr
        # The new media selection in the binding relationship.
        self.need_record = need_record
        # The operation type. Valid values:
        # - updateNoA: Updates Number A.
        # - updateNoB: Updates Number B.
        # - updateExpire: Updates the validity period of the binding relationship.
        # - updateGroup: Updates the Number G group.
        # - updateNoDefaultA: Updates the default callback Number A in GXB mode.
        # - updateCallRestrict: Sets the single-call restriction.
        # - updateOutId: Updates the OutId field.
        # - updateIsRecordingEnabled: Updates the recording status in the binding.
        # - updateAsr: Updates the ASR status in the binding.
        # - updateAudio: Updates the ringtone configuration in the binding.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # The order ID. This parameter is required in practice. Encrypt the order ID for reporting to the regulatory platform.
        self.order_id = order_id
        # The external business extension field. This parameter is returned in the call record receipt message.
        self.out_id = out_id
        self.owner_id = owner_id
        # The key of the number pool.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the binding relationship, which uniquely identifies the number binding relationship.
        # 
        # This parameter is required.
        self.subs_id = subs_id
        # The new Number A in the binding relationship.
        self.tel_a = tel_a
        # The new Number B in the binding relationship.
        self.tel_b = tel_b
        # The intermediate Number X. If the business user does not specify Number X, the application platform assigns a number from the number pool as Number X.
        # 
        # This parameter is required.
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

        if self.default_a is not None:
            result['DefaultA'] = self.default_a

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

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.subs_id is not None:
            result['SubsId'] = self.subs_id

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

        if m.get('DefaultA') is not None:
            self.default_a = m.get('DefaultA')

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

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')

        if m.get('TelA') is not None:
            self.tel_a = m.get('TelA')

        if m.get('TelB') is not None:
            self.tel_b = m.get('TelB')

        if m.get('TelX') is not None:
            self.tel_x = m.get('TelX')

        return self

