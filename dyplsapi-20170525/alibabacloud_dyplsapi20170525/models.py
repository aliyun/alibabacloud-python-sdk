# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddAxnTrackNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        phone_no_x: str = None,
        track_no: str = None,
        subs_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.phone_no_x = phone_no_x
        self.track_no = track_no
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.track_no is not None:
            result['trackNo'] = self.track_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('trackNo') is not None:
            self.track_no = m.get('trackNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class AddAxnTrackNoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddAxnTrackNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAxnTrackNoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddAxnTrackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSecretBlacklistRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        black_no: str = None,
        remark: str = None,
        black_type: str = None,
        way_control: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.black_no = black_no
        self.remark = remark
        self.black_type = black_type
        self.way_control = way_control

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.way_control is not None:
            result['WayControl'] = self.way_control
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('WayControl') is not None:
            self.way_control = m.get('WayControl')
        return self


class AddSecretBlacklistResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddSecretBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSecretBlacklistResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddSecretBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxbRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        expiration: str = None,
        expect_city: str = None,
        is_recording_enabled: bool = None,
        out_id: str = None,
        out_order_id: str = None,
        call_restrict: str = None,
        call_display_type: int = None,
        ring_config: str = None,
        asrstatus: bool = None,
        asrmodel_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.expiration = expiration
        self.expect_city = expect_city
        self.is_recording_enabled = is_recording_enabled
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.call_restrict = call_restrict
        self.call_display_type = call_display_type
        self.ring_config = ring_config
        self.asrstatus = asrstatus
        self.asrmodel_id = asrmodel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        return self


class BindAxbResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        subs_id: str = None,
        secret_no: str = None,
    ):
        self.extension = extension
        self.subs_id = subs_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BindAxbResponseBody(TeaModel):
    def __init__(
        self,
        secret_bind_dto: BindAxbResponseBodySecretBindDTO = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.secret_bind_dto = secret_bind_dto
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        result = dict()
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxbResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BindAxbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindAxbResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindAxbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxgRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        phone_no_a: str = None,
        group_id: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        expiration: str = None,
        expect_city: str = None,
        is_recording_enabled: bool = None,
        out_id: str = None,
        out_order_id: str = None,
        call_display_type: int = None,
        ring_config: str = None,
        asrstatus: bool = None,
        asrmodel_id: str = None,
        call_restrict: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.phone_no_a = phone_no_a
        self.group_id = group_id
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.expiration = expiration
        self.expect_city = expect_city
        self.is_recording_enabled = is_recording_enabled
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.call_display_type = call_display_type
        self.ring_config = ring_config
        self.asrstatus = asrstatus
        self.asrmodel_id = asrmodel_id
        self.call_restrict = call_restrict

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        return self


class BindAxgResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        subs_id: str = None,
        secret_no: str = None,
    ):
        self.extension = extension
        self.subs_id = subs_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BindAxgResponseBody(TeaModel):
    def __init__(
        self,
        secret_bind_dto: BindAxgResponseBodySecretBindDTO = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.secret_bind_dto = secret_bind_dto
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        result = dict()
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxgResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BindAxgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindAxgResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindAxgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxnRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        expiration: str = None,
        expect_city: str = None,
        is_recording_enabled: bool = None,
        no_type: str = None,
        out_id: str = None,
        out_order_id: str = None,
        call_display_type: int = None,
        ring_config: str = None,
        asrstatus: bool = None,
        asrmodel_id: str = None,
        call_timeout: int = None,
        call_restrict: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.expiration = expiration
        self.expect_city = expect_city
        self.is_recording_enabled = is_recording_enabled
        self.no_type = no_type
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.call_display_type = call_display_type
        self.ring_config = ring_config
        self.asrstatus = asrstatus
        self.asrmodel_id = asrmodel_id
        self.call_timeout = call_timeout
        self.call_restrict = call_restrict

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.no_type is not None:
            result['NoType'] = self.no_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.call_timeout is not None:
            result['CallTimeout'] = self.call_timeout
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('NoType') is not None:
            self.no_type = m.get('NoType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('CallTimeout') is not None:
            self.call_timeout = m.get('CallTimeout')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        return self


class BindAxnResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        subs_id: str = None,
        secret_no: str = None,
    ):
        self.extension = extension
        self.subs_id = subs_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BindAxnResponseBody(TeaModel):
    def __init__(
        self,
        secret_bind_dto: BindAxnResponseBodySecretBindDTO = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.secret_bind_dto = secret_bind_dto
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        result = dict()
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxnResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BindAxnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindAxnResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindAxnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindAxnExtensionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        phone_no_a: str = None,
        extension: str = None,
        phone_no_b: str = None,
        phone_no_x: str = None,
        expiration: str = None,
        expect_city: str = None,
        is_recording_enabled: bool = None,
        out_id: str = None,
        out_order_id: str = None,
        call_display_type: int = None,
        ring_config: str = None,
        asrstatus: bool = None,
        asrmodel_id: str = None,
        call_restrict: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.phone_no_a = phone_no_a
        self.extension = extension
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.expiration = expiration
        self.expect_city = expect_city
        self.is_recording_enabled = is_recording_enabled
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.call_display_type = call_display_type
        self.ring_config = ring_config
        self.asrstatus = asrstatus
        self.asrmodel_id = asrmodel_id
        self.call_restrict = call_restrict

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.expect_city is not None:
            result['ExpectCity'] = self.expect_city
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.out_order_id is not None:
            result['OutOrderId'] = self.out_order_id
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('ExpectCity') is not None:
            self.expect_city = m.get('ExpectCity')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('OutOrderId') is not None:
            self.out_order_id = m.get('OutOrderId')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        return self


class BindAxnExtensionResponseBodySecretBindDTO(TeaModel):
    def __init__(
        self,
        extension: str = None,
        subs_id: str = None,
        secret_no: str = None,
    ):
        self.extension = extension
        self.subs_id = subs_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BindAxnExtensionResponseBody(TeaModel):
    def __init__(
        self,
        secret_bind_dto: BindAxnExtensionResponseBodySecretBindDTO = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.secret_bind_dto = secret_bind_dto
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.secret_bind_dto:
            self.secret_bind_dto.validate()

    def to_map(self):
        result = dict()
        if self.secret_bind_dto is not None:
            result['SecretBindDTO'] = self.secret_bind_dto.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretBindDTO') is not None:
            temp_model = BindAxnExtensionResponseBodySecretBindDTO()
            self.secret_bind_dto = temp_model.from_map(m['SecretBindDTO'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BindAxnExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindAxnExtensionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindAxnExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuySecretNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        spec_id: int = None,
        city: str = None,
        secret_no: str = None,
        display_pool: bool = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.spec_id = spec_id
        self.city = city
        self.secret_no = secret_no
        self.display_pool = display_pool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.city is not None:
            result['City'] = self.city
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.display_pool is not None:
            result['DisplayPool'] = self.display_pool
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('DisplayPool') is not None:
            self.display_pool = m.get('DisplayPool')
        return self


class BuySecretNoResponseBodySecretBuyInfoDTO(TeaModel):
    def __init__(
        self,
        secret_no: str = None,
    ):
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
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
        message: str = None,
        request_id: str = None,
        secret_buy_info_dto: BuySecretNoResponseBodySecretBuyInfoDTO = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.secret_buy_info_dto = secret_buy_info_dto
        self.code = code

    def validate(self):
        if self.secret_buy_info_dto:
            self.secret_buy_info_dto.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_buy_info_dto is not None:
            result['SecretBuyInfoDTO'] = self.secret_buy_info_dto.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretBuyInfoDTO') is not None:
            temp_model = BuySecretNoResponseBodySecretBuyInfoDTO()
            self.secret_buy_info_dto = temp_model.from_map(m['SecretBuyInfoDTO'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class BuySecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BuySecretNoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BuySecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAxgGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        name: str = None,
        remark: str = None,
        numbers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.name = name
        self.remark = remark
        self.numbers = numbers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        return self


class CreateAxgGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        group_id: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class CreateAxgGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAxgGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAxgGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubscriptionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        secret_no: str = None,
        phone_no: str = None,
        bind_token: str = None,
        prod_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.secret_no = secret_no
        self.phone_no = phone_no
        self.bind_token = bind_token
        self.prod_code = prod_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.bind_token is not None:
            result['BindToken'] = self.bind_token
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('BindToken') is not None:
            self.bind_token = m.get('BindToken')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        return self


class CreateSubscriptionResponseBodyData(TeaModel):
    def __init__(
        self,
        subs_id: str = None,
    ):
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class CreateSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateSubscriptionResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class CreateSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretBlacklistRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        black_no: str = None,
        remark: str = None,
        black_type: str = None,
        way_control: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.black_no = black_no
        self.remark = remark
        self.black_type = black_type
        self.way_control = way_control

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.way_control is not None:
            result['WayControl'] = self.way_control
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('WayControl') is not None:
            self.way_control = m.get('WayControl')
        return self


class DeleteSecretBlacklistResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DeleteSecretBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSecretBlacklistResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSecretBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        verify_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.verify_token = verify_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.verify_token is not None:
            result['VerifyToken'] = self.verify_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('VerifyToken') is not None:
            self.verify_token = m.get('VerifyToken')
        return self


class GetFaceVerifyResponseBodyData(TeaModel):
    def __init__(
        self,
        verify_result: str = None,
    ):
        self.verify_result = verify_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyResult') is not None:
            self.verify_result = m.get('VerifyResult')
        return self


class GetFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetFaceVerifyResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetFaceVerifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetFaceVerifyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretAsrDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        call_id: str = None,
        call_time: str = None,
        pool_key: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.call_id = call_id
        self.call_time = call_time
        self.pool_key = pool_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        return self


class GetSecretAsrDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetSecretAsrDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSecretAsrDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSecretAsrDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        pool_key: str = None,
        subs_id: int = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.pool_key = pool_key
        self.subs_id = subs_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class GetSubscriptionDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        phone_no: str = None,
        city: str = None,
        switch_status: int = None,
        subs_id: int = None,
        secret_no: str = None,
        vendor: str = None,
        province: str = None,
    ):
        self.phone_no = phone_no
        self.city = city
        self.switch_status = switch_status
        self.subs_id = subs_id
        self.secret_no = secret_no
        self.vendor = vendor
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.city is not None:
            result['City'] = self.city
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class GetSubscriptionDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetSubscriptionDetailResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetSubscriptionDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetSubscriptionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSubscriptionDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSubscriptionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTotalPublicUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        check_subs: bool = None,
        partner_key: str = None,
        call_id: str = None,
        call_time: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.check_subs = check_subs
        self.partner_key = partner_key
        self.call_id = call_id
        self.call_time = call_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.check_subs is not None:
            result['CheckSubs'] = self.check_subs
        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CheckSubs') is not None:
            self.check_subs = m.get('CheckSubs')
        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        return self


class GetTotalPublicUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        ring_public_url: str = None,
        phone_public_url: str = None,
    ):
        self.ring_public_url = ring_public_url
        self.phone_public_url = phone_public_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ring_public_url is not None:
            result['RingPublicUrl'] = self.ring_public_url
        if self.phone_public_url is not None:
            result['PhonePublicUrl'] = self.phone_public_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RingPublicUrl') is not None:
            self.ring_public_url = m.get('RingPublicUrl')
        if m.get('PhonePublicUrl') is not None:
            self.phone_public_url = m.get('PhonePublicUrl')
        return self


class GetTotalPublicUrlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetTotalPublicUrlResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetTotalPublicUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetTotalPublicUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTotalPublicUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetTotalPublicUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitFaceVerifyRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        meta_info: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.meta_info = meta_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.meta_info is not None:
            result['MetaInfo'] = self.meta_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('MetaInfo') is not None:
            self.meta_info = m.get('MetaInfo')
        return self


class InitFaceVerifyResponseBodyData(TeaModel):
    def __init__(
        self,
        certify_id: str = None,
    ):
        self.certify_id = certify_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        return self


class InitFaceVerifyResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: InitFaceVerifyResponseBodyData = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = InitFaceVerifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class InitFaceVerifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitFaceVerifyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InitFaceVerifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockSecretNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class LockSecretNoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class LockSecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LockSecretNoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LockSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateAxgGroupRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        group_id: int = None,
        operate_type: str = None,
        numbers: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.group_id = group_id
        self.operate_type = operate_type
        self.numbers = numbers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        return self


class OperateAxgGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class OperateAxgGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OperateAxgGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperateAxgGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateBlackNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        black_no: str = None,
        operate_type: str = None,
        tips: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.black_no = black_no
        self.operate_type = operate_type
        self.tips = tips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.black_no is not None:
            result['BlackNo'] = self.black_no
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.tips is not None:
            result['Tips'] = self.tips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('BlackNo') is not None:
            self.black_no = m.get('BlackNo')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        return self


class OperateBlackNoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class OperateBlackNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OperateBlackNoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OperateBlackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        subs_id: str = None,
        call_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.subs_id = subs_id
        self.call_no = call_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.call_no is not None:
            result['CallNo'] = self.call_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('CallNo') is not None:
            self.call_no = m.get('CallNo')
        return self


class QueryCallStatusResponseBodySecretCallStatusDTO(TeaModel):
    def __init__(
        self,
        status: int = None,
        called_no: str = None,
    ):
        self.status = status
        self.called_no = called_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.called_no is not None:
            result['CalledNo'] = self.called_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CalledNo') is not None:
            self.called_no = m.get('CalledNo')
        return self


class QueryCallStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        secret_call_status_dto: QueryCallStatusResponseBodySecretCallStatusDTO = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.secret_call_status_dto = secret_call_status_dto

    def validate(self):
        if self.secret_call_status_dto:
            self.secret_call_status_dto.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.secret_call_status_dto is not None:
            result['SecretCallStatusDTO'] = self.secret_call_status_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SecretCallStatusDTO') is not None:
            temp_model = QueryCallStatusResponseBodySecretCallStatusDTO()
            self.secret_call_status_dto = temp_model.from_map(m['SecretCallStatusDTO'])
        return self


class QueryCallStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCallStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCallStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPhoneNoAByTrackNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        phone_no_x: str = None,
        track_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.phone_no_x = phone_no_x
        self.track_no = track_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.track_no is not None:
            result['trackNo'] = self.track_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('trackNo') is not None:
            self.track_no = m.get('trackNo')
        return self


class QueryPhoneNoAByTrackNoResponseBodyModulePhoneNoAInfo(TeaModel):
    def __init__(
        self,
        phone_no_x: str = None,
        phone_no_a: str = None,
    ):
        self.phone_no_x = phone_no_x
        self.phone_no_a = phone_no_a

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        return self


class QueryPhoneNoAByTrackNoResponseBodyModule(TeaModel):
    def __init__(
        self,
        phone_no_ainfo: List[QueryPhoneNoAByTrackNoResponseBodyModulePhoneNoAInfo] = None,
    ):
        self.phone_no_ainfo = phone_no_ainfo

    def validate(self):
        if self.phone_no_ainfo:
            for k in self.phone_no_ainfo:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['phoneNoAInfo'] = []
        if self.phone_no_ainfo is not None:
            for k in self.phone_no_ainfo:
                result['phoneNoAInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.phone_no_ainfo = []
        if m.get('phoneNoAInfo') is not None:
            for k in m.get('phoneNoAInfo'):
                temp_model = QueryPhoneNoAByTrackNoResponseBodyModulePhoneNoAInfo()
                self.phone_no_ainfo.append(temp_model.from_map(k))
        return self


class QueryPhoneNoAByTrackNoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        module: QueryPhoneNoAByTrackNoResponseBodyModule = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.module = module
        self.code = code

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.module is not None:
            result['Module'] = self.module.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Module') is not None:
            temp_model = QueryPhoneNoAByTrackNoResponseBodyModule()
            self.module = temp_model.from_map(m['Module'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryPhoneNoAByTrackNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPhoneNoAByTrackNoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPhoneNoAByTrackNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordFileDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        product_type: str = None,
        call_id: str = None,
        call_time: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.product_type = product_type
        self.call_id = call_id
        self.call_time = call_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        return self


class QueryRecordFileDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        download_url: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.download_url = download_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        return self


class QueryRecordFileDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRecordFileDownloadUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRecordFileDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySecretNoRemainRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spec_id: int = None,
        city: str = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.spec_id = spec_id
        self.city = city
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.city is not None:
            result['City'] = self.city
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class QuerySecretNoRemainResponseBodySecretRemainDTORemainDTOListRemainDTO(TeaModel):
    def __init__(
        self,
        amount: int = None,
        city: str = None,
    ):
        self.amount = amount
        self.city = city

    def validate(self):
        pass

    def to_map(self):
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
        self.amount = amount
        self.city = city
        self.remain_dtolist = remain_dtolist

    def validate(self):
        if self.remain_dtolist:
            self.remain_dtolist.validate()

    def to_map(self):
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
        message: str = None,
        request_id: str = None,
        secret_remain_dto: QuerySecretNoRemainResponseBodySecretRemainDTO = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.secret_remain_dto = secret_remain_dto
        self.code = code

    def validate(self):
        if self.secret_remain_dto:
            self.secret_remain_dto.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret_remain_dto is not None:
            result['SecretRemainDTO'] = self.secret_remain_dto.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretRemainDTO') is not None:
            temp_model = QuerySecretNoRemainResponseBodySecretRemainDTO()
            self.secret_remain_dto = temp_model.from_map(m['SecretRemainDTO'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QuerySecretNoRemainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySecretNoRemainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySecretNoRemainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySubscriptionDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        product_type: str = None,
        subs_id: str = None,
        phone_no_x: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.product_type = product_type
        self.subs_id = subs_id
        self.phone_no_x = phone_no_x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        return self


class QuerySubscriptionDetailResponseBodySecretBindDetailDTO(TeaModel):
    def __init__(
        self,
        status: int = None,
        extension: str = None,
        group_id: int = None,
        phone_no_b: str = None,
        asrstatus: bool = None,
        need_record: bool = None,
        gmt_create: str = None,
        expire_date: str = None,
        subs_id: str = None,
        call_restrict: str = None,
        phone_no_x: str = None,
        asrmodel_id: str = None,
        phone_no_a: str = None,
    ):
        self.status = status
        self.extension = extension
        self.group_id = group_id
        self.phone_no_b = phone_no_b
        self.asrstatus = asrstatus
        self.need_record = need_record
        self.gmt_create = gmt_create
        self.expire_date = expire_date
        self.subs_id = subs_id
        self.call_restrict = call_restrict
        self.phone_no_x = phone_no_x
        self.asrmodel_id = asrmodel_id
        self.phone_no_a = phone_no_a

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.need_record is not None:
            result['NeedRecord'] = self.need_record
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('NeedRecord') is not None:
            self.need_record = m.get('NeedRecord')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        return self


class QuerySubscriptionDetailResponseBody(TeaModel):
    def __init__(
        self,
        secret_bind_detail_dto: QuerySubscriptionDetailResponseBodySecretBindDetailDTO = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.secret_bind_detail_dto = secret_bind_detail_dto
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.secret_bind_detail_dto:
            self.secret_bind_detail_dto.validate()

    def to_map(self):
        result = dict()
        if self.secret_bind_detail_dto is not None:
            result['SecretBindDetailDTO'] = self.secret_bind_detail_dto.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretBindDetailDTO') is not None:
            temp_model = QuerySubscriptionDetailResponseBodySecretBindDetailDTO()
            self.secret_bind_detail_dto = temp_model.from_map(m['SecretBindDetailDTO'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QuerySubscriptionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySubscriptionDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySubscriptionDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySubsIdRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        phone_no_x: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.phone_no_x = phone_no_x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        return self


class QuerySubsIdResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        subs_id: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class QuerySubsIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QuerySubsIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySubsIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseSecretNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ReleaseSecretNoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ReleaseSecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseSecretNoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindSubscriptionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        product_type: str = None,
        subs_id: str = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.product_type = product_type
        self.subs_id = subs_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnbindSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        charge_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.charge_id = charge_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.charge_id is not None:
            result['ChargeId'] = self.charge_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChargeId') is not None:
            self.charge_id = m.get('ChargeId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UnbindSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockSecretNoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        secret_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnlockSecretNoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UnlockSecretNoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnlockSecretNoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnlockSecretNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDefaultBRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        pool_key: str = None,
        subs_id: int = None,
        secret_no: str = None,
        phone_no: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.pool_key = pool_key
        self.subs_id = subs_id
        self.secret_no = secret_no
        self.phone_no = phone_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        return self


class UpdateDefaultBResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateDefaultBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDefaultBResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDefaultBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneNumberRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        prod_code: str = None,
        pool_key: str = None,
        subs_id: int = None,
        secret_no: str = None,
        new_phone_no: str = None,
        bind_token: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.prod_code = prod_code
        self.pool_key = pool_key
        self.subs_id = subs_id
        self.secret_no = secret_no
        self.new_phone_no = new_phone_no
        self.bind_token = bind_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.new_phone_no is not None:
            result['NewPhoneNo'] = self.new_phone_no
        if self.bind_token is not None:
            result['BindToken'] = self.bind_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('NewPhoneNo') is not None:
            self.new_phone_no = m.get('NewPhoneNo')
        if m.get('BindToken') is not None:
            self.bind_token = m.get('BindToken')
        return self


class UpdatePhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdatePhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePhoneNumberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePhoneSwitchRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        subs_id: int = None,
        secret_no: str = None,
        switch_status: int = None,
        prod_code: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.subs_id = subs_id
        self.secret_no = secret_no
        self.switch_status = switch_status
        self.prod_code = prod_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        return self


class UpdatePhoneSwitchResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdatePhoneSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdatePhoneSwitchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdatePhoneSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubscriptionRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        pool_key: str = None,
        product_type: str = None,
        subs_id: str = None,
        phone_no_x: str = None,
        phone_no_a: str = None,
        phone_no_b: str = None,
        group_id: str = None,
        call_restrict: str = None,
        expiration: str = None,
        call_display_type: int = None,
        out_id: str = None,
        is_recording_enabled: bool = None,
        operate_type: str = None,
        ring_config: str = None,
        asrstatus: bool = None,
        asrmodel_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.pool_key = pool_key
        self.product_type = product_type
        self.subs_id = subs_id
        self.phone_no_x = phone_no_x
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.group_id = group_id
        self.call_restrict = call_restrict
        self.expiration = expiration
        self.call_display_type = call_display_type
        self.out_id = out_id
        self.is_recording_enabled = is_recording_enabled
        self.operate_type = operate_type
        self.ring_config = ring_config
        self.asrstatus = asrstatus
        self.asrmodel_id = asrmodel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.call_restrict is not None:
            result['CallRestrict'] = self.call_restrict
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.call_display_type is not None:
            result['CallDisplayType'] = self.call_display_type
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.is_recording_enabled is not None:
            result['IsRecordingEnabled'] = self.is_recording_enabled
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.ring_config is not None:
            result['RingConfig'] = self.ring_config
        if self.asrstatus is not None:
            result['ASRStatus'] = self.asrstatus
        if self.asrmodel_id is not None:
            result['ASRModelId'] = self.asrmodel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('CallRestrict') is not None:
            self.call_restrict = m.get('CallRestrict')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('CallDisplayType') is not None:
            self.call_display_type = m.get('CallDisplayType')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('IsRecordingEnabled') is not None:
            self.is_recording_enabled = m.get('IsRecordingEnabled')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('RingConfig') is not None:
            self.ring_config = m.get('RingConfig')
        if m.get('ASRStatus') is not None:
            self.asrstatus = m.get('ASRStatus')
        if m.get('ASRModelId') is not None:
            self.asrmodel_id = m.get('ASRModelId')
        return self


class UpdateSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class UpdateSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSubscriptionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


