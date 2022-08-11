# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class BatchAuditTest01Request(TeaModel):
    def __init__(
        self,
        batch_audit_test_01: str = None,
        demo_01: str = None,
        name: str = None,
        test_010101: bool = None,
    ):
        self.batch_audit_test_01 = batch_audit_test_01
        self.demo_01 = demo_01
        self.name = name
        self.test_010101 = test_010101

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_audit_test_01 is not None:
            result['BatchAuditTest01'] = self.batch_audit_test_01
        if self.demo_01 is not None:
            result['Demo01'] = self.demo_01
        if self.name is not None:
            result['Name'] = self.name
        if self.test_010101 is not None:
            result['Test010101'] = self.test_010101
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchAuditTest01') is not None:
            self.batch_audit_test_01 = m.get('BatchAuditTest01')
        if m.get('Demo01') is not None:
            self.demo_01 = m.get('Demo01')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Test010101') is not None:
            self.test_010101 = m.get('Test010101')
        return self


class BatchAuditTest01ResponseBodyDemo01Demo011Demo011(TeaModel):
    def __init__(
        self,
        demo_0111: str = None,
    ):
        self.demo_0111 = demo_0111

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_0111 is not None:
            result['Demo0111'] = self.demo_0111
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Demo0111') is not None:
            self.demo_0111 = m.get('Demo0111')
        return self


class BatchAuditTest01ResponseBodyDemo01Demo011(TeaModel):
    def __init__(
        self,
        demo_011: List[BatchAuditTest01ResponseBodyDemo01Demo011Demo011] = None,
    ):
        self.demo_011 = demo_011

    def validate(self):
        if self.demo_011:
            for k in self.demo_011:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Demo011'] = []
        if self.demo_011 is not None:
            for k in self.demo_011:
                result['Demo011'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.demo_011 = []
        if m.get('Demo011') is not None:
            for k in m.get('Demo011'):
                temp_model = BatchAuditTest01ResponseBodyDemo01Demo011Demo011()
                self.demo_011.append(temp_model.from_map(k))
        return self


class BatchAuditTest01ResponseBodyDemo01(TeaModel):
    def __init__(
        self,
        demo_011: BatchAuditTest01ResponseBodyDemo01Demo011 = None,
    ):
        self.demo_011 = demo_011

    def validate(self):
        if self.demo_011:
            self.demo_011.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_011 is not None:
            result['Demo011'] = self.demo_011.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Demo011') is not None:
            temp_model = BatchAuditTest01ResponseBodyDemo01Demo011()
            self.demo_011 = temp_model.from_map(m['Demo011'])
        return self


class BatchAuditTest01ResponseBody(TeaModel):
    def __init__(
        self,
        demo_01: BatchAuditTest01ResponseBodyDemo01 = None,
        name: str = None,
        request_id: str = None,
    ):
        self.demo_01 = demo_01
        self.name = name
        self.request_id = request_id

    def validate(self):
        if self.demo_01:
            self.demo_01.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.demo_01 is not None:
            result['Demo01'] = self.demo_01.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Demo01') is not None:
            temp_model = BatchAuditTest01ResponseBodyDemo01()
            self.demo_01 = temp_model.from_map(m['Demo01'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchAuditTest01Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchAuditTest01ResponseBody = None,
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
            temp_model = BatchAuditTest01ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FTApiAliasApiRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FTApiAliasApiResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FTApiAliasApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FTApiAliasApiResponseBody = None,
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
            temp_model = FTApiAliasApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtDynamicAddressDubboRequest(TeaModel):
    def __init__(
        self,
        int_value: int = None,
        string_value: str = None,
    ):
        self.int_value = int_value
        self.string_value = string_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_value is not None:
            result['IntValue'] = self.int_value
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntValue') is not None:
            self.int_value = m.get('IntValue')
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        return self


class FtDynamicAddressDubboResponseBody(TeaModel):
    def __init__(
        self,
        int_value: int = None,
        request_id: str = None,
        string_value: str = None,
    ):
        self.int_value = int_value
        self.request_id = request_id
        self.string_value = string_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_value is not None:
            result['IntValue'] = self.int_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntValue') is not None:
            self.int_value = m.get('IntValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        return self


class FtDynamicAddressDubboResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtDynamicAddressDubboResponseBody = None,
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
            temp_model = FtDynamicAddressDubboResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtDynamicAddressHsfResponseBody(TeaModel):
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


class FtDynamicAddressHsfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtDynamicAddressHsfResponseBody = None,
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
            temp_model = FtDynamicAddressHsfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtDynamicAddressHttpVpcRequest(TeaModel):
    def __init__(
        self,
        boolean_param: bool = None,
        default_value: Dict[str, Any] = None,
        other_param: Dict[str, Any] = None,
        p_1: str = None,
        string_value: Dict[str, Any] = None,
    ):
        self.boolean_param = boolean_param
        self.default_value = default_value
        self.other_param = other_param
        self.p_1 = p_1
        self.string_value = string_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.other_param is not None:
            result['OtherParam'] = self.other_param
        if self.p_1 is not None:
            result['P1'] = self.p_1
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BooleanParam') is not None:
            self.boolean_param = m.get('BooleanParam')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('OtherParam') is not None:
            self.other_param = m.get('OtherParam')
        if m.get('P1') is not None:
            self.p_1 = m.get('P1')
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        return self


class FtDynamicAddressHttpVpcShrinkRequest(TeaModel):
    def __init__(
        self,
        boolean_param: bool = None,
        default_value_shrink: str = None,
        other_param_shrink: str = None,
        p_1: str = None,
        string_value_shrink: str = None,
    ):
        self.boolean_param = boolean_param
        self.default_value_shrink = default_value_shrink
        self.other_param_shrink = other_param_shrink
        self.p_1 = p_1
        self.string_value_shrink = string_value_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        if self.default_value_shrink is not None:
            result['DefaultValue'] = self.default_value_shrink
        if self.other_param_shrink is not None:
            result['OtherParam'] = self.other_param_shrink
        if self.p_1 is not None:
            result['P1'] = self.p_1
        if self.string_value_shrink is not None:
            result['StringValue'] = self.string_value_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BooleanParam') is not None:
            self.boolean_param = m.get('BooleanParam')
        if m.get('DefaultValue') is not None:
            self.default_value_shrink = m.get('DefaultValue')
        if m.get('OtherParam') is not None:
            self.other_param_shrink = m.get('OtherParam')
        if m.get('P1') is not None:
            self.p_1 = m.get('P1')
        if m.get('StringValue') is not None:
            self.string_value_shrink = m.get('StringValue')
        return self


class FtDynamicAddressHttpVpcResponseBody(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_rpc_sign: str = None,
    ):
        self.params = params
        self.service_rpc_sign = service_rpc_sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_rpc_sign is not None:
            result['ServiceRpcSign'] = self.service_rpc_sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceRpcSign') is not None:
            self.service_rpc_sign = m.get('ServiceRpcSign')
        return self


class FtDynamicAddressHttpVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtDynamicAddressHttpVpcResponseBody = None,
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
            temp_model = FtDynamicAddressHttpVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtEagleEyeRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtEagleEyeResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
        eagle_eye_trace_id: str = None,
    ):
        self.name = name
        self.request_id = request_id
        self.eagle_eye_trace_id = eagle_eye_trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.eagle_eye_trace_id is not None:
            result['eagleEyeTraceId'] = self.eagle_eye_trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('eagleEyeTraceId') is not None:
            self.eagle_eye_trace_id = m.get('eagleEyeTraceId')
        return self


class FtEagleEyeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtEagleEyeResponseBody = None,
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
            temp_model = FtEagleEyeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtFlowSpecialRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtFlowSpecialResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FtFlowSpecialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtFlowSpecialResponseBody = None,
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
            temp_model = FtFlowSpecialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtGatedLaunchPolicy4Request(TeaModel):
    def __init__(
        self,
        is_gated_launch: str = None,
    ):
        self.is_gated_launch = is_gated_launch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_gated_launch is not None:
            result['IsGatedLaunch'] = self.is_gated_launch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGatedLaunch') is not None:
            self.is_gated_launch = m.get('IsGatedLaunch')
        return self


class FtGatedLaunchPolicy4ResponseBody(TeaModel):
    def __init__(
        self,
        is_gated_launch: str = None,
        request_id: str = None,
    ):
        self.is_gated_launch = is_gated_launch
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_gated_launch is not None:
            result['IsGatedLaunch'] = self.is_gated_launch
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsGatedLaunch') is not None:
            self.is_gated_launch = m.get('IsGatedLaunch')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FtGatedLaunchPolicy4Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtGatedLaunchPolicy4ResponseBody = None,
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
            temp_model = FtGatedLaunchPolicy4ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtIpFlowControlRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtIpFlowControlResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FtIpFlowControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtIpFlowControlResponseBody = None,
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
            temp_model = FtIpFlowControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FtParamListRequestDisk(TeaModel):
    def __init__(
        self,
        size: List[str] = None,
        type: List[str] = None,
    ):
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class FtParamListRequest(TeaModel):
    def __init__(
        self,
        disk: List[FtParamListRequestDisk] = None,
        name: str = None,
    ):
        self.disk = disk
        self.name = name

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = FtParamListRequestDisk()
                self.disk.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class FtParamListResponseBody(TeaModel):
    def __init__(
        self,
        name: str = None,
        request_id: str = None,
    ):
        self.name = name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class FtParamListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FtParamListResponseBody = None,
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
            temp_model = FtParamListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestFlowStrategy01Request(TeaModel):
    def __init__(
        self,
        names: Dict[str, Any] = None,
    ):
        self.names = names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        return self


class TestFlowStrategy01ShrinkRequest(TeaModel):
    def __init__(
        self,
        names_shrink: str = None,
    ):
        self.names_shrink = names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names_shrink is not None:
            result['Names'] = self.names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names_shrink = m.get('Names')
        return self


class TestFlowStrategy01ResponseBody(TeaModel):
    def __init__(
        self,
        list: List[str] = None,
        names: List[str] = None,
        request_id: str = None,
    ):
        self.list = list
        self.names = names
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list
        if self.names is not None:
            result['Names'] = self.names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            self.list = m.get('List')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TestFlowStrategy01Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestFlowStrategy01ResponseBody = None,
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
            temp_model = TestFlowStrategy01ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestHttpApiRequest(TeaModel):
    def __init__(
        self,
        boolean_param: bool = None,
        default_value: Dict[str, Any] = None,
        other_param: Dict[str, Any] = None,
        string_value: Dict[str, Any] = None,
    ):
        self.boolean_param = boolean_param
        self.default_value = default_value
        self.other_param = other_param
        self.string_value = string_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.other_param is not None:
            result['OtherParam'] = self.other_param
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BooleanParam') is not None:
            self.boolean_param = m.get('BooleanParam')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('OtherParam') is not None:
            self.other_param = m.get('OtherParam')
        if m.get('StringValue') is not None:
            self.string_value = m.get('StringValue')
        return self


class TestHttpApiShrinkRequest(TeaModel):
    def __init__(
        self,
        boolean_param: bool = None,
        default_value_shrink: str = None,
        other_param_shrink: str = None,
        string_value_shrink: str = None,
    ):
        self.boolean_param = boolean_param
        self.default_value_shrink = default_value_shrink
        self.other_param_shrink = other_param_shrink
        self.string_value_shrink = string_value_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        if self.default_value_shrink is not None:
            result['DefaultValue'] = self.default_value_shrink
        if self.other_param_shrink is not None:
            result['OtherParam'] = self.other_param_shrink
        if self.string_value_shrink is not None:
            result['StringValue'] = self.string_value_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BooleanParam') is not None:
            self.boolean_param = m.get('BooleanParam')
        if m.get('DefaultValue') is not None:
            self.default_value_shrink = m.get('DefaultValue')
        if m.get('OtherParam') is not None:
            self.other_param_shrink = m.get('OtherParam')
        if m.get('StringValue') is not None:
            self.string_value_shrink = m.get('StringValue')
        return self


class TestHttpApiResponseBody(TeaModel):
    def __init__(
        self,
        params: str = None,
        service_rpc_sign: str = None,
    ):
        self.params = params
        self.service_rpc_sign = service_rpc_sign

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.params is not None:
            result['Params'] = self.params
        if self.service_rpc_sign is not None:
            result['ServiceRpcSign'] = self.service_rpc_sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ServiceRpcSign') is not None:
            self.service_rpc_sign = m.get('ServiceRpcSign')
        return self


class TestHttpApiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestHttpApiResponseBody = None,
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
            temp_model = TestHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


