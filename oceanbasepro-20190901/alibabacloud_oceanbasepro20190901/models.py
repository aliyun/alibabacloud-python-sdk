# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateDatabaseRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        collation: str = None,
        database_name: str = None,
        description: str = None,
        encoding: str = None,
        instance_id: str = None,
        tenant_id: str = None,
    ):
        self.client_token = client_token
        self.collation = collation
        self.database_name = database_name
        self.description = description
        self.encoding = encoding
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CreateDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        request_id: str = None,
    ):
        self.database_name = database_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDatabaseResponseBody = None,
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
            temp_model = CreateDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        disk_size: int = None,
        disk_type: str = None,
        instance_class: str = None,
        instance_name: str = None,
        ob_version: str = None,
        period: int = None,
        period_unit: str = None,
        resource_group_id: str = None,
        series: str = None,
        zones: str = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.charge_type = charge_type
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.instance_class = instance_class
        self.instance_name = instance_name
        self.ob_version = ob_version
        self.period = period
        self.period_unit = period_unit
        self.resource_group_id = resource_group_id
        self.series = series
        self.zones = zones

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ob_version is not None:
            result['ObVersion'] = self.ob_version
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.series is not None:
            result['Series'] = self.series
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ObVersion') is not None:
            self.ob_version = m.get('ObVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class CreateInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: str = None,
        resource_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateInstanceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOmsMysqlDataSourceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        dg_database_id: str = None,
        instance_id: str = None,
        ip: str = None,
        name: str = None,
        password: str = None,
        port: str = None,
        schema: str = None,
        type: str = None,
        username: str = None,
        vpc_id: str = None,
    ):
        self.description = description
        self.dg_database_id = dg_database_id
        self.instance_id = instance_id
        self.ip = ip
        self.name = name
        self.password = password
        self.port = port
        self.schema = schema
        self.type = type
        self.username = username
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dg_database_id is not None:
            result['DgDatabaseId'] = self.dg_database_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.name is not None:
            result['Name'] = self.name
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.schema is not None:
            result['Schema'] = self.schema
        if self.type is not None:
            result['Type'] = self.type
        if self.username is not None:
            result['Username'] = self.username
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DgDatabaseId') is not None:
            self.dg_database_id = m.get('DgDatabaseId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Schema') is not None:
            self.schema = m.get('Schema')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateOmsMysqlDataSourceResponseBodyData(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
    ):
        self.endpoint_id = endpoint_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        return self


class CreateOmsMysqlDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateOmsMysqlDataSourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateOmsMysqlDataSourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOmsMysqlDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOmsMysqlDataSourceResponseBody = None,
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
            temp_model = CreateOmsMysqlDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOmsOpenAPIProjectRequestDestConfig(TeaModel):
    def __init__(
        self,
        enable_msg_trace: bool = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        msg_tags: str = None,
        partition: int = None,
        partition_mode: str = None,
        producer_group: str = None,
        send_msg_timeout: int = None,
        sequence_enable: bool = None,
        sequence_start_timestamp: int = None,
        serializer_type: str = None,
        topic_type: str = None,
    ):
        self.enable_msg_trace = enable_msg_trace
        self.endpoint_id = endpoint_id
        self.endpoint_type = endpoint_type
        self.msg_tags = msg_tags
        self.partition = partition
        self.partition_mode = partition_mode
        self.producer_group = producer_group
        self.send_msg_timeout = send_msg_timeout
        self.sequence_enable = sequence_enable
        self.sequence_start_timestamp = sequence_start_timestamp
        self.serializer_type = serializer_type
        self.topic_type = topic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class CreateOmsOpenAPIProjectRequestSourceConfig(TeaModel):
    def __init__(
        self,
        enable_msg_trace: bool = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        msg_tags: str = None,
        partition: int = None,
        partition_mode: str = None,
        producer_group: str = None,
        send_msg_timeout: int = None,
        sequence_enable: bool = None,
        sequence_start_timestamp: int = None,
        serializer_type: str = None,
        topic_type: str = None,
    ):
        self.enable_msg_trace = enable_msg_trace
        self.endpoint_id = endpoint_id
        self.endpoint_type = endpoint_type
        self.msg_tags = msg_tags
        self.partition = partition
        self.partition_mode = partition_mode
        self.producer_group = producer_group
        self.send_msg_timeout = send_msg_timeout
        self.sequence_enable = sequence_enable
        self.sequence_start_timestamp = sequence_start_timestamp
        self.serializer_type = serializer_type
        self.topic_type = topic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTablesAdbTableSchema(TeaModel):
    def __init__(
        self,
        distributed_keys: List[str] = None,
        partition_life_cycle: int = None,
        partition_statement: str = None,
        primary_keys: List[str] = None,
    ):
        self.distributed_keys = distributed_keys
        self.partition_life_cycle = partition_life_cycle
        self.partition_statement = partition_statement
        self.primary_keys = primary_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributed_keys is not None:
            result['DistributedKeys'] = self.distributed_keys
        if self.partition_life_cycle is not None:
            result['PartitionLifeCycle'] = self.partition_life_cycle
        if self.partition_statement is not None:
            result['PartitionStatement'] = self.partition_statement
        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributedKeys') is not None:
            self.distributed_keys = m.get('DistributedKeys')
        if m.get('PartitionLifeCycle') is not None:
            self.partition_life_cycle = m.get('PartitionLifeCycle')
        if m.get('PartitionStatement') is not None:
            self.partition_statement = m.get('PartitionStatement')
        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')
        return self


class CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTables(TeaModel):
    def __init__(
        self,
        adb_table_schema: CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTablesAdbTableSchema = None,
        filter_columns: List[str] = None,
        mapped_name: str = None,
        shard_columns: List[str] = None,
        table_id: str = None,
        table_name: str = None,
        type: str = None,
        where_clause: str = None,
    ):
        self.adb_table_schema = adb_table_schema
        self.filter_columns = filter_columns
        self.mapped_name = mapped_name
        self.shard_columns = shard_columns
        self.table_id = table_id
        self.table_name = table_name
        self.type = type
        self.where_clause = where_clause

    def validate(self):
        if self.adb_table_schema:
            self.adb_table_schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adb_table_schema is not None:
            result['AdbTableSchema'] = self.adb_table_schema.to_map()
        if self.filter_columns is not None:
            result['FilterColumns'] = self.filter_columns
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        if self.shard_columns is not None:
            result['ShardColumns'] = self.shard_columns
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.where_clause is not None:
            result['WhereClause'] = self.where_clause
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdbTableSchema') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTablesAdbTableSchema()
            self.adb_table_schema = temp_model.from_map(m['AdbTableSchema'])
        if m.get('FilterColumns') is not None:
            self.filter_columns = m.get('FilterColumns')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        if m.get('ShardColumns') is not None:
            self.shard_columns = m.get('ShardColumns')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhereClause') is not None:
            self.where_clause = m.get('WhereClause')
        return self


class CreateOmsOpenAPIProjectRequestTransferMappingDatabases(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        database_name: str = None,
        mapped_name: str = None,
        tables: List[CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTables] = None,
        tenant_name: str = None,
        type: str = None,
    ):
        self.database_id = database_id
        self.database_name = database_name
        self.mapped_name = mapped_name
        self.tables = tables
        self.tenant_name = tenant_name
        self.type = type

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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = CreateOmsOpenAPIProjectRequestTransferMappingDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateOmsOpenAPIProjectRequestTransferMapping(TeaModel):
    def __init__(
        self,
        databases: List[CreateOmsOpenAPIProjectRequestTransferMappingDatabases] = None,
        mode: str = None,
    ):
        self.databases = databases
        self.mode = mode

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = CreateOmsOpenAPIProjectRequestTransferMappingDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class CreateOmsOpenAPIProjectRequestTransferStepConfigIncrSyncStepTransferConfig(TeaModel):
    def __init__(
        self,
        record_type_list: List[str] = None,
        start_timestamp: int = None,
        store_log_kept_hour: int = None,
        store_transaction_enabled: bool = None,
        transfer_step_type: str = None,
    ):
        self.record_type_list = record_type_list
        self.start_timestamp = start_timestamp
        self.store_log_kept_hour = store_log_kept_hour
        self.store_transaction_enabled = store_transaction_enabled
        self.transfer_step_type = transfer_step_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_type_list is not None:
            result['RecordTypeList'] = self.record_type_list
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.store_log_kept_hour is not None:
            result['StoreLogKeptHour'] = self.store_log_kept_hour
        if self.store_transaction_enabled is not None:
            result['StoreTransactionEnabled'] = self.store_transaction_enabled
        if self.transfer_step_type is not None:
            result['TransferStepType'] = self.transfer_step_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordTypeList') is not None:
            self.record_type_list = m.get('RecordTypeList')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('StoreLogKeptHour') is not None:
            self.store_log_kept_hour = m.get('StoreLogKeptHour')
        if m.get('StoreTransactionEnabled') is not None:
            self.store_transaction_enabled = m.get('StoreTransactionEnabled')
        if m.get('TransferStepType') is not None:
            self.transfer_step_type = m.get('TransferStepType')
        return self


class CreateOmsOpenAPIProjectRequestTransferStepConfig(TeaModel):
    def __init__(
        self,
        enable_full_sync: bool = None,
        enable_incr_sync: bool = None,
        enable_struct_sync: bool = None,
        incr_sync_step_transfer_config: CreateOmsOpenAPIProjectRequestTransferStepConfigIncrSyncStepTransferConfig = None,
    ):
        self.enable_full_sync = enable_full_sync
        self.enable_incr_sync = enable_incr_sync
        self.enable_struct_sync = enable_struct_sync
        self.incr_sync_step_transfer_config = incr_sync_step_transfer_config

    def validate(self):
        if self.incr_sync_step_transfer_config:
            self.incr_sync_step_transfer_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_full_sync is not None:
            result['EnableFullSync'] = self.enable_full_sync
        if self.enable_incr_sync is not None:
            result['EnableIncrSync'] = self.enable_incr_sync
        if self.enable_struct_sync is not None:
            result['EnableStructSync'] = self.enable_struct_sync
        if self.incr_sync_step_transfer_config is not None:
            result['IncrSyncStepTransferConfig'] = self.incr_sync_step_transfer_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableFullSync') is not None:
            self.enable_full_sync = m.get('EnableFullSync')
        if m.get('EnableIncrSync') is not None:
            self.enable_incr_sync = m.get('EnableIncrSync')
        if m.get('EnableStructSync') is not None:
            self.enable_struct_sync = m.get('EnableStructSync')
        if m.get('IncrSyncStepTransferConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferStepConfigIncrSyncStepTransferConfig()
            self.incr_sync_step_transfer_config = temp_model.from_map(m['IncrSyncStepTransferConfig'])
        return self


class CreateOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        business_name: str = None,
        dest_config: CreateOmsOpenAPIProjectRequestDestConfig = None,
        label_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        project_name: str = None,
        source_config: CreateOmsOpenAPIProjectRequestSourceConfig = None,
        transfer_mapping: CreateOmsOpenAPIProjectRequestTransferMapping = None,
        transfer_step_config: CreateOmsOpenAPIProjectRequestTransferStepConfig = None,
        worker_grade_id: str = None,
    ):
        self.business_name = business_name
        self.dest_config = dest_config
        self.label_ids = label_ids
        self.page_number = page_number
        self.page_size = page_size
        self.project_name = project_name
        self.source_config = source_config
        self.transfer_mapping = transfer_mapping
        self.transfer_step_config = transfer_step_config
        self.worker_grade_id = worker_grade_id

    def validate(self):
        if self.dest_config:
            self.dest_config.validate()
        if self.source_config:
            self.source_config.validate()
        if self.transfer_mapping:
            self.transfer_mapping.validate()
        if self.transfer_step_config:
            self.transfer_step_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config is not None:
            result['DestConfig'] = self.dest_config.to_map()
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config.to_map()
        if self.transfer_mapping is not None:
            result['TransferMapping'] = self.transfer_mapping.to_map()
        if self.transfer_step_config is not None:
            result['TransferStepConfig'] = self.transfer_step_config.to_map()
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestDestConfig()
            self.dest_config = temp_model.from_map(m['DestConfig'])
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestSourceConfig()
            self.source_config = temp_model.from_map(m['SourceConfig'])
        if m.get('TransferMapping') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferMapping()
            self.transfer_mapping = temp_model.from_map(m['TransferMapping'])
        if m.get('TransferStepConfig') is not None:
            temp_model = CreateOmsOpenAPIProjectRequestTransferStepConfig()
            self.transfer_step_config = temp_model.from_map(m['TransferStepConfig'])
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class CreateOmsOpenAPIProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        business_name: str = None,
        dest_config_shrink: str = None,
        label_ids_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        project_name: str = None,
        source_config_shrink: str = None,
        transfer_mapping_shrink: str = None,
        transfer_step_config_shrink: str = None,
        worker_grade_id: str = None,
    ):
        self.business_name = business_name
        self.dest_config_shrink = dest_config_shrink
        self.label_ids_shrink = label_ids_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.project_name = project_name
        self.source_config_shrink = source_config_shrink
        self.transfer_mapping_shrink = transfer_mapping_shrink
        self.transfer_step_config_shrink = transfer_step_config_shrink
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config_shrink is not None:
            result['DestConfig'] = self.dest_config_shrink
        if self.label_ids_shrink is not None:
            result['LabelIds'] = self.label_ids_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.source_config_shrink is not None:
            result['SourceConfig'] = self.source_config_shrink
        if self.transfer_mapping_shrink is not None:
            result['TransferMapping'] = self.transfer_mapping_shrink
        if self.transfer_step_config_shrink is not None:
            result['TransferStepConfig'] = self.transfer_step_config_shrink
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            self.dest_config_shrink = m.get('DestConfig')
        if m.get('LabelIds') is not None:
            self.label_ids_shrink = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SourceConfig') is not None:
            self.source_config_shrink = m.get('SourceConfig')
        if m.get('TransferMapping') is not None:
            self.transfer_mapping_shrink = m.get('TransferMapping')
        if m.get('TransferStepConfig') is not None:
            self.transfer_step_config_shrink = m.get('TransferStepConfig')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class CreateOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class CreateOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: str = None,
        error_detail: CreateOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = CreateOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class CreateOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOmsOpenAPIProjectResponseBody = None,
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
            temp_model = CreateOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityIpGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class CreateSecurityIpGroupResponseBodySecurityIpGroup(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class CreateSecurityIpGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_group: CreateSecurityIpGroupResponseBodySecurityIpGroup = None,
    ):
        self.request_id = request_id
        self.security_ip_group = security_ip_group

    def validate(self):
        if self.security_ip_group:
            self.security_ip_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_group is not None:
            result['SecurityIpGroup'] = self.security_ip_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroup') is not None:
            temp_model = CreateSecurityIpGroupResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class CreateSecurityIpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecurityIpGroupResponseBody = None,
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
            temp_model = CreateSecurityIpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantRequest(TeaModel):
    def __init__(
        self,
        charset: str = None,
        cpu: int = None,
        description: str = None,
        instance_id: str = None,
        memory: int = None,
        primary_zone: str = None,
        tenant_mode: str = None,
        tenant_name: str = None,
        time_zone: str = None,
        unit_num: int = None,
        user_vswitch_id: str = None,
        user_vpc_id: str = None,
    ):
        self.charset = charset
        self.cpu = cpu
        self.description = description
        self.instance_id = instance_id
        self.memory = memory
        self.primary_zone = primary_zone
        self.tenant_mode = tenant_mode
        self.tenant_name = tenant_name
        self.time_zone = time_zone
        self.unit_num = unit_num
        self.user_vswitch_id = user_vswitch_id
        self.user_vpc_id = user_vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        if self.user_vswitch_id is not None:
            result['UserVSwitchId'] = self.user_vswitch_id
        if self.user_vpc_id is not None:
            result['UserVpcId'] = self.user_vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        if m.get('UserVSwitchId') is not None:
            self.user_vswitch_id = m.get('UserVSwitchId')
        if m.get('UserVpcId') is not None:
            self.user_vpc_id = m.get('UserVpcId')
        return self


class CreateTenantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_id: str = None,
    ):
        self.request_id = request_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CreateTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTenantResponseBody = None,
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
            temp_model = CreateTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantReadOnlyConnectionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: str = None,
        zone_id: str = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateTenantReadOnlyConnectionResponseBody(TeaModel):
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


class CreateTenantReadOnlyConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTenantReadOnlyConnectionResponseBody = None,
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
            temp_model = CreateTenantReadOnlyConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantUserRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        roles: str = None,
        tenant_id: str = None,
        user_name: str = None,
        user_password: str = None,
        user_type: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.roles = roles
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.roles is not None:
            result['Roles'] = self.roles
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_password is not None:
            result['UserPassword'] = self.user_password
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Roles') is not None:
            self.roles = m.get('Roles')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CreateTenantUserResponseBodyTenantUserRoles(TeaModel):
    def __init__(
        self,
        database: str = None,
        role: str = None,
    ):
        self.database = database
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class CreateTenantUserResponseBodyTenantUser(TeaModel):
    def __init__(
        self,
        roles: List[CreateTenantUserResponseBodyTenantUserRoles] = None,
        user_name: str = None,
        user_status: str = None,
        user_type: str = None,
    ):
        self.roles = roles
        self.user_name = user_name
        self.user_status = user_status
        self.user_type = user_type

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = CreateTenantUserResponseBodyTenantUserRoles()
                self.roles.append(temp_model.from_map(k))
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CreateTenantUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_user: List[CreateTenantUserResponseBodyTenantUser] = None,
    ):
        self.request_id = request_id
        self.tenant_user = tenant_user

    def validate(self):
        if self.tenant_user:
            for k in self.tenant_user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantUser'] = []
        if self.tenant_user is not None:
            for k in self.tenant_user:
                result['TenantUser'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_user = []
        if m.get('TenantUser') is not None:
            for k in m.get('TenantUser'):
                temp_model = CreateTenantUserResponseBodyTenantUser()
                self.tenant_user.append(temp_model.from_map(k))
        return self


class CreateTenantUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTenantUserResponseBody = None,
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
            temp_model = CreateTenantUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabasesRequest(TeaModel):
    def __init__(
        self,
        database_names: str = None,
        instance_id: str = None,
        tenant_id: str = None,
    ):
        self.database_names = database_names
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DeleteDatabasesResponseBody(TeaModel):
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


class DeleteDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatabasesResponseBody = None,
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
            temp_model = DeleteDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstancesRequest(TeaModel):
    def __init__(
        self,
        backup_retain_mode: str = None,
        instance_ids: str = None,
    ):
        self.backup_retain_mode = backup_retain_mode
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_retain_mode is not None:
            result['BackupRetainMode'] = self.backup_retain_mode
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupRetainMode') is not None:
            self.backup_retain_mode = m.get('BackupRetainMode')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DeleteInstancesResponseBody(TeaModel):
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


class DeleteInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstancesResponseBody = None,
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
            temp_model = DeleteInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class DeleteOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DeleteOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: bool = None,
        error_detail: DeleteOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = DeleteOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DeleteOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteOmsOpenAPIProjectResponseBody = None,
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
            temp_model = DeleteOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityIpGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        return self


class DeleteSecurityIpGroupResponseBodySecurityIpGroup(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        return self


class DeleteSecurityIpGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_group: DeleteSecurityIpGroupResponseBodySecurityIpGroup = None,
    ):
        self.request_id = request_id
        self.security_ip_group = security_ip_group

    def validate(self):
        if self.security_ip_group:
            self.security_ip_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_group is not None:
            result['SecurityIpGroup'] = self.security_ip_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroup') is not None:
            temp_model = DeleteSecurityIpGroupResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class DeleteSecurityIpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecurityIpGroupResponseBody = None,
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
            temp_model = DeleteSecurityIpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTenantUsersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: str = None,
        users: str = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class DeleteTenantUsersResponseBody(TeaModel):
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


class DeleteTenantUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTenantUsersResponseBody = None,
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
            temp_model = DeleteTenantUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTenantsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_ids: str = None,
    ):
        self.instance_id = instance_id
        self.tenant_ids = tenant_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_ids is not None:
            result['TenantIds'] = self.tenant_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantIds') is not None:
            self.tenant_ids = m.get('TenantIds')
        return self


class DeleteTenantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_ids: List[str] = None,
    ):
        self.request_id = request_id
        self.tenant_ids = tenant_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_ids is not None:
            result['TenantIds'] = self.tenant_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantIds') is not None:
            self.tenant_ids = m.get('TenantIds')
        return self


class DeleteTenantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTenantsResponseBody = None,
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
            temp_model = DeleteTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAnomalySQLListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        db_name: str = None,
        end_time: str = None,
        filter_condition: Dict[str, Any] = None,
        node_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        search_key_word: str = None,
        search_parameter: str = None,
        search_rule: str = None,
        search_value: str = None,
        sort_column: str = None,
        sort_order: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.accept_language = accept_language
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition = filter_condition
        self.node_ip = node_ip
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.search_key_word = search_key_word
        self.search_parameter = search_parameter
        self.search_rule = search_rule
        self.search_value = search_value
        self.sort_column = sort_column
        self.sort_order = sort_order
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeAnomalySQLListShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        db_name: str = None,
        end_time: str = None,
        filter_condition_shrink: str = None,
        node_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        search_key_word: str = None,
        search_parameter: str = None,
        search_rule: str = None,
        search_value: str = None,
        sort_column: str = None,
        sort_order: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.accept_language = accept_language
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition_shrink = filter_condition_shrink
        self.node_ip = node_ip
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.search_key_word = search_key_word
        self.search_parameter = search_parameter
        self.search_rule = search_rule
        self.search_value = search_value
        self.sort_column = sort_column
        self.sort_order = sort_order
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition_shrink is not None:
            result['FilterCondition'] = self.filter_condition_shrink
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition_shrink = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeAnomalySQLListResponseBodyAnomalySQLList(TeaModel):
    def __init__(
        self,
        cpu_time: float = None,
        db_name: str = None,
        diagnosis: str = None,
        diagnosis_rule: str = None,
        executions: int = None,
        key: int = None,
        request_time: float = None,
        request_time_utcstring: str = None,
        sqlid: str = None,
        sqltext: str = None,
        suggestion: str = None,
        user_name: str = None,
    ):
        self.cpu_time = cpu_time
        self.db_name = db_name
        self.diagnosis = diagnosis
        self.diagnosis_rule = diagnosis_rule
        self.executions = executions
        self.key = key
        self.request_time = request_time
        self.request_time_utcstring = request_time_utcstring
        self.sqlid = sqlid
        self.sqltext = sqltext
        self.suggestion = suggestion
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.diagnosis is not None:
            result['Diagnosis'] = self.diagnosis
        if self.diagnosis_rule is not None:
            result['DiagnosisRule'] = self.diagnosis_rule
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.key is not None:
            result['Key'] = self.key
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        if self.request_time_utcstring is not None:
            result['RequestTimeUTCString'] = self.request_time_utcstring
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Diagnosis') is not None:
            self.diagnosis = m.get('Diagnosis')
        if m.get('DiagnosisRule') is not None:
            self.diagnosis_rule = m.get('DiagnosisRule')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        if m.get('RequestTimeUTCString') is not None:
            self.request_time_utcstring = m.get('RequestTimeUTCString')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeAnomalySQLListResponseBody(TeaModel):
    def __init__(
        self,
        anomaly_sqllist: List[DescribeAnomalySQLListResponseBodyAnomalySQLList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.anomaly_sqllist = anomaly_sqllist
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.anomaly_sqllist:
            for k in self.anomaly_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnomalySQLList'] = []
        if self.anomaly_sqllist is not None:
            for k in self.anomaly_sqllist:
                result['AnomalySQLList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.anomaly_sqllist = []
        if m.get('AnomalySQLList') is not None:
            for k in m.get('AnomalySQLList'):
                temp_model = DescribeAnomalySQLListResponseBodyAnomalySQLList()
                self.anomaly_sqllist.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAnomalySQLListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAnomalySQLListResponseBody = None,
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
            temp_model = DescribeAnomalySQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableCpuResourceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        modify_type: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.modify_type = modify_type
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeAvailableCpuResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        max_cpu: int = None,
        min_cpu: int = None,
        unit_num: int = None,
    ):
        self.max_cpu = max_cpu
        self.min_cpu = min_cpu
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_cpu is not None:
            result['MaxCpu'] = self.max_cpu
        if self.min_cpu is not None:
            result['MinCpu'] = self.min_cpu
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCpu') is not None:
            self.max_cpu = m.get('MaxCpu')
        if m.get('MinCpu') is not None:
            self.min_cpu = m.get('MinCpu')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class DescribeAvailableCpuResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeAvailableCpuResourceResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeAvailableCpuResourceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableCpuResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableCpuResourceResponseBody = None,
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
            temp_model = DescribeAvailableCpuResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableMemResourceRequest(TeaModel):
    def __init__(
        self,
        cpu_num: int = None,
        instance_id: str = None,
        tenant_id: str = None,
        unit_num: int = None,
    ):
        self.cpu_num = cpu_num
        self.instance_id = instance_id
        self.tenant_id = tenant_id
        self.unit_num = unit_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_num is not None:
            result['CpuNum'] = self.cpu_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuNum') is not None:
            self.cpu_num = m.get('CpuNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class DescribeAvailableMemResourceResponseBodyData(TeaModel):
    def __init__(
        self,
        max_mem: int = None,
        min_mem: int = None,
        used_mem: int = None,
    ):
        self.max_mem = max_mem
        self.min_mem = min_mem
        self.used_mem = used_mem

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_mem is not None:
            result['MaxMem'] = self.max_mem
        if self.min_mem is not None:
            result['MinMem'] = self.min_mem
        if self.used_mem is not None:
            result['UsedMem'] = self.used_mem
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxMem') is not None:
            self.max_mem = m.get('MaxMem')
        if m.get('MinMem') is not None:
            self.min_mem = m.get('MinMem')
        if m.get('UsedMem') is not None:
            self.used_mem = m.get('UsedMem')
        return self


class DescribeAvailableMemResourceResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeAvailableMemResourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeAvailableMemResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAvailableMemResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableMemResourceResponseBody = None,
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
            temp_model = DescribeAvailableMemResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCharsetRequest(TeaModel):
    def __init__(
        self,
        tenant_mode: str = None,
    ):
        self.tenant_mode = tenant_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        return self


class DescribeCharsetResponseBodyCharset(TeaModel):
    def __init__(
        self,
        charset: str = None,
        collations: List[str] = None,
    ):
        self.charset = charset
        self.collations = collations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.collations is not None:
            result['Collations'] = self.collations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('Collations') is not None:
            self.collations = m.get('Collations')
        return self


class DescribeCharsetResponseBody(TeaModel):
    def __init__(
        self,
        charset: List[DescribeCharsetResponseBodyCharset] = None,
        request_id: str = None,
    ):
        self.charset = charset
        self.request_id = request_id

    def validate(self):
        if self.charset:
            for k in self.charset:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Charset'] = []
        if self.charset is not None:
            for k in self.charset:
                result['Charset'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.charset = []
        if m.get('Charset') is not None:
            for k in m.get('Charset'):
                temp_model = DescribeCharsetResponseBodyCharset()
                self.charset.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeCharsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCharsetResponseBody = None,
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
            temp_model = DescribeCharsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDatabasesRequest(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        tenant_id: str = None,
        with_tables: bool = None,
    ):
        self.database_name = database_name
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.tenant_id = tenant_id
        self.with_tables = with_tables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.with_tables is not None:
            result['WithTables'] = self.with_tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('WithTables') is not None:
            self.with_tables = m.get('WithTables')
        return self


class DescribeDatabasesResponseBodyDatabasesTables(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeDatabasesResponseBodyDatabasesUsers(TeaModel):
    def __init__(
        self,
        role: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.role = role
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeDatabasesResponseBodyDatabases(TeaModel):
    def __init__(
        self,
        collation: str = None,
        create_time: str = None,
        data_size: float = None,
        database_name: str = None,
        db_type: str = None,
        description: str = None,
        encoding: str = None,
        required_size: float = None,
        status: str = None,
        tables: List[DescribeDatabasesResponseBodyDatabasesTables] = None,
        tenant_id: str = None,
        users: List[DescribeDatabasesResponseBodyDatabasesUsers] = None,
    ):
        self.collation = collation
        self.create_time = create_time
        self.data_size = data_size
        self.database_name = database_name
        self.db_type = db_type
        self.description = description
        self.encoding = encoding
        self.required_size = required_size
        self.status = status
        self.tables = tables
        self.tenant_id = tenant_id
        self.users = users

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.description is not None:
            result['Description'] = self.description
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.required_size is not None:
            result['RequiredSize'] = self.required_size
        if self.status is not None:
            result['Status'] = self.status
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('RequiredSize') is not None:
            self.required_size = m.get('RequiredSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeDatabasesResponseBodyDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeDatabasesResponseBodyDatabasesUsers()
                self.users.append(temp_model.from_map(k))
        return self


class DescribeDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        databases: List[DescribeDatabasesResponseBodyDatabases] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.databases = databases
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DescribeDatabasesResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDatabasesResponseBody = None,
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
            temp_model = DescribeDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeInstanceResponseBodyInstanceResourceCpu(TeaModel):
    def __init__(
        self,
        total_cpu: int = None,
        unit_cpu: int = None,
        used_cpu: int = None,
    ):
        self.total_cpu = total_cpu
        self.unit_cpu = unit_cpu
        self.used_cpu = used_cpu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeInstanceResponseBodyInstanceResourceDiskSize(TeaModel):
    def __init__(
        self,
        data_used_size: float = None,
        max_disk_used_ob_server: List[str] = None,
        max_disk_used_percent: float = None,
        total_disk_size: int = None,
        unit_disk_size: int = None,
        used_disk_size: int = None,
    ):
        self.data_used_size = data_used_size
        self.max_disk_used_ob_server = max_disk_used_ob_server
        self.max_disk_used_percent = max_disk_used_percent
        self.total_disk_size = total_disk_size
        self.unit_disk_size = unit_disk_size
        self.used_disk_size = used_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_used_size is not None:
            result['DataUsedSize'] = self.data_used_size
        if self.max_disk_used_ob_server is not None:
            result['MaxDiskUsedObServer'] = self.max_disk_used_ob_server
        if self.max_disk_used_percent is not None:
            result['MaxDiskUsedPercent'] = self.max_disk_used_percent
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.unit_disk_size is not None:
            result['UnitDiskSize'] = self.unit_disk_size
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataUsedSize') is not None:
            self.data_used_size = m.get('DataUsedSize')
        if m.get('MaxDiskUsedObServer') is not None:
            self.max_disk_used_ob_server = m.get('MaxDiskUsedObServer')
        if m.get('MaxDiskUsedPercent') is not None:
            self.max_disk_used_percent = m.get('MaxDiskUsedPercent')
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UnitDiskSize') is not None:
            self.unit_disk_size = m.get('UnitDiskSize')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeInstanceResponseBodyInstanceResourceLogDiskSize(TeaModel):
    def __init__(
        self,
        total_disk_size: int = None,
        unit_disk_size: int = None,
    ):
        self.total_disk_size = total_disk_size
        self.unit_disk_size = unit_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.unit_disk_size is not None:
            result['UnitDiskSize'] = self.unit_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UnitDiskSize') is not None:
            self.unit_disk_size = m.get('UnitDiskSize')
        return self


class DescribeInstanceResponseBodyInstanceResourceMemory(TeaModel):
    def __init__(
        self,
        total_memory: int = None,
        unit_memory: int = None,
        used_memory: int = None,
    ):
        self.total_memory = total_memory
        self.unit_memory = unit_memory
        self.used_memory = used_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeInstanceResponseBodyInstanceResource(TeaModel):
    def __init__(
        self,
        cpu: DescribeInstanceResponseBodyInstanceResourceCpu = None,
        disk_size: DescribeInstanceResponseBodyInstanceResourceDiskSize = None,
        log_disk_size: DescribeInstanceResponseBodyInstanceResourceLogDiskSize = None,
        memory: DescribeInstanceResponseBodyInstanceResourceMemory = None,
        unit_count: int = None,
    ):
        self.cpu = cpu
        self.disk_size = disk_size
        self.log_disk_size = log_disk_size
        self.memory = memory
        self.unit_count = unit_count

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.log_disk_size:
            self.log_disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.unit_count is not None:
            result['UnitCount'] = self.unit_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('LogDiskSize') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceLogDiskSize()
            self.log_disk_size = temp_model.from_map(m['LogDiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('UnitCount') is not None:
            self.unit_count = m.get('UnitCount')
        return self


class DescribeInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        auto_renewal: bool = None,
        auto_upgrade_ob_version: bool = None,
        available_zones: List[str] = None,
        create_time: str = None,
        data_merge_time: str = None,
        deploy_mode: str = None,
        deploy_type: str = None,
        disk_type: str = None,
        enable_upgrade_log_disk: bool = None,
        expire_time: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        is_latest_ob_version: bool = None,
        is_trust_ecs: bool = None,
        maintain_time: str = None,
        ob_rpm_version: str = None,
        pay_type: str = None,
        resource: DescribeInstanceResponseBodyInstanceResource = None,
        series: str = None,
        status: str = None,
        version: str = None,
    ):
        self.auto_renewal = auto_renewal
        self.auto_upgrade_ob_version = auto_upgrade_ob_version
        self.available_zones = available_zones
        self.create_time = create_time
        self.data_merge_time = data_merge_time
        self.deploy_mode = deploy_mode
        self.deploy_type = deploy_type
        self.disk_type = disk_type
        self.enable_upgrade_log_disk = enable_upgrade_log_disk
        self.expire_time = expire_time
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.is_latest_ob_version = is_latest_ob_version
        self.is_trust_ecs = is_trust_ecs
        self.maintain_time = maintain_time
        self.ob_rpm_version = ob_rpm_version
        self.pay_type = pay_type
        self.resource = resource
        self.series = series
        self.status = status
        self.version = version

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.auto_upgrade_ob_version is not None:
            result['AutoUpgradeObVersion'] = self.auto_upgrade_ob_version
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_merge_time is not None:
            result['DataMergeTime'] = self.data_merge_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_upgrade_log_disk is not None:
            result['EnableUpgradeLogDisk'] = self.enable_upgrade_log_disk
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_latest_ob_version is not None:
            result['IsLatestObVersion'] = self.is_latest_ob_version
        if self.is_trust_ecs is not None:
            result['IsTrustEcs'] = self.is_trust_ecs
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.ob_rpm_version is not None:
            result['ObRpmVersion'] = self.ob_rpm_version
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.series is not None:
            result['Series'] = self.series
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('AutoUpgradeObVersion') is not None:
            self.auto_upgrade_ob_version = m.get('AutoUpgradeObVersion')
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataMergeTime') is not None:
            self.data_merge_time = m.get('DataMergeTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableUpgradeLogDisk') is not None:
            self.enable_upgrade_log_disk = m.get('EnableUpgradeLogDisk')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsLatestObVersion') is not None:
            self.is_latest_ob_version = m.get('IsLatestObVersion')
        if m.get('IsTrustEcs') is not None:
            self.is_trust_ecs = m.get('IsTrustEcs')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('ObRpmVersion') is not None:
            self.ob_rpm_version = m.get('ObRpmVersion')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Resource') is not None:
            temp_model = DescribeInstanceResponseBodyInstanceResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance: DescribeInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        self.instance = instance
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = DescribeInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceResponseBody = None,
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceCreatableZoneRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceCreatableZoneResponseBodyZoneList(TeaModel):
    def __init__(
        self,
        is_in_cluster: bool = None,
        zone: str = None,
    ):
        self.is_in_cluster = is_in_cluster
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_in_cluster is not None:
            result['IsInCluster'] = self.is_in_cluster
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsInCluster') is not None:
            self.is_in_cluster = m.get('IsInCluster')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeInstanceCreatableZoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zone_list: List[DescribeInstanceCreatableZoneResponseBodyZoneList] = None,
    ):
        self.request_id = request_id
        self.zone_list = zone_list

    def validate(self):
        if self.zone_list:
            for k in self.zone_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ZoneList'] = []
        if self.zone_list is not None:
            for k in self.zone_list:
                result['ZoneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zone_list = []
        if m.get('ZoneList') is not None:
            for k in m.get('ZoneList'):
                temp_model = DescribeInstanceCreatableZoneResponseBodyZoneList()
                self.zone_list.append(temp_model.from_map(k))
        return self


class DescribeInstanceCreatableZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceCreatableZoneResponseBody = None,
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
            temp_model = DescribeInstanceCreatableZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTenantModesRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceTenantModesResponseBody(TeaModel):
    def __init__(
        self,
        instance_modes: List[str] = None,
        request_id: str = None,
    ):
        self.instance_modes = instance_modes
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_modes is not None:
            result['InstanceModes'] = self.instance_modes
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceModes') is not None:
            self.instance_modes = m.get('InstanceModes')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTenantModesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceTenantModesResponseBody = None,
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
            temp_model = DescribeInstanceTenantModesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTopologyRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZonesUnits(TeaModel):
    def __init__(
        self,
        enable_cancel_migrate_unit: bool = None,
        enable_migrate_unit: bool = None,
        manual_migrate: bool = None,
        node_id: str = None,
        unit_cpu: float = None,
        unit_data_size: int = None,
        unit_id: str = None,
        unit_memory: float = None,
        unit_status: str = None,
    ):
        self.enable_cancel_migrate_unit = enable_cancel_migrate_unit
        self.enable_migrate_unit = enable_migrate_unit
        self.manual_migrate = manual_migrate
        self.node_id = node_id
        self.unit_cpu = unit_cpu
        self.unit_data_size = unit_data_size
        self.unit_id = unit_id
        self.unit_memory = unit_memory
        self.unit_status = unit_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_cancel_migrate_unit is not None:
            result['EnableCancelMigrateUnit'] = self.enable_cancel_migrate_unit
        if self.enable_migrate_unit is not None:
            result['EnableMigrateUnit'] = self.enable_migrate_unit
        if self.manual_migrate is not None:
            result['ManualMigrate'] = self.manual_migrate
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.unit_data_size is not None:
            result['UnitDataSize'] = self.unit_data_size
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.unit_status is not None:
            result['UnitStatus'] = self.unit_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableCancelMigrateUnit') is not None:
            self.enable_cancel_migrate_unit = m.get('EnableCancelMigrateUnit')
        if m.get('EnableMigrateUnit') is not None:
            self.enable_migrate_unit = m.get('EnableMigrateUnit')
        if m.get('ManualMigrate') is not None:
            self.manual_migrate = m.get('ManualMigrate')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UnitDataSize') is not None:
            self.unit_data_size = m.get('UnitDataSize')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UnitStatus') is not None:
            self.unit_status = m.get('UnitStatus')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZones(TeaModel):
    def __init__(
        self,
        is_primary_tenant_zone: str = None,
        tenant_zone_id: str = None,
        tenant_zone_role: str = None,
        units: List[DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZonesUnits] = None,
    ):
        self.is_primary_tenant_zone = is_primary_tenant_zone
        self.tenant_zone_id = tenant_zone_id
        self.tenant_zone_role = tenant_zone_role
        self.units = units

    def validate(self):
        if self.units:
            for k in self.units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_primary_tenant_zone is not None:
            result['IsPrimaryTenantZone'] = self.is_primary_tenant_zone
        if self.tenant_zone_id is not None:
            result['TenantZoneId'] = self.tenant_zone_id
        if self.tenant_zone_role is not None:
            result['TenantZoneRole'] = self.tenant_zone_role
        result['Units'] = []
        if self.units is not None:
            for k in self.units:
                result['Units'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPrimaryTenantZone') is not None:
            self.is_primary_tenant_zone = m.get('IsPrimaryTenantZone')
        if m.get('TenantZoneId') is not None:
            self.tenant_zone_id = m.get('TenantZoneId')
        if m.get('TenantZoneRole') is not None:
            self.tenant_zone_role = m.get('TenantZoneRole')
        self.units = []
        if m.get('Units') is not None:
            for k in m.get('Units'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZonesUnits()
                self.units.append(temp_model.from_map(k))
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyTenants(TeaModel):
    def __init__(
        self,
        primary_zone_deploy_type: str = None,
        tenant_cpu: float = None,
        tenant_deploy_type: str = None,
        tenant_id: str = None,
        tenant_memory: float = None,
        tenant_mode: str = None,
        tenant_name: str = None,
        tenant_status: str = None,
        tenant_unit_num: int = None,
        tenant_zones: List[DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZones] = None,
    ):
        self.primary_zone_deploy_type = primary_zone_deploy_type
        self.tenant_cpu = tenant_cpu
        self.tenant_deploy_type = tenant_deploy_type
        self.tenant_id = tenant_id
        self.tenant_memory = tenant_memory
        self.tenant_mode = tenant_mode
        self.tenant_name = tenant_name
        self.tenant_status = tenant_status
        self.tenant_unit_num = tenant_unit_num
        self.tenant_zones = tenant_zones

    def validate(self):
        if self.tenant_zones:
            for k in self.tenant_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.primary_zone_deploy_type is not None:
            result['PrimaryZoneDeployType'] = self.primary_zone_deploy_type
        if self.tenant_cpu is not None:
            result['TenantCpu'] = self.tenant_cpu
        if self.tenant_deploy_type is not None:
            result['TenantDeployType'] = self.tenant_deploy_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_memory is not None:
            result['TenantMemory'] = self.tenant_memory
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.tenant_status is not None:
            result['TenantStatus'] = self.tenant_status
        if self.tenant_unit_num is not None:
            result['TenantUnitNum'] = self.tenant_unit_num
        result['TenantZones'] = []
        if self.tenant_zones is not None:
            for k in self.tenant_zones:
                result['TenantZones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrimaryZoneDeployType') is not None:
            self.primary_zone_deploy_type = m.get('PrimaryZoneDeployType')
        if m.get('TenantCpu') is not None:
            self.tenant_cpu = m.get('TenantCpu')
        if m.get('TenantDeployType') is not None:
            self.tenant_deploy_type = m.get('TenantDeployType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantMemory') is not None:
            self.tenant_memory = m.get('TenantMemory')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TenantStatus') is not None:
            self.tenant_status = m.get('TenantStatus')
        if m.get('TenantUnitNum') is not None:
            self.tenant_unit_num = m.get('TenantUnitNum')
        self.tenant_zones = []
        if m.get('TenantZones') is not None:
            for k in m.get('TenantZones'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyTenantsTenantZones()
                self.tenant_zones.append(temp_model.from_map(k))
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceCpu(TeaModel):
    def __init__(
        self,
        total_cpu: int = None,
        used_cpu: float = None,
    ):
        self.total_cpu = total_cpu
        self.used_cpu = used_cpu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceDiskSize(TeaModel):
    def __init__(
        self,
        total_disk_size: float = None,
        used_disk_size: float = None,
    ):
        self.total_disk_size = total_disk_size
        self.used_disk_size = used_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceMemory(TeaModel):
    def __init__(
        self,
        total_memory: int = None,
        used_memory: float = None,
    ):
        self.total_memory = total_memory
        self.used_memory = used_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResource(TeaModel):
    def __init__(
        self,
        cpu: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceCpu = None,
        disk_size: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceDiskSize = None,
        memory: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceMemory = None,
    ):
        self.cpu = cpu
        self.disk_size = disk_size
        self.memory = memory

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodes(TeaModel):
    def __init__(
        self,
        node_copy_id: int = None,
        node_id: str = None,
        node_resource: List[DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResource] = None,
        node_status: str = None,
    ):
        self.node_copy_id = node_copy_id
        self.node_id = node_id
        self.node_resource = node_resource
        self.node_status = node_status

    def validate(self):
        if self.node_resource:
            for k in self.node_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_copy_id is not None:
            result['NodeCopyId'] = self.node_copy_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        result['NodeResource'] = []
        if self.node_resource is not None:
            for k in self.node_resource:
                result['NodeResource'].append(k.to_map() if k else None)
        if self.node_status is not None:
            result['NodeStatus'] = self.node_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCopyId') is not None:
            self.node_copy_id = m.get('NodeCopyId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        self.node_resource = []
        if m.get('NodeResource') is not None:
            for k in m.get('NodeResource'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodesNodeResource()
                self.node_resource.append(temp_model.from_map(k))
        if m.get('NodeStatus') is not None:
            self.node_status = m.get('NodeStatus')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResourceDiskSize(TeaModel):
    def __init__(
        self,
        max_disk_used_ob_server: List[str] = None,
        max_disk_used_percent: float = None,
    ):
        self.max_disk_used_ob_server = max_disk_used_ob_server
        self.max_disk_used_percent = max_disk_used_percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_disk_used_ob_server is not None:
            result['MaxDiskUsedObServer'] = self.max_disk_used_ob_server
        if self.max_disk_used_percent is not None:
            result['MaxDiskUsedPercent'] = self.max_disk_used_percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxDiskUsedObServer') is not None:
            self.max_disk_used_ob_server = m.get('MaxDiskUsedObServer')
        if m.get('MaxDiskUsedPercent') is not None:
            self.max_disk_used_percent = m.get('MaxDiskUsedPercent')
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResource(TeaModel):
    def __init__(
        self,
        disk_size: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResourceDiskSize = None,
    ):
        self.disk_size = disk_size

    def validate(self):
        if self.disk_size:
            self.disk_size.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopologyZones(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodes] = None,
        region: str = None,
        zone_disk: str = None,
        zone_id: str = None,
        zone_resource: DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResource = None,
    ):
        self.nodes = nodes
        self.region = region
        self.zone_disk = zone_disk
        self.zone_id = zone_id
        self.zone_resource = zone_resource

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.zone_resource:
            self.zone_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        if self.zone_disk is not None:
            result['ZoneDisk'] = self.zone_disk
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_resource is not None:
            result['ZoneResource'] = self.zone_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ZoneDisk') is not None:
            self.zone_disk = m.get('ZoneDisk')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneResource') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZonesZoneResource()
            self.zone_resource = temp_model.from_map(m['ZoneResource'])
        return self


class DescribeInstanceTopologyResponseBodyInstanceTopology(TeaModel):
    def __init__(
        self,
        tenants: List[DescribeInstanceTopologyResponseBodyInstanceTopologyTenants] = None,
        zones: List[DescribeInstanceTopologyResponseBodyInstanceTopologyZones] = None,
    ):
        self.tenants = tenants
        self.zones = zones

    def validate(self):
        if self.tenants:
            for k in self.tenants:
                if k:
                    k.validate()
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Tenants'] = []
        if self.tenants is not None:
            for k in self.tenants:
                result['Tenants'].append(k.to_map() if k else None)
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tenants = []
        if m.get('Tenants') is not None:
            for k in m.get('Tenants'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyTenants()
                self.tenants.append(temp_model.from_map(k))
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeInstanceTopologyResponseBodyInstanceTopologyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeInstanceTopologyResponseBody(TeaModel):
    def __init__(
        self,
        instance_topology: DescribeInstanceTopologyResponseBodyInstanceTopology = None,
        request_id: str = None,
    ):
        self.instance_topology = instance_topology
        self.request_id = request_id

    def validate(self):
        if self.instance_topology:
            self.instance_topology.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_topology is not None:
            result['InstanceTopology'] = self.instance_topology.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTopology') is not None:
            temp_model = DescribeInstanceTopologyResponseBodyInstanceTopology()
            self.instance_topology = temp_model.from_map(m['InstanceTopology'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceTopologyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceTopologyResponseBody = None,
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
            temp_model = DescribeInstanceTopologyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        search_key: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.page_number = page_number
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class DescribeInstancesResponseBodyInstancesResourceCpu(TeaModel):
    def __init__(
        self,
        total_cpu: int = None,
        unit_cpu: int = None,
        used_cpu: int = None,
    ):
        self.total_cpu = total_cpu
        self.unit_cpu = unit_cpu
        self.used_cpu = used_cpu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeInstancesResponseBodyInstancesResourceDiskSize(TeaModel):
    def __init__(
        self,
        total_disk_size: int = None,
        unit_disk_size: int = None,
        used_disk_size: int = None,
    ):
        self.total_disk_size = total_disk_size
        self.unit_disk_size = unit_disk_size
        self.used_disk_size = used_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_disk_size is not None:
            result['TotalDiskSize'] = self.total_disk_size
        if self.unit_disk_size is not None:
            result['UnitDiskSize'] = self.unit_disk_size
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDiskSize') is not None:
            self.total_disk_size = m.get('TotalDiskSize')
        if m.get('UnitDiskSize') is not None:
            self.unit_disk_size = m.get('UnitDiskSize')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeInstancesResponseBodyInstancesResourceMemory(TeaModel):
    def __init__(
        self,
        total_memory: int = None,
        unit_memory: int = None,
        used_memory: int = None,
    ):
        self.total_memory = total_memory
        self.unit_memory = unit_memory
        self.used_memory = used_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeInstancesResponseBodyInstancesResource(TeaModel):
    def __init__(
        self,
        cpu: DescribeInstancesResponseBodyInstancesResourceCpu = None,
        disk_size: DescribeInstancesResponseBodyInstancesResourceDiskSize = None,
        memory: DescribeInstancesResponseBodyInstancesResourceMemory = None,
        unit_count: int = None,
    ):
        self.cpu = cpu
        self.disk_size = disk_size
        self.memory = memory
        self.unit_count = unit_count

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.unit_count is not None:
            result['UnitCount'] = self.unit_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('UnitCount') is not None:
            self.unit_count = m.get('UnitCount')
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        available_zones: List[str] = None,
        commodity_code: str = None,
        cpu: int = None,
        create_time: str = None,
        deploy_mode: str = None,
        deploy_type: str = None,
        disk_size: str = None,
        disk_type: str = None,
        enable_upgrade_nodes: bool = None,
        expire_seconds: int = None,
        expire_time: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        maintain_time: str = None,
        mem: int = None,
        pay_type: str = None,
        resource: DescribeInstancesResponseBodyInstancesResource = None,
        resource_group_id: str = None,
        security_ips: List[str] = None,
        series: str = None,
        state: str = None,
        used_disk_size: int = None,
        version: str = None,
        vpc_id: str = None,
    ):
        self.available_zones = available_zones
        self.commodity_code = commodity_code
        self.cpu = cpu
        self.create_time = create_time
        self.deploy_mode = deploy_mode
        self.deploy_type = deploy_type
        self.disk_size = disk_size
        self.disk_type = disk_type
        self.enable_upgrade_nodes = enable_upgrade_nodes
        self.expire_seconds = expire_seconds
        self.expire_time = expire_time
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.maintain_time = maintain_time
        self.mem = mem
        self.pay_type = pay_type
        self.resource = resource
        self.resource_group_id = resource_group_id
        self.security_ips = security_ips
        self.series = series
        self.state = state
        self.used_disk_size = used_disk_size
        self.version = version
        self.vpc_id = vpc_id

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_upgrade_nodes is not None:
            result['EnableUpgradeNodes'] = self.enable_upgrade_nodes
        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.series is not None:
            result['Series'] = self.series
        if self.state is not None:
            result['State'] = self.state
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableUpgradeNodes') is not None:
            self.enable_upgrade_nodes = m.get('EnableUpgradeNodes')
        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Resource') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeMetricsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        metrics: str = None,
        node_id_list: str = None,
        node_name: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.metrics = metrics
        self.node_id_list = node_id_list
        self.node_name = node_name
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeNodeMetricsResponseBody(TeaModel):
    def __init__(
        self,
        node_metrics: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.node_metrics = node_metrics
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_metrics is not None:
            result['NodeMetrics'] = self.node_metrics
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeMetrics') is not None:
            self.node_metrics = m.get('NodeMetrics')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeNodeMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodeMetricsResponseBody = None,
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
            temp_model = DescribeNodeMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataDestConfig(TeaModel):
    def __init__(
        self,
        enable_msg_trace: bool = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        msg_tags: str = None,
        partition: int = None,
        partition_mode: str = None,
        producer_group: str = None,
        send_msg_timeout: int = None,
        sequence_enable: bool = None,
        sequence_start_timestamp: int = None,
        serializer_type: str = None,
        topic_type: str = None,
    ):
        self.enable_msg_trace = enable_msg_trace
        self.endpoint_id = endpoint_id
        self.endpoint_type = endpoint_type
        self.msg_tags = msg_tags
        self.partition = partition
        self.partition_mode = partition_mode
        self.producer_group = producer_group
        self.send_msg_timeout = send_msg_timeout
        self.sequence_enable = sequence_enable
        self.sequence_start_timestamp = sequence_start_timestamp
        self.serializer_type = serializer_type
        self.topic_type = topic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataLabels(TeaModel):
    def __init__(
        self,
        count: int = None,
        creator: str = None,
        id: str = None,
        name: str = None,
    ):
        self.count = count
        self.creator = creator
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataSourceConfig(TeaModel):
    def __init__(
        self,
        enable_msg_trace: bool = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        msg_tags: str = None,
        partition: int = None,
        partition_mode: str = None,
        producer_group: str = None,
        send_msg_timeout: int = None,
        sequence_enable: bool = None,
        sequence_start_timestamp: int = None,
        serializer_type: str = None,
        topic_type: str = None,
    ):
        self.enable_msg_trace = enable_msg_trace
        self.endpoint_id = endpoint_id
        self.endpoint_type = endpoint_type
        self.msg_tags = msg_tags
        self.partition = partition
        self.partition_mode = partition_mode
        self.producer_group = producer_group
        self.send_msg_timeout = send_msg_timeout
        self.sequence_enable = sequence_enable
        self.sequence_start_timestamp = sequence_start_timestamp
        self.serializer_type = serializer_type
        self.topic_type = topic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfoErrorDetails(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfo(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_details: List[DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfoErrorDetails] = None,
        error_msg: str = None,
        error_param: Dict[str, str] = None,
        failed_time: str = None,
    ):
        self.error_code = error_code
        self.error_details = error_details
        self.error_msg = error_msg
        self.error_param = error_param
        self.failed_time = failed_time

    def validate(self):
        if self.error_details:
            for k in self.error_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k in self.error_details:
                result['ErrorDetails'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.error_param is not None:
            result['ErrorParam'] = self.error_param
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k in m.get('ErrorDetails'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfoErrorDetails()
                self.error_details.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ErrorParam') is not None:
            self.error_param = m.get('ErrorParam')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfoConnectorFullProgressOverview(TeaModel):
    def __init__(
        self,
        estimated_remaining_time_of_sec: int = None,
        estimated_total_count: int = None,
        finished_count: int = None,
        progress: int = None,
    ):
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec
        self.estimated_total_count = estimated_total_count
        self.finished_count = finished_count
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_time_of_sec is not None:
            result['EstimatedRemainingTimeOfSec'] = self.estimated_remaining_time_of_sec
        if self.estimated_total_count is not None:
            result['EstimatedTotalCount'] = self.estimated_total_count
        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedRemainingTimeOfSec') is not None:
            self.estimated_remaining_time_of_sec = m.get('EstimatedRemainingTimeOfSec')
        if m.get('EstimatedTotalCount') is not None:
            self.estimated_total_count = m.get('EstimatedTotalCount')
        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfo(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        checkpoint: str = None,
        connector_full_progress_overview: DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfoConnectorFullProgressOverview = None,
        deploy_id: str = None,
        dst_iops: int = None,
        dst_rps: int = None,
        dst_rps_ref: int = None,
        dst_rt: int = None,
        dst_rt_ref: int = None,
        gmt: int = None,
        inconsistencies: int = None,
        incr_timestamp_checkpoint: int = None,
        job_id: str = None,
        processed_records: int = None,
        skipped: bool = None,
        src_iops: int = None,
        src_iops_ref: int = None,
        src_rps: int = None,
        src_rps_ref: int = None,
        src_rt: int = None,
        src_rt_ref: int = None,
        validated: bool = None,
    ):
        self.capacity = capacity
        self.checkpoint = checkpoint
        self.connector_full_progress_overview = connector_full_progress_overview
        self.deploy_id = deploy_id
        self.dst_iops = dst_iops
        self.dst_rps = dst_rps
        self.dst_rps_ref = dst_rps_ref
        self.dst_rt = dst_rt
        self.dst_rt_ref = dst_rt_ref
        self.gmt = gmt
        self.inconsistencies = inconsistencies
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint
        self.job_id = job_id
        self.processed_records = processed_records
        self.skipped = skipped
        self.src_iops = src_iops
        self.src_iops_ref = src_iops_ref
        self.src_rps = src_rps
        self.src_rps_ref = src_rps_ref
        self.src_rt = src_rt
        self.src_rt_ref = src_rt_ref
        self.validated = validated

    def validate(self):
        if self.connector_full_progress_overview:
            self.connector_full_progress_overview.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.connector_full_progress_overview is not None:
            result['ConnectorFullProgressOverview'] = self.connector_full_progress_overview.to_map()
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.dst_iops is not None:
            result['DstIops'] = self.dst_iops
        if self.dst_rps is not None:
            result['DstRps'] = self.dst_rps
        if self.dst_rps_ref is not None:
            result['DstRpsRef'] = self.dst_rps_ref
        if self.dst_rt is not None:
            result['DstRt'] = self.dst_rt
        if self.dst_rt_ref is not None:
            result['DstRtRef'] = self.dst_rt_ref
        if self.gmt is not None:
            result['Gmt'] = self.gmt
        if self.inconsistencies is not None:
            result['Inconsistencies'] = self.inconsistencies
        if self.incr_timestamp_checkpoint is not None:
            result['IncrTimestampCheckpoint'] = self.incr_timestamp_checkpoint
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.processed_records is not None:
            result['ProcessedRecords'] = self.processed_records
        if self.skipped is not None:
            result['Skipped'] = self.skipped
        if self.src_iops is not None:
            result['SrcIops'] = self.src_iops
        if self.src_iops_ref is not None:
            result['SrcIopsRef'] = self.src_iops_ref
        if self.src_rps is not None:
            result['SrcRps'] = self.src_rps
        if self.src_rps_ref is not None:
            result['SrcRpsRef'] = self.src_rps_ref
        if self.src_rt is not None:
            result['SrcRt'] = self.src_rt
        if self.src_rt_ref is not None:
            result['SrcRtRef'] = self.src_rt_ref
        if self.validated is not None:
            result['Validated'] = self.validated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConnectorFullProgressOverview') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfoConnectorFullProgressOverview()
            self.connector_full_progress_overview = temp_model.from_map(m['ConnectorFullProgressOverview'])
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('DstIops') is not None:
            self.dst_iops = m.get('DstIops')
        if m.get('DstRps') is not None:
            self.dst_rps = m.get('DstRps')
        if m.get('DstRpsRef') is not None:
            self.dst_rps_ref = m.get('DstRpsRef')
        if m.get('DstRt') is not None:
            self.dst_rt = m.get('DstRt')
        if m.get('DstRtRef') is not None:
            self.dst_rt_ref = m.get('DstRtRef')
        if m.get('Gmt') is not None:
            self.gmt = m.get('Gmt')
        if m.get('Inconsistencies') is not None:
            self.inconsistencies = m.get('Inconsistencies')
        if m.get('IncrTimestampCheckpoint') is not None:
            self.incr_timestamp_checkpoint = m.get('IncrTimestampCheckpoint')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProcessedRecords') is not None:
            self.processed_records = m.get('ProcessedRecords')
        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')
        if m.get('SrcIops') is not None:
            self.src_iops = m.get('SrcIops')
        if m.get('SrcIopsRef') is not None:
            self.src_iops_ref = m.get('SrcIopsRef')
        if m.get('SrcRps') is not None:
            self.src_rps = m.get('SrcRps')
        if m.get('SrcRpsRef') is not None:
            self.src_rps_ref = m.get('SrcRpsRef')
        if m.get('SrcRt') is not None:
            self.src_rt = m.get('SrcRt')
        if m.get('SrcRtRef') is not None:
            self.src_rt_ref = m.get('SrcRtRef')
        if m.get('Validated') is not None:
            self.validated = m.get('Validated')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataSteps(TeaModel):
    def __init__(
        self,
        estimated_remaining_seconds: int = None,
        extra_info: DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfo = None,
        finish_time: str = None,
        interactive: bool = None,
        start_time: str = None,
        step_description: str = None,
        step_info: DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfo = None,
        step_name: str = None,
        step_order: int = None,
        step_progress: int = None,
        step_status: str = None,
    ):
        self.estimated_remaining_seconds = estimated_remaining_seconds
        self.extra_info = extra_info
        self.finish_time = finish_time
        self.interactive = interactive
        self.start_time = start_time
        self.step_description = step_description
        self.step_info = step_info
        self.step_name = step_name
        self.step_order = step_order
        self.step_progress = step_progress
        self.step_status = step_status

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.step_info:
            self.step_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_seconds is not None:
            result['EstimatedRemainingSeconds'] = self.estimated_remaining_seconds
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_description is not None:
            result['StepDescription'] = self.step_description
        if self.step_info is not None:
            result['StepInfo'] = self.step_info.to_map()
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress
        if self.step_status is not None:
            result['StepStatus'] = self.step_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedRemainingSeconds') is not None:
            self.estimated_remaining_seconds = m.get('EstimatedRemainingSeconds')
        if m.get('ExtraInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepDescription') is not None:
            self.step_description = m.get('StepDescription')
        if m.get('StepInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataStepsStepInfo()
            self.step_info = temp_model.from_map(m['StepInfo'])
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')
        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema(TeaModel):
    def __init__(
        self,
        distributed_keys: List[str] = None,
        partition_life_cycle: int = None,
        partition_statement: str = None,
        primary_keys: List[str] = None,
    ):
        self.distributed_keys = distributed_keys
        self.partition_life_cycle = partition_life_cycle
        self.partition_statement = partition_statement
        self.primary_keys = primary_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributed_keys is not None:
            result['DistributedKeys'] = self.distributed_keys
        if self.partition_life_cycle is not None:
            result['PartitionLifeCycle'] = self.partition_life_cycle
        if self.partition_statement is not None:
            result['PartitionStatement'] = self.partition_statement
        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributedKeys') is not None:
            self.distributed_keys = m.get('DistributedKeys')
        if m.get('PartitionLifeCycle') is not None:
            self.partition_life_cycle = m.get('PartitionLifeCycle')
        if m.get('PartitionStatement') is not None:
            self.partition_statement = m.get('PartitionStatement')
        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTables(TeaModel):
    def __init__(
        self,
        adb_table_schema: DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema = None,
        filter_columns: List[str] = None,
        mapped_name: str = None,
        shard_columns: List[str] = None,
        table_id: str = None,
        table_name: str = None,
        type: str = None,
        where_clause: str = None,
    ):
        self.adb_table_schema = adb_table_schema
        self.filter_columns = filter_columns
        self.mapped_name = mapped_name
        self.shard_columns = shard_columns
        self.table_id = table_id
        self.table_name = table_name
        self.type = type
        self.where_clause = where_clause

    def validate(self):
        if self.adb_table_schema:
            self.adb_table_schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adb_table_schema is not None:
            result['AdbTableSchema'] = self.adb_table_schema.to_map()
        if self.filter_columns is not None:
            result['FilterColumns'] = self.filter_columns
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        if self.shard_columns is not None:
            result['ShardColumns'] = self.shard_columns
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.where_clause is not None:
            result['WhereClause'] = self.where_clause
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdbTableSchema') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema()
            self.adb_table_schema = temp_model.from_map(m['AdbTableSchema'])
        if m.get('FilterColumns') is not None:
            self.filter_columns = m.get('FilterColumns')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        if m.get('ShardColumns') is not None:
            self.shard_columns = m.get('ShardColumns')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhereClause') is not None:
            self.where_clause = m.get('WhereClause')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabases(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        database_name: str = None,
        mapped_name: str = None,
        tables: List[DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTables] = None,
        tenant_name: str = None,
        type: str = None,
    ):
        self.database_id = database_id
        self.database_name = database_name
        self.mapped_name = mapped_name
        self.tables = tables
        self.tenant_name = tenant_name
        self.type = type

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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferMapping(TeaModel):
    def __init__(
        self,
        databases: List[DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabases] = None,
        mode: str = None,
    ):
        self.databases = databases
        self.mode = mode

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMappingDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig(TeaModel):
    def __init__(
        self,
        record_type_list: List[str] = None,
        start_timestamp: int = None,
        store_log_kept_hour: int = None,
        store_transaction_enabled: bool = None,
        transfer_step_type: str = None,
    ):
        self.record_type_list = record_type_list
        self.start_timestamp = start_timestamp
        self.store_log_kept_hour = store_log_kept_hour
        self.store_transaction_enabled = store_transaction_enabled
        self.transfer_step_type = transfer_step_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_type_list is not None:
            result['RecordTypeList'] = self.record_type_list
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.store_log_kept_hour is not None:
            result['StoreLogKeptHour'] = self.store_log_kept_hour
        if self.store_transaction_enabled is not None:
            result['StoreTransactionEnabled'] = self.store_transaction_enabled
        if self.transfer_step_type is not None:
            result['TransferStepType'] = self.transfer_step_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordTypeList') is not None:
            self.record_type_list = m.get('RecordTypeList')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('StoreLogKeptHour') is not None:
            self.store_log_kept_hour = m.get('StoreLogKeptHour')
        if m.get('StoreTransactionEnabled') is not None:
            self.store_transaction_enabled = m.get('StoreTransactionEnabled')
        if m.get('TransferStepType') is not None:
            self.transfer_step_type = m.get('TransferStepType')
        return self


class DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfig(TeaModel):
    def __init__(
        self,
        enable_full_sync: bool = None,
        enable_incr_sync: bool = None,
        enable_struct_sync: bool = None,
        incr_sync_step_transfer_config: DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig = None,
    ):
        self.enable_full_sync = enable_full_sync
        self.enable_incr_sync = enable_incr_sync
        self.enable_struct_sync = enable_struct_sync
        self.incr_sync_step_transfer_config = incr_sync_step_transfer_config

    def validate(self):
        if self.incr_sync_step_transfer_config:
            self.incr_sync_step_transfer_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_full_sync is not None:
            result['EnableFullSync'] = self.enable_full_sync
        if self.enable_incr_sync is not None:
            result['EnableIncrSync'] = self.enable_incr_sync
        if self.enable_struct_sync is not None:
            result['EnableStructSync'] = self.enable_struct_sync
        if self.incr_sync_step_transfer_config is not None:
            result['IncrSyncStepTransferConfig'] = self.incr_sync_step_transfer_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableFullSync') is not None:
            self.enable_full_sync = m.get('EnableFullSync')
        if m.get('EnableIncrSync') is not None:
            self.enable_incr_sync = m.get('EnableIncrSync')
        if m.get('EnableStructSync') is not None:
            self.enable_struct_sync = m.get('EnableStructSync')
        if m.get('IncrSyncStepTransferConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig()
            self.incr_sync_step_transfer_config = temp_model.from_map(m['IncrSyncStepTransferConfig'])
        return self


class DescribeOmsOpenAPIProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        business_name: str = None,
        dest_config: DescribeOmsOpenAPIProjectResponseBodyDataDestConfig = None,
        labels: List[DescribeOmsOpenAPIProjectResponseBodyDataLabels] = None,
        project_id: str = None,
        project_name: str = None,
        project_owner: str = None,
        source_config: DescribeOmsOpenAPIProjectResponseBodyDataSourceConfig = None,
        steps: List[DescribeOmsOpenAPIProjectResponseBodyDataSteps] = None,
        transfer_mapping: DescribeOmsOpenAPIProjectResponseBodyDataTransferMapping = None,
        transfer_step_config: DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfig = None,
    ):
        self.business_name = business_name
        self.dest_config = dest_config
        self.labels = labels
        self.project_id = project_id
        self.project_name = project_name
        self.project_owner = project_owner
        self.source_config = source_config
        self.steps = steps
        self.transfer_mapping = transfer_mapping
        self.transfer_step_config = transfer_step_config

    def validate(self):
        if self.dest_config:
            self.dest_config.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.source_config:
            self.source_config.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()
        if self.transfer_mapping:
            self.transfer_mapping.validate()
        if self.transfer_step_config:
            self.transfer_step_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config is not None:
            result['DestConfig'] = self.dest_config.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_owner is not None:
            result['ProjectOwner'] = self.project_owner
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config.to_map()
        result['Steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['Steps'].append(k.to_map() if k else None)
        if self.transfer_mapping is not None:
            result['TransferMapping'] = self.transfer_mapping.to_map()
        if self.transfer_step_config is not None:
            result['TransferStepConfig'] = self.transfer_step_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataDestConfig()
            self.dest_config = temp_model.from_map(m['DestConfig'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectOwner') is not None:
            self.project_owner = m.get('ProjectOwner')
        if m.get('SourceConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataSourceConfig()
            self.source_config = temp_model.from_map(m['SourceConfig'])
        self.steps = []
        if m.get('Steps') is not None:
            for k in m.get('Steps'):
                temp_model = DescribeOmsOpenAPIProjectResponseBodyDataSteps()
                self.steps.append(temp_model.from_map(k))
        if m.get('TransferMapping') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferMapping()
            self.transfer_mapping = temp_model.from_map(m['TransferMapping'])
        if m.get('TransferStepConfig') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyDataTransferStepConfig()
            self.transfer_step_config = temp_model.from_map(m['TransferStepConfig'])
        return self


class DescribeOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: DescribeOmsOpenAPIProjectResponseBodyData = None,
        error_detail: DescribeOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorDetail') is not None:
            temp_model = DescribeOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOmsOpenAPIProjectResponseBody = None,
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
            temp_model = DescribeOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOmsOpenAPIProjectStepsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfoErrorDetails(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfo(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_details: List[DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfoErrorDetails] = None,
        error_msg: str = None,
        error_param: Dict[str, str] = None,
        failed_time: str = None,
    ):
        self.error_code = error_code
        self.error_details = error_details
        self.error_msg = error_msg
        self.error_param = error_param
        self.failed_time = failed_time

    def validate(self):
        if self.error_details:
            for k in self.error_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k in self.error_details:
                result['ErrorDetails'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.error_param is not None:
            result['ErrorParam'] = self.error_param
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k in m.get('ErrorDetails'):
                temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfoErrorDetails()
                self.error_details.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ErrorParam') is not None:
            self.error_param = m.get('ErrorParam')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfoConnectorFullProgressOverview(TeaModel):
    def __init__(
        self,
        estimated_remaining_time_of_sec: int = None,
        estimated_total_count: int = None,
        finished_count: int = None,
        progress: int = None,
    ):
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec
        self.estimated_total_count = estimated_total_count
        self.finished_count = finished_count
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_time_of_sec is not None:
            result['EstimatedRemainingTimeOfSec'] = self.estimated_remaining_time_of_sec
        if self.estimated_total_count is not None:
            result['EstimatedTotalCount'] = self.estimated_total_count
        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedRemainingTimeOfSec') is not None:
            self.estimated_remaining_time_of_sec = m.get('EstimatedRemainingTimeOfSec')
        if m.get('EstimatedTotalCount') is not None:
            self.estimated_total_count = m.get('EstimatedTotalCount')
        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfo(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        checkpoint: str = None,
        connector_full_progress_overview: DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfoConnectorFullProgressOverview = None,
        deploy_id: str = None,
        dst_iops: int = None,
        dst_rps: int = None,
        dst_rps_ref: int = None,
        dst_rt: int = None,
        dst_rt_ref: int = None,
        gmt: int = None,
        inconsistencies: int = None,
        incr_timestamp_checkpoint: int = None,
        job_id: str = None,
        processed_records: int = None,
        skipped: bool = None,
        src_iops: int = None,
        src_iops_ref: int = None,
        src_rps: int = None,
        src_rps_ref: int = None,
        src_rt: int = None,
        src_rt_ref: int = None,
        validated: bool = None,
    ):
        self.capacity = capacity
        self.checkpoint = checkpoint
        self.connector_full_progress_overview = connector_full_progress_overview
        self.deploy_id = deploy_id
        self.dst_iops = dst_iops
        self.dst_rps = dst_rps
        self.dst_rps_ref = dst_rps_ref
        self.dst_rt = dst_rt
        self.dst_rt_ref = dst_rt_ref
        self.gmt = gmt
        self.inconsistencies = inconsistencies
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint
        self.job_id = job_id
        self.processed_records = processed_records
        self.skipped = skipped
        self.src_iops = src_iops
        self.src_iops_ref = src_iops_ref
        self.src_rps = src_rps
        self.src_rps_ref = src_rps_ref
        self.src_rt = src_rt
        self.src_rt_ref = src_rt_ref
        self.validated = validated

    def validate(self):
        if self.connector_full_progress_overview:
            self.connector_full_progress_overview.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.connector_full_progress_overview is not None:
            result['ConnectorFullProgressOverview'] = self.connector_full_progress_overview.to_map()
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.dst_iops is not None:
            result['DstIops'] = self.dst_iops
        if self.dst_rps is not None:
            result['DstRps'] = self.dst_rps
        if self.dst_rps_ref is not None:
            result['DstRpsRef'] = self.dst_rps_ref
        if self.dst_rt is not None:
            result['DstRt'] = self.dst_rt
        if self.dst_rt_ref is not None:
            result['DstRtRef'] = self.dst_rt_ref
        if self.gmt is not None:
            result['Gmt'] = self.gmt
        if self.inconsistencies is not None:
            result['Inconsistencies'] = self.inconsistencies
        if self.incr_timestamp_checkpoint is not None:
            result['IncrTimestampCheckpoint'] = self.incr_timestamp_checkpoint
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.processed_records is not None:
            result['ProcessedRecords'] = self.processed_records
        if self.skipped is not None:
            result['Skipped'] = self.skipped
        if self.src_iops is not None:
            result['SrcIops'] = self.src_iops
        if self.src_iops_ref is not None:
            result['SrcIopsRef'] = self.src_iops_ref
        if self.src_rps is not None:
            result['SrcRps'] = self.src_rps
        if self.src_rps_ref is not None:
            result['SrcRpsRef'] = self.src_rps_ref
        if self.src_rt is not None:
            result['SrcRt'] = self.src_rt
        if self.src_rt_ref is not None:
            result['SrcRtRef'] = self.src_rt_ref
        if self.validated is not None:
            result['Validated'] = self.validated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConnectorFullProgressOverview') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfoConnectorFullProgressOverview()
            self.connector_full_progress_overview = temp_model.from_map(m['ConnectorFullProgressOverview'])
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('DstIops') is not None:
            self.dst_iops = m.get('DstIops')
        if m.get('DstRps') is not None:
            self.dst_rps = m.get('DstRps')
        if m.get('DstRpsRef') is not None:
            self.dst_rps_ref = m.get('DstRpsRef')
        if m.get('DstRt') is not None:
            self.dst_rt = m.get('DstRt')
        if m.get('DstRtRef') is not None:
            self.dst_rt_ref = m.get('DstRtRef')
        if m.get('Gmt') is not None:
            self.gmt = m.get('Gmt')
        if m.get('Inconsistencies') is not None:
            self.inconsistencies = m.get('Inconsistencies')
        if m.get('IncrTimestampCheckpoint') is not None:
            self.incr_timestamp_checkpoint = m.get('IncrTimestampCheckpoint')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProcessedRecords') is not None:
            self.processed_records = m.get('ProcessedRecords')
        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')
        if m.get('SrcIops') is not None:
            self.src_iops = m.get('SrcIops')
        if m.get('SrcIopsRef') is not None:
            self.src_iops_ref = m.get('SrcIopsRef')
        if m.get('SrcRps') is not None:
            self.src_rps = m.get('SrcRps')
        if m.get('SrcRpsRef') is not None:
            self.src_rps_ref = m.get('SrcRpsRef')
        if m.get('SrcRt') is not None:
            self.src_rt = m.get('SrcRt')
        if m.get('SrcRtRef') is not None:
            self.src_rt_ref = m.get('SrcRtRef')
        if m.get('Validated') is not None:
            self.validated = m.get('Validated')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyData(TeaModel):
    def __init__(
        self,
        estimated_remaining_seconds: int = None,
        extra_info: DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfo = None,
        finish_time: str = None,
        interactive: bool = None,
        start_time: str = None,
        step_description: str = None,
        step_info: DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfo = None,
        step_name: str = None,
        step_order: int = None,
        step_progress: int = None,
        step_status: str = None,
    ):
        self.estimated_remaining_seconds = estimated_remaining_seconds
        self.extra_info = extra_info
        self.finish_time = finish_time
        self.interactive = interactive
        self.start_time = start_time
        self.step_description = step_description
        self.step_info = step_info
        self.step_name = step_name
        self.step_order = step_order
        self.step_progress = step_progress
        self.step_status = step_status

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.step_info:
            self.step_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_seconds is not None:
            result['EstimatedRemainingSeconds'] = self.estimated_remaining_seconds
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_description is not None:
            result['StepDescription'] = self.step_description
        if self.step_info is not None:
            result['StepInfo'] = self.step_info.to_map()
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress
        if self.step_status is not None:
            result['StepStatus'] = self.step_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedRemainingSeconds') is not None:
            self.estimated_remaining_seconds = m.get('EstimatedRemainingSeconds')
        if m.get('ExtraInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepDescription') is not None:
            self.step_description = m.get('StepDescription')
        if m.get('StepInfo') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyDataStepInfo()
            self.step_info = temp_model.from_map(m['StepInfo'])
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')
        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class DescribeOmsOpenAPIProjectStepsResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: List[DescribeOmsOpenAPIProjectStepsResponseBodyData] = None,
        error_detail: DescribeOmsOpenAPIProjectStepsResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorDetail') is not None:
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOmsOpenAPIProjectStepsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOmsOpenAPIProjectStepsResponseBody = None,
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
            temp_model = DescribeOmsOpenAPIProjectStepsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOutlineBindingRequest(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        instance_id: str = None,
        is_concurrent_limit: bool = None,
        sqlid: str = None,
        table_name: str = None,
        tenant_id: str = None,
    ):
        self.database_name = database_name
        self.instance_id = instance_id
        self.is_concurrent_limit = is_concurrent_limit
        self.sqlid = sqlid
        self.table_name = table_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_concurrent_limit is not None:
            result['IsConcurrentLimit'] = self.is_concurrent_limit
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsConcurrentLimit') is not None:
            self.is_concurrent_limit = m.get('IsConcurrentLimit')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOutlineBindingResponseBodyOutlineBinding(TeaModel):
    def __init__(
        self,
        bind_index: str = None,
        bind_plan: str = None,
        max_concurrent: int = None,
        outline_id: int = None,
    ):
        self.bind_index = bind_index
        self.bind_plan = bind_plan
        self.max_concurrent = max_concurrent
        self.outline_id = outline_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_index is not None:
            result['BindIndex'] = self.bind_index
        if self.bind_plan is not None:
            result['BindPlan'] = self.bind_plan
        if self.max_concurrent is not None:
            result['MaxConcurrent'] = self.max_concurrent
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindIndex') is not None:
            self.bind_index = m.get('BindIndex')
        if m.get('BindPlan') is not None:
            self.bind_plan = m.get('BindPlan')
        if m.get('MaxConcurrent') is not None:
            self.max_concurrent = m.get('MaxConcurrent')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        return self


class DescribeOutlineBindingResponseBody(TeaModel):
    def __init__(
        self,
        outline_binding: DescribeOutlineBindingResponseBodyOutlineBinding = None,
        request_id: str = None,
    ):
        self.outline_binding = outline_binding
        self.request_id = request_id

    def validate(self):
        if self.outline_binding:
            self.outline_binding.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline_binding is not None:
            result['OutlineBinding'] = self.outline_binding.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutlineBinding') is not None:
            temp_model = DescribeOutlineBindingResponseBodyOutlineBinding()
            self.outline_binding = temp_model.from_map(m['OutlineBinding'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOutlineBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOutlineBindingResponseBody = None,
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
            temp_model = DescribeOutlineBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
    def __init__(
        self,
        dimension: str = None,
        dimension_value: str = None,
        instance_id: str = None,
    ):
        self.dimension = dimension
        self.dimension_value = dimension_value
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        acceptable_value: List[str] = None,
        current_value: str = None,
        default_value: str = None,
        description: str = None,
        name: str = None,
        need_reboot: bool = None,
        rejected_value: List[str] = None,
        value_type: str = None,
    ):
        self.acceptable_value = acceptable_value
        self.current_value = current_value
        self.default_value = default_value
        self.description = description
        self.name = name
        self.need_reboot = need_reboot
        self.rejected_value = rejected_value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceptable_value is not None:
            result['AcceptableValue'] = self.acceptable_value
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.need_reboot is not None:
            result['NeedReboot'] = self.need_reboot
        if self.rejected_value is not None:
            result['RejectedValue'] = self.rejected_value
        if self.value_type is not None:
            result['ValueType'] = self.value_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptableValue') is not None:
            self.acceptable_value = m.get('AcceptableValue')
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NeedReboot') is not None:
            self.need_reboot = m.get('NeedReboot')
        if m.get('RejectedValue') is not None:
            self.rejected_value = m.get('RejectedValue')
        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(
        self,
        parameters: List[DescribeParametersResponseBodyParameters] = None,
        request_id: str = None,
    ):
        self.parameters = parameters
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeParametersResponseBody = None,
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
            temp_model = DescribeParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersHistoryRequest(TeaModel):
    def __init__(
        self,
        dimension: str = None,
        dimension_value: str = None,
        end_time: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
    ):
        self.dimension = dimension
        self.dimension_value = dimension_value
        self.end_time = end_time
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeParametersHistoryResponseBodyRespondParameters(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        dimension_value: str = None,
        name: str = None,
        new_value: str = None,
        old_value: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.dimension_value = dimension_value
        self.name = name
        self.new_value = new_value
        self.old_value = old_value
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.name is not None:
            result['Name'] = self.name
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeParametersHistoryResponseBodyRespond(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        parameters: List[DescribeParametersHistoryResponseBodyRespondParameters] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.parameters = parameters
        self.total_count = total_count

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeParametersHistoryResponseBodyRespondParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeParametersHistoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        respond: List[DescribeParametersHistoryResponseBodyRespond] = None,
    ):
        self.request_id = request_id
        self.respond = respond

    def validate(self):
        if self.respond:
            for k in self.respond:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Respond'] = []
        if self.respond is not None:
            for k in self.respond:
                result['Respond'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.respond = []
        if m.get('Respond') is not None:
            for k in m.get('Respond'):
                temp_model = DescribeParametersHistoryResponseBodyRespond()
                self.respond.append(temp_model.from_map(k))
        return self


class DescribeParametersHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeParametersHistoryResponseBody = None,
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
            temp_model = DescribeParametersHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecommendIndexRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        sqlid: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.sqlid = sqlid
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeRecommendIndexResponseBodyRecommendIndex(TeaModel):
    def __init__(
        self,
        suggest_index: str = None,
        table_list: str = None,
        tenant_mode: str = None,
    ):
        self.suggest_index = suggest_index
        self.table_list = table_list
        self.tenant_mode = tenant_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.suggest_index is not None:
            result['SuggestIndex'] = self.suggest_index
        if self.table_list is not None:
            result['TableList'] = self.table_list
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuggestIndex') is not None:
            self.suggest_index = m.get('SuggestIndex')
        if m.get('TableList') is not None:
            self.table_list = m.get('TableList')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        return self


class DescribeRecommendIndexResponseBody(TeaModel):
    def __init__(
        self,
        recommend_index: DescribeRecommendIndexResponseBodyRecommendIndex = None,
        request_id: str = None,
    ):
        self.recommend_index = recommend_index
        self.request_id = request_id

    def validate(self):
        if self.recommend_index:
            self.recommend_index.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_index is not None:
            result['RecommendIndex'] = self.recommend_index.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendIndex') is not None:
            temp_model = DescribeRecommendIndexResponseBodyRecommendIndex()
            self.recommend_index = temp_model.from_map(m['RecommendIndex'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRecommendIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRecommendIndexResponseBody = None,
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
            temp_model = DescribeRecommendIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLDetailsRequest(TeaModel):
    def __init__(
        self,
        sqlid: str = None,
        tenant_id: str = None,
    ):
        self.sqlid = sqlid
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSQLDetailsResponseBodySQLDetails(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        sqltext: str = None,
        user_name: str = None,
    ):
        self.db_name = db_name
        self.sqltext = sqltext
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSQLDetailsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sqldetails: List[DescribeSQLDetailsResponseBodySQLDetails] = None,
    ):
        self.request_id = request_id
        self.sqldetails = sqldetails

    def validate(self):
        if self.sqldetails:
            for k in self.sqldetails:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SQLDetails'] = []
        if self.sqldetails is not None:
            for k in self.sqldetails:
                result['SQLDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sqldetails = []
        if m.get('SQLDetails') is not None:
            for k in m.get('SQLDetails'):
                temp_model = DescribeSQLDetailsResponseBodySQLDetails()
                self.sqldetails.append(temp_model.from_map(k))
        return self


class DescribeSQLDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLDetailsResponseBody = None,
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
            temp_model = DescribeSQLDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLHistoryListRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSQLHistoryListResponseBodySQLHistoryListList(TeaModel):
    def __init__(
        self,
        affected_rows: int = None,
        app_wait_time: float = None,
        block_cache_hit: int = None,
        block_index_cache_hit: int = None,
        bloom_filter_cache_hit: int = None,
        client_ip: str = None,
        concurrency_wait_time: float = None,
        cpu_time: float = None,
        db_name: str = None,
        decode_time: float = None,
        disk_read: int = None,
        elapsed_time: float = None,
        end_time: int = None,
        end_time_utcstring: str = None,
        event: str = None,
        exec_per_second: int = None,
        execute_time: float = None,
        executions: int = None,
        fail_times: int = None,
        get_plan_time: float = None,
        iowait_time: float = None,
        logical_read: int = None,
        max_cpu_time: float = None,
        max_elapsed_time: float = None,
        memstore_read_row_count: int = None,
        miss_plans: int = None,
        net_wait_time: float = None,
        node_ip: str = None,
        queue_time: float = None,
        rpccount: int = None,
        remote_plans: int = None,
        retry_count: int = None,
        return_rows: int = None,
        row_cache_hit: int = None,
        schedule_time: float = None,
        ssstore_read_row_count: int = None,
        total_wait_time: float = None,
        user_name: str = None,
    ):
        self.affected_rows = affected_rows
        self.app_wait_time = app_wait_time
        self.block_cache_hit = block_cache_hit
        self.block_index_cache_hit = block_index_cache_hit
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        self.client_ip = client_ip
        self.concurrency_wait_time = concurrency_wait_time
        self.cpu_time = cpu_time
        self.db_name = db_name
        self.decode_time = decode_time
        self.disk_read = disk_read
        self.elapsed_time = elapsed_time
        self.end_time = end_time
        self.end_time_utcstring = end_time_utcstring
        self.event = event
        self.exec_per_second = exec_per_second
        self.execute_time = execute_time
        self.executions = executions
        self.fail_times = fail_times
        self.get_plan_time = get_plan_time
        self.iowait_time = iowait_time
        self.logical_read = logical_read
        self.max_cpu_time = max_cpu_time
        self.max_elapsed_time = max_elapsed_time
        self.memstore_read_row_count = memstore_read_row_count
        self.miss_plans = miss_plans
        self.net_wait_time = net_wait_time
        self.node_ip = node_ip
        self.queue_time = queue_time
        self.rpccount = rpccount
        self.remote_plans = remote_plans
        self.retry_count = retry_count
        self.return_rows = return_rows
        self.row_cache_hit = row_cache_hit
        self.schedule_time = schedule_time
        self.ssstore_read_row_count = ssstore_read_row_count
        self.total_wait_time = total_wait_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.end_time_utcstring is not None:
            result['EndTimeUTCString'] = self.end_time_utcstring
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EndTimeUTCString') is not None:
            self.end_time_utcstring = m.get('EndTimeUTCString')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSQLHistoryListResponseBodySQLHistoryList(TeaModel):
    def __init__(
        self,
        count: int = None,
        list: List[DescribeSQLHistoryListResponseBodySQLHistoryListList] = None,
    ):
        self.count = count
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeSQLHistoryListResponseBodySQLHistoryListList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeSQLHistoryListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sqlhistory_list: DescribeSQLHistoryListResponseBodySQLHistoryList = None,
    ):
        self.request_id = request_id
        self.sqlhistory_list = sqlhistory_list

    def validate(self):
        if self.sqlhistory_list:
            self.sqlhistory_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sqlhistory_list is not None:
            result['SQLHistoryList'] = self.sqlhistory_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SQLHistoryList') is not None:
            temp_model = DescribeSQLHistoryListResponseBodySQLHistoryList()
            self.sqlhistory_list = temp_model.from_map(m['SQLHistoryList'])
        return self


class DescribeSQLHistoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLHistoryListResponseBody = None,
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
            temp_model = DescribeSQLHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSQLPlansRequest(TeaModel):
    def __init__(
        self,
        sqlid: str = None,
        tenant_id: str = None,
    ):
        self.sqlid = sqlid
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSQLPlansResponseBodySQLPlans(TeaModel):
    def __init__(
        self,
        avg_execution_ms: float = None,
        avg_execution_time_ms: int = None,
        first_load_time: int = None,
        first_load_time_utcstring: str = None,
        hit_count: int = None,
        merged_version: int = None,
        node_ip: str = None,
        outline_data: str = None,
        outline_id: int = None,
        outline_time: int = None,
        outline_time_utcstring: str = None,
        plan_full: str = None,
        plan_id: int = None,
        plan_info: str = None,
        plan_union_hash: str = None,
        query_sql: str = None,
    ):
        self.avg_execution_ms = avg_execution_ms
        self.avg_execution_time_ms = avg_execution_time_ms
        self.first_load_time = first_load_time
        self.first_load_time_utcstring = first_load_time_utcstring
        self.hit_count = hit_count
        self.merged_version = merged_version
        self.node_ip = node_ip
        self.outline_data = outline_data
        self.outline_id = outline_id
        self.outline_time = outline_time
        self.outline_time_utcstring = outline_time_utcstring
        self.plan_full = plan_full
        self.plan_id = plan_id
        self.plan_info = plan_info
        self.plan_union_hash = plan_union_hash
        self.query_sql = query_sql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_execution_ms is not None:
            result['AvgExecutionMS'] = self.avg_execution_ms
        if self.avg_execution_time_ms is not None:
            result['AvgExecutionTimeMS'] = self.avg_execution_time_ms
        if self.first_load_time is not None:
            result['FirstLoadTime'] = self.first_load_time
        if self.first_load_time_utcstring is not None:
            result['FirstLoadTimeUTCString'] = self.first_load_time_utcstring
        if self.hit_count is not None:
            result['HitCount'] = self.hit_count
        if self.merged_version is not None:
            result['MergedVersion'] = self.merged_version
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.outline_data is not None:
            result['OutlineData'] = self.outline_data
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.outline_time is not None:
            result['OutlineTime'] = self.outline_time
        if self.outline_time_utcstring is not None:
            result['OutlineTimeUTCString'] = self.outline_time_utcstring
        if self.plan_full is not None:
            result['PlanFull'] = self.plan_full
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_info is not None:
            result['PlanInfo'] = self.plan_info
        if self.plan_union_hash is not None:
            result['PlanUnionHash'] = self.plan_union_hash
        if self.query_sql is not None:
            result['QuerySQL'] = self.query_sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgExecutionMS') is not None:
            self.avg_execution_ms = m.get('AvgExecutionMS')
        if m.get('AvgExecutionTimeMS') is not None:
            self.avg_execution_time_ms = m.get('AvgExecutionTimeMS')
        if m.get('FirstLoadTime') is not None:
            self.first_load_time = m.get('FirstLoadTime')
        if m.get('FirstLoadTimeUTCString') is not None:
            self.first_load_time_utcstring = m.get('FirstLoadTimeUTCString')
        if m.get('HitCount') is not None:
            self.hit_count = m.get('HitCount')
        if m.get('MergedVersion') is not None:
            self.merged_version = m.get('MergedVersion')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('OutlineData') is not None:
            self.outline_data = m.get('OutlineData')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('OutlineTime') is not None:
            self.outline_time = m.get('OutlineTime')
        if m.get('OutlineTimeUTCString') is not None:
            self.outline_time_utcstring = m.get('OutlineTimeUTCString')
        if m.get('PlanFull') is not None:
            self.plan_full = m.get('PlanFull')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanInfo') is not None:
            self.plan_info = m.get('PlanInfo')
        if m.get('PlanUnionHash') is not None:
            self.plan_union_hash = m.get('PlanUnionHash')
        if m.get('QuerySQL') is not None:
            self.query_sql = m.get('QuerySQL')
        return self


class DescribeSQLPlansResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sqlplans: List[DescribeSQLPlansResponseBodySQLPlans] = None,
    ):
        self.request_id = request_id
        self.sqlplans = sqlplans

    def validate(self):
        if self.sqlplans:
            for k in self.sqlplans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SQLPlans'] = []
        if self.sqlplans is not None:
            for k in self.sqlplans:
                result['SQLPlans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sqlplans = []
        if m.get('SQLPlans') is not None:
            for k in m.get('SQLPlans'):
                temp_model = DescribeSQLPlansResponseBodySQLPlans()
                self.sqlplans.append(temp_model.from_map(k))
        return self


class DescribeSQLPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLPlansResponseBody = None,
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
            temp_model = DescribeSQLPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIpGroupsRequest(TeaModel):
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
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeSecurityIpGroupsResponseBodySecurityIpGroups(TeaModel):
    def __init__(
        self,
        security_ip_group_name: str = None,
        security_ips: str = None,
    ):
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class DescribeSecurityIpGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_groups: List[DescribeSecurityIpGroupsResponseBodySecurityIpGroups] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.security_ip_groups = security_ip_groups
        self.total_count = total_count

    def validate(self):
        if self.security_ip_groups:
            for k in self.security_ip_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityIpGroups'] = []
        if self.security_ip_groups is not None:
            for k in self.security_ip_groups:
                result['SecurityIpGroups'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_ip_groups = []
        if m.get('SecurityIpGroups') is not None:
            for k in m.get('SecurityIpGroups'):
                temp_model = DescribeSecurityIpGroupsResponseBodySecurityIpGroups()
                self.security_ip_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSecurityIpGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecurityIpGroupsResponseBody = None,
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
            temp_model = DescribeSecurityIpGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowSQLHistoryListRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryListList(TeaModel):
    def __init__(
        self,
        affected_rows: float = None,
        app_wait_time: float = None,
        block_cache_hit: float = None,
        block_index_cache_hit: float = None,
        bloom_filter_cache_hit: float = None,
        client_ip: str = None,
        concurrency_wait_time: float = None,
        cpu_time: float = None,
        db_name: str = None,
        decode_time: float = None,
        disk_read: float = None,
        elapsed_time: float = None,
        end_time_utcstring: str = None,
        event: str = None,
        exec_per_second: float = None,
        execute_time: float = None,
        executions: float = None,
        fail_times: float = None,
        getplan_time: float = None,
        iowait_time: float = None,
        logical_read: float = None,
        max_cpu_time: float = None,
        max_elapsed_time: float = None,
        memstore_read_row_count: float = None,
        miss_plans: float = None,
        netwait_time: float = None,
        node_ip: str = None,
        queue_time: float = None,
        rpccount: float = None,
        remote_plans: float = None,
        retry_count: float = None,
        return_rows: float = None,
        row_cache_hit: float = None,
        schedule_time: float = None,
        sql_id: str = None,
        sql_type: str = None,
        ssstore_read_row_count: float = None,
        tenant_name: str = None,
        total_wait_time: float = None,
        user_name: str = None,
    ):
        self.affected_rows = affected_rows
        self.app_wait_time = app_wait_time
        self.block_cache_hit = block_cache_hit
        self.block_index_cache_hit = block_index_cache_hit
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        self.client_ip = client_ip
        self.concurrency_wait_time = concurrency_wait_time
        self.cpu_time = cpu_time
        self.db_name = db_name
        self.decode_time = decode_time
        self.disk_read = disk_read
        self.elapsed_time = elapsed_time
        self.end_time_utcstring = end_time_utcstring
        self.event = event
        self.exec_per_second = exec_per_second
        self.execute_time = execute_time
        self.executions = executions
        self.fail_times = fail_times
        self.getplan_time = getplan_time
        self.iowait_time = iowait_time
        self.logical_read = logical_read
        self.max_cpu_time = max_cpu_time
        self.max_elapsed_time = max_elapsed_time
        self.memstore_read_row_count = memstore_read_row_count
        self.miss_plans = miss_plans
        self.netwait_time = netwait_time
        self.node_ip = node_ip
        self.queue_time = queue_time
        self.rpccount = rpccount
        self.remote_plans = remote_plans
        self.retry_count = retry_count
        self.return_rows = return_rows
        self.row_cache_hit = row_cache_hit
        self.schedule_time = schedule_time
        self.sql_id = sql_id
        self.sql_type = sql_type
        self.ssstore_read_row_count = ssstore_read_row_count
        self.tenant_name = tenant_name
        self.total_wait_time = total_wait_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.end_time_utcstring is not None:
            result['EndTimeUTCString'] = self.end_time_utcstring
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.getplan_time is not None:
            result['GetplanTime'] = self.getplan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.netwait_time is not None:
            result['NetwaitTime'] = self.netwait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('EndTimeUTCString') is not None:
            self.end_time_utcstring = m.get('EndTimeUTCString')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetplanTime') is not None:
            self.getplan_time = m.get('GetplanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetwaitTime') is not None:
            self.netwait_time = m.get('NetwaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryList(TeaModel):
    def __init__(
        self,
        count: int = None,
        list: List[DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryListList] = None,
    ):
        self.count = count
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryListList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeSlowSQLHistoryListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        slow_sqlhistory_list: DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryList = None,
    ):
        self.request_id = request_id
        self.slow_sqlhistory_list = slow_sqlhistory_list

    def validate(self):
        if self.slow_sqlhistory_list:
            self.slow_sqlhistory_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slow_sqlhistory_list is not None:
            result['SlowSQLHistoryList'] = self.slow_sqlhistory_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlowSQLHistoryList') is not None:
            temp_model = DescribeSlowSQLHistoryListResponseBodySlowSQLHistoryList()
            self.slow_sqlhistory_list = temp_model.from_map(m['SlowSQLHistoryList'])
        return self


class DescribeSlowSQLHistoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlowSQLHistoryListResponseBody = None,
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
            temp_model = DescribeSlowSQLHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlowSQLListRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        filter_condition: Dict[str, Any] = None,
        node_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        search_key_word: str = None,
        search_parameter: str = None,
        search_rule: str = None,
        search_value: str = None,
        sort_column: str = None,
        sort_order: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition = filter_condition
        self.node_ip = node_ip
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.search_key_word = search_key_word
        self.search_parameter = search_parameter
        self.search_rule = search_rule
        self.search_value = search_value
        self.sort_column = sort_column
        self.sort_order = sort_order
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSlowSQLListShrinkRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        filter_condition_shrink: str = None,
        node_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        search_key_word: str = None,
        search_parameter: str = None,
        search_rule: str = None,
        search_value: str = None,
        sort_column: str = None,
        sort_order: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition_shrink = filter_condition_shrink
        self.node_ip = node_ip
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.search_key_word = search_key_word
        self.search_parameter = search_parameter
        self.search_rule = search_rule
        self.search_value = search_value
        self.sort_column = sort_column
        self.sort_order = sort_order
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition_shrink is not None:
            result['FilterCondition'] = self.filter_condition_shrink
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition_shrink = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSlowSQLListResponseBodySlowSQLList(TeaModel):
    def __init__(
        self,
        affected_rows: int = None,
        app_wait_time: float = None,
        block_cache_hit: int = None,
        block_index_cache_hit: int = None,
        bloom_filter_cache_hit: int = None,
        client_ip: str = None,
        concurrency_wait_time: float = None,
        cpu_time: float = None,
        db_name: str = None,
        decode_time: float = None,
        disk_read: int = None,
        elapsed_time: float = None,
        event: str = None,
        exec_per_second: float = None,
        execute_time: float = None,
        executions: int = None,
        fail_times: int = None,
        get_plan_time: float = None,
        iowait_time: float = None,
        key: int = None,
        logical_read: int = None,
        max_cpu_time: float = None,
        max_elapsed_time: float = None,
        memstore_read_row_count: int = None,
        miss_plans: int = None,
        net_wait_time: float = None,
        node_ip: str = None,
        queue_time: float = None,
        rpccount: int = None,
        remote_plans: int = None,
        retry_count: int = None,
        return_rows: int = None,
        row_cache_hit: int = None,
        sqlid: str = None,
        sqltext: str = None,
        sqltype: int = None,
        schedule_time: float = None,
        ssstore_read_row_count: int = None,
        total_wait_time: float = None,
        user_name: str = None,
    ):
        self.affected_rows = affected_rows
        self.app_wait_time = app_wait_time
        self.block_cache_hit = block_cache_hit
        self.block_index_cache_hit = block_index_cache_hit
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        self.client_ip = client_ip
        self.concurrency_wait_time = concurrency_wait_time
        self.cpu_time = cpu_time
        self.db_name = db_name
        self.decode_time = decode_time
        self.disk_read = disk_read
        self.elapsed_time = elapsed_time
        self.event = event
        self.exec_per_second = exec_per_second
        self.execute_time = execute_time
        self.executions = executions
        self.fail_times = fail_times
        self.get_plan_time = get_plan_time
        self.iowait_time = iowait_time
        self.key = key
        self.logical_read = logical_read
        self.max_cpu_time = max_cpu_time
        self.max_elapsed_time = max_elapsed_time
        self.memstore_read_row_count = memstore_read_row_count
        self.miss_plans = miss_plans
        self.net_wait_time = net_wait_time
        self.node_ip = node_ip
        self.queue_time = queue_time
        self.rpccount = rpccount
        self.remote_plans = remote_plans
        self.retry_count = retry_count
        self.return_rows = return_rows
        self.row_cache_hit = row_cache_hit
        self.sqlid = sqlid
        self.sqltext = sqltext
        self.sqltype = sqltype
        self.schedule_time = schedule_time
        self.ssstore_read_row_count = ssstore_read_row_count
        self.total_wait_time = total_wait_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.key is not None:
            result['Key'] = self.key
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeSlowSQLListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        slow_sqllist: List[DescribeSlowSQLListResponseBodySlowSQLList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.slow_sqllist = slow_sqllist
        self.total_count = total_count

    def validate(self):
        if self.slow_sqllist:
            for k in self.slow_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SlowSQLList'] = []
        if self.slow_sqllist is not None:
            for k in self.slow_sqllist:
                result['SlowSQLList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slow_sqllist = []
        if m.get('SlowSQLList') is not None:
            for k in m.get('SlowSQLList'):
                temp_model = DescribeSlowSQLListResponseBodySlowSQLList()
                self.slow_sqllist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSlowSQLListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSlowSQLListResponseBody = None,
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
            temp_model = DescribeSlowSQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTenantResponseBodyTenantTenantConnections(TeaModel):
    def __init__(
        self,
        connection_role: str = None,
        connection_zones: List[str] = None,
        internet_address: str = None,
        internet_address_status: str = None,
        internet_port: int = None,
        intranet_address: str = None,
        intranet_address_master_zone_id: str = None,
        intranet_address_slave_zone_id: str = None,
        intranet_address_status: str = None,
        intranet_port: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.connection_role = connection_role
        self.connection_zones = connection_zones
        self.internet_address = internet_address
        self.internet_address_status = internet_address_status
        self.internet_port = internet_port
        self.intranet_address = intranet_address
        self.intranet_address_master_zone_id = intranet_address_master_zone_id
        self.intranet_address_slave_zone_id = intranet_address_slave_zone_id
        self.intranet_address_status = intranet_address_status
        self.intranet_port = intranet_port
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_role is not None:
            result['ConnectionRole'] = self.connection_role
        if self.connection_zones is not None:
            result['ConnectionZones'] = self.connection_zones
        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address
        if self.internet_address_status is not None:
            result['InternetAddressStatus'] = self.internet_address_status
        if self.internet_port is not None:
            result['InternetPort'] = self.internet_port
        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address
        if self.intranet_address_master_zone_id is not None:
            result['IntranetAddressMasterZoneId'] = self.intranet_address_master_zone_id
        if self.intranet_address_slave_zone_id is not None:
            result['IntranetAddressSlaveZoneId'] = self.intranet_address_slave_zone_id
        if self.intranet_address_status is not None:
            result['IntranetAddressStatus'] = self.intranet_address_status
        if self.intranet_port is not None:
            result['IntranetPort'] = self.intranet_port
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionRole') is not None:
            self.connection_role = m.get('ConnectionRole')
        if m.get('ConnectionZones') is not None:
            self.connection_zones = m.get('ConnectionZones')
        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')
        if m.get('InternetAddressStatus') is not None:
            self.internet_address_status = m.get('InternetAddressStatus')
        if m.get('InternetPort') is not None:
            self.internet_port = m.get('InternetPort')
        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')
        if m.get('IntranetAddressMasterZoneId') is not None:
            self.intranet_address_master_zone_id = m.get('IntranetAddressMasterZoneId')
        if m.get('IntranetAddressSlaveZoneId') is not None:
            self.intranet_address_slave_zone_id = m.get('IntranetAddressSlaveZoneId')
        if m.get('IntranetAddressStatus') is not None:
            self.intranet_address_status = m.get('IntranetAddressStatus')
        if m.get('IntranetPort') is not None:
            self.intranet_port = m.get('IntranetPort')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeTenantResponseBodyTenantTenantResourceCpu(TeaModel):
    def __init__(
        self,
        total_cpu: float = None,
        unit_cpu: float = None,
        used_cpu: float = None,
    ):
        self.total_cpu = total_cpu
        self.unit_cpu = unit_cpu
        self.used_cpu = used_cpu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['TotalCpu'] = self.total_cpu
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.used_cpu is not None:
            result['UsedCpu'] = self.used_cpu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCpu') is not None:
            self.total_cpu = m.get('TotalCpu')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UsedCpu') is not None:
            self.used_cpu = m.get('UsedCpu')
        return self


class DescribeTenantResponseBodyTenantTenantResourceDiskSize(TeaModel):
    def __init__(
        self,
        used_disk_size: float = None,
    ):
        self.used_disk_size = used_disk_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        return self


class DescribeTenantResponseBodyTenantTenantResourceMemory(TeaModel):
    def __init__(
        self,
        total_memory: float = None,
        unit_memory: float = None,
        used_memory: float = None,
    ):
        self.total_memory = total_memory
        self.unit_memory = unit_memory
        self.used_memory = used_memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_memory is not None:
            result['TotalMemory'] = self.total_memory
        if self.unit_memory is not None:
            result['UnitMemory'] = self.unit_memory
        if self.used_memory is not None:
            result['UsedMemory'] = self.used_memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalMemory') is not None:
            self.total_memory = m.get('TotalMemory')
        if m.get('UnitMemory') is not None:
            self.unit_memory = m.get('UnitMemory')
        if m.get('UsedMemory') is not None:
            self.used_memory = m.get('UsedMemory')
        return self


class DescribeTenantResponseBodyTenantTenantResource(TeaModel):
    def __init__(
        self,
        cpu: DescribeTenantResponseBodyTenantTenantResourceCpu = None,
        disk_size: DescribeTenantResponseBodyTenantTenantResourceDiskSize = None,
        memory: DescribeTenantResponseBodyTenantTenantResourceMemory = None,
        unit_num: int = None,
    ):
        self.cpu = cpu
        self.disk_size = disk_size
        self.memory = memory
        self.unit_num = unit_num

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.disk_size:
            self.disk_size.validate()
        if self.memory:
            self.memory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size.to_map()
        if self.memory is not None:
            result['Memory'] = self.memory.to_map()
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResourceCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('DiskSize') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResourceDiskSize()
            self.disk_size = temp_model.from_map(m['DiskSize'])
        if m.get('Memory') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResourceMemory()
            self.memory = temp_model.from_map(m['Memory'])
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        return self


class DescribeTenantResponseBodyTenantTenantZones(TeaModel):
    def __init__(
        self,
        region: str = None,
        tenant_zone_id: str = None,
        tenant_zone_role: str = None,
    ):
        self.region = region
        self.tenant_zone_id = tenant_zone_id
        self.tenant_zone_role = tenant_zone_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.tenant_zone_id is not None:
            result['TenantZoneId'] = self.tenant_zone_id
        if self.tenant_zone_role is not None:
            result['TenantZoneRole'] = self.tenant_zone_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TenantZoneId') is not None:
            self.tenant_zone_id = m.get('TenantZoneId')
        if m.get('TenantZoneRole') is not None:
            self.tenant_zone_role = m.get('TenantZoneRole')
        return self


class DescribeTenantResponseBodyTenant(TeaModel):
    def __init__(
        self,
        charset: str = None,
        clog_service_status: str = None,
        collation: str = None,
        create_time: str = None,
        deploy_mode: str = None,
        deploy_type: str = None,
        description: str = None,
        enable_clog_service: bool = None,
        enable_internet_address_service: bool = None,
        master_intranet_address_zone: str = None,
        primary_zone: str = None,
        primary_zone_deploy_type: str = None,
        status: str = None,
        tenant_connections: List[DescribeTenantResponseBodyTenantTenantConnections] = None,
        tenant_id: str = None,
        tenant_mode: str = None,
        tenant_name: str = None,
        tenant_resource: DescribeTenantResponseBodyTenantTenantResource = None,
        tenant_zones: List[DescribeTenantResponseBodyTenantTenantZones] = None,
        vpc_id: str = None,
    ):
        self.charset = charset
        self.clog_service_status = clog_service_status
        self.collation = collation
        self.create_time = create_time
        self.deploy_mode = deploy_mode
        self.deploy_type = deploy_type
        self.description = description
        self.enable_clog_service = enable_clog_service
        self.enable_internet_address_service = enable_internet_address_service
        self.master_intranet_address_zone = master_intranet_address_zone
        self.primary_zone = primary_zone
        self.primary_zone_deploy_type = primary_zone_deploy_type
        self.status = status
        self.tenant_connections = tenant_connections
        self.tenant_id = tenant_id
        self.tenant_mode = tenant_mode
        self.tenant_name = tenant_name
        self.tenant_resource = tenant_resource
        self.tenant_zones = tenant_zones
        self.vpc_id = vpc_id

    def validate(self):
        if self.tenant_connections:
            for k in self.tenant_connections:
                if k:
                    k.validate()
        if self.tenant_resource:
            self.tenant_resource.validate()
        if self.tenant_zones:
            for k in self.tenant_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.clog_service_status is not None:
            result['ClogServiceStatus'] = self.clog_service_status
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_clog_service is not None:
            result['EnableClogService'] = self.enable_clog_service
        if self.enable_internet_address_service is not None:
            result['EnableInternetAddressService'] = self.enable_internet_address_service
        if self.master_intranet_address_zone is not None:
            result['MasterIntranetAddressZone'] = self.master_intranet_address_zone
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.primary_zone_deploy_type is not None:
            result['PrimaryZoneDeployType'] = self.primary_zone_deploy_type
        if self.status is not None:
            result['Status'] = self.status
        result['TenantConnections'] = []
        if self.tenant_connections is not None:
            for k in self.tenant_connections:
                result['TenantConnections'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.tenant_resource is not None:
            result['TenantResource'] = self.tenant_resource.to_map()
        result['TenantZones'] = []
        if self.tenant_zones is not None:
            for k in self.tenant_zones:
                result['TenantZones'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('ClogServiceStatus') is not None:
            self.clog_service_status = m.get('ClogServiceStatus')
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableClogService') is not None:
            self.enable_clog_service = m.get('EnableClogService')
        if m.get('EnableInternetAddressService') is not None:
            self.enable_internet_address_service = m.get('EnableInternetAddressService')
        if m.get('MasterIntranetAddressZone') is not None:
            self.master_intranet_address_zone = m.get('MasterIntranetAddressZone')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('PrimaryZoneDeployType') is not None:
            self.primary_zone_deploy_type = m.get('PrimaryZoneDeployType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tenant_connections = []
        if m.get('TenantConnections') is not None:
            for k in m.get('TenantConnections'):
                temp_model = DescribeTenantResponseBodyTenantTenantConnections()
                self.tenant_connections.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('TenantResource') is not None:
            temp_model = DescribeTenantResponseBodyTenantTenantResource()
            self.tenant_resource = temp_model.from_map(m['TenantResource'])
        self.tenant_zones = []
        if m.get('TenantZones') is not None:
            for k in m.get('TenantZones'):
                temp_model = DescribeTenantResponseBodyTenantTenantZones()
                self.tenant_zones.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeTenantResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant: DescribeTenantResponseBodyTenant = None,
    ):
        self.request_id = request_id
        self.tenant = tenant

    def validate(self):
        if self.tenant:
            self.tenant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant is not None:
            result['Tenant'] = self.tenant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tenant') is not None:
            temp_model = DescribeTenantResponseBodyTenant()
            self.tenant = temp_model.from_map(m['Tenant'])
        return self


class DescribeTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantResponseBody = None,
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
            temp_model = DescribeTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantMetricsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        metrics: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: str = None,
        tenant_id: str = None,
        tenant_id_list: str = None,
        tenant_name: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.metrics = metrics
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.tenant_id = tenant_id
        self.tenant_id_list = tenant_id_list
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.metrics is not None:
            result['Metrics'] = self.metrics
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_id_list is not None:
            result['TenantIdList'] = self.tenant_id_list
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantIdList') is not None:
            self.tenant_id_list = m.get('TenantIdList')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class DescribeTenantMetricsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_metrics: str = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tenant_metrics = tenant_metrics
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_metrics is not None:
            result['TenantMetrics'] = self.tenant_metrics
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantMetrics') is not None:
            self.tenant_metrics = m.get('TenantMetrics')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTenantMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantMetricsResponseBody = None,
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
            temp_model = DescribeTenantMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantUserRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role: List[str] = None,
    ):
        self.request_id = request_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class DescribeTenantUserRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantUserRolesResponseBody = None,
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
            temp_model = DescribeTenantUserRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantUsersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        tenant_id: str = None,
        user_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.tenant_id = tenant_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeTenantUsersResponseBodyTenantUsersDatabases(TeaModel):
    def __init__(
        self,
        database: str = None,
        role: str = None,
        table: str = None,
    ):
        self.database = database
        self.role = role
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.role is not None:
            result['Role'] = self.role
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeTenantUsersResponseBodyTenantUsers(TeaModel):
    def __init__(
        self,
        databases: List[DescribeTenantUsersResponseBodyTenantUsersDatabases] = None,
        description: str = None,
        user_name: str = None,
        user_status: str = None,
        user_type: str = None,
    ):
        self.databases = databases
        self.description = description
        self.user_name = user_name
        self.user_status = user_status
        self.user_type = user_type

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = DescribeTenantUsersResponseBodyTenantUsersDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeTenantUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_users: List[DescribeTenantUsersResponseBodyTenantUsers] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tenant_users = tenant_users
        self.total_count = total_count

    def validate(self):
        if self.tenant_users:
            for k in self.tenant_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantUsers'] = []
        if self.tenant_users is not None:
            for k in self.tenant_users:
                result['TenantUsers'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_users = []
        if m.get('TenantUsers') is not None:
            for k in m.get('TenantUsers'):
                temp_model = DescribeTenantUsersResponseBodyTenantUsers()
                self.tenant_users.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTenantUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantUsersResponseBody = None,
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
            temp_model = DescribeTenantUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantZonesReadRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTenantZonesReadResponseBodyTenantZones(TeaModel):
    def __init__(
        self,
        is_electable: bool = None,
        is_primary: bool = None,
        is_read_only_address_master: bool = None,
        is_readable: str = None,
        zone: str = None,
    ):
        self.is_electable = is_electable
        self.is_primary = is_primary
        self.is_read_only_address_master = is_read_only_address_master
        self.is_readable = is_readable
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_electable is not None:
            result['IsElectable'] = self.is_electable
        if self.is_primary is not None:
            result['IsPrimary'] = self.is_primary
        if self.is_read_only_address_master is not None:
            result['IsReadOnlyAddressMaster'] = self.is_read_only_address_master
        if self.is_readable is not None:
            result['IsReadable'] = self.is_readable
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsElectable') is not None:
            self.is_electable = m.get('IsElectable')
        if m.get('IsPrimary') is not None:
            self.is_primary = m.get('IsPrimary')
        if m.get('IsReadOnlyAddressMaster') is not None:
            self.is_read_only_address_master = m.get('IsReadOnlyAddressMaster')
        if m.get('IsReadable') is not None:
            self.is_readable = m.get('IsReadable')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeTenantZonesReadResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_zones: List[DescribeTenantZonesReadResponseBodyTenantZones] = None,
    ):
        self.request_id = request_id
        self.tenant_zones = tenant_zones

    def validate(self):
        if self.tenant_zones:
            for k in self.tenant_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantZones'] = []
        if self.tenant_zones is not None:
            for k in self.tenant_zones:
                result['TenantZones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_zones = []
        if m.get('TenantZones') is not None:
            for k in m.get('TenantZones'):
                temp_model = DescribeTenantZonesReadResponseBodyTenantZones()
                self.tenant_zones.append(temp_model.from_map(k))
        return self


class DescribeTenantZonesReadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantZonesReadResponseBody = None,
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
            temp_model = DescribeTenantZonesReadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class DescribeTenantsResponseBodyTenants(TeaModel):
    def __init__(
        self,
        charset: str = None,
        collation: str = None,
        cpu: int = None,
        create_time: str = None,
        deploy_mode: str = None,
        deploy_type: str = None,
        description: str = None,
        mem: int = None,
        primary_zone: str = None,
        status: str = None,
        tenant_id: str = None,
        tenant_mode: str = None,
        tenant_name: str = None,
        unit_cpu: int = None,
        unit_mem: int = None,
        unit_num: int = None,
        used_disk_size: float = None,
        vpc_id: str = None,
    ):
        self.charset = charset
        self.collation = collation
        self.cpu = cpu
        self.create_time = create_time
        self.deploy_mode = deploy_mode
        self.deploy_type = deploy_type
        self.description = description
        self.mem = mem
        self.primary_zone = primary_zone
        self.status = status
        self.tenant_id = tenant_id
        self.tenant_mode = tenant_mode
        self.tenant_name = tenant_name
        self.unit_cpu = unit_cpu
        self.unit_mem = unit_mem
        self.unit_num = unit_num
        self.used_disk_size = used_disk_size
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charset is not None:
            result['Charset'] = self.charset
        if self.collation is not None:
            result['Collation'] = self.collation
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_mode is not None:
            result['DeployMode'] = self.deploy_mode
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.mem is not None:
            result['Mem'] = self.mem
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.unit_cpu is not None:
            result['UnitCpu'] = self.unit_cpu
        if self.unit_mem is not None:
            result['UnitMem'] = self.unit_mem
        if self.unit_num is not None:
            result['UnitNum'] = self.unit_num
        if self.used_disk_size is not None:
            result['UsedDiskSize'] = self.used_disk_size
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Charset') is not None:
            self.charset = m.get('Charset')
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMode') is not None:
            self.deploy_mode = m.get('DeployMode')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UnitCpu') is not None:
            self.unit_cpu = m.get('UnitCpu')
        if m.get('UnitMem') is not None:
            self.unit_mem = m.get('UnitMem')
        if m.get('UnitNum') is not None:
            self.unit_num = m.get('UnitNum')
        if m.get('UsedDiskSize') is not None:
            self.used_disk_size = m.get('UsedDiskSize')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeTenantsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenants: List[DescribeTenantsResponseBodyTenants] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.tenants = tenants
        self.total_count = total_count

    def validate(self):
        if self.tenants:
            for k in self.tenants:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tenants'] = []
        if self.tenants is not None:
            for k in self.tenants:
                result['Tenants'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenants = []
        if m.get('Tenants') is not None:
            for k in m.get('Tenants'):
                temp_model = DescribeTenantsResponseBodyTenants()
                self.tenants.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTenantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantsResponseBody = None,
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
            temp_model = DescribeTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTimeZonesResponseBodyTimeZonesList(TeaModel):
    def __init__(
        self,
        description: str = None,
        time_zone: str = None,
    ):
        self.description = description
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        return self


class DescribeTimeZonesResponseBodyTimeZones(TeaModel):
    def __init__(
        self,
        default: str = None,
        list: List[DescribeTimeZonesResponseBodyTimeZonesList] = None,
    ):
        self.default = default
        self.list = list

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default is not None:
            result['Default'] = self.default
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = DescribeTimeZonesResponseBodyTimeZonesList()
                self.list.append(temp_model.from_map(k))
        return self


class DescribeTimeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_zones: DescribeTimeZonesResponseBodyTimeZones = None,
    ):
        self.request_id = request_id
        self.time_zones = time_zones

    def validate(self):
        if self.time_zones:
            self.time_zones.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_zones is not None:
            result['TimeZones'] = self.time_zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeZones') is not None:
            temp_model = DescribeTimeZonesResponseBodyTimeZones()
            self.time_zones = temp_model.from_map(m['TimeZones'])
        return self


class DescribeTimeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTimeZonesResponseBody = None,
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
            temp_model = DescribeTimeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopSQLListRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        filter_condition: Dict[str, Any] = None,
        node_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        search_key_word: str = None,
        search_parameter: str = None,
        search_rule: str = None,
        search_value: str = None,
        sort_column: str = None,
        sort_order: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition = filter_condition
        self.node_ip = node_ip
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.search_key_word = search_key_word
        self.search_parameter = search_parameter
        self.search_rule = search_rule
        self.search_value = search_value
        self.sort_column = sort_column
        self.sort_order = sort_order
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTopSQLListShrinkRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        filter_condition_shrink: str = None,
        node_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        sqlid: str = None,
        search_key_word: str = None,
        search_parameter: str = None,
        search_rule: str = None,
        search_value: str = None,
        sort_column: str = None,
        sort_order: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition_shrink = filter_condition_shrink
        self.node_ip = node_ip
        self.page_number = page_number
        self.page_size = page_size
        self.sqlid = sqlid
        self.search_key_word = search_key_word
        self.search_parameter = search_parameter
        self.search_rule = search_rule
        self.search_value = search_value
        self.sort_column = sort_column
        self.sort_order = sort_order
        self.start_time = start_time
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition_shrink is not None:
            result['FilterCondition'] = self.filter_condition_shrink
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_parameter is not None:
            result['SearchParameter'] = self.search_parameter
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sort_column is not None:
            result['SortColumn'] = self.sort_column
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition_shrink = m.get('FilterCondition')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParameter') is not None:
            self.search_parameter = m.get('SearchParameter')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SortColumn') is not None:
            self.sort_column = m.get('SortColumn')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTopSQLListResponseBodyTopSQLList(TeaModel):
    def __init__(
        self,
        affected_rows: int = None,
        app_wait_time: float = None,
        block_cache_hit: int = None,
        block_index_cache_hit: int = None,
        bloom_filter_cache_hit: int = None,
        client_ip: str = None,
        concurrency_wait_time: float = None,
        cpu_time: float = None,
        db_name: str = None,
        decode_time: float = None,
        disk_read: int = None,
        elapsed_time: float = None,
        event: str = None,
        exec_per_second: float = None,
        execute_time: float = None,
        executions: int = None,
        fail_times: int = None,
        get_plan_time: float = None,
        iowait_time: float = None,
        key: int = None,
        logical_read: int = None,
        max_cpu_time: float = None,
        max_elapsed_time: float = None,
        memstore_read_row_count: int = None,
        miss_plans: int = None,
        net_wait_time: float = None,
        node_ip: str = None,
        queue_time: float = None,
        rpccount: int = None,
        remote_plans: int = None,
        retry_count: int = None,
        return_rows: int = None,
        row_cache_hit: int = None,
        sqlid: str = None,
        sqltext: str = None,
        sqltype: int = None,
        schedule_time: float = None,
        ssstore_read_row_count: int = None,
        total_wait_time: float = None,
        user_name: str = None,
    ):
        self.affected_rows = affected_rows
        self.app_wait_time = app_wait_time
        self.block_cache_hit = block_cache_hit
        self.block_index_cache_hit = block_index_cache_hit
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        self.client_ip = client_ip
        self.concurrency_wait_time = concurrency_wait_time
        self.cpu_time = cpu_time
        self.db_name = db_name
        self.decode_time = decode_time
        self.disk_read = disk_read
        self.elapsed_time = elapsed_time
        self.event = event
        self.exec_per_second = exec_per_second
        self.execute_time = execute_time
        self.executions = executions
        self.fail_times = fail_times
        self.get_plan_time = get_plan_time
        self.iowait_time = iowait_time
        self.key = key
        self.logical_read = logical_read
        self.max_cpu_time = max_cpu_time
        self.max_elapsed_time = max_elapsed_time
        self.memstore_read_row_count = memstore_read_row_count
        self.miss_plans = miss_plans
        self.net_wait_time = net_wait_time
        self.node_ip = node_ip
        self.queue_time = queue_time
        self.rpccount = rpccount
        self.remote_plans = remote_plans
        self.retry_count = retry_count
        self.return_rows = return_rows
        self.row_cache_hit = row_cache_hit
        self.sqlid = sqlid
        self.sqltext = sqltext
        self.sqltype = sqltype
        self.schedule_time = schedule_time
        self.ssstore_read_row_count = ssstore_read_row_count
        self.total_wait_time = total_wait_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.app_wait_time is not None:
            result['AppWaitTime'] = self.app_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_read is not None:
            result['DiskRead'] = self.disk_read
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.event is not None:
            result['Event'] = self.event
        if self.exec_per_second is not None:
            result['ExecPerSecond'] = self.exec_per_second
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_times is not None:
            result['FailTimes'] = self.fail_times
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.iowait_time is not None:
            result['IOWaitTime'] = self.iowait_time
        if self.key is not None:
            result['Key'] = self.key
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.memstore_read_row_count is not None:
            result['MemstoreReadRowCount'] = self.memstore_read_row_count
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.rpccount is not None:
            result['RPCCount'] = self.rpccount
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.sqltext is not None:
            result['SQLText'] = self.sqltext
        if self.sqltype is not None:
            result['SQLType'] = self.sqltype
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.ssstore_read_row_count is not None:
            result['SsstoreReadRowCount'] = self.ssstore_read_row_count
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('AppWaitTime') is not None:
            self.app_wait_time = m.get('AppWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskRead') is not None:
            self.disk_read = m.get('DiskRead')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('ExecPerSecond') is not None:
            self.exec_per_second = m.get('ExecPerSecond')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailTimes') is not None:
            self.fail_times = m.get('FailTimes')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('IOWaitTime') is not None:
            self.iowait_time = m.get('IOWaitTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MemstoreReadRowCount') is not None:
            self.memstore_read_row_count = m.get('MemstoreReadRowCount')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RPCCount') is not None:
            self.rpccount = m.get('RPCCount')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')
        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('SsstoreReadRowCount') is not None:
            self.ssstore_read_row_count = m.get('SsstoreReadRowCount')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeTopSQLListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        top_sqllist: List[DescribeTopSQLListResponseBodyTopSQLList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.top_sqllist = top_sqllist
        self.total_count = total_count

    def validate(self):
        if self.top_sqllist:
            for k in self.top_sqllist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TopSQLList'] = []
        if self.top_sqllist is not None:
            for k in self.top_sqllist:
                result['TopSQLList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.top_sqllist = []
        if m.get('TopSQLList') is not None:
            for k in m.get('TopSQLList'):
                temp_model = DescribeTopSQLListResponseBodyTopSQLList()
                self.top_sqllist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTopSQLListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTopSQLListResponseBody = None,
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
            temp_model = DescribeTopSQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        deploy_type: str = None,
        series: str = None,
    ):
        self.deploy_type = deploy_type
        self.series = series

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.series is not None:
            result['Series'] = self.series
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        deploy_type: str = None,
        series: str = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        self.deploy_type = deploy_type
        self.series = series
        self.zone_id = zone_id
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.series is not None:
            result['Series'] = self.series
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[DescribeZonesResponseBodyZones] = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseDescriptionRequest(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        description: str = None,
        instance_id: str = None,
        tenant_id: str = None,
    ):
        self.database_name = database_name
        self.description = description
        self.instance_id = instance_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyDatabaseDescriptionResponseBody(TeaModel):
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


class ModifyDatabaseDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseDescriptionResponseBody = None,
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
            temp_model = ModifyDatabaseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseUserRolesRequest(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        instance_id: str = None,
        tenant_id: str = None,
        users: str = None,
    ):
        self.database_name = database_name
        self.instance_id = instance_id
        self.tenant_id = tenant_id
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ModifyDatabaseUserRolesResponseBodyTenantUserUsers(TeaModel):
    def __init__(
        self,
        role: str = None,
        user_name: str = None,
    ):
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyDatabaseUserRolesResponseBodyTenantUser(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        tenant_id: str = None,
        users: List[ModifyDatabaseUserRolesResponseBodyTenantUserUsers] = None,
    ):
        self.database_name = database_name
        self.tenant_id = tenant_id
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ModifyDatabaseUserRolesResponseBodyTenantUserUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ModifyDatabaseUserRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_user: ModifyDatabaseUserRolesResponseBodyTenantUser = None,
    ):
        self.request_id = request_id
        self.tenant_user = tenant_user

    def validate(self):
        if self.tenant_user:
            self.tenant_user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_user is not None:
            result['TenantUser'] = self.tenant_user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantUser') is not None:
            temp_model = ModifyDatabaseUserRolesResponseBodyTenantUser()
            self.tenant_user = temp_model.from_map(m['TenantUser'])
        return self


class ModifyDatabaseUserRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseUserRolesResponseBody = None,
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
            temp_model = ModifyDatabaseUserRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNameRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class ModifyInstanceNameResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceNameResponseBody = None,
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
            temp_model = ModifyInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParametersRequest(TeaModel):
    def __init__(
        self,
        dimension: str = None,
        dimension_value: str = None,
        instance_id: str = None,
        parameters: str = None,
    ):
        self.dimension = dimension
        self.dimension_value = dimension_value
        self.instance_id = instance_id
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimension is not None:
            result['Dimension'] = self.dimension
        if self.dimension_value is not None:
            result['DimensionValue'] = self.dimension_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')
        if m.get('DimensionValue') is not None:
            self.dimension_value = m.get('DimensionValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class ModifyParametersResponseBodyResults(TeaModel):
    def __init__(
        self,
        message: str = None,
        success: bool = None,
    ):
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyParametersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        results: ModifyParametersResponseBodyResults = None,
    ):
        self.request_id = request_id
        self.results = results

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.results is not None:
            result['Results'] = self.results.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Results') is not None:
            temp_model = ModifyParametersResponseBodyResults()
            self.results = temp_model.from_map(m['Results'])
        return self


class ModifyParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyParametersResponseBody = None,
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
            temp_model = ModifyParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIpsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifySecurityIpsResponseBodySecurityIpGroup(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        return self


class ModifySecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_group: ModifySecurityIpsResponseBodySecurityIpGroup = None,
    ):
        self.request_id = request_id
        self.security_ip_group = security_ip_group

    def validate(self):
        if self.security_ip_group:
            self.security_ip_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_ip_group is not None:
            result['SecurityIpGroup'] = self.security_ip_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIpGroup') is not None:
            temp_model = ModifySecurityIpsResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class ModifySecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecurityIpsResponseBody = None,
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
            temp_model = ModifySecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantPrimaryZoneRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        master_intranet_address_zone: str = None,
        modify_type: str = None,
        primary_zone: str = None,
        primary_zone_deploy_type: str = None,
        tenant_id: str = None,
        user_vswitch_id: str = None,
    ):
        self.instance_id = instance_id
        self.master_intranet_address_zone = master_intranet_address_zone
        self.modify_type = modify_type
        self.primary_zone = primary_zone
        self.primary_zone_deploy_type = primary_zone_deploy_type
        self.tenant_id = tenant_id
        self.user_vswitch_id = user_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.master_intranet_address_zone is not None:
            result['MasterIntranetAddressZone'] = self.master_intranet_address_zone
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.primary_zone_deploy_type is not None:
            result['PrimaryZoneDeployType'] = self.primary_zone_deploy_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_vswitch_id is not None:
            result['UserVSwitchId'] = self.user_vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MasterIntranetAddressZone') is not None:
            self.master_intranet_address_zone = m.get('MasterIntranetAddressZone')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('PrimaryZoneDeployType') is not None:
            self.primary_zone_deploy_type = m.get('PrimaryZoneDeployType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserVSwitchId') is not None:
            self.user_vswitch_id = m.get('UserVSwitchId')
        return self


class ModifyTenantPrimaryZoneResponseBody(TeaModel):
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


class ModifyTenantPrimaryZoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantPrimaryZoneResponseBody = None,
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
            temp_model = ModifyTenantPrimaryZoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantResourceRequest(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        instance_id: str = None,
        memory: int = None,
        tenant_id: str = None,
    ):
        self.cpu = cpu
        self.instance_id = instance_id
        self.memory = memory
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_id: str = None,
    ):
        self.request_id = request_id
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantResourceResponseBody = None,
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
            temp_model = ModifyTenantResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserDescriptionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        tenant_id: str = None,
        user_name: str = None,
    ):
        self.description = description
        self.instance_id = instance_id
        self.tenant_id = tenant_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyTenantUserDescriptionResponseBody(TeaModel):
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


class ModifyTenantUserDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantUserDescriptionResponseBody = None,
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
            temp_model = ModifyTenantUserDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserPasswordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: str = None,
        user_name: str = None,
        user_password: str = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.user_password = user_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_password is not None:
            result['UserPassword'] = self.user_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserPassword') is not None:
            self.user_password = m.get('UserPassword')
        return self


class ModifyTenantUserPasswordResponseBody(TeaModel):
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


class ModifyTenantUserPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantUserPasswordResponseBody = None,
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
            temp_model = ModifyTenantUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserRolesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        modify_type: str = None,
        tenant_id: str = None,
        user_name: str = None,
        user_role: str = None,
    ):
        self.instance_id = instance_id
        self.modify_type = modify_type
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.user_role = user_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_role is not None:
            result['UserRole'] = self.user_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')
        return self


class ModifyTenantUserRolesResponseBodyTenantUserUserRole(TeaModel):
    def __init__(
        self,
        database: str = None,
        is_success: bool = None,
        role: str = None,
        table: str = None,
    ):
        self.database = database
        self.is_success = is_success
        self.role = role
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.role is not None:
            result['Role'] = self.role
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class ModifyTenantUserRolesResponseBodyTenantUser(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
        user_name: str = None,
        user_role: List[ModifyTenantUserRolesResponseBodyTenantUserUserRole] = None,
    ):
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.user_role = user_role

    def validate(self):
        if self.user_role:
            for k in self.user_role:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        result['UserRole'] = []
        if self.user_role is not None:
            for k in self.user_role:
                result['UserRole'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        self.user_role = []
        if m.get('UserRole') is not None:
            for k in m.get('UserRole'):
                temp_model = ModifyTenantUserRolesResponseBodyTenantUserUserRole()
                self.user_role.append(temp_model.from_map(k))
        return self


class ModifyTenantUserRolesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_user: ModifyTenantUserRolesResponseBodyTenantUser = None,
    ):
        self.request_id = request_id
        self.tenant_user = tenant_user

    def validate(self):
        if self.tenant_user:
            self.tenant_user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_user is not None:
            result['TenantUser'] = self.tenant_user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantUser') is not None:
            temp_model = ModifyTenantUserRolesResponseBodyTenantUser()
            self.tenant_user = temp_model.from_map(m['TenantUser'])
        return self


class ModifyTenantUserRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantUserRolesResponseBody = None,
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
            temp_model = ModifyTenantUserRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantUserStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: str = None,
        user_name: str = None,
        user_status: str = None,
    ):
        self.instance_id = instance_id
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class ModifyTenantUserStatusResponseBodyTenantUser(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
        user_name: str = None,
        user_status: str = None,
    ):
        self.tenant_id = tenant_id
        self.user_name = user_name
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class ModifyTenantUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_user: List[ModifyTenantUserStatusResponseBodyTenantUser] = None,
    ):
        self.request_id = request_id
        self.tenant_user = tenant_user

    def validate(self):
        if self.tenant_user:
            for k in self.tenant_user:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TenantUser'] = []
        if self.tenant_user is not None:
            for k in self.tenant_user:
                result['TenantUser'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tenant_user = []
        if m.get('TenantUser') is not None:
            for k in m.get('TenantUser'):
                temp_model = ModifyTenantUserStatusResponseBodyTenantUser()
                self.tenant_user.append(temp_model.from_map(k))
        return self


class ModifyTenantUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantUserStatusResponseBody = None,
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
            temp_model = ModifyTenantUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class ReleaseOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class ReleaseOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: bool = None,
        error_detail: ReleaseOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = ReleaseOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ReleaseOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseOmsOpenAPIProjectResponseBody = None,
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
            temp_model = ReleaseOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class ResetOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class ResetOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: bool = None,
        error_detail: ResetOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = ResetOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ResetOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetOmsOpenAPIProjectResponseBody = None,
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
            temp_model = ResetOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class ResumeOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class ResumeOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: bool = None,
        error_detail: ResumeOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = ResumeOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ResumeOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResumeOmsOpenAPIProjectResponseBody = None,
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
            temp_model = ResumeOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchOmsOpenAPIMonitorMetricRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        max_point_num: int = None,
        metric: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.max_point_num = max_point_num
        self.metric = metric
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_point_num is not None:
            result['MaxPointNum'] = self.max_point_num
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxPointNum') is not None:
            self.max_point_num = m.get('MaxPointNum')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class SearchOmsOpenAPIMonitorMetricResponseBodyDataDataPoints(TeaModel):
    def __init__(
        self,
        timestamp: int = None,
        value: float = None,
    ):
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchOmsOpenAPIMonitorMetricResponseBodyData(TeaModel):
    def __init__(
        self,
        data_points: List[SearchOmsOpenAPIMonitorMetricResponseBodyDataDataPoints] = None,
        metric: str = None,
        tags: Dict[str, str] = None,
    ):
        self.data_points = data_points
        self.metric = metric
        self.tags = tags

    def validate(self):
        if self.data_points:
            for k in self.data_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataPoints'] = []
        if self.data_points is not None:
            for k in self.data_points:
                result['DataPoints'].append(k.to_map() if k else None)
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_points = []
        if m.get('DataPoints') is not None:
            for k in m.get('DataPoints'):
                temp_model = SearchOmsOpenAPIMonitorMetricResponseBodyDataDataPoints()
                self.data_points.append(temp_model.from_map(k))
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class SearchOmsOpenAPIMonitorMetricResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class SearchOmsOpenAPIMonitorMetricResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: List[SearchOmsOpenAPIMonitorMetricResponseBodyData] = None,
        error_detail: SearchOmsOpenAPIMonitorMetricResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchOmsOpenAPIMonitorMetricResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorDetail') is not None:
            temp_model = SearchOmsOpenAPIMonitorMetricResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchOmsOpenAPIMonitorMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchOmsOpenAPIMonitorMetricResponseBody = None,
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
            temp_model = SearchOmsOpenAPIMonitorMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchOmsOpenAPIProjectsRequest(TeaModel):
    def __init__(
        self,
        dest_db_types: List[str] = None,
        label_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        source_db_types: List[str] = None,
        status_list: List[str] = None,
        worker_grade_id: str = None,
    ):
        self.dest_db_types = dest_db_types
        self.label_ids = label_ids
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.source_db_types = source_db_types
        self.status_list = status_list
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_db_types is not None:
            result['DestDbTypes'] = self.dest_db_types
        if self.label_ids is not None:
            result['LabelIds'] = self.label_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.source_db_types is not None:
            result['SourceDbTypes'] = self.source_db_types
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestDbTypes') is not None:
            self.dest_db_types = m.get('DestDbTypes')
        if m.get('LabelIds') is not None:
            self.label_ids = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SourceDbTypes') is not None:
            self.source_db_types = m.get('SourceDbTypes')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class SearchOmsOpenAPIProjectsShrinkRequest(TeaModel):
    def __init__(
        self,
        dest_db_types_shrink: str = None,
        label_ids_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
        source_db_types_shrink: str = None,
        status_list_shrink: str = None,
        worker_grade_id: str = None,
    ):
        self.dest_db_types_shrink = dest_db_types_shrink
        self.label_ids_shrink = label_ids_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key
        self.source_db_types_shrink = source_db_types_shrink
        self.status_list_shrink = status_list_shrink
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_db_types_shrink is not None:
            result['DestDbTypes'] = self.dest_db_types_shrink
        if self.label_ids_shrink is not None:
            result['LabelIds'] = self.label_ids_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.source_db_types_shrink is not None:
            result['SourceDbTypes'] = self.source_db_types_shrink
        if self.status_list_shrink is not None:
            result['StatusList'] = self.status_list_shrink
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestDbTypes') is not None:
            self.dest_db_types_shrink = m.get('DestDbTypes')
        if m.get('LabelIds') is not None:
            self.label_ids_shrink = m.get('LabelIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('SourceDbTypes') is not None:
            self.source_db_types_shrink = m.get('SourceDbTypes')
        if m.get('StatusList') is not None:
            self.status_list_shrink = m.get('StatusList')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataDestConfig(TeaModel):
    def __init__(
        self,
        enable_msg_trace: bool = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        msg_tags: str = None,
        partition: int = None,
        partition_mode: str = None,
        producer_group: str = None,
        send_msg_timeout: int = None,
        sequence_enable: bool = None,
        sequence_start_timestamp: int = None,
        serializer_type: str = None,
        topic_type: str = None,
    ):
        self.enable_msg_trace = enable_msg_trace
        self.endpoint_id = endpoint_id
        self.endpoint_type = endpoint_type
        self.msg_tags = msg_tags
        self.partition = partition
        self.partition_mode = partition_mode
        self.producer_group = producer_group
        self.send_msg_timeout = send_msg_timeout
        self.sequence_enable = sequence_enable
        self.sequence_start_timestamp = sequence_start_timestamp
        self.serializer_type = serializer_type
        self.topic_type = topic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataLabels(TeaModel):
    def __init__(
        self,
        count: int = None,
        creator: str = None,
        id: str = None,
        name: str = None,
    ):
        self.count = count
        self.creator = creator
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataSourceConfig(TeaModel):
    def __init__(
        self,
        enable_msg_trace: bool = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        msg_tags: str = None,
        partition: int = None,
        partition_mode: str = None,
        producer_group: str = None,
        send_msg_timeout: int = None,
        sequence_enable: bool = None,
        sequence_start_timestamp: int = None,
        serializer_type: str = None,
        topic_type: str = None,
    ):
        self.enable_msg_trace = enable_msg_trace
        self.endpoint_id = endpoint_id
        self.endpoint_type = endpoint_type
        self.msg_tags = msg_tags
        self.partition = partition
        self.partition_mode = partition_mode
        self.producer_group = producer_group
        self.send_msg_timeout = send_msg_timeout
        self.sequence_enable = sequence_enable
        self.sequence_start_timestamp = sequence_start_timestamp
        self.serializer_type = serializer_type
        self.topic_type = topic_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_msg_trace is not None:
            result['EnableMsgTrace'] = self.enable_msg_trace
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.msg_tags is not None:
            result['MsgTags'] = self.msg_tags
        if self.partition is not None:
            result['Partition'] = self.partition
        if self.partition_mode is not None:
            result['PartitionMode'] = self.partition_mode
        if self.producer_group is not None:
            result['ProducerGroup'] = self.producer_group
        if self.send_msg_timeout is not None:
            result['SendMsgTimeout'] = self.send_msg_timeout
        if self.sequence_enable is not None:
            result['SequenceEnable'] = self.sequence_enable
        if self.sequence_start_timestamp is not None:
            result['SequenceStartTimestamp'] = self.sequence_start_timestamp
        if self.serializer_type is not None:
            result['SerializerType'] = self.serializer_type
        if self.topic_type is not None:
            result['TopicType'] = self.topic_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableMsgTrace') is not None:
            self.enable_msg_trace = m.get('EnableMsgTrace')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MsgTags') is not None:
            self.msg_tags = m.get('MsgTags')
        if m.get('Partition') is not None:
            self.partition = m.get('Partition')
        if m.get('PartitionMode') is not None:
            self.partition_mode = m.get('PartitionMode')
        if m.get('ProducerGroup') is not None:
            self.producer_group = m.get('ProducerGroup')
        if m.get('SendMsgTimeout') is not None:
            self.send_msg_timeout = m.get('SendMsgTimeout')
        if m.get('SequenceEnable') is not None:
            self.sequence_enable = m.get('SequenceEnable')
        if m.get('SequenceStartTimestamp') is not None:
            self.sequence_start_timestamp = m.get('SequenceStartTimestamp')
        if m.get('SerializerType') is not None:
            self.serializer_type = m.get('SerializerType')
        if m.get('TopicType') is not None:
            self.topic_type = m.get('TopicType')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfoErrorDetails(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfo(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_details: List[SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfoErrorDetails] = None,
        error_msg: str = None,
        error_param: Dict[str, str] = None,
        failed_time: str = None,
    ):
        self.error_code = error_code
        self.error_details = error_details
        self.error_msg = error_msg
        self.error_param = error_param
        self.failed_time = failed_time

    def validate(self):
        if self.error_details:
            for k in self.error_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k in self.error_details:
                result['ErrorDetails'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.error_param is not None:
            result['ErrorParam'] = self.error_param
        if self.failed_time is not None:
            result['FailedTime'] = self.failed_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k in m.get('ErrorDetails'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfoErrorDetails()
                self.error_details.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ErrorParam') is not None:
            self.error_param = m.get('ErrorParam')
        if m.get('FailedTime') is not None:
            self.failed_time = m.get('FailedTime')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfoConnectorFullProgressOverview(TeaModel):
    def __init__(
        self,
        estimated_remaining_time_of_sec: int = None,
        estimated_total_count: int = None,
        finished_count: int = None,
        progress: int = None,
    ):
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec
        self.estimated_total_count = estimated_total_count
        self.finished_count = finished_count
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_time_of_sec is not None:
            result['EstimatedRemainingTimeOfSec'] = self.estimated_remaining_time_of_sec
        if self.estimated_total_count is not None:
            result['EstimatedTotalCount'] = self.estimated_total_count
        if self.finished_count is not None:
            result['FinishedCount'] = self.finished_count
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedRemainingTimeOfSec') is not None:
            self.estimated_remaining_time_of_sec = m.get('EstimatedRemainingTimeOfSec')
        if m.get('EstimatedTotalCount') is not None:
            self.estimated_total_count = m.get('EstimatedTotalCount')
        if m.get('FinishedCount') is not None:
            self.finished_count = m.get('FinishedCount')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfo(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        checkpoint: str = None,
        connector_full_progress_overview: SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfoConnectorFullProgressOverview = None,
        deploy_id: str = None,
        dst_iops: int = None,
        dst_rps: int = None,
        dst_rps_ref: int = None,
        dst_rt: int = None,
        dst_rt_ref: int = None,
        gmt: int = None,
        inconsistencies: int = None,
        incr_timestamp_checkpoint: int = None,
        job_id: str = None,
        processed_records: int = None,
        skipped: bool = None,
        src_iops: int = None,
        src_iops_ref: int = None,
        src_rps: int = None,
        src_rps_ref: int = None,
        src_rt: int = None,
        src_rt_ref: int = None,
        validated: bool = None,
    ):
        self.capacity = capacity
        self.checkpoint = checkpoint
        self.connector_full_progress_overview = connector_full_progress_overview
        self.deploy_id = deploy_id
        self.dst_iops = dst_iops
        self.dst_rps = dst_rps
        self.dst_rps_ref = dst_rps_ref
        self.dst_rt = dst_rt
        self.dst_rt_ref = dst_rt_ref
        self.gmt = gmt
        self.inconsistencies = inconsistencies
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint
        self.job_id = job_id
        self.processed_records = processed_records
        self.skipped = skipped
        self.src_iops = src_iops
        self.src_iops_ref = src_iops_ref
        self.src_rps = src_rps
        self.src_rps_ref = src_rps_ref
        self.src_rt = src_rt
        self.src_rt_ref = src_rt_ref
        self.validated = validated

    def validate(self):
        if self.connector_full_progress_overview:
            self.connector_full_progress_overview.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.connector_full_progress_overview is not None:
            result['ConnectorFullProgressOverview'] = self.connector_full_progress_overview.to_map()
        if self.deploy_id is not None:
            result['DeployId'] = self.deploy_id
        if self.dst_iops is not None:
            result['DstIops'] = self.dst_iops
        if self.dst_rps is not None:
            result['DstRps'] = self.dst_rps
        if self.dst_rps_ref is not None:
            result['DstRpsRef'] = self.dst_rps_ref
        if self.dst_rt is not None:
            result['DstRt'] = self.dst_rt
        if self.dst_rt_ref is not None:
            result['DstRtRef'] = self.dst_rt_ref
        if self.gmt is not None:
            result['Gmt'] = self.gmt
        if self.inconsistencies is not None:
            result['Inconsistencies'] = self.inconsistencies
        if self.incr_timestamp_checkpoint is not None:
            result['IncrTimestampCheckpoint'] = self.incr_timestamp_checkpoint
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.processed_records is not None:
            result['ProcessedRecords'] = self.processed_records
        if self.skipped is not None:
            result['Skipped'] = self.skipped
        if self.src_iops is not None:
            result['SrcIops'] = self.src_iops
        if self.src_iops_ref is not None:
            result['SrcIopsRef'] = self.src_iops_ref
        if self.src_rps is not None:
            result['SrcRps'] = self.src_rps
        if self.src_rps_ref is not None:
            result['SrcRpsRef'] = self.src_rps_ref
        if self.src_rt is not None:
            result['SrcRt'] = self.src_rt
        if self.src_rt_ref is not None:
            result['SrcRtRef'] = self.src_rt_ref
        if self.validated is not None:
            result['Validated'] = self.validated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('ConnectorFullProgressOverview') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfoConnectorFullProgressOverview()
            self.connector_full_progress_overview = temp_model.from_map(m['ConnectorFullProgressOverview'])
        if m.get('DeployId') is not None:
            self.deploy_id = m.get('DeployId')
        if m.get('DstIops') is not None:
            self.dst_iops = m.get('DstIops')
        if m.get('DstRps') is not None:
            self.dst_rps = m.get('DstRps')
        if m.get('DstRpsRef') is not None:
            self.dst_rps_ref = m.get('DstRpsRef')
        if m.get('DstRt') is not None:
            self.dst_rt = m.get('DstRt')
        if m.get('DstRtRef') is not None:
            self.dst_rt_ref = m.get('DstRtRef')
        if m.get('Gmt') is not None:
            self.gmt = m.get('Gmt')
        if m.get('Inconsistencies') is not None:
            self.inconsistencies = m.get('Inconsistencies')
        if m.get('IncrTimestampCheckpoint') is not None:
            self.incr_timestamp_checkpoint = m.get('IncrTimestampCheckpoint')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProcessedRecords') is not None:
            self.processed_records = m.get('ProcessedRecords')
        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')
        if m.get('SrcIops') is not None:
            self.src_iops = m.get('SrcIops')
        if m.get('SrcIopsRef') is not None:
            self.src_iops_ref = m.get('SrcIopsRef')
        if m.get('SrcRps') is not None:
            self.src_rps = m.get('SrcRps')
        if m.get('SrcRpsRef') is not None:
            self.src_rps_ref = m.get('SrcRpsRef')
        if m.get('SrcRt') is not None:
            self.src_rt = m.get('SrcRt')
        if m.get('SrcRtRef') is not None:
            self.src_rt_ref = m.get('SrcRtRef')
        if m.get('Validated') is not None:
            self.validated = m.get('Validated')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataSteps(TeaModel):
    def __init__(
        self,
        estimated_remaining_seconds: int = None,
        extra_info: SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfo = None,
        finish_time: str = None,
        interactive: bool = None,
        start_time: str = None,
        step_description: str = None,
        step_info: SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfo = None,
        step_name: str = None,
        step_order: int = None,
        step_progress: int = None,
        step_status: str = None,
    ):
        self.estimated_remaining_seconds = estimated_remaining_seconds
        self.extra_info = extra_info
        self.finish_time = finish_time
        self.interactive = interactive
        self.start_time = start_time
        self.step_description = step_description
        self.step_info = step_info
        self.step_name = step_name
        self.step_order = step_order
        self.step_progress = step_progress
        self.step_status = step_status

    def validate(self):
        if self.extra_info:
            self.extra_info.validate()
        if self.step_info:
            self.step_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_remaining_seconds is not None:
            result['EstimatedRemainingSeconds'] = self.estimated_remaining_seconds
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info.to_map()
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.interactive is not None:
            result['Interactive'] = self.interactive
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_description is not None:
            result['StepDescription'] = self.step_description
        if self.step_info is not None:
            result['StepInfo'] = self.step_info.to_map()
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_order is not None:
            result['StepOrder'] = self.step_order
        if self.step_progress is not None:
            result['StepProgress'] = self.step_progress
        if self.step_status is not None:
            result['StepStatus'] = self.step_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedRemainingSeconds') is not None:
            self.estimated_remaining_seconds = m.get('EstimatedRemainingSeconds')
        if m.get('ExtraInfo') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsExtraInfo()
            self.extra_info = temp_model.from_map(m['ExtraInfo'])
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Interactive') is not None:
            self.interactive = m.get('Interactive')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepDescription') is not None:
            self.step_description = m.get('StepDescription')
        if m.get('StepInfo') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataStepsStepInfo()
            self.step_info = temp_model.from_map(m['StepInfo'])
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepOrder') is not None:
            self.step_order = m.get('StepOrder')
        if m.get('StepProgress') is not None:
            self.step_progress = m.get('StepProgress')
        if m.get('StepStatus') is not None:
            self.step_status = m.get('StepStatus')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema(TeaModel):
    def __init__(
        self,
        distributed_keys: List[str] = None,
        partition_life_cycle: int = None,
        partition_statement: str = None,
        primary_keys: List[str] = None,
    ):
        self.distributed_keys = distributed_keys
        self.partition_life_cycle = partition_life_cycle
        self.partition_statement = partition_statement
        self.primary_keys = primary_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distributed_keys is not None:
            result['DistributedKeys'] = self.distributed_keys
        if self.partition_life_cycle is not None:
            result['PartitionLifeCycle'] = self.partition_life_cycle
        if self.partition_statement is not None:
            result['PartitionStatement'] = self.partition_statement
        if self.primary_keys is not None:
            result['PrimaryKeys'] = self.primary_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributedKeys') is not None:
            self.distributed_keys = m.get('DistributedKeys')
        if m.get('PartitionLifeCycle') is not None:
            self.partition_life_cycle = m.get('PartitionLifeCycle')
        if m.get('PartitionStatement') is not None:
            self.partition_statement = m.get('PartitionStatement')
        if m.get('PrimaryKeys') is not None:
            self.primary_keys = m.get('PrimaryKeys')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTables(TeaModel):
    def __init__(
        self,
        adb_table_schema: SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema = None,
        filter_columns: List[str] = None,
        mapped_name: str = None,
        shard_columns: List[str] = None,
        table_id: str = None,
        table_name: str = None,
        type: str = None,
        where_clause: str = None,
    ):
        self.adb_table_schema = adb_table_schema
        self.filter_columns = filter_columns
        self.mapped_name = mapped_name
        self.shard_columns = shard_columns
        self.table_id = table_id
        self.table_name = table_name
        self.type = type
        self.where_clause = where_clause

    def validate(self):
        if self.adb_table_schema:
            self.adb_table_schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adb_table_schema is not None:
            result['AdbTableSchema'] = self.adb_table_schema.to_map()
        if self.filter_columns is not None:
            result['FilterColumns'] = self.filter_columns
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        if self.shard_columns is not None:
            result['ShardColumns'] = self.shard_columns
        if self.table_id is not None:
            result['TableId'] = self.table_id
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.type is not None:
            result['Type'] = self.type
        if self.where_clause is not None:
            result['WhereClause'] = self.where_clause
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdbTableSchema') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTablesAdbTableSchema()
            self.adb_table_schema = temp_model.from_map(m['AdbTableSchema'])
        if m.get('FilterColumns') is not None:
            self.filter_columns = m.get('FilterColumns')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        if m.get('ShardColumns') is not None:
            self.shard_columns = m.get('ShardColumns')
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WhereClause') is not None:
            self.where_clause = m.get('WhereClause')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabases(TeaModel):
    def __init__(
        self,
        database_id: str = None,
        database_name: str = None,
        mapped_name: str = None,
        tables: List[SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTables] = None,
        tenant_name: str = None,
        type: str = None,
    ):
        self.database_id = database_id
        self.database_name = database_name
        self.mapped_name = mapped_name
        self.tables = tables
        self.tenant_name = tenant_name
        self.type = type

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
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.mapped_name is not None:
            result['MappedName'] = self.mapped_name
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('MappedName') is not None:
            self.mapped_name = m.get('MappedName')
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabasesTables()
                self.tables.append(temp_model.from_map(k))
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferMapping(TeaModel):
    def __init__(
        self,
        databases: List[SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabases] = None,
        mode: str = None,
    ):
        self.databases = databases
        self.mode = mode

    def validate(self):
        if self.databases:
            for k in self.databases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Databases'] = []
        if self.databases is not None:
            for k in self.databases:
                result['Databases'].append(k.to_map() if k else None)
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k in m.get('Databases'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMappingDatabases()
                self.databases.append(temp_model.from_map(k))
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig(TeaModel):
    def __init__(
        self,
        record_type_list: List[str] = None,
        start_timestamp: int = None,
        store_log_kept_hour: int = None,
        store_transaction_enabled: bool = None,
        transfer_step_type: str = None,
    ):
        self.record_type_list = record_type_list
        self.start_timestamp = start_timestamp
        self.store_log_kept_hour = store_log_kept_hour
        self.store_transaction_enabled = store_transaction_enabled
        self.transfer_step_type = transfer_step_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.record_type_list is not None:
            result['RecordTypeList'] = self.record_type_list
        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp
        if self.store_log_kept_hour is not None:
            result['StoreLogKeptHour'] = self.store_log_kept_hour
        if self.store_transaction_enabled is not None:
            result['StoreTransactionEnabled'] = self.store_transaction_enabled
        if self.transfer_step_type is not None:
            result['TransferStepType'] = self.transfer_step_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordTypeList') is not None:
            self.record_type_list = m.get('RecordTypeList')
        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')
        if m.get('StoreLogKeptHour') is not None:
            self.store_log_kept_hour = m.get('StoreLogKeptHour')
        if m.get('StoreTransactionEnabled') is not None:
            self.store_transaction_enabled = m.get('StoreTransactionEnabled')
        if m.get('TransferStepType') is not None:
            self.transfer_step_type = m.get('TransferStepType')
        return self


class SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfig(TeaModel):
    def __init__(
        self,
        enable_full_sync: bool = None,
        enable_incr_sync: bool = None,
        enable_struct_sync: bool = None,
        incr_sync_step_transfer_config: SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig = None,
    ):
        self.enable_full_sync = enable_full_sync
        self.enable_incr_sync = enable_incr_sync
        self.enable_struct_sync = enable_struct_sync
        self.incr_sync_step_transfer_config = incr_sync_step_transfer_config

    def validate(self):
        if self.incr_sync_step_transfer_config:
            self.incr_sync_step_transfer_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_full_sync is not None:
            result['EnableFullSync'] = self.enable_full_sync
        if self.enable_incr_sync is not None:
            result['EnableIncrSync'] = self.enable_incr_sync
        if self.enable_struct_sync is not None:
            result['EnableStructSync'] = self.enable_struct_sync
        if self.incr_sync_step_transfer_config is not None:
            result['IncrSyncStepTransferConfig'] = self.incr_sync_step_transfer_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableFullSync') is not None:
            self.enable_full_sync = m.get('EnableFullSync')
        if m.get('EnableIncrSync') is not None:
            self.enable_incr_sync = m.get('EnableIncrSync')
        if m.get('EnableStructSync') is not None:
            self.enable_struct_sync = m.get('EnableStructSync')
        if m.get('IncrSyncStepTransferConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfigIncrSyncStepTransferConfig()
            self.incr_sync_step_transfer_config = temp_model.from_map(m['IncrSyncStepTransferConfig'])
        return self


class SearchOmsOpenAPIProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        business_name: str = None,
        dest_config: SearchOmsOpenAPIProjectsResponseBodyDataDestConfig = None,
        labels: List[SearchOmsOpenAPIProjectsResponseBodyDataLabels] = None,
        project_id: str = None,
        project_name: str = None,
        project_owner: str = None,
        source_config: SearchOmsOpenAPIProjectsResponseBodyDataSourceConfig = None,
        steps: List[SearchOmsOpenAPIProjectsResponseBodyDataSteps] = None,
        transfer_mapping: SearchOmsOpenAPIProjectsResponseBodyDataTransferMapping = None,
        transfer_step_config: SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfig = None,
    ):
        self.business_name = business_name
        self.dest_config = dest_config
        self.labels = labels
        self.project_id = project_id
        self.project_name = project_name
        self.project_owner = project_owner
        self.source_config = source_config
        self.steps = steps
        self.transfer_mapping = transfer_mapping
        self.transfer_step_config = transfer_step_config

    def validate(self):
        if self.dest_config:
            self.dest_config.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.source_config:
            self.source_config.validate()
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()
        if self.transfer_mapping:
            self.transfer_mapping.validate()
        if self.transfer_step_config:
            self.transfer_step_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.dest_config is not None:
            result['DestConfig'] = self.dest_config.to_map()
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_owner is not None:
            result['ProjectOwner'] = self.project_owner
        if self.source_config is not None:
            result['SourceConfig'] = self.source_config.to_map()
        result['Steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['Steps'].append(k.to_map() if k else None)
        if self.transfer_mapping is not None:
            result['TransferMapping'] = self.transfer_mapping.to_map()
        if self.transfer_step_config is not None:
            result['TransferStepConfig'] = self.transfer_step_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('DestConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataDestConfig()
            self.dest_config = temp_model.from_map(m['DestConfig'])
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectOwner') is not None:
            self.project_owner = m.get('ProjectOwner')
        if m.get('SourceConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataSourceConfig()
            self.source_config = temp_model.from_map(m['SourceConfig'])
        self.steps = []
        if m.get('Steps') is not None:
            for k in m.get('Steps'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyDataSteps()
                self.steps.append(temp_model.from_map(k))
        if m.get('TransferMapping') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferMapping()
            self.transfer_mapping = temp_model.from_map(m['TransferMapping'])
        if m.get('TransferStepConfig') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyDataTransferStepConfig()
            self.transfer_step_config = temp_model.from_map(m['TransferStepConfig'])
        return self


class SearchOmsOpenAPIProjectsResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class SearchOmsOpenAPIProjectsResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: List[SearchOmsOpenAPIProjectsResponseBodyData] = None,
        error_detail: SearchOmsOpenAPIProjectsResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchOmsOpenAPIProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorDetail') is not None:
            temp_model = SearchOmsOpenAPIProjectsResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchOmsOpenAPIProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchOmsOpenAPIProjectsResponseBody = None,
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
            temp_model = SearchOmsOpenAPIProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class StartOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class StartOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: bool = None,
        error_detail: StartOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = StartOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class StartOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartOmsOpenAPIProjectResponseBody = None,
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
            temp_model = StartOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopOmsOpenAPIProjectRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        worker_grade_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.worker_grade_id = worker_grade_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.worker_grade_id is not None:
            result['WorkerGradeId'] = self.worker_grade_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WorkerGradeId') is not None:
            self.worker_grade_id = m.get('WorkerGradeId')
        return self


class StopOmsOpenAPIProjectResponseBodyErrorDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
        level: str = None,
        message: str = None,
        proposal: str = None,
    ):
        self.code = code
        self.level = level
        self.message = message
        self.proposal = proposal

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.proposal is not None:
            result['Proposal'] = self.proposal
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')
        return self


class StopOmsOpenAPIProjectResponseBody(TeaModel):
    def __init__(
        self,
        advice: str = None,
        code: str = None,
        cost: str = None,
        data: bool = None,
        error_detail: StopOmsOpenAPIProjectResponseBodyErrorDetail = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.advice = advice
        self.code = code
        self.cost = cost
        self.data = data
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.error_detail:
            self.error_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advice is not None:
            result['Advice'] = self.advice
        if self.code is not None:
            result['Code'] = self.code
        if self.cost is not None:
            result['Cost'] = self.cost
        if self.data is not None:
            result['Data'] = self.data
        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Advice') is not None:
            self.advice = m.get('Advice')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Cost') is not None:
            self.cost = m.get('Cost')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorDetail') is not None:
            temp_model = StopOmsOpenAPIProjectResponseBodyErrorDetail()
            self.error_detail = temp_model.from_map(m['ErrorDetail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class StopOmsOpenAPIProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopOmsOpenAPIProjectResponseBody = None,
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
            temp_model = StopOmsOpenAPIProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


