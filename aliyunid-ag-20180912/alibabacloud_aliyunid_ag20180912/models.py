# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAgAccountRequest(TeaModel):
    def __init__(
        self,
        login_email: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.login_email = login_email
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAgAccountResponseBodyAgRelationDto(TeaModel):
    def __init__(
        self,
        mpk: str = None,
        pk: str = None,
        type: str = None,
    ):
        # MPK（UID）
        self.mpk = mpk
        self.pk = pk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mpk is not None:
            result['Mpk'] = self.mpk
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAgAccountResponseBody(TeaModel):
    def __init__(
        self,
        ag_relation_dto: CreateAgAccountResponseBodyAgRelationDto = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.ag_relation_dto = ag_relation_dto
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.ag_relation_dto:
            self.ag_relation_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ag_relation_dto is not None:
            result['AgRelationDto'] = self.ag_relation_dto.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgRelationDto') is not None:
            temp_model = CreateAgAccountResponseBodyAgRelationDto()
            self.ag_relation_dto = temp_model.from_map(m['AgRelationDto'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAgAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAgAccountResponseBody = None,
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
            temp_model = CreateAgAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgRelationRequest(TeaModel):
    def __init__(
        self,
        pk: str = None,
    ):
        # This parameter is required.
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class GetAgRelationResponseBodyAgRelationDto(TeaModel):
    def __init__(
        self,
        mpk: str = None,
        pk: str = None,
        type: str = None,
    ):
        self.mpk = mpk
        self.pk = pk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mpk is not None:
            result['Mpk'] = self.mpk
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAgRelationResponseBody(TeaModel):
    def __init__(
        self,
        ag_relation_dto: GetAgRelationResponseBodyAgRelationDto = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.ag_relation_dto = ag_relation_dto
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.ag_relation_dto:
            self.ag_relation_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ag_relation_dto is not None:
            result['AgRelationDto'] = self.ag_relation_dto.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgRelationDto') is not None:
            temp_model = GetAgRelationResponseBodyAgRelationDto()
            self.ag_relation_dto = temp_model.from_map(m['AgRelationDto'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAgRelationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgRelationResponseBody = None,
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
            temp_model = GetAgRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRamBindRequest(TeaModel):
    def __init__(
        self,
        pk: str = None,
    ):
        # This parameter is required.
        self.pk = pk

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pk is not None:
            result['Pk'] = self.pk
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        return self


class GetRamBindResponseBodyRamBindDto(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetRamBindResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        ram_bind_dto: GetRamBindResponseBodyRamBindDto = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.ram_bind_dto = ram_bind_dto
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.ram_bind_dto:
            self.ram_bind_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.ram_bind_dto is not None:
            result['RamBindDto'] = self.ram_bind_dto.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RamBindDto') is not None:
            temp_model = GetRamBindResponseBodyRamBindDto()
            self.ram_bind_dto = temp_model.from_map(m['RamBindDto'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRamBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRamBindResponseBody = None,
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
            temp_model = GetRamBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PaginateAgRelationsRequest(TeaModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        query_count: bool = None,
    ):
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.query_count = query_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        return self


class PaginateAgRelationsResponseBodyAgRelationDtosAgRelationDto(TeaModel):
    def __init__(
        self,
        mpk: str = None,
        pk: str = None,
        type: str = None,
    ):
        self.mpk = mpk
        self.pk = pk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mpk is not None:
            result['Mpk'] = self.mpk
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class PaginateAgRelationsResponseBodyAgRelationDtos(TeaModel):
    def __init__(
        self,
        ag_relation_dto: List[PaginateAgRelationsResponseBodyAgRelationDtosAgRelationDto] = None,
    ):
        self.ag_relation_dto = ag_relation_dto

    def validate(self):
        if self.ag_relation_dto:
            for k in self.ag_relation_dto:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AgRelationDto'] = []
        if self.ag_relation_dto is not None:
            for k in self.ag_relation_dto:
                result['AgRelationDto'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ag_relation_dto = []
        if m.get('AgRelationDto') is not None:
            for k in m.get('AgRelationDto'):
                temp_model = PaginateAgRelationsResponseBodyAgRelationDtosAgRelationDto()
                self.ag_relation_dto.append(temp_model.from_map(k))
        return self


class PaginateAgRelationsResponseBody(TeaModel):
    def __init__(
        self,
        ag_relation_dtos: PaginateAgRelationsResponseBodyAgRelationDtos = None,
        code: str = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.ag_relation_dtos = ag_relation_dtos
        self.code = code
        self.message = message
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.ag_relation_dtos:
            self.ag_relation_dtos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ag_relation_dtos is not None:
            result['AgRelationDtos'] = self.ag_relation_dtos.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgRelationDtos') is not None:
            temp_model = PaginateAgRelationsResponseBodyAgRelationDtos()
            self.ag_relation_dtos = temp_model.from_map(m['AgRelationDtos'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PaginateAgRelationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PaginateAgRelationsResponseBody = None,
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
            temp_model = PaginateAgRelationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


