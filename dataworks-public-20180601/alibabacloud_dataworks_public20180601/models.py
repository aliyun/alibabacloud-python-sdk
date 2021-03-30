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
        return_code: str = None,
        return_value: bool = None,
        request_id: str = None,
    ):
        self.return_code = return_code
        self.return_value = return_value
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        project_name: str = None,
        flow_name: str = None,
        dag_para: str = None,
        node_para: str = None,
        bizdate: str = None,
    ):
        self.project_name = project_name
        self.flow_name = flow_name
        self.dag_para = dag_para
        self.node_para = node_para
        self.bizdate = bizdate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name
        if self.dag_para is not None:
            result['DagPara'] = self.dag_para
        if self.node_para is not None:
            result['NodePara'] = self.node_para
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')
        if m.get('DagPara') is not None:
            self.dag_para = m.get('DagPara')
        if m.get('NodePara') is not None:
            self.node_para = m.get('NodePara')
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')
        return self


class CreateManualDagResponseBody(TeaModel):
    def __init__(
        self,
        return_error_solution: str = None,
        return_code: str = None,
        request_id: str = None,
        return_message: str = None,
        return_value: int = None,
    ):
        self.return_error_solution = return_error_solution
        self.return_code = return_code
        self.request_id = request_id
        self.return_message = return_message
        self.return_value = return_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_error_solution is not None:
            result['ReturnErrorSolution'] = self.return_error_solution
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.return_message is not None:
            result['ReturnMessage'] = self.return_message
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReturnErrorSolution') is not None:
            self.return_error_solution = m.get('ReturnErrorSolution')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        dataworks_version: str = None,
        create_res_group: bool = None,
        resource_spec: str = None,
        data_source: str = None,
        tables: str = None,
        table_rule: str = None,
        job_config: str = None,
    ):
        self.dataworks_version = dataworks_version
        self.create_res_group = create_res_group
        self.resource_spec = resource_spec
        self.data_source = data_source
        self.tables = tables
        self.table_rule = table_rule
        self.job_config = job_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataworks_version is not None:
            result['DataworksVersion'] = self.dataworks_version
        if self.create_res_group is not None:
            result['CreateResGroup'] = self.create_res_group
        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.table_rule is not None:
            result['TableRule'] = self.table_rule
        if self.job_config is not None:
            result['JobConfig'] = self.job_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataworksVersion') is not None:
            self.dataworks_version = m.get('DataworksVersion')
        if m.get('CreateResGroup') is not None:
            self.create_res_group = m.get('CreateResGroup')
        if m.get('ResourceSpec') is not None:
            self.resource_spec = m.get('ResourceSpec')
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('TableRule') is not None:
            self.table_rule = m.get('TableRule')
        if m.get('JobConfig') is not None:
            self.job_config = m.get('JobConfig')
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
        message: str = None,
        request_id: str = None,
        data: CreateRealTimeProcessResponseBodyData = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateRealTimeProcessResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
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


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        project_identifier: str = None,
        file_id: int = None,
    ):
        self.project_id = project_id
        self.project_identifier = project_identifier
        self.file_id = file_id

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
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        http_status_code: int = None,
        error_code: str = None,
        error_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.error_code = error_code
        self.error_message = error_message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
        column_name: str = None,
        column_comment: str = None,
        comment: str = None,
        column_type: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        column_position: int = None,
    ):
        self.column_name = column_name
        self.column_comment = column_comment
        self.comment = comment
        self.column_type = column_type
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.column_position = column_position

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.column_comment is not None:
            result['ColumnComment'] = self.column_comment
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.column_type is not None:
            result['ColumnType'] = self.column_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.column_position is not None:
            result['ColumnPosition'] = self.column_position
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('ColumnComment') is not None:
            self.column_comment = m.get('ColumnComment')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ColumnPosition') is not None:
            self.column_position = m.get('ColumnPosition')
        return self


class DescribeEmrHiveTableResponseBodyData(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        owner: str = None,
        table_parameters: str = None,
        gmt_modified: str = None,
        table_desc: str = None,
        owner_id: str = None,
        columns: List[DescribeEmrHiveTableResponseBodyDataColumns] = None,
        table_size: int = None,
        database_name: str = None,
        is_temporary: bool = None,
        cluster_biz_name: str = None,
        is_compressed: bool = None,
        serialization_lib: str = None,
        last_access_time: str = None,
        table_comment: str = None,
        last_modify_time: str = None,
        gmt_create: str = None,
        output_format: str = None,
        table_type: str = None,
        owner_type: str = None,
        partition_keys: str = None,
        cluster_biz_id: str = None,
        location: str = None,
        input_format: str = None,
    ):
        self.table_name = table_name
        self.owner = owner
        self.table_parameters = table_parameters
        self.gmt_modified = gmt_modified
        self.table_desc = table_desc
        self.owner_id = owner_id
        self.columns = columns
        self.table_size = table_size
        self.database_name = database_name
        self.is_temporary = is_temporary
        self.cluster_biz_name = cluster_biz_name
        self.is_compressed = is_compressed
        self.serialization_lib = serialization_lib
        self.last_access_time = last_access_time
        self.table_comment = table_comment
        self.last_modify_time = last_modify_time
        self.gmt_create = gmt_create
        self.output_format = output_format
        self.table_type = table_type
        self.owner_type = owner_type
        self.partition_keys = partition_keys
        self.cluster_biz_id = cluster_biz_id
        self.location = location
        self.input_format = input_format

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
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.table_parameters is not None:
            result['TableParameters'] = self.table_parameters
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.table_desc is not None:
            result['TableDesc'] = self.table_desc
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.table_size is not None:
            result['TableSize'] = self.table_size
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_temporary is not None:
            result['IsTemporary'] = self.is_temporary
        if self.cluster_biz_name is not None:
            result['ClusterBizName'] = self.cluster_biz_name
        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.table_comment is not None:
            result['TableComment'] = self.table_comment
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.location is not None:
            result['Location'] = self.location
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TableParameters') is not None:
            self.table_parameters = m.get('TableParameters')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TableDesc') is not None:
            self.table_desc = m.get('TableDesc')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = DescribeEmrHiveTableResponseBodyDataColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsTemporary') is not None:
            self.is_temporary = m.get('IsTemporary')
        if m.get('ClusterBizName') is not None:
            self.cluster_biz_name = m.get('ClusterBizName')
        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('TableComment') is not None:
            self.table_comment = m.get('TableComment')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        return self


class DescribeEmrHiveTableResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeEmrHiveTableResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeEmrHiveTableResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class ListEmrHiveAuditLogsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
        table_name: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.page_number = page_number
        self.page_size = page_size
        self.table_name = table_name
        self.start_time = start_time
        self.end_time = end_time

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
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
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
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ListEmrHiveAuditLogsResponseBodyDataPagedData(TeaModel):
    def __init__(
        self,
        operation: str = None,
        event_time: int = None,
        groups: List[str] = None,
        database: str = None,
        user: str = None,
        table: str = None,
    ):
        self.operation = operation
        self.event_time = event_time
        self.groups = groups
        self.database = database
        self.user = user
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.database is not None:
            result['Database'] = self.database
        if self.user is not None:
            result['User'] = self.user
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class ListEmrHiveAuditLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        paged_data: List[ListEmrHiveAuditLogsResponseBodyDataPagedData] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.paged_data = paged_data
        self.page_number = page_number
        self.page_size = page_size
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
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListEmrHiveAuditLogsResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEmrHiveAuditLogsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListEmrHiveAuditLogsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListEmrHiveAuditLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
        status: str = None,
        type: str = None,
        owner: str = None,
        comment: str = None,
        gmt_modified: int = None,
        owner_id: str = None,
        parameters: str = None,
        region: str = None,
        gmt_create: int = None,
        owner_type: str = None,
        name: str = None,
        location: str = None,
    ):
        self.status = status
        self.type = type
        self.owner = owner
        self.comment = comment
        self.gmt_modified = gmt_modified
        self.owner_id = owner_id
        self.parameters = parameters
        self.region = region
        self.gmt_create = gmt_create
        self.owner_type = owner_type
        self.name = name
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region is not None:
            result['Region'] = self.region
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.name is not None:
            result['Name'] = self.name
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ListEmrHiveDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[ListEmrHiveDatabasesResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListEmrHiveDatabasesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
        table_name: str = None,
        owner: str = None,
        table_parameters: str = None,
        gmt_modified: str = None,
        is_compressed: bool = None,
        table_desc: str = None,
        serialization_lib: str = None,
        owner_id: str = None,
        last_access_time: str = None,
        table_comment: str = None,
        last_modify_time: str = None,
        database_name: str = None,
        is_temporary: bool = None,
        gmt_create: str = None,
        output_format: str = None,
        table_type: str = None,
        owner_type: str = None,
        partition_keys: str = None,
        cluster_biz_id: str = None,
        location: str = None,
        cluster_biz_name: str = None,
        input_format: str = None,
    ):
        self.table_name = table_name
        self.owner = owner
        self.table_parameters = table_parameters
        self.gmt_modified = gmt_modified
        self.is_compressed = is_compressed
        self.table_desc = table_desc
        self.serialization_lib = serialization_lib
        self.owner_id = owner_id
        self.last_access_time = last_access_time
        self.table_comment = table_comment
        self.last_modify_time = last_modify_time
        self.database_name = database_name
        self.is_temporary = is_temporary
        self.gmt_create = gmt_create
        self.output_format = output_format
        self.table_type = table_type
        self.owner_type = owner_type
        self.partition_keys = partition_keys
        self.cluster_biz_id = cluster_biz_id
        self.location = location
        self.cluster_biz_name = cluster_biz_name
        self.input_format = input_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.table_parameters is not None:
            result['TableParameters'] = self.table_parameters
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.is_compressed is not None:
            result['IsCompressed'] = self.is_compressed
        if self.table_desc is not None:
            result['TableDesc'] = self.table_desc
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.table_comment is not None:
            result['TableComment'] = self.table_comment
        if self.last_modify_time is not None:
            result['LastModifyTime'] = self.last_modify_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.is_temporary is not None:
            result['IsTemporary'] = self.is_temporary
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.location is not None:
            result['Location'] = self.location
        if self.cluster_biz_name is not None:
            result['ClusterBizName'] = self.cluster_biz_name
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('TableParameters') is not None:
            self.table_parameters = m.get('TableParameters')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('IsCompressed') is not None:
            self.is_compressed = m.get('IsCompressed')
        if m.get('TableDesc') is not None:
            self.table_desc = m.get('TableDesc')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('TableComment') is not None:
            self.table_comment = m.get('TableComment')
        if m.get('LastModifyTime') is not None:
            self.last_modify_time = m.get('LastModifyTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('IsTemporary') is not None:
            self.is_temporary = m.get('IsTemporary')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('ClusterBizName') is not None:
            self.cluster_biz_name = m.get('ClusterBizName')
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        return self


class ListEmrHiveTablesResponseBodyData(TeaModel):
    def __init__(
        self,
        paged_data: List[ListEmrHiveTablesResponseBodyDataPagedData] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.paged_data = paged_data
        self.page_number = page_number
        self.page_size = page_size
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
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListEmrHiveTablesResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEmrHiveTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListEmrHiveTablesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListEmrHiveTablesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
        database_name: str = None,
        table_name: str = None,
        column_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.table_name = table_name
        self.column_name = column_name

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
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        return self


class ListHiveColumnLineagesResponseBodyDataUpstreamLineages(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        direct_upper_table_number: int = None,
        table_name: str = None,
        modified_time: str = None,
        create_time: str = None,
        direct_down_table_number: int = None,
        database_name: str = None,
        direct_down_column_number: int = None,
        direct_upper_column_number: int = None,
        source: str = None,
        cluster_id: str = None,
    ):
        self.column_name = column_name
        self.direct_upper_table_number = direct_upper_table_number
        self.table_name = table_name
        self.modified_time = modified_time
        self.create_time = create_time
        self.direct_down_table_number = direct_down_table_number
        self.database_name = database_name
        self.direct_down_column_number = direct_down_column_number
        self.direct_upper_column_number = direct_upper_column_number
        self.source = source
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.direct_upper_table_number is not None:
            result['DirectUpperTableNumber'] = self.direct_upper_table_number
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.direct_down_table_number is not None:
            result['DirectDownTableNumber'] = self.direct_down_table_number
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.direct_down_column_number is not None:
            result['DirectDownColumnNumber'] = self.direct_down_column_number
        if self.direct_upper_column_number is not None:
            result['DirectUpperColumnNumber'] = self.direct_upper_column_number
        if self.source is not None:
            result['Source'] = self.source
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DirectUpperTableNumber') is not None:
            self.direct_upper_table_number = m.get('DirectUpperTableNumber')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectDownTableNumber') is not None:
            self.direct_down_table_number = m.get('DirectDownTableNumber')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DirectDownColumnNumber') is not None:
            self.direct_down_column_number = m.get('DirectDownColumnNumber')
        if m.get('DirectUpperColumnNumber') is not None:
            self.direct_upper_column_number = m.get('DirectUpperColumnNumber')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListHiveColumnLineagesResponseBodyDataDownstreamLineages(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        direct_upper_table_number: int = None,
        table_name: str = None,
        modified_time: str = None,
        create_time: str = None,
        direct_down_table_number: int = None,
        database_name: str = None,
        direct_down_column_number: int = None,
        direct_upper_column_number: int = None,
        source: str = None,
        cluster_id: str = None,
    ):
        self.column_name = column_name
        self.direct_upper_table_number = direct_upper_table_number
        self.table_name = table_name
        self.modified_time = modified_time
        self.create_time = create_time
        self.direct_down_table_number = direct_down_table_number
        self.database_name = database_name
        self.direct_down_column_number = direct_down_column_number
        self.direct_upper_column_number = direct_upper_column_number
        self.source = source
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['ColumnName'] = self.column_name
        if self.direct_upper_table_number is not None:
            result['DirectUpperTableNumber'] = self.direct_upper_table_number
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.direct_down_table_number is not None:
            result['DirectDownTableNumber'] = self.direct_down_table_number
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.direct_down_column_number is not None:
            result['DirectDownColumnNumber'] = self.direct_down_column_number
        if self.direct_upper_column_number is not None:
            result['DirectUpperColumnNumber'] = self.direct_upper_column_number
        if self.source is not None:
            result['Source'] = self.source
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')
        if m.get('DirectUpperTableNumber') is not None:
            self.direct_upper_table_number = m.get('DirectUpperTableNumber')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DirectDownTableNumber') is not None:
            self.direct_down_table_number = m.get('DirectDownTableNumber')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DirectDownColumnNumber') is not None:
            self.direct_down_column_number = m.get('DirectDownColumnNumber')
        if m.get('DirectUpperColumnNumber') is not None:
            self.direct_upper_column_number = m.get('DirectUpperColumnNumber')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListHiveColumnLineagesResponseBodyData(TeaModel):
    def __init__(
        self,
        upstream_lineages: List[ListHiveColumnLineagesResponseBodyDataUpstreamLineages] = None,
        downstream_lineages: List[ListHiveColumnLineagesResponseBodyDataDownstreamLineages] = None,
        upstream_number: int = None,
        downstream_number: int = None,
    ):
        self.upstream_lineages = upstream_lineages
        self.downstream_lineages = downstream_lineages
        self.upstream_number = upstream_number
        self.downstream_number = downstream_number

    def validate(self):
        if self.upstream_lineages:
            for k in self.upstream_lineages:
                if k:
                    k.validate()
        if self.downstream_lineages:
            for k in self.downstream_lineages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UpstreamLineages'] = []
        if self.upstream_lineages is not None:
            for k in self.upstream_lineages:
                result['UpstreamLineages'].append(k.to_map() if k else None)
        result['DownstreamLineages'] = []
        if self.downstream_lineages is not None:
            for k in self.downstream_lineages:
                result['DownstreamLineages'].append(k.to_map() if k else None)
        if self.upstream_number is not None:
            result['UpstreamNumber'] = self.upstream_number
        if self.downstream_number is not None:
            result['DownstreamNumber'] = self.downstream_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.upstream_lineages = []
        if m.get('UpstreamLineages') is not None:
            for k in m.get('UpstreamLineages'):
                temp_model = ListHiveColumnLineagesResponseBodyDataUpstreamLineages()
                self.upstream_lineages.append(temp_model.from_map(k))
        self.downstream_lineages = []
        if m.get('DownstreamLineages') is not None:
            for k in m.get('DownstreamLineages'):
                temp_model = ListHiveColumnLineagesResponseBodyDataDownstreamLineages()
                self.downstream_lineages.append(temp_model.from_map(k))
        if m.get('UpstreamNumber') is not None:
            self.upstream_number = m.get('UpstreamNumber')
        if m.get('DownstreamNumber') is not None:
            self.downstream_number = m.get('DownstreamNumber')
        return self


class ListHiveColumnLineagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListHiveColumnLineagesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListHiveColumnLineagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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


class ListHiveTableLineagesResponseBodyDataUpstreamLineages(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        modified_time: str = None,
        query_text: str = None,
        job_id: str = None,
        create_time: str = None,
        database_name: str = None,
        engine: str = None,
        source: str = None,
        cluster_id: str = None,
    ):
        self.table_name = table_name
        self.modified_time = modified_time
        self.query_text = query_text
        self.job_id = job_id
        self.create_time = create_time
        self.database_name = database_name
        self.engine = engine
        self.source = source
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.source is not None:
            result['Source'] = self.source
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListHiveTableLineagesResponseBodyDataDownstreamLineages(TeaModel):
    def __init__(
        self,
        table_name: str = None,
        modified_time: str = None,
        query_text: str = None,
        job_id: str = None,
        create_time: str = None,
        database_name: str = None,
        engine: str = None,
        source: str = None,
        cluster_id: str = None,
    ):
        self.table_name = table_name
        self.modified_time = modified_time
        self.query_text = query_text
        self.job_id = job_id
        self.create_time = create_time
        self.database_name = database_name
        self.engine = engine
        self.source = source
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.query_text is not None:
            result['QueryText'] = self.query_text
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.source is not None:
            result['Source'] = self.source
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListHiveTableLineagesResponseBodyData(TeaModel):
    def __init__(
        self,
        upstream_lineages: List[ListHiveTableLineagesResponseBodyDataUpstreamLineages] = None,
        downstream_lineages: List[ListHiveTableLineagesResponseBodyDataDownstreamLineages] = None,
        upstream_number: int = None,
        downstream_number: int = None,
    ):
        self.upstream_lineages = upstream_lineages
        self.downstream_lineages = downstream_lineages
        self.upstream_number = upstream_number
        self.downstream_number = downstream_number

    def validate(self):
        if self.upstream_lineages:
            for k in self.upstream_lineages:
                if k:
                    k.validate()
        if self.downstream_lineages:
            for k in self.downstream_lineages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UpstreamLineages'] = []
        if self.upstream_lineages is not None:
            for k in self.upstream_lineages:
                result['UpstreamLineages'].append(k.to_map() if k else None)
        result['DownstreamLineages'] = []
        if self.downstream_lineages is not None:
            for k in self.downstream_lineages:
                result['DownstreamLineages'].append(k.to_map() if k else None)
        if self.upstream_number is not None:
            result['UpstreamNumber'] = self.upstream_number
        if self.downstream_number is not None:
            result['DownstreamNumber'] = self.downstream_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.upstream_lineages = []
        if m.get('UpstreamLineages') is not None:
            for k in m.get('UpstreamLineages'):
                temp_model = ListHiveTableLineagesResponseBodyDataUpstreamLineages()
                self.upstream_lineages.append(temp_model.from_map(k))
        self.downstream_lineages = []
        if m.get('DownstreamLineages') is not None:
            for k in m.get('DownstreamLineages'):
                temp_model = ListHiveTableLineagesResponseBodyDataDownstreamLineages()
                self.downstream_lineages.append(temp_model.from_map(k))
        if m.get('UpstreamNumber') is not None:
            self.upstream_number = m.get('UpstreamNumber')
        if m.get('DownstreamNumber') is not None:
            self.downstream_number = m.get('DownstreamNumber')
        return self


class ListHiveTableLineagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListHiveTableLineagesResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListHiveTableLineagesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
        page_number: int = None,
        page_size: int = None,
        table_name: str = None,
        order: str = None,
    ):
        self.cluster_id = cluster_id
        self.database_name = database_name
        self.page_number = page_number
        self.page_size = page_size
        self.table_name = table_name
        self.order = order

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
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.order is not None:
            result['Order'] = self.order
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
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class ListTablePartitionsResponseBodyDataPagedData(TeaModel):
    def __init__(
        self,
        partition_path: str = None,
        partition_comment: str = None,
        partition_name: str = None,
        gmt_create: int = None,
        partition_type: str = None,
        gmt_modified: int = None,
        location: str = None,
    ):
        self.partition_path = partition_path
        self.partition_comment = partition_comment
        self.partition_name = partition_name
        self.gmt_create = gmt_create
        self.partition_type = partition_type
        self.gmt_modified = gmt_modified
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partition_path is not None:
            result['PartitionPath'] = self.partition_path
        if self.partition_comment is not None:
            result['PartitionComment'] = self.partition_comment
        if self.partition_name is not None:
            result['PartitionName'] = self.partition_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.partition_type is not None:
            result['PartitionType'] = self.partition_type
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PartitionPath') is not None:
            self.partition_path = m.get('PartitionPath')
        if m.get('PartitionComment') is not None:
            self.partition_comment = m.get('PartitionComment')
        if m.get('PartitionName') is not None:
            self.partition_name = m.get('PartitionName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('PartitionType') is not None:
            self.partition_type = m.get('PartitionType')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class ListTablePartitionsResponseBodyData(TeaModel):
    def __init__(
        self,
        paged_data: List[ListTablePartitionsResponseBodyDataPagedData] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.paged_data = paged_data
        self.page_size = page_size
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
        result['PagedData'] = []
        if self.paged_data is not None:
            for k in self.paged_data:
                result['PagedData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.paged_data = []
        if m.get('PagedData') is not None:
            for k in m.get('PagedData'):
                temp_model = ListTablePartitionsResponseBodyDataPagedData()
                self.paged_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTablePartitionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListTablePartitionsResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListTablePartitionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
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
        status: str = None,
        message: str = None,
        task_id: str = None,
        task_url: str = None,
    ):
        self.status = status
        self.message = message
        self.task_id = task_id
        self.task_url = task_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_url is not None:
            result['TaskUrl'] = self.task_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskUrl') is not None:
            self.task_url = m.get('TaskUrl')
        return self


class QueryRealTimeProcessStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: QueryRealTimeProcessStatusResponseBodyData = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryRealTimeProcessStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
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
        project_name: str = None,
        dag_id: int = None,
    ):
        self.project_name = project_name
        self.dag_id = dag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        return self


class SearchManualDagNodeInstanceResponseBodyDataNodeInsInfo(TeaModel):
    def __init__(
        self,
        status: int = None,
        begin_running_time: str = None,
        finish_time: str = None,
        create_time: str = None,
        para_value: str = None,
        dag_id: int = None,
        instance_id: int = None,
        begin_wait_res_time: str = None,
        dag_type: int = None,
        bizdate: str = None,
        node_name: str = None,
        begin_wait_time_time: str = None,
        modify_time: str = None,
    ):
        self.status = status
        self.begin_running_time = begin_running_time
        self.finish_time = finish_time
        self.create_time = create_time
        self.para_value = para_value
        self.dag_id = dag_id
        self.instance_id = instance_id
        self.begin_wait_res_time = begin_wait_res_time
        self.dag_type = dag_type
        self.bizdate = bizdate
        self.node_name = node_name
        self.begin_wait_time_time = begin_wait_time_time
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.begin_running_time is not None:
            result['BeginRunningTime'] = self.begin_running_time
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.para_value is not None:
            result['ParaValue'] = self.para_value
        if self.dag_id is not None:
            result['DagId'] = self.dag_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.begin_wait_res_time is not None:
            result['BeginWaitResTime'] = self.begin_wait_res_time
        if self.dag_type is not None:
            result['DagType'] = self.dag_type
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.begin_wait_time_time is not None:
            result['BeginWaitTimeTime'] = self.begin_wait_time_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BeginRunningTime') is not None:
            self.begin_running_time = m.get('BeginRunningTime')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ParaValue') is not None:
            self.para_value = m.get('ParaValue')
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BeginWaitResTime') is not None:
            self.begin_wait_res_time = m.get('BeginWaitResTime')
        if m.get('DagType') is not None:
            self.dag_type = m.get('DagType')
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('BeginWaitTimeTime') is not None:
            self.begin_wait_time_time = m.get('BeginWaitTimeTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
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
        request_id: str = None,
        err_msg: str = None,
        data: SearchManualDagNodeInstanceResponseBodyData = None,
        success: bool = None,
        err_code: str = None,
    ):
        self.request_id = request_id
        self.err_msg = err_msg
        self.data = data
        self.success = success
        self.err_code = err_code

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('Data') is not None:
            temp_model = SearchManualDagNodeInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
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
        tenant_id: int = None,
        type: str = None,
        start_time: int = None,
        end_time: int = None,
        user: str = None,
        code: str = None,
        connection_info: str = None,
        task_env_param: str = None,
        sub_type: str = None,
        resources: List[str] = None,
    ):
        self.tenant_id = tenant_id
        self.type = type
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        self.code = code
        self.connection_info = connection_info
        self.task_env_param = task_env_param
        self.sub_type = sub_type
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.user is not None:
            result['User'] = self.user
        if self.code is not None:
            result['Code'] = self.code
        if self.connection_info is not None:
            result['ConnectionInfo'] = self.connection_info
        if self.task_env_param is not None:
            result['TaskEnvParam'] = self.task_env_param
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConnectionInfo') is not None:
            self.connection_info = m.get('ConnectionInfo')
        if m.get('TaskEnvParam') is not None:
            self.task_env_param = m.get('TaskEnvParam')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class SendTaskMetaCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_msg: str = None,
        data: str = None,
        error_code: int = None,
    ):
        self.request_id = request_id
        self.err_msg = err_msg
        self.data = data
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
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


