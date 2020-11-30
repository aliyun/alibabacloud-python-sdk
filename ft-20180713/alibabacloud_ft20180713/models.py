# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import Dict, Any, List
except ImportError:
    pass


class TestFlowStrategy01Request(TeaModel):
    def __init__(self, names=None):
        self.names = names              # type: Dict[str, Any]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, map={}):
        if map.get('Names') is not None:
            self.names = map.get('Names')
        return self


class TestFlowStrategy01ShrinkRequest(TeaModel):
    def __init__(self, names_shrink=None):
        self.names_shrink = names_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.names_shrink is not None:
            result['Names'] = self.names_shrink
        return result

    def from_map(self, map={}):
        if map.get('Names') is not None:
            self.names_shrink = map.get('Names')
        return self


class TestFlowStrategy01Response(TeaModel):
    def __init__(self, request_id=None, list=None, names=None):
        self.request_id = request_id    # type: str
        self.list = list                # type: List[str]
        self.names = names              # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.list, 'list')
        self.validate_required(self.names, 'names')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.list is not None:
            result['List'] = self.list
        if self.names is not None:
            result['Names'] = self.names
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('List') is not None:
            self.list = map.get('List')
        if map.get('Names') is not None:
            self.names = map.get('Names')
        return self


class TestHttpApiRequest(TeaModel):
    def __init__(self, string_value=None, default_value=None, other_param=None, boolean_param=None):
        self.string_value = string_value  # type: Dict[str, Any]
        self.default_value = default_value  # type: Dict[str, Any]
        self.other_param = other_param  # type: Dict[str, Any]
        self.boolean_param = boolean_param  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.other_param is not None:
            result['OtherParam'] = self.other_param
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        return result

    def from_map(self, map={}):
        if map.get('StringValue') is not None:
            self.string_value = map.get('StringValue')
        if map.get('DefaultValue') is not None:
            self.default_value = map.get('DefaultValue')
        if map.get('OtherParam') is not None:
            self.other_param = map.get('OtherParam')
        if map.get('BooleanParam') is not None:
            self.boolean_param = map.get('BooleanParam')
        return self


class TestHttpApiShrinkRequest(TeaModel):
    def __init__(self, string_value_shrink=None, default_value_shrink=None, other_param_shrink=None,
                 boolean_param=None):
        self.string_value_shrink = string_value_shrink  # type: str
        self.default_value_shrink = default_value_shrink  # type: str
        self.other_param_shrink = other_param_shrink  # type: str
        self.boolean_param = boolean_param  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.string_value_shrink is not None:
            result['StringValue'] = self.string_value_shrink
        if self.default_value_shrink is not None:
            result['DefaultValue'] = self.default_value_shrink
        if self.other_param_shrink is not None:
            result['OtherParam'] = self.other_param_shrink
        if self.boolean_param is not None:
            result['BooleanParam'] = self.boolean_param
        return result

    def from_map(self, map={}):
        if map.get('StringValue') is not None:
            self.string_value_shrink = map.get('StringValue')
        if map.get('DefaultValue') is not None:
            self.default_value_shrink = map.get('DefaultValue')
        if map.get('OtherParam') is not None:
            self.other_param_shrink = map.get('OtherParam')
        if map.get('BooleanParam') is not None:
            self.boolean_param = map.get('BooleanParam')
        return self


class TestHttpApiResponse(TeaModel):
    def __init__(self, params=None, service_rpc_sign=None):
        self.params = params            # type: str
        self.service_rpc_sign = service_rpc_sign  # type: str

    def validate(self):
        self.validate_required(self.params, 'params')
        self.validate_required(self.service_rpc_sign, 'service_rpc_sign')

    def to_map(self):
        result = {}
        if self.params is not None:
            result['Params'] = self.params
        if self.service_rpc_sign is not None:
            result['ServiceRpcSign'] = self.service_rpc_sign
        return result

    def from_map(self, map={}):
        if map.get('Params') is not None:
            self.params = map.get('Params')
        if map.get('ServiceRpcSign') is not None:
            self.service_rpc_sign = map.get('ServiceRpcSign')
        return self


class BatchAuditTest01Request(TeaModel):
    def __init__(self, name=None, batch_audit_test_01=None, demo_01=None, test_010101=None):
        self.name = name                # type: str
        self.batch_audit_test_01 = batch_audit_test_01  # type: str
        self.demo_01 = demo_01          # type: str
        self.test_010101 = test_010101  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        if self.batch_audit_test_01 is not None:
            result['BatchAuditTest01'] = self.batch_audit_test_01
        if self.demo_01 is not None:
            result['Demo01'] = self.demo_01
        if self.test_010101 is not None:
            result['Test010101'] = self.test_010101
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('BatchAuditTest01') is not None:
            self.batch_audit_test_01 = map.get('BatchAuditTest01')
        if map.get('Demo01') is not None:
            self.demo_01 = map.get('Demo01')
        if map.get('Test010101') is not None:
            self.test_010101 = map.get('Test010101')
        return self


class BatchAuditTest01Response(TeaModel):
    def __init__(self, request_id=None, name=None, demo_01=None):
        self.request_id = request_id    # type: str
        self.name = name                # type: str
        self.demo_01 = demo_01          # type: BatchAuditTest01ResponseDemo01

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.demo_01, 'demo_01')
        if self.demo_01:
            self.demo_01.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.demo_01 is not None:
            result['Demo01'] = self.demo_01.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('Demo01') is not None:
            temp_model = BatchAuditTest01ResponseDemo01()
            self.demo_01 = temp_model.from_map(map['Demo01'])
        return self


class BatchAuditTest01ResponseDemo01Demo011Demo011(TeaModel):
    def __init__(self, demo_0111=None):
        self.demo_0111 = demo_0111      # type: str

    def validate(self):
        self.validate_required(self.demo_0111, 'demo_0111')

    def to_map(self):
        result = {}
        if self.demo_0111 is not None:
            result['Demo0111'] = self.demo_0111
        return result

    def from_map(self, map={}):
        if map.get('Demo0111') is not None:
            self.demo_0111 = map.get('Demo0111')
        return self


class BatchAuditTest01ResponseDemo01Demo011(TeaModel):
    def __init__(self, demo_011=None):
        self.demo_011 = demo_011        # type: List[BatchAuditTest01ResponseDemo01Demo011Demo011]

    def validate(self):
        self.validate_required(self.demo_011, 'demo_011')
        if self.demo_011:
            for k in self.demo_011:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Demo011'] = []
        if self.demo_011 is not None:
            for k in self.demo_011:
                result['Demo011'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.demo_011 = []
        if map.get('Demo011') is not None:
            for k in map.get('Demo011'):
                temp_model = BatchAuditTest01ResponseDemo01Demo011Demo011()
                self.demo_011.append(temp_model.from_map(k))
        return self


class BatchAuditTest01ResponseDemo01(TeaModel):
    def __init__(self, demo_011=None):
        self.demo_011 = demo_011        # type: BatchAuditTest01ResponseDemo01Demo011

    def validate(self):
        self.validate_required(self.demo_011, 'demo_011')
        if self.demo_011:
            self.demo_011.validate()

    def to_map(self):
        result = {}
        if self.demo_011 is not None:
            result['Demo011'] = self.demo_011.to_map()
        return result

    def from_map(self, map={}):
        if map.get('Demo011') is not None:
            temp_model = BatchAuditTest01ResponseDemo01Demo011()
            self.demo_011 = temp_model.from_map(map['Demo011'])
        return self


class FtIpFlowControlRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FtIpFlowControlResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id    # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FtDynamicAddressDubboRequest(TeaModel):
    def __init__(self, int_value=None, string_value=None):
        self.int_value = int_value      # type: int
        self.string_value = string_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.int_value is not None:
            result['IntValue'] = self.int_value
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        return result

    def from_map(self, map={}):
        if map.get('IntValue') is not None:
            self.int_value = map.get('IntValue')
        if map.get('StringValue') is not None:
            self.string_value = map.get('StringValue')
        return self


class FtDynamicAddressDubboResponse(TeaModel):
    def __init__(self, request_id=None, string_value=None, int_value=None):
        self.request_id = request_id    # type: str
        self.string_value = string_value  # type: str
        self.int_value = int_value      # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.string_value, 'string_value')
        self.validate_required(self.int_value, 'int_value')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.string_value is not None:
            result['StringValue'] = self.string_value
        if self.int_value is not None:
            result['IntValue'] = self.int_value
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('StringValue') is not None:
            self.string_value = map.get('StringValue')
        if map.get('IntValue') is not None:
            self.int_value = map.get('IntValue')
        return self


class FtDynamicAddressHsfRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class FtDynamicAddressHsfResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class FtFlowSpecialRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FtFlowSpecialResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id    # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FTApiAliasApiRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FTApiAliasApiResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id    # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FtEagleEyeRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FtEagleEyeResponse(TeaModel):
    def __init__(self, request_id=None, name=None, eagle_eye_trace_id=None):
        self.request_id = request_id    # type: str
        self.name = name                # type: str
        self.eagle_eye_trace_id = eagle_eye_trace_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.eagle_eye_trace_id, 'eagle_eye_trace_id')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        if self.eagle_eye_trace_id is not None:
            result['eagleEyeTraceId'] = self.eagle_eye_trace_id
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        if map.get('eagleEyeTraceId') is not None:
            self.eagle_eye_trace_id = map.get('eagleEyeTraceId')
        return self


class FtParamListRequest(TeaModel):
    def __init__(self, name=None, disk=None):
        self.name = name                # type: str
        self.disk = disk                # type: List[FtParamListRequestDisk]

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.name is not None:
            result['Name'] = self.name
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('Name') is not None:
            self.name = map.get('Name')
        self.disk = []
        if map.get('Disk') is not None:
            for k in map.get('Disk'):
                temp_model = FtParamListRequestDisk()
                self.disk.append(temp_model.from_map(k))
        return self


class FtParamListRequestDisk(TeaModel):
    def __init__(self, size=None, type=None):
        self.size = size                # type: List[str]
        self.type = type                # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.size is not None:
            result['Size'] = self.size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('Size') is not None:
            self.size = map.get('Size')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        return self


class FtParamListResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id    # type: str
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Name') is not None:
            self.name = map.get('Name')
        return self


class FtGatedLaunchPolicy4Request(TeaModel):
    def __init__(self, is_gated_launch=None):
        self.is_gated_launch = is_gated_launch  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.is_gated_launch is not None:
            result['IsGatedLaunch'] = self.is_gated_launch
        return result

    def from_map(self, map={}):
        if map.get('IsGatedLaunch') is not None:
            self.is_gated_launch = map.get('IsGatedLaunch')
        return self


class FtGatedLaunchPolicy4Response(TeaModel):
    def __init__(self, request_id=None, is_gated_launch=None):
        self.request_id = request_id    # type: str
        self.is_gated_launch = is_gated_launch  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_gated_launch, 'is_gated_launch')

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_gated_launch is not None:
            result['IsGatedLaunch'] = self.is_gated_launch
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('IsGatedLaunch') is not None:
            self.is_gated_launch = map.get('IsGatedLaunch')
        return self
