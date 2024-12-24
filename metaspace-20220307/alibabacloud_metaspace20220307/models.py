# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class ApplyCoordinationWithCodeRequest(TeaModel):
    def __init__(
        self,
        coordination_code: str = None,
        login_region_id: str = None,
        login_token: str = None,
        session_id: str = None,
        uuid: str = None,
    ):
        self.coordination_code = coordination_code
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.session_id = session_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordination_code is not None:
            result['CoordinationCode'] = self.coordination_code
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinationCode') is not None:
            self.coordination_code = m.get('CoordinationCode')
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyCoordinationWithCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        co_id: str = None,
        coordinate_status: str = None,
        coordinate_ticket: str = None,
        coordinator_ali_uid: int = None,
        coordinator_user_id: str = None,
        owner_ali_uid: int = None,
        owner_user_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        self.co_id = co_id
        self.coordinate_status = coordinate_status
        self.coordinate_ticket = coordinate_ticket
        self.coordinator_ali_uid = coordinator_ali_uid
        self.coordinator_user_id = coordinator_user_id
        self.owner_ali_uid = owner_ali_uid
        self.owner_user_id = owner_user_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_id is not None:
            result['CoId'] = self.co_id
        if self.coordinate_status is not None:
            result['CoordinateStatus'] = self.coordinate_status
        if self.coordinate_ticket is not None:
            result['CoordinateTicket'] = self.coordinate_ticket
        if self.coordinator_ali_uid is not None:
            result['CoordinatorAliUid'] = self.coordinator_ali_uid
        if self.coordinator_user_id is not None:
            result['CoordinatorUserId'] = self.coordinator_user_id
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid
        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')
        if m.get('CoordinateStatus') is not None:
            self.coordinate_status = m.get('CoordinateStatus')
        if m.get('CoordinateTicket') is not None:
            self.coordinate_ticket = m.get('CoordinateTicket')
        if m.get('CoordinatorAliUid') is not None:
            self.coordinator_ali_uid = m.get('CoordinatorAliUid')
        if m.get('CoordinatorUserId') is not None:
            self.coordinator_user_id = m.get('CoordinatorUserId')
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ApplyCoordinationWithCodeResponseBody(TeaModel):
    def __init__(
        self,
        data: ApplyCoordinationWithCodeResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ApplyCoordinationWithCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyCoordinationWithCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyCoordinationWithCodeResponseBody = None,
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
            temp_model = ApplyCoordinationWithCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EndAllCoordinationByOwnerRequest(TeaModel):
    def __init__(
        self,
        login_region_id: str = None,
        login_token: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
        session_id: str = None,
    ):
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.resource_id = resource_id
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class EndAllCoordinationByOwnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EndAllCoordinationByOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EndAllCoordinationByOwnerResponseBody = None,
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
            temp_model = EndAllCoordinationByOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCoordinationCodeRequest(TeaModel):
    def __init__(
        self,
        login_region_id: str = None,
        login_token: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
        session_id: str = None,
    ):
        self.login_region_id = login_region_id
        self.login_token = login_token
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_region_id is not None:
            result['LoginRegionId'] = self.login_region_id
        if self.login_token is not None:
            result['LoginToken'] = self.login_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginRegionId') is not None:
            self.login_region_id = m.get('LoginRegionId')
        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class GenerateCoordinationCodeResponseBody(TeaModel):
    def __init__(
        self,
        coordination_code: str = None,
        request_id: str = None,
    ):
        self.coordination_code = coordination_code
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordination_code is not None:
            result['CoordinationCode'] = self.coordination_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinationCode') is not None:
            self.coordination_code = m.get('CoordinationCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateCoordinationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCoordinationCodeResponseBody = None,
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
            temp_model = GenerateCoordinationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


