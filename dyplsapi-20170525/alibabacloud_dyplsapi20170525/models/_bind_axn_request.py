# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAxnRequest(DaraModel):
    def __init__(
        self,
        asrmodel_id: str = None,
        asrstatus: bool = None,
        call_display_type: int = None,
        call_restrict: str = None,
        call_timeout: int = None,
        expect_city: str = None,
        expiration: str = None,
        extend: str = None,
        is_recording_enabled: bool = None,
        no_type: str = None,
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
        # - 7ee372834d2f4cc7ac0d0ab2d0ae1aac: General-Telephone-Mandarin Chinese model.
        # 
        # - 9b4afe3d224e4fa3bf963697113e2f77: General-Telephone-Cantonese model.
        # 
        # - 3655a6cb94764145a1f9a38a3c3b3b4b: General-Telephone-Regional accent model.
        self.asrmodel_id = asrmodel_id
        # The ASR status. Valid values:
        # 
        # - **false**: Disabled. This is the default value.
        # - **true**: Enabled.
        self.asrstatus = asrstatus
        # Resets the number display logic in the binding relationship. Set the value to **1**, which indicates that the intermediate Number X is displayed for both the caller and the callee.
        # 
        # > Due to carrier regulatory restrictions, the setting to display the real number during a call does not take effect.
        self.call_display_type = call_display_type
        # The single-call restriction status. Valid values:
        # 
        # - **CONTROL_AX_DISABLE**: Number A cannot call Number X.
        # - **CONTROL_BX_DISABLE**: Number B cannot call Number X.
        self.call_restrict = call_restrict
        # The ring duration. Unit: seconds.
        self.call_timeout = call_timeout
        # The city specified for selecting Number X.
        # 
        # > - If no available numbers in the specified city exist in the current number pool, or if this parameter is not specified, a number from another city is randomly assigned from the current number pool as Number X.
        # > - If the **Number X allocation mode** is set to **strict match mode**, the system returns an allocation error when no eligible numbers are available.
        self.expect_city = expect_city
        # The expiration time of the binding relationship. Unit: seconds.
        # 
        # > The expiration time must be at least 60 seconds later than the current time.
        # 
        # This parameter is required.
        self.expiration = expiration
        self.extend = extend
        # Specifies whether to record all calls generated for this binding relationship. Valid values:
        # 
        # - **true**: Records calls.
        # - **false**: Does not record calls. This is the default value.
        self.is_recording_enabled = is_recording_enabled
        # The number type.
        # 
        # > This parameter applies to former Alibaba Dayu customers. Alibaba Cloud users can ignore this parameter.
        self.no_type = no_type
        # The external business extension field. This parameter is returned in the call record receipt message.
        self.out_id = out_id
        # The external business ID.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # Number A of the AXN privacy number. Number A can be a mobile phone number or a landline number. If it is a landline number, the area code must be included, and no hyphen is required between the area code and the phone number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # Number B of the AXN privacy number.
        # 
        # Number B can be a mobile phone number or a landline number. If it is a landline number, the area code must be included, and no hyphen is required between the area code and the phone number.
        # > - When Number A dials Number X, the call is forwarded to Number B by default. If Number B is not set, the call cannot be connected.
        # > - When Number A dials Number X, the call is forwarded to Number B only when the **callback mode for Number A** is set to **default mode**. Otherwise, the call cannot be connected.
        # > - To modify the **callback mode for Number A**, go to [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool?resType=1) > filter **AXN privacy number** > **Number Pool Management** > **Callback mode for Number A** > **Adjust Configuration**.
        # > - To update Number B, call the [UpdateSubscription](https://www.alibabacloud.com/help/en/pnp/developer-reference/api-dyplsapi-2017-05-25-updatesubscription) operation.
        self.phone_no_b = phone_no_b
        # Number X of the AXN privacy number.
        # 
        # Number X is a privacy number that you have [purchased](https://dyplsnext.console.aliyun.com/numberbuy?spm=a2c4g.11186623.0.0.7e6449bbtiHP8m) in the console.
        # 
        # > If Number X is not specified, a number is randomly selected from the specified number pool based on the ExpectCity parameter as Number X.
        self.phone_no_x = phone_no_x
        # The key of the number pool. You can obtain the **number pool key** on the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool?spm=a2c4g.11186623.0.0.7e6449bbtiHP8m) page in the Privacy Protection console.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sets the corporate color ringback tone (CRBT) played during a dial-up to Number X after the AXN privacy number is attached.
        # 
        # Specify the **ringtone field** and **CRBT encoding** for this parameter.
        # 
        # **Ringtone field** valid values:
        # - AXNRing_AB: The ringtone Settings before Number A dials Number X and the call is connected (with a callback number) in AXN mode.
        # - AXNRing_A: The ringtone Settings before Number A dials Number X and the call is connected (without a callback number) in AXN mode.
        # - AXNRing_N: The ringtone Settings before Number N dials Number X and the call is connected in AXN mode.
        # - AXNRing_A_PICKUP: The ringtone Settings after Number A dials Number X and the call is connected in AXN mode.
        # - AXNRing_N_PICKUP: The ringtone Settings after Number N dials Number X and the call is connected in AXN mode.
        # 
        # **CRBT encoding**:
        # 
        # You can obtain the corporate CRBT encoding on the [Corporate CRBT Management](https://dyplsnext.console.aliyun.com/number-pool/ringtone?resType=1) page in the Privacy Protection console.
        # 
        # **Example**:
        # 
        # To set the ringtone played before Number A dials Number X and the call is connected (without a callback number), enter "AXNRing_A": "1000****1".
        # 
        # > The corporate CRBT configured at the attachment level takes precedence. If it is not set or does not take effect, the CRBT configured at the number pool level is used.
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

        if self.call_timeout is not None:
            result['CallTimeout'] = self.call_timeout

        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled

        if self.no_type is not None:
            result['NoType'] = self.no_type

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

        if m.get('CallTimeout') is not None:
            self.call_timeout = m.get('CallTimeout')

        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')

        if m.get('NoType') is not None:
            self.no_type = m.get('NoType')

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

