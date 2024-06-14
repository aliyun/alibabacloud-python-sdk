# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class DataValue(TeaModel):
    def __init__(
        self,
        service_id: int = None,
        status: str = None,
        code: int = None,
        message: str = None,
    ):
        self.service_id = service_id
        self.status = status
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ADClockRequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_code: str = None,
    ):
        self.params = params
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADClockResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADClockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ADClockResponseBody = None,
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
            temp_model = ADClockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ADMMURequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_code: str = None,
    ):
        self.params = params
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADMMUResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADMMUResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ADMMUResponseBody = None,
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
            temp_model = ADMMUResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ADMiniCogRequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_code: str = None,
    ):
        self.params = params
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADMiniCogResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADMiniCogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ADMiniCogResponseBody = None,
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
            temp_model = ADMiniCogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ADMiniCogResultRequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_code: str = None,
    ):
        self.params = params
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class ADMiniCogResultResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ADMiniCogResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ADMiniCogResultResponseBody = None,
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
            temp_model = ADMiniCogResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceDataByConditionsRequest(TeaModel):
    def __init__(
        self,
        conditions: Dict[str, Any] = None,
        service_id: int = None,
        x_dash_scope_open_apisource: str = None,
    ):
        # This parameter is required.
        self.conditions = conditions
        # This parameter is required.
        self.service_id = service_id
        self.x_dash_scope_open_apisource = x_dash_scope_open_apisource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.x_dash_scope_open_apisource is not None:
            result['X-DashScope-OpenAPISource'] = self.x_dash_scope_open_apisource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('X-DashScope-OpenAPISource') is not None:
            self.x_dash_scope_open_apisource = m.get('X-DashScope-OpenAPISource')
        return self


class DeleteServiceDataByConditionsShrinkRequest(TeaModel):
    def __init__(
        self,
        conditions_shrink: str = None,
        service_id: int = None,
        x_dash_scope_open_apisource: str = None,
    ):
        # This parameter is required.
        self.conditions_shrink = conditions_shrink
        # This parameter is required.
        self.service_id = service_id
        self.x_dash_scope_open_apisource = x_dash_scope_open_apisource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.x_dash_scope_open_apisource is not None:
            result['X-DashScope-OpenAPISource'] = self.x_dash_scope_open_apisource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('X-DashScope-OpenAPISource') is not None:
            self.x_dash_scope_open_apisource = m.get('X-DashScope-OpenAPISource')
        return self


class DeleteServiceDataByConditionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteServiceDataByConditionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceDataByConditionsResponseBody = None,
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
            temp_model = DeleteServiceDataByConditionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceDataByIdsRequest(TeaModel):
    def __init__(
        self,
        ids: List[str] = None,
        service_id: int = None,
    ):
        # This parameter is required.
        self.ids = ids
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceDataByIdsShrinkRequest(TeaModel):
    def __init__(
        self,
        ids_shrink: str = None,
        service_id: int = None,
    ):
        # This parameter is required.
        self.ids_shrink = ids_shrink
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteServiceDataByIdsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteServiceDataByIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceDataByIdsResponseBody = None,
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
            temp_model = DeleteServiceDataByIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBrandChEcomRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        service_code: str = None,
        text: str = None,
    ):
        self.image_url = image_url
        # This parameter is required.
        self.service_code = service_code
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetBrandChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBrandChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBrandChEcomResponseBody = None,
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
            temp_model = GetBrandChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCateChEcomRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        service_code: str = None,
        text: str = None,
    ):
        self.image_url = image_url
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetCateChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCateChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCateChEcomResponseBody = None,
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
            temp_model = GetCateChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCheckDuplicationChMedicalRequest(TeaModel):
    def __init__(
        self,
        origin_q: str = None,
        origin_t: str = None,
        service_code: str = None,
    ):
        # This parameter is required.
        self.origin_q = origin_q
        # This parameter is required.
        self.origin_t = origin_t
        # This parameter is required.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_q is not None:
            result['OriginQ'] = self.origin_q
        if self.origin_t is not None:
            result['OriginT'] = self.origin_t
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginQ') is not None:
            self.origin_q = m.get('OriginQ')
        if m.get('OriginT') is not None:
            self.origin_t = m.get('OriginT')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetCheckDuplicationChMedicalResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCheckDuplicationChMedicalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCheckDuplicationChMedicalResponseBody = None,
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
            temp_model = GetCheckDuplicationChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnosisChMedicalRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        service_code: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetDiagnosisChMedicalResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDiagnosisChMedicalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDiagnosisChMedicalResponseBody = None,
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
            temp_model = GetDiagnosisChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDpChEcomRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetDpChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDpChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDpChEcomResponseBody = None,
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
            temp_model = GetDpChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDpChGeneralCTBRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetDpChGeneralCTBResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDpChGeneralCTBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDpChGeneralCTBResponseBody = None,
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
            temp_model = GetDpChGeneralCTBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDpChGeneralStanfordRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetDpChGeneralStanfordResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDpChGeneralStanfordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDpChGeneralStanfordResponseBody = None,
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
            temp_model = GetDpChGeneralStanfordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEcChGeneralRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetEcChGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEcChGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEcChGeneralResponseBody = None,
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
            temp_model = GetEcChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEcEnGeneralRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetEcEnGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEcEnGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEcEnGeneralResponseBody = None,
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
            temp_model = GetEcEnGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEmbeddingRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        text_type: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        self.text = text
        self.text_type = text_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.text_type is not None:
            result['TextType'] = self.text_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TextType') is not None:
            self.text_type = m.get('TextType')
        return self


class GetEmbeddingResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEmbeddingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEmbeddingResponseBody = None,
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
            temp_model = GetEmbeddingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemPubChEcomRequest(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        service_code: str = None,
        text: str = None,
    ):
        self.image_url = image_url
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetItemPubChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetItemPubChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetItemPubChEcomResponseBody = None,
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
            temp_model = GetItemPubChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKeywordChEcomRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        service_code: str = None,
        text: str = None,
    ):
        self.api_version = api_version
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetKeywordChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetKeywordChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKeywordChEcomResponseBody = None,
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
            temp_model = GetKeywordChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKeywordEnEcomRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetKeywordEnEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetKeywordEnEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKeywordEnEcomResponseBody = None,
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
            temp_model = GetKeywordEnEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMedicineChMedicalRequest(TeaModel):
    def __init__(
        self,
        factory: str = None,
        name: str = None,
        service_code: str = None,
        specification: str = None,
        unit: str = None,
    ):
        self.factory = factory
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.service_code = service_code
        self.specification = specification
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory is not None:
            result['Factory'] = self.factory
        if self.name is not None:
            result['Name'] = self.name
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Factory') is not None:
            self.factory = m.get('Factory')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class GetMedicineChMedicalResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMedicineChMedicalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMedicineChMedicalResponseBody = None,
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
            temp_model = GetMedicineChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerChEcomRequest(TeaModel):
    def __init__(
        self,
        lexer_id: str = None,
        service_code: str = None,
        text: str = None,
    ):
        self.lexer_id = lexer_id
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lexer_id is not None:
            result['LexerId'] = self.lexer_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LexerId') is not None:
            self.lexer_id = m.get('LexerId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNerChEcomResponseBody = None,
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
            temp_model = GetNerChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerChMedicalRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerChMedicalResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerChMedicalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNerChMedicalResponseBody = None,
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
            temp_model = GetNerChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerCustomizedChEcomRequest(TeaModel):
    def __init__(
        self,
        lexer_id: str = None,
        service_code: str = None,
        text: str = None,
    ):
        self.lexer_id = lexer_id
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lexer_id is not None:
            result['LexerId'] = self.lexer_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LexerId') is not None:
            self.lexer_id = m.get('LexerId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerCustomizedChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerCustomizedChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNerCustomizedChEcomResponseBody = None,
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
            temp_model = GetNerCustomizedChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNerCustomizedSeaEcomRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.language = language
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetNerCustomizedSeaEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNerCustomizedSeaEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNerCustomizedSeaEcomResponseBody = None,
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
            temp_model = GetNerCustomizedSeaEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenNLURequest(TeaModel):
    def __init__(
        self,
        examples: str = None,
        labels: str = None,
        sentence: str = None,
        service_code: str = None,
        task: str = None,
    ):
        self.examples = examples
        self.labels = labels
        self.sentence = sentence
        # This parameter is required.
        self.service_code = service_code
        self.task = task

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.examples is not None:
            result['Examples'] = self.examples
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.sentence is not None:
            result['Sentence'] = self.sentence
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.task is not None:
            result['Task'] = self.task
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Examples') is not None:
            self.examples = m.get('Examples')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Sentence') is not None:
            self.sentence = m.get('Sentence')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        return self


class GetOpenNLUResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOpenNLUResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOpenNLUResponseBody = None,
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
            temp_model = GetOpenNLUResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpenNLUHighRecallRequest(TeaModel):
    def __init__(
        self,
        examples: str = None,
        labels: str = None,
        sentence: str = None,
        service_code: str = None,
        task: str = None,
    ):
        self.examples = examples
        self.labels = labels
        self.sentence = sentence
        # This parameter is required.
        self.service_code = service_code
        self.task = task

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.examples is not None:
            result['Examples'] = self.examples
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.sentence is not None:
            result['Sentence'] = self.sentence
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.task is not None:
            result['Task'] = self.task
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Examples') is not None:
            self.examples = m.get('Examples')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Sentence') is not None:
            self.sentence = m.get('Sentence')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        return self


class GetOpenNLUHighRecallResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOpenNLUHighRecallResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOpenNLUHighRecallResponseBody = None,
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
            temp_model = GetOpenNLUHighRecallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOperationChMedicalRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        service_code: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetOperationChMedicalResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOperationChMedicalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOperationChMedicalResponseBody = None,
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
            temp_model = GetOperationChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPosChEcomRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetPosChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPosChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPosChEcomResponseBody = None,
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
            temp_model = GetPosChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPosChGeneralRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetPosChGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPosChGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPosChGeneralResponseBody = None,
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
            temp_model = GetPosChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPriceChEcomRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetPriceChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPriceChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPriceChEcomResponseBody = None,
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
            temp_model = GetPriceChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSSETestRequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_code: str = None,
    ):
        self.params = params
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetSSETestResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSSETestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSSETestResponseBody = None,
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
            temp_model = GetSSETestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSaChGeneralRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSaChGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSaChGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSaChGeneralResponseBody = None,
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
            temp_model = GetSaChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSaSeaEcomRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.language = language
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSaSeaEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSaSeaEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSaSeaEcomResponseBody = None,
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
            temp_model = GetSaSeaEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceDataImportStatusRequest(TeaModel):
    def __init__(
        self,
        data_import_ids: List[int] = None,
    ):
        # This parameter is required.
        self.data_import_ids = data_import_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_import_ids is not None:
            result['DataImportIds'] = self.data_import_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataImportIds') is not None:
            self.data_import_ids = m.get('DataImportIds')
        return self


class GetServiceDataImportStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        data_import_ids_shrink: str = None,
    ):
        # This parameter is required.
        self.data_import_ids_shrink = data_import_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_import_ids_shrink is not None:
            result['DataImportIds'] = self.data_import_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataImportIds') is not None:
            self.data_import_ids_shrink = m.get('DataImportIds')
        return self


class GetServiceDataImportStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, DataValue] = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v in self.data.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                result['Data'][k] = v.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = {}
        if m.get('Data') is not None:
            for k, v in m.get('Data').items():
                temp_model = DataValue()
                self.data[k] = temp_model.from_map(v)
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetServiceDataImportStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceDataImportStatusResponseBody = None,
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
            temp_model = GetServiceDataImportStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSimilarityChMedicalRequest(TeaModel):
    def __init__(
        self,
        origin_q: str = None,
        origin_t: str = None,
        service_code: str = None,
    ):
        # This parameter is required.
        self.origin_q = origin_q
        # This parameter is required.
        self.origin_t = origin_t
        # This parameter is required.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_q is not None:
            result['OriginQ'] = self.origin_q
        if self.origin_t is not None:
            result['OriginT'] = self.origin_t
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginQ') is not None:
            self.origin_q = m.get('OriginQ')
        if m.get('OriginT') is not None:
            self.origin_t = m.get('OriginT')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetSimilarityChMedicalResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSimilarityChMedicalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSimilarityChMedicalResponseBody = None,
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
            temp_model = GetSimilarityChMedicalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSummaryChEcomRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSummaryChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSummaryChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSummaryChEcomResponseBody = None,
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
            temp_model = GetSummaryChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableQAServiceInfoByIdRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        service_id: str = None,
    ):
        self.service_code = service_code
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetTableQAServiceInfoByIdResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTableQAServiceInfoByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTableQAServiceInfoByIdResponseBody = None,
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
            temp_model = GetTableQAServiceInfoByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTcChEcomRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetTcChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTcChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTcChEcomResponseBody = None,
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
            temp_model = GetTcChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTcChGeneralRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetTcChGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTcChGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTcChGeneralResponseBody = None,
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
            temp_model = GetTcChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTsChEcomRequest(TeaModel):
    def __init__(
        self,
        origin_q: str = None,
        origin_t: str = None,
        service_code: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.origin_q = origin_q
        # This parameter is required.
        self.origin_t = origin_t
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_q is not None:
            result['OriginQ'] = self.origin_q
        if self.origin_t is not None:
            result['OriginT'] = self.origin_t
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginQ') is not None:
            self.origin_q = m.get('OriginQ')
        if m.get('OriginT') is not None:
            self.origin_t = m.get('OriginT')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTsChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTsChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTsChEcomResponseBody = None,
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
            temp_model = GetTsChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserUploadSignRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
    ):
        # This parameter is required.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class GetUserUploadSignResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserUploadSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserUploadSignResponseBody = None,
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
            temp_model = GetUserUploadSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChCommentRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        service_code: str = None,
        size: str = None,
        text: str = None,
        tokenizer_id: str = None,
        type: str = None,
    ):
        self.operation = operation
        # This parameter is required.
        self.service_code = service_code
        self.size = size
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.tokenizer_id = tokenizer_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChCommentResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWeChCommentResponseBody = None,
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
            temp_model = GetWeChCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChEcomRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        service_code: str = None,
        size: str = None,
        text: str = None,
        tokenizer_id: str = None,
        type: str = None,
    ):
        self.operation = operation
        # This parameter is required.
        self.service_code = service_code
        self.size = size
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.tokenizer_id = tokenizer_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWeChEcomResponseBody = None,
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
            temp_model = GetWeChEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChEntertainmentRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        service_code: str = None,
        size: str = None,
        text: str = None,
        tokenizer_id: str = None,
        type: str = None,
    ):
        self.operation = operation
        # This parameter is required.
        self.service_code = service_code
        self.size = size
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.tokenizer_id = tokenizer_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChEntertainmentResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChEntertainmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWeChEntertainmentResponseBody = None,
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
            temp_model = GetWeChEntertainmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChGeneralRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        service_code: str = None,
        size: str = None,
        text: str = None,
        type: str = None,
    ):
        self.operation = operation
        # This parameter is required.
        self.service_code = service_code
        self.size = size
        # This parameter is required.
        self.text = text
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWeChGeneralResponseBody = None,
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
            temp_model = GetWeChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeChSearchRequest(TeaModel):
    def __init__(
        self,
        operation: str = None,
        service_code: str = None,
        size: str = None,
        text: str = None,
        tokenizer_id: str = None,
        type: str = None,
    ):
        self.operation = operation
        # This parameter is required.
        self.service_code = service_code
        self.size = size
        # This parameter is required.
        self.text = text
        # This parameter is required.
        self.tokenizer_id = tokenizer_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.size is not None:
            result['Size'] = self.size
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetWeChSearchResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWeChSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWeChSearchResponseBody = None,
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
            temp_model = GetWeChSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsChGeneralRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsChGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsChGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsChGeneralResponseBody = None,
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
            temp_model = GetWsChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEcomCommentRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEcomCommentResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEcomCommentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedChEcomCommentResponseBody = None,
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
            temp_model = GetWsCustomizedChEcomCommentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEcomContentRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEcomContentResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEcomContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedChEcomContentResponseBody = None,
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
            temp_model = GetWsCustomizedChEcomContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEcomTitleRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEcomTitleResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEcomTitleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedChEcomTitleResponseBody = None,
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
            temp_model = GetWsCustomizedChEcomTitleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChEntertainmentRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChEntertainmentResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChEntertainmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedChEntertainmentResponseBody = None,
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
            temp_model = GetWsCustomizedChEntertainmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChGeneralRequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedChGeneralResponseBody = None,
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
            temp_model = GetWsCustomizedChGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedChO2ORequest(TeaModel):
    def __init__(
        self,
        out_type: str = None,
        service_code: str = None,
        text: str = None,
        tokenizer_id: str = None,
    ):
        self.out_type = out_type
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text
        self.tokenizer_id = tokenizer_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_type is not None:
            result['OutType'] = self.out_type
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.tokenizer_id is not None:
            result['TokenizerId'] = self.tokenizer_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TokenizerId') is not None:
            self.tokenizer_id = m.get('TokenizerId')
        return self


class GetWsCustomizedChO2OResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedChO2OResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedChO2OResponseBody = None,
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
            temp_model = GetWsCustomizedChO2OResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedSeaEcomRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.language = language
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetWsCustomizedSeaEcomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedSeaEcomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedSeaEcomResponseBody = None,
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
            temp_model = GetWsCustomizedSeaEcomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWsCustomizedSeaGeneralRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        service_code: str = None,
        text: str = None,
    ):
        # This parameter is required.
        self.language = language
        # This parameter is required.
        self.service_code = service_code
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetWsCustomizedSeaGeneralResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetWsCustomizedSeaGeneralResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWsCustomizedSeaGeneralResponseBody = None,
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
            temp_model = GetWsCustomizedSeaGeneralResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportServiceDataRequest(TeaModel):
    def __init__(
        self,
        partition: List[Dict[str, str]] = None,
        service_id: int = None,
        sub_path: str = None,
        url: str = None,
    ):
        self.partition = partition
        # This parameter is required.
        self.service_id = service_id
        self.sub_path = sub_path
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ImportServiceDataShrinkRequest(TeaModel):
    def __init__(
        self,
        partition_shrink: str = None,
        service_id: int = None,
        sub_path: str = None,
        url: str = None,
    ):
        self.partition_shrink = partition_shrink
        # This parameter is required.
        self.service_id = service_id
        self.sub_path = sub_path
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partition_shrink is not None:
            result['Partition'] = self.partition_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sub_path is not None:
            result['SubPath'] = self.sub_path
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Partition') is not None:
            self.partition_shrink = m.get('Partition')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ImportServiceDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportServiceDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportServiceDataResponseBody = None,
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
            temp_model = ImportServiceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportServiceDataV2RequestDocuments(TeaModel):
    def __init__(
        self,
        biz_params: Dict[str, str] = None,
        doc_id: str = None,
        file_extension: str = None,
        file_name: str = None,
        file_path: str = None,
        version: str = None,
    ):
        self.biz_params = biz_params
        self.doc_id = doc_id
        self.file_extension = file_extension
        self.file_name = file_name
        self.file_path = file_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ImportServiceDataV2Request(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        documents: List[ImportServiceDataV2RequestDocuments] = None,
        service_id: int = None,
    ):
        self.data_type = data_type
        self.documents = documents
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = ImportServiceDataV2RequestDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ImportServiceDataV2ShrinkRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        documents_shrink: str = None,
        service_id: int = None,
    ):
        self.data_type = data_type
        self.documents_shrink = documents_shrink
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ImportServiceDataV2ResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportServiceDataV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportServiceDataV2ResponseBody = None,
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
            temp_model = ImportServiceDataV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertCustomRequest(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        custom_file_name: str = None,
        custom_url: str = None,
        reg_file_name: str = None,
        reg_url: str = None,
        service_code: str = None,
    ):
        # This parameter is required.
        self.api_id = api_id
        self.custom_file_name = custom_file_name
        self.custom_url = custom_url
        self.reg_file_name = reg_file_name
        self.reg_url = reg_url
        # This parameter is required.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.custom_file_name is not None:
            result['CustomFileName'] = self.custom_file_name
        if self.custom_url is not None:
            result['CustomUrl'] = self.custom_url
        if self.reg_file_name is not None:
            result['RegFileName'] = self.reg_file_name
        if self.reg_url is not None:
            result['RegUrl'] = self.reg_url
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('CustomFileName') is not None:
            self.custom_file_name = m.get('CustomFileName')
        if m.get('CustomUrl') is not None:
            self.custom_url = m.get('CustomUrl')
        if m.get('RegFileName') is not None:
            self.reg_file_name = m.get('RegFileName')
        if m.get('RegUrl') is not None:
            self.reg_url = m.get('RegUrl')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class InsertCustomResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InsertCustomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertCustomResponseBody = None,
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
            temp_model = InsertCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenAlinlpServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenAlinlpServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenAlinlpServiceResponseBody = None,
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
            temp_model = OpenAlinlpServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostISConvRewriterRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        debug: bool = None,
        input: Dict[str, Any] = None,
        model: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.algorithm = algorithm
        self.debug = debug
        self.input = input
        self.model = model
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input is not None:
            result['Input'] = self.input
        if self.model is not None:
            result['Model'] = self.model
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class PostISConvRewriterShrinkRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        debug: bool = None,
        input_shrink: str = None,
        model: str = None,
        parameters_shrink: str = None,
    ):
        self.algorithm = algorithm
        self.debug = debug
        self.input_shrink = input_shrink
        self.model = model
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.model is not None:
            result['Model'] = self.model
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class PostISConvRewriterResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        debug_info: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        status: int = None,
    ):
        self.data = data
        self.debug_info = debug_info
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostISConvRewriterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostISConvRewriterResponseBody = None,
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
            temp_model = PostISConvRewriterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostISRerankRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        debug: bool = None,
        input: Dict[str, Any] = None,
        model: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.algorithm = algorithm
        self.debug = debug
        self.input = input
        self.model = model
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input is not None:
            result['Input'] = self.input
        if self.model is not None:
            result['Model'] = self.model
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class PostISRerankShrinkRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        debug: bool = None,
        input_shrink: str = None,
        model: str = None,
        parameters_shrink: str = None,
    ):
        self.algorithm = algorithm
        self.debug = debug
        self.input_shrink = input_shrink
        self.model = model
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.model is not None:
            result['Model'] = self.model
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class PostISRerankResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        debug_info: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        status: int = None,
    ):
        self.data = data
        self.debug_info = debug_info
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostISRerankResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostISRerankResponseBody = None,
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
            temp_model = PostISRerankResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostISRetrieveRouterRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        debug: bool = None,
        input: Dict[str, Any] = None,
        model: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.algorithm = algorithm
        self.debug = debug
        self.input = input
        self.model = model
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input is not None:
            result['Input'] = self.input
        if self.model is not None:
            result['Model'] = self.model
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input = m.get('Input')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class PostISRetrieveRouterShrinkRequest(TeaModel):
    def __init__(
        self,
        algorithm: str = None,
        debug: bool = None,
        input_shrink: str = None,
        model: str = None,
        parameters_shrink: str = None,
    ):
        self.algorithm = algorithm
        self.debug = debug
        self.input_shrink = input_shrink
        self.model = model
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.model is not None:
            result['Model'] = self.model
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class PostISRetrieveRouterResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        debug_info: Dict[str, Any] = None,
        message: str = None,
        request_id: str = None,
        status: int = None,
    ):
        self.data = data
        self.debug_info = debug_info
        self.message = message
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.debug_info is not None:
            result['DebugInfo'] = self.debug_info
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DebugInfo') is not None:
            self.debug_info = m.get('DebugInfo')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostISRetrieveRouterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostISRetrieveRouterResponseBody = None,
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
            temp_model = PostISRetrieveRouterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSConvSearchTokenGeneratedResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSConvSearchTokenGeneratedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostMSConvSearchTokenGeneratedResponseBody = None,
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
            temp_model = PostMSConvSearchTokenGeneratedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSDataProcessingCountRequest(TeaModel):
    def __init__(
        self,
        data_ids: List[str] = None,
        data_import_id: int = None,
        service_id: int = None,
        x_dash_scope_open_apisource: str = None,
    ):
        self.data_ids = data_ids
        self.data_import_id = data_import_id
        self.service_id = service_id
        self.x_dash_scope_open_apisource = x_dash_scope_open_apisource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ids is not None:
            result['DataIds'] = self.data_ids
        if self.data_import_id is not None:
            result['DataImportId'] = self.data_import_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.x_dash_scope_open_apisource is not None:
            result['X-DashScope-OpenAPISource'] = self.x_dash_scope_open_apisource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIds') is not None:
            self.data_ids = m.get('DataIds')
        if m.get('DataImportId') is not None:
            self.data_import_id = m.get('DataImportId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('X-DashScope-OpenAPISource') is not None:
            self.x_dash_scope_open_apisource = m.get('X-DashScope-OpenAPISource')
        return self


class PostMSDataProcessingCountShrinkRequest(TeaModel):
    def __init__(
        self,
        data_ids_shrink: str = None,
        data_import_id: int = None,
        service_id: int = None,
        x_dash_scope_open_apisource: str = None,
    ):
        self.data_ids_shrink = data_ids_shrink
        self.data_import_id = data_import_id
        self.service_id = service_id
        self.x_dash_scope_open_apisource = x_dash_scope_open_apisource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_ids_shrink is not None:
            result['DataIds'] = self.data_ids_shrink
        if self.data_import_id is not None:
            result['DataImportId'] = self.data_import_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.x_dash_scope_open_apisource is not None:
            result['X-DashScope-OpenAPISource'] = self.x_dash_scope_open_apisource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIds') is not None:
            self.data_ids_shrink = m.get('DataIds')
        if m.get('DataImportId') is not None:
            self.data_import_id = m.get('DataImportId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('X-DashScope-OpenAPISource') is not None:
            self.x_dash_scope_open_apisource = m.get('X-DashScope-OpenAPISource')
        return self


class PostMSDataProcessingCountResponseBodyDataDataProcessedStatusesErrorDataList(TeaModel):
    def __init__(
        self,
        count: int = None,
        error_code: str = None,
        op_type: str = None,
    ):
        self.count = count
        self.error_code = error_code
        self.op_type = op_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.op_type is not None:
            result['OpType'] = self.op_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')
        return self


class PostMSDataProcessingCountResponseBodyDataDataProcessedStatuses(TeaModel):
    def __init__(
        self,
        chunk_num: str = None,
        data_id: str = None,
        error_data_list: List[PostMSDataProcessingCountResponseBodyDataDataProcessedStatusesErrorDataList] = None,
        op_status: Dict[str, int] = None,
        status: str = None,
        version_value: str = None,
    ):
        self.chunk_num = chunk_num
        self.data_id = data_id
        self.error_data_list = error_data_list
        self.op_status = op_status
        self.status = status
        self.version_value = version_value

    def validate(self):
        if self.error_data_list:
            for k in self.error_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chunk_num is not None:
            result['ChunkNum'] = self.chunk_num
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['ErrorDataList'] = []
        if self.error_data_list is not None:
            for k in self.error_data_list:
                result['ErrorDataList'].append(k.to_map() if k else None)
        if self.op_status is not None:
            result['OpStatus'] = self.op_status
        if self.status is not None:
            result['Status'] = self.status
        if self.version_value is not None:
            result['VersionValue'] = self.version_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkNum') is not None:
            self.chunk_num = m.get('ChunkNum')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.error_data_list = []
        if m.get('ErrorDataList') is not None:
            for k in m.get('ErrorDataList'):
                temp_model = PostMSDataProcessingCountResponseBodyDataDataProcessedStatusesErrorDataList()
                self.error_data_list.append(temp_model.from_map(k))
        if m.get('OpStatus') is not None:
            self.op_status = m.get('OpStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionValue') is not None:
            self.version_value = m.get('VersionValue')
        return self


class PostMSDataProcessingCountResponseBodyData(TeaModel):
    def __init__(
        self,
        data_processed_statuses: List[PostMSDataProcessingCountResponseBodyDataDataProcessedStatuses] = None,
        status: str = None,
    ):
        self.data_processed_statuses = data_processed_statuses
        self.status = status

    def validate(self):
        if self.data_processed_statuses:
            for k in self.data_processed_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataProcessedStatuses'] = []
        if self.data_processed_statuses is not None:
            for k in self.data_processed_statuses:
                result['DataProcessedStatuses'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_processed_statuses = []
        if m.get('DataProcessedStatuses') is not None:
            for k in m.get('DataProcessedStatuses'):
                temp_model = PostMSDataProcessingCountResponseBodyDataDataProcessedStatuses()
                self.data_processed_statuses.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class PostMSDataProcessingCountResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: PostMSDataProcessingCountResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = PostMSDataProcessingCountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSDataProcessingCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostMSDataProcessingCountResponseBody = None,
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
            temp_model = PostMSDataProcessingCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSSearchEnhanceRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        custom_config_info: Dict[str, Any] = None,
        debug: bool = None,
        fields: List[str] = None,
        filters: str = None,
        min_score: float = None,
        page: int = None,
        queries: str = None,
        rank_model_info: Dict[str, Any] = None,
        rows: int = None,
        service_id: int = None,
        sort: List[str] = None,
        type: str = None,
        uq: str = None,
        x_dash_scope_open_apisource: str = None,
    ):
        self.body = body
        self.custom_config_info = custom_config_info
        self.debug = debug
        self.fields = fields
        self.filters = filters
        self.min_score = min_score
        self.page = page
        self.queries = queries
        self.rank_model_info = rank_model_info
        self.rows = rows
        self.service_id = service_id
        self.sort = sort
        self.type = type
        self.uq = uq
        self.x_dash_scope_open_apisource = x_dash_scope_open_apisource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.custom_config_info is not None:
            result['CustomConfigInfo'] = self.custom_config_info
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.page is not None:
            result['Page'] = self.page
        if self.queries is not None:
            result['Queries'] = self.queries
        if self.rank_model_info is not None:
            result['RankModelInfo'] = self.rank_model_info
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.type is not None:
            result['Type'] = self.type
        if self.uq is not None:
            result['Uq'] = self.uq
        if self.x_dash_scope_open_apisource is not None:
            result['X-DashScope-OpenAPISource'] = self.x_dash_scope_open_apisource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('CustomConfigInfo') is not None:
            self.custom_config_info = m.get('CustomConfigInfo')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Queries') is not None:
            self.queries = m.get('Queries')
        if m.get('RankModelInfo') is not None:
            self.rank_model_info = m.get('RankModelInfo')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uq') is not None:
            self.uq = m.get('Uq')
        if m.get('X-DashScope-OpenAPISource') is not None:
            self.x_dash_scope_open_apisource = m.get('X-DashScope-OpenAPISource')
        return self


class PostMSSearchEnhanceShrinkRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        custom_config_info_shrink: str = None,
        debug: bool = None,
        fields_shrink: str = None,
        filters: str = None,
        min_score: float = None,
        page: int = None,
        queries: str = None,
        rank_model_info_shrink: str = None,
        rows: int = None,
        service_id: int = None,
        sort_shrink: str = None,
        type: str = None,
        uq: str = None,
        x_dash_scope_open_apisource: str = None,
    ):
        self.body = body
        self.custom_config_info_shrink = custom_config_info_shrink
        self.debug = debug
        self.fields_shrink = fields_shrink
        self.filters = filters
        self.min_score = min_score
        self.page = page
        self.queries = queries
        self.rank_model_info_shrink = rank_model_info_shrink
        self.rows = rows
        self.service_id = service_id
        self.sort_shrink = sort_shrink
        self.type = type
        self.uq = uq
        self.x_dash_scope_open_apisource = x_dash_scope_open_apisource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.custom_config_info_shrink is not None:
            result['CustomConfigInfo'] = self.custom_config_info_shrink
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.fields_shrink is not None:
            result['Fields'] = self.fields_shrink
        if self.filters is not None:
            result['Filters'] = self.filters
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.page is not None:
            result['Page'] = self.page
        if self.queries is not None:
            result['Queries'] = self.queries
        if self.rank_model_info_shrink is not None:
            result['RankModelInfo'] = self.rank_model_info_shrink
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.sort_shrink is not None:
            result['Sort'] = self.sort_shrink
        if self.type is not None:
            result['Type'] = self.type
        if self.uq is not None:
            result['Uq'] = self.uq
        if self.x_dash_scope_open_apisource is not None:
            result['X-DashScope-OpenAPISource'] = self.x_dash_scope_open_apisource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('CustomConfigInfo') is not None:
            self.custom_config_info_shrink = m.get('CustomConfigInfo')
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Fields') is not None:
            self.fields_shrink = m.get('Fields')
        if m.get('Filters') is not None:
            self.filters = m.get('Filters')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Queries') is not None:
            self.queries = m.get('Queries')
        if m.get('RankModelInfo') is not None:
            self.rank_model_info_shrink = m.get('RankModelInfo')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Sort') is not None:
            self.sort_shrink = m.get('Sort')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uq') is not None:
            self.uq = m.get('Uq')
        if m.get('X-DashScope-OpenAPISource') is not None:
            self.x_dash_scope_open_apisource = m.get('X-DashScope-OpenAPISource')
        return self


class PostMSSearchEnhanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
        # Id of the request
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSSearchEnhanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostMSSearchEnhanceResponseBody = None,
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
            temp_model = PostMSSearchEnhanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PostMSServiceDataImportRequestDocuments(TeaModel):
    def __init__(
        self,
        biz_params: Dict[str, Any] = None,
        doc_id: str = None,
        file_extension: str = None,
        file_name: str = None,
        file_path: str = None,
        version: str = None,
    ):
        self.biz_params = biz_params
        self.doc_id = doc_id
        self.file_extension = file_extension
        self.file_name = file_name
        self.file_path = file_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizParams') is not None:
            self.biz_params = m.get('BizParams')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class PostMSServiceDataImportRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        documents: List[PostMSServiceDataImportRequestDocuments] = None,
        service_id: int = None,
    ):
        self.data_type = data_type
        self.documents = documents
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = PostMSServiceDataImportRequestDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class PostMSServiceDataImportShrinkRequest(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        documents_shrink: str = None,
        service_id: int = None,
    ):
        self.data_type = data_type
        self.documents_shrink = documents_shrink
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class PostMSServiceDataImportResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PostMSServiceDataImportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PostMSServiceDataImportResponseBody = None,
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
            temp_model = PostMSServiceDataImportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestTableQARequest(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_code: str = None,
    ):
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RequestTableQAResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RequestTableQAResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RequestTableQAResponseBody = None,
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
            temp_model = RequestTableQAResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestTableQAOnlineRequest(TeaModel):
    def __init__(
        self,
        bot_id: str = None,
        params: str = None,
        question: str = None,
        service_code: str = None,
    ):
        self.bot_id = bot_id
        self.params = params
        self.question = question
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot_id is not None:
            result['BotId'] = self.bot_id
        if self.params is not None:
            result['Params'] = self.params
        if self.question is not None:
            result['Question'] = self.question
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Question') is not None:
            self.question = m.get('Question')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class RequestTableQAOnlineResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RequestTableQAOnlineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RequestTableQAOnlineResponseBody = None,
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
            temp_model = RequestTableQAOnlineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceDataRequest(TeaModel):
    def __init__(
        self,
        conditions: Dict[str, Any] = None,
        service_id: int = None,
    ):
        # This parameter is required.
        self.conditions = conditions
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions is not None:
            result['Conditions'] = self.conditions
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateServiceDataShrinkRequest(TeaModel):
    def __init__(
        self,
        conditions_shrink: str = None,
        service_id: int = None,
    ):
        # This parameter is required.
        self.conditions_shrink = conditions_shrink
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conditions_shrink is not None:
            result['Conditions'] = self.conditions_shrink
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conditions') is not None:
            self.conditions_shrink = m.get('Conditions')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateServiceDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateServiceDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceDataResponseBody = None,
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
            temp_model = UpdateServiceDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


