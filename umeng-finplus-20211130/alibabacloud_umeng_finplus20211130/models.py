# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CancelComputeTaskByBcIdRequest(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
    ):
        self.bc_id = bc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        return self


class CancelComputeTaskByBcIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class CancelComputeTaskByBcIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelComputeTaskByBcIdResponseBody = None,
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
            temp_model = CancelComputeTaskByBcIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComputeTaskByDataSetIdRequestBatchInfoFormCuVersions(TeaModel):
    def __init__(
        self,
        cu_id: str = None,
        cu_version: str = None,
    ):
        self.cu_id = cu_id
        self.cu_version = cu_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_id is not None:
            result['CuId'] = self.cu_id
        if self.cu_version is not None:
            result['CuVersion'] = self.cu_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CuId') is not None:
            self.cu_id = m.get('CuId')
        if m.get('CuVersion') is not None:
            self.cu_version = m.get('CuVersion')
        return self


class CreateComputeTaskByDataSetIdRequestBatchInfoForm(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        cu_versions: List[CreateComputeTaskByDataSetIdRequestBatchInfoFormCuVersions] = None,
    ):
        self.app_id = app_id
        self.cu_versions = cu_versions

    def validate(self):
        if self.cu_versions:
            for k in self.cu_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        result['CuVersions'] = []
        if self.cu_versions is not None:
            for k in self.cu_versions:
                result['CuVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        self.cu_versions = []
        if m.get('CuVersions') is not None:
            for k in m.get('CuVersions'):
                temp_model = CreateComputeTaskByDataSetIdRequestBatchInfoFormCuVersions()
                self.cu_versions.append(temp_model.from_map(k))
        return self


class CreateComputeTaskByDataSetIdRequest(TeaModel):
    def __init__(
        self,
        batch_info_form: List[CreateComputeTaskByDataSetIdRequestBatchInfoForm] = None,
        dataset_id: int = None,
        name: str = None,
        remarks: str = None,
    ):
        self.batch_info_form = batch_info_form
        self.dataset_id = dataset_id
        self.name = name
        self.remarks = remarks

    def validate(self):
        if self.batch_info_form:
            for k in self.batch_info_form:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchInfoForm'] = []
        if self.batch_info_form is not None:
            for k in self.batch_info_form:
                result['BatchInfoForm'].append(k.to_map() if k else None)
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_info_form = []
        if m.get('BatchInfoForm') is not None:
            for k in m.get('BatchInfoForm'):
                temp_model = CreateComputeTaskByDataSetIdRequestBatchInfoForm()
                self.batch_info_form.append(temp_model.from_map(k))
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        return self


class CreateComputeTaskByDataSetIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[int] = None,
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


class CreateComputeTaskByDataSetIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateComputeTaskByDataSetIdResponseBody = None,
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
            temp_model = CreateComputeTaskByDataSetIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateComputeTaskByMultiDataSetIdRequest(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        data_set_ids: str = None,
        name: str = None,
        remarks: str = None,
    ):
        self.app_id = app_id
        self.data_set_ids = data_set_ids
        self.name = name
        self.remarks = remarks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.data_set_ids is not None:
            result['dataSetIds'] = self.data_set_ids
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('dataSetIds') is not None:
            self.data_set_ids = m.get('dataSetIds')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        return self


class CreateComputeTaskByMultiDataSetIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class CreateComputeTaskByMultiDataSetIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateComputeTaskByMultiDataSetIdResponseBody = None,
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
            temp_model = CreateComputeTaskByMultiDataSetIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAvailableDataSetListResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_set_type: int = None,
        dataset_id: int = None,
        id_type_desc: str = None,
        name: str = None,
        status_desc: str = None,
    ):
        self.create_time = create_time
        self.data_set_type = data_set_type
        self.dataset_id = dataset_id
        self.id_type_desc = id_type_desc
        self.name = name
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.id_type_desc is not None:
            result['idTypeDesc'] = self.id_type_desc
        if self.name is not None:
            result['name'] = self.name
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('idTypeDesc') is not None:
            self.id_type_desc = m.get('idTypeDesc')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        return self


class GetAvailableDataSetListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetAvailableDataSetListResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAvailableDataSetListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAvailableDataSetListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAvailableDataSetListResponseBody = None,
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
            temp_model = GetAvailableDataSetListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetComputeResultRequest(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
    ):
        self.bc_id = bc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        return self


class GetComputeResultResponseBodyData(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
        billed_num: int = None,
        code_10000num: int = None,
        code_108num: int = None,
        code_109num: int = None,
        export_file_name: str = None,
        file_line_number: int = None,
        name: str = None,
        password: str = None,
        state: str = None,
    ):
        self.bc_id = bc_id
        self.billed_num = billed_num
        self.code_10000num = code_10000num
        self.code_108num = code_108num
        self.code_109num = code_109num
        self.export_file_name = export_file_name
        self.file_line_number = file_line_number
        self.name = name
        self.password = password
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.billed_num is not None:
            result['billedNum'] = self.billed_num
        if self.code_10000num is not None:
            result['code10000Num'] = self.code_10000num
        if self.code_108num is not None:
            result['code108Num'] = self.code_108num
        if self.code_109num is not None:
            result['code109Num'] = self.code_109num
        if self.export_file_name is not None:
            result['exportFileName'] = self.export_file_name
        if self.file_line_number is not None:
            result['fileLineNumber'] = self.file_line_number
        if self.name is not None:
            result['name'] = self.name
        if self.password is not None:
            result['password'] = self.password
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('billedNum') is not None:
            self.billed_num = m.get('billedNum')
        if m.get('code10000Num') is not None:
            self.code_10000num = m.get('code10000Num')
        if m.get('code108Num') is not None:
            self.code_108num = m.get('code108Num')
        if m.get('code109Num') is not None:
            self.code_109num = m.get('code109Num')
        if m.get('exportFileName') is not None:
            self.export_file_name = m.get('exportFileName')
        if m.get('fileLineNumber') is not None:
            self.file_line_number = m.get('fileLineNumber')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class GetComputeResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetComputeResultResponseBodyData = None,
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
            temp_model = GetComputeResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetComputeResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetComputeResultResponseBody = None,
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
            temp_model = GetComputeResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSetStatusRequest(TeaModel):
    def __init__(
        self,
        data_set_id: int = None,
    ):
        self.data_set_id = data_set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_id is not None:
            result['dataSetId'] = self.data_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSetId') is not None:
            self.data_set_id = m.get('dataSetId')
        return self


class GetDataSetStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_set_type: int = None,
        dataset_id: int = None,
        id_type_desc: str = None,
        message: str = None,
        name: str = None,
        status_desc: str = None,
    ):
        self.create_time = create_time
        self.data_set_type = data_set_type
        self.dataset_id = dataset_id
        self.id_type_desc = id_type_desc
        self.message = message
        self.name = name
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.id_type_desc is not None:
            result['idTypeDesc'] = self.id_type_desc
        if self.message is not None:
            result['message'] = self.message
        if self.name is not None:
            result['name'] = self.name
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('idTypeDesc') is not None:
            self.id_type_desc = m.get('idTypeDesc')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        return self


class GetDataSetStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDataSetStatusResponseBodyData = None,
        msg: str = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.success = success
        self.request_id = request_id

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
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetDataSetStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetDataSetStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataSetStatusResponseBody = None,
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
            temp_model = GetDataSetStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSetStsAKResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        id: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        self.bucket = bucket
        self.endpoint = endpoint
        self.id = id
        self.path = path
        self.secret = secret
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.secret is not None:
            result['Secret'] = self.secret
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetDataSetStsAKResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDataSetStsAKResponseBodyData = None,
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
            temp_model = GetDataSetStsAKResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataSetStsAKResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataSetStsAKResponseBody = None,
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
            temp_model = GetDataSetStsAKResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDataSetTaskRequest(TeaModel):
    def __init__(
        self,
        data_set_type: int = None,
        id_type: int = None,
        name: str = None,
        oss_file_name: str = None,
    ):
        self.data_set_type = data_set_type
        self.id_type = id_type
        self.name = name
        self.oss_file_name = oss_file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.id_type is not None:
            result['idType'] = self.id_type
        if self.name is not None:
            result['name'] = self.name
        if self.oss_file_name is not None:
            result['ossFileName'] = self.oss_file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('idType') is not None:
            self.id_type = m.get('idType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ossFileName') is not None:
            self.oss_file_name = m.get('ossFileName')
        return self


class SubmitDataSetTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        msg: str = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.success = success
        self.request_id = request_id

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
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class SubmitDataSetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDataSetTaskResponseBody = None,
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
            temp_model = SubmitDataSetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelYydTaskByBcIdRequest(TeaModel):
    def __init__(
        self,
        bc_id: int = None,
    ):
        self.bc_id = bc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        return self


class CancelYydTaskByBcIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
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


class CancelYydTaskByBcIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelYydTaskByBcIdResponseBody = None,
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
            temp_model = CancelYydTaskByBcIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateYydComputeTaskRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        name: str = None,
        remarks: str = None,
        app_id: int = None,
    ):
        self.dataset_id = dataset_id
        self.name = name
        self.remarks = remarks
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.name is not None:
            result['Name'] = self.name
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.app_id is not None:
            result['appId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        return self


class CreateYydComputeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
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


class CreateYydComputeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateYydComputeTaskResponseBody = None,
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
            temp_model = CreateYydComputeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateYydDataSetRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        oss_file_name: str = None,
    ):
        self.name = name
        self.oss_file_name = oss_file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.oss_file_name is not None:
            result['ossFileName'] = self.oss_file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ossFileName') is not None:
            self.oss_file_name = m.get('ossFileName')
        return self


class CreateYydDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        msg: str = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.success = success
        self.request_id = request_id

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
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateYydDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateYydDataSetResponseBody = None,
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
            temp_model = CreateYydDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYydComputeTaskListResponseBodyData(TeaModel):
    def __init__(
        self,
        app_id: int = None,
        bc_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        remarks: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.bc_id = bc_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.name = name
        self.remarks = remarks
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.bc_id is not None:
            result['bcId'] = self.bc_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.name is not None:
            result['name'] = self.name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('bcId') is not None:
            self.bc_id = m.get('bcId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListYydComputeTaskListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListYydComputeTaskListResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListYydComputeTaskListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListYydComputeTaskListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListYydComputeTaskListResponseBody = None,
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
            temp_model = ListYydComputeTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListYydDataSetResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        data_set_type: int = None,
        dataset_id: int = None,
        id_type_desc: str = None,
        message: str = None,
        name: str = None,
        status_desc: str = None,
    ):
        self.create_time = create_time
        self.data_set_type = data_set_type
        self.dataset_id = dataset_id
        self.id_type_desc = id_type_desc
        self.message = message
        self.name = name
        self.status_desc = status_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.data_set_type is not None:
            result['dataSetType'] = self.data_set_type
        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id
        if self.id_type_desc is not None:
            result['idTypeDesc'] = self.id_type_desc
        if self.message is not None:
            result['message'] = self.message
        if self.name is not None:
            result['name'] = self.name
        if self.status_desc is not None:
            result['statusDesc'] = self.status_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dataSetType') is not None:
            self.data_set_type = m.get('dataSetType')
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('idTypeDesc') is not None:
            self.id_type_desc = m.get('idTypeDesc')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('statusDesc') is not None:
            self.status_desc = m.get('statusDesc')
        return self


class ListYydDataSetResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListYydDataSetResponseBodyData] = None,
        msg: str = None,
        success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.success = success
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListYydDataSetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListYydDataSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListYydDataSetResponseBody = None,
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
            temp_model = ListYydDataSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


