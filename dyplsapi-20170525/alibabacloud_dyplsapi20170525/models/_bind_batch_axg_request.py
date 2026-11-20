# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class BindBatchAxgRequest(DaraModel):
    def __init__(
        self,
        axg_bind_list: List[main_models.BindBatchAxgRequestAxgBindList] = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The list of AXG bindings.
        # 
        # This parameter is required.
        self.axg_bind_list = axg_bind_list
        self.owner_id = owner_id
        # The key of the number pool.
        # 
        # You can log on to the Phone Number Protection console and obtain the key on the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool) page.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.axg_bind_list:
            for v1 in self.axg_bind_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AxgBindList'] = []
        if self.axg_bind_list is not None:
            for k1 in self.axg_bind_list:
                result['AxgBindList'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.axg_bind_list = []
        if m.get('AxgBindList') is not None:
            for k1 in m.get('AxgBindList'):
                temp_model = main_models.BindBatchAxgRequestAxgBindList()
                self.axg_bind_list.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class BindBatchAxgRequestAxgBindList(DaraModel):
    def __init__(
        self,
        asrmodel_id: str = None,
        asrstatus: bool = None,
        call_display_type: int = None,
        call_restrict: str = None,
        expect_city: str = None,
        expiration: str = None,
        group_id: str = None,
        is_recording_enabled: bool = None,
        out_id: str = None,
        out_order_id: str = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        ring_config: str = None,
    ):
        # The ASR model ID. Valid values:
        # 
        # - The ID of the telephony model for Mandarin: 7ee372834d2f4cc7ac0d0ab2d0ae1aac
        # 
        # - The ID of the telephony model for Cantonese: 9b4afe3d224e4fa3bf963697113e2f77
        # 
        # - The ID of the telephony model for local accents: 3655a6cb94764145a1f9a38a3c3b3b4b
        self.asrmodel_id = asrmodel_id
        # The automatic speech recognition (ASR) status. Valid values:
        # 
        # - **false** (default): The ASR feature is disabled.
        # 
        # - **true**: The ASR feature is enabled.
        self.asrstatus = asrstatus
        # Resets the number display logic for the binding. Set the value to **1**. This indicates that the intermediate number (Number X) is displayed to both the calling and called parties.
        # 
        # > Due to carrier regulations, the feature of displaying real numbers is not supported.
        self.call_display_type = call_display_type
        # The one-way call restriction. Valid values:
        # 
        # - **CONTROL_AX_DISABLE**: Number A cannot call Number X.
        # 
        # - **CONTROL_BX_DISABLE**: Number B cannot call Number X.
        self.call_restrict = call_restrict
        # The city to which Number X belongs.
        # 
        # > - If no numbers are available in the specified city, or if this parameter is not specified, a number from another city in the current number pool is randomly selected and used as Number X.
        # >
        # > - If **Number X Assignment Mode** is set to **Strict Match Mode** and no eligible number is found, an allocation error is reported.
        self.expect_city = expect_city
        # The expiration time of the binding. The value is accurate to seconds.
        # 
        # > - The expiration time must be more than 1 minute later than the current time.
        # >
        # > - This parameter is required.
        self.expiration = expiration
        # The group ID (GID) in the AXG binding.
        # 
        # You can view the GID in the following ways:
        # 
        # - Log on to the Phone Number Protection console. On the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool) page, select **AXG Privacy Number** and click **G Number Group Management** to view the GIDs of all G number groups.
        # 
        # - If you use the [CreateAxgGroup](https://help.aliyun.com/document_detail/110250.html) operation to create a G number group, the value of the **GroupId** parameter in the response is the GID.
        # 
        # > The G number group must contain at least one phone number.
        # 
        # This parameter is required.
        self.group_id = group_id
        # Specifies whether to record all calls made in the binding. Valid values:
        # 
        # - **true**: Call recording is enabled.
        # 
        # - **false** (default): Call recording is disabled.
        self.is_recording_enabled = is_recording_enabled
        # The extension field. This parameter is carried in call record messages.
        self.out_id = out_id
        # The external business ID.
        self.out_order_id = out_order_id
        # Number A in the AXG binding. Number A can be a mobile phone number or a landline number. If you use a landline number, add the area code, and do not add a hyphen between the area code and the landline number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # Number B in the AXG binding.
        # 
        # Number B can be a mobile phone number or a landline number. If you use a landline number, add the area code, and do not add a hyphen between the area code and the landline number.
        # 
        # > - When Number A calls Number X, the call is transferred to Number B by default. If Number B is not specified, the call fails.
        # >
        # > - When Number A calls Number X, if **A Callback Mode** is set to **Default Mode**, the call is transferred to Number B. Otherwise, the call fails.
        # >
        # > - To modify **A Callback Mode**, on the [Number Pool Management](https://dyplsnext.console.aliyun.com/number-pool?resType=1) page, select **AXG Privacy Number** and choose **Pool Management** > **A Callback Mode** > **Adjust Configuration**.
        # >
        # > - To update Number B, call the [UpdateSubscription](https://help.aliyun.com/zh/pnp/developer-reference/api-dyplsapi-2017-05-25-updatesubscription?spm=a2c4g.11186623.0.i16) operation.
        self.phone_no_b = phone_no_b
        # Number X in the AXG binding.
        # 
        # Number X must be a [purchased privacy number](https://dyplsnext.console.aliyun.com/numberbuy?spm=a2c4g.11186623.0.0.7e6449bbtiHP8m). You can log on to the Phone Number Protection console, go to the [Number Management](https://dyplsnext.console.aliyun.com/number/list) page, and then select **AXG Privacy Number** to obtain Number X.
        # 
        # > If you do not specify Number X, a random number is selected from the number pool based on the **ExpectCity** parameter and used as Number X.
        self.phone_no_x = phone_no_x
        # The corporate ringback tone (CRBT) that is played when Number X in an AXG binding is called.
        # 
        # You must specify the **ringtone field** and the **CRBT code**.
        # 
        # Valid values for the **ringtone field**:
        # 
        # - `AXGRing_AB`: the ringtone for calls from Number A to Number X (with a callback number).
        # 
        # - `AXGRing_A`: the ringtone for calls from Number A to Number X (without a callback number).
        # 
        # - `AXGRing_G`: the ringtone for calls from a number in Group G to Number X.
        # 
        # **CRBT code**:
        # 
        # You can log on to the Phone Number Protection console and obtain the CRBT code on the [Corporate CRBT Management](https://dyplsnext.console.aliyun.com/number-pool/ringtone?resType=1) page.
        # 
        # **Example**:
        # 
        # To set the ringtone for calls from Number A to Number X (without a callback number), specify `"AXGRing_A": "1000****1"`.
        # 
        # > The CRBT that is set at the binding level takes precedence over the CRBT that is set at the number pool level.
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id

        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a

        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b

        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x

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

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')

        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')

        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')

        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')

        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')

        return self

