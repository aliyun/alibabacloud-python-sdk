# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddPartitionsRequestPartitionStorageDescriptorCol(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 列注释
        self.comment = comment
        # 列名
        self.name = name
        # 列类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddPartitionsRequestPartitionStorageDescriptorSerDeInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        # SerDe 的名字
        self.name = name
        # SerDe 的
        self.parameters = parameters
        # SerDe 的 serializationLib 信息
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class AddPartitionsRequestPartitionStorageDescriptor(TeaModel):
    def __init__(
        self,
        col: List[AddPartitionsRequestPartitionStorageDescriptorCol] = None,
        input_format: str = None,
        location: str = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        ser_de_info: AddPartitionsRequestPartitionStorageDescriptorSerDeInfo = None,
    ):
        # 表的列信息
        self.col = col
        # 表的 inputFormat
        self.input_format = input_format
        # 表路径
        self.location = location
        # 表的 outputFormat
        self.output_format = output_format
        # StorageDescriptor 的属性
        self.parameters = parameters
        # 表的 serDeInfo
        self.ser_de_info = ser_de_info

    def validate(self):
        if self.col:
            for k in self.col:
                if k:
                    k.validate()
        if self.ser_de_info:
            self.ser_de_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Col'] = []
        if self.col is not None:
            for k in self.col:
                result['Col'].append(k.to_map() if k else None)
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.col = []
        if m.get('Col') is not None:
            for k in m.get('Col'):
                temp_model = AddPartitionsRequestPartitionStorageDescriptorCol()
                self.col.append(temp_model.from_map(k))
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfo') is not None:
            temp_model = AddPartitionsRequestPartitionStorageDescriptorSerDeInfo()
            self.ser_de_info = temp_model.from_map(m['SerDeInfo'])
        return self


class AddPartitionsRequestPartition(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        parameters: Dict[str, str] = None,
        storage_descriptor: AddPartitionsRequestPartitionStorageDescriptor = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 分区属性
        self.parameters = parameters
        # 分区的 StorageDescriptor 
        self.storage_descriptor = storage_descriptor
        # 表名
        self.table_name = table_name
        # 需要添加的分区
        self.values = values

    def validate(self):
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('StorageDescriptor') is not None:
            temp_model = AddPartitionsRequestPartitionStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m['StorageDescriptor'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class AddPartitionsRequest(TeaModel):
    def __init__(
        self,
        partition: List[AddPartitionsRequestPartition] = None,
    ):
        # 添加的分区
        self.partition = partition

    def validate(self):
        if self.partition:
            for k in self.partition:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Partition'] = []
        if self.partition is not None:
            for k in self.partition:
                result['Partition'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.partition = []
        if m.get('Partition') is not None:
            for k in m.get('Partition'):
                temp_model = AddPartitionsRequestPartition()
                self.partition.append(temp_model.from_map(k))
        return self


class AddPartitionsShrinkRequest(TeaModel):
    def __init__(
        self,
        partition_shrink: str = None,
    ):
        # 添加的分区
        self.partition_shrink = partition_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.partition_shrink is not None:
            result['Partition'] = self.partition_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Partition') is not None:
            self.partition_shrink = m.get('Partition')
        return self


class AddPartitionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 成功添加的分区个数
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddPartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddPartitionsResponseBody = None,
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
            temp_model = AddPartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AlterDatabaseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        location_uri: str = None,
        old_db_name: str = None,
        parameters: Dict[str, str] = None,
    ):
        # 修改数据库的新名称
        self.name = name
        # 数据库描述
        self.description = description
        # 数据库的
        self.location_uri = location_uri
        # 修改数据库的旧名称
        self.old_db_name = old_db_name
        # 数据库的
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.old_db_name is not None:
            result['OldDbName'] = self.old_db_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('OldDbName') is not None:
            self.old_db_name = m.get('OldDbName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class AlterDatabaseShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        location_uri: str = None,
        old_db_name: str = None,
        parameters_shrink: str = None,
    ):
        # 修改数据库的新名称
        self.name = name
        # 数据库描述
        self.description = description
        # 数据库的
        self.location_uri = location_uri
        # 修改数据库的旧名称
        self.old_db_name = old_db_name
        # 数据库的
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.old_db_name is not None:
            result['OldDbName'] = self.old_db_name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('OldDbName') is not None:
            self.old_db_name = m.get('OldDbName')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class AlterDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # null
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AlterDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AlterDatabaseResponseBody = None,
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
            temp_model = AlterDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AlterTableRequestCol(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 列注释
        self.comment = comment
        # 列名称
        self.name = name
        # 列类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AlterTableRequest(TeaModel):
    def __init__(
        self,
        old_db_name: str = None,
        old_table_name: str = None,
        new_db_name: str = None,
        new_table_name: str = None,
        parameters: Dict[str, str] = None,
        col: List[AlterTableRequestCol] = None,
    ):
        # 旧数据库名称
        self.old_db_name = old_db_name
        # 旧表名
        self.old_table_name = old_table_name
        # 新的数据库名
        self.new_db_name = new_db_name
        # 新表名
        self.new_table_name = new_table_name
        # 表的新参数
        self.parameters = parameters
        # 表的列信息
        self.col = col

    def validate(self):
        if self.col:
            for k in self.col:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_db_name is not None:
            result['OldDbName'] = self.old_db_name
        if self.old_table_name is not None:
            result['OldTableName'] = self.old_table_name
        if self.new_db_name is not None:
            result['NewDbName'] = self.new_db_name
        if self.new_table_name is not None:
            result['NewTableName'] = self.new_table_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['Col'] = []
        if self.col is not None:
            for k in self.col:
                result['Col'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldDbName') is not None:
            self.old_db_name = m.get('OldDbName')
        if m.get('OldTableName') is not None:
            self.old_table_name = m.get('OldTableName')
        if m.get('NewDbName') is not None:
            self.new_db_name = m.get('NewDbName')
        if m.get('NewTableName') is not None:
            self.new_table_name = m.get('NewTableName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.col = []
        if m.get('Col') is not None:
            for k in m.get('Col'):
                temp_model = AlterTableRequestCol()
                self.col.append(temp_model.from_map(k))
        return self


class AlterTableShrinkRequest(TeaModel):
    def __init__(
        self,
        old_db_name: str = None,
        old_table_name: str = None,
        new_db_name: str = None,
        new_table_name: str = None,
        parameters_shrink: str = None,
        col_shrink: str = None,
    ):
        # 旧数据库名称
        self.old_db_name = old_db_name
        # 旧表名
        self.old_table_name = old_table_name
        # 新的数据库名
        self.new_db_name = new_db_name
        # 新表名
        self.new_table_name = new_table_name
        # 表的新参数
        self.parameters_shrink = parameters_shrink
        # 表的列信息
        self.col_shrink = col_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.old_db_name is not None:
            result['OldDbName'] = self.old_db_name
        if self.old_table_name is not None:
            result['OldTableName'] = self.old_table_name
        if self.new_db_name is not None:
            result['NewDbName'] = self.new_db_name
        if self.new_table_name is not None:
            result['NewTableName'] = self.new_table_name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.col_shrink is not None:
            result['Col'] = self.col_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OldDbName') is not None:
            self.old_db_name = m.get('OldDbName')
        if m.get('OldTableName') is not None:
            self.old_table_name = m.get('OldTableName')
        if m.get('NewDbName') is not None:
            self.new_db_name = m.get('NewDbName')
        if m.get('NewTableName') is not None:
            self.new_table_name = m.get('NewTableName')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('Col') is not None:
            self.col_shrink = m.get('Col')
        return self


class AlterTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 修改表是否成功
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AlterTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AlterTableResponseBody = None,
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
            temp_model = AlterTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDatabaseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        location_uri: str = None,
        parameters: Dict[str, str] = None,
    ):
        # 创建数据库的名字
        self.name = name
        # 数据库描述
        self.description = description
        # 数据库的 location
        self.location_uri = location_uri
        # 数据库属性
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class CreateDatabaseShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        location_uri: str = None,
        parameters_shrink: str = None,
    ):
        # 创建数据库的名字
        self.name = name
        # 数据库描述
        self.description = description
        # 数据库的 location
        self.location_uri = location_uri
        # 数据库属性
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class CreateDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 成功创建库的库ID
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDatabaseResponseBody = None,
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
            temp_model = CreateDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTableRequestPartitionKeys(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 分区字段的注释
        self.comment = comment
        # 分区字段的列名
        self.name = name
        # 分区字段的类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTableRequestStorageDescriptorCols(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 列注释
        self.comment = comment
        # 列名
        self.name = name
        # 列类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTableRequestStorageDescriptorSerDeInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        # SerDe 的名字
        self.name = name
        # SerDe 的属性
        self.parameters = parameters
        # SerDe 的 serializationLib 信息
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class CreateTableRequestStorageDescriptor(TeaModel):
    def __init__(
        self,
        cols: List[CreateTableRequestStorageDescriptorCols] = None,
        input_format: str = None,
        location: str = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        ser_de_info: CreateTableRequestStorageDescriptorSerDeInfo = None,
    ):
        # 表的列信息
        self.cols = cols
        # 表的 inputFormat
        self.input_format = input_format
        # 表路径
        self.location = location
        # 表的 outputFormat
        self.output_format = output_format
        # StorageDescriptor 的属性
        self.parameters = parameters
        # 表的 serDeInfo
        self.ser_de_info = ser_de_info

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()
        if self.ser_de_info:
            self.ser_de_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = CreateTableRequestStorageDescriptorCols()
                self.cols.append(temp_model.from_map(k))
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfo') is not None:
            temp_model = CreateTableRequestStorageDescriptorSerDeInfo()
            self.ser_de_info = temp_model.from_map(m['SerDeInfo'])
        return self


class CreateTableRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
        partition_keys: List[CreateTableRequestPartitionKeys] = None,
        parameters: Dict[str, str] = None,
        storage_descriptor: CreateTableRequestStorageDescriptor = None,
        view_original_text: str = None,
        view_expanded_text: str = None,
        table_type: str = None,
    ):
        # 创建表所在数据库的名称
        self.db_name = db_name
        # 创建表的名称
        self.table_name = table_name
        # 分区字段，可选
        self.partition_keys = partition_keys
        # 表属性
        self.parameters = parameters
        # storageDescriptorModel
        self.storage_descriptor = storage_descriptor
        # 视图的原始 SQL
        self.view_original_text = view_original_text
        # 视图的展开 SQL
        self.view_expanded_text = view_expanded_text
        # 表的类型
        self.table_type = table_type

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = CreateTableRequestPartitionKeys()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('StorageDescriptor') is not None:
            temp_model = CreateTableRequestStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m['StorageDescriptor'])
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class CreateTableShrinkRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
        partition_keys_shrink: str = None,
        parameters_shrink: str = None,
        storage_descriptor_shrink: str = None,
        view_original_text: str = None,
        view_expanded_text: str = None,
        table_type: str = None,
    ):
        # 创建表所在数据库的名称
        self.db_name = db_name
        # 创建表的名称
        self.table_name = table_name
        # 分区字段，可选
        self.partition_keys_shrink = partition_keys_shrink
        # 表属性
        self.parameters_shrink = parameters_shrink
        # storageDescriptorModel
        self.storage_descriptor_shrink = storage_descriptor_shrink
        # 视图的原始 SQL
        self.view_original_text = view_original_text
        # 视图的展开 SQL
        self.view_expanded_text = view_expanded_text
        # 表的类型
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.partition_keys_shrink is not None:
            result['PartitionKeys'] = self.partition_keys_shrink
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.storage_descriptor_shrink is not None:
            result['StorageDescriptor'] = self.storage_descriptor_shrink
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.table_type is not None:
            result['TableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('PartitionKeys') is not None:
            self.partition_keys_shrink = m.get('PartitionKeys')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('StorageDescriptor') is not None:
            self.storage_descriptor_shrink = m.get('StorageDescriptor')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        return self


class CreateTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 创建成功的表 ID
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTableResponseBody = None,
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
            temp_model = CreateTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropDatabaseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        cascade: bool = None,
    ):
        # 需要删除的数据库名称
        self.name = name
        # 如果设置为ture，那么数据库里面有表会先把表删除，再删除数据库；如果设置为false，那么数据库里面有表则不能删除数据库。
        self.cascade = cascade

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.cascade is not None:
            result['Cascade'] = self.cascade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Cascade') is not None:
            self.cascade = m.get('Cascade')
        return self


class DropDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # null
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DropDatabaseResponseBody = None,
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
            temp_model = DropDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropPartitionRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
        part_values: List[str] = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 表名
        self.table_name = table_name
        # 需要删除的分区
        self.part_values = part_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.part_values is not None:
            result['PartValues'] = self.part_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('PartValues') is not None:
            self.part_values = m.get('PartValues')
        return self


class DropPartitionShrinkRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
        part_values_shrink: str = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 表名
        self.table_name = table_name
        # 需要删除的分区
        self.part_values_shrink = part_values_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.part_values_shrink is not None:
            result['PartValues'] = self.part_values_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('PartValues') is not None:
            self.part_values_shrink = m.get('PartValues')
        return self


class DropPartitionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 删除分区是否成功
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropPartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DropPartitionResponseBody = None,
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
            temp_model = DropPartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropTableRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 表名称
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DropTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 标记表是否删除成功
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DropTableResponseBody = None,
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
            temp_model = DropTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 返回的数据库列表
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllDatabasesResponseBody = None,
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
            temp_model = GetAllDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllTablesRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
    ):
        # 数据库名称
        self.db_name = db_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        return self


class GetAllTablesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 请求数据库低下的所有表
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAllTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAllTablesResponseBody = None,
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
            temp_model = GetAllTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabaseRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # 数据库名称
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


class GetDatabaseResponseBodyDatabaseModel(TeaModel):
    def __init__(
        self,
        description: str = None,
        location_uri: str = None,
        name: str = None,
        owner_name: str = None,
        parameters: Dict[str, str] = None,
        tenant_id: str = None,
    ):
        # 数据库描述
        self.description = description
        # 数据库地址
        self.location_uri = location_uri
        # 数据库名称
        self.name = name
        # 数据库所属 DLA userName
        self.owner_name = owner_name
        # 数据库参数
        self.parameters = parameters
        # 数据库所属的阿里云UID
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        database_model: GetDatabaseResponseBodyDatabaseModel = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 返回的数据库结构
        self.database_model = database_model
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
        self.success = success

    def validate(self):
        if self.database_model:
            self.database_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.database_model is not None:
            result['DatabaseModel'] = self.database_model.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatabaseModel') is not None:
            temp_model = GetDatabaseResponseBodyDatabaseModel()
            self.database_model = temp_model.from_map(m['DatabaseModel'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDatabaseResponseBody = None,
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
            temp_model = GetDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPartitionRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 表名
        self.table_name = table_name
        # 分区
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetPartitionShrinkRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
        values_shrink: str = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 表名
        self.table_name = table_name
        # 分区
        self.values_shrink = values_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values_shrink is not None:
            result['Values'] = self.values_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values_shrink = m.get('Values')
        return self


class GetPartitionResponseBodyPartitionModelStorageDescriptorModelCols(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 列注释
        self.comment = comment
        # 列名
        self.name = name
        # 列类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPartitionResponseBodyPartitionModelStorageDescriptorModelSerDeInfoModel(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        # SerDe 的名称
        self.name = name
        # SerDe 的属性
        self.parameters = parameters
        # SerDe 的 serializationLib
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class GetPartitionResponseBodyPartitionModelStorageDescriptorModel(TeaModel):
    def __init__(
        self,
        cols: List[GetPartitionResponseBodyPartitionModelStorageDescriptorModelCols] = None,
        input_format: str = None,
        location: str = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        ser_de_info_model: GetPartitionResponseBodyPartitionModelStorageDescriptorModelSerDeInfoModel = None,
    ):
        # 表的列信息
        self.cols = cols
        # 表的InputFormat
        self.input_format = input_format
        # 表的路径
        self.location = location
        # 表的OutputFormat
        self.output_format = output_format
        # 表的属性
        self.parameters = parameters
        # 表的 SerDe 信息
        self.ser_de_info_model = ser_de_info_model

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()
        if self.ser_de_info_model:
            self.ser_de_info_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info_model is not None:
            result['SerDeInfoModel'] = self.ser_de_info_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = GetPartitionResponseBodyPartitionModelStorageDescriptorModelCols()
                self.cols.append(temp_model.from_map(k))
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfoModel') is not None:
            temp_model = GetPartitionResponseBodyPartitionModelStorageDescriptorModelSerDeInfoModel()
            self.ser_de_info_model = temp_model.from_map(m['SerDeInfoModel'])
        return self


class GetPartitionResponseBodyPartitionModel(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        db_name: str = None,
        parameters: Dict[str, str] = None,
        storage_descriptor_model: GetPartitionResponseBodyPartitionModelStorageDescriptorModel = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        # 分区创建时间
        self.create_time = create_time
        # 数据库名称
        self.db_name = db_name
        # 分区参数
        self.parameters = parameters
        # 分区 SD
        self.storage_descriptor_model = storage_descriptor_model
        # 表名
        self.table_name = table_name
        # 分区信息
        self.values = values

    def validate(self):
        if self.storage_descriptor_model:
            self.storage_descriptor_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.storage_descriptor_model is not None:
            result['StorageDescriptorModel'] = self.storage_descriptor_model.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('StorageDescriptorModel') is not None:
            temp_model = GetPartitionResponseBodyPartitionModelStorageDescriptorModel()
            self.storage_descriptor_model = temp_model.from_map(m['StorageDescriptorModel'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetPartitionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partition_model: GetPartitionResponseBodyPartitionModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 获取到的分区
        self.partition_model = partition_model
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
        self.success = success

    def validate(self):
        if self.partition_model:
            self.partition_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.partition_model is not None:
            result['PartitionModel'] = self.partition_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PartitionModel') is not None:
            temp_model = GetPartitionResponseBodyPartitionModel()
            self.partition_model = temp_model.from_map(m['PartitionModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPartitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPartitionResponseBody = None,
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
            temp_model = GetPartitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPartitionsRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
        max_parts: int = None,
    ):
        # 数据库名
        self.db_name = db_name
        # 表名
        self.table_name = table_name
        # 获取多少分区
        self.max_parts = max_parts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.max_parts is not None:
            result['MaxParts'] = self.max_parts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('MaxParts') is not None:
            self.max_parts = m.get('MaxParts')
        return self


class GetPartitionsResponseBodyPartitionsStorageDescriptorModelCols(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 列注释
        self.comment = comment
        # 列名
        self.name = name
        # 列类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPartitionsResponseBodyPartitionsStorageDescriptorModelSerDeInfoModel(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        # SerDe名称
        self.name = name
        # SerDe属性
        self.parameters = parameters
        # SerDe的serializationLib
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class GetPartitionsResponseBodyPartitionsStorageDescriptorModel(TeaModel):
    def __init__(
        self,
        cols: List[GetPartitionsResponseBodyPartitionsStorageDescriptorModelCols] = None,
        input_format: str = None,
        location: str = None,
        output_format: str = None,
        parameters: Dict[str, str] = None,
        ser_de_info_model: GetPartitionsResponseBodyPartitionsStorageDescriptorModelSerDeInfoModel = None,
    ):
        # 表的列
        self.cols = cols
        # 表的InputFormat
        self.input_format = input_format
        # 表的路径
        self.location = location
        # 表的OutputFormat
        self.output_format = output_format
        # 表属性
        self.parameters = parameters
        # 表的 SerDe 信息
        self.ser_de_info_model = ser_de_info_model

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()
        if self.ser_de_info_model:
            self.ser_de_info_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info_model is not None:
            result['SerDeInfoModel'] = self.ser_de_info_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = GetPartitionsResponseBodyPartitionsStorageDescriptorModelCols()
                self.cols.append(temp_model.from_map(k))
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfoModel') is not None:
            temp_model = GetPartitionsResponseBodyPartitionsStorageDescriptorModelSerDeInfoModel()
            self.ser_de_info_model = temp_model.from_map(m['SerDeInfoModel'])
        return self


class GetPartitionsResponseBodyPartitions(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        db_name: str = None,
        parameters: Dict[str, str] = None,
        storage_descriptor_model: GetPartitionsResponseBodyPartitionsStorageDescriptorModel = None,
        table_name: str = None,
        values: List[str] = None,
    ):
        # 分区创建时间
        self.create_time = create_time
        # 数据库名
        self.db_name = db_name
        # 分区属性
        self.parameters = parameters
        # 分区的 SD 信息
        self.storage_descriptor_model = storage_descriptor_model
        # 表名
        self.table_name = table_name
        # 分区的值
        self.values = values

    def validate(self):
        if self.storage_descriptor_model:
            self.storage_descriptor_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.storage_descriptor_model is not None:
            result['StorageDescriptorModel'] = self.storage_descriptor_model.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('StorageDescriptorModel') is not None:
            temp_model = GetPartitionsResponseBodyPartitionsStorageDescriptorModel()
            self.storage_descriptor_model = temp_model.from_map(m['StorageDescriptorModel'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetPartitionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        partitions: List[GetPartitionsResponseBodyPartitions] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 获取的分区
        self.partitions = partitions
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
        self.success = success

    def validate(self):
        if self.partitions:
            for k in self.partitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Partitions'] = []
        if self.partitions is not None:
            for k in self.partitions:
                result['Partitions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.partitions = []
        if m.get('Partitions') is not None:
            for k in m.get('Partitions'):
                temp_model = GetPartitionsResponseBodyPartitions()
                self.partitions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPartitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPartitionsResponseBody = None,
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
            temp_model = GetPartitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTableRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        table_name: str = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 表名称
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GetTableResponseBodyTablePartitionKeys(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 分区注释
        self.comment = comment
        # 分区名称
        self.name = name
        # 分区类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTableResponseBodyTableStorageDescriptorCols(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        type: str = None,
    ):
        # 列注释
        self.comment = comment
        # 列名称
        self.name = name
        # 列类型
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
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetTableResponseBodyTableStorageDescriptorSerDeInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        serialization_lib: str = None,
    ):
        # SerDe 的名称
        self.name = name
        # SerDe 的属性
        self.parameters = parameters
        # SerDe 的 serializationLib
        self.serialization_lib = serialization_lib

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.serialization_lib is not None:
            result['SerializationLib'] = self.serialization_lib
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerializationLib') is not None:
            self.serialization_lib = m.get('SerializationLib')
        return self


class GetTableResponseBodyTableStorageDescriptor(TeaModel):
    def __init__(
        self,
        cols: List[GetTableResponseBodyTableStorageDescriptorCols] = None,
        input_format: str = None,
        location: str = None,
        output_format: str = None,
        parameters: Dict[str, Any] = None,
        ser_de_info: GetTableResponseBodyTableStorageDescriptorSerDeInfo = None,
    ):
        # 表的列信息
        self.cols = cols
        # 表的 inputFormat
        self.input_format = input_format
        # 表路径
        self.location = location
        # 表的 outputFormat
        self.output_format = output_format
        # SD 的属性
        self.parameters = parameters
        # 表的 SerDe 信息
        self.ser_de_info = ser_de_info

    def validate(self):
        if self.cols:
            for k in self.cols:
                if k:
                    k.validate()
        if self.ser_de_info:
            self.ser_de_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cols'] = []
        if self.cols is not None:
            for k in self.cols:
                result['Cols'].append(k.to_map() if k else None)
        if self.input_format is not None:
            result['InputFormat'] = self.input_format
        if self.location is not None:
            result['Location'] = self.location
        if self.output_format is not None:
            result['OutputFormat'] = self.output_format
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ser_de_info is not None:
            result['SerDeInfo'] = self.ser_de_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cols = []
        if m.get('Cols') is not None:
            for k in m.get('Cols'):
                temp_model = GetTableResponseBodyTableStorageDescriptorCols()
                self.cols.append(temp_model.from_map(k))
        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('SerDeInfo') is not None:
            temp_model = GetTableResponseBodyTableStorageDescriptorSerDeInfo()
            self.ser_de_info = temp_model.from_map(m['SerDeInfo'])
        return self


class GetTableResponseBodyTable(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        db_name: str = None,
        last_access_time: int = None,
        owner: str = None,
        parameters: Dict[str, str] = None,
        partition_keys: List[GetTableResponseBodyTablePartitionKeys] = None,
        storage_descriptor: GetTableResponseBodyTableStorageDescriptor = None,
        table_name: str = None,
        table_type: str = None,
        view_expanded_text: str = None,
        view_original_text: str = None,
    ):
        # 表的创建时间
        self.create_time = create_time
        # 数据库名称
        self.db_name = db_name
        # 最后一次访问时间
        self.last_access_time = last_access_time
        # 表的所属用户
        self.owner = owner
        # 表属性
        self.parameters = parameters
        # 分区信息
        self.partition_keys = partition_keys
        # 表的 sd 信息
        self.storage_descriptor = storage_descriptor
        # 表的名称
        self.table_name = table_name
        # 表的类型
        self.table_type = table_type
        # 如果表是视图，则存储扩展视图SQL
        self.view_expanded_text = view_expanded_text
        # 如果表是视图，则存储原生视图SQL
        self.view_original_text = view_original_text

    def validate(self):
        if self.partition_keys:
            for k in self.partition_keys:
                if k:
                    k.validate()
        if self.storage_descriptor:
            self.storage_descriptor.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.last_access_time is not None:
            result['LastAccessTime'] = self.last_access_time
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        result['PartitionKeys'] = []
        if self.partition_keys is not None:
            for k in self.partition_keys:
                result['PartitionKeys'].append(k.to_map() if k else None)
        if self.storage_descriptor is not None:
            result['StorageDescriptor'] = self.storage_descriptor.to_map()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.table_type is not None:
            result['TableType'] = self.table_type
        if self.view_expanded_text is not None:
            result['ViewExpandedText'] = self.view_expanded_text
        if self.view_original_text is not None:
            result['ViewOriginalText'] = self.view_original_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('LastAccessTime') is not None:
            self.last_access_time = m.get('LastAccessTime')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        self.partition_keys = []
        if m.get('PartitionKeys') is not None:
            for k in m.get('PartitionKeys'):
                temp_model = GetTableResponseBodyTablePartitionKeys()
                self.partition_keys.append(temp_model.from_map(k))
        if m.get('StorageDescriptor') is not None:
            temp_model = GetTableResponseBodyTableStorageDescriptor()
            self.storage_descriptor = temp_model.from_map(m['StorageDescriptor'])
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')
        if m.get('ViewExpandedText') is not None:
            self.view_expanded_text = m.get('ViewExpandedText')
        if m.get('ViewOriginalText') is not None:
            self.view_original_text = m.get('ViewOriginalText')
        return self


class GetTableResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        table: GetTableResponseBodyTable = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
        self.success = success
        # 获取的表信息
        self.table = table

    def validate(self):
        if self.table:
            self.table.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.table is not None:
            result['Table'] = self.table.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Table') is not None:
            temp_model = GetTableResponseBodyTable()
            self.table = temp_model.from_map(m['Table'])
        return self


class GetTableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTableResponseBody = None,
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
            temp_model = GetTableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilegeHiveObjectRef(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        hive_object_type: str = None,
        table_name: str = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 授权粒度
        self.hive_object_type = hive_object_type
        # 表名
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.hive_object_type is not None:
            result['HiveObjectType'] = self.hive_object_type
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('HiveObjectType') is not None:
            self.hive_object_type = m.get('HiveObjectType')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilegePrivilegeGrantInfo(TeaModel):
    def __init__(
        self,
        grant_option: bool = None,
        grantor: str = None,
        principal_type: str = None,
        privilege: str = None,
    ):
        # 权限是否可以传递
        self.grant_option = grant_option
        # 授权者
        self.grantor = grantor
        # 授权者的类型，只能为 USER
        self.principal_type = principal_type
        # 权限
        self.privilege = privilege

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.grantor is not None:
            result['Grantor'] = self.grantor
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.privilege is not None:
            result['Privilege'] = self.privilege
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('Grantor') is not None:
            self.grantor = m.get('Grantor')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')
        return self


class GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilege(TeaModel):
    def __init__(
        self,
        hive_object_ref: GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilegeHiveObjectRef = None,
        principal_name: str = None,
        principal_type: str = None,
        privilege_grant_info: GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilegePrivilegeGrantInfo = None,
    ):
        # HiveObjectRef
        self.hive_object_ref = hive_object_ref
        # 给谁授权
        self.principal_name = principal_name
        # 授权类型，只能为 USER
        self.principal_type = principal_type
        # 授权者的信息
        self.privilege_grant_info = privilege_grant_info

    def validate(self):
        if self.hive_object_ref:
            self.hive_object_ref.validate()
        if self.privilege_grant_info:
            self.privilege_grant_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hive_object_ref is not None:
            result['HiveObjectRef'] = self.hive_object_ref.to_map()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.privilege_grant_info is not None:
            result['PrivilegeGrantInfo'] = self.privilege_grant_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HiveObjectRef') is not None:
            temp_model = GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilegeHiveObjectRef()
            self.hive_object_ref = temp_model.from_map(m['HiveObjectRef'])
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('PrivilegeGrantInfo') is not None:
            temp_model = GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilegePrivilegeGrantInfo()
            self.privilege_grant_info = temp_model.from_map(m['PrivilegeGrantInfo'])
        return self


class GrantPrivilegesRequestPrivilegeBag(TeaModel):
    def __init__(
        self,
        hive_object_privilege: List[GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilege] = None,
    ):
        # 权限信息
        self.hive_object_privilege = hive_object_privilege

    def validate(self):
        if self.hive_object_privilege:
            for k in self.hive_object_privilege:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HiveObjectPrivilege'] = []
        if self.hive_object_privilege is not None:
            for k in self.hive_object_privilege:
                result['HiveObjectPrivilege'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hive_object_privilege = []
        if m.get('HiveObjectPrivilege') is not None:
            for k in m.get('HiveObjectPrivilege'):
                temp_model = GrantPrivilegesRequestPrivilegeBagHiveObjectPrivilege()
                self.hive_object_privilege.append(temp_model.from_map(k))
        return self


class GrantPrivilegesRequest(TeaModel):
    def __init__(
        self,
        privilege_bag: GrantPrivilegesRequestPrivilegeBag = None,
    ):
        # 权限信息
        self.privilege_bag = privilege_bag

    def validate(self):
        if self.privilege_bag:
            self.privilege_bag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privilege_bag is not None:
            result['PrivilegeBag'] = self.privilege_bag.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivilegeBag') is not None:
            temp_model = GrantPrivilegesRequestPrivilegeBag()
            self.privilege_bag = temp_model.from_map(m['PrivilegeBag'])
        return self


class GrantPrivilegesShrinkRequest(TeaModel):
    def __init__(
        self,
        privilege_bag_shrink: str = None,
    ):
        # 权限信息
        self.privilege_bag_shrink = privilege_bag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privilege_bag_shrink is not None:
            result['PrivilegeBag'] = self.privilege_bag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivilegeBag') is not None:
            self.privilege_bag_shrink = m.get('PrivilegeBag')
        return self


class GrantPrivilegesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 授权是否成功
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GrantPrivilegesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GrantPrivilegesResponseBody = None,
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
            temp_model = GrantPrivilegesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilegeHiveObjectRef(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        hive_object_type: str = None,
        table_name: str = None,
    ):
        # 数据库名称
        self.db_name = db_name
        # 授权粒度
        self.hive_object_type = hive_object_type
        # 表名
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.hive_object_type is not None:
            result['HiveObjectType'] = self.hive_object_type
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('HiveObjectType') is not None:
            self.hive_object_type = m.get('HiveObjectType')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilegePrivilegeGrantInfo(TeaModel):
    def __init__(
        self,
        grant_option: bool = None,
        grantor: str = None,
        principal_type: str = None,
        privilege: str = None,
    ):
        # 权限是否可以传递
        self.grant_option = grant_option
        # 授权者
        self.grantor = grantor
        # 授权者的类型，只能为 USER
        self.principal_type = principal_type
        # 权限
        self.privilege = privilege

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grant_option is not None:
            result['GrantOption'] = self.grant_option
        if self.grantor is not None:
            result['Grantor'] = self.grantor
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.privilege is not None:
            result['Privilege'] = self.privilege
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantOption') is not None:
            self.grant_option = m.get('GrantOption')
        if m.get('Grantor') is not None:
            self.grantor = m.get('Grantor')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('Privilege') is not None:
            self.privilege = m.get('Privilege')
        return self


class RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilege(TeaModel):
    def __init__(
        self,
        hive_object_ref: RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilegeHiveObjectRef = None,
        principal_name: str = None,
        principal_type: str = None,
        privilege_grant_info: RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilegePrivilegeGrantInfo = None,
    ):
        # HiveObjectRef
        self.hive_object_ref = hive_object_ref
        # 给谁授权
        self.principal_name = principal_name
        # 授权类型，只能为 USER
        self.principal_type = principal_type
        # 授权者的信息
        self.privilege_grant_info = privilege_grant_info

    def validate(self):
        if self.hive_object_ref:
            self.hive_object_ref.validate()
        if self.privilege_grant_info:
            self.privilege_grant_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hive_object_ref is not None:
            result['HiveObjectRef'] = self.hive_object_ref.to_map()
        if self.principal_name is not None:
            result['PrincipalName'] = self.principal_name
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        if self.privilege_grant_info is not None:
            result['PrivilegeGrantInfo'] = self.privilege_grant_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HiveObjectRef') is not None:
            temp_model = RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilegeHiveObjectRef()
            self.hive_object_ref = temp_model.from_map(m['HiveObjectRef'])
        if m.get('PrincipalName') is not None:
            self.principal_name = m.get('PrincipalName')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        if m.get('PrivilegeGrantInfo') is not None:
            temp_model = RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilegePrivilegeGrantInfo()
            self.privilege_grant_info = temp_model.from_map(m['PrivilegeGrantInfo'])
        return self


class RevokePrivilegesRequestPrivilegeBag(TeaModel):
    def __init__(
        self,
        hive_object_privilege: List[RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilege] = None,
    ):
        # 权限信息
        self.hive_object_privilege = hive_object_privilege

    def validate(self):
        if self.hive_object_privilege:
            for k in self.hive_object_privilege:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HiveObjectPrivilege'] = []
        if self.hive_object_privilege is not None:
            for k in self.hive_object_privilege:
                result['HiveObjectPrivilege'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hive_object_privilege = []
        if m.get('HiveObjectPrivilege') is not None:
            for k in m.get('HiveObjectPrivilege'):
                temp_model = RevokePrivilegesRequestPrivilegeBagHiveObjectPrivilege()
                self.hive_object_privilege.append(temp_model.from_map(k))
        return self


class RevokePrivilegesRequest(TeaModel):
    def __init__(
        self,
        privilege_bag: RevokePrivilegesRequestPrivilegeBag = None,
    ):
        # 权限信息
        self.privilege_bag = privilege_bag

    def validate(self):
        if self.privilege_bag:
            self.privilege_bag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privilege_bag is not None:
            result['PrivilegeBag'] = self.privilege_bag.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivilegeBag') is not None:
            temp_model = RevokePrivilegesRequestPrivilegeBag()
            self.privilege_bag = temp_model.from_map(m['PrivilegeBag'])
        return self


class RevokePrivilegesShrinkRequest(TeaModel):
    def __init__(
        self,
        privilege_bag_shrink: str = None,
    ):
        # 权限信息
        self.privilege_bag_shrink = privilege_bag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.privilege_bag_shrink is not None:
            result['PrivilegeBag'] = self.privilege_bag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivilegeBag') is not None:
            self.privilege_bag_shrink = m.get('PrivilegeBag')
        return self


class RevokePrivilegesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 如果后端处理出现错误，则表示错误的类型
        self.code = code
        # 取消权限是否成功
        self.data = data
        # 如果后端处理出现错误，则表示错误的信息
        self.message = message
        # 请求的 ID
        self.request_id = request_id
        # 标识本次请求是否成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RevokePrivilegesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RevokePrivilegesResponseBody = None,
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
            temp_model = RevokePrivilegesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


