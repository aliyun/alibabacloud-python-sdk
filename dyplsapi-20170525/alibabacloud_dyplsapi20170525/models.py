# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddAxnTrackNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_no_x: str = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subs_id: str = None,
        track_no: str = None,
    ):
        self.owner_id = owner_id
        # The private number in the AXN binding, that is, phone number X.
        # 
        # You can call the [BindAxn](https://help.aliyun.com/document_detail/110258.html) operation to obtain the value of PhoneNoX.
        # 
        # This parameter is required.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The binding ID.
        # 
        # You can call the [BindAxn](https://help.aliyun.com/document_detail/110258.html) operation to obtain the value of SubsId.
        # 
        # This parameter is required.
        self.subs_id = subs_id
        # The tracking number.
        # 
        # This parameter is required.
        self.track_no = track_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.track_no is not None:
            result['trackNo'] = self.track_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('trackNo') is not None:
            self.track_no = m.get('trackNo')
        return self


class AddAxnTrackNoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddAxnTrackNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddAxnTrackNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddAxnTrackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSecretBlacklistRequest(TeaModel):
    def __init__(
        self,
        black_no: str = None,
        black_type: str = None,
        pool_key: str = None,
        remark: str = None,
        way_control: str = None,
    ):
        # The numbers in the blacklist. A point-to-point blacklist has a pair of numbers separated by a colon (:). A number pool blacklist has only one single number.
        # 
        # >  The asterisks (\\*) in the sample value are not wildcards.
        # 
        # This parameter is required.
        self.black_no = black_no
        # The blacklist type. Valid values:
        # 
        # *   **POINT_TO_POINT_BLACK**: point-to-point blacklist.
        # *   **PARTNER_GLOBAL_NUMBER_BLACK**: number pool blacklist.
        # 
        # This parameter is required.
        self.black_type = black_type
        # The key of the phone number pool.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the Number Pool Management page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        # The blacklist remarks.
        self.remark = remark
        # The control on the call direction.
        # 
        # *   **PHONEA_REJECT**: The first number in the blacklist can be used to call the second number, but the second number cannot be used to call the first number.
        # *   **PHONEB_REJECT**: The first number in the blacklist cannot be used to call the second number, but the second number can be used to call the first number.
        # *   If this parameter is left empty, the two numbers in the blacklist cannot be used to call each other.
        # 
        # >  This parameter is available only for a point-to-point blacklist.
        # 
        # Valid values:
        # 
        # *   DUPLEX_REJECT
        # *   PHONEA_REJECT
        # *   PHONEB_REJECT
        self.way_control = way_control

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.way_control is not None:
            result['WayControl'] = self.way_control
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('WayControl') is not None:
            self.way_control = m.get('WayControl')
        return self


class AddSecretBlacklistResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddSecretBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSecretBlacklistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddSecretBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxbRequest(TeaModel):
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
        # *   **true**\
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class BindAxbResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        secret_no: str = None,
        subs_id: str = None,
    ):
        # The extension of the phone number.
        # 
        # >  The BindAxb operation does not involve an extension. Ignore this parameter.
        self.extension = extension
        # The private number, that is, phone number X.
        self.secret_no = secret_no
        # The binding ID.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxbResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_bind_dto: BindAxbResponseBodySecretBindDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the phone numbers were bound.
        self.secret_bind_dto = secret_bind_dto

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxbResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAxbResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindAxbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxgRequest(TeaModel):
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
        owner_id: int = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        ring_config: str = None,
    ):
        # The ID of the ASR model.
        self.asrmodel_id = asrmodel_id
        # Specifies whether to enable automatic speech recognition (ASR). Valid values:
        # 
        # *   **False** (default): disables ASR.
        # *   **True**: enables ASR.
        self.asrstatus = asrstatus
        # Re-sets the phone number display logic in the AXG binding. Fixed value: **1**, indicating that phone number X is displayed on both the calling phone and the called phone.
        # 
        # >  Due to the regulatory restrictions imposed by carriers, the setting to display real phone numbers during calls does not take effect.
        self.call_display_type = call_display_type
        # The status of call restrictions. Valid values:
        # 
        # *   **CONTROL_AX_DISABLE**: Phone number A cannot be used to call phone number X.
        # *   **CONTROL_BX_DISABLE**: Phone number B cannot be used to call phone number X.
        self.call_restrict = call_restrict
        # Specifies the city to which phone number X to be selected belongs.
        # 
        # *   If no phone number for the specified city is available in the current phone number pool or this parameter is not specified, a phone number that belongs to another city is randomly selected from the current phone number pool and assigned as phone number X.
        # *   If Number X Assignment Mode is set to Strict Matching Mode and no phone number meets the requirement, the system displays an allocation error.
        self.expect_city = expect_city
        # The expiration time of the AXG binding. The value is accurate to seconds.
        # 
        # >  The expiration time must be more than 1 minute later than the time when you call this API operation.
        # 
        # This parameter is required.
        self.expiration = expiration
        # The group ID in the AXG binding. You can view the group ID by using either of the following methods:
        # 
        # *   On the **Number Pool Management** page in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account), filter AXG privacy numbers and click **Number Group G Management** to view the group IDs of number groups G.****\
        # *   If the [CreateAxgGroup](https://help.aliyun.com/document_detail/110250.html) operation is called to create number group G, the value of **GroupId** in the response of the CreateAxgGroup operation is specified as the value of the request parameter **GroupId** of the BindAxg operation.
        # 
        # >  Number group G must have one or more phone numbers.
        # 
        # This parameter is required.
        self.group_id = group_id
        # Specifies whether to record all calls made by the bound phone numbers.
        self.is_recording_enabled = is_recording_enabled
        # The extension field for the external business. This parameter is returned in a call record receipt.
        self.out_id = out_id
        # The ID of the external business.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # Phone number A in the AXG binding. Phone number A can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # Phone number B in the AXG binding. If phone number A is used to call phone number X, the call is forwarded to phone number B. If you need to update phone number B, call the [UpdateSubscription](https://help.aliyun.com/document_detail/110253.html) operation.
        # 
        # Phone number B can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        self.phone_no_b = phone_no_b
        # Phone number X in the AXG binding. If you do not specify this parameter, a random phone number is selected from the phone number pool based on the value of the **ExpectCity** parameter and is used as phone number X.
        # 
        # >  Phone number X is the phone number that you purchased in the Phone Number Protection console or by using the [BuySecretNo](https://help.aliyun.com/document_detail/110266.html) operation before you bind a phone number. Phone number X is used to forward calls.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sets the ringtone for enterprise Color Ring Back Tone (CRBT) in the AXG binding.
        # 
        # *   Ringtone setting (with a callback number) when phone number A is used to call phone number X in the AXG binding: AXGRing_AB
        # *   Ringtone setting (without a callback number) when phone number A is used to call phone number X in the AXG binding: AXGRing_A
        # *   Ringtone setting when a phone number in number group G is used to call phone number X in the AXG binding: AXGRing_G
        # *   Enterprise CRBT codes: Enterprise CRBT codes can be queried in the Phone Number Protection console. You can choose **Number Pool Management > Enterprise CRBT Management** to view and manage enterprise CRBT codes. You can also upload, delete, or perform other operations on enterprise CRBT codes.
        # 
        # >  The bound enterprise CRBTs are preferentially used. If no enterprise CRBT is set or the setting does not take effect, the enterprise CRBTs at the phone number pool level are used.
        self.ring_config = ring_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
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


class BindAxgResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        secret_no: str = None,
        subs_id: str = None,
    ):
        # The extension of the phone number.
        # 
        # >  The BindAxg operation does not involve an extension. Ignore this parameter.
        self.extension = extension
        # The private number, that is, phone number X.
        self.secret_no = secret_no
        # The binding ID.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxgResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_bind_dto: BindAxgResponseBodySecretBindDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the phone numbers were bound.
        self.secret_bind_dto = secret_bind_dto

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxgResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAxgResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindAxgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxnRequest(TeaModel):
    def __init__(
        self,
        asrmodel_id: str = None,
        asrstatus: bool = None,
        call_display_type: int = None,
        call_restrict: str = None,
        call_timeout: int = None,
        expect_city: str = None,
        expiration: str = None,
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
        # The ID of the ASR model. On the [Automatic Speech Recognition (ASR) Model Management](https://dyplsnext.console.aliyun.com/?spm=5176.12818093.categories-n-products.ddypls.22e616d0a0tEFC#/asr) page, you can view the ID of the ASR model.
        self.asrmodel_id = asrmodel_id
        # Specifies whether to enable automatic speech recognition (ASR). Valid values:
        # 
        # *   **false** (default): disables ASR.
        # *   **true**: enables ASR.
        self.asrstatus = asrstatus
        # Re-sets the phone number display logic in the AXN binding. Fixed value: **1**, indicating that phone number X is displayed on both the calling phone and the called phone.
        # 
        # >  Due to the regulatory restrictions imposed by carriers, the setting to display real phone numbers during calls does not take effect.
        self.call_display_type = call_display_type
        # The status of one-way call restrictions. Valid values:
        # 
        # *   **CONTROL_AX_DISABLE**: Phone number A cannot be used to call phone number X.
        # *   **CONTROL_BX_DISABLE**: Phone number B cannot be used to call phone number X.
        self.call_restrict = call_restrict
        # The maximum ringing duration for each number in sequential ringing. Unit: seconds.
        self.call_timeout = call_timeout
        # Specifies the city to which phone number X to be selected belongs.
        # 
        # *   If no phone number for the specified city is available in the current phone number pool or this parameter is not specified, a phone number that belongs to another city is randomly selected from the current phone number pool and assigned as phone number X.
        # *   If **Number X Assignment Mode** is set to **Strict Matching Mode** and no phone number meets the requirement, the system displays an allocation error.
        self.expect_city = expect_city
        # The expiration time of the AXN binding. Unit: seconds.
        # 
        # >  The expiration time must be more than 60 seconds later than the time when you call this API operation.
        # 
        # This parameter is required.
        self.expiration = expiration
        # Specifies whether to record all calls made by the bound phone numbers. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.is_recording_enabled = is_recording_enabled
        # The type of the phone number.
        # 
        # >  This parameter is applicable to the key accounts of Alibaba Cloud. This parameter can be ignored for Alibaba Cloud users.
        self.no_type = no_type
        # The extension field for the external business. This parameter is returned in a call record receipt.
        self.out_id = out_id
        # The ID of the external business.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # Phone number A in the AXN binding. Phone number A can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # Phone number B in the AXN binding. If phone number A is used to call phone number X, the call is forwarded to phone number B. Phone number B can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        # 
        # >  If phone number B is not specified in the AXN binding, the system automatically generates a nonexistent number. If phone number A is used to call phone number X, the nonexistent number is returned. If you need to update phone number B, call the [UpdateSubscription](https://help.aliyun.com/document_detail/110253.html) operation.
        self.phone_no_b = phone_no_b
        # Phone number X in the AXN binding. Phone number X is the phone number that you purchased in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) or by using the [BuySecretNo](https://help.aliyun.com/document_detail/110266.html) operation before you bind a phone number. Phone number X is used to forward calls.
        # 
        # >  If you do not specify this parameter, a random phone number is selected from the phone number pool based on the value of the ExpectCity parameter and is used as phone number X.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool. Log on to the [Phone Number Protection console ](https://dypls.console.aliyun.com/dypls.htm#/account)and view the key of the phone number pool on the **Number Pool Management** page.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sets the ringtone code for enterprise Color Ring Back Tone (CRBT) in the AXN extension binding.
        # 
        # *   Ringtone setting (with a callback number) when phone number A is used to call phone number X in the AXN extension binding: AXNRing_AB
        # *   Ringtone setting (without a callback number) when phone number A is used to call phone number X in the AXN extension binding: AXNRing_A
        # *   Ringtone setting when an N-side number is used to call phone number X in the AXN extension binding: AXNRing_N
        # 
        # Enterprise CRBT codes: Enterprise CRBT codes can be queried in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). You can choose **Number Pool Management > Enterprise CRBT Management** to view enterprise CRBT codes. You can also upload, delete, or perform other operations on enterprise CRBT codes.
        # 
        # >  The bound enterprise CRBTs are preferentially used. If no enterprise CRBT is set or the setting does not take effect, the enterprise CRBTs at the phone number pool level are used.
        self.ring_config = ring_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class BindAxnResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        secret_no: str = None,
        subs_id: str = None,
    ):
        # The extension of the phone number.
        # 
        # >  The BindAxn operation does not involve an extension. Ignore this parameter.
        self.extension = extension
        # The private number, that is, phone number X.
        self.secret_no = secret_no
        # The binding ID.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxnResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_bind_dto: BindAxnResponseBodySecretBindDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the phone numbers were bound.
        self.secret_bind_dto = secret_bind_dto

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxnResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAxnResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindAxnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxnExtensionRequest(TeaModel):
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
        # The ID of the ASR model. On the [Automatic Speech Recognition (ASR) Model Management](https://dyplsnext.console.aliyun.com/?spm=5176.12818093.categories-n-products.ddypls.22e616d0a0tEFC#/asr) page, you can view the ID of the ASR model.
        self.asrmodel_id = asrmodel_id
        # Specifies whether to enable automatic speech recognition (ASR). Valid values:
        # 
        # *   **false** (default): disables ASR.
        # *   **true**: enables ASR.
        self.asrstatus = asrstatus
        # Re-sets the phone number display logic in the AXN extension binding. Fixed value: **1**, indicating that phone number X is displayed on both the calling phone and the called phone.
        # 
        # >  Due to the regulatory restrictions imposed by carriers, the setting to display real phone numbers during calls does not take effect.
        self.call_display_type = call_display_type
        # The status of call restrictions. Valid values:
        # 
        # *   **CONTROL_AX_DISABLE**: Phone number A cannot be used to call phone number X.
        # *   **CONTROL_BX_DISABLE**: Phone number B cannot be used to call phone number X.
        self.call_restrict = call_restrict
        # Specifies the city to which phone number X to be selected belongs.
        # 
        # *   If no phone number for the specified city is available in the current phone number pool or this parameter is not specified, a phone number that belongs to another city is randomly selected from the current phone number pool and assigned as phone number X.
        # *   If Number X Assignment Mode is set to Strict Matching Mode and no phone number meets the requirement, the system displays an allocation error.
        self.expect_city = expect_city
        # The expiration time of the AXN extension binding. The value is accurate to seconds.
        # 
        # >  The expiration time must be more than 1 minute later than the time when you call this API operation.
        # 
        # This parameter is required.
        self.expiration = expiration
        self.extend = extend
        # The extension of phone number X. The extension is 1 to 3 digits in length.
        # 
        # >  If you specify Extension, you must also specify PhoneNoX.
        self.extension = extension
        # Specifies whether to record all calls made by the bound phone numbers. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.is_recording_enabled = is_recording_enabled
        # The extension field for the external business. This parameter is returned in a call record receipt.
        self.out_id = out_id
        # The ID of the external business.
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        # Phone number A in the AXN extension binding. Phone number A can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        # 
        # This parameter is required.
        self.phone_no_a = phone_no_a
        # Phone number B in the AXN extension binding. When phone number A is used to call phone number X, the call is forwarded to phone number B. If you need to update phone number B, call the [UpdateSubscription](https://help.aliyun.com/document_detail/110253.html) operation.
        # 
        # Phone number B can be set to a mobile phone number or a landline phone number. The landline phone number must be added with an area code, and no hyphen is required between the area code and the landline phone number.
        self.phone_no_b = phone_no_b
        # Phone number X in the AXN extension binding. If you do not specify this parameter, a random phone number is selected from the phone number pool based on the value of the **ExpectCity** parameter and is used as phone number X.
        # 
        # >  Phone number X is the phone number that you purchased in the Phone Number Protection console or by using the [BuySecretNo](https://help.aliyun.com/document_detail/110266.html) operation before you bind a phone number. Phone number X is used to forward calls.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Sets the ringtone for enterprise Color Ring Back Tone (CRBT) in the AXN extension binding.
        # 
        # *   Ringtone setting (with a callback number) when phone number A is used to call phone number X in the AXN extension binding: AXNRing_AB
        # *   Ringtone setting (without a callback number) when phone number A is used to call phone number X in the AXN extension binding: AXNRing_A
        # *   Ringtone setting when an N-side number is used to call phone number X in the AXN extension binding: AXNRing_N
        # 
        # Enterprise CRBT codes: Enterprise CRBT codes can be queried in the Phone Number Protection console. You can choose **Number Pool Management > Enterprise CRBT Management** to view and manage enterprise CRBT codes. You can also upload, delete, or perform other operations on enterprise CRBT codes.
        # 
        # >  The bound enterprise CRBTs are preferentially used. If no enterprise CRBT is set or the setting does not take effect, the enterprise CRBTs at the phone number pool level are used.
        self.ring_config = ring_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class BindAxnExtensionResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        secret_no: str = None,
        subs_id: str = None,
    ):
        # The extension of the phone number.
        self.extension = extension
        # The private number, that is, phone number X.
        self.secret_no = secret_no
        # The binding ID.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindAxnExtensionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_bind_dto: BindAxnExtensionResponseBodySecretBindDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the phone numbers were bound.
        self.secret_bind_dto = secret_bind_dto

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxnExtensionResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        return self


class BindAxnExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAxnExtensionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindAxnExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindBatchAxgRequestAxgBindList(TeaModel):
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
        self.asrmodel_id = asrmodel_id
        self.asrstatus = asrstatus
        self.call_display_type = call_display_type
        self.call_restrict = call_restrict
        self.expect_city = expect_city
        self.expiration = expiration
        # This parameter is required.
        self.group_id = group_id
        self.is_recording_enabled = is_recording_enabled
        self.out_id = out_id
        self.out_order_id = out_order_id
        # This parameter is required.
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.ring_config = ring_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class BindBatchAxgRequest(TeaModel):
    def __init__(
        self,
        axg_bind_list: List[BindBatchAxgRequestAxgBindList] = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.axg_bind_list = axg_bind_list
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.axg_bind_list:
            for k in self.axg_bind_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AxgBindList'] = []
        if self.axg_bind_list is not None:
            for k in self.axg_bind_list:
                result['AxgBindList'].append(k.to_map() if k else None)
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
            for k in m.get('AxgBindList'):
                temp_model = BindBatchAxgRequestAxgBindList()
                self.axg_bind_list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BindBatchAxgShrinkRequest(TeaModel):
    def __init__(
        self,
        axg_bind_list_shrink: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.axg_bind_list_shrink = axg_bind_list_shrink
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.axg_bind_list_shrink is not None:
            result['AxgBindList'] = self.axg_bind_list_shrink
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
        if m.get('AxgBindList') is not None:
            self.axg_bind_list_shrink = m.get('AxgBindList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BindBatchAxgResponseBodySecretBindListSecretBind(TeaModel):
    def __init__(
        self,
        code: str = None,
        extension: str = None,
        group_id: str = None,
        message: str = None,
        phone_no_a: str = None,
        secret_no: str = None,
        subs_id: str = None,
    ):
        self.code = code
        self.extension = extension
        self.group_id = group_id
        self.message = message
        self.phone_no_a = phone_no_a
        self.secret_no = secret_no
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class BindBatchAxgResponseBodySecretBindList(TeaModel):
    def __init__(
        self,
        secret_bind: List[BindBatchAxgResponseBodySecretBindListSecretBind] = None,
    ):
        self.secret_bind = secret_bind

    def validate(self):
        if self.secret_bind:
            for k in self.secret_bind:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecretBind'] = []
        if self.secret_bind is not None:
            for k in self.secret_bind:
                result['SecretBind'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.secret_bind = []
        if m.get('SecretBind') is not None:
            for k in m.get('SecretBind'):
                temp_model = BindBatchAxgResponseBodySecretBindListSecretBind()
                self.secret_bind.append(temp_model.from_map(k))
        return self


class BindBatchAxgResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_bind_list: BindBatchAxgResponseBodySecretBindList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.secret_bind_list = secret_bind_list

    def validate(self):
        if self.secret_bind_list:
            self.secret_bind_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_list is not None:
            result['SecretBindList'] = self.secret_bind_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindList') is not None:
            temp_model = BindBatchAxgResponseBodySecretBindList()
            self.secret_bind_list = temp_model.from_map(m['SecretBindList'])
        return self


class BindBatchAxgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindBatchAxgResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindBatchAxgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuySecretNoRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        display_pool: bool = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
        spec_id: int = None,
    ):
        # Specifies the home location of the phone number.
        # 
        # > 
        # 
        # *   The home location can be set only to a location in the Chinese mainland.
        # 
        # *   A phone number that starts with 95 does not have a home location. If you purchase a phone number that starts with 95, set this parameter to **Nationwide**.
        # 
        # This parameter is required.
        self.city = city
        # Specifies whether to add the phone number to the pool of numbers that will be displayed during calls.
        # 
        # >  This parameter takes effect only for customers who have enabled the number display feature.
        self.display_pool = display_pool
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The prefix of the phone number. If you specify the value of **SecretNo** when you purchase a phone number, a phone number starting with the specified prefix is selected.
        # 
        # >  You can specify up to 18 digits of the phone number prefix.
        self.secret_no = secret_no
        # The type of the phone number. Valid values:
        # 
        # *   **1**: a phone number assigned by a virtual network operator, that is, a phone number that belongs to the 170 or 171 number segment.
        # *   **2**: a phone number provided by a carrier.
        # *   **3**: a phone number that starts with 95.
        # 
        # This parameter is required.
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.display_pool is not None:
            result['DisplayPool'] = self.display_pool
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('DisplayPool') is not None:
            self.display_pool = m.get('DisplayPool')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class BuySecretNoResponseBodySecretBuyInfoDTO(TeaModel):
    def __init__(
        self,
        secret_no: str = None,
    ):
        # The private number, that is, phone number X.
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BuySecretNoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_buy_info_dto: BuySecretNoResponseBodySecretBuyInfoDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the operation was called.
        self.secret_buy_info_dto = secret_buy_info_dto

    def validate(self):
        if self.secret_buy_info_dto:
            self.secret_buy_info_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_buy_info_dto is not None:
            result['SecretBuyInfoDTO'] = self.secret_buy_info_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBuyInfoDTO') is not None:
            temp_model = BuySecretNoResponseBodySecretBuyInfoDTO()
            self.secret_buy_info_dto = temp_model.from_map(m['SecretBuyInfoDTO'])
        return self


class BuySecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BuySecretNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BuySecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPickUpWaybillRequest(TeaModel):
    def __init__(
        self,
        cancel_desc: str = None,
        outer_order_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The cancellation reason.
        # 
        # This parameter is required.
        self.cancel_desc = cancel_desc
        # The ID of the external order.
        # 
        # This parameter is required.
        self.outer_order_code = outer_order_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancel_desc is not None:
            result['CancelDesc'] = self.cancel_desc
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelDesc') is not None:
            self.cancel_desc = m.get('CancelDesc')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CancelPickUpWaybillResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The cancellation result.
        self.message = message
        # Indicates whether the cancellation was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelPickUpWaybillResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CancelPickUpWaybillResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CancelPickUpWaybillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelPickUpWaybillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelPickUpWaybillResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelPickUpWaybillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAxgGroupRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        numbers: str = None,
        owner_id: int = None,
        pool_key: str = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The name of number group G. If the name of number group G is not specified, the ID of number group G is used as the name of number group G.
        # 
        # >  The value must be 1 to 128 characters in length.
        self.name = name
        # The phone numbers that you add to number group G. Separate multiple phone numbers with commas (,). A maximum of 200 phone numbers can be added to number group G.
        self.numbers = numbers
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        # The remarks of number group G. The value must be 0 to 256 characters in length.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateAxgGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        group_id: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The ID of number group G. The value of this parameter is required when the [BindAxg](https://help.aliyun.com/document_detail/110249.html) operation is called to add an AXG binding.
        self.group_id = group_id
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAxgGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAxgGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAxgGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePickUpWaybillRequestConsigneeAddress(TeaModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address of the consignee.
        # 
        # This parameter is required.
        self.address_detail = address_detail
        # The district where the consignee is located.
        # 
        # This parameter is required.
        self.area_name = area_name
        # The city where the consignee is located.
        # 
        # This parameter is required.
        self.city_name = city_name
        # The province where the consignee is located.
        # 
        # This parameter is required.
        self.province_name = province_name
        # The street where the consignee is located.
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillRequestGoodsInfos(TeaModel):
    def __init__(
        self,
        name: str = None,
        quantity: str = None,
        weight: str = None,
    ):
        # The item name.
        self.name = name
        # The item quantity.
        self.quantity = quantity
        # The item weight. Unit: gram.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class CreatePickUpWaybillRequestSendAddress(TeaModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address of the sender.
        # 
        # This parameter is required.
        self.address_detail = address_detail
        # The district where the sender is located.
        # 
        # This parameter is required.
        self.area_name = area_name
        # The city where the sender is located.
        # 
        # This parameter is required.
        self.city_name = city_name
        # The province where the sender is located.
        # 
        # This parameter is required.
        self.province_name = province_name
        # The street where the sender is located.
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillRequest(TeaModel):
    def __init__(
        self,
        appoint_got_end_time: str = None,
        appoint_got_start_time: str = None,
        biz_type: int = None,
        consignee_address: CreatePickUpWaybillRequestConsigneeAddress = None,
        consignee_mobile: str = None,
        consignee_name: str = None,
        consignee_phone: str = None,
        cp_code: str = None,
        goods_infos: List[CreatePickUpWaybillRequestGoodsInfos] = None,
        order_channels: str = None,
        outer_order_code: str = None,
        remark: str = None,
        send_address: CreatePickUpWaybillRequestSendAddress = None,
        send_mobile: str = None,
        send_name: str = None,
        send_phone: str = None,
    ):
        # The end time of the door-to-door pickup in the appointment. The value of **AppointGotEndTime** is the value of **EndTime** of **AppointTimes** in **CpTimeSelectList** returned by the [CreatePickUpWaybillPreQuery](~~CreatePickUpWaybillPreQuery~~#resultMapping) operation.
        # 
        # >  This parameter is required when **BizType** is set to **1**.
        self.appoint_got_end_time = appoint_got_end_time
        # The start time of the door-to-door pickup in the appointment. The value of **AppointGotStartTime** is the value of **StartTime** of **AppointTimes** in **CpTimeSelectList** returned by the [CreatePickUpWaybillPreQuery](~~CreatePickUpWaybillPreQuery~~#resultMapping) operation.
        # 
        # >  This parameter is required when **BizType** is set to **1**.
        self.appoint_got_start_time = appoint_got_start_time
        # The pickup mode. Valid values:
        # 
        # *   **0** (default): real-time order.
        # *   **1**: appointment order.
        self.biz_type = biz_type
        # The address of the consignee.
        # 
        # This parameter is required.
        self.consignee_address = consignee_address
        # The mobile phone number of the consignee.
        # 
        # >  Either ConsigneeMobile or ConsigneePhone must be set.
        self.consignee_mobile = consignee_mobile
        # The name of the consignee.
        # 
        # This parameter is required.
        self.consignee_name = consignee_name
        # The landline phone number of the consignee.
        # 
        # >  Either ConsigneeMobile or ConsigneePhone must be set.
        self.consignee_phone = consignee_phone
        # The code of the courier company.
        self.cp_code = cp_code
        # The items.
        self.goods_infos = goods_infos
        # The external channel sources.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The ID of the external order.
        # 
        # This parameter is required.
        self.outer_order_code = outer_order_code
        # The additional information about the order. The additional information will be printed on the order.
        self.remark = remark
        # The address of the sender.
        # 
        # This parameter is required.
        self.send_address = send_address
        # The mobile phone number of the sender.
        # 
        # >  Either SendMobile or SendPhone must be set.
        self.send_mobile = send_mobile
        # The name of the sender.
        # 
        # This parameter is required.
        self.send_name = send_name
        # The landline phone number of the sender.
        # 
        # >  Either SendMobile or SendPhone must be set.
        self.send_phone = send_phone

    def validate(self):
        if self.consignee_address:
            self.consignee_address.validate()
        if self.goods_infos:
            for k in self.goods_infos:
                if k:
                    k.validate()
        if self.send_address:
            self.send_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time
        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.consignee_address is not None:
            result['ConsigneeAddress'] = self.consignee_address.to_map()
        if self.consignee_mobile is not None:
            result['ConsigneeMobile'] = self.consignee_mobile
        if self.consignee_name is not None:
            result['ConsigneeName'] = self.consignee_name
        if self.consignee_phone is not None:
            result['ConsigneePhone'] = self.consignee_phone
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        result['GoodsInfos'] = []
        if self.goods_infos is not None:
            for k in self.goods_infos:
                result['GoodsInfos'].append(k.to_map() if k else None)
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.send_address is not None:
            result['SendAddress'] = self.send_address.to_map()
        if self.send_mobile is not None:
            result['SendMobile'] = self.send_mobile
        if self.send_name is not None:
            result['SendName'] = self.send_name
        if self.send_phone is not None:
            result['SendPhone'] = self.send_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')
        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ConsigneeAddress') is not None:
            temp_model = CreatePickUpWaybillRequestConsigneeAddress()
            self.consignee_address = temp_model.from_map(m['ConsigneeAddress'])
        if m.get('ConsigneeMobile') is not None:
            self.consignee_mobile = m.get('ConsigneeMobile')
        if m.get('ConsigneeName') is not None:
            self.consignee_name = m.get('ConsigneeName')
        if m.get('ConsigneePhone') is not None:
            self.consignee_phone = m.get('ConsigneePhone')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        self.goods_infos = []
        if m.get('GoodsInfos') is not None:
            for k in m.get('GoodsInfos'):
                temp_model = CreatePickUpWaybillRequestGoodsInfos()
                self.goods_infos.append(temp_model.from_map(k))
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SendAddress') is not None:
            temp_model = CreatePickUpWaybillRequestSendAddress()
            self.send_address = temp_model.from_map(m['SendAddress'])
        if m.get('SendMobile') is not None:
            self.send_mobile = m.get('SendMobile')
        if m.get('SendName') is not None:
            self.send_name = m.get('SendName')
        if m.get('SendPhone') is not None:
            self.send_phone = m.get('SendPhone')
        return self


class CreatePickUpWaybillShrinkRequest(TeaModel):
    def __init__(
        self,
        appoint_got_end_time: str = None,
        appoint_got_start_time: str = None,
        biz_type: int = None,
        consignee_address_shrink: str = None,
        consignee_mobile: str = None,
        consignee_name: str = None,
        consignee_phone: str = None,
        cp_code: str = None,
        goods_infos_shrink: str = None,
        order_channels: str = None,
        outer_order_code: str = None,
        remark: str = None,
        send_address_shrink: str = None,
        send_mobile: str = None,
        send_name: str = None,
        send_phone: str = None,
    ):
        # The end time of the door-to-door pickup in the appointment. The value of **AppointGotEndTime** is the value of **EndTime** of **AppointTimes** in **CpTimeSelectList** returned by the [CreatePickUpWaybillPreQuery](~~CreatePickUpWaybillPreQuery~~#resultMapping) operation.
        # 
        # >  This parameter is required when **BizType** is set to **1**.
        self.appoint_got_end_time = appoint_got_end_time
        # The start time of the door-to-door pickup in the appointment. The value of **AppointGotStartTime** is the value of **StartTime** of **AppointTimes** in **CpTimeSelectList** returned by the [CreatePickUpWaybillPreQuery](~~CreatePickUpWaybillPreQuery~~#resultMapping) operation.
        # 
        # >  This parameter is required when **BizType** is set to **1**.
        self.appoint_got_start_time = appoint_got_start_time
        # The pickup mode. Valid values:
        # 
        # *   **0** (default): real-time order.
        # *   **1**: appointment order.
        self.biz_type = biz_type
        # The address of the consignee.
        # 
        # This parameter is required.
        self.consignee_address_shrink = consignee_address_shrink
        # The mobile phone number of the consignee.
        # 
        # >  Either ConsigneeMobile or ConsigneePhone must be set.
        self.consignee_mobile = consignee_mobile
        # The name of the consignee.
        # 
        # This parameter is required.
        self.consignee_name = consignee_name
        # The landline phone number of the consignee.
        # 
        # >  Either ConsigneeMobile or ConsigneePhone must be set.
        self.consignee_phone = consignee_phone
        # The code of the courier company.
        self.cp_code = cp_code
        # The items.
        self.goods_infos_shrink = goods_infos_shrink
        # The external channel sources.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The ID of the external order.
        # 
        # This parameter is required.
        self.outer_order_code = outer_order_code
        # The additional information about the order. The additional information will be printed on the order.
        self.remark = remark
        # The address of the sender.
        # 
        # This parameter is required.
        self.send_address_shrink = send_address_shrink
        # The mobile phone number of the sender.
        # 
        # >  Either SendMobile or SendPhone must be set.
        self.send_mobile = send_mobile
        # The name of the sender.
        # 
        # This parameter is required.
        self.send_name = send_name
        # The landline phone number of the sender.
        # 
        # >  Either SendMobile or SendPhone must be set.
        self.send_phone = send_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time
        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.consignee_address_shrink is not None:
            result['ConsigneeAddress'] = self.consignee_address_shrink
        if self.consignee_mobile is not None:
            result['ConsigneeMobile'] = self.consignee_mobile
        if self.consignee_name is not None:
            result['ConsigneeName'] = self.consignee_name
        if self.consignee_phone is not None:
            result['ConsigneePhone'] = self.consignee_phone
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.goods_infos_shrink is not None:
            result['GoodsInfos'] = self.goods_infos_shrink
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.send_address_shrink is not None:
            result['SendAddress'] = self.send_address_shrink
        if self.send_mobile is not None:
            result['SendMobile'] = self.send_mobile
        if self.send_name is not None:
            result['SendName'] = self.send_name
        if self.send_phone is not None:
            result['SendPhone'] = self.send_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')
        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ConsigneeAddress') is not None:
            self.consignee_address_shrink = m.get('ConsigneeAddress')
        if m.get('ConsigneeMobile') is not None:
            self.consignee_mobile = m.get('ConsigneeMobile')
        if m.get('ConsigneeName') is not None:
            self.consignee_name = m.get('ConsigneeName')
        if m.get('ConsigneePhone') is not None:
            self.consignee_phone = m.get('ConsigneePhone')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('GoodsInfos') is not None:
            self.goods_infos_shrink = m.get('GoodsInfos')
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SendAddress') is not None:
            self.send_address_shrink = m.get('SendAddress')
        if m.get('SendMobile') is not None:
            self.send_mobile = m.get('SendMobile')
        if m.get('SendName') is not None:
            self.send_name = m.get('SendName')
        if m.get('SendPhone') is not None:
            self.send_phone = m.get('SendPhone')
        return self


class CreatePickUpWaybillResponseBodyData(TeaModel):
    def __init__(
        self,
        cp_code: str = None,
        error_code: str = None,
        error_msg: str = None,
        got_code: str = None,
        mail_no: str = None,
        success: str = None,
    ):
        # The code of the courier company.
        self.cp_code = cp_code
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The pickup code.
        self.got_code = got_code
        # The order ID.
        self.mail_no = mail_no
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.got_code is not None:
            result['GotCode'] = self.got_code
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GotCode') is not None:
            self.got_code = m.get('GotCode')
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePickUpWaybillResponseBody(TeaModel):
    def __init__(
        self,
        data: CreatePickUpWaybillResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreatePickUpWaybillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePickUpWaybillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePickUpWaybillResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePickUpWaybillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo(TeaModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address of the consignee.
        self.address_detail = address_detail
        # The district where the consignee is located.
        self.area_name = area_name
        # The city where the consignee is located.
        self.city_name = city_name
        # The province where the consignee is located.
        self.province_name = province_name
        # The street where the consignee is located.
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillPreQueryRequestConsigneeInfo(TeaModel):
    def __init__(
        self,
        address_info: CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo = None,
        mobile: str = None,
        name: str = None,
    ):
        # The address of the consignee.
        self.address_info = address_info
        # The mobile phone number of the consignee.
        # 
        # This parameter is required.
        self.mobile = mobile
        # The name of the consignee.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.address_info:
            self.address_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info.to_map()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestConsigneeInfoAddressInfo()
            self.address_info = temp_model.from_map(m['AddressInfo'])
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo(TeaModel):
    def __init__(
        self,
        address_detail: str = None,
        area_name: str = None,
        city_name: str = None,
        province_name: str = None,
        town_name: str = None,
    ):
        # The detailed address of the sender.
        self.address_detail = address_detail
        # The district where the sender is located.
        self.area_name = area_name
        # The city where the sender is located.
        self.city_name = city_name
        # The province where the sender is located.
        self.province_name = province_name
        # The street where the sender is located.
        self.town_name = town_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.area_name is not None:
            result['AreaName'] = self.area_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.town_name is not None:
            result['TownName'] = self.town_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('TownName') is not None:
            self.town_name = m.get('TownName')
        return self


class CreatePickUpWaybillPreQueryRequestSenderInfo(TeaModel):
    def __init__(
        self,
        address_info: CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo = None,
        mobile: str = None,
        name: str = None,
    ):
        # The address of the sender.
        self.address_info = address_info
        # The mobile phone number of the sender.
        # 
        # This parameter is required.
        self.mobile = mobile
        # The name of the sender.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.address_info:
            self.address_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info.to_map()
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestSenderInfoAddressInfo()
            self.address_info = temp_model.from_map(m['AddressInfo'])
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePickUpWaybillPreQueryRequest(TeaModel):
    def __init__(
        self,
        consignee_info: CreatePickUpWaybillPreQueryRequestConsigneeInfo = None,
        cp_code: str = None,
        order_channels: str = None,
        outer_order_code: str = None,
        pre_weight: str = None,
        sender_info: CreatePickUpWaybillPreQueryRequestSenderInfo = None,
    ):
        # The consignee information.
        # 
        # This parameter is required.
        self.consignee_info = consignee_info
        # The code of the courier company. If no courier company is specified, the system allocates a courier company.
        self.cp_code = cp_code
        # The identifier of the external channel source. It cannot contain underscores.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The order number of the access system.
        self.outer_order_code = outer_order_code
        # The estimated weight. Unit: gram.
        # 
        # >  If you need to query the estimated price, this parameter is required.
        self.pre_weight = pre_weight
        # The sender information.
        # 
        # This parameter is required.
        self.sender_info = sender_info

    def validate(self):
        if self.consignee_info:
            self.consignee_info.validate()
        if self.sender_info:
            self.sender_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consignee_info is not None:
            result['ConsigneeInfo'] = self.consignee_info.to_map()
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.pre_weight is not None:
            result['PreWeight'] = self.pre_weight
        if self.sender_info is not None:
            result['SenderInfo'] = self.sender_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsigneeInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestConsigneeInfo()
            self.consignee_info = temp_model.from_map(m['ConsigneeInfo'])
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('PreWeight') is not None:
            self.pre_weight = m.get('PreWeight')
        if m.get('SenderInfo') is not None:
            temp_model = CreatePickUpWaybillPreQueryRequestSenderInfo()
            self.sender_info = temp_model.from_map(m['SenderInfo'])
        return self


class CreatePickUpWaybillPreQueryShrinkRequest(TeaModel):
    def __init__(
        self,
        consignee_info_shrink: str = None,
        cp_code: str = None,
        order_channels: str = None,
        outer_order_code: str = None,
        pre_weight: str = None,
        sender_info_shrink: str = None,
    ):
        # The consignee information.
        # 
        # This parameter is required.
        self.consignee_info_shrink = consignee_info_shrink
        # The code of the courier company. If no courier company is specified, the system allocates a courier company.
        self.cp_code = cp_code
        # The identifier of the external channel source. It cannot contain underscores.
        # 
        # This parameter is required.
        self.order_channels = order_channels
        # The order number of the access system.
        self.outer_order_code = outer_order_code
        # The estimated weight. Unit: gram.
        # 
        # >  If you need to query the estimated price, this parameter is required.
        self.pre_weight = pre_weight
        # The sender information.
        # 
        # This parameter is required.
        self.sender_info_shrink = sender_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consignee_info_shrink is not None:
            result['ConsigneeInfo'] = self.consignee_info_shrink
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.order_channels is not None:
            result['OrderChannels'] = self.order_channels
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.pre_weight is not None:
            result['PreWeight'] = self.pre_weight
        if self.sender_info_shrink is not None:
            result['SenderInfo'] = self.sender_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsigneeInfo') is not None:
            self.consignee_info_shrink = m.get('ConsigneeInfo')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('OrderChannels') is not None:
            self.order_channels = m.get('OrderChannels')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('PreWeight') is not None:
            self.pre_weight = m.get('PreWeight')
        if m.get('SenderInfo') is not None:
            self.sender_info_shrink = m.get('SenderInfo')
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        select_disable_tip: str = None,
        selectable: bool = None,
        start_time: str = None,
    ):
        # The end of the time range.
        self.end_time = end_time
        # The tip displayed when the scheduled pickup is not available.
        self.select_disable_tip = select_disable_tip
        # Indicates whether the time range can be selected for the scheduled pickup.
        self.selectable = selectable
        # The beginning of the time range.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.select_disable_tip is not None:
            result['SelectDisableTip'] = self.select_disable_tip
        if self.selectable is not None:
            result['Selectable'] = self.selectable
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SelectDisableTip') is not None:
            self.select_disable_tip = m.get('SelectDisableTip')
        if m.get('Selectable') is not None:
            self.selectable = m.get('Selectable')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes(TeaModel):
    def __init__(
        self,
        date: str = None,
        date_selectable: bool = None,
        time_list: List[CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList] = None,
    ):
        # The date in the YYYY-MM-DD format.
        self.date = date
        # Indicates whether the date is selectable.
        self.date_selectable = date_selectable
        # The time range for the scheduled pickup for this date.
        self.time_list = time_list

    def validate(self):
        if self.time_list:
            for k in self.time_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        if self.date_selectable is not None:
            result['DateSelectable'] = self.date_selectable
        result['TimeList'] = []
        if self.time_list is not None:
            for k in self.time_list:
                result['TimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('DateSelectable') is not None:
            self.date_selectable = m.get('DateSelectable')
        self.time_list = []
        if m.get('TimeList') is not None:
            for k in m.get('TimeList'):
                temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimesTimeList()
                self.time_list.append(temp_model.from_map(k))
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime(TeaModel):
    def __init__(
        self,
        name: str = None,
        select_disable_tip: str = None,
        selectable: bool = None,
    ):
        # The name of the real-time order type.
        self.name = name
        # The tip displayed when the real-time order cannot be placed.
        self.select_disable_tip = select_disable_tip
        # Indicates whether the real-time order can be placed after the deadline for placing a real-time order is reached.
        self.selectable = selectable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.select_disable_tip is not None:
            result['SelectDisableTip'] = self.select_disable_tip
        if self.selectable is not None:
            result['Selectable'] = self.selectable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SelectDisableTip') is not None:
            self.select_disable_tip = m.get('SelectDisableTip')
        if m.get('Selectable') is not None:
            self.selectable = m.get('Selectable')
        return self


class CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList(TeaModel):
    def __init__(
        self,
        appoint_times: List[CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes] = None,
        pre_price: str = None,
        real_time: CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime = None,
    ):
        # The available time for the scheduled pickup. If the current courier company cannot accept the scheduled pickup, this field is left empty.
        self.appoint_times = appoint_times
        # The estimated price. Unit: CNY. The value is accurate to two decimal places. The value of this parameter is displayed if an estimated weight is specified.
        self.pre_price = pre_price
        # The information about whether the real-time order can be selected.
        self.real_time = real_time

    def validate(self):
        if self.appoint_times:
            for k in self.appoint_times:
                if k:
                    k.validate()
        if self.real_time:
            self.real_time.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppointTimes'] = []
        if self.appoint_times is not None:
            for k in self.appoint_times:
                result['AppointTimes'].append(k.to_map() if k else None)
        if self.pre_price is not None:
            result['PrePrice'] = self.pre_price
        if self.real_time is not None:
            result['RealTime'] = self.real_time.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.appoint_times = []
        if m.get('AppointTimes') is not None:
            for k in m.get('AppointTimes'):
                temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListAppointTimes()
                self.appoint_times.append(temp_model.from_map(k))
        if m.get('PrePrice') is not None:
            self.pre_price = m.get('PrePrice')
        if m.get('RealTime') is not None:
            temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectListRealTime()
            self.real_time = temp_model.from_map(m['RealTime'])
        return self


class CreatePickUpWaybillPreQueryResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        cp_time_select_list: List[CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList] = None,
        error_code: str = None,
        error_msg: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The information about whether the courier company can accept the order.
        self.cp_time_select_list = cp_time_select_list
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The response content.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.cp_time_select_list:
            for k in self.cp_time_select_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['CpTimeSelectList'] = []
        if self.cp_time_select_list is not None:
            for k in self.cp_time_select_list:
                result['CpTimeSelectList'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.cp_time_select_list = []
        if m.get('CpTimeSelectList') is not None:
            for k in m.get('CpTimeSelectList'):
                temp_model = CreatePickUpWaybillPreQueryResponseBodyDataCpTimeSelectList()
                self.cp_time_select_list.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePickUpWaybillPreQueryResponseBody(TeaModel):
    def __init__(
        self,
        data: CreatePickUpWaybillPreQueryResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The result set.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreatePickUpWaybillPreQueryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePickUpWaybillPreQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePickUpWaybillPreQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePickUpWaybillPreQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAxgGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.group_id = group_id
        self.owner_id = owner_id
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
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
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteAxgGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAxgGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAxgGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAxgGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretBlacklistRequest(TeaModel):
    def __init__(
        self,
        black_no: str = None,
        black_type: str = None,
        pool_key: str = None,
        remark: str = None,
        way_control: str = None,
    ):
        # The phone numbers in the blacklist. A point-to-point blacklist has a pair of numbers separated by a colon (":"). A number pool blacklist or a platform blacklist has only one single number.
        # 
        # This parameter is required.
        self.black_no = black_no
        # The blacklist type. Valid values:
        # 
        # *   **POINT_TO_POINT_BLACK**: point-to-point blacklist
        # *   **PARTNER_GLOBAL_NUMBER_BLACK**: number pool blacklist
        # 
        # This parameter is required.
        self.black_type = black_type
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        # The remarks for the blacklist.
        self.remark = remark
        # The control on the call direction.
        # 
        # *   **PHONEA_REJECT**: The first phone number in the blacklist can be used to call the second phone number, but the second phone number in the blacklist cannot be used to call the first phone number.
        # *   **PHONEB_REJECT**: The first phone number in the blacklist cannot be used to call the second phone number, but the second phone number in the blacklist can be used to call the first phone number.
        # *   If this parameter is not specified, the two phone numbers in the blacklist cannot be used to call each other.
        # 
        # Valid values:
        # 
        # *   DUPLEX_REJECT
        # *   PHONEA_REJECT
        # *   PHONEB_REJECT
        self.way_control = way_control

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.way_control is not None:
            result['WayControl'] = self.way_control
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('WayControl') is not None:
            self.way_control = m.get('WayControl')
        return self


class DeleteSecretBlacklistResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSecretBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecretBlacklistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSecretBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretAsrDetailRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        call_time: str = None,
        pool_key: str = None,
    ):
        # The ID of the call record.
        # 
        # You can log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view **Call Record ID** on the **Call Record Query** page.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The call initiation time in the call record.
        # 
        # You can log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). View **Call Initiated At** on the **Call Record Query** page, or view the call_time field in the Call Detail Record (CDR) receipt.
        # 
        # This parameter is required.
        self.call_time = call_time
        # The key of the phone number pool.
        # 
        # You can log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        return self


class GetSecretAsrDetailResponseBodyDataSentences(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        channel_id: int = None,
        emotion_value: str = None,
        end_time: int = None,
        silence_duration: int = None,
        speech_rate: int = None,
        text: str = None,
    ):
        # The start time offset of the sentence. Unit: milliseconds.
        self.begin_time = begin_time
        # The ID of the audio track to which the sentence belongs.
        self.channel_id = channel_id
        # The emotion value. Value range: 1 to 10. The higher the value, the stronger the emotion.
        self.emotion_value = emotion_value
        # The end time offset of the sentence. Unit: milliseconds.
        self.end_time = end_time
        # The silence duration between the current sentence and the previous sentence. Unit: seconds.
        self.silence_duration = silence_duration
        # The average speech rate of the sentence. Unit: number of words per minute.
        self.speech_rate = speech_rate
        # The recognition result of the sentence.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSecretAsrDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_duration: int = None,
        business_id: str = None,
        business_key: str = None,
        code: str = None,
        msg: str = None,
        request_id: str = None,
        sentences: List[GetSecretAsrDetailResponseBodyDataSentences] = None,
        type: str = None,
    ):
        # The total duration of the audio file that was recognized. Unit: milliseconds.
        self.biz_duration = biz_duration
        # The ID of the business process.
        self.business_id = business_id
        # The business keyword.
        self.business_key = business_key
        # The status code. The status code 21050000 indicates that the request was successful.
        self.code = code
        # The description.
        self.msg = msg
        # The request ID.
        self.request_id = request_id
        # The ASR result.
        self.sentences = sentences
        # The type.
        self.type = type

    def validate(self):
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_duration is not None:
            result['BizDuration'] = self.biz_duration
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_key is not None:
            result['BusinessKey'] = self.business_key
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['Sentences'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDuration') is not None:
            self.biz_duration = m.get('BizDuration')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessKey') is not None:
            self.business_key = m.get('BusinessKey')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sentences = []
        if m.get('Sentences') is not None:
            for k in m.get('Sentences'):
                temp_model = GetSecretAsrDetailResponseBodyDataSentences()
                self.sentences.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSecretAsrDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSecretAsrDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The ASR details.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSecretAsrDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretAsrDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecretAsrDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSecretAsrDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTotalPublicUrlRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        call_time: str = None,
        check_subs: bool = None,
        owner_id: int = None,
        partner_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the call record.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view **Call Record ID** on the **Call Record Query** page.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The call initiation time in the call record.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). View **Call Initiated At** on the **Call Record Query** page, or view the call_time field in the Call Detail Record (CDR) receipt.
        # 
        # This parameter is required.
        self.call_time = call_time
        # Specifies whether the verification on the binding ID is required.
        # 
        # This parameter is required.
        self.check_subs = check_subs
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.partner_key = partner_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.check_subs is not None:
            result['CheckSubs'] = self.check_subs
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CheckSubs') is not None:
            self.check_subs = m.get('CheckSubs')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetTotalPublicUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        phone_public_url: str = None,
        ring_public_url: str = None,
    ):
        # The download URL of the recorded call.
        # 
        # >  The download URL of the recorded call is valid for 30 days.
        self.phone_public_url = phone_public_url
        # The download URL of the recorded ringing tone.
        # 
        # >  The download URL of the recorded ringing tone is valid for 30 days.
        self.ring_public_url = ring_public_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_public_url is not None:
            result['PhonePublicUrl'] = self.phone_public_url
        if self.ring_public_url is not None:
            result['RingPublicUrl'] = self.ring_public_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhonePublicUrl') is not None:
            self.phone_public_url = m.get('PhonePublicUrl')
        if m.get('RingPublicUrl') is not None:
            self.ring_public_url = m.get('RingPublicUrl')
        return self


class GetTotalPublicUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTotalPublicUrlResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The download URLs of the recording files.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTotalPublicUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTotalPublicUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTotalPublicUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTotalPublicUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockSecretNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        # The key of the phone number pool.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The private number that you want to lock. You must enter a complete mobile phone number.
        # 
        # This parameter is required.
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class LockSecretNoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LockSecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LockSecretNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LockSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAxgGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: int = None,
        numbers: str = None,
        operate_type: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The group ID in the AXG binding.
        # 
        # You can view the group ID by using either of the following methods:
        # 
        # *   On the **Number Pool Management** page in the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account), filter AXG private numbers and click **Number Group G Management** to view the group IDs of number groups G.****\
        # *   If the [CreateAxgGroup](https://help.aliyun.com/document_detail/110250.html) operation is called to create number group G, the value of **GroupId** in the response of the CreateAxgGroup operation is specified as the value of the request parameter **GroupId** of the OperateAxgGroup operation.
        # 
        # >  Number group G must have one or more phone numbers.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The phone numbers that you add to number group G. Separate the phone numbers with commas (,). You can add up to 200 phone numbers at a time.
        # 
        # This parameter is required.
        self.numbers = numbers
        # The type of the operation on number group G. Valid values:
        # 
        # *   **addNumbers**: adds phone numbers to number group G.
        # *   **deleteNumbers**: deletes phone numbers from number group G.
        # *   **overwriteNumbers**: replaces all phone numbers in number group G. All the original phone numbers are deleted from number group G, and new phone numbers are added to number group G.
        # 
        # > 
        # 
        # *   When you replace all phone numbers in number group G, the quantity of original phone numbers in number group G cannot exceed 200.
        # 
        # *   You can add up to 200 phone numbers to number group G at a time.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
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
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OperateAxgGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OperateAxgGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateAxgGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateAxgGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateBlackNoRequest(TeaModel):
    def __init__(
        self,
        black_no: str = None,
        operate_type: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tips: str = None,
    ):
        # The phone number to be added to or deleted from the blacklist.
        # 
        # This parameter is required.
        self.black_no = black_no
        # The type of the operation on the phone number. Valid values:
        # 
        # *   **AddBlack**: adds the phone number to the blacklist.
        # *   **DeleteBlack**: deletes the phone number from the blacklist.
        # 
        # This parameter is required.
        self.operate_type = operate_type
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The description.
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class OperateBlackNoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OperateBlackNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateBlackNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateBlackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPhoneNoAByTrackNoRequest(TeaModel):
    def __init__(
        self,
        cabinet_no: str = None,
        owner_id: int = None,
        phone_no_x: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        track_no: str = None,
    ):
        # The cabinet number.
        self.cabinet_no = cabinet_no
        self.owner_id = owner_id
        # Phone number X returned by the API operation for creating a binding.
        self.phone_no_x = phone_no_x
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The tracking number.
        # 
        # This parameter is required.
        self.track_no = track_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cabinet_no is not None:
            result['CabinetNo'] = self.cabinet_no
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.track_no is not None:
            result['trackNo'] = self.track_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CabinetNo') is not None:
            self.cabinet_no = m.get('CabinetNo')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('trackNo') is not None:
            self.track_no = m.get('trackNo')
        return self


class QueryPhoneNoAByTrackNoResponseBodyModule(TeaModel):
    def __init__(
        self,
        extension: str = None,
        phone_no_a: str = None,
        phone_no_x: str = None,
    ):
        # The extension of phone number X.
        self.extension = extension
        # Phone number A.
        self.phone_no_a = phone_no_a
        # The private number, that is, phone number X.
        self.phone_no_x = phone_no_x

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        return self


class QueryPhoneNoAByTrackNoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[QueryPhoneNoAByTrackNoResponseBodyModule] = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The information returned after the phone numbers were bound.
        self.module = module
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = QueryPhoneNoAByTrackNoResponseBodyModule()
                self.module.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPhoneNoAByTrackNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPhoneNoAByTrackNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPhoneNoAByTrackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordFileDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        call_time: str = None,
        owner_id: int = None,
        pool_key: str = None,
        product_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the call record. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view **Call Record ID** on the **Call Record Query** page.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The call initiation time in the call record. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account). View **Call Initiated At** on the **Call Record Query** page, or view the call_time field in the Call Detail Record (CDR) receipt.
        self.call_time = call_time
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # >  This parameter is required when **ProductType** is left empty.
        self.pool_key = pool_key
        # The product type. Valid values:
        # 
        # *   **AXB_170**.
        # *   **AXN_170**.
        # *   **AXN_95**.
        # *   **AXN_EXTENSION_REUSE**\
        # 
        # > 
        # 
        # *   This parameter is applicable to the original key accounts of Alibaba Cloud. This parameter can be ignored for Alibaba Cloud users.
        # 
        # *   This parameter is required when **PoolKey** is left empty.
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRecordFileDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        download_url: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The download URL of the recording file. The download URL is valid for 2 hours.
        self.download_url = download_url
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRecordFileDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryRecordFileDownloadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRecordFileDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySecretNoDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        # The key of the phone number pool.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The private number.
        # 
        # This parameter is required.
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class QuerySecretNoDetailResponseBodySecretNoInfoDTO(TeaModel):
    def __init__(
        self,
        certify_status: int = None,
        city: str = None,
        province: str = None,
        purchase_time: str = None,
        secret_status: int = None,
        vendor: int = None,
    ):
        # The verification status of the phone number. Valid values:
        # 
        # *   **0**: The phone number is not verified.
        # *   **1**: The phone number is verified.
        self.certify_status = certify_status
        # The city.
        self.city = city
        # The province.
        self.province = province
        # The time when the phone number was purchased.
        self.purchase_time = purchase_time
        # The status of the phone number. Valid values:
        # 
        # *   **0**: The phone number is not bound to other phone numbers.
        # *   **1**: The phone number is bound to other phone numbers.
        # *   **2**: The phone number is locked.
        # *   **3**: The phone number is frozen.
        self.secret_status = secret_status
        # The carrier to which the phone number belongs. Valid values:
        # 
        # *   **1**: China Mobile
        # *   **2**: China Unicom
        # *   **3**: China Telecom
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        if self.purchase_time is not None:
            result['PurchaseTime'] = self.purchase_time
        if self.secret_status is not None:
            result['SecretStatus'] = self.secret_status
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('PurchaseTime') is not None:
            self.purchase_time = m.get('PurchaseTime')
        if m.get('SecretStatus') is not None:
            self.secret_status = m.get('SecretStatus')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class QuerySecretNoDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_no_info_dto: QuerySecretNoDetailResponseBodySecretNoInfoDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The attributes of the phone number.
        self.secret_no_info_dto = secret_no_info_dto

    def validate(self):
        if self.secret_no_info_dto:
            self.secret_no_info_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_no_info_dto is not None:
            result['SecretNoInfoDTO'] = self.secret_no_info_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretNoInfoDTO') is not None:
            temp_model = QuerySecretNoDetailResponseBodySecretNoInfoDTO()
            self.secret_no_info_dto = temp_model.from_map(m['SecretNoInfoDTO'])
        return self


class QuerySecretNoDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySecretNoDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySecretNoDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySecretNoRemainRequest(TeaModel):
    def __init__(
        self,
        city: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
        spec_id: int = None,
    ):
        # The home location of the phone number.
        # 
        # *   If **SpecId** is set to 1 or 2, you can specify the **City** parameter to query the quantity of available phone numbers.
        # 
        # 1.  You can enter a single city name to perform a query.
        # 2.  You can enter National to query the quantity of remaining phone numbers available in the Chinese mainland for online purchase.
        # 3.  You can enter National List to query the cities with available phone numbers and the quantities of remaining phone numbers in the Chinese mainland. Cities without available phone numbers will not be returned.
        # 
        # *   If **SpecId** is set to 3, home locations are not distinguished for phone numbers that start with 95 and only the quantity of all the remaining phone numbers that start with 95 and are available for online purchase can be queried. If SpecId is set to 3, **City** must be set to **Nationwide**.
        # 
        # >  Home locations can be set to only locations in the Chinese mainland.
        # 
        # This parameter is required.
        self.city = city
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The prefix of the phone number. When you call the QuerySecretNoRemain operation with **SecretNo** specified, the quantity of remaining phone numbers with the specified prefix that are available for online purchase is queried.
        # 
        # Up to 18 digits of a phone number prefix can be specified.
        self.secret_no = secret_no
        # The type of the phone number. Valid values:
        # 
        # *   **1**: a phone number assigned by a virtual network operator, that is, a phone number that belongs to the 170 or 171 number segment.
        # *   **2**: a phone number provided by a carrier.
        # *   **3**: a phone number that starts with 95.
        # 
        # This parameter is required.
        self.spec_id = spec_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO(TeaModel):
    def __init__(
        self,
        amount: int = None,
        city: str = None,
    ):
        # The quantity of remaining phone numbers available for online purchase for the city.
        self.amount = amount
        # The home location of the phone numbers.
        self.city = city

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.city is not None:
            result['City'] = self.city
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('City') is not None:
            self.city = m.get('City')
        return self


class QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList(TeaModel):
    def __init__(
        self,
        remain_dto: List[QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO] = None,
    ):
        self.remain_dto = remain_dto

    def validate(self):
        if self.remain_dto:
            for k in self.remain_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['remainDTO'] = []
        if self.remain_dto is not None:
            for k in self.remain_dto:
                result['remainDTO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remain_dto = []
        if m.get('remainDTO') is not None:
            for k in m.get('remainDTO'):
                temp_model = QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO()
                self.remain_dto.append(temp_model.from_map(k))
        return self


class QuerySecretNoRemainResponseBodySecretRemainDTO(TeaModel):
    def __init__(
        self,
        amount: int = None,
        city: str = None,
        remain_dtolist: QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList = None,
    ):
        # The quantity of remaining phone numbers available for online purchase.
        self.amount = amount
        # The home location of the phone numbers.
        self.city = city
        # The information about remaining phone numbers available for online purchase.
        self.remain_dtolist = remain_dtolist

    def validate(self):
        if self.remain_dtolist:
            self.remain_dtolist.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.city is not None:
            result['City'] = self.city
        if self.remain_dtolist is not None:
            result['RemainDTOList'] = self.remain_dtolist.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('RemainDTOList') is not None:
            temp_model = QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOList()
            self.remain_dtolist = temp_model.from_map(m['RemainDTOList'])
        return self


class QuerySecretNoRemainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_remain_dto: QuerySecretNoRemainResponseBodySecretRemainDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the operation was called.
        self.secret_remain_dto = secret_remain_dto

    def validate(self):
        if self.secret_remain_dto:
            self.secret_remain_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_remain_dto is not None:
            result['SecretRemainDTO'] = self.secret_remain_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretRemainDTO') is not None:
            temp_model = QuerySecretNoRemainResponseBodySecretRemainDTO()
            self.secret_remain_dto = temp_model.from_map(m['SecretRemainDTO'])
        return self


class QuerySecretNoRemainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySecretNoRemainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySecretNoRemainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySubsIdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_no_x: str = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_id = owner_id
        # The private number in the binding, that is, phone number X.
        # 
        # This parameter is required.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool.
        # 
        # Log on to the [Phone Number Protection console](https://dyplsnext.console.aliyun.com/overview) and view the key of the phone number pool on the Number Pool Management page.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySubsIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        subs_id: str = None,
    ):
        # The response code. The value OK indicates that the request was successful.
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The binding ID.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class QuerySubsIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySubsIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySubsIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySubscriptionDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        phone_no_x: str = None,
        pool_key: str = None,
        product_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subs_id: str = None,
    ):
        self.owner_id = owner_id
        # The private number in the binding, that is, phone number X.
        # 
        # This parameter is required.
        self.phone_no_x = phone_no_x
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # >  This parameter is required when **ProductType** is left empty.
        self.pool_key = pool_key
        # The product type. Valid values:
        # 
        # *   **AXB_170**\
        # *   **AXN_170**\
        # *   **AXN_95**\
        # *   **AXN_EXTENSION_REUSE**\
        # 
        # > 
        # 
        # *   This parameter is applicable to the original key accounts of Alibaba Cloud. This parameter can be ignored for Alibaba Cloud users.
        # 
        # *   This parameter is required when **PoolKey** is left empty.
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The binding ID.
        # 
        # Log on to the Phone Number Protection console, choose **Number and Number Pool** > **Number Management**. On the Number Management page, select the desired record and click Details to view the binding ID. Alternatively, you can view the value of the **SubsId** parameter returned by an API operation for a phone number binding such as [BindAxb](https://help.aliyun.com/document_detail/110248.html). The value of this parameter indicates a binding ID.
        # 
        # This parameter is required.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
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
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
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
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class QuerySubscriptionDetailResponseBodySecretBindDetailDTO(TeaModel):
    def __init__(
        self,
        asrmodel_id: str = None,
        asrstatus: bool = None,
        call_restrict: str = None,
        expire_date: str = None,
        extension: str = None,
        gmt_create: str = None,
        group_id: int = None,
        need_record: bool = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        status: int = None,
        subs_id: str = None,
    ):
        # The ID of the ASR model.
        self.asrmodel_id = asrmodel_id
        # Indicates whether automatic speech recognition (ASR) is enabled. Valid values:
        # 
        # *   **false**: ASR is disabled.
        # *   **true**: ASR is enabled.
        self.asrstatus = asrstatus
        # The status of one-way call restrictions. No value is returned for this parameter if one-way call restrictions are not set. Valid values:
        # 
        # *   **CONTROL_AX_DISABLE**: Phone number A cannot be used to call phone number X.
        # *   **CONTROL_BX_DISABLE**: Phone number B cannot be used to call phone number X.
        self.call_restrict = call_restrict
        # The expiration time of the binding.
        self.expire_date = expire_date
        # The extension in the AXG extension binding.
        self.extension = extension
        # The creation time of the binding.
        self.gmt_create = gmt_create
        # The ID of number group G in the binding.
        self.group_id = group_id
        # Indicates whether all calls made by the bound phone numbers are recorded. Valid values:
        # 
        # *   **false**\
        # *   **true**\
        self.need_record = need_record
        # Phone number A in the binding.
        self.phone_no_a = phone_no_a
        # Phone number B in the binding.
        self.phone_no_b = phone_no_b
        # The private number in the binding, that is, phone number X.
        self.phone_no_x = phone_no_x
        # The binding status. Valid values:
        # 
        # *   **0**: The binding expired.
        # *   **1**: The binding is in effect.
        self.status = status
        # The binding ID.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.need_record is not None:
            result['NeedRecord'] = self.need_record
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.status is not None:
            result['Status'] = self.status
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NeedRecord') is not None:
            self.need_record = m.get('NeedRecord')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class QuerySubscriptionDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_bind_detail_dto: QuerySubscriptionDetailResponseBodySecretBindDetailDTO = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The information returned after the QuerySubscriptionDetail operation was called.
        self.secret_bind_detail_dto = secret_bind_detail_dto

    def validate(self):
        if self.secret_bind_detail_dto:
            self.secret_bind_detail_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_bind_detail_dto is not None:
            result['SecretBindDetailDTO'] = self.secret_bind_detail_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBindDetailDTO') is not None:
            temp_model = QuerySubscriptionDetailResponseBodySecretBindDetailDTO()
            self.secret_bind_detail_dto = temp_model.from_map(m['SecretBindDetailDTO'])
        return self


class QuerySubscriptionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QuerySubscriptionDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySubscriptionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseSecretNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The prefix of phone numbers. When you call the ReleaseSecretNo operation with **SecretNo** specified, the system performs fuzzy matching against phone numbers based on the prefix.
        # 
        # >  Up to 18 digits of a phone number prefix can be specified.
        # 
        # This parameter is required.
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ReleaseSecretNoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseSecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseSecretNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindSubscriptionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_key: str = None,
        product_type: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
        subs_id: str = None,
    ):
        self.owner_id = owner_id
        # The key of the phone number pool. Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # >  This parameter is required when **ProductType** is left empty.
        self.pool_key = pool_key
        # The product type. Fixed value: **AXB_170**.
        # 
        # > 
        # 
        # *   This parameter is applicable to the original key accounts of Alibaba Cloud. This parameter can be ignored for Alibaba Cloud users.
        # 
        # *   This parameter is required when **PoolKey** is left empty.
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The private number, that is, phone number X specified in an API operation for a phone number binding such as [BindAXG](https://help.aliyun.com/document_detail/110249.html) or automatically assigned after such an operation is called.
        # 
        # This parameter is required.
        self.secret_no = secret_no
        # The binding ID.
        # 
        # Log on to the Phone Number Protection console, choose **Number and Number Pool** > **Number Management**. On the Number Management page, select the desired record and click Details to view the binding ID. Alternatively, you can view the value of the **SubsId** parameter returned by an API operation for a phone number binding such as BindAxb. The value of this parameter indicates a binding ID.
        # 
        # This parameter is required.
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class UnbindSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        charge_id: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # A deprecated parameter.
        self.charge_id = charge_id
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_id is not None:
            result['ChargeId'] = self.charge_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeId') is not None:
            self.charge_id = m.get('ChargeId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockSecretNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        # The key of the phone number pool.
        # 
        # Log on to the [Phone Number Protection console](https://dypls.console.aliyun.com/dypls.htm#/account) and view the key of the phone number pool on the **Number Pool Management** page.
        # 
        # This parameter is required.
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The private number that you want to unlock. You must enter a complete mobile phone number.
        # 
        # This parameter is required.
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnlockSecretNoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnlockSecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnlockSecretNoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnlockSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubscriptionRequest(TeaModel):
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
        # *   **AXB_170**\
        # *   **AXN_170**\
        # *   **AXN_95**\
        # *   **AXN_EXTENSION_REUSE**\
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class UpdateSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other values indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


