# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class DataStreamMapping(TeaModel):
    def __init__(
        self,
        case_sensitive: bool = None,
        doc_values: bool = None,
        index: bool = None,
        key: str = None,
        properties: List['DataStreamMapping'] = None,
        tokenize_on_chars: List[str] = None,
        type: str = None,
    ):
        self.case_sensitive = case_sensitive
        self.doc_values = doc_values
        self.index = index
        self.key = key
        self.properties = properties
        self.tokenize_on_chars = tokenize_on_chars
        self.type = type

    def validate(self):
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive
        if self.doc_values is not None:
            result['docValues'] = self.doc_values
        if self.index is not None:
            result['index'] = self.index
        if self.key is not None:
            result['key'] = self.key
        result['properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['properties'].append(k.to_map() if k else None)
        if self.tokenize_on_chars is not None:
            result['tokenizeOnChars'] = self.tokenize_on_chars
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')
        if m.get('docValues') is not None:
            self.doc_values = m.get('docValues')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('key') is not None:
            self.key = m.get('key')
        self.properties = []
        if m.get('properties') is not None:
            for k in m.get('properties'):
                temp_model = DataStreamMapping()
                self.properties.append(temp_model.from_map(k))
        if m.get('tokenizeOnChars') is not None:
            self.tokenize_on_chars = m.get('tokenizeOnChars')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        charge_type: str = None,
        description: str = None,
    ):
        # 应用名
        self.app_name = app_name
        self.charge_type = charge_type
        # 应用备注
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateAppResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataStreamRequestTemplate(TeaModel):
    def __init__(
        self,
        mappings: List[DataStreamMapping] = None,
    ):
        # 索引字段设置
        self.mappings = mappings

    def validate(self):
        if self.mappings:
            for k in self.mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mappings'] = []
        if self.mappings is not None:
            for k in self.mappings:
                result['mappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mappings = []
        if m.get('mappings') is not None:
            for k in m.get('mappings'):
                temp_model = DataStreamMapping()
                self.mappings.append(temp_model.from_map(k))
        return self


class CreateDataStreamRequest(TeaModel):
    def __init__(
        self,
        data_stream_name: str = None,
        delete_phase: str = None,
        dynamic: str = None,
        region_id: str = None,
        template: CreateDataStreamRequestTemplate = None,
        time_stamp_key: str = None,
        type: str = None,
    ):
        # 代表资源名称的资源属性字段
        self.data_stream_name = data_stream_name
        # 删除时间
        self.delete_phase = delete_phase
        self.dynamic = dynamic
        self.region_id = region_id
        # 数据流模板
        self.template = template
        self.time_stamp_key = time_stamp_key
        # 数据流类型
        self.type = type

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream_name is not None:
            result['dataStreamName'] = self.data_stream_name
        if self.delete_phase is not None:
            result['deletePhase'] = self.delete_phase
        if self.dynamic is not None:
            result['dynamic'] = self.dynamic
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.time_stamp_key is not None:
            result['timeStampKey'] = self.time_stamp_key
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStreamName') is not None:
            self.data_stream_name = m.get('dataStreamName')
        if m.get('deletePhase') is not None:
            self.delete_phase = m.get('deletePhase')
        if m.get('dynamic') is not None:
            self.dynamic = m.get('dynamic')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('template') is not None:
            temp_model = CreateDataStreamRequestTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('timeStampKey') is not None:
            self.time_stamp_key = m.get('timeStampKey')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateDataStreamResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateDataStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataStreamResponseBody = None,
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
            temp_model = CreateDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessTokenResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccessTokenResponseBody = None,
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
            temp_model = DeleteAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: DeleteAppResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = DeleteAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DeleteDataStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataStreamResponseBody = None,
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
            temp_model = DeleteDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescibeRegionsResponseBodyResult(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        local_name: str = None,
        region_id: str = None,
    ):
        self.endpoint = endpoint
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.local_name is not None:
            result['localName'] = self.local_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('localName') is not None:
            self.local_name = m.get('localName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class DescibeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[DescibeRegionsResponseBodyResult] = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = DescibeRegionsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescibeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescibeRegionsResponseBody = None,
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
            temp_model = DescibeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAccessTokenResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DisableAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAccessTokenResponseBody = None,
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
            temp_model = DisableAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableAccessTokenResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class EnableAccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableAccessTokenResponseBody = None,
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
            temp_model = EnableAccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateAcccessTokenResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GenerateAcccessTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateAcccessTokenResponseBody = None,
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
            temp_model = GenerateAcccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        description: str = None,
        flow_quota: str = None,
        owner_id: str = None,
        region_id: str = None,
        status: str = None,
        storage_quota: str = None,
    ):
        # 代表资源名称的资源属性字段
        self.app_name = app_name
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 应用备注
        self.description = description
        # 流量限流额
        self.flow_quota = flow_quota
        # OwnerID账号ID
        self.owner_id = owner_id
        # 代表region的资源属性字段
        self.region_id = region_id
        # 代表资源状态的资源属性字段
        self.status = status
        # 存储限流额
        self.storage_quota = storage_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.flow_quota is not None:
            result['flowQuota'] = self.flow_quota
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.storage_quota is not None:
            result['storageQuota'] = self.storage_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('flowQuota') is not None:
            self.flow_quota = m.get('flowQuota')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('storageQuota') is not None:
            self.storage_quota = m.get('storageQuota')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAppResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetAppResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppResponseBody = None,
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataStreamResponseBodyResultTemplate(TeaModel):
    def __init__(
        self,
        mappings: List[DataStreamMapping] = None,
    ):
        # 索引字段设置
        self.mappings = mappings

    def validate(self):
        if self.mappings:
            for k in self.mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mappings'] = []
        if self.mappings is not None:
            for k in self.mappings:
                result['mappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mappings = []
        if m.get('mappings') is not None:
            for k in m.get('mappings'):
                temp_model = DataStreamMapping()
                self.mappings.append(temp_model.from_map(k))
        return self


class GetDataStreamResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        data_stream_id: str = None,
        data_stream_name: str = None,
        delete_phase: str = None,
        region_id: str = None,
        template: GetDataStreamResponseBodyResultTemplate = None,
        time_stamp_key: str = None,
        type: str = None,
    ):
        # 关联的应用AppId
        self.app_name = app_name
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 代表资源一级ID的资源属性字段
        self.data_stream_id = data_stream_id
        # 代表资源名称的资源属性字段
        self.data_stream_name = data_stream_name
        # 删除时间
        self.delete_phase = delete_phase
        # 代表region的资源属性字段
        self.region_id = region_id
        # 数据流模板
        self.template = template
        self.time_stamp_key = time_stamp_key
        # 数据流类型
        self.type = type

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_stream_id is not None:
            result['dataStreamId'] = self.data_stream_id
        if self.data_stream_name is not None:
            result['dataStreamName'] = self.data_stream_name
        if self.delete_phase is not None:
            result['deletePhase'] = self.delete_phase
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.time_stamp_key is not None:
            result['timeStampKey'] = self.time_stamp_key
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataStreamId') is not None:
            self.data_stream_id = m.get('dataStreamId')
        if m.get('dataStreamName') is not None:
            self.data_stream_name = m.get('dataStreamName')
        if m.get('deletePhase') is not None:
            self.delete_phase = m.get('deletePhase')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('template') is not None:
            temp_model = GetDataStreamResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('timeStampKey') is not None:
            self.time_stamp_key = m.get('timeStampKey')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetDataStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetDataStreamResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = GetDataStreamResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class GetDataStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataStreamResponseBody = None,
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
            temp_model = GetDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionInfoResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRegionInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegionInfoResponseBody = None,
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
            temp_model = GetRegionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessTokensRequest(TeaModel):
    def __init__(
        self,
        token_id: str = None,
    ):
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        return self


class ListAccessTokensResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListAccessTokensResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccessTokensResponseBody = None,
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
            temp_model = ListAccessTokensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        description: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.app_name = app_name
        self.description = description
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.description is not None:
            result['description'] = self.description
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListAppsResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        description: str = None,
        flow_quota: str = None,
        owner_id: str = None,
        region_id: str = None,
        status: str = None,
        storage_quota: str = None,
    ):
        # 代表资源名称的资源属性字段
        self.app_name = app_name
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 应用备注
        self.description = description
        # 流量限流额
        self.flow_quota = flow_quota
        # OwnerID账号ID
        self.owner_id = owner_id
        # 代表region的资源属性字段
        self.region_id = region_id
        # 代表资源状态的资源属性字段
        self.status = status
        # 存储限流额
        self.storage_quota = storage_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.flow_quota is not None:
            result['flowQuota'] = self.flow_quota
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.storage_quota is not None:
            result['storageQuota'] = self.storage_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('flowQuota') is not None:
            self.flow_quota = m.get('flowQuota')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('storageQuota') is not None:
            self.storage_quota = m.get('storageQuota')
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListAppsResponseBodyResult] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.result = result
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListAppsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppsResponseBody = None,
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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataStreamsRequest(TeaModel):
    def __init__(
        self,
        data_stream_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.data_stream_name = data_stream_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_stream_name is not None:
            result['dataStreamName'] = self.data_stream_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStreamName') is not None:
            self.data_stream_name = m.get('dataStreamName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListDataStreamsResponseBodyResultTemplate(TeaModel):
    def __init__(
        self,
        mappings: List[DataStreamMapping] = None,
    ):
        # 索引字段设置
        self.mappings = mappings

    def validate(self):
        if self.mappings:
            for k in self.mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mappings'] = []
        if self.mappings is not None:
            for k in self.mappings:
                result['mappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mappings = []
        if m.get('mappings') is not None:
            for k in m.get('mappings'):
                temp_model = DataStreamMapping()
                self.mappings.append(temp_model.from_map(k))
        return self


class ListDataStreamsResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        data_stream_id: str = None,
        data_stream_name: str = None,
        delete_phase: str = None,
        region_id: str = None,
        template: ListDataStreamsResponseBodyResultTemplate = None,
        time_stamp_key: str = None,
        type: str = None,
    ):
        # 关联的应用AppId
        self.app_name = app_name
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 代表资源一级ID的资源属性字段
        self.data_stream_id = data_stream_id
        # 代表资源名称的资源属性字段
        self.data_stream_name = data_stream_name
        # 删除时间
        self.delete_phase = delete_phase
        # 代表region的资源属性字段
        self.region_id = region_id
        # 数据流模板
        self.template = template
        self.time_stamp_key = time_stamp_key
        # 数据流类型
        self.type = type

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_stream_id is not None:
            result['dataStreamId'] = self.data_stream_id
        if self.data_stream_name is not None:
            result['dataStreamName'] = self.data_stream_name
        if self.delete_phase is not None:
            result['deletePhase'] = self.delete_phase
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.time_stamp_key is not None:
            result['timeStampKey'] = self.time_stamp_key
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataStreamId') is not None:
            self.data_stream_id = m.get('dataStreamId')
        if m.get('dataStreamName') is not None:
            self.data_stream_name = m.get('dataStreamName')
        if m.get('deletePhase') is not None:
            self.delete_phase = m.get('deletePhase')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('template') is not None:
            temp_model = ListDataStreamsResponseBodyResultTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('timeStampKey') is not None:
            self.time_stamp_key = m.get('timeStampKey')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListDataStreamsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[ListDataStreamsResponseBodyResult] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.result = result
        self.total_count = total_count

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = ListDataStreamsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListDataStreamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataStreamsResponseBody = None,
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
            temp_model = ListDataStreamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
    ):
        # 应用备注
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateAppResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppResponseBody = None,
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
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataStreamRequestTemplate(TeaModel):
    def __init__(
        self,
        mappings: List[DataStreamMapping] = None,
    ):
        self.mappings = mappings

    def validate(self):
        if self.mappings:
            for k in self.mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['mappings'] = []
        if self.mappings is not None:
            for k in self.mappings:
                result['mappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mappings = []
        if m.get('mappings') is not None:
            for k in m.get('mappings'):
                temp_model = DataStreamMapping()
                self.mappings.append(temp_model.from_map(k))
        return self


class UpdateDataStreamRequest(TeaModel):
    def __init__(
        self,
        delete_phase: str = None,
        dynamic: str = None,
        template: UpdateDataStreamRequestTemplate = None,
        time_stamp_key: str = None,
    ):
        # 删除时间
        self.delete_phase = delete_phase
        self.dynamic = dynamic
        self.template = template
        self.time_stamp_key = time_stamp_key

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_phase is not None:
            result['deletePhase'] = self.delete_phase
        if self.dynamic is not None:
            result['dynamic'] = self.dynamic
        if self.template is not None:
            result['template'] = self.template.to_map()
        if self.time_stamp_key is not None:
            result['timeStampKey'] = self.time_stamp_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deletePhase') is not None:
            self.delete_phase = m.get('deletePhase')
        if m.get('dynamic') is not None:
            self.dynamic = m.get('dynamic')
        if m.get('template') is not None:
            temp_model = UpdateDataStreamRequestTemplate()
            self.template = temp_model.from_map(m['template'])
        if m.get('timeStampKey') is not None:
            self.time_stamp_key = m.get('timeStampKey')
        return self


class UpdateDataStreamResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_name: str = None,
    ):
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        return self


class UpdateDataStreamResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: UpdateDataStreamResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('result') is not None:
            temp_model = UpdateDataStreamResponseBodyResult()
            self.result = temp_model.from_map(m['result'])
        return self


class UpdateDataStreamResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataStreamResponseBody = None,
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
            temp_model = UpdateDataStreamResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


