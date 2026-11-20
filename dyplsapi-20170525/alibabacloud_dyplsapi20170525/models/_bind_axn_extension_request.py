# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAxnExtensionRequest(DaraModel):
    def __init__(
        self,
        asrmodel_id: str = None,
        asrstatus: bool = None,
        call_display_type: int = None,
        call_restrict: str = None,
        expect_city: str = None,
        expiration: str = None,
        extend: str = None,
        extension: str = None,
        is_recording_enabled: bool = None,
        out_id: str = None,
        out_order_id: str = None,
        owner_id: int = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ring_config: str = None,
    ):
        # The ASR model ID. Valid values:
        # 
        # - General-Telephone-Mandarin Chinese model ID: 7ee372834d2f4cc7ac0d0ab2d0ae1aac
        # 
        # - General-Telephone-Cantonese model ID: 9b4afe3d224e4fa3bf963697113e2f77
        # 
        # - General-Telephone-Regional accent model ID: 3655a6cb94764145a1f9a38a3c3b3b4b
        self.asrmodel_id = asrmodel_id
        # The ASR status. Valid values:
        # 
        # - **false**: Disabled. This is the default value.
        # - **true**: Enabled.
        self.asrstatus = asrstatus
        # Resets the number display logic in the binding relationship. Set the value to **1**, which indicates that the intermediate number X is displayed for both the caller and the callee.
        # 
        # > Due to carrier regulatory restrictions, the setting to display the real number during a call does not take effect.
        self.call_display_type = call_display_type
        # The call restriction status. Valid values:
        # 
        # - **CONTROL_AX_DISABLE**: Number A cannot call number X.
        # - **CONTROL_BX_DISABLE**: Number B cannot call number X.
        self.call_restrict = call_restrict
        # The city where you want to select number X.
        # 
        # > - If no available numbers exist in the specified city in the current number pool, or if this parameter is not specified, the system randomly assigns a number from another city in the current number pool as number X.
        # > - If the **number X allocation mode** is set to **strict match mode**, the system returns an allocation error when no eligible numbers are available.
        self.expect_city = expect_city
        # The expiration time of the binding relationship. The time is accurate to seconds.
        # > The expiration time must be at least 1 minute later than the current time.
        # 
        # This parameter is required.
        self.expiration = expiration
        self.extend = extend
        # The extension number of number X. The extension number must be 1 to 3 digits in length.
        # 
        # > If you specify an extension number, you must also specify number X. This means that both the Extension and PhoneNoX parameters must be specified.
        self.extension = extension
        # Specifies whether to record all calls generated for this binding relationship. Valid values:
        # 
        # - **true**: Records calls.
        # - **false**: Does not record calls. This is the default value.
        self.is_recording_enabled = is_recording_enabled
        # The external business extension field. This parameter is returned in the call record receipt message.
        self.out_id = out_id
        # The external business ID.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # The number A of the AXN extension number.
        # Number A can be a mobile phone number or a landline number. For a landline number, you must add the area code. Do not add a hyphen between the area code and the phone number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # The number B of the AXN extension number.
        # 
        # Number B can be a mobile phone number or a landline number. For a landline number, you must add the area code. Do not add a hyphen between the area code and the phone number.
        # > - When number A calls number X, the call is forwarded to number B by default. If number B is not specified, the call cannot be connected.
        # > - When number A calls number X, the call is forwarded to number B only when the **callback mode for number A** is set to **default mode**. If it is not set to **default mode**, the call cannot be connected.
        # > - To modify the **callback mode for number A**, go to [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool?resType=1) > filter by **AXN Extension Number** > **Number Pool Management** > **Callback Mode for Number A** > **Adjust Configuration**.
        # > - To update number B, call the [UpdateSubscription](https://www.alibabacloud.com/help/en/pnp/developer-reference/api-dyplsapi-2017-05-25-updatesubscription) operation.
        self.phone_no_b = phone_no_b
        # The number X of the AXN extension number.
        # 
        # Number X is a privacy number that you have [purchased](https://dyplsnext.console.aliyun.com/numberbuy?spm=a2c4g.11186623.0.0.7e6449bbtiHP8m) in the console.
        # 
        # > If you do not specify number X, the system randomly assigns a number from the specified number pool as number X based on the ExpectCity parameter.
        self.phone_no_x = phone_no_x
        # The key of the number pool.
        # 
        # You can obtain the **number pool key** on the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool?spm=a2c4g.11186623.0.0.7e6449bbtiHP8m) page in the Privacy Protection console.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Set the corporate ringback tone for dial-up to number X after the AXN extension number is bound.
        # 
        # Specify the **ringtone field** and **ringback tone encoding** for this parameter.
        # 
        # Valid values for the **ringtone field**:
        # - AXNRing_AB: The ringtone settings before number A calls number X and the call is connected (with a callback number) in the AXN extension number scenario.
        # - AXNRing_A: The ringtone settings before number A calls number X and the call is connected (without a callback number) in the AXN extension number scenario.
        # - AXNRing_N: The ringtone settings before the number on side N calls number X and the call is connected in the AXN extension number scenario.
        # - AXNRing_A_PICKUP: The ringtone settings after number A calls number X and the call is connected in the AXN extension number scenario.
        # - AXNRing_N_PICKUP: The ringtone settings after the number on side N calls number X and the call is connected in the AXN extension number scenario.
        # 
        # **Ringback tone encoding**:
        # 
        # You can obtain the corporate ringback tone encoding on the [Corporate Ringback Tone Management](https://dyplsnext.console.aliyun.com/number-pool/ringtone?resType=1) page in the Privacy Protection console.
        # 
        # **Example**:
        # 
        # To set the ringtone before number A calls number X and the call is connected (without a callback number), enter "AXNRing_A": "1000****1".
        self.ring_config = ring_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id

        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus

        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type

        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict

        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a

        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b

        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')

        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')

        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')

        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')

        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')

        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')

        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')

        return self

