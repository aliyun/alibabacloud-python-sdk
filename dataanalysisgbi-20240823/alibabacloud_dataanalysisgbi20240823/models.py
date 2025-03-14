# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Any, Dict


class BatchDeleteSynonymsRequest(TeaModel):
    def __init__(
        self,
        synonym_id_keys: List[str] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.synonym_id_keys = synonym_id_keys
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synonym_id_keys is not None:
            result['synonymIdKeys'] = self.synonym_id_keys
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('synonymIdKeys') is not None:
            self.synonym_id_keys = m.get('synonymIdKeys')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class BatchDeleteSynonymsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class BatchDeleteSynonymsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchDeleteSynonymsResponseBody = None,
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
            temp_model = BatchDeleteSynonymsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelDatasourceAuthorizationRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CancelDatasourceAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CancelDatasourceAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelDatasourceAuthorizationResponseBody = None,
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
            temp_model = CancelDatasourceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBusinessLogicRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        type: int = None,
        workspace_id: str = None,
    ):
        self.description = description
        self.type = type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateBusinessLogicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateBusinessLogicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBusinessLogicResponseBody = None,
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
            temp_model = CreateBusinessLogicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatasourceAuthorizationRequest(TeaModel):
    def __init__(
        self,
        password: str = None,
        type: int = None,
        url: str = None,
        user_name: str = None,
        vdb_id: str = None,
        workspace_id: str = None,
    ):
        self.password = password
        # This parameter is required.
        self.type = type
        self.url = url
        self.user_name = user_name
        self.vdb_id = vdb_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.password is not None:
            result['password'] = self.password
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.vdb_id is not None:
            result['vdbId'] = self.vdb_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('vdbId') is not None:
            self.vdb_id = m.get('vdbId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateDatasourceAuthorizationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateDatasourceAuthorizationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatasourceAuthorizationResponseBody = None,
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
            temp_model = CreateDatasourceAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSynonymsRequest(TeaModel):
    def __init__(
        self,
        columns: List[str] = None,
        word: str = None,
        word_synonyms: List[str] = None,
        workspace_id: str = None,
    ):
        self.columns = columns
        # This parameter is required.
        self.word = word
        # This parameter is required.
        self.word_synonyms = word_synonyms
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.word is not None:
            result['word'] = self.word
        if self.word_synonyms is not None:
            result['wordSynonyms'] = self.word_synonyms
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('wordSynonyms') is not None:
            self.word_synonyms = m.get('wordSynonyms')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateSynonymsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSynonymsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSynonymsResponseBody = None,
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
            temp_model = CreateSynonymsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualDatasourceInstanceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: int = None,
        workspace_id: str = None,
    ):
        self.description = description
        self.name = name
        self.type = type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateVirtualDatasourceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateVirtualDatasourceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVirtualDatasourceInstanceResponseBody = None,
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
            temp_model = CreateVirtualDatasourceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBusinessLogicRequest(TeaModel):
    def __init__(
        self,
        business_logic_id_keys: List[str] = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.business_logic_id_keys = business_logic_id_keys
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_logic_id_keys is not None:
            result['businessLogicIdKeys'] = self.business_logic_id_keys
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessLogicIdKeys') is not None:
            self.business_logic_id_keys = m.get('businessLogicIdKeys')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DeleteBusinessLogicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteBusinessLogicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBusinessLogicResponseBody = None,
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
            temp_model = DeleteBusinessLogicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteColumnRequest(TeaModel):
    def __init__(
        self,
        column_id_key: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.column_id_key = column_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_id_key is not None:
            result['columnIdKey'] = self.column_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnIdKey') is not None:
            self.column_id_key = m.get('columnIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DeleteColumnResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteColumnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteColumnResponseBody = None,
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
            temp_model = DeleteColumnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSelectedTableRequest(TeaModel):
    def __init__(
        self,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DeleteSelectedTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteSelectedTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSelectedTableResponseBody = None,
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
            temp_model = DeleteSelectedTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualDatasourceInstanceRequest(TeaModel):
    def __init__(
        self,
        vdb_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.vdb_id = vdb_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vdb_id is not None:
            result['vdbId'] = self.vdb_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vdbId') is not None:
            self.vdb_id = m.get('vdbId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DeleteVirtualDatasourceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteVirtualDatasourceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVirtualDatasourceInstanceResponseBody = None,
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
            temp_model = DeleteVirtualDatasourceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBusinessLogicRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListBusinessLogicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListBusinessLogicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBusinessLogicResponseBody = None,
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
            temp_model = ListBusinessLogicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListColumnRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: int = None,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListColumnResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListColumnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListColumnResponseBody = None,
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
            temp_model = ListColumnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEnumMappingRequest(TeaModel):
    def __init__(
        self,
        column_id_key: str = None,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.column_id_key = column_id_key
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_id_key is not None:
            result['columnIdKey'] = self.column_id_key
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnIdKey') is not None:
            self.column_id_key = m.get('columnIdKey')
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListEnumMappingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEnumMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEnumMappingResponseBody = None,
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
            temp_model = ListEnumMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSelectedTablesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListSelectedTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListSelectedTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSelectedTablesResponseBody = None,
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
            temp_model = ListSelectedTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSynonymsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListSynonymsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListSynonymsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSynonymsResponseBody = None,
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
            temp_model = ListSynonymsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualDatasourceInstanceRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListVirtualDatasourceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListVirtualDatasourceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVirtualDatasourceInstanceResponseBody = None,
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
            temp_model = ListVirtualDatasourceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoverColumnRequest(TeaModel):
    def __init__(
        self,
        column_id_key: str = None,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.column_id_key = column_id_key
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_id_key is not None:
            result['columnIdKey'] = self.column_id_key
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnIdKey') is not None:
            self.column_id_key = m.get('columnIdKey')
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class RecoverColumnResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RecoverColumnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecoverColumnResponseBody = None,
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
            temp_model = RecoverColumnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResyncTableRequest(TeaModel):
    def __init__(
        self,
        keep: bool = None,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        self.keep = keep
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep is not None:
            result['keep'] = self.keep
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep') is not None:
            self.keep = m.get('keep')
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ResyncTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ResyncTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResyncTableResponseBody = None,
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
            temp_model = ResyncTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunDataAnalysisRequest(TeaModel):
    def __init__(
        self,
        agent_ctrl_params: Any = None,
        data_role: List[str] = None,
        generate_sql_only: bool = None,
        query: str = None,
        session_id: str = None,
        specification_type: str = None,
        user_params: Any = None,
    ):
        self.agent_ctrl_params = agent_ctrl_params
        self.data_role = data_role
        self.generate_sql_only = generate_sql_only
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.specification_type = specification_type
        self.user_params = user_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_ctrl_params is not None:
            result['agentCtrlParams'] = self.agent_ctrl_params
        if self.data_role is not None:
            result['dataRole'] = self.data_role
        if self.generate_sql_only is not None:
            result['generateSqlOnly'] = self.generate_sql_only
        if self.query is not None:
            result['query'] = self.query
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.specification_type is not None:
            result['specificationType'] = self.specification_type
        if self.user_params is not None:
            result['userParams'] = self.user_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentCtrlParams') is not None:
            self.agent_ctrl_params = m.get('agentCtrlParams')
        if m.get('dataRole') is not None:
            self.data_role = m.get('dataRole')
        if m.get('generateSqlOnly') is not None:
            self.generate_sql_only = m.get('generateSqlOnly')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('specificationType') is not None:
            self.specification_type = m.get('specificationType')
        if m.get('userParams') is not None:
            self.user_params = m.get('userParams')
        return self


class RunDataAnalysisResponseBodyDataSqlData(TeaModel):
    def __init__(
        self,
        column: List[str] = None,
        data: List[Dict[str, Any]] = None,
    ):
        self.column = column
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['column'] = self.column
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('column') is not None:
            self.column = m.get('column')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class RunDataAnalysisResponseBodyDataVisualizationData(TeaModel):
    def __init__(
        self,
        plot_type: str = None,
        x_axis: List[str] = None,
        y_axis: List[str] = None,
    ):
        self.plot_type = plot_type
        self.x_axis = x_axis
        self.y_axis = y_axis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plot_type is not None:
            result['plotType'] = self.plot_type
        if self.x_axis is not None:
            result['xAxis'] = self.x_axis
        if self.y_axis is not None:
            result['yAxis'] = self.y_axis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plotType') is not None:
            self.plot_type = m.get('plotType')
        if m.get('xAxis') is not None:
            self.x_axis = m.get('xAxis')
        if m.get('yAxis') is not None:
            self.y_axis = m.get('yAxis')
        return self


class RunDataAnalysisResponseBodyDataVisualization(TeaModel):
    def __init__(
        self,
        data: RunDataAnalysisResponseBodyDataVisualizationData = None,
        text: str = None,
    ):
        self.data = data
        self.text = text

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = RunDataAnalysisResponseBodyDataVisualizationData()
            self.data = temp_model.from_map(m['data'])
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunDataAnalysisResponseBodyData(TeaModel):
    def __init__(
        self,
        attempts: List[Any] = None,
        error_message: str = None,
        event: str = None,
        evidence: str = None,
        http_status_code: int = None,
        request_id: str = None,
        rewrite: str = None,
        selector: List[str] = None,
        session_id: str = None,
        sql: str = None,
        sql_data: RunDataAnalysisResponseBodyDataSqlData = None,
        sql_error: str = None,
        visualization: RunDataAnalysisResponseBodyDataVisualization = None,
    ):
        self.attempts = attempts
        self.error_message = error_message
        self.event = event
        self.evidence = evidence
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.rewrite = rewrite
        self.selector = selector
        self.session_id = session_id
        self.sql = sql
        self.sql_data = sql_data
        self.sql_error = sql_error
        self.visualization = visualization

    def validate(self):
        if self.sql_data:
            self.sql_data.validate()
        if self.visualization:
            self.visualization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attempts is not None:
            result['attempts'] = self.attempts
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.evidence is not None:
            result['evidence'] = self.evidence
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite
        if self.selector is not None:
            result['selector'] = self.selector
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.sql is not None:
            result['sql'] = self.sql
        if self.sql_data is not None:
            result['sqlData'] = self.sql_data.to_map()
        if self.sql_error is not None:
            result['sqlError'] = self.sql_error
        if self.visualization is not None:
            result['visualization'] = self.visualization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attempts') is not None:
            self.attempts = m.get('attempts')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('evidence') is not None:
            self.evidence = m.get('evidence')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('rewrite') is not None:
            self.rewrite = m.get('rewrite')
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        if m.get('sqlData') is not None:
            temp_model = RunDataAnalysisResponseBodyDataSqlData()
            self.sql_data = temp_model.from_map(m['sqlData'])
        if m.get('sqlError') is not None:
            self.sql_error = m.get('sqlError')
        if m.get('visualization') is not None:
            temp_model = RunDataAnalysisResponseBodyDataVisualization()
            self.visualization = temp_model.from_map(m['visualization'])
        return self


class RunDataAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RunDataAnalysisResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = RunDataAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RunDataAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunDataAnalysisResponseBody = None,
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
            temp_model = RunDataAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunDataResultAnalysisRequestSqlData(TeaModel):
    def __init__(
        self,
        column: List[str] = None,
        data: List[Dict[str, str]] = None,
    ):
        self.column = column
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['column'] = self.column
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('column') is not None:
            self.column = m.get('column')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class RunDataResultAnalysisRequest(TeaModel):
    def __init__(
        self,
        analysis_mode: str = None,
        request_id: str = None,
        sql_data: RunDataResultAnalysisRequestSqlData = None,
        workspace_id: str = None,
    ):
        self.analysis_mode = analysis_mode
        # This parameter is required.
        self.request_id = request_id
        self.sql_data = sql_data
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.sql_data:
            self.sql_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_mode is not None:
            result['analysisMode'] = self.analysis_mode
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.sql_data is not None:
            result['sqlData'] = self.sql_data.to_map()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisMode') is not None:
            self.analysis_mode = m.get('analysisMode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sqlData') is not None:
            temp_model = RunDataResultAnalysisRequestSqlData()
            self.sql_data = temp_model.from_map(m['sqlData'])
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class RunDataResultAnalysisResponseBodyDataVisualizationData(TeaModel):
    def __init__(
        self,
        plot_type: str = None,
        x_axis: List[str] = None,
        y_axis: List[str] = None,
    ):
        self.plot_type = plot_type
        self.x_axis = x_axis
        self.y_axis = y_axis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plot_type is not None:
            result['plotType'] = self.plot_type
        if self.x_axis is not None:
            result['xAxis'] = self.x_axis
        if self.y_axis is not None:
            result['yAxis'] = self.y_axis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plotType') is not None:
            self.plot_type = m.get('plotType')
        if m.get('xAxis') is not None:
            self.x_axis = m.get('xAxis')
        if m.get('yAxis') is not None:
            self.y_axis = m.get('yAxis')
        return self


class RunDataResultAnalysisResponseBodyDataVisualization(TeaModel):
    def __init__(
        self,
        data: RunDataResultAnalysisResponseBodyDataVisualizationData = None,
        text: str = None,
    ):
        self.data = data
        self.text = text

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = RunDataResultAnalysisResponseBodyDataVisualizationData()
            self.data = temp_model.from_map(m['data'])
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class RunDataResultAnalysisResponseBodyData(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        event: str = None,
        request_id: str = None,
        rewrite: str = None,
        sql: str = None,
        visualization: RunDataResultAnalysisResponseBodyDataVisualization = None,
    ):
        self.error_message = error_message
        self.event = event
        self.request_id = request_id
        self.rewrite = rewrite
        self.sql = sql
        self.visualization = visualization

    def validate(self):
        if self.visualization:
            self.visualization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite
        if self.sql is not None:
            result['sql'] = self.sql
        if self.visualization is not None:
            result['visualization'] = self.visualization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('rewrite') is not None:
            self.rewrite = m.get('rewrite')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        if m.get('visualization') is not None:
            temp_model = RunDataResultAnalysisResponseBodyDataVisualization()
            self.visualization = temp_model.from_map(m['visualization'])
        return self


class RunDataResultAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        data: RunDataResultAnalysisResponseBodyData = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = RunDataResultAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class RunDataResultAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunDataResultAnalysisResponseBody = None,
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
            temp_model = RunDataResultAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunSqlGenerationRequest(TeaModel):
    def __init__(
        self,
        query: str = None,
        session_id: str = None,
        specification_type: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.specification_type = specification_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.specification_type is not None:
            result['specificationType'] = self.specification_type
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('specificationType') is not None:
            self.specification_type = m.get('specificationType')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class RunSqlGenerationResponseBodyData(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        event: str = None,
        evidence: str = None,
        request_id: str = None,
        rewrite: str = None,
        selector: List[str] = None,
        session_id: str = None,
        sql: str = None,
        sql_error: str = None,
    ):
        self.error_message = error_message
        self.event = event
        self.evidence = evidence
        self.request_id = request_id
        self.rewrite = rewrite
        self.selector = selector
        self.session_id = session_id
        self.sql = sql
        self.sql_error = sql_error

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.event is not None:
            result['event'] = self.event
        if self.evidence is not None:
            result['evidence'] = self.evidence
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite
        if self.selector is not None:
            result['selector'] = self.selector
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.sql is not None:
            result['sql'] = self.sql
        if self.sql_error is not None:
            result['sqlError'] = self.sql_error
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('evidence') is not None:
            self.evidence = m.get('evidence')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('rewrite') is not None:
            self.rewrite = m.get('rewrite')
        if m.get('selector') is not None:
            self.selector = m.get('selector')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        if m.get('sqlError') is not None:
            self.sql_error = m.get('sqlError')
        return self


class RunSqlGenerationResponseBody(TeaModel):
    def __init__(
        self,
        data: RunSqlGenerationResponseBodyData = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = RunSqlGenerationResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class RunSqlGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunSqlGenerationResponseBody = None,
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
            temp_model = RunSqlGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveVirtualDatasourceDdlRequest(TeaModel):
    def __init__(
        self,
        ddl: str = None,
        vdb_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.ddl = ddl
        # This parameter is required.
        self.vdb_id = vdb_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['ddl'] = self.ddl
        if self.vdb_id is not None:
            result['vdbId'] = self.vdb_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ddl') is not None:
            self.ddl = m.get('ddl')
        if m.get('vdbId') is not None:
            self.vdb_id = m.get('vdbId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SaveVirtualDatasourceDdlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SaveVirtualDatasourceDdlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveVirtualDatasourceDdlResponseBody = None,
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
            temp_model = SaveVirtualDatasourceDdlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncRemoteTablesRequest(TeaModel):
    def __init__(
        self,
        keep_table_names: List[str] = None,
        no_modified_table_names: List[str] = None,
        pull_samples: bool = None,
        table_names: List[str] = None,
        workspace_id: str = None,
    ):
        self.keep_table_names = keep_table_names
        self.no_modified_table_names = no_modified_table_names
        self.pull_samples = pull_samples
        # This parameter is required.
        self.table_names = table_names
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_table_names is not None:
            result['keepTableNames'] = self.keep_table_names
        if self.no_modified_table_names is not None:
            result['noModifiedTableNames'] = self.no_modified_table_names
        if self.pull_samples is not None:
            result['pullSamples'] = self.pull_samples
        if self.table_names is not None:
            result['tableNames'] = self.table_names
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keepTableNames') is not None:
            self.keep_table_names = m.get('keepTableNames')
        if m.get('noModifiedTableNames') is not None:
            self.no_modified_table_names = m.get('noModifiedTableNames')
        if m.get('pullSamples') is not None:
            self.pull_samples = m.get('pullSamples')
        if m.get('tableNames') is not None:
            self.table_names = m.get('tableNames')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class SyncRemoteTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SyncRemoteTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncRemoteTablesResponseBody = None,
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
            temp_model = SyncRemoteTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBusinessLogicRequest(TeaModel):
    def __init__(
        self,
        business_logic_id_key: str = None,
        description: str = None,
        type: int = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.business_logic_id_key = business_logic_id_key
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_logic_id_key is not None:
            result['businessLogicIdKey'] = self.business_logic_id_key
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessLogicIdKey') is not None:
            self.business_logic_id_key = m.get('businessLogicIdKey')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class UpdateBusinessLogicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateBusinessLogicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBusinessLogicResponseBody = None,
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
            temp_model = UpdateBusinessLogicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateColumnRequest(TeaModel):
    def __init__(
        self,
        chinese_name: str = None,
        column_id_key: str = None,
        description: str = None,
        enum_type: int = None,
        enum_values: List[str] = None,
        range_max: int = None,
        range_min: int = None,
        samples: List[str] = None,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        self.chinese_name = chinese_name
        # This parameter is required.
        self.column_id_key = column_id_key
        self.description = description
        # This parameter is required.
        self.enum_type = enum_type
        self.enum_values = enum_values
        self.range_max = range_max
        self.range_min = range_min
        self.samples = samples
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_name is not None:
            result['chineseName'] = self.chinese_name
        if self.column_id_key is not None:
            result['columnIdKey'] = self.column_id_key
        if self.description is not None:
            result['description'] = self.description
        if self.enum_type is not None:
            result['enumType'] = self.enum_type
        if self.enum_values is not None:
            result['enumValues'] = self.enum_values
        if self.range_max is not None:
            result['rangeMax'] = self.range_max
        if self.range_min is not None:
            result['rangeMin'] = self.range_min
        if self.samples is not None:
            result['samples'] = self.samples
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chineseName') is not None:
            self.chinese_name = m.get('chineseName')
        if m.get('columnIdKey') is not None:
            self.column_id_key = m.get('columnIdKey')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enumType') is not None:
            self.enum_type = m.get('enumType')
        if m.get('enumValues') is not None:
            self.enum_values = m.get('enumValues')
        if m.get('rangeMax') is not None:
            self.range_max = m.get('rangeMax')
        if m.get('rangeMin') is not None:
            self.range_min = m.get('rangeMin')
        if m.get('samples') is not None:
            self.samples = m.get('samples')
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class UpdateColumnResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateColumnResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateColumnResponseBody = None,
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
            temp_model = UpdateColumnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnumMappingRequest(TeaModel):
    def __init__(
        self,
        column_id_key: str = None,
        enum_mapping: Dict[str, List[str]] = None,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.column_id_key = column_id_key
        self.enum_mapping = enum_mapping
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_id_key is not None:
            result['columnIdKey'] = self.column_id_key
        if self.enum_mapping is not None:
            result['enumMapping'] = self.enum_mapping
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnIdKey') is not None:
            self.column_id_key = m.get('columnIdKey')
        if m.get('enumMapping') is not None:
            self.enum_mapping = m.get('enumMapping')
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class UpdateEnumMappingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateEnumMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEnumMappingResponseBody = None,
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
            temp_model = UpdateEnumMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSynonymsRequest(TeaModel):
    def __init__(
        self,
        columns: List[str] = None,
        synonym_id_key: str = None,
        word: str = None,
        word_synonyms: List[str] = None,
        workspace_id: str = None,
    ):
        self.columns = columns
        # This parameter is required.
        self.synonym_id_key = synonym_id_key
        # This parameter is required.
        self.word = word
        # This parameter is required.
        self.word_synonyms = word_synonyms
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.synonym_id_key is not None:
            result['synonymIdKey'] = self.synonym_id_key
        if self.word is not None:
            result['word'] = self.word
        if self.word_synonyms is not None:
            result['wordSynonyms'] = self.word_synonyms
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('synonymIdKey') is not None:
            self.synonym_id_key = m.get('synonymIdKey')
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('wordSynonyms') is not None:
            self.word_synonyms = m.get('wordSynonyms')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class UpdateSynonymsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSynonymsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSynonymsResponseBody = None,
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
            temp_model = UpdateSynonymsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTableInfoRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        foreign_keys: List[str] = None,
        primary_key: str = None,
        table_id_key: str = None,
        workspace_id: str = None,
    ):
        self.description = description
        self.foreign_keys = foreign_keys
        self.primary_key = primary_key
        # This parameter is required.
        self.table_id_key = table_id_key
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.foreign_keys is not None:
            result['foreignKeys'] = self.foreign_keys
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key
        if self.table_id_key is not None:
            result['tableIdKey'] = self.table_id_key
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('foreignKeys') is not None:
            self.foreign_keys = m.get('foreignKeys')
        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')
        if m.get('tableIdKey') is not None:
            self.table_id_key = m.get('tableIdKey')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class UpdateTableInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateTableInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTableInfoResponseBody = None,
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
            temp_model = UpdateTableInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVirtualDatasourceInstanceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: int = None,
        vdb_id: str = None,
        workspace_id: str = None,
    ):
        self.description = description
        self.name = name
        self.type = type
        # This parameter is required.
        self.vdb_id = vdb_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.vdb_id is not None:
            result['vdbId'] = self.vdb_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('vdbId') is not None:
            self.vdb_id = m.get('vdbId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class UpdateVirtualDatasourceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateVirtualDatasourceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVirtualDatasourceInstanceResponseBody = None,
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
            temp_model = UpdateVirtualDatasourceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


