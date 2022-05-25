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
        self.phone_no_x = phone_no_x
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subs_id = subs_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.black_no = black_no
        self.black_type = black_type
        self.pool_key = pool_key
        self.remark = remark
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.asrmodel_id = asrmodel_id
        self.asrstatus = asrstatus
        self.call_display_type = call_display_type
        self.call_restrict = call_restrict
        self.call_timeout = call_timeout
        self.expect_city = expect_city
        self.expiration = expiration
        self.is_recording_enabled = is_recording_enabled
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.extension = extension
        self.secret_no = secret_no
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.asrmodel_id = asrmodel_id
        self.asrstatus = asrstatus
        self.call_display_type = call_display_type
        self.call_restrict = call_restrict
        self.expect_city = expect_city
        self.expiration = expiration
        self.group_id = group_id
        self.is_recording_enabled = is_recording_enabled
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.extension = extension
        self.secret_no = secret_no
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.asrmodel_id = asrmodel_id
        self.asrstatus = asrstatus
        self.call_display_type = call_display_type
        self.call_restrict = call_restrict
        self.call_timeout = call_timeout
        self.expect_city = expect_city
        self.expiration = expiration
        self.is_recording_enabled = is_recording_enabled
        self.no_type = no_type
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.extension = extension
        self.secret_no = secret_no
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.asrmodel_id = asrmodel_id
        self.asrstatus = asrstatus
        self.call_display_type = call_display_type
        self.call_restrict = call_restrict
        self.expect_city = expect_city
        self.expiration = expiration
        self.extension = extension
        self.is_recording_enabled = is_recording_enabled
        self.out_id = out_id
        self.out_order_id = out_order_id
        self.owner_id = owner_id
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.extension = extension
        self.secret_no = secret_no
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.city = city
        self.display_pool = display_pool
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.cancel_desc = cancel_desc
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
        self.error_code = error_code
        self.error_msg = error_msg
        self.message = message
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
        self.code = code
        self.data = data
        self.message = message
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class ConfirmSendSmsRequest(TeaModel):
    def __init__(
        self,
        call_id: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
    ):
        self.call_id = call_id
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
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
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
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


class ConfirmSendSmsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfirmSendSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmSendSmsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ConfirmSendSmsResponseBody()
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
        self.name = name
        self.numbers = numbers
        self.owner_id = owner_id
        self.pool_key = pool_key
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
        self.code = code
        self.group_id = group_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.address_detail = address_detail
        self.area_name = area_name
        self.city_name = city_name
        self.province_name = province_name
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
        self.name = name
        self.quantity = quantity
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
        self.address_detail = address_detail
        self.area_name = area_name
        self.city_name = city_name
        self.province_name = province_name
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
        self.appoint_got_end_time = appoint_got_end_time
        self.appoint_got_start_time = appoint_got_start_time
        self.biz_type = biz_type
        self.consignee_address = consignee_address
        self.consignee_mobile = consignee_mobile
        self.consignee_name = consignee_name
        self.consignee_phone = consignee_phone
        self.cp_code = cp_code
        self.goods_infos = goods_infos
        self.order_channels = order_channels
        self.outer_order_code = outer_order_code
        self.remark = remark
        self.send_address = send_address
        self.send_mobile = send_mobile
        self.send_name = send_name
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
        self.appoint_got_end_time = appoint_got_end_time
        self.appoint_got_start_time = appoint_got_start_time
        self.biz_type = biz_type
        self.consignee_address_shrink = consignee_address_shrink
        self.consignee_mobile = consignee_mobile
        self.consignee_name = consignee_name
        self.consignee_phone = consignee_phone
        self.cp_code = cp_code
        self.goods_infos_shrink = goods_infos_shrink
        self.order_channels = order_channels
        self.outer_order_code = outer_order_code
        self.remark = remark
        self.send_address_shrink = send_address_shrink
        self.send_mobile = send_mobile
        self.send_name = send_name
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
        self.cp_code = cp_code
        self.error_code = error_code
        self.error_msg = error_msg
        self.got_code = got_code
        self.mail_no = mail_no
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
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.address_detail = address_detail
        self.area_name = area_name
        self.city_name = city_name
        self.province_name = province_name
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
        self.address_info = address_info
        self.mobile = mobile
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
        self.address_detail = address_detail
        self.area_name = area_name
        self.city_name = city_name
        self.province_name = province_name
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
        self.address_info = address_info
        self.mobile = mobile
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
        self.consignee_info = consignee_info
        self.cp_code = cp_code
        self.order_channels = order_channels
        self.outer_order_code = outer_order_code
        self.pre_weight = pre_weight
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
        self.consignee_info_shrink = consignee_info_shrink
        self.cp_code = cp_code
        self.order_channels = order_channels
        self.outer_order_code = outer_order_code
        self.pre_weight = pre_weight
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
        self.end_time = end_time
        self.select_disable_tip = select_disable_tip
        self.selectable = selectable
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
        self.date = date
        self.date_selectable = date_selectable
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
        self.name = name
        self.select_disable_tip = select_disable_tip
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
        self.appoint_times = appoint_times
        self.pre_price = pre_price
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
        self.code = code
        self.cp_time_select_list = cp_time_select_list
        self.error_code = error_code
        self.error_msg = error_msg
        self.message = message
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
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DeleteSecretBlacklistRequest(TeaModel):
    def __init__(
        self,
        black_no: str = None,
        black_type: str = None,
        pool_key: str = None,
        remark: str = None,
        way_control: str = None,
    ):
        self.black_no = black_no
        self.black_type = black_type
        self.pool_key = pool_key
        self.remark = remark
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.call_id = call_id
        self.call_time = call_time
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
        self.begin_time = begin_time
        self.channel_id = channel_id
        self.emotion_value = emotion_value
        self.end_time = end_time
        self.silence_duration = silence_duration
        self.speech_rate = speech_rate
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
        self.biz_duration = biz_duration
        self.business_id = business_id
        self.business_key = business_key
        self.code = code
        self.msg = msg
        self.request_id = request_id
        self.sentences = sentences
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
        self.code = code
        self.data = data
        self.message = message
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class GetSubscriptionDetailRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secret_no: str = None,
        subs_id: int = None,
    ):
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no
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
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        return self


class GetSubscriptionDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        city: str = None,
        phone_no: str = None,
        province: str = None,
        secret_no: str = None,
        subs_id: int = None,
        switch_status: int = None,
        vendor: str = None,
    ):
        self.city = city
        self.phone_no = phone_no
        self.province = province
        self.secret_no = secret_no
        self.subs_id = subs_id
        self.switch_status = switch_status
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.province is not None:
            result['Province'] = self.province
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.subs_id is not None:
            result['SubsId'] = self.subs_id
        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubsId') is not None:
            self.subs_id = m.get('SubsId')
        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class GetSubscriptionDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSubscriptionDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetSubscriptionDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSubscriptionDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubscriptionDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = GetSubscriptionDetailResponseBody()
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
        self.call_id = call_id
        self.call_time = call_time
        self.check_subs = check_subs
        self.owner_id = owner_id
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
        self.phone_public_url = phone_public_url
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
        self.code = code
        self.data = data
        self.message = message
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.group_id = group_id
        self.numbers = numbers
        self.operate_type = operate_type
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.black_no = black_no
        self.operate_type = operate_type
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class QueryCallStatusRequest(TeaModel):
    def __init__(
        self,
        call_no: str = None,
        owner_id: int = None,
        pool_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        subs_id: str = None,
    ):
        self.call_no = call_no
        self.owner_id = owner_id
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.subs_id = subs_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_no is not None:
            result['CallNo'] = self.call_no
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallNo') is not None:
            self.call_no = m.get('CallNo')
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
        return self


class QueryCallStatusResponseBodySecretCallStatusDTO(TeaModel):
    def __init__(
        self,
        called_no: str = None,
        extension: str = None,
        status: int = None,
    ):
        self.called_no = called_no
        self.extension = extension
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_no is not None:
            result['CalledNo'] = self.called_no
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNo') is not None:
            self.called_no = m.get('CalledNo')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryCallStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        secret_call_status_dto: QueryCallStatusResponseBodySecretCallStatusDTO = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.secret_call_status_dto = secret_call_status_dto

    def validate(self):
        if self.secret_call_status_dto:
            self.secret_call_status_dto.validate()

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
        if self.secret_call_status_dto is not None:
            result['SecretCallStatusDTO'] = self.secret_call_status_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecretCallStatusDTO') is not None:
            temp_model = QueryCallStatusResponseBodySecretCallStatusDTO()
            self.secret_call_status_dto = temp_model.from_map(m['SecretCallStatusDTO'])
        return self


class QueryCallStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryCallStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = QueryCallStatusResponseBody()
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
        self.cabinet_no = cabinet_no
        self.owner_id = owner_id
        self.phone_no_x = phone_no_x
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.extension = extension
        self.phone_no_a = phone_no_a
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
        self.code = code
        self.message = message
        self.module = module
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.call_id = call_id
        self.call_time = call_time
        self.owner_id = owner_id
        self.pool_key = pool_key
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
        self.code = code
        self.download_url = download_url
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.certify_status = certify_status
        self.city = city
        self.province = province
        self.purchase_time = purchase_time
        self.secret_status = secret_status
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.city = city
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no
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
        self.amount = amount
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
        self.amount = amount
        self.city = city
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.phone_no_x = phone_no_x
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.phone_no_x = phone_no_x
        self.pool_key = pool_key
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.asrmodel_id = asrmodel_id
        self.asrstatus = asrstatus
        self.call_restrict = call_restrict
        self.expire_date = expire_date
        self.extension = extension
        self.gmt_create = gmt_create
        self.group_id = group_id
        self.need_record = need_record
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.status = status
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
        self.code = code
        self.message = message
        self.request_id = request_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.pool_key = pool_key
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secret_no = secret_no
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
        self.charge_id = charge_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.pool_key = pool_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.asrmodel_id = asrmodel_id
        self.asrstatus = asrstatus
        self.call_display_type = call_display_type
        self.call_restrict = call_restrict
        self.expiration = expiration
        self.group_id = group_id
        self.is_recording_enabled = is_recording_enabled
        self.operate_type = operate_type
        self.out_id = out_id
        self.owner_id = owner_id
        self.phone_no_a = phone_no_a
        self.phone_no_b = phone_no_b
        self.phone_no_x = phone_no_x
        self.pool_key = pool_key
        self.product_type = product_type
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.ring_config = ring_config
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


