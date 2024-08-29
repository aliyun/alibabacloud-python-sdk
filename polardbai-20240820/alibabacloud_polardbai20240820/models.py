# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class OpenApiModelsPredictCmd(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PredictSseRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        input: str = None,
        instance_name: str = None,
        model_class: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.db_name = db_name
        self.input = input
        self.instance_name = instance_name
        self.model_class = model_class
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['dbName'] = self.db_name
        if self.input is not None:
            result['input'] = self.input
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.model_class is not None:
            result['modelClass'] = self.model_class
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
        if m.get('input') is not None:
            self.input = m.get('input')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('modelClass') is not None:
            self.model_class = m.get('modelClass')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class PredictSseResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
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
        if self.data is not None:
            result['data'] = self.data
        if self.err_code is not None:
            result['errCode'] = self.err_code
        if self.err_message is not None:
            result['errMessage'] = self.err_message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')
        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class PredictSseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PredictSseResponseBody = None,
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
            temp_model = PredictSseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


