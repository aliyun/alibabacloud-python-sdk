# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAxbRequest(DaraModel):
    def __init__(
        self,
        asrmodel_id: str = None,
        asrstatus: bool = None,
        call_display_type: int = None,
        call_restrict: str = None,
        call_timeout: int = None,
        dtmf_config: str = None,
        expect_city: str = None,
        expiration: str = None,
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
        # The ID of the ASR model. On the [Automatic Speech Recognition (ASR) Model Management](https://dyplsnext.console.aliyun.com/?spm=5176.12818093.categories-n-products.ddypls.22e616d0a0tEFC#/asr) page, you can view the ID of the ASR model.
        self.asrmodel_id = asrmodel_id
        # Specifies whether to enable automatic speech recognition (ASR). Valid values:
        # 
        # *   **false** (default): disables ASR.
        # *   **true**: enables ASR.
        self.asrstatus = asrstatus
        # Re-sets the phone number display logic in the AXB binding. Fixed value: **1**, indicating that phone number X is displayed on both the calling phone and the called phone.
        # 
        # >  Due to the regulatory restrictions imposed by carriers, the setting to display real phone numbers during calls does not take effect.
        self.call_display_type = call_display_type
        # The status of the one-way call restriction. Valid values:
        # 
        # *   **CONTROL_AX_DISABLE**: Phone number A cannot be used to call phone number X.
        # *   **CONTROL_BX_DISABLE**: Phone number B cannot be used to call phone number X.
        self.call_restrict = call_restrict
        # The maximum ringing duration for each number in sequential ringing. Unit: seconds. The value ranges from 5 to 20.
        self.call_timeout = call_timeout
        # Specifies the dual tone multiple frequency (DTMF) key configuration in the AXB binding. The following content can be configured:
        # 
        # *   endCallIvrPhoneNo: for whom the audio is played, user A or user B.
        # *   waitingDtmfTime: the maximum waiting time after the first audio is played. The maximum waiting time is 30 seconds.
        # *   maxLoop: the maximum number of loop playback times of the first audio if the DTMF key is not matched. The maximum number of loop playback times is 5.
        # *   step1File: the name of the first audio.
        # *   step2File: the name of the second audio.
        # *   validKey: the valid key values, such as 1,2. Only two valid key values can be set, and the key values are separated by a comma (,).
        # *   waitingEndCall: The waiting duration to hang up a call. The waiting duration is allowed by a carrier. The maximum waiting duration is 10 seconds.
        self.dtmf_config = dtmf_config
        # Specifies the city to which phone number X to be selected belongs.
        # 
        # *   If no phone number for the specified city is available in the current phone number pool or this parameter is not specified, a phone number that belongs to another city is randomly selected from the current phone number pool and assigned as phone number X.
        # *   If**Number X Assignment Mode** is set to **Strict Matching Mode** and no phone number meets the requirement, the system displays an allocation error.
        self.expect_city = expect_city
        # The expiration time of the AXB binding.
        # 
        # >  The expiration time must be more than 1 minute later than the time when you call this API operation.
        # 
        # This parameter is required.
        self.expiration = expiration
        # Specifies whether to record all calls made by the bound phone numbers. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.is_recording_enabled = is_recording_enabled
        # The extension field for the external business. This parameter is returned in a call record receipt.
        self.out_id = out_id
        # The ID of the external business.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # Phone number A in the AXB binding.
        # 
        # Phone number A can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # Phone number B in the AXB binding. If phone number A is used to call phone number X, the call is forwarded to phone number B. Phone number B can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        # 
        # >  If you need to update phone number B, call the [UpdateSubscription](https://help.aliyun.com/document_detail/110253.html) operation.
        self.phone_no_b = phone_no_b
        # Phone number X in the AXB binding.
        # 
        # Phone number X is the phone number that you purchased in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) or by using the [BuySecretNo](https://help.aliyun.com/document_detail/110266.html) operation before you bind a phone number. Phone number X is used to forward calls.
        # 
        # If you do not specify this parameter, a random phone number is selected from the phone number pool based on the value of the ExpectCity parameter and is used as phone number X.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sets the ringtone code for enterprise Color Ring Back Tone (CRBT) in the AXB binding.
        # 
        # *   Ringtone setting when phone number A is used to call phone number X in the AXB binding: AXBRing_A
        # *   Ringtone setting when phone number B is used to call phone number X in the AXB binding: AXBRing_B
        # 
        # Enterprise CRBT codes: Enterprise CRBT codes can be queried in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). You can choose **Number Pool Management** > **Enterprise CRBT Management** to view enterprise CRBT codes. You can also upload, delete, or perform other operations on enterprise CRBT codes.
        # 
        # >  The bound enterprise CRBTs are preferentially used. If no enterprise CRBT is set or the setting does not take effect, the enterprise CRBTs at the phone number pool level are used.
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

        if self.dtmf_config is not None:
            result['DtmfConfig'] = self.dtmf_config

        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city

        if self.expiration is not None:
            result['Expiration'] = self.expiration

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

        if m.get('CallTimeout') is not None:
            self.call_timeout = m.get('CallTimeout')

        if m.get('DtmfConfig') is not None:
            self.dtmf_config = m.get('DtmfConfig')

        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

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

