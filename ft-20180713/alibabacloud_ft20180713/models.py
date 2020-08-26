# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class TestFlowStrategy01Request(TeaModel):
    def __init__(self, names=None):
        self.names = names

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Names'] = self.names
        return result

    def from_map(self, map={}):
        self.names = map.get('Names')
        return self


class TestFlowStrategy01Response(TeaModel):
    def __init__(self, request_id=None, list_=None, names=None):
        self.request_id = request_id
        self.list_ = list_
        self.names = names

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.list_, 'list_')
        self.validate_required(self.names, 'names')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['List'] = []
        if self.list_ is not None:
            for k in self.list_:
                result['List'].append(k)
        else:
            result['List'] = None
        result['Names'] = []
        if self.names is not None:
            for k in self.names:
                result['Names'].append(k)
        else:
            result['Names'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.list_ = []
        if map.get('List') is not None:
            for k in map.get('List'):
                self.list_.append(k)
        else:
            self.list_ = None
        self.names = []
        if map.get('Names') is not None:
            for k in map.get('Names'):
                self.names.append(k)
        else:
            self.names = None
        return self


class TestHttpApiRequest(TeaModel):
    def __init__(self, string_value=None, default_value=None, other_param=None, boolean_param=None):
        self.string_value = string_value
        self.default_value = default_value
        self.other_param = other_param
        self.boolean_param = boolean_param

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['StringValue'] = self.string_value
        result['DefaultValue'] = self.default_value
        result['OtherParam'] = self.other_param
        result['BooleanParam'] = self.boolean_param
        return result

    def from_map(self, map={}):
        self.string_value = map.get('StringValue')
        self.default_value = map.get('DefaultValue')
        self.other_param = map.get('OtherParam')
        self.boolean_param = map.get('BooleanParam')
        return self


class TestHttpApiResponse(TeaModel):
    def __init__(self, params=None, service_rpc_sign=None):
        self.params = params
        self.service_rpc_sign = service_rpc_sign

    def validate(self):
        self.validate_required(self.params, 'params')
        self.validate_required(self.service_rpc_sign, 'service_rpc_sign')

    def to_map(self):
        result = {}
        result['Params'] = self.params
        result['ServiceRpcSign'] = self.service_rpc_sign
        return result

    def from_map(self, map={}):
        self.params = map.get('Params')
        self.service_rpc_sign = map.get('ServiceRpcSign')
        return self


class BatchAuditTest01Request(TeaModel):
    def __init__(self, name=None, batch_audit_test_01=None, demo_01=None, test_010101=None):
        self.name = name
        self.batch_audit_test_01 = batch_audit_test_01
        self.demo_01 = demo_01
        self.test_010101 = test_010101

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['BatchAuditTest01'] = self.batch_audit_test_01
        result['Demo01'] = self.demo_01
        result['Test010101'] = self.test_010101
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.batch_audit_test_01 = map.get('BatchAuditTest01')
        self.demo_01 = map.get('Demo01')
        self.test_010101 = map.get('Test010101')
        return self


class BatchAuditTest01Response(TeaModel):
    def __init__(self, request_id=None, name=None, demo_01=None):
        self.request_id = request_id
        self.name = name
        self.demo_01 = demo_01

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.demo_01, 'demo_01')
        if self.demo_01:
            self.demo_01.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        if self.demo_01 is not None:
            result['Demo01'] = self.demo_01.to_map()
        else:
            result['Demo01'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        if map.get('Demo01') is not None:
            temp_model = BatchAuditTest01ResponseDemo01()
            self.demo_01 = temp_model.from_map(map['Demo01'])
        else:
            self.demo_01 = None
        return self


class BatchAuditTest01ResponseDemo01Demo011Demo011(TeaModel):
    def __init__(self, demo_0111=None):
        self.demo_0111 = demo_0111

    def validate(self):
        self.validate_required(self.demo_0111, 'demo_0111')

    def to_map(self):
        result = {}
        result['Demo0111'] = self.demo_0111
        return result

    def from_map(self, map={}):
        self.demo_0111 = map.get('Demo0111')
        return self


class BatchAuditTest01ResponseDemo01Demo011(TeaModel):
    def __init__(self, demo_011=None):
        self.demo_011 = demo_011

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
        else:
            result['Demo011'] = None
        return result

    def from_map(self, map={}):
        self.demo_011 = []
        if map.get('Demo011') is not None:
            for k in map.get('Demo011'):
                temp_model = BatchAuditTest01ResponseDemo01Demo011Demo011()
                temp_model = temp_model.from_map(k)
                self.demo_011.append(temp_model)
        else:
            self.demo_011 = None
        return self


class BatchAuditTest01ResponseDemo01(TeaModel):
    def __init__(self, demo_011=None):
        self.demo_011 = demo_011

    def validate(self):
        self.validate_required(self.demo_011, 'demo_011')
        if self.demo_011:
            self.demo_011.validate()

    def to_map(self):
        result = {}
        if self.demo_011 is not None:
            result['Demo011'] = self.demo_011.to_map()
        else:
            result['Demo011'] = None
        return result

    def from_map(self, map={}):
        if map.get('Demo011') is not None:
            temp_model = BatchAuditTest01ResponseDemo01Demo011()
            self.demo_011 = temp_model.from_map(map['Demo011'])
        else:
            self.demo_011 = None
        return self
class FtIpFlowControlRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        return self


class FtIpFlowControlResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id
        self.name = name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        return self


class FtDynamicAddressDubboRequest(TeaModel):
    def __init__(self, int_value=None, string_value=None):
        self.int_value = int_value
        self.string_value = string_value

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['IntValue'] = self.int_value
        result['StringValue'] = self.string_value
        return result

    def from_map(self, map={}):
        self.int_value = map.get('IntValue')
        self.string_value = map.get('StringValue')
        return self


class FtDynamicAddressDubboResponse(TeaModel):
    def __init__(self, request_id=None, string_value=None, int_value=None):
        self.request_id = request_id
        self.string_value = string_value
        self.int_value = int_value

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.string_value, 'string_value')
        self.validate_required(self.int_value, 'int_value')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['StringValue'] = self.string_value
        result['IntValue'] = self.int_value
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.string_value = map.get('StringValue')
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
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class FtFlowSpecialRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        return self


class FtFlowSpecialResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id
        self.name = name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        return self


class FTApiAliasApiRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        return self


class FTApiAliasApiResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id
        self.name = name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        return self


class FtEagleEyeRequest(TeaModel):
    def __init__(self, name=None):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        return self


class FtEagleEyeResponse(TeaModel):
    def __init__(self, request_id=None, name=None, eagle_eye_trace_id=None):
        self.request_id = request_id
        self.name = name
        self.eagle_eye_trace_id = eagle_eye_trace_id

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.eagle_eye_trace_id, 'eagle_eye_trace_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        result['eagleEyeTraceId'] = self.eagle_eye_trace_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        self.eagle_eye_trace_id = map.get('eagleEyeTraceId')
        return self


class FtParamListRequest(TeaModel):
    def __init__(self, name=None, disk=None):
        self.name = name
        self.disk = disk

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        else:
            result['Disk'] = None
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.disk = []
        if map.get('Disk') is not None:
            for k in map.get('Disk'):
                temp_model = FtParamListRequestDisk()
                temp_model = temp_model.from_map(k)
                self.disk.append(temp_model)
        else:
            self.disk = None
        return self


class FtParamListRequestDisk(TeaModel):
    def __init__(self, size=None, type=None):
        self.size = size
        self.type = type

    def validate(self):
        self.validate_required(self.size, 'size')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['Size'] = []
        if self.size is not None:
            for k in self.size:
                result['Size'].append(k)
        else:
            result['Size'] = None
        result['Type'] = []
        if self.type is not None:
            for k in self.type:
                result['Type'].append(k)
        else:
            result['Type'] = None
        return result

    def from_map(self, map={}):
        self.size = []
        if map.get('Size') is not None:
            for k in map.get('Size'):
                self.size.append(k)
        else:
            self.size = None
        self.type = []
        if map.get('Type') is not None:
            for k in map.get('Type'):
                self.type.append(k)
        else:
            self.type = None
        return self
class FtParamListResponse(TeaModel):
    def __init__(self, request_id=None, name=None):
        self.request_id = request_id
        self.name = name

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.name = map.get('Name')
        return self


class FtGatedLaunchPolicy4Request(TeaModel):
    def __init__(self, is_gated_launch=None):
        self.is_gated_launch = is_gated_launch

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['IsGatedLaunch'] = self.is_gated_launch
        return result

    def from_map(self, map={}):
        self.is_gated_launch = map.get('IsGatedLaunch')
        return self


class FtGatedLaunchPolicy4Response(TeaModel):
    def __init__(self, request_id=None, is_gated_launch=None):
        self.request_id = request_id
        self.is_gated_launch = is_gated_launch

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.is_gated_launch, 'is_gated_launch')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['IsGatedLaunch'] = self.is_gated_launch
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.is_gated_launch = map.get('IsGatedLaunch')
        return self
