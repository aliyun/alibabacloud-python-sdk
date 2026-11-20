# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSubscriptionRequest(DaraModel):
    def __init__(
        self,
        asrmodel_id: str = None,
        asrstatus: bool = None,
        call_display_type: int = None,
        call_restrict: str = None,
        expiration: str = None,
        group_id: str = None,
        is_recording_enabled: bool = None,
        operate_type: str = None,
        out_id: str = None,
        owner_id: int = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        pool_key: str = None,
        product_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ring_config: str = None,
        subs_id: str = None,
    ):
        # The ID of the ASR model.
        self.asrmodel_id = asrmodel_id
        # Specifies whether to enable automatic speech recognition (ASR). Valid values:
        # 
        # *   **false** (default): disables ASR.
        # *   **true**: enables ASR.
        self.asrstatus = asrstatus
        # Re-sets the phone number display logic in the phone number binding. Fixed value: **1**, indicating that phone number X is displayed on both the calling phone and the called phone.
        # 
        # >  Due to the regulatory restrictions imposed by carriers, the setting to display real phone numbers during calls does not take effect.
        self.call_display_type = call_display_type
        # One-way call restrictions. Valid values:
        # 
        # *   **CONTROL_AX_DISABLE**: Phone number A cannot be used to call phone number X.
        # *   **CONTROL_BX_DISABLE**: Phone number B cannot be used to call phone number X.
        # *   **CONTROL_CLEAR_DISABLE**: The call restrictions are cleared.
        # 
        # >  This parameter is required when **OperateType** is set to **updateCallRestrict**.
        self.call_restrict = call_restrict
        # Re-sets the expiration time of the phone number binding.
        # 
        # > 
        # 
        # *   This parameter is required when **OperateType** is set to **updateExpire**.
        # 
        # *   The expiration time must be more than 1 minute later than the time when you call this API operation.
        self.expiration = expiration
        # The ID of number group G in the phone number binding.
        # 
        # >  This parameter is required when **OperateType** is set to **updateAxgGroup**.
        self.group_id = group_id
        # Re-sets the recording status in the phone number binding.
        # 
        # >  This parameter does not have a default value. If you do not specify this parameter, the value of the corresponding field is not updated.
        self.is_recording_enabled = is_recording_enabled
        # The operation to modify the phone number binding. Valid values:
        # 
        # *   **updateNoA**: modifies phone number A.
        # *   **updateNoB**: modifies phone number B.
        # *   **updateExpire**: modifies the validity period of the binding.
        # *   **updateAxgGroup**: modifies number group G.
        # *   **updateCallRestrict**: modifies one-way call restrictions.
        # *   **updateCallDisplayType**: updates the number display logic for calls.
        # *   **updateOutId**: updates the value of the OutId parameter.
        # *   **updateIsRecordingEnabled**: updates the status of the recording feature in the binding.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        # Re-sets the value of the OutId parameter in the phone number binding.
        self.out_id = out_id
        self.owner_id = owner_id
        # Phone number A in the phone number binding.
        # 
        # >  This parameter is required when **OperateType** is set to **updateNoA**.
        self.phone_no_a = phone_no_a
        # Phone number B in the phone number binding.
        # 
        # >  This parameter is required when **OperateType** is set to **updateNoB**.
        self.phone_no_b = phone_no_b
        # Phone number X in the phone number binding.
        # 
        # This parameter is required.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # >  This parameter is required when **ProductType** is left empty.
        self.pool_key = pool_key
        # The product type. Valid values:
        # 
        # *   **AXB_170**
        # *   **AXN_170**
        # *   **AXN_95**
        # *   **AXN_EXTENSION_REUSE**
        # 
        # > 
        # 
        # *   This parameter is applicable to the original key accounts of Alibaba Cloud. This parameter can be ignored for Alibaba Cloud users.
        # 
        # *   This parameter is required when **PoolKey** is left empty.
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Updates the ringtone code for enterprise Color Ring Back Tone (CRBT) in the phone number binding.
        # 
        # AXB product:
        # 
        # *   Ringtone setting when phone number A is used to call phone number X in the AXB binding: AXBRing_A
        # *   Ringtone setting when phone number B is used to call phone number X in the AXB binding: AXBRing_B
        # 
        # AXN product:
        # 
        # *   Ringtone setting (with a callback number) when phone number A is used to call phone number X in the AXN extension binding: AXNRing_AB
        # *   Ringtone setting (without a callback number) when phone number A is used to call phone number X in the AXN extension binding: AXNRing_A
        # *   Ringtone setting when phone number N is used to call phone number X in the AXN extension binding: AXNRing_N
        # 
        # AXG product:
        # 
        # *   Ringtone setting (with a callback number) when phone number A is used to call phone number X in the AXG binding: AXGRing_AB
        # *   Ringtone setting (without a callback number) when phone number A is used to call phone number X in the AXG binding: AXGRing_A
        # *   Ringtone setting when a phone number in number group G is used to call phone number X in the AXG binding: AXGRing_G
        # 
        # Enterprise CRBT codes: Enterprise CRBT codes can be queried in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). You can choose **Number Pool Management** > **Enterprise CRBT Management** to view and manage enterprise CRBT codes. You can also upload, delete, or perform other operations on enterprise CRBT codes.
        # 
        # >  The bound enterprise CRBTs are preferentially used. If no enterprise CRBT is set or the setting does not take effect, the enterprise CRBTs at the phone number pool level are used.
        self.ring_config = ring_config
        # The binding ID.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account), choose **Number and Number Pool** > **Number Management**. On the Number Management page, select the desired record and click Details to view the binding ID. Alternatively, you can view the value of the **SubsId** parameter returned by an API operation for a phone number binding such as BindAxb. The value of this parameter indicates a binding ID.
        # 
        # This parameter is required.
        self.subs_id = subs_id

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

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.out_id is not None:
            result['OutId'] = self.out_id

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

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config

        if self.subs_id is not None:
            result['SubsId'] = self.subs_id

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

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

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

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')

        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')

        return self

