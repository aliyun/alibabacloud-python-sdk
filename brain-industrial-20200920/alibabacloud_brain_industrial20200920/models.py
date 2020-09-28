# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any, BinaryIO


class GetOpPvCustomValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetOpPvCustomValuesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetOpPvCustomValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetOpPvCustomValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetOpPvCustomValuesResponseDataOppvCustomDataInfoOpzdy(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetOpPvCustomValuesResponseDataOppvCustomDataInfoPvzdy(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetOpPvCustomValuesResponseDataOppvCustomDataInfo(TeaModel):
    def __init__(self, opzdy=None, pvzdy=None):
        self.opzdy = opzdy              # type: List[GetOpPvCustomValuesResponseDataOppvCustomDataInfoOpzdy]
        self.pvzdy = pvzdy              # type: List[GetOpPvCustomValuesResponseDataOppvCustomDataInfoPvzdy]

    def validate(self):
        self.validate_required(self.opzdy, 'opzdy')
        if self.opzdy:
            for k in self.opzdy:
                if k:
                    k.validate()
        self.validate_required(self.pvzdy, 'pvzdy')
        if self.pvzdy:
            for k in self.pvzdy:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Opzdy'] = []
        if self.opzdy is not None:
            for k in self.opzdy:
                result['Opzdy'].append(k.to_map() if k else None)
        else:
            result['Opzdy'] = None
        result['Pvzdy'] = []
        if self.pvzdy is not None:
            for k in self.pvzdy:
                result['Pvzdy'].append(k.to_map() if k else None)
        else:
            result['Pvzdy'] = None
        return result

    def from_map(self, map={}):
        self.opzdy = []
        if map.get('Opzdy') is not None:
            for k in map.get('Opzdy'):
                temp_model = GetOpPvCustomValuesResponseDataOppvCustomDataInfoOpzdy()
                self.opzdy.append(temp_model.from_map(k))
        else:
            self.opzdy = None
        self.pvzdy = []
        if map.get('Pvzdy') is not None:
            for k in map.get('Pvzdy'):
                temp_model = GetOpPvCustomValuesResponseDataOppvCustomDataInfoPvzdy()
                self.pvzdy.append(temp_model.from_map(k))
        else:
            self.pvzdy = None
        return self


class GetOpPvCustomValuesResponseData(TeaModel):
    def __init__(self, status=None, oppv_custom_data_info=None):
        self.status = status            # type: bool
        self.oppv_custom_data_info = oppv_custom_data_info  # type: GetOpPvCustomValuesResponseDataOppvCustomDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.oppv_custom_data_info, 'oppv_custom_data_info')
        if self.oppv_custom_data_info:
            self.oppv_custom_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.oppv_custom_data_info is not None:
            result['OppvCustomDataInfo'] = self.oppv_custom_data_info.to_map()
        else:
            result['OppvCustomDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('OppvCustomDataInfo') is not None:
            temp_model = GetOpPvCustomValuesResponseDataOppvCustomDataInfo()
            self.oppv_custom_data_info = temp_model.from_map(map['OppvCustomDataInfo'])
        else:
            self.oppv_custom_data_info = None
        return self


class SubmitPidLoopEvaluationRequest(TeaModel):
    def __init__(self, pid_loop_id_list=None, pid_project_id=None, start_time=None, end_time=None):
        self.pid_loop_id_list = pid_loop_id_list  # type: Dict[str, Any]
        self.pid_project_id = pid_project_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id_list, 'pid_loop_id_list')
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['PidLoopIdList'] = self.pid_loop_id_list
        result['PidProjectId'] = self.pid_project_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.pid_loop_id_list = map.get('PidLoopIdList')
        self.pid_project_id = map.get('PidProjectId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class SubmitPidLoopEvaluationResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        return self


class GetDefaultAdjustValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetDefaultAdjustValuesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetDefaultAdjustValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetDefaultAdjustValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoManualCtrl(TeaModel):
    def __init__(self, kp=None, ti=None, td=None):
        self.kp = kp                    # type: float
        self.ti = ti                    # type: float
        self.td = td                    # type: float

    def validate(self):
        self.validate_required(self.kp, 'kp')
        self.validate_required(self.ti, 'ti')
        self.validate_required(self.td, 'td')

    def to_map(self):
        result = {}
        result['Kp'] = self.kp
        result['Ti'] = self.ti
        result['Td'] = self.td
        return result

    def from_map(self, map={}):
        self.kp = map.get('Kp')
        self.ti = map.get('Ti')
        self.td = map.get('Td')
        return self


class GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoPerform(TeaModel):
    def __init__(self, raise_time=None, final_value=None, over_value=None, stable_error=None, adjust_time=None,
                 dynamic=None, robust=None):
        self.raise_time = raise_time    # type: float
        self.final_value = final_value  # type: float
        self.over_value = over_value    # type: float
        self.stable_error = stable_error  # type: float
        self.adjust_time = adjust_time  # type: float
        self.dynamic = dynamic          # type: float
        self.robust = robust            # type: float

    def validate(self):
        self.validate_required(self.raise_time, 'raise_time')
        self.validate_required(self.final_value, 'final_value')
        self.validate_required(self.over_value, 'over_value')
        self.validate_required(self.stable_error, 'stable_error')
        self.validate_required(self.adjust_time, 'adjust_time')
        self.validate_required(self.dynamic, 'dynamic')
        self.validate_required(self.robust, 'robust')

    def to_map(self):
        result = {}
        result['RaiseTime'] = self.raise_time
        result['FinalValue'] = self.final_value
        result['OverValue'] = self.over_value
        result['StableError'] = self.stable_error
        result['AdjustTime'] = self.adjust_time
        result['Dynamic'] = self.dynamic
        result['Robust'] = self.robust
        return result

    def from_map(self, map={}):
        self.raise_time = map.get('RaiseTime')
        self.final_value = map.get('FinalValue')
        self.over_value = map.get('OverValue')
        self.stable_error = map.get('StableError')
        self.adjust_time = map.get('AdjustTime')
        self.dynamic = map.get('Dynamic')
        self.robust = map.get('Robust')
        return self


class GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoManualPerform(TeaModel):
    def __init__(self, raise_time=None, final_value=None, over_value=None, stable_error=None, adjust_time=None,
                 dynamic=None, robust=None):
        self.raise_time = raise_time    # type: float
        self.final_value = final_value  # type: float
        self.over_value = over_value    # type: float
        self.stable_error = stable_error  # type: float
        self.adjust_time = adjust_time  # type: float
        self.dynamic = dynamic          # type: float
        self.robust = robust            # type: float

    def validate(self):
        self.validate_required(self.raise_time, 'raise_time')
        self.validate_required(self.final_value, 'final_value')
        self.validate_required(self.over_value, 'over_value')
        self.validate_required(self.stable_error, 'stable_error')
        self.validate_required(self.adjust_time, 'adjust_time')
        self.validate_required(self.dynamic, 'dynamic')
        self.validate_required(self.robust, 'robust')

    def to_map(self):
        result = {}
        result['RaiseTime'] = self.raise_time
        result['FinalValue'] = self.final_value
        result['OverValue'] = self.over_value
        result['StableError'] = self.stable_error
        result['AdjustTime'] = self.adjust_time
        result['Dynamic'] = self.dynamic
        result['Robust'] = self.robust
        return result

    def from_map(self, map={}):
        self.raise_time = map.get('RaiseTime')
        self.final_value = map.get('FinalValue')
        self.over_value = map.get('OverValue')
        self.stable_error = map.get('StableError')
        self.adjust_time = map.get('AdjustTime')
        self.dynamic = map.get('Dynamic')
        self.robust = map.get('Robust')
        return self


class GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfo(TeaModel):
    def __init__(self, manual_ctrl=None, perform=None, manual_perform=None):
        self.manual_ctrl = manual_ctrl  # type: GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoManualCtrl
        self.perform = perform          # type: GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoPerform
        self.manual_perform = manual_perform  # type: GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoManualPerform

    def validate(self):
        self.validate_required(self.manual_ctrl, 'manual_ctrl')
        if self.manual_ctrl:
            self.manual_ctrl.validate()
        self.validate_required(self.perform, 'perform')
        if self.perform:
            self.perform.validate()
        self.validate_required(self.manual_perform, 'manual_perform')
        if self.manual_perform:
            self.manual_perform.validate()

    def to_map(self):
        result = {}
        if self.manual_ctrl is not None:
            result['ManualCtrl'] = self.manual_ctrl.to_map()
        else:
            result['ManualCtrl'] = None
        if self.perform is not None:
            result['Perform'] = self.perform.to_map()
        else:
            result['Perform'] = None
        if self.manual_perform is not None:
            result['ManualPerform'] = self.manual_perform.to_map()
        else:
            result['ManualPerform'] = None
        return result

    def from_map(self, map={}):
        if map.get('ManualCtrl') is not None:
            temp_model = GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoManualCtrl()
            self.manual_ctrl = temp_model.from_map(map['ManualCtrl'])
        else:
            self.manual_ctrl = None
        if map.get('Perform') is not None:
            temp_model = GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoPerform()
            self.perform = temp_model.from_map(map['Perform'])
        else:
            self.perform = None
        if map.get('ManualPerform') is not None:
            temp_model = GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfoManualPerform()
            self.manual_perform = temp_model.from_map(map['ManualPerform'])
        else:
            self.manual_perform = None
        return self


class GetDefaultAdjustValuesResponseData(TeaModel):
    def __init__(self, status=None, default_adjust_data_info=None):
        self.status = status            # type: bool
        self.default_adjust_data_info = default_adjust_data_info  # type: GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.default_adjust_data_info, 'default_adjust_data_info')
        if self.default_adjust_data_info:
            self.default_adjust_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.default_adjust_data_info is not None:
            result['DefaultAdjustDataInfo'] = self.default_adjust_data_info.to_map()
        else:
            result['DefaultAdjustDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('DefaultAdjustDataInfo') is not None:
            temp_model = GetDefaultAdjustValuesResponseDataDefaultAdjustDataInfo()
            self.default_adjust_data_info = temp_model.from_map(map['DefaultAdjustDataInfo'])
        else:
            self.default_adjust_data_info = None
        return self


class GetPvOpAdjustValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetPvOpAdjustValuesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetPvOpAdjustValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetPvOpAdjustValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoOp(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoPv(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoSp(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetPvOpAdjustValuesResponseDataPvopAdjustDataInfo(TeaModel):
    def __init__(self, op=None, pv=None, sp=None):
        self.op = op                    # type: List[GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoOp]
        self.pv = pv                    # type: List[GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoPv]
        self.sp = sp                    # type: List[GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoSp]

    def validate(self):
        self.validate_required(self.op, 'op')
        if self.op:
            for k in self.op:
                if k:
                    k.validate()
        self.validate_required(self.pv, 'pv')
        if self.pv:
            for k in self.pv:
                if k:
                    k.validate()
        self.validate_required(self.sp, 'sp')
        if self.sp:
            for k in self.sp:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Op'] = []
        if self.op is not None:
            for k in self.op:
                result['Op'].append(k.to_map() if k else None)
        else:
            result['Op'] = None
        result['Pv'] = []
        if self.pv is not None:
            for k in self.pv:
                result['Pv'].append(k.to_map() if k else None)
        else:
            result['Pv'] = None
        result['Sp'] = []
        if self.sp is not None:
            for k in self.sp:
                result['Sp'].append(k.to_map() if k else None)
        else:
            result['Sp'] = None
        return result

    def from_map(self, map={}):
        self.op = []
        if map.get('Op') is not None:
            for k in map.get('Op'):
                temp_model = GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoOp()
                self.op.append(temp_model.from_map(k))
        else:
            self.op = None
        self.pv = []
        if map.get('Pv') is not None:
            for k in map.get('Pv'):
                temp_model = GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoPv()
                self.pv.append(temp_model.from_map(k))
        else:
            self.pv = None
        self.sp = []
        if map.get('Sp') is not None:
            for k in map.get('Sp'):
                temp_model = GetPvOpAdjustValuesResponseDataPvopAdjustDataInfoSp()
                self.sp.append(temp_model.from_map(k))
        else:
            self.sp = None
        return self


class GetPvOpAdjustValuesResponseData(TeaModel):
    def __init__(self, status=None, pvop_adjust_data_info=None):
        self.status = status            # type: bool
        self.pvop_adjust_data_info = pvop_adjust_data_info  # type: GetPvOpAdjustValuesResponseDataPvopAdjustDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.pvop_adjust_data_info, 'pvop_adjust_data_info')
        if self.pvop_adjust_data_info:
            self.pvop_adjust_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.pvop_adjust_data_info is not None:
            result['PvopAdjustDataInfo'] = self.pvop_adjust_data_info.to_map()
        else:
            result['PvopAdjustDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('PvopAdjustDataInfo') is not None:
            temp_model = GetPvOpAdjustValuesResponseDataPvopAdjustDataInfo()
            self.pvop_adjust_data_info = temp_model.from_map(map['PvopAdjustDataInfo'])
        else:
            self.pvop_adjust_data_info = None
        return self


class GetPvCustomSimulationValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetPvCustomSimulationValuesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetPvCustomSimulationValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetPvCustomSimulationValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetPvCustomSimulationValuesResponseDataPvCustomSimulateDataInfoPv(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetPvCustomSimulationValuesResponseDataPvCustomSimulateDataInfo(TeaModel):
    def __init__(self, pv=None):
        self.pv = pv                    # type: List[GetPvCustomSimulationValuesResponseDataPvCustomSimulateDataInfoPv]

    def validate(self):
        self.validate_required(self.pv, 'pv')
        if self.pv:
            for k in self.pv:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Pv'] = []
        if self.pv is not None:
            for k in self.pv:
                result['Pv'].append(k.to_map() if k else None)
        else:
            result['Pv'] = None
        return result

    def from_map(self, map={}):
        self.pv = []
        if map.get('Pv') is not None:
            for k in map.get('Pv'):
                temp_model = GetPvCustomSimulationValuesResponseDataPvCustomSimulateDataInfoPv()
                self.pv.append(temp_model.from_map(k))
        else:
            self.pv = None
        return self


class GetPvCustomSimulationValuesResponseData(TeaModel):
    def __init__(self, status=None, pv_custom_simulate_data_info=None):
        self.status = status            # type: bool
        self.pv_custom_simulate_data_info = pv_custom_simulate_data_info  # type: GetPvCustomSimulationValuesResponseDataPvCustomSimulateDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.pv_custom_simulate_data_info, 'pv_custom_simulate_data_info')
        if self.pv_custom_simulate_data_info:
            self.pv_custom_simulate_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.pv_custom_simulate_data_info is not None:
            result['PvCustomSimulateDataInfo'] = self.pv_custom_simulate_data_info.to_map()
        else:
            result['PvCustomSimulateDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('PvCustomSimulateDataInfo') is not None:
            temp_model = GetPvCustomSimulationValuesResponseDataPvCustomSimulateDataInfo()
            self.pv_custom_simulate_data_info = temp_model.from_map(map['PvCustomSimulateDataInfo'])
        else:
            self.pv_custom_simulate_data_info = None
        return self


class GetIdentificateValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetIdentificateValuesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetIdentificateValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetIdentificateValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetIdentificateValuesResponseDataIdentificateDataInfoDj(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetIdentificateValuesResponseDataIdentificateDataInfoGj(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetIdentificateValuesResponseDataIdentificateDataInfoBs(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetIdentificateValuesResponseDataIdentificateDataInfo(TeaModel):
    def __init__(self, dj=None, gj=None, bs=None):
        self.dj = dj                    # type: List[GetIdentificateValuesResponseDataIdentificateDataInfoDj]
        self.gj = gj                    # type: List[GetIdentificateValuesResponseDataIdentificateDataInfoGj]
        self.bs = bs                    # type: List[GetIdentificateValuesResponseDataIdentificateDataInfoBs]

    def validate(self):
        self.validate_required(self.dj, 'dj')
        if self.dj:
            for k in self.dj:
                if k:
                    k.validate()
        self.validate_required(self.gj, 'gj')
        if self.gj:
            for k in self.gj:
                if k:
                    k.validate()
        self.validate_required(self.bs, 'bs')
        if self.bs:
            for k in self.bs:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Dj'] = []
        if self.dj is not None:
            for k in self.dj:
                result['Dj'].append(k.to_map() if k else None)
        else:
            result['Dj'] = None
        result['Gj'] = []
        if self.gj is not None:
            for k in self.gj:
                result['Gj'].append(k.to_map() if k else None)
        else:
            result['Gj'] = None
        result['Bs'] = []
        if self.bs is not None:
            for k in self.bs:
                result['Bs'].append(k.to_map() if k else None)
        else:
            result['Bs'] = None
        return result

    def from_map(self, map={}):
        self.dj = []
        if map.get('Dj') is not None:
            for k in map.get('Dj'):
                temp_model = GetIdentificateValuesResponseDataIdentificateDataInfoDj()
                self.dj.append(temp_model.from_map(k))
        else:
            self.dj = None
        self.gj = []
        if map.get('Gj') is not None:
            for k in map.get('Gj'):
                temp_model = GetIdentificateValuesResponseDataIdentificateDataInfoGj()
                self.gj.append(temp_model.from_map(k))
        else:
            self.gj = None
        self.bs = []
        if map.get('Bs') is not None:
            for k in map.get('Bs'):
                temp_model = GetIdentificateValuesResponseDataIdentificateDataInfoBs()
                self.bs.append(temp_model.from_map(k))
        else:
            self.bs = None
        return self


class GetIdentificateValuesResponseData(TeaModel):
    def __init__(self, status=None, identificate_data_info=None):
        self.status = status            # type: bool
        self.identificate_data_info = identificate_data_info  # type: GetIdentificateValuesResponseDataIdentificateDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.identificate_data_info, 'identificate_data_info')
        if self.identificate_data_info:
            self.identificate_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.identificate_data_info is not None:
            result['IdentificateDataInfo'] = self.identificate_data_info.to_map()
        else:
            result['IdentificateDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('IdentificateDataInfo') is not None:
            temp_model = GetIdentificateValuesResponseDataIdentificateDataInfo()
            self.identificate_data_info = temp_model.from_map(map['IdentificateDataInfo'])
        else:
            self.identificate_data_info = None
        return self


class GetPvIdentSimulationValuesRequest(TeaModel):
    def __init__(self, pid_loop_id=None, pid_loop_parameter_id=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        return self


class GetPvIdentSimulationValuesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetPvIdentSimulationValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetPvIdentSimulationValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetPvIdentSimulationValuesResponseDataPvIdentSimulateDataInfoPv(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetPvIdentSimulationValuesResponseDataPvIdentSimulateDataInfo(TeaModel):
    def __init__(self, pv=None):
        self.pv = pv                    # type: List[GetPvIdentSimulationValuesResponseDataPvIdentSimulateDataInfoPv]

    def validate(self):
        self.validate_required(self.pv, 'pv')
        if self.pv:
            for k in self.pv:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Pv'] = []
        if self.pv is not None:
            for k in self.pv:
                result['Pv'].append(k.to_map() if k else None)
        else:
            result['Pv'] = None
        return result

    def from_map(self, map={}):
        self.pv = []
        if map.get('Pv') is not None:
            for k in map.get('Pv'):
                temp_model = GetPvIdentSimulationValuesResponseDataPvIdentSimulateDataInfoPv()
                self.pv.append(temp_model.from_map(k))
        else:
            self.pv = None
        return self


class GetPvIdentSimulationValuesResponseData(TeaModel):
    def __init__(self, status=None, pv_ident_simulate_data_info=None):
        self.status = status            # type: bool
        self.pv_ident_simulate_data_info = pv_ident_simulate_data_info  # type: GetPvIdentSimulationValuesResponseDataPvIdentSimulateDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.pv_ident_simulate_data_info, 'pv_ident_simulate_data_info')
        if self.pv_ident_simulate_data_info:
            self.pv_ident_simulate_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.pv_ident_simulate_data_info is not None:
            result['PvIdentSimulateDataInfo'] = self.pv_ident_simulate_data_info.to_map()
        else:
            result['PvIdentSimulateDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('PvIdentSimulateDataInfo') is not None:
            temp_model = GetPvIdentSimulationValuesResponseDataPvIdentSimulateDataInfo()
            self.pv_ident_simulate_data_info = temp_model.from_map(map['PvIdentSimulateDataInfo'])
        else:
            self.pv_ident_simulate_data_info = None
        return self


class GetCustomIdentValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetCustomIdentValuesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.data = data                # type: GetCustomIdentValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetCustomIdentValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetCustomIdentValuesResponseDataCustomIdentDataInfoCustomModelTrend(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetCustomIdentValuesResponseDataCustomIdentDataInfoCustomResidual(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None, quality=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str
        self.quality = quality          # type: int

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')
        self.validate_required(self.quality, 'quality')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        result['Quality'] = self.quality
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        self.quality = map.get('Quality')
        return self


class GetCustomIdentValuesResponseDataCustomIdentDataInfo(TeaModel):
    def __init__(self, custom_model_trend=None, custom_residual=None):
        self.custom_model_trend = custom_model_trend  # type: List[GetCustomIdentValuesResponseDataCustomIdentDataInfoCustomModelTrend]
        self.custom_residual = custom_residual  # type: List[GetCustomIdentValuesResponseDataCustomIdentDataInfoCustomResidual]

    def validate(self):
        self.validate_required(self.custom_model_trend, 'custom_model_trend')
        if self.custom_model_trend:
            for k in self.custom_model_trend:
                if k:
                    k.validate()
        self.validate_required(self.custom_residual, 'custom_residual')
        if self.custom_residual:
            for k in self.custom_residual:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CustomModelTrend'] = []
        if self.custom_model_trend is not None:
            for k in self.custom_model_trend:
                result['CustomModelTrend'].append(k.to_map() if k else None)
        else:
            result['CustomModelTrend'] = None
        result['CustomResidual'] = []
        if self.custom_residual is not None:
            for k in self.custom_residual:
                result['CustomResidual'].append(k.to_map() if k else None)
        else:
            result['CustomResidual'] = None
        return result

    def from_map(self, map={}):
        self.custom_model_trend = []
        if map.get('CustomModelTrend') is not None:
            for k in map.get('CustomModelTrend'):
                temp_model = GetCustomIdentValuesResponseDataCustomIdentDataInfoCustomModelTrend()
                self.custom_model_trend.append(temp_model.from_map(k))
        else:
            self.custom_model_trend = None
        self.custom_residual = []
        if map.get('CustomResidual') is not None:
            for k in map.get('CustomResidual'):
                temp_model = GetCustomIdentValuesResponseDataCustomIdentDataInfoCustomResidual()
                self.custom_residual.append(temp_model.from_map(k))
        else:
            self.custom_residual = None
        return self


class GetCustomIdentValuesResponseData(TeaModel):
    def __init__(self, status=None, custom_ident_data_info=None):
        self.status = status            # type: bool
        self.custom_ident_data_info = custom_ident_data_info  # type: GetCustomIdentValuesResponseDataCustomIdentDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.custom_ident_data_info, 'custom_ident_data_info')
        if self.custom_ident_data_info:
            self.custom_ident_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.custom_ident_data_info is not None:
            result['CustomIdentDataInfo'] = self.custom_ident_data_info.to_map()
        else:
            result['CustomIdentDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('CustomIdentDataInfo') is not None:
            temp_model = GetCustomIdentValuesResponseDataCustomIdentDataInfo()
            self.custom_ident_data_info = temp_model.from_map(map['CustomIdentDataInfo'])
        else:
            self.custom_ident_data_info = None
        return self


class GetPidProjectReportOverviewRequest(TeaModel):
    def __init__(self, pid_project_id=None, start_time=None, end_time=None):
        self.pid_project_id = pid_project_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class GetPidProjectReportOverviewResponse(TeaModel):
    def __init__(self, request_id=None, code=None, success=None, message=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.message = message          # type: str
        self.data = data                # type: GetPidProjectReportOverviewResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Success'] = self.success
        result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.message = map.get('Message')
        if map.get('Data') is not None:
            temp_model = GetPidProjectReportOverviewResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetPidProjectReportOverviewResponseDataAllPerformMetricsList(TeaModel):
    def __init__(self, xlabel=None, ylabel=None):
        self.xlabel = xlabel            # type: str
        self.ylabel = ylabel            # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetPidProjectReportOverviewResponseDataKeyPerformMetricsList(TeaModel):
    def __init__(self, xlabel=None, ylabel=None):
        self.xlabel = xlabel            # type: str
        self.ylabel = ylabel            # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetPidProjectReportOverviewResponseDataAllOperationRateList(TeaModel):
    def __init__(self, xlabel=None, ylabel=None):
        self.xlabel = xlabel            # type: str
        self.ylabel = ylabel            # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetPidProjectReportOverviewResponseDataKeyOperationRateList(TeaModel):
    def __init__(self, xlabel=None, ylabel=None):
        self.xlabel = xlabel            # type: str
        self.ylabel = ylabel            # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetPidProjectReportOverviewResponseDataLoopScoreList(TeaModel):
    def __init__(self, xlabel=None, ylabel=None):
        self.xlabel = xlabel            # type: str
        self.ylabel = ylabel            # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetPidProjectReportOverviewResponseDataLoopOperationRateList(TeaModel):
    def __init__(self, xlabel=None, ylabel=None):
        self.xlabel = xlabel            # type: str
        self.ylabel = ylabel            # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetPidProjectReportOverviewResponseDataStatusAll(TeaModel):
    def __init__(self, best=None, good=None, middle=None, bad=None, open_loop=None):
        self.best = best                # type: int
        self.good = good                # type: int
        self.middle = middle            # type: int
        self.bad = bad                  # type: int
        self.open_loop = open_loop      # type: int

    def validate(self):
        self.validate_required(self.best, 'best')
        self.validate_required(self.good, 'good')
        self.validate_required(self.middle, 'middle')
        self.validate_required(self.bad, 'bad')
        self.validate_required(self.open_loop, 'open_loop')

    def to_map(self):
        result = {}
        result['Best'] = self.best
        result['Good'] = self.good
        result['Middle'] = self.middle
        result['Bad'] = self.bad
        result['OpenLoop'] = self.open_loop
        return result

    def from_map(self, map={}):
        self.best = map.get('Best')
        self.good = map.get('Good')
        self.middle = map.get('Middle')
        self.bad = map.get('Bad')
        self.open_loop = map.get('OpenLoop')
        return self


class GetPidProjectReportOverviewResponseDataStatusKey(TeaModel):
    def __init__(self, best=None, good=None, middle=None, bad=None, open_loop=None):
        self.best = best                # type: int
        self.good = good                # type: int
        self.middle = middle            # type: int
        self.bad = bad                  # type: int
        self.open_loop = open_loop      # type: int

    def validate(self):
        self.validate_required(self.best, 'best')
        self.validate_required(self.good, 'good')
        self.validate_required(self.middle, 'middle')
        self.validate_required(self.bad, 'bad')
        self.validate_required(self.open_loop, 'open_loop')

    def to_map(self):
        result = {}
        result['Best'] = self.best
        result['Good'] = self.good
        result['Middle'] = self.middle
        result['Bad'] = self.bad
        result['OpenLoop'] = self.open_loop
        return result

    def from_map(self, map={}):
        self.best = map.get('Best')
        self.good = map.get('Good')
        self.middle = map.get('Middle')
        self.bad = map.get('Bad')
        self.open_loop = map.get('OpenLoop')
        return self


class GetPidProjectReportOverviewResponseDataStatus(TeaModel):
    def __init__(self, all=None, key=None):
        self.all = all                  # type: GetPidProjectReportOverviewResponseDataStatusAll
        self.key = key                  # type: GetPidProjectReportOverviewResponseDataStatusKey

    def validate(self):
        self.validate_required(self.all, 'all')
        if self.all:
            self.all.validate()
        self.validate_required(self.key, 'key')
        if self.key:
            self.key.validate()

    def to_map(self):
        result = {}
        if self.all is not None:
            result['All'] = self.all.to_map()
        else:
            result['All'] = None
        if self.key is not None:
            result['Key'] = self.key.to_map()
        else:
            result['Key'] = None
        return result

    def from_map(self, map={}):
        if map.get('All') is not None:
            temp_model = GetPidProjectReportOverviewResponseDataStatusAll()
            self.all = temp_model.from_map(map['All'])
        else:
            self.all = None
        if map.get('Key') is not None:
            temp_model = GetPidProjectReportOverviewResponseDataStatusKey()
            self.key = temp_model.from_map(map['Key'])
        else:
            self.key = None
        return self


class GetPidProjectReportOverviewResponseData(TeaModel):
    def __init__(self, perform_metrics=None, operation_rate=None, all_perform_metrics_list=None,
                 key_perform_metrics_list=None, all_operation_rate_list=None, key_operation_rate_list=None, loop_score_list=None,
                 loop_operation_rate_list=None, status=None):
        self.perform_metrics = perform_metrics  # type: float
        self.operation_rate = operation_rate  # type: int
        self.all_perform_metrics_list = all_perform_metrics_list  # type: List[GetPidProjectReportOverviewResponseDataAllPerformMetricsList]
        self.key_perform_metrics_list = key_perform_metrics_list  # type: List[GetPidProjectReportOverviewResponseDataKeyPerformMetricsList]
        self.all_operation_rate_list = all_operation_rate_list  # type: List[GetPidProjectReportOverviewResponseDataAllOperationRateList]
        self.key_operation_rate_list = key_operation_rate_list  # type: List[GetPidProjectReportOverviewResponseDataKeyOperationRateList]
        self.loop_score_list = loop_score_list  # type: List[GetPidProjectReportOverviewResponseDataLoopScoreList]
        self.loop_operation_rate_list = loop_operation_rate_list  # type: List[GetPidProjectReportOverviewResponseDataLoopOperationRateList]
        self.status = status            # type: GetPidProjectReportOverviewResponseDataStatus

    def validate(self):
        self.validate_required(self.perform_metrics, 'perform_metrics')
        self.validate_required(self.operation_rate, 'operation_rate')
        self.validate_required(self.all_perform_metrics_list, 'all_perform_metrics_list')
        if self.all_perform_metrics_list:
            for k in self.all_perform_metrics_list:
                if k:
                    k.validate()
        self.validate_required(self.key_perform_metrics_list, 'key_perform_metrics_list')
        if self.key_perform_metrics_list:
            for k in self.key_perform_metrics_list:
                if k:
                    k.validate()
        self.validate_required(self.all_operation_rate_list, 'all_operation_rate_list')
        if self.all_operation_rate_list:
            for k in self.all_operation_rate_list:
                if k:
                    k.validate()
        self.validate_required(self.key_operation_rate_list, 'key_operation_rate_list')
        if self.key_operation_rate_list:
            for k in self.key_operation_rate_list:
                if k:
                    k.validate()
        self.validate_required(self.loop_score_list, 'loop_score_list')
        if self.loop_score_list:
            for k in self.loop_score_list:
                if k:
                    k.validate()
        self.validate_required(self.loop_operation_rate_list, 'loop_operation_rate_list')
        if self.loop_operation_rate_list:
            for k in self.loop_operation_rate_list:
                if k:
                    k.validate()
        self.validate_required(self.status, 'status')
        if self.status:
            self.status.validate()

    def to_map(self):
        result = {}
        result['PerformMetrics'] = self.perform_metrics
        result['OperationRate'] = self.operation_rate
        result['AllPerformMetricsList'] = []
        if self.all_perform_metrics_list is not None:
            for k in self.all_perform_metrics_list:
                result['AllPerformMetricsList'].append(k.to_map() if k else None)
        else:
            result['AllPerformMetricsList'] = None
        result['KeyPerformMetricsList'] = []
        if self.key_perform_metrics_list is not None:
            for k in self.key_perform_metrics_list:
                result['KeyPerformMetricsList'].append(k.to_map() if k else None)
        else:
            result['KeyPerformMetricsList'] = None
        result['AllOperationRateList'] = []
        if self.all_operation_rate_list is not None:
            for k in self.all_operation_rate_list:
                result['AllOperationRateList'].append(k.to_map() if k else None)
        else:
            result['AllOperationRateList'] = None
        result['KeyOperationRateList'] = []
        if self.key_operation_rate_list is not None:
            for k in self.key_operation_rate_list:
                result['KeyOperationRateList'].append(k.to_map() if k else None)
        else:
            result['KeyOperationRateList'] = None
        result['LoopScoreList'] = []
        if self.loop_score_list is not None:
            for k in self.loop_score_list:
                result['LoopScoreList'].append(k.to_map() if k else None)
        else:
            result['LoopScoreList'] = None
        result['LoopOperationRateList'] = []
        if self.loop_operation_rate_list is not None:
            for k in self.loop_operation_rate_list:
                result['LoopOperationRateList'].append(k.to_map() if k else None)
        else:
            result['LoopOperationRateList'] = None
        if self.status is not None:
            result['Status'] = self.status.to_map()
        else:
            result['Status'] = None
        return result

    def from_map(self, map={}):
        self.perform_metrics = map.get('PerformMetrics')
        self.operation_rate = map.get('OperationRate')
        self.all_perform_metrics_list = []
        if map.get('AllPerformMetricsList') is not None:
            for k in map.get('AllPerformMetricsList'):
                temp_model = GetPidProjectReportOverviewResponseDataAllPerformMetricsList()
                self.all_perform_metrics_list.append(temp_model.from_map(k))
        else:
            self.all_perform_metrics_list = None
        self.key_perform_metrics_list = []
        if map.get('KeyPerformMetricsList') is not None:
            for k in map.get('KeyPerformMetricsList'):
                temp_model = GetPidProjectReportOverviewResponseDataKeyPerformMetricsList()
                self.key_perform_metrics_list.append(temp_model.from_map(k))
        else:
            self.key_perform_metrics_list = None
        self.all_operation_rate_list = []
        if map.get('AllOperationRateList') is not None:
            for k in map.get('AllOperationRateList'):
                temp_model = GetPidProjectReportOverviewResponseDataAllOperationRateList()
                self.all_operation_rate_list.append(temp_model.from_map(k))
        else:
            self.all_operation_rate_list = None
        self.key_operation_rate_list = []
        if map.get('KeyOperationRateList') is not None:
            for k in map.get('KeyOperationRateList'):
                temp_model = GetPidProjectReportOverviewResponseDataKeyOperationRateList()
                self.key_operation_rate_list.append(temp_model.from_map(k))
        else:
            self.key_operation_rate_list = None
        self.loop_score_list = []
        if map.get('LoopScoreList') is not None:
            for k in map.get('LoopScoreList'):
                temp_model = GetPidProjectReportOverviewResponseDataLoopScoreList()
                self.loop_score_list.append(temp_model.from_map(k))
        else:
            self.loop_score_list = None
        self.loop_operation_rate_list = []
        if map.get('LoopOperationRateList') is not None:
            for k in map.get('LoopOperationRateList'):
                temp_model = GetPidProjectReportOverviewResponseDataLoopOperationRateList()
                self.loop_operation_rate_list.append(temp_model.from_map(k))
        else:
            self.loop_operation_rate_list = None
        if map.get('Status') is not None:
            temp_model = GetPidProjectReportOverviewResponseDataStatus()
            self.status = temp_model.from_map(map['Status'])
        else:
            self.status = None
        return self


class GetLowModelPerformValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetLowModelPerformValuesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, data=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: Dict[str, Any]
        self.data = data                # type: GetLowModelPerformValuesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('Data') is not None:
            temp_model = GetLowModelPerformValuesResponseData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetLowModelPerformValuesResponseDataLowModelPerformDataInfoManualModel(TeaModel):
    def __init__(self, k=None, tau=None, t_1=None, t_2=None):
        self.k = k                      # type: float
        self.tau = tau                  # type: float
        self.t_1 = t_1                  # type: float
        self.t_2 = t_2                  # type: float

    def validate(self):
        self.validate_required(self.k, 'k')
        self.validate_required(self.tau, 'tau')
        self.validate_required(self.t_1, 't_1')
        self.validate_required(self.t_2, 't_2')

    def to_map(self):
        result = {}
        result['K'] = self.k
        result['Tau'] = self.tau
        result['T1'] = self.t_1
        result['T2'] = self.t_2
        return result

    def from_map(self, map={}):
        self.k = map.get('K')
        self.tau = map.get('Tau')
        self.t_1 = map.get('T1')
        self.t_2 = map.get('T2')
        return self


class GetLowModelPerformValuesResponseDataLowModelPerformDataInfo(TeaModel):
    def __init__(self, confidence=None, fit_degree=None, manual_model=None):
        self.confidence = confidence    # type: float
        self.fit_degree = fit_degree    # type: float
        self.manual_model = manual_model  # type: GetLowModelPerformValuesResponseDataLowModelPerformDataInfoManualModel

    def validate(self):
        self.validate_required(self.confidence, 'confidence')
        self.validate_required(self.fit_degree, 'fit_degree')
        self.validate_required(self.manual_model, 'manual_model')
        if self.manual_model:
            self.manual_model.validate()

    def to_map(self):
        result = {}
        result['Confidence'] = self.confidence
        result['FitDegree'] = self.fit_degree
        if self.manual_model is not None:
            result['ManualModel'] = self.manual_model.to_map()
        else:
            result['ManualModel'] = None
        return result

    def from_map(self, map={}):
        self.confidence = map.get('Confidence')
        self.fit_degree = map.get('FitDegree')
        if map.get('ManualModel') is not None:
            temp_model = GetLowModelPerformValuesResponseDataLowModelPerformDataInfoManualModel()
            self.manual_model = temp_model.from_map(map['ManualModel'])
        else:
            self.manual_model = None
        return self


class GetLowModelPerformValuesResponseData(TeaModel):
    def __init__(self, status=None, low_model_perform_data_info=None):
        self.status = status            # type: bool
        self.low_model_perform_data_info = low_model_perform_data_info  # type: GetLowModelPerformValuesResponseDataLowModelPerformDataInfo

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.low_model_perform_data_info, 'low_model_perform_data_info')
        if self.low_model_perform_data_info:
            self.low_model_perform_data_info.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.low_model_perform_data_info is not None:
            result['LowModelPerformDataInfo'] = self.low_model_perform_data_info.to_map()
        else:
            result['LowModelPerformDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('LowModelPerformDataInfo') is not None:
            temp_model = GetLowModelPerformValuesResponseDataLowModelPerformDataInfo()
            self.low_model_perform_data_info = temp_model.from_map(map['LowModelPerformDataInfo'])
        else:
            self.low_model_perform_data_info = None
        return self


class ListPidLoopEvaluationsRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, pid_project_id=None, order=None, order_by_property=None,
                 pid_loop_name=None, grade=None, date=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.pid_project_id = pid_project_id  # type: str
        self.order = order              # type: str
        self.order_by_property = order_by_property  # type: str
        self.pid_loop_name = pid_loop_name  # type: str
        self.grade = grade              # type: str
        self.date = date                # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')

    def to_map(self):
        result = {}
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        result['PidProjectId'] = self.pid_project_id
        result['Order'] = self.order
        result['OrderByProperty'] = self.order_by_property
        result['PidLoopName'] = self.pid_loop_name
        result['Grade'] = self.grade
        result['Date'] = self.date
        return result

    def from_map(self, map={}):
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        self.pid_project_id = map.get('PidProjectId')
        self.order = map.get('Order')
        self.order_by_property = map.get('OrderByProperty')
        self.pid_loop_name = map.get('PidLoopName')
        self.grade = map.get('Grade')
        self.date = map.get('Date')
        return self


class ListPidLoopEvaluationsResponse(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, success=None, current_page=None, page_size=None,
                 total_count=None, data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.message = message          # type: str
        self.success = success          # type: bool
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.data = data                # type: List[ListPidLoopEvaluationsResponseData]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.success, 'success')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Message'] = self.message
        result['Success'] = self.success
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.success = map.get('Success')
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.data = []
        if map.get('Data') is not None:
            for k in map.get('Data'):
                temp_model = ListPidLoopEvaluationsResponseData()
                self.data.append(temp_model.from_map(k))
        else:
            self.data = None
        return self


class ListPidLoopEvaluationsResponseData(TeaModel):
    def __init__(self, after_pid_parameters=None, before_pid_parameters=None, pid_loop_remark=None,
                 assess_time=None, robust=None, valid_operation_rate=None, operation_rate=None, perform_metrics=None,
                 multiple_score=None, grade=None, pid_loop_name=None, pid_project_id=None, pid_loop_id=None,
                 pid_loop_parameter_id=None):
        self.after_pid_parameters = after_pid_parameters  # type: Dict[str, Any]
        self.before_pid_parameters = before_pid_parameters  # type: Dict[str, Any]
        self.pid_loop_remark = pid_loop_remark  # type: str
        self.assess_time = assess_time  # type: int
        self.robust = robust            # type: float
        self.valid_operation_rate = valid_operation_rate  # type: float
        self.operation_rate = operation_rate  # type: float
        self.perform_metrics = perform_metrics  # type: float
        self.multiple_score = multiple_score  # type: float
        self.grade = grade              # type: str
        self.pid_loop_name = pid_loop_name  # type: str
        self.pid_project_id = pid_project_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str

    def validate(self):
        self.validate_required(self.after_pid_parameters, 'after_pid_parameters')
        self.validate_required(self.before_pid_parameters, 'before_pid_parameters')
        self.validate_required(self.pid_loop_remark, 'pid_loop_remark')
        self.validate_required(self.assess_time, 'assess_time')
        self.validate_required(self.robust, 'robust')
        self.validate_required(self.valid_operation_rate, 'valid_operation_rate')
        self.validate_required(self.operation_rate, 'operation_rate')
        self.validate_required(self.perform_metrics, 'perform_metrics')
        self.validate_required(self.multiple_score, 'multiple_score')
        self.validate_required(self.grade, 'grade')
        self.validate_required(self.pid_loop_name, 'pid_loop_name')
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')

    def to_map(self):
        result = {}
        result['AfterPidParameters'] = self.after_pid_parameters
        result['BeforePidParameters'] = self.before_pid_parameters
        result['PidLoopRemark'] = self.pid_loop_remark
        result['AssessTime'] = self.assess_time
        result['Robust'] = self.robust
        result['ValidOperationRate'] = self.valid_operation_rate
        result['OperationRate'] = self.operation_rate
        result['PerformMetrics'] = self.perform_metrics
        result['MultipleScore'] = self.multiple_score
        result['Grade'] = self.grade
        result['PidLoopName'] = self.pid_loop_name
        result['PidProjectId'] = self.pid_project_id
        result['PidLoopId'] = self.pid_loop_id
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        return result

    def from_map(self, map={}):
        self.after_pid_parameters = map.get('AfterPidParameters')
        self.before_pid_parameters = map.get('BeforePidParameters')
        self.pid_loop_remark = map.get('PidLoopRemark')
        self.assess_time = map.get('AssessTime')
        self.robust = map.get('Robust')
        self.valid_operation_rate = map.get('ValidOperationRate')
        self.operation_rate = map.get('OperationRate')
        self.perform_metrics = map.get('PerformMetrics')
        self.multiple_score = map.get('MultipleScore')
        self.grade = map.get('Grade')
        self.pid_loop_name = map.get('PidLoopName')
        self.pid_project_id = map.get('PidProjectId')
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        return self


class ListLoopParameterTagValuesRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, data_start_time=None, data_end_time=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.data_start_time = data_start_time  # type: str
        self.data_end_time = data_end_time  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['DataStartTime'] = self.data_start_time
        result['DataEndTime'] = self.data_end_time
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.data_start_time = map.get('DataStartTime')
        self.data_end_time = map.get('DataEndTime')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class ListLoopParameterTagValuesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, tags_values_rsp=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.tags_values_rsp = tags_values_rsp  # type: ListLoopParameterTagValuesResponseTagsValuesRsp

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.tags_values_rsp, 'tags_values_rsp')
        if self.tags_values_rsp:
            self.tags_values_rsp.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.tags_values_rsp is not None:
            result['TagsValuesRsp'] = self.tags_values_rsp.to_map()
        else:
            result['TagsValuesRsp'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('TagsValuesRsp') is not None:
            temp_model = ListLoopParameterTagValuesResponseTagsValuesRsp()
            self.tags_values_rsp = temp_model.from_map(map['TagsValuesRsp'])
        else:
            self.tags_values_rsp = None
        return self


class ListLoopParameterTagValuesResponseTagsValuesRspDataListOp(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class ListLoopParameterTagValuesResponseTagsValuesRspDataListOp1(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class ListLoopParameterTagValuesResponseTagsValuesRspDataListOp2(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class ListLoopParameterTagValuesResponseTagsValuesRspDataListSp(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class ListLoopParameterTagValuesResponseTagsValuesRspDataListPv(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class ListLoopParameterTagValuesResponseTagsValuesRspDataList(TeaModel):
    def __init__(self, op=None, op_1=None, op_2=None, sp=None, pv=None):
        self.op = op                    # type: List[ListLoopParameterTagValuesResponseTagsValuesRspDataListOp]
        self.op_1 = op_1                # type: List[ListLoopParameterTagValuesResponseTagsValuesRspDataListOp1]
        self.op_2 = op_2                # type: List[ListLoopParameterTagValuesResponseTagsValuesRspDataListOp2]
        self.sp = sp                    # type: List[ListLoopParameterTagValuesResponseTagsValuesRspDataListSp]
        self.pv = pv                    # type: List[ListLoopParameterTagValuesResponseTagsValuesRspDataListPv]

    def validate(self):
        self.validate_required(self.op, 'op')
        if self.op:
            for k in self.op:
                if k:
                    k.validate()
        self.validate_required(self.op_1, 'op_1')
        if self.op_1:
            for k in self.op_1:
                if k:
                    k.validate()
        self.validate_required(self.op_2, 'op_2')
        if self.op_2:
            for k in self.op_2:
                if k:
                    k.validate()
        self.validate_required(self.sp, 'sp')
        if self.sp:
            for k in self.sp:
                if k:
                    k.validate()
        self.validate_required(self.pv, 'pv')
        if self.pv:
            for k in self.pv:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Op'] = []
        if self.op is not None:
            for k in self.op:
                result['Op'].append(k.to_map() if k else None)
        else:
            result['Op'] = None
        result['Op1'] = []
        if self.op_1 is not None:
            for k in self.op_1:
                result['Op1'].append(k.to_map() if k else None)
        else:
            result['Op1'] = None
        result['Op2'] = []
        if self.op_2 is not None:
            for k in self.op_2:
                result['Op2'].append(k.to_map() if k else None)
        else:
            result['Op2'] = None
        result['Sp'] = []
        if self.sp is not None:
            for k in self.sp:
                result['Sp'].append(k.to_map() if k else None)
        else:
            result['Sp'] = None
        result['Pv'] = []
        if self.pv is not None:
            for k in self.pv:
                result['Pv'].append(k.to_map() if k else None)
        else:
            result['Pv'] = None
        return result

    def from_map(self, map={}):
        self.op = []
        if map.get('Op') is not None:
            for k in map.get('Op'):
                temp_model = ListLoopParameterTagValuesResponseTagsValuesRspDataListOp()
                self.op.append(temp_model.from_map(k))
        else:
            self.op = None
        self.op_1 = []
        if map.get('Op1') is not None:
            for k in map.get('Op1'):
                temp_model = ListLoopParameterTagValuesResponseTagsValuesRspDataListOp1()
                self.op_1.append(temp_model.from_map(k))
        else:
            self.op_1 = None
        self.op_2 = []
        if map.get('Op2') is not None:
            for k in map.get('Op2'):
                temp_model = ListLoopParameterTagValuesResponseTagsValuesRspDataListOp2()
                self.op_2.append(temp_model.from_map(k))
        else:
            self.op_2 = None
        self.sp = []
        if map.get('Sp') is not None:
            for k in map.get('Sp'):
                temp_model = ListLoopParameterTagValuesResponseTagsValuesRspDataListSp()
                self.sp.append(temp_model.from_map(k))
        else:
            self.sp = None
        self.pv = []
        if map.get('Pv') is not None:
            for k in map.get('Pv'):
                temp_model = ListLoopParameterTagValuesResponseTagsValuesRspDataListPv()
                self.pv.append(temp_model.from_map(k))
        else:
            self.pv = None
        return self


class ListLoopParameterTagValuesResponseTagsValuesRsp(TeaModel):
    def __init__(self, status=None, data_list=None):
        self.status = status            # type: bool
        self.data_list = data_list      # type: ListLoopParameterTagValuesResponseTagsValuesRspDataList

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.data_list, 'data_list')
        if self.data_list:
            self.data_list.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.data_list is not None:
            result['DataList'] = self.data_list.to_map()
        else:
            result['DataList'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('DataList') is not None:
            temp_model = ListLoopParameterTagValuesResponseTagsValuesRspDataList()
            self.data_list = temp_model.from_map(map['DataList'])
        else:
            self.data_list = None
        return self


class GetPidLoopParameterRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetPidLoopParameterResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_loop_parameter=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_loop_parameter = pid_loop_parameter  # type: GetPidLoopParameterResponsePidLoopParameter

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_loop_parameter, 'pid_loop_parameter')
        if self.pid_loop_parameter:
            self.pid_loop_parameter.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.pid_loop_parameter is not None:
            result['PidLoopParameter'] = self.pid_loop_parameter.to_map()
        else:
            result['PidLoopParameter'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('PidLoopParameter') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameter()
            self.pid_loop_parameter = temp_model.from_map(map['PidLoopParameter'])
        else:
            self.pid_loop_parameter = None
        return self


class GetPidLoopParameterResponsePidLoopParameterPidIdentParamLimitMax(TeaModel):
    def __init__(self, k=None, tau=None, t_1=None, t_2=None):
        self.k = k                      # type: float
        self.tau = tau                  # type: float
        self.t_1 = t_1                  # type: float
        self.t_2 = t_2                  # type: float

    def validate(self):
        self.validate_required(self.k, 'k')
        self.validate_required(self.tau, 'tau')
        self.validate_required(self.t_1, 't_1')
        self.validate_required(self.t_2, 't_2')

    def to_map(self):
        result = {}
        result['K'] = self.k
        result['Tau'] = self.tau
        result['T1'] = self.t_1
        result['T2'] = self.t_2
        return result

    def from_map(self, map={}):
        self.k = map.get('K')
        self.tau = map.get('Tau')
        self.t_1 = map.get('T1')
        self.t_2 = map.get('T2')
        return self


class GetPidLoopParameterResponsePidLoopParameterPidIdentParamLimitMin(TeaModel):
    def __init__(self, k=None, tau=None, t_1=None, t_2=None):
        self.k = k                      # type: float
        self.tau = tau                  # type: float
        self.t_1 = t_1                  # type: float
        self.t_2 = t_2                  # type: float

    def validate(self):
        self.validate_required(self.k, 'k')
        self.validate_required(self.tau, 'tau')
        self.validate_required(self.t_1, 't_1')
        self.validate_required(self.t_2, 't_2')

    def to_map(self):
        result = {}
        result['K'] = self.k
        result['Tau'] = self.tau
        result['T1'] = self.t_1
        result['T2'] = self.t_2
        return result

    def from_map(self, map={}):
        self.k = map.get('K')
        self.tau = map.get('Tau')
        self.t_1 = map.get('T1')
        self.t_2 = map.get('T2')
        return self


class GetPidLoopParameterResponsePidLoopParameterPidIdentParamManualModel(TeaModel):
    def __init__(self, k=None, tau=None, t_1=None, t_2=None):
        self.k = k                      # type: float
        self.tau = tau                  # type: float
        self.t_1 = t_1                  # type: float
        self.t_2 = t_2                  # type: float

    def validate(self):
        self.validate_required(self.k, 'k')
        self.validate_required(self.tau, 'tau')
        self.validate_required(self.t_1, 't_1')
        self.validate_required(self.t_2, 't_2')

    def to_map(self):
        result = {}
        result['K'] = self.k
        result['Tau'] = self.tau
        result['T1'] = self.t_1
        result['T2'] = self.t_2
        return result

    def from_map(self, map={}):
        self.k = map.get('K')
        self.tau = map.get('Tau')
        self.t_1 = map.get('T1')
        self.t_2 = map.get('T2')
        return self


class GetPidLoopParameterResponsePidLoopParameterPidIdentParam(TeaModel):
    def __init__(self, model_type=None, integral=None, trend_control=None, delay=None, smooth=None, robust=None,
                 limit_sw=None, manual_trend=None, start_time=None, end_time=None, pid_data_process_id=None, limit_max=None,
                 limit_min=None, manual_model=None):
        self.model_type = model_type    # type: int
        self.integral = integral        # type: bool
        self.trend_control = trend_control  # type: bool
        self.delay = delay              # type: int
        self.smooth = smooth            # type: int
        self.robust = robust            # type: int
        self.limit_sw = limit_sw        # type: bool
        self.manual_trend = manual_trend  # type: bool
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.pid_data_process_id = pid_data_process_id  # type: int
        self.limit_max = limit_max      # type: GetPidLoopParameterResponsePidLoopParameterPidIdentParamLimitMax
        self.limit_min = limit_min      # type: GetPidLoopParameterResponsePidLoopParameterPidIdentParamLimitMin
        self.manual_model = manual_model  # type: GetPidLoopParameterResponsePidLoopParameterPidIdentParamManualModel

    def validate(self):
        self.validate_required(self.model_type, 'model_type')
        self.validate_required(self.integral, 'integral')
        self.validate_required(self.trend_control, 'trend_control')
        self.validate_required(self.delay, 'delay')
        self.validate_required(self.smooth, 'smooth')
        self.validate_required(self.robust, 'robust')
        self.validate_required(self.limit_sw, 'limit_sw')
        self.validate_required(self.manual_trend, 'manual_trend')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.pid_data_process_id, 'pid_data_process_id')
        self.validate_required(self.limit_max, 'limit_max')
        if self.limit_max:
            self.limit_max.validate()
        self.validate_required(self.limit_min, 'limit_min')
        if self.limit_min:
            self.limit_min.validate()
        self.validate_required(self.manual_model, 'manual_model')
        if self.manual_model:
            self.manual_model.validate()

    def to_map(self):
        result = {}
        result['ModelType'] = self.model_type
        result['Integral'] = self.integral
        result['TrendControl'] = self.trend_control
        result['Delay'] = self.delay
        result['Smooth'] = self.smooth
        result['Robust'] = self.robust
        result['LimitSw'] = self.limit_sw
        result['ManualTrend'] = self.manual_trend
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PidDataProcessId'] = self.pid_data_process_id
        if self.limit_max is not None:
            result['LimitMax'] = self.limit_max.to_map()
        else:
            result['LimitMax'] = None
        if self.limit_min is not None:
            result['LimitMin'] = self.limit_min.to_map()
        else:
            result['LimitMin'] = None
        if self.manual_model is not None:
            result['ManualModel'] = self.manual_model.to_map()
        else:
            result['ManualModel'] = None
        return result

    def from_map(self, map={}):
        self.model_type = map.get('ModelType')
        self.integral = map.get('Integral')
        self.trend_control = map.get('TrendControl')
        self.delay = map.get('Delay')
        self.smooth = map.get('Smooth')
        self.robust = map.get('Robust')
        self.limit_sw = map.get('LimitSw')
        self.manual_trend = map.get('ManualTrend')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.pid_data_process_id = map.get('PidDataProcessId')
        if map.get('LimitMax') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPidIdentParamLimitMax()
            self.limit_max = temp_model.from_map(map['LimitMax'])
        else:
            self.limit_max = None
        if map.get('LimitMin') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPidIdentParamLimitMin()
            self.limit_min = temp_model.from_map(map['LimitMin'])
        else:
            self.limit_min = None
        if map.get('ManualModel') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPidIdentParamManualModel()
            self.manual_model = temp_model.from_map(map['ManualModel'])
        else:
            self.manual_model = None
        return self


class GetPidLoopParameterResponsePidLoopParameterPIdResetParamMeasuredValueRange(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopParameterResponsePidLoopParameterPIdResetParamValvePositionRange(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopParameterResponsePidLoopParameterPIdResetParamManualCtrl(TeaModel):
    def __init__(self, kp=None, ti=None, td=None):
        self.kp = kp                    # type: float
        self.ti = ti                    # type: float
        self.td = td                    # type: float

    def validate(self):
        self.validate_required(self.kp, 'kp')
        self.validate_required(self.ti, 'ti')
        self.validate_required(self.td, 'td')

    def to_map(self):
        result = {}
        result['Kp'] = self.kp
        result['Ti'] = self.ti
        result['Td'] = self.td
        return result

    def from_map(self, map={}):
        self.kp = map.get('Kp')
        self.ti = map.get('Ti')
        self.td = map.get('Td')
        return self


class GetPidLoopParameterResponsePidLoopParameterPIdResetParam(TeaModel):
    def __init__(self, dcs_type=None, model=None, model_type=None, integral=None, ctrl_mode=None, ctrl_stuc=None,
                 robust=None, dynamic=None, manual_trend=None, measured_value_range=None, valve_position_range=None,
                 manual_ctrl=None):
        self.dcs_type = dcs_type        # type: str
        self.model = model              # type: str
        self.model_type = model_type    # type: int
        self.integral = integral        # type: bool
        self.ctrl_mode = ctrl_mode      # type: int
        self.ctrl_stuc = ctrl_stuc      # type: int
        self.robust = robust            # type: int
        self.dynamic = dynamic          # type: float
        self.manual_trend = manual_trend  # type: bool
        self.measured_value_range = measured_value_range  # type: GetPidLoopParameterResponsePidLoopParameterPIdResetParamMeasuredValueRange
        self.valve_position_range = valve_position_range  # type: GetPidLoopParameterResponsePidLoopParameterPIdResetParamValvePositionRange
        self.manual_ctrl = manual_ctrl  # type: GetPidLoopParameterResponsePidLoopParameterPIdResetParamManualCtrl

    def validate(self):
        self.validate_required(self.dcs_type, 'dcs_type')
        self.validate_required(self.model, 'model')
        self.validate_required(self.model_type, 'model_type')
        self.validate_required(self.integral, 'integral')
        self.validate_required(self.ctrl_mode, 'ctrl_mode')
        self.validate_required(self.ctrl_stuc, 'ctrl_stuc')
        self.validate_required(self.robust, 'robust')
        self.validate_required(self.dynamic, 'dynamic')
        self.validate_required(self.manual_trend, 'manual_trend')
        self.validate_required(self.measured_value_range, 'measured_value_range')
        if self.measured_value_range:
            self.measured_value_range.validate()
        self.validate_required(self.valve_position_range, 'valve_position_range')
        if self.valve_position_range:
            self.valve_position_range.validate()
        self.validate_required(self.manual_ctrl, 'manual_ctrl')
        if self.manual_ctrl:
            self.manual_ctrl.validate()

    def to_map(self):
        result = {}
        result['DcsType'] = self.dcs_type
        result['Model'] = self.model
        result['ModelType'] = self.model_type
        result['Integral'] = self.integral
        result['CtrlMode'] = self.ctrl_mode
        result['CtrlStuc'] = self.ctrl_stuc
        result['Robust'] = self.robust
        result['Dynamic'] = self.dynamic
        result['ManualTrend'] = self.manual_trend
        if self.measured_value_range is not None:
            result['MeasuredValueRange'] = self.measured_value_range.to_map()
        else:
            result['MeasuredValueRange'] = None
        if self.valve_position_range is not None:
            result['ValvePositionRange'] = self.valve_position_range.to_map()
        else:
            result['ValvePositionRange'] = None
        if self.manual_ctrl is not None:
            result['ManualCtrl'] = self.manual_ctrl.to_map()
        else:
            result['ManualCtrl'] = None
        return result

    def from_map(self, map={}):
        self.dcs_type = map.get('DcsType')
        self.model = map.get('Model')
        self.model_type = map.get('ModelType')
        self.integral = map.get('Integral')
        self.ctrl_mode = map.get('CtrlMode')
        self.ctrl_stuc = map.get('CtrlStuc')
        self.robust = map.get('Robust')
        self.dynamic = map.get('Dynamic')
        self.manual_trend = map.get('ManualTrend')
        if map.get('MeasuredValueRange') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPIdResetParamMeasuredValueRange()
            self.measured_value_range = temp_model.from_map(map['MeasuredValueRange'])
        else:
            self.measured_value_range = None
        if map.get('ValvePositionRange') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPIdResetParamValvePositionRange()
            self.valve_position_range = temp_model.from_map(map['ValvePositionRange'])
        else:
            self.valve_position_range = None
        if map.get('ManualCtrl') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPIdResetParamManualCtrl()
            self.manual_ctrl = temp_model.from_map(map['ManualCtrl'])
        else:
            self.manual_ctrl = None
        return self


class GetPidLoopParameterResponsePidLoopParameter(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_project_id=None, pid_loop_id=None, pid_ident_task_date=None,
                 pid_reset_task_date=None, pid_ident_param=None, pid_reset_param=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_project_id = pid_project_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_ident_task_date = pid_ident_task_date  # type: str
        self.pid_reset_task_date = pid_reset_task_date  # type: str
        self.pid_ident_param = pid_ident_param  # type: GetPidLoopParameterResponsePidLoopParameterPidIdentParam
        self.pid_reset_param = pid_reset_param  # type: GetPidLoopParameterResponsePidLoopParameterPIdResetParam

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.pid_ident_task_date, 'pid_ident_task_date')
        self.validate_required(self.pid_reset_task_date, 'pid_reset_task_date')
        self.validate_required(self.pid_ident_param, 'pid_ident_param')
        if self.pid_ident_param:
            self.pid_ident_param.validate()
        self.validate_required(self.pid_reset_param, 'pid_reset_param')
        if self.pid_reset_param:
            self.pid_reset_param.validate()

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidProjectId'] = self.pid_project_id
        result['PidLoopId'] = self.pid_loop_id
        result['PidIdentTaskDate'] = self.pid_ident_task_date
        result['PidResetTaskDate'] = self.pid_reset_task_date
        if self.pid_ident_param is not None:
            result['PidIdentParam'] = self.pid_ident_param.to_map()
        else:
            result['PidIdentParam'] = None
        if self.pid_reset_param is not None:
            result['PIdResetParam'] = self.pid_reset_param.to_map()
        else:
            result['PIdResetParam'] = None
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_project_id = map.get('PidProjectId')
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_ident_task_date = map.get('PidIdentTaskDate')
        self.pid_reset_task_date = map.get('PidResetTaskDate')
        if map.get('PidIdentParam') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPidIdentParam()
            self.pid_ident_param = temp_model.from_map(map['PidIdentParam'])
        else:
            self.pid_ident_param = None
        if map.get('PIdResetParam') is not None:
            temp_model = GetPidLoopParameterResponsePidLoopParameterPIdResetParam()
            self.pid_reset_param = temp_model.from_map(map['PIdResetParam'])
        else:
            self.pid_reset_param = None
        return self


class GetDailyReportInfoRequest(TeaModel):
    def __init__(self, pid_loop_id=None, report_date=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.report_date = report_date  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['ReportDate'] = self.report_date
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.report_date = map.get('ReportDate')
        return self


class GetDailyReportInfoResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, day_result_rsp=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.day_result_rsp = day_result_rsp  # type: GetDailyReportInfoResponseDayResultRsp

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.day_result_rsp, 'day_result_rsp')
        if self.day_result_rsp:
            self.day_result_rsp.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.day_result_rsp is not None:
            result['DayResultRsp'] = self.day_result_rsp.to_map()
        else:
            result['DayResultRsp'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('DayResultRsp') is not None:
            temp_model = GetDailyReportInfoResponseDayResultRsp()
            self.day_result_rsp = temp_model.from_map(map['DayResultRsp'])
        else:
            self.day_result_rsp = None
        return self


class GetDailyReportInfoResponseDayResultRspDayResultData(TeaModel):
    def __init__(self, loop_name=None, report_date=None, multiple_score=None, perform_metrics=None,
                 multiple_score_index=None, operation_rate=None, valid_operation_rate=None, oscillation_index=None,
                 valve_stick_index=None, pv_mean=None, pv_std=None, pv_max=None, pv_min=None, err_mean=None, err_std=None, err_max=None,
                 err_min=None, op_mean=None, op_std=None, op_max=None, op_min=None, loop_trans=None, sp_cross=None,
                 op_turn=None, op_sum=None, good_rate=None, satu_rate=None):
        self.loop_name = loop_name      # type: str
        self.report_date = report_date  # type: str
        self.multiple_score = multiple_score  # type: str
        self.perform_metrics = perform_metrics  # type: str
        self.multiple_score_index = multiple_score_index  # type: str
        self.operation_rate = operation_rate  # type: str
        self.valid_operation_rate = valid_operation_rate  # type: str
        self.oscillation_index = oscillation_index  # type: str
        self.valve_stick_index = valve_stick_index  # type: str
        self.pv_mean = pv_mean          # type: str
        self.pv_std = pv_std            # type: str
        self.pv_max = pv_max            # type: str
        self.pv_min = pv_min            # type: str
        self.err_mean = err_mean        # type: str
        self.err_std = err_std          # type: str
        self.err_max = err_max          # type: str
        self.err_min = err_min          # type: str
        self.op_mean = op_mean          # type: str
        self.op_std = op_std            # type: str
        self.op_max = op_max            # type: str
        self.op_min = op_min            # type: str
        self.loop_trans = loop_trans    # type: str
        self.sp_cross = sp_cross        # type: str
        self.op_turn = op_turn          # type: str
        self.op_sum = op_sum            # type: str
        self.good_rate = good_rate      # type: str
        self.satu_rate = satu_rate      # type: str

    def validate(self):
        self.validate_required(self.loop_name, 'loop_name')
        self.validate_required(self.report_date, 'report_date')
        self.validate_required(self.multiple_score, 'multiple_score')
        self.validate_required(self.perform_metrics, 'perform_metrics')
        self.validate_required(self.multiple_score_index, 'multiple_score_index')
        self.validate_required(self.operation_rate, 'operation_rate')
        self.validate_required(self.valid_operation_rate, 'valid_operation_rate')
        self.validate_required(self.oscillation_index, 'oscillation_index')
        self.validate_required(self.valve_stick_index, 'valve_stick_index')
        self.validate_required(self.pv_mean, 'pv_mean')
        self.validate_required(self.pv_std, 'pv_std')
        self.validate_required(self.pv_max, 'pv_max')
        self.validate_required(self.pv_min, 'pv_min')
        self.validate_required(self.err_mean, 'err_mean')
        self.validate_required(self.err_std, 'err_std')
        self.validate_required(self.err_max, 'err_max')
        self.validate_required(self.err_min, 'err_min')
        self.validate_required(self.op_mean, 'op_mean')
        self.validate_required(self.op_std, 'op_std')
        self.validate_required(self.op_max, 'op_max')
        self.validate_required(self.op_min, 'op_min')
        self.validate_required(self.loop_trans, 'loop_trans')
        self.validate_required(self.sp_cross, 'sp_cross')
        self.validate_required(self.op_turn, 'op_turn')
        self.validate_required(self.op_sum, 'op_sum')
        self.validate_required(self.good_rate, 'good_rate')
        self.validate_required(self.satu_rate, 'satu_rate')

    def to_map(self):
        result = {}
        result['LoopName'] = self.loop_name
        result['ReportDate'] = self.report_date
        result['MultipleScore'] = self.multiple_score
        result['PerformMetrics'] = self.perform_metrics
        result['MultipleScoreIndex'] = self.multiple_score_index
        result['OperationRate'] = self.operation_rate
        result['ValidOperationRate'] = self.valid_operation_rate
        result['OscillationIndex'] = self.oscillation_index
        result['ValveStickIndex'] = self.valve_stick_index
        result['PvMean'] = self.pv_mean
        result['PvStd'] = self.pv_std
        result['PvMax'] = self.pv_max
        result['PvMin'] = self.pv_min
        result['ErrMean'] = self.err_mean
        result['ErrStd'] = self.err_std
        result['ErrMax'] = self.err_max
        result['ErrMin'] = self.err_min
        result['OpMean'] = self.op_mean
        result['OpStd'] = self.op_std
        result['OpMax'] = self.op_max
        result['OpMin'] = self.op_min
        result['LoopTrans'] = self.loop_trans
        result['SpCross'] = self.sp_cross
        result['OpTurn'] = self.op_turn
        result['OpSum'] = self.op_sum
        result['GoodRate'] = self.good_rate
        result['SatuRate'] = self.satu_rate
        return result

    def from_map(self, map={}):
        self.loop_name = map.get('LoopName')
        self.report_date = map.get('ReportDate')
        self.multiple_score = map.get('MultipleScore')
        self.perform_metrics = map.get('PerformMetrics')
        self.multiple_score_index = map.get('MultipleScoreIndex')
        self.operation_rate = map.get('OperationRate')
        self.valid_operation_rate = map.get('ValidOperationRate')
        self.oscillation_index = map.get('OscillationIndex')
        self.valve_stick_index = map.get('ValveStickIndex')
        self.pv_mean = map.get('PvMean')
        self.pv_std = map.get('PvStd')
        self.pv_max = map.get('PvMax')
        self.pv_min = map.get('PvMin')
        self.err_mean = map.get('ErrMean')
        self.err_std = map.get('ErrStd')
        self.err_max = map.get('ErrMax')
        self.err_min = map.get('ErrMin')
        self.op_mean = map.get('OpMean')
        self.op_std = map.get('OpStd')
        self.op_max = map.get('OpMax')
        self.op_min = map.get('OpMin')
        self.loop_trans = map.get('LoopTrans')
        self.sp_cross = map.get('SpCross')
        self.op_turn = map.get('OpTurn')
        self.op_sum = map.get('OpSum')
        self.good_rate = map.get('GoodRate')
        self.satu_rate = map.get('SatuRate')
        return self


class GetDailyReportInfoResponseDayResultRsp(TeaModel):
    def __init__(self, status=None, day_result_data=None):
        self.status = status            # type: bool
        self.day_result_data = day_result_data  # type: GetDailyReportInfoResponseDayResultRspDayResultData

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.day_result_data, 'day_result_data')
        if self.day_result_data:
            self.day_result_data.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.day_result_data is not None:
            result['DayResultData'] = self.day_result_data.to_map()
        else:
            result['DayResultData'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('DayResultData') is not None:
            temp_model = GetDailyReportInfoResponseDayResultRspDayResultData()
            self.day_result_data = temp_model.from_map(map['DayResultData'])
        else:
            self.day_result_data = None
        return self


class GetPidLoopRequest(TeaModel):
    def __init__(self, pid_loop_id=None):
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetPidLoopResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, loop_configuration=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.loop_configuration = loop_configuration  # type: GetPidLoopResponseLoopConfiguration

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.loop_configuration, 'loop_configuration')
        if self.loop_configuration:
            self.loop_configuration.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.loop_configuration is not None:
            result['LoopConfiguration'] = self.loop_configuration.to_map()
        else:
            result['LoopConfiguration'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('LoopConfiguration') is not None:
            temp_model = GetPidLoopResponseLoopConfiguration()
            self.loop_configuration = temp_model.from_map(map['LoopConfiguration'])
        else:
            self.loop_configuration = None
        return self


class GetPidLoopResponseLoopConfigurationBaseParamPvRange(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamSpOperate(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOpParamOpScope(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOpParamRange(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOpParamOperate(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOpParamIncrement(TeaModel):
    def __init__(self, max=None):
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOpParam(TeaModel):
    def __init__(self, trend=None, op_scope=None, range=None, operate=None, increment=None):
        self.trend = trend              # type: int
        self.op_scope = op_scope        # type: GetPidLoopResponseLoopConfigurationBaseParamOpParamOpScope
        self.range = range              # type: GetPidLoopResponseLoopConfigurationBaseParamOpParamRange
        self.operate = operate          # type: GetPidLoopResponseLoopConfigurationBaseParamOpParamOperate
        self.increment = increment      # type: GetPidLoopResponseLoopConfigurationBaseParamOpParamIncrement

    def validate(self):
        self.validate_required(self.trend, 'trend')
        self.validate_required(self.op_scope, 'op_scope')
        if self.op_scope:
            self.op_scope.validate()
        self.validate_required(self.range, 'range')
        if self.range:
            self.range.validate()
        self.validate_required(self.operate, 'operate')
        if self.operate:
            self.operate.validate()
        self.validate_required(self.increment, 'increment')
        if self.increment:
            self.increment.validate()

    def to_map(self):
        result = {}
        result['Trend'] = self.trend
        if self.op_scope is not None:
            result['OpScope'] = self.op_scope.to_map()
        else:
            result['OpScope'] = None
        if self.range is not None:
            result['Range'] = self.range.to_map()
        else:
            result['Range'] = None
        if self.operate is not None:
            result['Operate'] = self.operate.to_map()
        else:
            result['Operate'] = None
        if self.increment is not None:
            result['Increment'] = self.increment.to_map()
        else:
            result['Increment'] = None
        return result

    def from_map(self, map={}):
        self.trend = map.get('Trend')
        if map.get('OpScope') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOpParamOpScope()
            self.op_scope = temp_model.from_map(map['OpScope'])
        else:
            self.op_scope = None
        if map.get('Range') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOpParamRange()
            self.range = temp_model.from_map(map['Range'])
        else:
            self.range = None
        if map.get('Operate') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOpParamOperate()
            self.operate = temp_model.from_map(map['Operate'])
        else:
            self.operate = None
        if map.get('Increment') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOpParamIncrement()
            self.increment = temp_model.from_map(map['Increment'])
        else:
            self.increment = None
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp1ParamOpScope(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp1ParamRange(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp1ParamOperate(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp1ParamIncrement(TeaModel):
    def __init__(self, max=None):
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp1Param(TeaModel):
    def __init__(self, trend=None, op_scope=None, range=None, operate=None, increment=None):
        self.trend = trend              # type: int
        self.op_scope = op_scope        # type: GetPidLoopResponseLoopConfigurationBaseParamOp1ParamOpScope
        self.range = range              # type: GetPidLoopResponseLoopConfigurationBaseParamOp1ParamRange
        self.operate = operate          # type: GetPidLoopResponseLoopConfigurationBaseParamOp1ParamOperate
        self.increment = increment      # type: GetPidLoopResponseLoopConfigurationBaseParamOp1ParamIncrement

    def validate(self):
        self.validate_required(self.trend, 'trend')
        self.validate_required(self.op_scope, 'op_scope')
        if self.op_scope:
            self.op_scope.validate()
        self.validate_required(self.range, 'range')
        if self.range:
            self.range.validate()
        self.validate_required(self.operate, 'operate')
        if self.operate:
            self.operate.validate()
        self.validate_required(self.increment, 'increment')
        if self.increment:
            self.increment.validate()

    def to_map(self):
        result = {}
        result['Trend'] = self.trend
        if self.op_scope is not None:
            result['OpScope'] = self.op_scope.to_map()
        else:
            result['OpScope'] = None
        if self.range is not None:
            result['Range'] = self.range.to_map()
        else:
            result['Range'] = None
        if self.operate is not None:
            result['Operate'] = self.operate.to_map()
        else:
            result['Operate'] = None
        if self.increment is not None:
            result['Increment'] = self.increment.to_map()
        else:
            result['Increment'] = None
        return result

    def from_map(self, map={}):
        self.trend = map.get('Trend')
        if map.get('OpScope') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp1ParamOpScope()
            self.op_scope = temp_model.from_map(map['OpScope'])
        else:
            self.op_scope = None
        if map.get('Range') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp1ParamRange()
            self.range = temp_model.from_map(map['Range'])
        else:
            self.range = None
        if map.get('Operate') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp1ParamOperate()
            self.operate = temp_model.from_map(map['Operate'])
        else:
            self.operate = None
        if map.get('Increment') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp1ParamIncrement()
            self.increment = temp_model.from_map(map['Increment'])
        else:
            self.increment = None
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp2ParamOpScope(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp2ParamRange(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp2ParamOperate(TeaModel):
    def __init__(self, min=None, max=None):
        self.min = min                  # type: float
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.min, 'min')
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Min'] = self.min
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.min = map.get('Min')
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp2ParamIncrement(TeaModel):
    def __init__(self, max=None):
        self.max = max                  # type: float

    def validate(self):
        self.validate_required(self.max, 'max')

    def to_map(self):
        result = {}
        result['Max'] = self.max
        return result

    def from_map(self, map={}):
        self.max = map.get('Max')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamOp2Param(TeaModel):
    def __init__(self, trend=None, op_scope=None, range=None, operate=None, increment=None):
        self.trend = trend              # type: int
        self.op_scope = op_scope        # type: GetPidLoopResponseLoopConfigurationBaseParamOp2ParamOpScope
        self.range = range              # type: GetPidLoopResponseLoopConfigurationBaseParamOp2ParamRange
        self.operate = operate          # type: GetPidLoopResponseLoopConfigurationBaseParamOp2ParamOperate
        self.increment = increment      # type: GetPidLoopResponseLoopConfigurationBaseParamOp2ParamIncrement

    def validate(self):
        self.validate_required(self.trend, 'trend')
        self.validate_required(self.op_scope, 'op_scope')
        if self.op_scope:
            self.op_scope.validate()
        self.validate_required(self.range, 'range')
        if self.range:
            self.range.validate()
        self.validate_required(self.operate, 'operate')
        if self.operate:
            self.operate.validate()
        self.validate_required(self.increment, 'increment')
        if self.increment:
            self.increment.validate()

    def to_map(self):
        result = {}
        result['Trend'] = self.trend
        if self.op_scope is not None:
            result['OpScope'] = self.op_scope.to_map()
        else:
            result['OpScope'] = None
        if self.range is not None:
            result['Range'] = self.range.to_map()
        else:
            result['Range'] = None
        if self.operate is not None:
            result['Operate'] = self.operate.to_map()
        else:
            result['Operate'] = None
        if self.increment is not None:
            result['Increment'] = self.increment.to_map()
        else:
            result['Increment'] = None
        return result

    def from_map(self, map={}):
        self.trend = map.get('Trend')
        if map.get('OpScope') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp2ParamOpScope()
            self.op_scope = temp_model.from_map(map['OpScope'])
        else:
            self.op_scope = None
        if map.get('Range') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp2ParamRange()
            self.range = temp_model.from_map(map['Range'])
        else:
            self.range = None
        if map.get('Operate') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp2ParamOperate()
            self.operate = temp_model.from_map(map['Operate'])
        else:
            self.operate = None
        if map.get('Increment') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp2ParamIncrement()
            self.increment = temp_model.from_map(map['Increment'])
        else:
            self.increment = None
        return self


class GetPidLoopResponseLoopConfigurationBaseParamKp(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamTd(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamTi(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        return self


class GetPidLoopResponseLoopConfigurationBaseParamKd(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key          # type: str
        self.tag_value = tag_value      # type: str

    def validate(self):
        self.validate_required(self.tag_key, 'tag_key')
        self.validate_required(self.tag_value, 'tag_value')

    def to_map(self):
        result = {}
        result['TagKey'] = self.tag_key
        result['TagValue'] = self.tag_value
        return result

    def from_map(self, map={}):
        self.tag_key = map.get('TagKey')
        self.tag_value = map.get('TagValue')
        return self


class GetPidLoopResponseLoopConfigurationBaseParam(TeaModel):
    def __init__(self, open_loop_time=None, sample_time=None, suit_ctrl_time=None, pv=None, sp=None,
                 split_range_control=None, op=None, op_1=None, op_2=None, control_switch=None, mv=None, forward_controller=None,
                 forward_variable=None, integral=None, pv_range=None, sp_operate=None, op_param=None, op_1param=None, op_2param=None,
                 kp=None, td=None, ti=None, kd=None):
        self.open_loop_time = open_loop_time  # type: int
        self.sample_time = sample_time  # type: int
        self.suit_ctrl_time = suit_ctrl_time  # type: int
        self.pv = pv                    # type: str
        self.sp = sp                    # type: str
        self.split_range_control = split_range_control  # type: bool
        self.op = op                    # type: str
        self.op_1 = op_1                # type: str
        self.op_2 = op_2                # type: str
        self.control_switch = control_switch  # type: str
        self.mv = mv                    # type: str
        self.forward_controller = forward_controller  # type: bool
        self.forward_variable = forward_variable  # type: str
        self.integral = integral        # type: bool
        self.pv_range = pv_range        # type: GetPidLoopResponseLoopConfigurationBaseParamPvRange
        self.sp_operate = sp_operate    # type: GetPidLoopResponseLoopConfigurationBaseParamSpOperate
        self.op_param = op_param        # type: GetPidLoopResponseLoopConfigurationBaseParamOpParam
        self.op_1param = op_1param      # type: GetPidLoopResponseLoopConfigurationBaseParamOp1Param
        self.op_2param = op_2param      # type: GetPidLoopResponseLoopConfigurationBaseParamOp2Param
        self.kp = kp                    # type: GetPidLoopResponseLoopConfigurationBaseParamKp
        self.td = td                    # type: GetPidLoopResponseLoopConfigurationBaseParamTd
        self.ti = ti                    # type: GetPidLoopResponseLoopConfigurationBaseParamTi
        self.kd = kd                    # type: GetPidLoopResponseLoopConfigurationBaseParamKd

    def validate(self):
        self.validate_required(self.open_loop_time, 'open_loop_time')
        self.validate_required(self.sample_time, 'sample_time')
        self.validate_required(self.suit_ctrl_time, 'suit_ctrl_time')
        self.validate_required(self.pv, 'pv')
        self.validate_required(self.sp, 'sp')
        self.validate_required(self.split_range_control, 'split_range_control')
        self.validate_required(self.op, 'op')
        self.validate_required(self.op_1, 'op_1')
        self.validate_required(self.op_2, 'op_2')
        self.validate_required(self.control_switch, 'control_switch')
        self.validate_required(self.mv, 'mv')
        self.validate_required(self.forward_controller, 'forward_controller')
        self.validate_required(self.forward_variable, 'forward_variable')
        self.validate_required(self.integral, 'integral')
        self.validate_required(self.pv_range, 'pv_range')
        if self.pv_range:
            self.pv_range.validate()
        self.validate_required(self.sp_operate, 'sp_operate')
        if self.sp_operate:
            self.sp_operate.validate()
        self.validate_required(self.op_param, 'op_param')
        if self.op_param:
            self.op_param.validate()
        self.validate_required(self.op_1param, 'op_1param')
        if self.op_1param:
            self.op_1param.validate()
        self.validate_required(self.op_2param, 'op_2param')
        if self.op_2param:
            self.op_2param.validate()
        self.validate_required(self.kp, 'kp')
        if self.kp:
            self.kp.validate()
        self.validate_required(self.td, 'td')
        if self.td:
            self.td.validate()
        self.validate_required(self.ti, 'ti')
        if self.ti:
            self.ti.validate()
        self.validate_required(self.kd, 'kd')
        if self.kd:
            self.kd.validate()

    def to_map(self):
        result = {}
        result['OpenLoopTime'] = self.open_loop_time
        result['SampleTime'] = self.sample_time
        result['SuitCtrlTime'] = self.suit_ctrl_time
        result['Pv'] = self.pv
        result['Sp'] = self.sp
        result['SplitRangeControl'] = self.split_range_control
        result['Op'] = self.op
        result['Op1'] = self.op_1
        result['Op2'] = self.op_2
        result['ControlSwitch'] = self.control_switch
        result['Mv'] = self.mv
        result['ForwardController'] = self.forward_controller
        result['ForwardVariable'] = self.forward_variable
        result['Integral'] = self.integral
        if self.pv_range is not None:
            result['PvRange'] = self.pv_range.to_map()
        else:
            result['PvRange'] = None
        if self.sp_operate is not None:
            result['SpOperate'] = self.sp_operate.to_map()
        else:
            result['SpOperate'] = None
        if self.op_param is not None:
            result['OpParam'] = self.op_param.to_map()
        else:
            result['OpParam'] = None
        if self.op_1param is not None:
            result['Op1Param'] = self.op_1param.to_map()
        else:
            result['Op1Param'] = None
        if self.op_2param is not None:
            result['Op2Param'] = self.op_2param.to_map()
        else:
            result['Op2Param'] = None
        if self.kp is not None:
            result['Kp'] = self.kp.to_map()
        else:
            result['Kp'] = None
        if self.td is not None:
            result['Td'] = self.td.to_map()
        else:
            result['Td'] = None
        if self.ti is not None:
            result['Ti'] = self.ti.to_map()
        else:
            result['Ti'] = None
        if self.kd is not None:
            result['Kd'] = self.kd.to_map()
        else:
            result['Kd'] = None
        return result

    def from_map(self, map={}):
        self.open_loop_time = map.get('OpenLoopTime')
        self.sample_time = map.get('SampleTime')
        self.suit_ctrl_time = map.get('SuitCtrlTime')
        self.pv = map.get('Pv')
        self.sp = map.get('Sp')
        self.split_range_control = map.get('SplitRangeControl')
        self.op = map.get('Op')
        self.op_1 = map.get('Op1')
        self.op_2 = map.get('Op2')
        self.control_switch = map.get('ControlSwitch')
        self.mv = map.get('Mv')
        self.forward_controller = map.get('ForwardController')
        self.forward_variable = map.get('ForwardVariable')
        self.integral = map.get('Integral')
        if map.get('PvRange') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamPvRange()
            self.pv_range = temp_model.from_map(map['PvRange'])
        else:
            self.pv_range = None
        if map.get('SpOperate') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamSpOperate()
            self.sp_operate = temp_model.from_map(map['SpOperate'])
        else:
            self.sp_operate = None
        if map.get('OpParam') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOpParam()
            self.op_param = temp_model.from_map(map['OpParam'])
        else:
            self.op_param = None
        if map.get('Op1Param') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp1Param()
            self.op_1param = temp_model.from_map(map['Op1Param'])
        else:
            self.op_1param = None
        if map.get('Op2Param') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamOp2Param()
            self.op_2param = temp_model.from_map(map['Op2Param'])
        else:
            self.op_2param = None
        if map.get('Kp') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamKp()
            self.kp = temp_model.from_map(map['Kp'])
        else:
            self.kp = None
        if map.get('Td') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamTd()
            self.td = temp_model.from_map(map['Td'])
        else:
            self.td = None
        if map.get('Ti') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamTi()
            self.ti = temp_model.from_map(map['Ti'])
        else:
            self.ti = None
        if map.get('Kd') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParamKd()
            self.kd = temp_model.from_map(map['Kd'])
        else:
            self.kd = None
        return self


class GetPidLoopResponseLoopConfigurationIdentParam(TeaModel):
    def __init__(self, model_type=None, delay=None):
        self.model_type = model_type    # type: int
        self.delay = delay              # type: int

    def validate(self):
        self.validate_required(self.model_type, 'model_type')
        self.validate_required(self.delay, 'delay')

    def to_map(self):
        result = {}
        result['ModelType'] = self.model_type
        result['Delay'] = self.delay
        return result

    def from_map(self, map={}):
        self.model_type = map.get('ModelType')
        self.delay = map.get('Delay')
        return self


class GetPidLoopResponseLoopConfigurationResetParam(TeaModel):
    def __init__(self, ctrl_mode=None, ctrl_stuc=None):
        self.ctrl_mode = ctrl_mode      # type: int
        self.ctrl_stuc = ctrl_stuc      # type: int

    def validate(self):
        self.validate_required(self.ctrl_mode, 'ctrl_mode')
        self.validate_required(self.ctrl_stuc, 'ctrl_stuc')

    def to_map(self):
        result = {}
        result['CtrlMode'] = self.ctrl_mode
        result['CtrlStuc'] = self.ctrl_stuc
        return result

    def from_map(self, map={}):
        self.ctrl_mode = map.get('CtrlMode')
        self.ctrl_stuc = map.get('CtrlStuc')
        return self


class GetPidLoopResponseLoopConfiguration(TeaModel):
    def __init__(self, base_param=None, ident_param=None, reset_param=None):
        self.base_param = base_param    # type: GetPidLoopResponseLoopConfigurationBaseParam
        self.ident_param = ident_param  # type: GetPidLoopResponseLoopConfigurationIdentParam
        self.reset_param = reset_param  # type: GetPidLoopResponseLoopConfigurationResetParam

    def validate(self):
        self.validate_required(self.base_param, 'base_param')
        if self.base_param:
            self.base_param.validate()
        self.validate_required(self.ident_param, 'ident_param')
        if self.ident_param:
            self.ident_param.validate()
        self.validate_required(self.reset_param, 'reset_param')
        if self.reset_param:
            self.reset_param.validate()

    def to_map(self):
        result = {}
        if self.base_param is not None:
            result['BaseParam'] = self.base_param.to_map()
        else:
            result['BaseParam'] = None
        if self.ident_param is not None:
            result['IdentParam'] = self.ident_param.to_map()
        else:
            result['IdentParam'] = None
        if self.reset_param is not None:
            result['ResetParam'] = self.reset_param.to_map()
        else:
            result['ResetParam'] = None
        return result

    def from_map(self, map={}):
        if map.get('BaseParam') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationBaseParam()
            self.base_param = temp_model.from_map(map['BaseParam'])
        else:
            self.base_param = None
        if map.get('IdentParam') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationIdentParam()
            self.ident_param = temp_model.from_map(map['IdentParam'])
        else:
            self.ident_param = None
        if map.get('ResetParam') is not None:
            temp_model = GetPidLoopResponseLoopConfigurationResetParam()
            self.reset_param = temp_model.from_map(map['ResetParam'])
        else:
            self.reset_param = None
        return self


class CreatePidProjectRequest(TeaModel):
    def __init__(self, pid_project_name=None, pid_organisation_id=None, pid_project_desc=None, client_token=None):
        self.pid_project_name = pid_project_name  # type: str
        self.pid_organisation_id = pid_organisation_id  # type: str
        self.pid_project_desc = pid_project_desc  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.pid_project_name, 'pid_project_name')
        self.validate_required(self.pid_organisation_id, 'pid_organisation_id')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['PidProjectName'] = self.pid_project_name
        result['PidOrganisationId'] = self.pid_organisation_id
        result['PidProjectDesc'] = self.pid_project_desc
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.pid_project_name = map.get('PidProjectName')
        self.pid_organisation_id = map.get('PidOrganisationId')
        self.pid_project_desc = map.get('PidProjectDesc')
        self.client_token = map.get('ClientToken')
        return self


class CreatePidProjectResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_project_id=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_project_id = pid_project_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_project_id, 'pid_project_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidProjectId'] = self.pid_project_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_project_id = map.get('PidProjectId')
        return self


class ListIdentModelsRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class ListIdentModelsResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_ident_model_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_ident_model_list = pid_ident_model_list  # type: List[ListIdentModelsResponsePidIdentModelList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_ident_model_list, 'pid_ident_model_list')
        if self.pid_ident_model_list:
            for k in self.pid_ident_model_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidIdentModelList'] = []
        if self.pid_ident_model_list is not None:
            for k in self.pid_ident_model_list:
                result['PidIdentModelList'].append(k.to_map() if k else None)
        else:
            result['PidIdentModelList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_ident_model_list = []
        if map.get('PidIdentModelList') is not None:
            for k in map.get('PidIdentModelList'):
                temp_model = ListIdentModelsResponsePidIdentModelList()
                self.pid_ident_model_list.append(temp_model.from_map(k))
        else:
            self.pid_ident_model_list = None
        return self


class ListIdentModelsResponsePidIdentModelListModel(TeaModel):
    def __init__(self, k=None, tau=None, t_1=None, t_2=None):
        self.k = k                      # type: float
        self.tau = tau                  # type: float
        self.t_1 = t_1                  # type: float
        self.t_2 = t_2                  # type: float

    def validate(self):
        self.validate_required(self.k, 'k')
        self.validate_required(self.tau, 'tau')
        self.validate_required(self.t_1, 't_1')
        self.validate_required(self.t_2, 't_2')

    def to_map(self):
        result = {}
        result['K'] = self.k
        result['Tau'] = self.tau
        result['T1'] = self.t_1
        result['T2'] = self.t_2
        return result

    def from_map(self, map={}):
        self.k = map.get('K')
        self.tau = map.get('Tau')
        self.t_1 = map.get('T1')
        self.t_2 = map.get('T2')
        return self


class ListIdentModelsResponsePidIdentModelList(TeaModel):
    def __init__(self, model_id=None, desc=None, model=None):
        self.model_id = model_id        # type: int
        self.desc = desc                # type: str
        self.model = model              # type: ListIdentModelsResponsePidIdentModelListModel

    def validate(self):
        self.validate_required(self.model_id, 'model_id')
        self.validate_required(self.desc, 'desc')
        self.validate_required(self.model, 'model')
        if self.model:
            self.model.validate()

    def to_map(self):
        result = {}
        result['ModelId'] = self.model_id
        result['Desc'] = self.desc
        if self.model is not None:
            result['Model'] = self.model.to_map()
        else:
            result['Model'] = None
        return result

    def from_map(self, map={}):
        self.model_id = map.get('ModelId')
        self.desc = map.get('Desc')
        if map.get('Model') is not None:
            temp_model = ListIdentModelsResponsePidIdentModelListModel()
            self.model = temp_model.from_map(map['Model'])
        else:
            self.model = None
        return self


class ListPidDataProcessRequest(TeaModel):
    def __init__(self, pid_loop_id=None, only_complete_status=None, pid_data_process_type=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.only_complete_status = only_complete_status  # type: bool
        self.pid_data_process_type = pid_data_process_type  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.only_complete_status, 'only_complete_status')
        self.validate_required(self.pid_data_process_type, 'pid_data_process_type')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['OnlyCompleteStatus'] = self.only_complete_status
        result['PidDataProcessType'] = self.pid_data_process_type
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.only_complete_status = map.get('OnlyCompleteStatus')
        self.pid_data_process_type = map.get('PidDataProcessType')
        return self


class ListPidDataProcessResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_data_process_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_data_process_list = pid_data_process_list  # type: List[ListPidDataProcessResponsePidDataProcessList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_data_process_list, 'pid_data_process_list')
        if self.pid_data_process_list:
            for k in self.pid_data_process_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidDataProcessList'] = []
        if self.pid_data_process_list is not None:
            for k in self.pid_data_process_list:
                result['PidDataProcessList'].append(k.to_map() if k else None)
        else:
            result['PidDataProcessList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_data_process_list = []
        if map.get('PidDataProcessList') is not None:
            for k in map.get('PidDataProcessList'):
                temp_model = ListPidDataProcessResponsePidDataProcessList()
                self.pid_data_process_list.append(temp_model.from_map(k))
        else:
            self.pid_data_process_list = None
        return self


class ListPidDataProcessResponsePidDataProcessList(TeaModel):
    def __init__(self, pid_data_process_id=None, start_time=None, end_time=None, pid_data_process_status=None,
                 pid_data_process_progress=None):
        self.pid_data_process_id = pid_data_process_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.pid_data_process_status = pid_data_process_status  # type: str
        self.pid_data_process_progress = pid_data_process_progress  # type: str

    def validate(self):
        self.validate_required(self.pid_data_process_id, 'pid_data_process_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.pid_data_process_status, 'pid_data_process_status')
        self.validate_required(self.pid_data_process_progress, 'pid_data_process_progress')

    def to_map(self):
        result = {}
        result['PidDataProcessId'] = self.pid_data_process_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PidDataProcessStatus'] = self.pid_data_process_status
        result['PidDataProcessProgress'] = self.pid_data_process_progress
        return result

    def from_map(self, map={}):
        self.pid_data_process_id = map.get('PidDataProcessId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.pid_data_process_status = map.get('PidDataProcessStatus')
        self.pid_data_process_progress = map.get('PidDataProcessProgress')
        return self


class AddCustomIdentModelRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, key=None, value=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.key = key                  # type: str
        self.value = value              # type: float
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['Key'] = self.key
        result['Value'] = self.value
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.key = map.get('Key')
        self.value = map.get('Value')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class AddCustomIdentModelResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class GetLoopParameterStepRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetLoopParameterStepResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_loop_param_turning_step=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_loop_param_turning_step = pid_loop_param_turning_step  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_loop_param_turning_step, 'pid_loop_param_turning_step')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidLoopParamTurningStep'] = self.pid_loop_param_turning_step
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_loop_param_turning_step = map.get('PidLoopParamTurningStep')
        return self


class ListPidLoopsRequest(TeaModel):
    def __init__(self, pid_project_id=None, pid_loop_name=None, current_page=None, page_size=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_loop_name = pid_loop_name  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidLoopName'] = self.pid_loop_name
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_loop_name = map.get('PidLoopName')
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        return self


class ListPidLoopsResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, current_page=None, page_size=None,
                 total_count=None, pid_loop_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.pid_loop_list = pid_loop_list  # type: List[ListPidLoopsResponsePidLoopList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.pid_loop_list, 'pid_loop_list')
        if self.pid_loop_list:
            for k in self.pid_loop_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['PidLoopList'] = []
        if self.pid_loop_list is not None:
            for k in self.pid_loop_list:
                result['PidLoopList'].append(k.to_map() if k else None)
        else:
            result['PidLoopList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.pid_loop_list = []
        if map.get('PidLoopList') is not None:
            for k in map.get('PidLoopList'):
                temp_model = ListPidLoopsResponsePidLoopList()
                self.pid_loop_list.append(temp_model.from_map(k))
        else:
            self.pid_loop_list = None
        return self


class ListPidLoopsResponsePidLoopList(TeaModel):
    def __init__(self, pid_loop_id=None, pid_loop_name=None, crucial=None, pid_publish_status=None,
                 parameter_tunning_id=None, pid_loop_dcs_type=None, pid_loop_type=None, pid_loop_progress=None,
                 pid_loop_report_progress=None, pid_loop_data_progress=None, parameter_tunning_id_list=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_loop_name = pid_loop_name  # type: str
        self.crucial = crucial          # type: bool
        self.pid_publish_status = pid_publish_status  # type: str
        self.parameter_tunning_id = parameter_tunning_id  # type: str
        self.pid_loop_dcs_type = pid_loop_dcs_type  # type: str
        self.pid_loop_type = pid_loop_type  # type: str
        self.pid_loop_progress = pid_loop_progress  # type: str
        self.pid_loop_report_progress = pid_loop_report_progress  # type: str
        self.pid_loop_data_progress = pid_loop_data_progress  # type: str
        self.parameter_tunning_id_list = parameter_tunning_id_list  # type: List[str]

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.pid_loop_name, 'pid_loop_name')
        self.validate_required(self.crucial, 'crucial')
        self.validate_required(self.pid_publish_status, 'pid_publish_status')
        self.validate_required(self.parameter_tunning_id, 'parameter_tunning_id')
        self.validate_required(self.pid_loop_dcs_type, 'pid_loop_dcs_type')
        self.validate_required(self.pid_loop_type, 'pid_loop_type')
        self.validate_required(self.pid_loop_progress, 'pid_loop_progress')
        self.validate_required(self.pid_loop_report_progress, 'pid_loop_report_progress')
        self.validate_required(self.pid_loop_data_progress, 'pid_loop_data_progress')
        self.validate_required(self.parameter_tunning_id_list, 'parameter_tunning_id_list')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['PidLoopName'] = self.pid_loop_name
        result['Crucial'] = self.crucial
        result['PidPublishStatus'] = self.pid_publish_status
        result['ParameterTunningId'] = self.parameter_tunning_id
        result['PidLoopDcsType'] = self.pid_loop_dcs_type
        result['PidLoopType'] = self.pid_loop_type
        result['PidLoopProgress'] = self.pid_loop_progress
        result['PidLoopReportProgress'] = self.pid_loop_report_progress
        result['PidLoopDataProgress'] = self.pid_loop_data_progress
        result['ParameterTunningIdList'] = self.parameter_tunning_id_list
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_loop_name = map.get('PidLoopName')
        self.crucial = map.get('Crucial')
        self.pid_publish_status = map.get('PidPublishStatus')
        self.parameter_tunning_id = map.get('ParameterTunningId')
        self.pid_loop_dcs_type = map.get('PidLoopDcsType')
        self.pid_loop_type = map.get('PidLoopType')
        self.pid_loop_progress = map.get('PidLoopProgress')
        self.pid_loop_report_progress = map.get('PidLoopReportProgress')
        self.pid_loop_data_progress = map.get('PidLoopDataProgress')
        self.parameter_tunning_id_list = map.get('ParameterTunningIdList')
        return self


class MovePidOrganizationRequest(TeaModel):
    def __init__(self, organization_id=None, move_type=None):
        self.organization_id = organization_id  # type: str
        self.move_type = move_type      # type: str

    def validate(self):
        self.validate_required(self.organization_id, 'organization_id')
        self.validate_required(self.move_type, 'move_type')

    def to_map(self):
        result = {}
        result['OrganizationId'] = self.organization_id
        result['MoveType'] = self.move_type
        return result

    def from_map(self, map={}):
        self.organization_id = map.get('OrganizationId')
        self.move_type = map.get('MoveType')
        return self


class MovePidOrganizationResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class UpdatePidLoopRequest(TeaModel):
    def __init__(self, pid_loop_id=None, pid_loop_name=None, crucial=None, pid_loop_desc=None, pid_project_id=None,
                 pid_loop_dcs_type=None, pid_loop_type=None, pid_loop_configuration=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_loop_name = pid_loop_name  # type: str
        self.crucial = crucial          # type: bool
        self.pid_loop_desc = pid_loop_desc  # type: str
        self.pid_project_id = pid_project_id  # type: str
        self.pid_loop_dcs_type = pid_loop_dcs_type  # type: str
        self.pid_loop_type = pid_loop_type  # type: str
        self.pid_loop_configuration = pid_loop_configuration  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.pid_loop_name, 'pid_loop_name')
        self.validate_required(self.crucial, 'crucial')
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_loop_dcs_type, 'pid_loop_dcs_type')
        self.validate_required(self.pid_loop_type, 'pid_loop_type')
        self.validate_required(self.pid_loop_configuration, 'pid_loop_configuration')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['PidLoopName'] = self.pid_loop_name
        result['Crucial'] = self.crucial
        result['PidLoopDesc'] = self.pid_loop_desc
        result['PidProjectId'] = self.pid_project_id
        result['PidLoopDcsType'] = self.pid_loop_dcs_type
        result['PidLoopType'] = self.pid_loop_type
        result['PidLoopConfiguration'] = self.pid_loop_configuration
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_loop_name = map.get('PidLoopName')
        self.crucial = map.get('Crucial')
        self.pid_loop_desc = map.get('PidLoopDesc')
        self.pid_project_id = map.get('PidProjectId')
        self.pid_loop_dcs_type = map.get('PidLoopDcsType')
        self.pid_loop_type = map.get('PidLoopType')
        self.pid_loop_configuration = map.get('PidLoopConfiguration')
        return self


class UpdatePidLoopResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class AddPidLoopToScheduleRequest(TeaModel):
    def __init__(self, pid_loop_id_list=None):
        self.pid_loop_id_list = pid_loop_id_list  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.pid_loop_id_list, 'pid_loop_id_list')

    def to_map(self):
        result = {}
        result['PidLoopIdList'] = self.pid_loop_id_list
        return result

    def from_map(self, map={}):
        self.pid_loop_id_list = map.get('PidLoopIdList')
        return self


class AddPidLoopToScheduleResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class GetParsingTagTaskRequest(TeaModel):
    def __init__(self, pid_project_id=None):
        self.pid_project_id = pid_project_id  # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        return self


class GetParsingTagTaskResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_tag_task_status=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_tag_task_status = pid_tag_task_status  # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_tag_task_status, 'pid_tag_task_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidTagTaskStatus'] = self.pid_tag_task_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_tag_task_status = map.get('PidTagTaskStatus')
        return self


class GetPidLoopLatestTaskStatusRequest(TeaModel):
    def __init__(self, pid_loop_parameter_id=None, type=None, pid_loop_id=None):
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.type = type                # type: str
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['Type'] = self.type
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.type = map.get('Type')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class GetPidLoopLatestTaskStatusResponse(TeaModel):
    def __init__(self, request_id=None, code=None, success=None, message=None, status=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.message = message          # type: str
        self.status = status            # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['Success'] = self.success
        result['Message'] = self.message
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.message = map.get('Message')
        self.status = map.get('Status')
        return self


class DeletePidLoopRequest(TeaModel):
    def __init__(self, pid_loop_id=None):
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        return self


class DeletePidLoopResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class GetSummaryReportInfoRequest(TeaModel):
    def __init__(self, pid_loop_id=None, start_time=None, end_time=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class GetSummaryReportInfoResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, summary_result_rsp=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.summary_result_rsp = summary_result_rsp  # type: GetSummaryReportInfoResponseSummaryResultRsp

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.summary_result_rsp, 'summary_result_rsp')
        if self.summary_result_rsp:
            self.summary_result_rsp.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.summary_result_rsp is not None:
            result['SummaryResultRsp'] = self.summary_result_rsp.to_map()
        else:
            result['SummaryResultRsp'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('SummaryResultRsp') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRsp()
            self.summary_result_rsp = temp_model.from_map(map['SummaryResultRsp'])
        else:
            self.summary_result_rsp = None
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataMultipleScoreIndexRsp(TeaModel):
    def __init__(self, average=None, best=None, worst=None):
        self.average = average          # type: str
        self.best = best                # type: str
        self.worst = worst              # type: str

    def validate(self):
        self.validate_required(self.average, 'average')
        self.validate_required(self.best, 'best')
        self.validate_required(self.worst, 'worst')

    def to_map(self):
        result = {}
        result['Average'] = self.average
        result['Best'] = self.best
        result['Worst'] = self.worst
        return result

    def from_map(self, map={}):
        self.average = map.get('Average')
        self.best = map.get('Best')
        self.worst = map.get('Worst')
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataMultipleScoreRsp(TeaModel):
    def __init__(self, average=None, best=None, worst=None):
        self.average = average          # type: str
        self.best = best                # type: str
        self.worst = worst              # type: str

    def validate(self):
        self.validate_required(self.average, 'average')
        self.validate_required(self.best, 'best')
        self.validate_required(self.worst, 'worst')

    def to_map(self):
        result = {}
        result['Average'] = self.average
        result['Best'] = self.best
        result['Worst'] = self.worst
        return result

    def from_map(self, map={}):
        self.average = map.get('Average')
        self.best = map.get('Best')
        self.worst = map.get('Worst')
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataOperationRate(TeaModel):
    def __init__(self, average=None, best=None, worst=None):
        self.average = average          # type: str
        self.best = best                # type: str
        self.worst = worst              # type: str

    def validate(self):
        self.validate_required(self.average, 'average')
        self.validate_required(self.best, 'best')
        self.validate_required(self.worst, 'worst')

    def to_map(self):
        result = {}
        result['Average'] = self.average
        result['Best'] = self.best
        result['Worst'] = self.worst
        return result

    def from_map(self, map={}):
        self.average = map.get('Average')
        self.best = map.get('Best')
        self.worst = map.get('Worst')
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataOscillationIndex(TeaModel):
    def __init__(self, average=None, best=None, worst=None):
        self.average = average          # type: str
        self.best = best                # type: str
        self.worst = worst              # type: str

    def validate(self):
        self.validate_required(self.average, 'average')
        self.validate_required(self.best, 'best')
        self.validate_required(self.worst, 'worst')

    def to_map(self):
        result = {}
        result['Average'] = self.average
        result['Best'] = self.best
        result['Worst'] = self.worst
        return result

    def from_map(self, map={}):
        self.average = map.get('Average')
        self.best = map.get('Best')
        self.worst = map.get('Worst')
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataPerformMetrics(TeaModel):
    def __init__(self, average=None, best=None, worst=None):
        self.average = average          # type: str
        self.best = best                # type: str
        self.worst = worst              # type: str

    def validate(self):
        self.validate_required(self.average, 'average')
        self.validate_required(self.best, 'best')
        self.validate_required(self.worst, 'worst')

    def to_map(self):
        result = {}
        result['Average'] = self.average
        result['Best'] = self.best
        result['Worst'] = self.worst
        return result

    def from_map(self, map={}):
        self.average = map.get('Average')
        self.best = map.get('Best')
        self.worst = map.get('Worst')
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataValidOperationRate(TeaModel):
    def __init__(self, average=None, best=None, worst=None):
        self.average = average          # type: str
        self.best = best                # type: str
        self.worst = worst              # type: str

    def validate(self):
        self.validate_required(self.average, 'average')
        self.validate_required(self.best, 'best')
        self.validate_required(self.worst, 'worst')

    def to_map(self):
        result = {}
        result['Average'] = self.average
        result['Best'] = self.best
        result['Worst'] = self.worst
        return result

    def from_map(self, map={}):
        self.average = map.get('Average')
        self.best = map.get('Best')
        self.worst = map.get('Worst')
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataValveStickIndex(TeaModel):
    def __init__(self, average=None, best=None, worst=None):
        self.average = average          # type: str
        self.best = best                # type: str
        self.worst = worst              # type: str

    def validate(self):
        self.validate_required(self.average, 'average')
        self.validate_required(self.best, 'best')
        self.validate_required(self.worst, 'worst')

    def to_map(self):
        result = {}
        result['Average'] = self.average
        result['Best'] = self.best
        result['Worst'] = self.worst
        return result

    def from_map(self, map={}):
        self.average = map.get('Average')
        self.best = map.get('Best')
        self.worst = map.get('Worst')
        return self


class GetSummaryReportInfoResponseSummaryResultRspSummaryResultData(TeaModel):
    def __init__(self, loop_name=None, multiple_score_index_rsp=None, multiple_score_rsp=None, operation_rate=None,
                 oscillation_index=None, perform_metrics=None, valid_operation_rate=None, valve_stick_index=None):
        self.loop_name = loop_name      # type: str
        self.multiple_score_index_rsp = multiple_score_index_rsp  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataMultipleScoreIndexRsp
        self.multiple_score_rsp = multiple_score_rsp  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataMultipleScoreRsp
        self.operation_rate = operation_rate  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataOperationRate
        self.oscillation_index = oscillation_index  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataOscillationIndex
        self.perform_metrics = perform_metrics  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataPerformMetrics
        self.valid_operation_rate = valid_operation_rate  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataValidOperationRate
        self.valve_stick_index = valve_stick_index  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataValveStickIndex

    def validate(self):
        self.validate_required(self.loop_name, 'loop_name')
        self.validate_required(self.multiple_score_index_rsp, 'multiple_score_index_rsp')
        if self.multiple_score_index_rsp:
            self.multiple_score_index_rsp.validate()
        self.validate_required(self.multiple_score_rsp, 'multiple_score_rsp')
        if self.multiple_score_rsp:
            self.multiple_score_rsp.validate()
        self.validate_required(self.operation_rate, 'operation_rate')
        if self.operation_rate:
            self.operation_rate.validate()
        self.validate_required(self.oscillation_index, 'oscillation_index')
        if self.oscillation_index:
            self.oscillation_index.validate()
        self.validate_required(self.perform_metrics, 'perform_metrics')
        if self.perform_metrics:
            self.perform_metrics.validate()
        self.validate_required(self.valid_operation_rate, 'valid_operation_rate')
        if self.valid_operation_rate:
            self.valid_operation_rate.validate()
        self.validate_required(self.valve_stick_index, 'valve_stick_index')
        if self.valve_stick_index:
            self.valve_stick_index.validate()

    def to_map(self):
        result = {}
        result['LoopName'] = self.loop_name
        if self.multiple_score_index_rsp is not None:
            result['MultipleScoreIndexRsp'] = self.multiple_score_index_rsp.to_map()
        else:
            result['MultipleScoreIndexRsp'] = None
        if self.multiple_score_rsp is not None:
            result['MultipleScoreRsp'] = self.multiple_score_rsp.to_map()
        else:
            result['MultipleScoreRsp'] = None
        if self.operation_rate is not None:
            result['OperationRate'] = self.operation_rate.to_map()
        else:
            result['OperationRate'] = None
        if self.oscillation_index is not None:
            result['OscillationIndex'] = self.oscillation_index.to_map()
        else:
            result['OscillationIndex'] = None
        if self.perform_metrics is not None:
            result['PerformMetrics'] = self.perform_metrics.to_map()
        else:
            result['PerformMetrics'] = None
        if self.valid_operation_rate is not None:
            result['ValidOperationRate'] = self.valid_operation_rate.to_map()
        else:
            result['ValidOperationRate'] = None
        if self.valve_stick_index is not None:
            result['ValveStickIndex'] = self.valve_stick_index.to_map()
        else:
            result['ValveStickIndex'] = None
        return result

    def from_map(self, map={}):
        self.loop_name = map.get('LoopName')
        if map.get('MultipleScoreIndexRsp') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataMultipleScoreIndexRsp()
            self.multiple_score_index_rsp = temp_model.from_map(map['MultipleScoreIndexRsp'])
        else:
            self.multiple_score_index_rsp = None
        if map.get('MultipleScoreRsp') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataMultipleScoreRsp()
            self.multiple_score_rsp = temp_model.from_map(map['MultipleScoreRsp'])
        else:
            self.multiple_score_rsp = None
        if map.get('OperationRate') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataOperationRate()
            self.operation_rate = temp_model.from_map(map['OperationRate'])
        else:
            self.operation_rate = None
        if map.get('OscillationIndex') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataOscillationIndex()
            self.oscillation_index = temp_model.from_map(map['OscillationIndex'])
        else:
            self.oscillation_index = None
        if map.get('PerformMetrics') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataPerformMetrics()
            self.perform_metrics = temp_model.from_map(map['PerformMetrics'])
        else:
            self.perform_metrics = None
        if map.get('ValidOperationRate') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataValidOperationRate()
            self.valid_operation_rate = temp_model.from_map(map['ValidOperationRate'])
        else:
            self.valid_operation_rate = None
        if map.get('ValveStickIndex') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultDataValveStickIndex()
            self.valve_stick_index = temp_model.from_map(map['ValveStickIndex'])
        else:
            self.valve_stick_index = None
        return self


class GetSummaryReportInfoResponseSummaryResultRsp(TeaModel):
    def __init__(self, status=None, summary_result_data=None):
        self.status = status            # type: bool
        self.summary_result_data = summary_result_data  # type: GetSummaryReportInfoResponseSummaryResultRspSummaryResultData

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.summary_result_data, 'summary_result_data')
        if self.summary_result_data:
            self.summary_result_data.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.summary_result_data is not None:
            result['SummaryResultData'] = self.summary_result_data.to_map()
        else:
            result['SummaryResultData'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('SummaryResultData') is not None:
            temp_model = GetSummaryReportInfoResponseSummaryResultRspSummaryResultData()
            self.summary_result_data = temp_model.from_map(map['SummaryResultData'])
        else:
            self.summary_result_data = None
        return self


class GetSummaryReportDataTrendRequest(TeaModel):
    def __init__(self, pid_loop_id=None, start_time=None, end_time=None, trend_type=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.trend_type = trend_type    # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.trend_type, 'trend_type')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['TrendType'] = self.trend_type
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.trend_type = map.get('TrendType')
        return self


class GetSummaryReportDataTrendResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, summary_trend_data=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.summary_trend_data = summary_trend_data  # type: GetSummaryReportDataTrendResponseSummaryTrendData

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.summary_trend_data, 'summary_trend_data')
        if self.summary_trend_data:
            self.summary_trend_data.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.summary_trend_data is not None:
            result['SummaryTrendData'] = self.summary_trend_data.to_map()
        else:
            result['SummaryTrendData'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('SummaryTrendData') is not None:
            temp_model = GetSummaryReportDataTrendResponseSummaryTrendData()
            self.summary_trend_data = temp_model.from_map(map['SummaryTrendData'])
        else:
            self.summary_trend_data = None
        return self


class GetSummaryReportDataTrendResponseSummaryTrendDataDataOp2(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportDataTrendResponseSummaryTrendDataDataOp(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportDataTrendResponseSummaryTrendDataDataOp1(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportDataTrendResponseSummaryTrendDataDataPv(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportDataTrendResponseSummaryTrendDataDataSp(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportDataTrendResponseSummaryTrendDataData(TeaModel):
    def __init__(self, op_2=None, op=None, op_1=None, pv=None, sp=None):
        self.op_2 = op_2                # type: List[GetSummaryReportDataTrendResponseSummaryTrendDataDataOp2]
        self.op = op                    # type: List[GetSummaryReportDataTrendResponseSummaryTrendDataDataOp]
        self.op_1 = op_1                # type: List[GetSummaryReportDataTrendResponseSummaryTrendDataDataOp1]
        self.pv = pv                    # type: List[GetSummaryReportDataTrendResponseSummaryTrendDataDataPv]
        self.sp = sp                    # type: List[GetSummaryReportDataTrendResponseSummaryTrendDataDataSp]

    def validate(self):
        self.validate_required(self.op_2, 'op_2')
        if self.op_2:
            for k in self.op_2:
                if k:
                    k.validate()
        self.validate_required(self.op, 'op')
        if self.op:
            for k in self.op:
                if k:
                    k.validate()
        self.validate_required(self.op_1, 'op_1')
        if self.op_1:
            for k in self.op_1:
                if k:
                    k.validate()
        self.validate_required(self.pv, 'pv')
        if self.pv:
            for k in self.pv:
                if k:
                    k.validate()
        self.validate_required(self.sp, 'sp')
        if self.sp:
            for k in self.sp:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Op2'] = []
        if self.op_2 is not None:
            for k in self.op_2:
                result['Op2'].append(k.to_map() if k else None)
        else:
            result['Op2'] = None
        result['Op'] = []
        if self.op is not None:
            for k in self.op:
                result['Op'].append(k.to_map() if k else None)
        else:
            result['Op'] = None
        result['Op1'] = []
        if self.op_1 is not None:
            for k in self.op_1:
                result['Op1'].append(k.to_map() if k else None)
        else:
            result['Op1'] = None
        result['Pv'] = []
        if self.pv is not None:
            for k in self.pv:
                result['Pv'].append(k.to_map() if k else None)
        else:
            result['Pv'] = None
        result['Sp'] = []
        if self.sp is not None:
            for k in self.sp:
                result['Sp'].append(k.to_map() if k else None)
        else:
            result['Sp'] = None
        return result

    def from_map(self, map={}):
        self.op_2 = []
        if map.get('Op2') is not None:
            for k in map.get('Op2'):
                temp_model = GetSummaryReportDataTrendResponseSummaryTrendDataDataOp2()
                self.op_2.append(temp_model.from_map(k))
        else:
            self.op_2 = None
        self.op = []
        if map.get('Op') is not None:
            for k in map.get('Op'):
                temp_model = GetSummaryReportDataTrendResponseSummaryTrendDataDataOp()
                self.op.append(temp_model.from_map(k))
        else:
            self.op = None
        self.op_1 = []
        if map.get('Op1') is not None:
            for k in map.get('Op1'):
                temp_model = GetSummaryReportDataTrendResponseSummaryTrendDataDataOp1()
                self.op_1.append(temp_model.from_map(k))
        else:
            self.op_1 = None
        self.pv = []
        if map.get('Pv') is not None:
            for k in map.get('Pv'):
                temp_model = GetSummaryReportDataTrendResponseSummaryTrendDataDataPv()
                self.pv.append(temp_model.from_map(k))
        else:
            self.pv = None
        self.sp = []
        if map.get('Sp') is not None:
            for k in map.get('Sp'):
                temp_model = GetSummaryReportDataTrendResponseSummaryTrendDataDataSp()
                self.sp.append(temp_model.from_map(k))
        else:
            self.sp = None
        return self


class GetSummaryReportDataTrendResponseSummaryTrendData(TeaModel):
    def __init__(self, status=None, data=None):
        self.status = status            # type: bool
        self.data = data                # type: GetSummaryReportDataTrendResponseSummaryTrendDataData

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('Data') is not None:
            temp_model = GetSummaryReportDataTrendResponseSummaryTrendDataData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class GetSummaryReportChartRequest(TeaModel):
    def __init__(self, pid_loop_id=None, start_time=None, end_time=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class GetSummaryReportChartResponse(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None, summary_line_chart_data_rsp=None):
        self.code = code                # type: str
        self.message = message          # type: str
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.summary_line_chart_data_rsp = summary_line_chart_data_rsp  # type: GetSummaryReportChartResponseSummaryLineChartDataRsp

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.summary_line_chart_data_rsp, 'summary_line_chart_data_rsp')
        if self.summary_line_chart_data_rsp:
            self.summary_line_chart_data_rsp.validate()

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Message'] = self.message
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        if self.summary_line_chart_data_rsp is not None:
            result['SummaryLineChartDataRsp'] = self.summary_line_chart_data_rsp.to_map()
        else:
            result['SummaryLineChartDataRsp'] = None
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        if map.get('SummaryLineChartDataRsp') is not None:
            temp_model = GetSummaryReportChartResponseSummaryLineChartDataRsp()
            self.summary_line_chart_data_rsp = temp_model.from_map(map['SummaryLineChartDataRsp'])
        else:
            self.summary_line_chart_data_rsp = None
        return self


class GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataMultipleScoreList(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataOperationRateList(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataPerformMetricsList(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataValidOperationRateList(TeaModel):
    def __init__(self, name=None, xlabel=None, ylabel=None):
        self.name = name                # type: str
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        return self


class GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartData(TeaModel):
    def __init__(self, multiple_score_list=None, operation_rate_list=None, perform_metrics_list=None,
                 valid_operation_rate_list=None):
        self.multiple_score_list = multiple_score_list  # type: List[GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataMultipleScoreList]
        self.operation_rate_list = operation_rate_list  # type: List[GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataOperationRateList]
        self.perform_metrics_list = perform_metrics_list  # type: List[GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataPerformMetricsList]
        self.valid_operation_rate_list = valid_operation_rate_list  # type: List[GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataValidOperationRateList]

    def validate(self):
        self.validate_required(self.multiple_score_list, 'multiple_score_list')
        if self.multiple_score_list:
            for k in self.multiple_score_list:
                if k:
                    k.validate()
        self.validate_required(self.operation_rate_list, 'operation_rate_list')
        if self.operation_rate_list:
            for k in self.operation_rate_list:
                if k:
                    k.validate()
        self.validate_required(self.perform_metrics_list, 'perform_metrics_list')
        if self.perform_metrics_list:
            for k in self.perform_metrics_list:
                if k:
                    k.validate()
        self.validate_required(self.valid_operation_rate_list, 'valid_operation_rate_list')
        if self.valid_operation_rate_list:
            for k in self.valid_operation_rate_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MultipleScoreList'] = []
        if self.multiple_score_list is not None:
            for k in self.multiple_score_list:
                result['MultipleScoreList'].append(k.to_map() if k else None)
        else:
            result['MultipleScoreList'] = None
        result['OperationRateList'] = []
        if self.operation_rate_list is not None:
            for k in self.operation_rate_list:
                result['OperationRateList'].append(k.to_map() if k else None)
        else:
            result['OperationRateList'] = None
        result['PerformMetricsList'] = []
        if self.perform_metrics_list is not None:
            for k in self.perform_metrics_list:
                result['PerformMetricsList'].append(k.to_map() if k else None)
        else:
            result['PerformMetricsList'] = None
        result['ValidOperationRateList'] = []
        if self.valid_operation_rate_list is not None:
            for k in self.valid_operation_rate_list:
                result['ValidOperationRateList'].append(k.to_map() if k else None)
        else:
            result['ValidOperationRateList'] = None
        return result

    def from_map(self, map={}):
        self.multiple_score_list = []
        if map.get('MultipleScoreList') is not None:
            for k in map.get('MultipleScoreList'):
                temp_model = GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataMultipleScoreList()
                self.multiple_score_list.append(temp_model.from_map(k))
        else:
            self.multiple_score_list = None
        self.operation_rate_list = []
        if map.get('OperationRateList') is not None:
            for k in map.get('OperationRateList'):
                temp_model = GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataOperationRateList()
                self.operation_rate_list.append(temp_model.from_map(k))
        else:
            self.operation_rate_list = None
        self.perform_metrics_list = []
        if map.get('PerformMetricsList') is not None:
            for k in map.get('PerformMetricsList'):
                temp_model = GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataPerformMetricsList()
                self.perform_metrics_list.append(temp_model.from_map(k))
        else:
            self.perform_metrics_list = None
        self.valid_operation_rate_list = []
        if map.get('ValidOperationRateList') is not None:
            for k in map.get('ValidOperationRateList'):
                temp_model = GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartDataValidOperationRateList()
                self.valid_operation_rate_list.append(temp_model.from_map(k))
        else:
            self.valid_operation_rate_list = None
        return self


class GetSummaryReportChartResponseSummaryLineChartDataRsp(TeaModel):
    def __init__(self, status=None, summary_line_chart_data=None):
        self.status = status            # type: bool
        self.summary_line_chart_data = summary_line_chart_data  # type: GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartData

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.summary_line_chart_data, 'summary_line_chart_data')
        if self.summary_line_chart_data:
            self.summary_line_chart_data.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.summary_line_chart_data is not None:
            result['SummaryLineChartData'] = self.summary_line_chart_data.to_map()
        else:
            result['SummaryLineChartData'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('SummaryLineChartData') is not None:
            temp_model = GetSummaryReportChartResponseSummaryLineChartDataRspSummaryLineChartData()
            self.summary_line_chart_data = temp_model.from_map(map['SummaryLineChartData'])
        else:
            self.summary_line_chart_data = None
        return self


class GetDailyReportDataTrendRequest(TeaModel):
    def __init__(self, pid_loop_id=None, report_date=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.report_date = report_date  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['ReportDate'] = self.report_date
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.report_date = map.get('ReportDate')
        return self


class GetDailyReportDataTrendResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, tags_values_rsp=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.tags_values_rsp = tags_values_rsp  # type: GetDailyReportDataTrendResponseTagsValuesRsp

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.tags_values_rsp, 'tags_values_rsp')
        if self.tags_values_rsp:
            self.tags_values_rsp.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.tags_values_rsp is not None:
            result['TagsValuesRsp'] = self.tags_values_rsp.to_map()
        else:
            result['TagsValuesRsp'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('TagsValuesRsp') is not None:
            temp_model = GetDailyReportDataTrendResponseTagsValuesRsp()
            self.tags_values_rsp = temp_model.from_map(map['TagsValuesRsp'])
        else:
            self.tags_values_rsp = None
        return self


class GetDailyReportDataTrendResponseTagsValuesRspDataOp(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportDataTrendResponseTagsValuesRspDataOp1(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportDataTrendResponseTagsValuesRspDataOp2(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportDataTrendResponseTagsValuesRspDataSp(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportDataTrendResponseTagsValuesRspDataPv(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportDataTrendResponseTagsValuesRspData(TeaModel):
    def __init__(self, op=None, op_1=None, op_2=None, sp=None, pv=None):
        self.op = op                    # type: List[GetDailyReportDataTrendResponseTagsValuesRspDataOp]
        self.op_1 = op_1                # type: List[GetDailyReportDataTrendResponseTagsValuesRspDataOp1]
        self.op_2 = op_2                # type: List[GetDailyReportDataTrendResponseTagsValuesRspDataOp2]
        self.sp = sp                    # type: List[GetDailyReportDataTrendResponseTagsValuesRspDataSp]
        self.pv = pv                    # type: List[GetDailyReportDataTrendResponseTagsValuesRspDataPv]

    def validate(self):
        self.validate_required(self.op, 'op')
        if self.op:
            for k in self.op:
                if k:
                    k.validate()
        self.validate_required(self.op_1, 'op_1')
        if self.op_1:
            for k in self.op_1:
                if k:
                    k.validate()
        self.validate_required(self.op_2, 'op_2')
        if self.op_2:
            for k in self.op_2:
                if k:
                    k.validate()
        self.validate_required(self.sp, 'sp')
        if self.sp:
            for k in self.sp:
                if k:
                    k.validate()
        self.validate_required(self.pv, 'pv')
        if self.pv:
            for k in self.pv:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Op'] = []
        if self.op is not None:
            for k in self.op:
                result['Op'].append(k.to_map() if k else None)
        else:
            result['Op'] = None
        result['Op1'] = []
        if self.op_1 is not None:
            for k in self.op_1:
                result['Op1'].append(k.to_map() if k else None)
        else:
            result['Op1'] = None
        result['Op2'] = []
        if self.op_2 is not None:
            for k in self.op_2:
                result['Op2'].append(k.to_map() if k else None)
        else:
            result['Op2'] = None
        result['Sp'] = []
        if self.sp is not None:
            for k in self.sp:
                result['Sp'].append(k.to_map() if k else None)
        else:
            result['Sp'] = None
        result['Pv'] = []
        if self.pv is not None:
            for k in self.pv:
                result['Pv'].append(k.to_map() if k else None)
        else:
            result['Pv'] = None
        return result

    def from_map(self, map={}):
        self.op = []
        if map.get('Op') is not None:
            for k in map.get('Op'):
                temp_model = GetDailyReportDataTrendResponseTagsValuesRspDataOp()
                self.op.append(temp_model.from_map(k))
        else:
            self.op = None
        self.op_1 = []
        if map.get('Op1') is not None:
            for k in map.get('Op1'):
                temp_model = GetDailyReportDataTrendResponseTagsValuesRspDataOp1()
                self.op_1.append(temp_model.from_map(k))
        else:
            self.op_1 = None
        self.op_2 = []
        if map.get('Op2') is not None:
            for k in map.get('Op2'):
                temp_model = GetDailyReportDataTrendResponseTagsValuesRspDataOp2()
                self.op_2.append(temp_model.from_map(k))
        else:
            self.op_2 = None
        self.sp = []
        if map.get('Sp') is not None:
            for k in map.get('Sp'):
                temp_model = GetDailyReportDataTrendResponseTagsValuesRspDataSp()
                self.sp.append(temp_model.from_map(k))
        else:
            self.sp = None
        self.pv = []
        if map.get('Pv') is not None:
            for k in map.get('Pv'):
                temp_model = GetDailyReportDataTrendResponseTagsValuesRspDataPv()
                self.pv.append(temp_model.from_map(k))
        else:
            self.pv = None
        return self


class GetDailyReportDataTrendResponseTagsValuesRsp(TeaModel):
    def __init__(self, status=None, data=None):
        self.status = status            # type: bool
        self.data = data                # type: GetDailyReportDataTrendResponseTagsValuesRspData

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.data is not None:
            result['Data'] = self.data.to_map()
        else:
            result['Data'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('Data') is not None:
            temp_model = GetDailyReportDataTrendResponseTagsValuesRspData()
            self.data = temp_model.from_map(map['Data'])
        else:
            self.data = None
        return self


class ListTagValueTrendRequest(TeaModel):
    def __init__(self, pid_project_id=None, pid_tag=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_tag = pid_tag          # type: List[ListTagValueTrendRequestPidTag]

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_tag, 'pid_tag')
        if self.pid_tag:
            for k in self.pid_tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidTag'] = []
        if self.pid_tag is not None:
            for k in self.pid_tag:
                result['PidTag'].append(k.to_map() if k else None)
        else:
            result['PidTag'] = None
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_tag = []
        if map.get('PidTag') is not None:
            for k in map.get('PidTag'):
                temp_model = ListTagValueTrendRequestPidTag()
                self.pid_tag.append(temp_model.from_map(k))
        else:
            self.pid_tag = None
        return self


class ListTagValueTrendRequestPidTag(TeaModel):
    def __init__(self, pid_tag_id=None):
        self.pid_tag_id = pid_tag_id    # type: str

    def validate(self):
        self.validate_required(self.pid_tag_id, 'pid_tag_id')

    def to_map(self):
        result = {}
        result['PidTagId'] = self.pid_tag_id
        return result

    def from_map(self, map={}):
        self.pid_tag_id = map.get('PidTagId')
        return self


class ListTagValueTrendResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_tag_trend_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_tag_trend_list = pid_tag_trend_list  # type: List[ListTagValueTrendResponsePidTagTrendList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_tag_trend_list, 'pid_tag_trend_list')
        if self.pid_tag_trend_list:
            for k in self.pid_tag_trend_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidTagTrendList'] = []
        if self.pid_tag_trend_list is not None:
            for k in self.pid_tag_trend_list:
                result['PidTagTrendList'].append(k.to_map() if k else None)
        else:
            result['PidTagTrendList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_tag_trend_list = []
        if map.get('PidTagTrendList') is not None:
            for k in map.get('PidTagTrendList'):
                temp_model = ListTagValueTrendResponsePidTagTrendList()
                self.pid_tag_trend_list.append(temp_model.from_map(k))
        else:
            self.pid_tag_trend_list = None
        return self


class ListTagValueTrendResponsePidTagTrendListPidTagValueList(TeaModel):
    def __init__(self, time=None, value=None):
        self.time = time                # type: int
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Time'] = self.time
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.time = map.get('Time')
        self.value = map.get('Value')
        return self


class ListTagValueTrendResponsePidTagTrendList(TeaModel):
    def __init__(self, pid_tag_name=None, pid_tag_value_list=None):
        self.pid_tag_name = pid_tag_name  # type: str
        self.pid_tag_value_list = pid_tag_value_list  # type: List[ListTagValueTrendResponsePidTagTrendListPidTagValueList]

    def validate(self):
        self.validate_required(self.pid_tag_name, 'pid_tag_name')
        self.validate_required(self.pid_tag_value_list, 'pid_tag_value_list')
        if self.pid_tag_value_list:
            for k in self.pid_tag_value_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PidTagName'] = self.pid_tag_name
        result['PidTagValueList'] = []
        if self.pid_tag_value_list is not None:
            for k in self.pid_tag_value_list:
                result['PidTagValueList'].append(k.to_map() if k else None)
        else:
            result['PidTagValueList'] = None
        return result

    def from_map(self, map={}):
        self.pid_tag_name = map.get('PidTagName')
        self.pid_tag_value_list = []
        if map.get('PidTagValueList') is not None:
            for k in map.get('PidTagValueList'):
                temp_model = ListTagValueTrendResponsePidTagTrendListPidTagValueList()
                self.pid_tag_value_list.append(temp_model.from_map(k))
        else:
            self.pid_tag_value_list = None
        return self


class GetDailyReportChartRequest(TeaModel):
    def __init__(self, pid_loop_id=None, report_date=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.report_date = report_date  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['ReportDate'] = self.report_date
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.report_date = map.get('ReportDate')
        return self


class GetDailyReportChartResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, day_line_chart_data_rsp=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.day_line_chart_data_rsp = day_line_chart_data_rsp  # type: GetDailyReportChartResponseDayLineChartDataRsp

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.day_line_chart_data_rsp, 'day_line_chart_data_rsp')
        if self.day_line_chart_data_rsp:
            self.day_line_chart_data_rsp.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.day_line_chart_data_rsp is not None:
            result['DayLineChartDataRsp'] = self.day_line_chart_data_rsp.to_map()
        else:
            result['DayLineChartDataRsp'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('DayLineChartDataRsp') is not None:
            temp_model = GetDailyReportChartResponseDayLineChartDataRsp()
            self.day_line_chart_data_rsp = temp_model.from_map(map['DayLineChartDataRsp'])
        else:
            self.day_line_chart_data_rsp = None
        return self


class GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataHarris(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataCloseLoop(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataBode(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataResidualStage(TeaModel):
    def __init__(self, xlabel=None, ylabel=None, name=None):
        self.xlabel = xlabel            # type: float
        self.ylabel = ylabel            # type: float
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.xlabel, 'xlabel')
        self.validate_required(self.ylabel, 'ylabel')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Xlabel'] = self.xlabel
        result['Ylabel'] = self.ylabel
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.xlabel = map.get('Xlabel')
        self.ylabel = map.get('Ylabel')
        self.name = map.get('Name')
        return self


class GetDailyReportChartResponseDayLineChartDataRspDayLineChartData(TeaModel):
    def __init__(self, harris=None, close_loop=None, bode=None, residual_stage=None):
        self.harris = harris            # type: List[GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataHarris]
        self.close_loop = close_loop    # type: List[GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataCloseLoop]
        self.bode = bode                # type: List[GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataBode]
        self.residual_stage = residual_stage  # type: List[GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataResidualStage]

    def validate(self):
        self.validate_required(self.harris, 'harris')
        if self.harris:
            for k in self.harris:
                if k:
                    k.validate()
        self.validate_required(self.close_loop, 'close_loop')
        if self.close_loop:
            for k in self.close_loop:
                if k:
                    k.validate()
        self.validate_required(self.bode, 'bode')
        if self.bode:
            for k in self.bode:
                if k:
                    k.validate()
        self.validate_required(self.residual_stage, 'residual_stage')
        if self.residual_stage:
            for k in self.residual_stage:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Harris'] = []
        if self.harris is not None:
            for k in self.harris:
                result['Harris'].append(k.to_map() if k else None)
        else:
            result['Harris'] = None
        result['CloseLoop'] = []
        if self.close_loop is not None:
            for k in self.close_loop:
                result['CloseLoop'].append(k.to_map() if k else None)
        else:
            result['CloseLoop'] = None
        result['Bode'] = []
        if self.bode is not None:
            for k in self.bode:
                result['Bode'].append(k.to_map() if k else None)
        else:
            result['Bode'] = None
        result['ResidualStage'] = []
        if self.residual_stage is not None:
            for k in self.residual_stage:
                result['ResidualStage'].append(k.to_map() if k else None)
        else:
            result['ResidualStage'] = None
        return result

    def from_map(self, map={}):
        self.harris = []
        if map.get('Harris') is not None:
            for k in map.get('Harris'):
                temp_model = GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataHarris()
                self.harris.append(temp_model.from_map(k))
        else:
            self.harris = None
        self.close_loop = []
        if map.get('CloseLoop') is not None:
            for k in map.get('CloseLoop'):
                temp_model = GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataCloseLoop()
                self.close_loop.append(temp_model.from_map(k))
        else:
            self.close_loop = None
        self.bode = []
        if map.get('Bode') is not None:
            for k in map.get('Bode'):
                temp_model = GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataBode()
                self.bode.append(temp_model.from_map(k))
        else:
            self.bode = None
        self.residual_stage = []
        if map.get('ResidualStage') is not None:
            for k in map.get('ResidualStage'):
                temp_model = GetDailyReportChartResponseDayLineChartDataRspDayLineChartDataResidualStage()
                self.residual_stage.append(temp_model.from_map(k))
        else:
            self.residual_stage = None
        return self


class GetDailyReportChartResponseDayLineChartDataRsp(TeaModel):
    def __init__(self, status=None, day_line_chart_data=None):
        self.status = status            # type: bool
        self.day_line_chart_data = day_line_chart_data  # type: GetDailyReportChartResponseDayLineChartDataRspDayLineChartData

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.day_line_chart_data, 'day_line_chart_data')
        if self.day_line_chart_data:
            self.day_line_chart_data.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.day_line_chart_data is not None:
            result['DayLineChartData'] = self.day_line_chart_data.to_map()
        else:
            result['DayLineChartData'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('DayLineChartData') is not None:
            temp_model = GetDailyReportChartResponseDayLineChartDataRspDayLineChartData()
            self.day_line_chart_data = temp_model.from_map(map['DayLineChartData'])
        else:
            self.day_line_chart_data = None
        return self


class ListPidOrganizationsRequest(TeaModel):
    def __init__(self, parent_organization_id=None):
        self.parent_organization_id = parent_organization_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ParentOrganizationId'] = self.parent_organization_id
        return result

    def from_map(self, map={}):
        self.parent_organization_id = map.get('ParentOrganizationId')
        return self


class ListPidOrganizationsResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, organization_list=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.organization_list = organization_list  # type: List[ListPidOrganizationsResponseOrganizationList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.organization_list, 'organization_list')
        if self.organization_list:
            for k in self.organization_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        result['OrganizationList'] = []
        if self.organization_list is not None:
            for k in self.organization_list:
                result['OrganizationList'].append(k.to_map() if k else None)
        else:
            result['OrganizationList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.organization_list = []
        if map.get('OrganizationList') is not None:
            for k in map.get('OrganizationList'):
                temp_model = ListPidOrganizationsResponseOrganizationList()
                self.organization_list.append(temp_model.from_map(k))
        else:
            self.organization_list = None
        return self


class ListPidOrganizationsResponseOrganizationList(TeaModel):
    def __init__(self, organization_id=None, organization_name=None, organization_level=None,
                 parent_organization_id=None, level_name=None):
        self.organization_id = organization_id  # type: str
        self.organization_name = organization_name  # type: str
        self.organization_level = organization_level  # type: int
        self.parent_organization_id = parent_organization_id  # type: str
        self.level_name = level_name    # type: str

    def validate(self):
        self.validate_required(self.organization_id, 'organization_id')
        self.validate_required(self.organization_name, 'organization_name')
        self.validate_required(self.organization_level, 'organization_level')
        self.validate_required(self.parent_organization_id, 'parent_organization_id')
        self.validate_required(self.level_name, 'level_name')

    def to_map(self):
        result = {}
        result['OrganizationId'] = self.organization_id
        result['OrganizationName'] = self.organization_name
        result['OrganizationLevel'] = self.organization_level
        result['ParentOrganizationId'] = self.parent_organization_id
        result['LevelName'] = self.level_name
        return result

    def from_map(self, map={}):
        self.organization_id = map.get('OrganizationId')
        self.organization_name = map.get('OrganizationName')
        self.organization_level = map.get('OrganizationLevel')
        self.parent_organization_id = map.get('ParentOrganizationId')
        self.level_name = map.get('LevelName')
        return self


class CreatePidDataProcessesRequest(TeaModel):
    def __init__(self, pid_project_id=None, pid_loop_id=None, data_process_time=None, client_token=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str
        self.data_process_time = data_process_time  # type: List[CreatePidDataProcessesRequestDataProcessTime]
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.data_process_time, 'data_process_time')
        if self.data_process_time:
            for k in self.data_process_time:
                if k:
                    k.validate()
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidLoopId'] = self.pid_loop_id
        result['DataProcessTime'] = []
        if self.data_process_time is not None:
            for k in self.data_process_time:
                result['DataProcessTime'].append(k.to_map() if k else None)
        else:
            result['DataProcessTime'] = None
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_loop_id = map.get('PidLoopId')
        self.data_process_time = []
        if map.get('DataProcessTime') is not None:
            for k in map.get('DataProcessTime'):
                temp_model = CreatePidDataProcessesRequestDataProcessTime()
                self.data_process_time.append(temp_model.from_map(k))
        else:
            self.data_process_time = None
        self.client_token = map.get('ClientToken')
        return self


class CreatePidDataProcessesRequestDataProcessTime(TeaModel):
    def __init__(self, start_time=None, end_time=None):
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class CreatePidDataProcessesResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_data_process_id_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_data_process_id_list = pid_data_process_id_list  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_data_process_id_list, 'pid_data_process_id_list')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidDataProcessIdList'] = self.pid_data_process_id_list
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_data_process_id_list = map.get('PidDataProcessIdList')
        return self


class GetDailyReportPidParamRequest(TeaModel):
    def __init__(self, pid_loop_id=None, pid_report_date=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_report_date = pid_report_date  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['PidReportDate'] = self.pid_report_date
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_report_date = map.get('PidReportDate')
        return self


class GetDailyReportPidParamResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, day_pid_param_rsp=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.day_pid_param_rsp = day_pid_param_rsp  # type: GetDailyReportPidParamResponseDayPidParamRsp

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.day_pid_param_rsp, 'day_pid_param_rsp')
        if self.day_pid_param_rsp:
            self.day_pid_param_rsp.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        if self.day_pid_param_rsp is not None:
            result['DayPidParamRsp'] = self.day_pid_param_rsp.to_map()
        else:
            result['DayPidParamRsp'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        if map.get('DayPidParamRsp') is not None:
            temp_model = GetDailyReportPidParamResponseDayPidParamRsp()
            self.day_pid_param_rsp = temp_model.from_map(map['DayPidParamRsp'])
        else:
            self.day_pid_param_rsp = None
        return self


class GetDailyReportPidParamResponseDayPidParamRspDayPidParam(TeaModel):
    def __init__(self, kp=None, ti=None, td=None, recommend_index=None):
        self.kp = kp                    # type: float
        self.ti = ti                    # type: float
        self.td = td                    # type: float
        self.recommend_index = recommend_index  # type: float

    def validate(self):
        self.validate_required(self.kp, 'kp')
        self.validate_required(self.ti, 'ti')
        self.validate_required(self.td, 'td')
        self.validate_required(self.recommend_index, 'recommend_index')

    def to_map(self):
        result = {}
        result['Kp'] = self.kp
        result['Ti'] = self.ti
        result['Td'] = self.td
        result['RecommendIndex'] = self.recommend_index
        return result

    def from_map(self, map={}):
        self.kp = map.get('Kp')
        self.ti = map.get('Ti')
        self.td = map.get('Td')
        self.recommend_index = map.get('RecommendIndex')
        return self


class GetDailyReportPidParamResponseDayPidParamRsp(TeaModel):
    def __init__(self, status=None, day_pid_param=None):
        self.status = status            # type: bool
        self.day_pid_param = day_pid_param  # type: GetDailyReportPidParamResponseDayPidParamRspDayPidParam

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.day_pid_param, 'day_pid_param')
        if self.day_pid_param:
            self.day_pid_param.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        if self.day_pid_param is not None:
            result['DayPidParam'] = self.day_pid_param.to_map()
        else:
            result['DayPidParam'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        if map.get('DayPidParam') is not None:
            temp_model = GetDailyReportPidParamResponseDayPidParamRspDayPidParam()
            self.day_pid_param = temp_model.from_map(map['DayPidParam'])
        else:
            self.day_pid_param = None
        return self


class AddParameterToPidLoopRequest(TeaModel):
    def __init__(self, pid_project_id=None, pid_loop_id=None, pid_loop_parameter_id=None, adjust_type=None,
                 model_distinguish=None, parameter_tuning=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str
        self.adjust_type = adjust_type  # type: int
        self.model_distinguish = model_distinguish  # type: Dict[str, Any]
        self.parameter_tuning = parameter_tuning  # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')
        self.validate_required(self.adjust_type, 'adjust_type')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidLoopId'] = self.pid_loop_id
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        result['AdjustType'] = self.adjust_type
        result['ModelDistinguish'] = self.model_distinguish
        result['ParameterTuning'] = self.parameter_tuning
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        self.adjust_type = map.get('AdjustType')
        self.model_distinguish = map.get('ModelDistinguish')
        self.parameter_tuning = map.get('ParameterTuning')
        return self


class AddParameterToPidLoopResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_loop_parameter_id=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        return self


class ListPidProjectsRequest(TeaModel):
    def __init__(self, pid_project_name=None, pid_organisation_id=None, page_size=None, current_page=None):
        self.pid_project_name = pid_project_name  # type: str
        self.pid_organisation_id = pid_organisation_id  # type: str
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PidProjectName'] = self.pid_project_name
        result['PidOrganisationId'] = self.pid_organisation_id
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        return result

    def from_map(self, map={}):
        self.pid_project_name = map.get('PidProjectName')
        self.pid_organisation_id = map.get('PidOrganisationId')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        return self


class ListPidProjectsResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, page_size=None, current_page=None,
                 total_count=None, pid_project_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.page_size = page_size      # type: int
        self.current_page = current_page  # type: int
        self.total_count = total_count  # type: int
        self.pid_project_list = pid_project_list  # type: List[ListPidProjectsResponsePidProjectList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.pid_project_list, 'pid_project_list')
        if self.pid_project_list:
            for k in self.pid_project_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PageSize'] = self.page_size
        result['CurrentPage'] = self.current_page
        result['TotalCount'] = self.total_count
        result['PidProjectList'] = []
        if self.pid_project_list is not None:
            for k in self.pid_project_list:
                result['PidProjectList'].append(k.to_map() if k else None)
        else:
            result['PidProjectList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.page_size = map.get('PageSize')
        self.current_page = map.get('CurrentPage')
        self.total_count = map.get('TotalCount')
        self.pid_project_list = []
        if map.get('PidProjectList') is not None:
            for k in map.get('PidProjectList'):
                temp_model = ListPidProjectsResponsePidProjectList()
                self.pid_project_list.append(temp_model.from_map(k))
        else:
            self.pid_project_list = None
        return self


class ListPidProjectsResponsePidProjectList(TeaModel):
    def __init__(self, pid_project_id=None, pid_project_name=None, pid_project_desc=None, pid_organisation_id=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_project_name = pid_project_name  # type: str
        self.pid_project_desc = pid_project_desc  # type: str
        self.pid_organisation_id = pid_organisation_id  # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_project_name, 'pid_project_name')
        self.validate_required(self.pid_project_desc, 'pid_project_desc')
        self.validate_required(self.pid_organisation_id, 'pid_organisation_id')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidProjectName'] = self.pid_project_name
        result['PidProjectDesc'] = self.pid_project_desc
        result['PidOrganisationId'] = self.pid_organisation_id
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_project_name = map.get('PidProjectName')
        self.pid_project_desc = map.get('PidProjectDesc')
        self.pid_organisation_id = map.get('PidOrganisationId')
        return self


class DeletePidOrganizationRequest(TeaModel):
    def __init__(self, organization_id=None):
        self.organization_id = organization_id  # type: str

    def validate(self):
        self.validate_required(self.organization_id, 'organization_id')

    def to_map(self):
        result = {}
        result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, map={}):
        self.organization_id = map.get('OrganizationId')
        return self


class DeletePidOrganizationResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class SetPidLoopDefaultParameterRequest(TeaModel):
    def __init__(self, pid_loop_id=None, pid_loop_parameter_id=None):
        self.pid_loop_id = pid_loop_id  # type: str
        self.pid_loop_parameter_id = pid_loop_parameter_id  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_id, 'pid_loop_id')
        self.validate_required(self.pid_loop_parameter_id, 'pid_loop_parameter_id')

    def to_map(self):
        result = {}
        result['PidLoopId'] = self.pid_loop_id
        result['PidLoopParameterId'] = self.pid_loop_parameter_id
        return result

    def from_map(self, map={}):
        self.pid_loop_id = map.get('PidLoopId')
        self.pid_loop_parameter_id = map.get('PidLoopParameterId')
        return self


class SetPidLoopDefaultParameterResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class GetPidOrganizationParentIdsRequest(TeaModel):
    def __init__(self, organization_id=None):
        self.organization_id = organization_id  # type: str

    def validate(self):
        self.validate_required(self.organization_id, 'organization_id')

    def to_map(self):
        result = {}
        result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, map={}):
        self.organization_id = map.get('OrganizationId')
        return self


class GetPidOrganizationParentIdsResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, organization_id_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.organization_id_list = organization_id_list  # type: List[str]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.organization_id_list, 'organization_id_list')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['OrganizationIdList'] = self.organization_id_list
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.organization_id_list = map.get('OrganizationIdList')
        return self


class CreatePidOrganizationRequest(TeaModel):
    def __init__(self, organization_name=None, parent_organization_id=None, client_token=None):
        self.organization_name = organization_name  # type: str
        self.parent_organization_id = parent_organization_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.organization_name, 'organization_name')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['OrganizationName'] = self.organization_name
        result['ParentOrganizationId'] = self.parent_organization_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.organization_name = map.get('OrganizationName')
        self.parent_organization_id = map.get('ParentOrganizationId')
        self.client_token = map.get('ClientToken')
        return self


class CreatePidOrganizationResponse(TeaModel):
    def __init__(self, request_id=None, organization_id=None, code=None, success=None, message=None):
        self.request_id = request_id    # type: str
        self.organization_id = organization_id  # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.message = message          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.organization_id, 'organization_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.message, 'message')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OrganizationId'] = self.organization_id
        result['Code'] = self.code
        result['Success'] = self.success
        result['Message'] = self.message
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.organization_id = map.get('OrganizationId')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.message = map.get('Message')
        return self


class UpdatePidOrganizationRequest(TeaModel):
    def __init__(self, organization_id=None, organization_name=None):
        self.organization_id = organization_id  # type: str
        self.organization_name = organization_name  # type: str

    def validate(self):
        self.validate_required(self.organization_id, 'organization_id')
        self.validate_required(self.organization_name, 'organization_name')

    def to_map(self):
        result = {}
        result['OrganizationId'] = self.organization_id
        result['OrganizationName'] = self.organization_name
        return result

    def from_map(self, map={}):
        self.organization_id = map.get('OrganizationId')
        self.organization_name = map.get('OrganizationName')
        return self


class UpdatePidOrganizationResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class CreatePidLoopRequest(TeaModel):
    def __init__(self, pid_loop_name=None, is_crucial_pid_loop=None, pid_loop_desc=None, pid_project_id=None,
                 pid_loop_dcs_type=None, pid_loop_type=None, pid_loop_configuration=None, client_token=None):
        self.pid_loop_name = pid_loop_name  # type: str
        self.is_crucial_pid_loop = is_crucial_pid_loop  # type: bool
        self.pid_loop_desc = pid_loop_desc  # type: str
        self.pid_project_id = pid_project_id  # type: str
        self.pid_loop_dcs_type = pid_loop_dcs_type  # type: str
        self.pid_loop_type = pid_loop_type  # type: str
        self.pid_loop_configuration = pid_loop_configuration  # type: Dict[str, Any]
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.pid_loop_name, 'pid_loop_name')
        self.validate_required(self.is_crucial_pid_loop, 'is_crucial_pid_loop')
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_loop_dcs_type, 'pid_loop_dcs_type')
        self.validate_required(self.pid_loop_type, 'pid_loop_type')
        self.validate_required(self.pid_loop_configuration, 'pid_loop_configuration')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['PidLoopName'] = self.pid_loop_name
        result['IsCrucialPidLoop'] = self.is_crucial_pid_loop
        result['PidLoopDesc'] = self.pid_loop_desc
        result['PidProjectId'] = self.pid_project_id
        result['PidLoopDcsType'] = self.pid_loop_dcs_type
        result['PidLoopType'] = self.pid_loop_type
        result['PidLoopConfiguration'] = self.pid_loop_configuration
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.pid_loop_name = map.get('PidLoopName')
        self.is_crucial_pid_loop = map.get('IsCrucialPidLoop')
        self.pid_loop_desc = map.get('PidLoopDesc')
        self.pid_project_id = map.get('PidProjectId')
        self.pid_loop_dcs_type = map.get('PidLoopDcsType')
        self.pid_loop_type = map.get('PidLoopType')
        self.pid_loop_configuration = map.get('PidLoopConfiguration')
        self.client_token = map.get('ClientToken')
        return self


class CreatePidLoopResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_loop_id=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_loop_id = pid_loop_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_loop_id, 'pid_loop_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidLoopId'] = self.pid_loop_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_loop_id = map.get('PidLoopId')
        return self


class UpdatePidProjectRequest(TeaModel):
    def __init__(self, pid_project_id=None, pid_project_name=None, pid_project_desc=None, pid_organisation_id=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_project_name = pid_project_name  # type: str
        self.pid_project_desc = pid_project_desc  # type: str
        self.pid_organisation_id = pid_organisation_id  # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_organisation_id, 'pid_organisation_id')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidProjectName'] = self.pid_project_name
        result['PidProjectDesc'] = self.pid_project_desc
        result['PidOrganisationId'] = self.pid_organisation_id
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_project_name = map.get('PidProjectName')
        self.pid_project_desc = map.get('PidProjectDesc')
        self.pid_organisation_id = map.get('PidOrganisationId')
        return self


class UpdatePidProjectResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class ListPidTagsRequest(TeaModel):
    def __init__(self, pid_project_id=None, pid_tag_name=None, current_page=None, page_size=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_tag_name = pid_tag_name  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidTagName'] = self.pid_tag_name
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_tag_name = map.get('PidTagName')
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        return self


class ListPidTagsResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, current_page=None, page_size=None,
                 total_count=None, pid_tag_list=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.current_page = current_page  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.pid_tag_list = pid_tag_list  # type: List[ListPidTagsResponsePidTagList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.current_page, 'current_page')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.pid_tag_list, 'pid_tag_list')
        if self.pid_tag_list:
            for k in self.pid_tag_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['CurrentPage'] = self.current_page
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        result['PidTagList'] = []
        if self.pid_tag_list is not None:
            for k in self.pid_tag_list:
                result['PidTagList'].append(k.to_map() if k else None)
        else:
            result['PidTagList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.current_page = map.get('CurrentPage')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        self.pid_tag_list = []
        if map.get('PidTagList') is not None:
            for k in map.get('PidTagList'):
                temp_model = ListPidTagsResponsePidTagList()
                self.pid_tag_list.append(temp_model.from_map(k))
        else:
            self.pid_tag_list = None
        return self


class ListPidTagsResponsePidTagList(TeaModel):
    def __init__(self, pid_tag_id=None, pid_project_id=None, pid_tag_name=None, pid_tag_type=None,
                 upload_project_id=None):
        self.pid_tag_id = pid_tag_id    # type: str
        self.pid_project_id = pid_project_id  # type: str
        self.pid_tag_name = pid_tag_name  # type: str
        self.pid_tag_type = pid_tag_type  # type: str
        self.upload_project_id = upload_project_id  # type: int

    def validate(self):
        self.validate_required(self.pid_tag_id, 'pid_tag_id')
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_tag_name, 'pid_tag_name')
        self.validate_required(self.pid_tag_type, 'pid_tag_type')
        self.validate_required(self.upload_project_id, 'upload_project_id')

    def to_map(self):
        result = {}
        result['PidTagId'] = self.pid_tag_id
        result['PidProjectId'] = self.pid_project_id
        result['PidTagName'] = self.pid_tag_name
        result['PidTagType'] = self.pid_tag_type
        result['UploadProjectId'] = self.upload_project_id
        return result

    def from_map(self, map={}):
        self.pid_tag_id = map.get('PidTagId')
        self.pid_project_id = map.get('PidProjectId')
        self.pid_tag_name = map.get('PidTagName')
        self.pid_tag_type = map.get('PidTagType')
        self.upload_project_id = map.get('UploadProjectId')
        return self


class DeletePidDataProcessRequest(TeaModel):
    def __init__(self, pid_data_process_id=None):
        self.pid_data_process_id = pid_data_process_id  # type: str

    def validate(self):
        self.validate_required(self.pid_data_process_id, 'pid_data_process_id')

    def to_map(self):
        result = {}
        result['PidDataProcessId'] = self.pid_data_process_id
        return result

    def from_map(self, map={}):
        self.pid_data_process_id = map.get('PidDataProcessId')
        return self


class DeletePidDataProcessResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None, pid_data=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool
        self.pid_data = pid_data        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')
        self.validate_required(self.pid_data, 'pid_data')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        result['PidData'] = self.pid_data
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        self.pid_data = map.get('PidData')
        return self


class CreatePidDataSourceRequest(TeaModel):
    def __init__(self, pid_project_id=None, type=None, oss_path=None, file_name=None, open_upload=None,
                 need_create_time=None, start_date=None, sample_time=None, client_token=None):
        self.pid_project_id = pid_project_id  # type: str
        self.type = type                # type: str
        self.oss_path = oss_path        # type: str
        self.file_name = file_name      # type: str
        self.open_upload = open_upload  # type: int
        self.need_create_time = need_create_time  # type: int
        self.start_date = start_date    # type: str
        self.sample_time = sample_time  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.oss_path, 'oss_path')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.need_create_time, 'need_create_time')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['Type'] = self.type
        result['OssPath'] = self.oss_path
        result['FileName'] = self.file_name
        result['OpenUpload'] = self.open_upload
        result['NeedCreateTime'] = self.need_create_time
        result['StartDate'] = self.start_date
        result['SampleTime'] = self.sample_time
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.type = map.get('Type')
        self.oss_path = map.get('OssPath')
        self.file_name = map.get('FileName')
        self.open_upload = map.get('OpenUpload')
        self.need_create_time = map.get('NeedCreateTime')
        self.start_date = map.get('StartDate')
        self.sample_time = map.get('SampleTime')
        self.client_token = map.get('ClientToken')
        return self


class CreatePidDataSourceResponse(TeaModel):
    def __init__(self, request_id=None, success=None, code=None, message=None, pid_data_source_id=None):
        self.request_id = request_id    # type: str
        self.success = success          # type: bool
        self.code = code                # type: str
        self.message = message          # type: str
        self.pid_data_source_id = pid_data_source_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.success, 'success')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.pid_data_source_id, 'pid_data_source_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Success'] = self.success
        result['Code'] = self.code
        result['Message'] = self.message
        result['PidDataSourceId'] = self.pid_data_source_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.success = map.get('Success')
        self.code = map.get('Code')
        self.message = map.get('Message')
        self.pid_data_source_id = map.get('PidDataSourceId')
        return self


class CreatePidDataSourceAdvanceRequest(TeaModel):
    def __init__(self, oss_path_object=None, pid_project_id=None, type=None, file_name=None, open_upload=None,
                 need_create_time=None, start_date=None, sample_time=None, client_token=None):
        self.oss_path_object = oss_path_object  # type: BinaryIO
        self.pid_project_id = pid_project_id  # type: str
        self.type = type                # type: str
        self.file_name = file_name      # type: str
        self.open_upload = open_upload  # type: int
        self.need_create_time = need_create_time  # type: int
        self.start_date = start_date    # type: str
        self.sample_time = sample_time  # type: int
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.oss_path_object, 'oss_path_object')
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.type, 'type')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.need_create_time, 'need_create_time')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['OssPathObject'] = self.oss_path_object
        result['PidProjectId'] = self.pid_project_id
        result['Type'] = self.type
        result['FileName'] = self.file_name
        result['OpenUpload'] = self.open_upload
        result['NeedCreateTime'] = self.need_create_time
        result['StartDate'] = self.start_date
        result['SampleTime'] = self.sample_time
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.oss_path_object = map.get('OssPathObject')
        self.pid_project_id = map.get('PidProjectId')
        self.type = map.get('Type')
        self.file_name = map.get('FileName')
        self.open_upload = map.get('OpenUpload')
        self.need_create_time = map.get('NeedCreateTime')
        self.start_date = map.get('StartDate')
        self.sample_time = map.get('SampleTime')
        self.client_token = map.get('ClientToken')
        return self


class DeletePidProjectRequest(TeaModel):
    def __init__(self, pid_project_id=None):
        self.pid_project_id = pid_project_id  # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        return self


class DeletePidProjectResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self


class DeletePidTagRequest(TeaModel):
    def __init__(self, pid_project_id=None, pid_tag_id=None):
        self.pid_project_id = pid_project_id  # type: str
        self.pid_tag_id = pid_tag_id    # type: str

    def validate(self):
        self.validate_required(self.pid_project_id, 'pid_project_id')
        self.validate_required(self.pid_tag_id, 'pid_tag_id')

    def to_map(self):
        result = {}
        result['PidProjectId'] = self.pid_project_id
        result['PidTagId'] = self.pid_tag_id
        return result

    def from_map(self, map={}):
        self.pid_project_id = map.get('PidProjectId')
        self.pid_tag_id = map.get('PidTagId')
        return self


class DeletePidTagResponse(TeaModel):
    def __init__(self, request_id=None, message=None, code=None, success=None):
        self.request_id = request_id    # type: str
        self.message = message          # type: str
        self.code = code                # type: str
        self.success = success          # type: bool

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message, 'message')
        self.validate_required(self.code, 'code')
        self.validate_required(self.success, 'success')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Message'] = self.message
        result['Code'] = self.code
        result['Success'] = self.success
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message = map.get('Message')
        self.code = map.get('Code')
        self.success = map.get('Success')
        return self
