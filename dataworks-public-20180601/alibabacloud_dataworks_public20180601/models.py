# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateManualDagRequest(TeaModel):
    def __init__(
        self,
        bizdate: str = None,
        dag_para: str = None,
        flow_name: str = None,
        node_para: str = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.bizdate = bizdate
        self.dag_para = dag_para
        # This parameter is required.
        self.flow_name = flow_name
        self.node_para = node_para
        # This parameter is required.
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
        status_code: int = None,
        body: CreateManualDagResponseBody = None,
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
            temp_model = CreateManualDagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        file_id: int = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # This parameter is required.
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
        status_code: int = None,
        body: DeleteFileResponseBody = None,
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
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
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
        status_code: int = None,
        body: DescribeEmrHiveTableResponseBody = None,
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
            temp_model = DescribeEmrHiveTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataServiceApiAuthMapContextRequest(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_path: str = None,
        project_id: int = None,
        verbose: bool = None,
    ):
        # API ID
        self.api_id = api_id
        self.api_path = api_path
        self.project_id = project_id
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_path is not None:
            result['ApiPath'] = self.api_path
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiPath') is not None:
            self.api_path = m.get('ApiPath')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetDataServiceApiAuthMapContextResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataServiceApiAuthMapContextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataServiceApiAuthMapContextResponseBody = None,
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
            temp_model = GetDataServiceApiAuthMapContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataServiceApiContextRequest(TeaModel):
    def __init__(
        self,
        api_id: int = None,
        api_status: int = None,
        cache_key: str = None,
        for_private_res_group: bool = None,
        verbose: bool = None,
    ):
        # apiId
        # 
        # This parameter is required.
        self.api_id = api_id
        self.api_status = api_status
        self.cache_key = cache_key
        self.for_private_res_group = for_private_res_group
        self.verbose = verbose

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_status is not None:
            result['ApiStatus'] = self.api_status
        if self.cache_key is not None:
            result['CacheKey'] = self.cache_key
        if self.for_private_res_group is not None:
            result['ForPrivateResGroup'] = self.for_private_res_group
        if self.verbose is not None:
            result['Verbose'] = self.verbose
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')
        if m.get('CacheKey') is not None:
            self.cache_key = m.get('CacheKey')
        if m.get('ForPrivateResGroup') is not None:
            self.for_private_res_group = m.get('ForPrivateResGroup')
        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')
        return self


class GetDataServiceApiContextResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataServiceApiContextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataServiceApiContextResponseBody = None,
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
            temp_model = GetDataServiceApiContextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataServiceConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_id: int = None,
        data_source_type: str = None,
    ):
        self.connection_id = connection_id
        self.data_source_type = data_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')
        return self


class GetDataServiceConnectionResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataServiceConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataServiceConnectionResponseBody = None,
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
            temp_model = GetDataServiceConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataServiceContextUpdateEventResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataServiceContextUpdateEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataServiceContextUpdateEventResponseBody = None,
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
            temp_model = GetDataServiceContextUpdateEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataServiceFunctionRequest(TeaModel):
    def __init__(
        self,
        function_id: int = None,
    ):
        self.function_id = function_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_id is not None:
            result['FunctionId'] = self.function_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionId') is not None:
            self.function_id = m.get('FunctionId')
        return self


class GetDataServiceFunctionResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
    ):
        # Id of the request
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataServiceFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataServiceFunctionResponseBody = None,
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
            temp_model = GetDataServiceFunctionResponseBody()
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
        status_code: int = None,
        body: GetSwitchValueResponseBody = None,
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
            temp_model = GetSwitchValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTimeMachineTaskRequest(TeaModel):
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


class GetTimeMachineTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        host_name: str = None,
        id: str = None,
        obj_id: str = None,
        obj_name: str = None,
        oper_type: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.host_name = host_name
        self.id = id
        self.obj_id = obj_id
        self.obj_name = obj_name
        self.oper_type = oper_type
        self.status = status

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
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.obj_id is not None:
            result['ObjId'] = self.obj_id
        if self.obj_name is not None:
            result['ObjName'] = self.obj_name
        if self.oper_type is not None:
            result['OperType'] = self.oper_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ObjId') is not None:
            self.obj_id = m.get('ObjId')
        if m.get('ObjName') is not None:
            self.obj_name = m.get('ObjName')
        if m.get('OperType') is not None:
            self.oper_type = m.get('OperType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTimeMachineTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTimeMachineTaskResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetTimeMachineTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTimeMachineTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTimeMachineTaskResponseBody = None,
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
            temp_model = GetTimeMachineTaskResponseBody()
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
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.database_name = database_name
        self.end_time = end_time
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.start_time = start_time
        # This parameter is required.
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
        status_code: int = None,
        body: ListEmrHiveAuditLogsResponseBody = None,
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
            temp_model = ListEmrHiveAuditLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEmrHiveDatabasesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # This parameter is required.
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
        status_code: int = None,
        body: ListEmrHiveDatabasesResponseBody = None,
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
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.database_name = database_name
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
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
        status_code: int = None,
        body: ListEmrHiveTablesResponseBody = None,
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
            temp_model = ListEmrHiveTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGovernanceIssueDataServiceAPIsRequest(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        owner_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        rule_category: str = None,
        rule_id: str = None,
    ):
        self.biz_date = biz_date
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.rule_category = rule_category
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListGovernanceIssueDataServiceAPIsResponseBodyDataAPIs(TeaModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        biz_date: str = None,
        owner_id: str = None,
        project_id: int = None,
        properties: str = None,
        rule_category: str = None,
        rule_id: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.biz_date = biz_date
        self.owner_id = owner_id
        self.project_id = project_id
        self.properties = properties
        self.rule_category = rule_category
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_id is not None:
            result['ApiId'] = self.api_id
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListGovernanceIssueDataServiceAPIsResponseBodyData(TeaModel):
    def __init__(
        self,
        apis: List[ListGovernanceIssueDataServiceAPIsResponseBodyDataAPIs] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.apis = apis
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.apis:
            for k in self.apis:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['APIs'] = []
        if self.apis is not None:
            for k in self.apis:
                result['APIs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apis = []
        if m.get('APIs') is not None:
            for k in m.get('APIs'):
                temp_model = ListGovernanceIssueDataServiceAPIsResponseBodyDataAPIs()
                self.apis.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGovernanceIssueDataServiceAPIsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListGovernanceIssueDataServiceAPIsResponseBodyData = None,
        dynamic_error_code: str = None,
        dynamic_error_message: str = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.dynamic_error_code = dynamic_error_code
        self.dynamic_error_message = dynamic_error_message
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
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
        if self.dynamic_error_code is not None:
            result['DynamicErrorCode'] = self.dynamic_error_code
        if self.dynamic_error_message is not None:
            result['DynamicErrorMessage'] = self.dynamic_error_message
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
        if m.get('Data') is not None:
            temp_model = ListGovernanceIssueDataServiceAPIsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicErrorCode') is not None:
            self.dynamic_error_code = m.get('DynamicErrorCode')
        if m.get('DynamicErrorMessage') is not None:
            self.dynamic_error_message = m.get('DynamicErrorMessage')
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


class ListGovernanceIssueDataServiceAPIsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGovernanceIssueDataServiceAPIsResponseBody = None,
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
            temp_model = ListGovernanceIssueDataServiceAPIsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGovernanceIssueTablesRequest(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        owner_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        rule_category: str = None,
        rule_id: str = None,
    ):
        self.biz_date = biz_date
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.rule_category = rule_category
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListGovernanceIssueTablesResponseBodyDataTables(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        cluster_id: str = None,
        create_time: int = None,
        database_name: str = None,
        datasource_type: str = None,
        downstream_dependency_count: int = None,
        last_access_time: int = None,
        life_cycle: int = None,
        mc_project_name: str = None,
        owner_id: str = None,
        project_id: int = None,
        properties: str = None,
        rule_category: str = None,
        rule_id: str = None,
        schema: str = None,
        table_guid: str = None,
        table_name: str = None,
        table_size: int = None,
    ):
        self.biz_date = biz_date
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.database_name = database_name
        self.datasource_type = datasource_type
        self.downstream_dependency_count = downstream_dependency_count
        self.last_access_time = last_access_time
        self.life_cycle = life_cycle
        self.mc_project_name = mc_project_name
        self.owner_id = owner_id
        self.project_id = project_id
        self.properties = properties
        self.rule_category = rule_category
        self.rule_id = rule_id
        self.schema = schema
        self.table_guid = table_guid
        self.table_name = table_name
        self.table_size = table_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type
        if self.downstream_dependency_count is not None:
            result['DownstreamDependencyCount'] = self.downstream_dependency_count
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle
        if self.mc_project_name is not None:
            result['McProjectName'] = self.mc_project_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_size is not None:
            result['TableSize'] = self.table_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')
        if m.get('DownstreamDependencyCount') is not None:
            self.downstream_dependency_count = m.get('DownstreamDependencyCount')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('LifeCycle') is not None:
            self.life_cycle = m.get('LifeCycle')
        if m.get('McProjectName') is not None:
            self.mc_project_name = m.get('McProjectName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableSize') is not None:
            self.table_size = m.get('TableSize')
        return self


class ListGovernanceIssueTablesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        tables: List[ListGovernanceIssueTablesResponseBodyDataTables] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.tables = tables
        self.total_count = total_count

    def validate(self):
        if self.tables:
            for k in self.tables:
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
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = ListGovernanceIssueTablesResponseBodyDataTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGovernanceIssueTablesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListGovernanceIssueTablesResponseBodyData = None,
        dynamic_error_code: str = None,
        dynamic_error_message: str = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.dynamic_error_code = dynamic_error_code
        self.dynamic_error_message = dynamic_error_message
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
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
        if self.dynamic_error_code is not None:
            result['DynamicErrorCode'] = self.dynamic_error_code
        if self.dynamic_error_message is not None:
            result['DynamicErrorMessage'] = self.dynamic_error_message
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
        if m.get('Data') is not None:
            temp_model = ListGovernanceIssueTablesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicErrorCode') is not None:
            self.dynamic_error_code = m.get('DynamicErrorCode')
        if m.get('DynamicErrorMessage') is not None:
            self.dynamic_error_message = m.get('DynamicErrorMessage')
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


class ListGovernanceIssueTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGovernanceIssueTablesResponseBody = None,
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
            temp_model = ListGovernanceIssueTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGovernanceIssueTasksRequest(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        owner_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        rule_category: str = None,
        rule_id: str = None,
    ):
        self.biz_date = biz_date
        self.owner_id = owner_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.rule_category = rule_category
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListGovernanceIssueTasksResponseBodyDataTasks(TeaModel):
    def __init__(
        self,
        biz_date: str = None,
        node_id: int = None,
        node_name: str = None,
        node_type: str = None,
        owner_id: str = None,
        project_id: int = None,
        properties: str = None,
        rule_category: str = None,
        rule_id: str = None,
    ):
        self.biz_date = biz_date
        self.node_id = node_id
        self.node_name = node_name
        self.node_type = node_type
        self.owner_id = owner_id
        self.project_id = project_id
        self.properties = properties
        self.rule_category = rule_category
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.rule_category is not None:
            result['RuleCategory'] = self.rule_category
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('RuleCategory') is not None:
            self.rule_category = m.get('RuleCategory')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListGovernanceIssueTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        tasks: List[ListGovernanceIssueTasksResponseBodyDataTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
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
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListGovernanceIssueTasksResponseBodyDataTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGovernanceIssueTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: ListGovernanceIssueTasksResponseBodyData = None,
        dynamic_error_code: str = None,
        dynamic_error_message: str = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.dynamic_error_code = dynamic_error_code
        self.dynamic_error_message = dynamic_error_message
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
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
        if self.dynamic_error_code is not None:
            result['DynamicErrorCode'] = self.dynamic_error_code
        if self.dynamic_error_message is not None:
            result['DynamicErrorMessage'] = self.dynamic_error_message
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
        if m.get('Data') is not None:
            temp_model = ListGovernanceIssueTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicErrorCode') is not None:
            self.dynamic_error_code = m.get('DynamicErrorCode')
        if m.get('DynamicErrorMessage') is not None:
            self.dynamic_error_message = m.get('DynamicErrorMessage')
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


class ListGovernanceIssueTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGovernanceIssueTasksResponseBody = None,
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
            temp_model = ListGovernanceIssueTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGovernanceRulesRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        issue_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.category = category
        self.issue_type = issue_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.issue_type is not None:
            result['IssueType'] = self.issue_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('IssueType') is not None:
            self.issue_type = m.get('IssueType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGovernanceRulesResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        guide: str = None,
        id: str = None,
        issue_type: str = None,
        name: str = None,
        note: str = None,
        rule: str = None,
    ):
        self.category = category
        self.description = description
        self.guide = guide
        self.id = id
        self.issue_type = issue_type
        self.name = name
        self.note = note
        self.rule = rule

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.guide is not None:
            result['Guide'] = self.guide
        if self.id is not None:
            result['Id'] = self.id
        if self.issue_type is not None:
            result['IssueType'] = self.issue_type
        if self.name is not None:
            result['Name'] = self.name
        if self.note is not None:
            result['Note'] = self.note
        if self.rule is not None:
            result['Rule'] = self.rule
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guide') is not None:
            self.guide = m.get('Guide')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IssueType') is not None:
            self.issue_type = m.get('IssueType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        return self


class ListGovernanceRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        rules: List[ListGovernanceRulesResponseBodyDataRules] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.rules = rules
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for k in self.rules:
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
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListGovernanceRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGovernanceRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListGovernanceRulesResponseBodyData = None,
        dynamic_error_code: str = None,
        dynamic_error_message: str = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.dynamic_error_code = dynamic_error_code
        self.dynamic_error_message = dynamic_error_message
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
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
        if self.dynamic_error_code is not None:
            result['DynamicErrorCode'] = self.dynamic_error_code
        if self.dynamic_error_message is not None:
            result['DynamicErrorMessage'] = self.dynamic_error_message
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
        if m.get('Data') is not None:
            temp_model = ListGovernanceRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicErrorCode') is not None:
            self.dynamic_error_code = m.get('DynamicErrorCode')
        if m.get('DynamicErrorMessage') is not None:
            self.dynamic_error_message = m.get('DynamicErrorMessage')
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


class ListGovernanceRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGovernanceRulesResponseBody = None,
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
            temp_model = ListGovernanceRulesResponseBody()
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
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.column_name = column_name
        # This parameter is required.
        self.database_name = database_name
        # This parameter is required.
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
        status_code: int = None,
        body: ListHiveColumnLineagesResponseBody = None,
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
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.database_name = database_name
        # This parameter is required.
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
        status_code: int = None,
        body: ListHiveTableLineagesResponseBody = None,
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
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.database_name = database_name
        self.order = order
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
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
        status_code: int = None,
        body: ListTablePartitionsResponseBody = None,
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
            temp_model = ListTablePartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenDataWorksStandardServiceRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        # This parameter is required.
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
        status_code: int = None,
        body: OpenDataWorksStandardServiceResponseBody = None,
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
            temp_model = OpenDataWorksStandardServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchManualDagNodeInstanceRequest(TeaModel):
    def __init__(
        self,
        dag_id: int = None,
        project_name: str = None,
    ):
        # This parameter is required.
        self.dag_id = dag_id
        # This parameter is required.
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
        status_code: int = None,
        body: SearchManualDagNodeInstanceResponseBody = None,
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
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.connection_info = connection_info
        # This parameter is required.
        self.end_time = end_time
        self.resources = resources
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.sub_type = sub_type
        # This parameter is required.
        self.task_env_param = task_env_param
        # This parameter is required.
        self.tenant_id = tenant_id
        # This parameter is required.
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
        status_code: int = None,
        body: SendTaskMetaCallbackResponseBody = None,
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
            temp_model = SendTaskMetaCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSwitchValueRequest(TeaModel):
    def __init__(
        self,
        switch_name: str = None,
        switch_value: str = None,
    ):
        self.switch_name = switch_name
        self.switch_value = switch_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.switch_name is not None:
            result['SwitchName'] = self.switch_name
        if self.switch_value is not None:
            result['SwitchValue'] = self.switch_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchName') is not None:
            self.switch_name = m.get('SwitchName')
        if m.get('SwitchValue') is not None:
            self.switch_value = m.get('SwitchValue')
        return self


class SetSwitchValueResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class SetSwitchValueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSwitchValueResponseBody = None,
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
            temp_model = SetSwitchValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartCollectQualityRequest(TeaModel):
    def __init__(
        self,
        callback_result_string: str = None,
    ):
        # This parameter is required.
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


class StartCollectQualityResponseBodyReturnValueStrongMethodSet(TeaModel):
    def __init__(
        self,
        col_name: str = None,
        is_col_rule: bool = None,
        is_sql_rule: bool = None,
        is_strong_rule: bool = None,
        method_name: str = None,
        rule_id: int = None,
    ):
        self.col_name = col_name
        self.is_col_rule = is_col_rule
        self.is_sql_rule = is_sql_rule
        self.is_strong_rule = is_strong_rule
        self.method_name = method_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.col_name is not None:
            result['ColName'] = self.col_name
        if self.is_col_rule is not None:
            result['IsColRule'] = self.is_col_rule
        if self.is_sql_rule is not None:
            result['IsSqlRule'] = self.is_sql_rule
        if self.is_strong_rule is not None:
            result['IsStrongRule'] = self.is_strong_rule
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColName') is not None:
            self.col_name = m.get('ColName')
        if m.get('IsColRule') is not None:
            self.is_col_rule = m.get('IsColRule')
        if m.get('IsSqlRule') is not None:
            self.is_sql_rule = m.get('IsSqlRule')
        if m.get('IsStrongRule') is not None:
            self.is_strong_rule = m.get('IsStrongRule')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class StartCollectQualityResponseBodyReturnValueWeakMethodSet(TeaModel):
    def __init__(
        self,
        col_name: str = None,
        is_col_rule: bool = None,
        is_sql_rule: bool = None,
        is_strong_rule: bool = None,
        method_name: str = None,
        rule_id: int = None,
    ):
        self.col_name = col_name
        self.is_col_rule = is_col_rule
        self.is_sql_rule = is_sql_rule
        self.is_strong_rule = is_strong_rule
        self.method_name = method_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.col_name is not None:
            result['ColName'] = self.col_name
        if self.is_col_rule is not None:
            result['IsColRule'] = self.is_col_rule
        if self.is_sql_rule is not None:
            result['IsSqlRule'] = self.is_sql_rule
        if self.is_strong_rule is not None:
            result['IsStrongRule'] = self.is_strong_rule
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColName') is not None:
            self.col_name = m.get('ColName')
        if m.get('IsColRule') is not None:
            self.is_col_rule = m.get('IsColRule')
        if m.get('IsSqlRule') is not None:
            self.is_sql_rule = m.get('IsSqlRule')
        if m.get('IsStrongRule') is not None:
            self.is_strong_rule = m.get('IsStrongRule')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class StartCollectQualityResponseBodyReturnValue(TeaModel):
    def __init__(
        self,
        actual_expression: str = None,
        biz_date: str = None,
        callback_url: str = None,
        connection: str = None,
        entity_id: int = None,
        match_expression: str = None,
        plugin_name: str = None,
        strong_method_set: List[StartCollectQualityResponseBodyReturnValueStrongMethodSet] = None,
        table_guid: str = None,
        task_id: str = None,
        weak_method_set: List[StartCollectQualityResponseBodyReturnValueWeakMethodSet] = None,
    ):
        self.actual_expression = actual_expression
        self.biz_date = biz_date
        self.callback_url = callback_url
        self.connection = connection
        self.entity_id = entity_id
        self.match_expression = match_expression
        self.plugin_name = plugin_name
        self.strong_method_set = strong_method_set
        self.table_guid = table_guid
        self.task_id = task_id
        self.weak_method_set = weak_method_set

    def validate(self):
        if self.strong_method_set:
            for k in self.strong_method_set:
                if k:
                    k.validate()
        if self.weak_method_set:
            for k in self.weak_method_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_expression is not None:
            result['ActualExpression'] = self.actual_expression
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.connection is not None:
            result['Connection'] = self.connection
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.match_expression is not None:
            result['MatchExpression'] = self.match_expression
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        result['StrongMethodSet'] = []
        if self.strong_method_set is not None:
            for k in self.strong_method_set:
                result['StrongMethodSet'].append(k.to_map() if k else None)
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['WeakMethodSet'] = []
        if self.weak_method_set is not None:
            for k in self.weak_method_set:
                result['WeakMethodSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualExpression') is not None:
            self.actual_expression = m.get('ActualExpression')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Connection') is not None:
            self.connection = m.get('Connection')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('MatchExpression') is not None:
            self.match_expression = m.get('MatchExpression')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        self.strong_method_set = []
        if m.get('StrongMethodSet') is not None:
            for k in m.get('StrongMethodSet'):
                temp_model = StartCollectQualityResponseBodyReturnValueStrongMethodSet()
                self.strong_method_set.append(temp_model.from_map(k))
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.weak_method_set = []
        if m.get('WeakMethodSet') is not None:
            for k in m.get('WeakMethodSet'):
                temp_model = StartCollectQualityResponseBodyReturnValueWeakMethodSet()
                self.weak_method_set.append(temp_model.from_map(k))
        return self


class StartCollectQualityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        return_code: str = None,
        return_value: List[StartCollectQualityResponseBodyReturnValue] = None,
    ):
        self.request_id = request_id
        self.return_code = return_code
        self.return_value = return_value

    def validate(self):
        if self.return_value:
            for k in self.return_value:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        result['ReturnValue'] = []
        if self.return_value is not None:
            for k in self.return_value:
                result['ReturnValue'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        self.return_value = []
        if m.get('ReturnValue') is not None:
            for k in m.get('ReturnValue'):
                temp_model = StartCollectQualityResponseBodyReturnValue()
                self.return_value.append(temp_model.from_map(k))
        return self


class StartCollectQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartCollectQualityResponseBody = None,
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
            temp_model = StartCollectQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDoCheckQualityRequest(TeaModel):
    def __init__(
        self,
        callback_result_string: str = None,
    ):
        # This parameter is required.
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


class StartDoCheckQualityResponseBody(TeaModel):
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


class StartDoCheckQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDoCheckQualityResponseBody = None,
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
            temp_model = StartDoCheckQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTaskQualityRequest(TeaModel):
    def __init__(
        self,
        callback_result_string: str = None,
    ):
        # This parameter is required.
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


class StartTaskQualityResponseBodyReturnValueStrongMethodSet(TeaModel):
    def __init__(
        self,
        col_name: str = None,
        is_col_rule: bool = None,
        is_sql_rule: bool = None,
        is_strong_rule: bool = None,
        method_name: str = None,
        rule_id: int = None,
    ):
        self.col_name = col_name
        self.is_col_rule = is_col_rule
        self.is_sql_rule = is_sql_rule
        self.is_strong_rule = is_strong_rule
        self.method_name = method_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.col_name is not None:
            result['ColName'] = self.col_name
        if self.is_col_rule is not None:
            result['IsColRule'] = self.is_col_rule
        if self.is_sql_rule is not None:
            result['IsSqlRule'] = self.is_sql_rule
        if self.is_strong_rule is not None:
            result['IsStrongRule'] = self.is_strong_rule
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColName') is not None:
            self.col_name = m.get('ColName')
        if m.get('IsColRule') is not None:
            self.is_col_rule = m.get('IsColRule')
        if m.get('IsSqlRule') is not None:
            self.is_sql_rule = m.get('IsSqlRule')
        if m.get('IsStrongRule') is not None:
            self.is_strong_rule = m.get('IsStrongRule')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class StartTaskQualityResponseBodyReturnValueWeakMethodSet(TeaModel):
    def __init__(
        self,
        col_name: str = None,
        is_col_rule: bool = None,
        is_sql_rule: bool = None,
        is_strong_rule: bool = None,
        method_name: str = None,
        rule_id: int = None,
    ):
        self.col_name = col_name
        self.is_col_rule = is_col_rule
        self.is_sql_rule = is_sql_rule
        self.is_strong_rule = is_strong_rule
        self.method_name = method_name
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.col_name is not None:
            result['ColName'] = self.col_name
        if self.is_col_rule is not None:
            result['IsColRule'] = self.is_col_rule
        if self.is_sql_rule is not None:
            result['IsSqlRule'] = self.is_sql_rule
        if self.is_strong_rule is not None:
            result['IsStrongRule'] = self.is_strong_rule
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColName') is not None:
            self.col_name = m.get('ColName')
        if m.get('IsColRule') is not None:
            self.is_col_rule = m.get('IsColRule')
        if m.get('IsSqlRule') is not None:
            self.is_sql_rule = m.get('IsSqlRule')
        if m.get('IsStrongRule') is not None:
            self.is_strong_rule = m.get('IsStrongRule')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class StartTaskQualityResponseBodyReturnValue(TeaModel):
    def __init__(
        self,
        actual_expression: str = None,
        biz_date: str = None,
        callback_url: str = None,
        connection: str = None,
        entity_id: int = None,
        match_expression: str = None,
        plugin_name: str = None,
        statistics_flag: int = None,
        strong_method_set: List[StartTaskQualityResponseBodyReturnValueStrongMethodSet] = None,
        table_guid: str = None,
        task_id: str = None,
        trigger_flag: int = None,
        weak_method_set: List[StartTaskQualityResponseBodyReturnValueWeakMethodSet] = None,
    ):
        self.actual_expression = actual_expression
        self.biz_date = biz_date
        self.callback_url = callback_url
        self.connection = connection
        self.entity_id = entity_id
        self.match_expression = match_expression
        self.plugin_name = plugin_name
        self.statistics_flag = statistics_flag
        self.strong_method_set = strong_method_set
        self.table_guid = table_guid
        self.task_id = task_id
        self.trigger_flag = trigger_flag
        self.weak_method_set = weak_method_set

    def validate(self):
        if self.strong_method_set:
            for k in self.strong_method_set:
                if k:
                    k.validate()
        if self.weak_method_set:
            for k in self.weak_method_set:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actual_expression is not None:
            result['ActualExpression'] = self.actual_expression
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.connection is not None:
            result['Connection'] = self.connection
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.match_expression is not None:
            result['MatchExpression'] = self.match_expression
        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name
        if self.statistics_flag is not None:
            result['StatisticsFlag'] = self.statistics_flag
        result['StrongMethodSet'] = []
        if self.strong_method_set is not None:
            for k in self.strong_method_set:
                result['StrongMethodSet'].append(k.to_map() if k else None)
        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trigger_flag is not None:
            result['TriggerFlag'] = self.trigger_flag
        result['WeakMethodSet'] = []
        if self.weak_method_set is not None:
            for k in self.weak_method_set:
                result['WeakMethodSet'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualExpression') is not None:
            self.actual_expression = m.get('ActualExpression')
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Connection') is not None:
            self.connection = m.get('Connection')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('MatchExpression') is not None:
            self.match_expression = m.get('MatchExpression')
        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')
        if m.get('StatisticsFlag') is not None:
            self.statistics_flag = m.get('StatisticsFlag')
        self.strong_method_set = []
        if m.get('StrongMethodSet') is not None:
            for k in m.get('StrongMethodSet'):
                temp_model = StartTaskQualityResponseBodyReturnValueStrongMethodSet()
                self.strong_method_set.append(temp_model.from_map(k))
        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TriggerFlag') is not None:
            self.trigger_flag = m.get('TriggerFlag')
        self.weak_method_set = []
        if m.get('WeakMethodSet') is not None:
            for k in m.get('WeakMethodSet'):
                temp_model = StartTaskQualityResponseBodyReturnValueWeakMethodSet()
                self.weak_method_set.append(temp_model.from_map(k))
        return self


class StartTaskQualityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        return_code: str = None,
        return_value: StartTaskQualityResponseBodyReturnValue = None,
    ):
        self.request_id = request_id
        self.return_code = return_code
        self.return_value = return_value

    def validate(self):
        if self.return_value:
            self.return_value.validate()

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
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnValue') is not None:
            temp_model = StartTaskQualityResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class StartTaskQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartTaskQualityResponseBody = None,
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
            temp_model = StartTaskQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerDataLoaderResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
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


class TriggerDataLoaderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerDataLoaderResponseBody = None,
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
            temp_model = TriggerDataLoaderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerTimeMachineTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        gmt_create: str = None,
        gmt_modified: str = None,
        host_name: str = None,
        id: str = None,
        obj_id: str = None,
        obj_name: str = None,
        oper_type: str = None,
        status: str = None,
    ):
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.host_name = host_name
        self.id = id
        self.obj_id = obj_id
        self.obj_name = obj_name
        self.oper_type = oper_type
        self.status = status

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
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.obj_id is not None:
            result['ObjId'] = self.obj_id
        if self.obj_name is not None:
            result['ObjName'] = self.obj_name
        if self.oper_type is not None:
            result['OperType'] = self.oper_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ObjId') is not None:
            self.obj_id = m.get('ObjId')
        if m.get('ObjName') is not None:
            self.obj_name = m.get('ObjName')
        if m.get('OperType') is not None:
            self.oper_type = m.get('OperType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class TriggerTimeMachineTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: TriggerTimeMachineTaskResponseBodyData = None,
        err_code: str = None,
        err_msg: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_msg = err_msg
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = TriggerTimeMachineTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TriggerTimeMachineTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerTimeMachineTaskResponseBody = None,
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
            temp_model = TriggerTimeMachineTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


