# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CheckCallbackRequest(TeaModel):
    def __init__(
        self,
        callback_result_string: str = None,
    ):
        self.callback_result_string = callback_result_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_result_string is not None:
            result['CallbackResultString'] = self.callback_result_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackResultString') is not None:
            self.callback_result_string = m.get('CallbackResultString')
        return self


class CheckCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        return_code: str = None,
        return_value: bool = None,
    ):
        self.request_id = request_id
        self.return_code = return_code
        self.return_value = return_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')
        return self


class CheckCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckCallbackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateManualDagRequest(TeaModel):
    def __init__(
        self,
        bizdate: str = None,
        dag_para: str = None,
        flow_name: str = None,
        node_para: str = None,
        project_name: str = None,
    ):
        self.bizdate = bizdate
        self.dag_para = dag_para
        self.flow_name = flow_name
        self.node_para = node_para
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate
        if self.dag_para is not None:
            result['DagPara'] = self.dag_para
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.node_para is not None:
            result['NodePara'] = self.node_para
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')
        if m.get('DagPara') is not None:
            self.dag_para = m.get('DagPara')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('NodePara') is not None:
            self.node_para = m.get('NodePara')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class CreateManualDagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        return_code: str = None,
        return_error_solution: str = None,
        return_message: str = None,
        return_value: int = None,
    ):
        self.request_id = request_id
        self.return_code = return_code
        self.return_error_solution = return_error_solution
        self.return_message = return_message
        self.return_value = return_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.return_error_solution is not None:
            result['ReturnErrorSolution'] = self.return_error_solution
        if self.return_message is not None:
            result['ReturnMessage'] = self.return_message
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnErrorSolution') is not None:
            self.return_error_solution = m.get('ReturnErrorSolution')
        if m.get('ReturnMessage') is not None:
            self.return_message = m.get('ReturnMessage')
        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')
        return self


class CreateManualDagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateManualDagResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateManualDagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRealTimeProcessRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        create_res_group: bool = None,
        data_source: str = None,
        dataworks_version: str = None,
        file_id: int = None,
        job_config: str = None,
        project_id: int = None,
        resource_spec: str = None,
        table_rule: str = None,
        tables: str = None,
    ):
        self.action_type = action_type
        self.create_res_group = create_res_group
        self.data_source = data_source
        self.dataworks_version = dataworks_version
        self.file_id = file_id
        self.job_config = job_config
        self.project_id = project_id
        self.resource_spec = resource_spec
        self.table_rule = table_rule
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.create_res_group is not None:
            result['CreateResGroup'] = self.create_res_group
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.dataworks_version is not None:
            result['DataworksVersion'] = self.dataworks_version
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.job_config is not None:
            result['JobConfig'] = self.job_config
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec
        if self.table_rule is not None:
            result['TableRule'] = self.table_rule
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CreateResGroup') is not None:
            self.create_res_group = m.get('CreateResGroup')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('DataworksVersion') is not None:
            self.dataworks_version = m.get('DataworksVersion')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('JobConfig') is not None:
            self.job_config = m.get('JobConfig')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceSpec') is not None:
            self.resource_spec = m.get('ResourceSpec')
        if m.get('TableRule') is not None:
            self.table_rule = m.get('TableRule')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class CreateRealTimeProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateRealTimeProcessResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateRealTimeProcessResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateRealTimeProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRealTimeProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRealTimeProcessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateRealTimeProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDISyncTaskRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DeleteDISyncTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeleteDISyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDISyncTaskResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDISyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDISyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.project_identifier = project_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployDISyncTaskRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DeployDISyncTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DeployDISyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: DeployDISyncTaskResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeployDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeployDISyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployDISyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEmrHiveTableRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeEmrHiveTableResponseBodyDataColumns(TeaModel):
    def __init__(
        self,
        column_comment: str = None,
        column_name: str = None,
        column_position: int = None,
        column_type: str = None,
        comment: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        self.column_comment = column_comment
        self.column_name = column_name
        self.column_position = column_position
        self.column_type = column_type
        self.comment = comment
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_comment is not None:
            result['ColumnComment'] = self.column_comment
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_position is not None:
            result['ColumnPosition'] = self.column_position
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnComment') is not None:
            self.column_comment = m.get('ColumnComment')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnPosition') is not None:
            self.column_position = m.get('ColumnPosition')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class DescribeEmrHiveTableResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        cluster_biz_name: str = None,
        columns: List[DescribeEmrHiveTableResponseBodyDataColumns] = None,
        database_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        input_format: str = None,
        is_compressed: bool = None,
        is_temporary: bool = None,
        last_access_time: str = None,
        last_modify_time: str = None,
        location: str = None,
        output_format: str = None,
        owner: str = None,
        owner_id: str = None,
        owner_type: str = None,
        partition_keys: str = None,
        serialization_lib: str = None,
        table_comment: str = None,
        table_desc: str = None,
        table_name: str = None,
        table_parameters: str = None,
        table_size: int = None,
        table_type: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.cluster_biz_name = cluster_biz_name
        self.columns = columns
        self.database_name = database_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.input_format = input_format
        self.is_compressed = is_compressed
        self.is_temporary = is_temporary
        self.last_access_time = last_access_time
        self.last_modify_time = last_modify_time
        self.location = location
        self.output_format = output_format
        self.owner = owner
        self.owner_id = owner_id
        self.owner_type = owner_type
        self.partition_keys = partition_keys
        self.serialization_lib = serialization_lib
        self.table_comment = table_comment
        self.table_desc = table_desc
        self.table_name = table_name
        self.table_parameters = table_parameters
        self.table_size = table_size
        self.table_type = table_type

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_biz_name is not None:
            result['ClusterBizName'] = self.cluster_biz_name
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed
        if self.is_temporary is not None:
            result['IsTemporary'] = self.is_temporary
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        if self.table_comment is not None:
            result['TableComment'] = self.table_comment
        if self.table_desc is not None:
            result['TableDesc'] = self.table_desc
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_parameters is not None:
            result['TableParameters'] = self.table_parameters
        if self.table_size is not None:
            result['TableSize'] = self.table_size
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterBizName') is not None:
            self.cluster_biz_name = m.get('ClusterBizName')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = DescribeEmrHiveTableResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')
        if m.get('IsTemporary') is not None:
            self.is_temporary = m.get('IsTemporary')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        if m.get('TableComment') is not None:
            self.table_comment = m.get('TableComment')
        if m.get('TableDesc') is not None:
            self.table_desc = m.get('TableDesc')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableParameters') is not None:
            self.table_parameters = m.get('TableParameters')
        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class DescribeEmrHiveTableResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeEmrHiveTableResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeEmrHiveTableResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeEmrHiveTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEmrHiveTableResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEmrHiveTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDISyncInstanceInfoRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetDISyncInstanceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        name: str = None,
        status: str = None,
    ):
        self.message = message
        self.name = name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDISyncInstanceInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDISyncInstanceInfoResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDISyncInstanceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDISyncInstanceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDISyncInstanceInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDISyncInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDISyncTaskRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetDISyncTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        status: str = None,
    ):
        self.code = code
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDISyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDISyncTaskResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDISyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDISyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSwitchValueRequest(TeaModel):
    def __init__(
        self,
        switch_name: str = None,
    ):
        self.switch_name = switch_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.switch_name is not None:
            result['SwitchName'] = self.switch_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchName') is not None:
            self.switch_name = m.get('SwitchName')
        return self


class GetSwitchValueResponseBody(TeaModel):
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


class GetSwitchValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSwitchValueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSwitchValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmrHiveAuditLogsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListEmrHiveAuditLogsResponseBodyDataPagedData(TeaModel):
    def __init__(
        self,
        database: str = None,
        event_time: int = None,
        groups: List[str] = None,
        operation: str = None,
        table: str = None,
        user: str = None,
    ):
        self.database = database
        self.event_time = event_time
        self.groups = groups
        self.operation = operation
        self.table = table
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.table is not None:
            result['Table'] = self.table
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class ListEmrHiveAuditLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        paged_data: List[ListEmrHiveAuditLogsResponseBodyDataPagedData] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.paged_data = paged_data
        self.total_count = total_count

    def validate(self):
        if self.paged_data:
            for k in self.paged_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListEmrHiveAuditLogsResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEmrHiveAuditLogsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEmrHiveAuditLogsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListEmrHiveAuditLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEmrHiveAuditLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEmrHiveAuditLogsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEmrHiveAuditLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmrHiveDatabasesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListEmrHiveDatabasesResponseBodyData(TeaModel):
    def __init__(
        self,
        comment: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        location: str = None,
        name: str = None,
        owner: str = None,
        owner_id: str = None,
        owner_type: str = None,
        parameters: str = None,
        region: str = None,
        status: str = None,
        type: str = None,
    ):
        self.comment = comment
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.location = location
        self.name = name
        self.owner = owner
        self.owner_id = owner_id
        self.owner_type = owner_type
        self.parameters = parameters
        self.region = region
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.location is not None:
            result['Location'] = self.location
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEmrHiveDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListEmrHiveDatabasesResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEmrHiveDatabasesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEmrHiveDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEmrHiveDatabasesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEmrHiveDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmrHiveTablesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListEmrHiveTablesResponseBodyDataPagedData(TeaModel):
    def __init__(
        self,
        cluster_biz_id: str = None,
        cluster_biz_name: str = None,
        database_name: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        input_format: str = None,
        is_compressed: bool = None,
        is_temporary: bool = None,
        last_access_time: str = None,
        last_modify_time: str = None,
        location: str = None,
        output_format: str = None,
        owner: str = None,
        owner_id: str = None,
        owner_type: str = None,
        partition_keys: str = None,
        serialization_lib: str = None,
        table_comment: str = None,
        table_desc: str = None,
        table_name: str = None,
        table_parameters: str = None,
        table_type: str = None,
    ):
        self.cluster_biz_id = cluster_biz_id
        self.cluster_biz_name = cluster_biz_name
        self.database_name = database_name
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.input_format = input_format
        self.is_compressed = is_compressed
        self.is_temporary = is_temporary
        self.last_access_time = last_access_time
        self.last_modify_time = last_modify_time
        self.location = location
        self.output_format = output_format
        self.owner = owner
        self.owner_id = owner_id
        self.owner_type = owner_type
        self.partition_keys = partition_keys
        self.serialization_lib = serialization_lib
        self.table_comment = table_comment
        self.table_desc = table_desc
        self.table_name = table_name
        self.table_parameters = table_parameters
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_biz_name is not None:
            result['ClusterBizName'] = self.cluster_biz_name
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed
        if self.is_temporary is not None:
            result['IsTemporary'] = self.is_temporary
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        if self.table_comment is not None:
            result['TableComment'] = self.table_comment
        if self.table_desc is not None:
            result['TableDesc'] = self.table_desc
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_parameters is not None:
            result['TableParameters'] = self.table_parameters
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterBizName') is not None:
            self.cluster_biz_name = m.get('ClusterBizName')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')
        if m.get('IsTemporary') is not None:
            self.is_temporary = m.get('IsTemporary')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        if m.get('TableComment') is not None:
            self.table_comment = m.get('TableComment')
        if m.get('TableDesc') is not None:
            self.table_desc = m.get('TableDesc')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableParameters') is not None:
            self.table_parameters = m.get('TableParameters')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class ListEmrHiveTablesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        paged_data: List[ListEmrHiveTablesResponseBodyDataPagedData] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.paged_data = paged_data
        self.total_count = total_count

    def validate(self):
        if self.paged_data:
            for k in self.paged_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListEmrHiveTablesResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEmrHiveTablesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEmrHiveTablesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListEmrHiveTablesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListEmrHiveTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListEmrHiveTablesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListEmrHiveTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHiveColumnLineagesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        column_name: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.column_name = column_name
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveColumnLineagesResponseBodyDataDownstreamLineages(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        column_name: str = None,
        create_time: str = None,
        database_name: str = None,
        direct_down_column_number: int = None,
        direct_down_table_number: int = None,
        direct_upper_column_number: int = None,
        direct_upper_table_number: int = None,
        modified_time: str = None,
        source: str = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.column_name = column_name
        self.create_time = create_time
        self.database_name = database_name
        self.direct_down_column_number = direct_down_column_number
        self.direct_down_table_number = direct_down_table_number
        self.direct_upper_column_number = direct_upper_column_number
        self.direct_upper_table_number = direct_upper_table_number
        self.modified_time = modified_time
        self.source = source
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.direct_down_column_number is not None:
            result['DirectDownColumnNumber'] = self.direct_down_column_number
        if self.direct_down_table_number is not None:
            result['DirectDownTableNumber'] = self.direct_down_table_number
        if self.direct_upper_column_number is not None:
            result['DirectUpperColumnNumber'] = self.direct_upper_column_number
        if self.direct_upper_table_number is not None:
            result['DirectUpperTableNumber'] = self.direct_upper_table_number
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DirectDownColumnNumber') is not None:
            self.direct_down_column_number = m.get('DirectDownColumnNumber')
        if m.get('DirectDownTableNumber') is not None:
            self.direct_down_table_number = m.get('DirectDownTableNumber')
        if m.get('DirectUpperColumnNumber') is not None:
            self.direct_upper_column_number = m.get('DirectUpperColumnNumber')
        if m.get('DirectUpperTableNumber') is not None:
            self.direct_upper_table_number = m.get('DirectUpperTableNumber')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveColumnLineagesResponseBodyDataUpstreamLineages(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        column_name: str = None,
        create_time: str = None,
        database_name: str = None,
        direct_down_column_number: int = None,
        direct_down_table_number: int = None,
        direct_upper_column_number: int = None,
        direct_upper_table_number: int = None,
        modified_time: str = None,
        source: str = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.column_name = column_name
        self.create_time = create_time
        self.database_name = database_name
        self.direct_down_column_number = direct_down_column_number
        self.direct_down_table_number = direct_down_table_number
        self.direct_upper_column_number = direct_upper_column_number
        self.direct_upper_table_number = direct_upper_table_number
        self.modified_time = modified_time
        self.source = source
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.direct_down_column_number is not None:
            result['DirectDownColumnNumber'] = self.direct_down_column_number
        if self.direct_down_table_number is not None:
            result['DirectDownTableNumber'] = self.direct_down_table_number
        if self.direct_upper_column_number is not None:
            result['DirectUpperColumnNumber'] = self.direct_upper_column_number
        if self.direct_upper_table_number is not None:
            result['DirectUpperTableNumber'] = self.direct_upper_table_number
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DirectDownColumnNumber') is not None:
            self.direct_down_column_number = m.get('DirectDownColumnNumber')
        if m.get('DirectDownTableNumber') is not None:
            self.direct_down_table_number = m.get('DirectDownTableNumber')
        if m.get('DirectUpperColumnNumber') is not None:
            self.direct_upper_column_number = m.get('DirectUpperColumnNumber')
        if m.get('DirectUpperTableNumber') is not None:
            self.direct_upper_table_number = m.get('DirectUpperTableNumber')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveColumnLineagesResponseBodyData(TeaModel):
    def __init__(
        self,
        downstream_lineages: List[ListHiveColumnLineagesResponseBodyDataDownstreamLineages] = None,
        downstream_number: int = None,
        upstream_lineages: List[ListHiveColumnLineagesResponseBodyDataUpstreamLineages] = None,
        upstream_number: int = None,
    ):
        self.downstream_lineages = downstream_lineages
        self.downstream_number = downstream_number
        self.upstream_lineages = upstream_lineages
        self.upstream_number = upstream_number

    def validate(self):
        if self.downstream_lineages:
            for k in self.downstream_lineages:
                if k:
                    k.validate()
        if self.upstream_lineages:
            for k in self.upstream_lineages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DownstreamLineages'] = []
        if self.downstream_lineages is not None:
            for k in self.downstream_lineages:
                result['DownstreamLineages'].append(k.to_map() if k else None)
        if self.downstream_number is not None:
            result['DownstreamNumber'] = self.downstream_number
        result['UpstreamLineages'] = []
        if self.upstream_lineages is not None:
            for k in self.upstream_lineages:
                result['UpstreamLineages'].append(k.to_map() if k else None)
        if self.upstream_number is not None:
            result['UpstreamNumber'] = self.upstream_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.downstream_lineages = []
        if m.get('DownstreamLineages') is not None:
            for k in m.get('DownstreamLineages'):
                temp_model = ListHiveColumnLineagesResponseBodyDataDownstreamLineages()
                self.downstream_lineages.append(temp_model.from_map(k))
        if m.get('DownstreamNumber') is not None:
            self.downstream_number = m.get('DownstreamNumber')
        self.upstream_lineages = []
        if m.get('UpstreamLineages') is not None:
            for k in m.get('UpstreamLineages'):
                temp_model = ListHiveColumnLineagesResponseBodyDataUpstreamLineages()
                self.upstream_lineages.append(temp_model.from_map(k))
        if m.get('UpstreamNumber') is not None:
            self.upstream_number = m.get('UpstreamNumber')
        return self


class ListHiveColumnLineagesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListHiveColumnLineagesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListHiveColumnLineagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHiveColumnLineagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHiveColumnLineagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHiveColumnLineagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHiveTableLineagesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveTableLineagesResponseBodyDataDownstreamLineages(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: str = None,
        database_name: str = None,
        engine: str = None,
        job_id: str = None,
        modified_time: str = None,
        query_text: str = None,
        source: str = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.database_name = database_name
        self.engine = engine
        self.job_id = job_id
        self.modified_time = modified_time
        self.query_text = query_text
        self.source = source
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveTableLineagesResponseBodyDataUpstreamLineages(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: str = None,
        database_name: str = None,
        engine: str = None,
        job_id: str = None,
        modified_time: str = None,
        query_text: str = None,
        source: str = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.database_name = database_name
        self.engine = engine
        self.job_id = job_id
        self.modified_time = modified_time
        self.query_text = query_text
        self.source = source
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.source is not None:
            result['Source'] = self.source
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListHiveTableLineagesResponseBodyData(TeaModel):
    def __init__(
        self,
        downstream_lineages: List[ListHiveTableLineagesResponseBodyDataDownstreamLineages] = None,
        downstream_number: int = None,
        upstream_lineages: List[ListHiveTableLineagesResponseBodyDataUpstreamLineages] = None,
        upstream_number: int = None,
    ):
        self.downstream_lineages = downstream_lineages
        self.downstream_number = downstream_number
        self.upstream_lineages = upstream_lineages
        self.upstream_number = upstream_number

    def validate(self):
        if self.downstream_lineages:
            for k in self.downstream_lineages:
                if k:
                    k.validate()
        if self.upstream_lineages:
            for k in self.upstream_lineages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DownstreamLineages'] = []
        if self.downstream_lineages is not None:
            for k in self.downstream_lineages:
                result['DownstreamLineages'].append(k.to_map() if k else None)
        if self.downstream_number is not None:
            result['DownstreamNumber'] = self.downstream_number
        result['UpstreamLineages'] = []
        if self.upstream_lineages is not None:
            for k in self.upstream_lineages:
                result['UpstreamLineages'].append(k.to_map() if k else None)
        if self.upstream_number is not None:
            result['UpstreamNumber'] = self.upstream_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.downstream_lineages = []
        if m.get('DownstreamLineages') is not None:
            for k in m.get('DownstreamLineages'):
                temp_model = ListHiveTableLineagesResponseBodyDataDownstreamLineages()
                self.downstream_lineages.append(temp_model.from_map(k))
        if m.get('DownstreamNumber') is not None:
            self.downstream_number = m.get('DownstreamNumber')
        self.upstream_lineages = []
        if m.get('UpstreamLineages') is not None:
            for k in m.get('UpstreamLineages'):
                temp_model = ListHiveTableLineagesResponseBodyDataUpstreamLineages()
                self.upstream_lineages.append(temp_model.from_map(k))
        if m.get('UpstreamNumber') is not None:
            self.upstream_number = m.get('UpstreamNumber')
        return self


class ListHiveTableLineagesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListHiveTableLineagesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListHiveTableLineagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHiveTableLineagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHiveTableLineagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHiveTableLineagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTablePartitionsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        table_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class ListTablePartitionsResponseBodyDataPagedData(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        location: str = None,
        partition_comment: str = None,
        partition_name: str = None,
        partition_path: str = None,
        partition_type: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.location = location
        self.partition_comment = partition_comment
        self.partition_name = partition_name
        self.partition_path = partition_path
        self.partition_type = partition_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.location is not None:
            result['Location'] = self.location
        if self.partition_comment is not None:
            result['PartitionComment'] = self.partition_comment
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        if self.partition_path is not None:
            result['PartitionPath'] = self.partition_path
        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('PartitionComment') is not None:
            self.partition_comment = m.get('PartitionComment')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        if m.get('PartitionPath') is not None:
            self.partition_path = m.get('PartitionPath')
        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')
        return self


class ListTablePartitionsResponseBodyData(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        paged_data: List[ListTablePartitionsResponseBodyDataPagedData] = None,
        total_count: int = None,
    ):
        self.page_size = page_size
        self.paged_data = paged_data
        self.total_count = total_count

    def validate(self):
        if self.paged_data:
            for k in self.paged_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListTablePartitionsResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTablePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListTablePartitionsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListTablePartitionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTablePartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTablePartitionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTablePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDataWorksStandardServiceRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class OpenDataWorksStandardServiceResponseBody(TeaModel):
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


class OpenDataWorksStandardServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenDataWorksStandardServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenDataWorksStandardServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataImportProcessRequest(TeaModel):
    def __init__(
        self,
        sub_uid: str = None,
    ):
        self.sub_uid = sub_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        return self


class QueryDataImportProcessResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDataImportProcessResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryDataImportProcessResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryDataImportProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDataImportProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDataImportProcessResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDataImportProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDataImportProcessStatusRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDataImportProcessStatusResponseBodyDataProjectList(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        project_identifier: str = None,
        project_name: str = None,
    ):
        self.project_id = project_id
        self.project_identifier = project_identifier
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class QueryDataImportProcessStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        project_list: List[QueryDataImportProcessStatusResponseBodyDataProjectList] = None,
        status: str = None,
    ):
        self.message = message
        self.project_list = project_list
        self.status = status

    def validate(self):
        if self.project_list:
            for k in self.project_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        result['ProjectList'] = []
        if self.project_list is not None:
            for k in self.project_list:
                result['ProjectList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.project_list = []
        if m.get('ProjectList') is not None:
            for k in m.get('ProjectList'):
                temp_model = QueryDataImportProcessStatusResponseBodyDataProjectList()
                self.project_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDataImportProcessStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryDataImportProcessStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryDataImportProcessStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDataImportProcessStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDataImportProcessStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDataImportProcessStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRealTimeProcessStatusRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryRealTimeProcessStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        message: str = None,
        project_id: int = None,
        status: str = None,
        task_id: str = None,
        task_url: str = None,
    ):
        self.file_id = file_id
        self.message = message
        self.project_id = project_id
        self.status = status
        self.task_id = task_id
        self.task_url = task_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.message is not None:
            result['Message'] = self.message
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_url is not None:
            result['TaskUrl'] = self.task_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskUrl') is not None:
            self.task_url = m.get('TaskUrl')
        return self


class QueryRealTimeProcessStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryRealTimeProcessStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryRealTimeProcessStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRealTimeProcessStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRealTimeProcessStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRealTimeProcessStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchManualDagNodeInstanceRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        project_name: str = None,
    ):
        self.dag_id = dag_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo(TeaModel):
    def __init__(
        self,
        begin_running_time: str = None,
        begin_wait_res_time: str = None,
        begin_wait_time_time: str = None,
        bizdate: str = None,
        create_time: str = None,
        dag_id: int = None,
        dag_type: int = None,
        finish_time: str = None,
        instance_id: int = None,
        modify_time: str = None,
        node_name: str = None,
        para_value: str = None,
        status: int = None,
    ):
        self.begin_running_time = begin_running_time
        self.begin_wait_res_time = begin_wait_res_time
        self.begin_wait_time_time = begin_wait_time_time
        self.bizdate = bizdate
        self.create_time = create_time
        self.dag_id = dag_id
        self.dag_type = dag_type
        self.finish_time = finish_time
        self.instance_id = instance_id
        self.modify_time = modify_time
        self.node_name = node_name
        self.para_value = para_value
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_running_time is not None:
            result['BeginRunningTime'] = self.begin_running_time
        if self.begin_wait_res_time is not None:
            result['BeginWaitResTime'] = self.begin_wait_res_time
        if self.begin_wait_time_time is not None:
            result['BeginWaitTimeTime'] = self.begin_wait_time_time
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.dag_type is not None:
            result['DagType'] = self.dag_type
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.para_value is not None:
            result['ParaValue'] = self.para_value
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginRunningTime') is not None:
            self.begin_running_time = m.get('BeginRunningTime')
        if m.get('BeginWaitResTime') is not None:
            self.begin_wait_res_time = m.get('BeginWaitResTime')
        if m.get('BeginWaitTimeTime') is not None:
            self.begin_wait_time_time = m.get('BeginWaitTimeTime')
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('DagType') is not None:
            self.dag_type = m.get('DagType')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SearchManualDagNodeInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        node_ins_info: List[SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo] = None,
    ):
        self.node_ins_info = node_ins_info

    def validate(self):
        if self.node_ins_info:
            for k in self.node_ins_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInsInfo'] = []
        if self.node_ins_info is not None:
            for k in self.node_ins_info:
                result['NodeInsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_ins_info = []
        if m.get('NodeInsInfo') is not None:
            for k in m.get('NodeInsInfo'):
                temp_model = SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo()
                self.node_ins_info.append(temp_model.from_map(k))
        return self


class SearchManualDagNodeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: SearchManualDagNodeInstanceResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SearchManualDagNodeInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchManualDagNodeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchManualDagNodeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SearchManualDagNodeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTaskMetaCallbackRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        connection_info: str = None,
        end_time: int = None,
        resources: List[str] = None,
        start_time: int = None,
        sub_type: str = None,
        task_env_param: str = None,
        tenant_id: int = None,
        type: str = None,
        user: str = None,
    ):
        self.code = code
        self.connection_info = connection_info
        self.end_time = end_time
        self.resources = resources
        self.start_time = start_time
        self.sub_type = sub_type
        self.task_env_param = task_env_param
        self.tenant_id = tenant_id
        self.type = type
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.connection_info is not None:
            result['ConnectionInfo'] = self.connection_info
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.task_env_param is not None:
            result['TaskEnvParam'] = self.task_env_param
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConnectionInfo') is not None:
            self.connection_info = m.get('ConnectionInfo')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('TaskEnvParam') is not None:
            self.task_env_param = m.get('TaskEnvParam')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class SendTaskMetaCallbackResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_msg: str = None,
        error_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.err_msg = err_msg
        self.error_code = error_code
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
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendTaskMetaCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendTaskMetaCallbackResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SendTaskMetaCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDISyncInstanceRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        start_param: str = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.start_param = start_param
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.start_param is not None:
            result['StartParam'] = self.start_param
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StartParam') is not None:
            self.start_param = m.get('StartParam')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class StartDISyncInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StartDISyncInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: StartDISyncInstanceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StartDISyncInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartDISyncInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDISyncInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartDISyncInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDISyncInstanceRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class StopDISyncInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class StopDISyncInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: StopDISyncInstanceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = StopDISyncInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopDISyncInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDISyncInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopDISyncInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateDISyncInstanceRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class TerminateDISyncInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class TerminateDISyncInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: TerminateDISyncInstanceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = TerminateDISyncInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TerminateDISyncInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TerminateDISyncInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TerminateDISyncInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerDataLoaderResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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


class TriggerDataLoaderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TriggerDataLoaderResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TriggerDataLoaderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDISyncTaskRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        task_content: str = None,
        task_param: str = None,
        task_type: str = None,
    ):
        self.file_id = file_id
        self.project_id = project_id
        self.task_content = task_content
        self.task_param = task_param
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.task_content is not None:
            result['TaskContent'] = self.task_content
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('TaskContent') is not None:
            self.task_content = m.get('TaskContent')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class UpdateDISyncTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateDISyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateDISyncTaskResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDISyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDISyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDISyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


