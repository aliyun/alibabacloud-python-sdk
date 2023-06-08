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
        # The name of the database.
        self.client_token = client_token
        # The encoding standard of the database.
        # For more information, see the Charset field returned by the DescribeCharset operation.
        self.collation = collation
        # Alibaba Cloud CLI
        self.database_name = database_name
        # The operation that you want to perform.   
        # Set the value to **CreateDatabase**.
        self.description = description
        # The ID of the tenant.
        self.encoding = encoding
        # The collation.
        self.instance_id = instance_id
        # The name of the database.   
        # You cannot use reserved keywords, such as test and mysql.
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
        # CreateDatabase
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
        # Specifies whether to enable automatic renewal.   
        # This parameter is valid only when the ChargeType parameter is set to PrePaid. Valid values: 
        # - true: enables automatic renewal for the instance.   
        # - false: disables automatic renewal for the instance. This is the default value.
        self.auto_renew = auto_renew
        # The automatic renewal period of the instance. This parameter is required when the AutoRenew parameter is set to true. Valid values:  
        # - If the PeriodUnit parameter is set to Year: "1", "2", and "3".   
        # - If the PeriodUnit parameter is set to Month: "1", "2", "3", "6", and "12".
        self.auto_renew_period = auto_renew_period
        # The billing method of the instance. Valid values:  
        # - PrePay: the subscription billing method. You must ensure that the remaining balance or credit balance of your account can cover the cost of the subscription. Otherwise, you will receive an InvalidPayMethod error. 
        # - PostPay: the pay-as-you-go billing method. This is the default value. By default, fees are charged on an hourly basis.
        self.charge_type = charge_type
        # The size of the storage space,in GB.    
        # The limits on the storage space vary with the cluster specifications:   
        # - 8C32GB: 100 GB to 10000 GB   
        # - 14C70GB: 200 GB to 10000 GB   
        # - 30C180GB: 400 GB to 10000 GB   
        # - 62C400GB: 800 GB to 10000 GB    
        # The preceding minimum storage space sizes are the default storage space sizes of the corresponding cluster specification plans.
        self.disk_size = disk_size
        # The return result of the request.
        self.disk_type = disk_type
        # The specifications of the cluster.     
        # You can specify one of the following four plans:   
        #  - 8C32GB: indicates 8 CPU cores and 32 GB of memory.    
        #  - 14C70GB: indicates 14 CPU cores and 70 GB of memory. This is the default value.
        # - 30C180GB: indicates 30 CPU cores and 180 GB of memory.     
        # - 62C400GB: indicates 62 CPU cores and 400 GB of memory.
        self.instance_class = instance_class
        # The name of the OceanBase cluster.    
        # It must be 1 to 20 characters in length.   
        # If this parameter is not specified, the value is the instance ID of the cluster by default.
        self.instance_name = instance_name
        # OceanBase Server version number.
        self.ob_version = ob_version
        # The valid duration of the purchased resources. The unit is specified by the PeriodUnit parameter.   
        # This parameter is valid and required only when the InstanceChargeType parameter is set to PrePaid.      
        # Valid values:     
        # - When the PeriodUnit parameter is set to Month: "1", "2", "3", "4", "5", "6", "7", "8", "9". 
        # - When the PeriodUnit parameter is set to Year: "1", "2", "3".
        self.period = period
        # The unit of the valid duration of the purchased resources.     
        # Valid value for subscription: Month or Year.
        # Default value: Month for subscription, and Hour for pay-as-you-go.
        self.period_unit = period_unit
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The series of the OceanBase cluster. Valid values:    
        # - normal: Standard Cluster Edition (Cloud Disk). This is the default value.
        # - normal_ssd: Standard Cluster Edition (Local Disk).
        # - history: History Database Cluster Edition.
        self.series = series
        # The ID of the zone to which the instance belongs.   
        # For more information about how to obtain the list of zones, see [DescribeZones](~~25610~~).
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
        # 订单ID。该参数只有创建包年包月ECS实例（请求参数InstanceChargeType=PrePaid）时有返回值。
        self.instance_id = instance_id
        # 资源组ID
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
        # 实例ID
        self.data = data
        # Response parameters
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
        # ```
        # http(s)://[Endpoint]/?Action=CreateOmsMysqlDataSource
        # &Name=oms-mysql
        # &Type=INTERNET
        # &VpcId=vpc-12345abcde*******\
        # &InstanceId=pc-12ab34cd56******\
        # &DgDatabaseId=dg-yhss6sdlaff****\
        # &Ip=10.0.****\
        # &Port=3306
        # &Schema=test
        # &Username=omsTestUser
        # &Password=YWJjZDEyM0Ah
        # &Description=MySQL data source for OMS testing
        # &Common request parameters
        # ```
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
        # 页序号，分页查询时生效
        self.page_number = page_number
        # 页大小，分页查询时生效
        self.page_size = page_size
        self.project_name = project_name
        self.source_config = source_config
        self.transfer_mapping = transfer_mapping
        self.transfer_step_config = transfer_step_config
        # 实例规格 ID，创建项目时生效
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
        # 页序号，分页查询时生效
        self.page_number = page_number
        # 页大小，分页查询时生效
        self.page_size = page_size
        self.project_name = project_name
        self.source_config_shrink = source_config_shrink
        self.transfer_mapping_shrink = transfer_mapping_shrink
        self.transfer_step_config_shrink = transfer_step_config_shrink
        # 实例规格 ID，创建项目时生效
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
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id
        # The name of the whitelist group.
        self.security_ip_group_name = security_ip_group_name
        # The return result of the request.
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
        # ```
        # http(s)://[Endpoint]/?Action=CreateSecurityIpGroup
        # &InstanceId=ob317v4uif****\
        # &SecurityIps=192.168.1.1,192.168.0.0.1/8
        # &SecurityIpGroupName=pay_online
        # &Common request parameters
        # ```
        self.instance_id = instance_id
        # You can call this operation to create an IP address whitelist group.
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
        # The IP addresses or CIDR blocks in the IP address whitelist group.   
        # The return values of SecurityIps are strings that are separated with commas (,).
        self.request_id = request_id
        # The operation that you want to perform.   
        # Set the value to **CreateSecurityIpGroup**.
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
        # The description of the database.
        self.charset = charset
        # The number of resource distribution nodes in the tenant.    
        # The number is determined by the deployment mode of the cluster. If the cluster is deployed in 2-2-2 mode, the maximum number of resource distribution nodes is 2.
        self.cpu = cpu
        # $.parameters[13].schema.example
        self.description = description
        # The ID of the vSwitch.    
        # If no suitable vSwitch is available, create a vSwitch as prompted.   
        # For more information, see Use a vSwitch.
        self.instance_id = instance_id
        # The return result of the request.
        self.memory = memory
        # $.parameters[12].schema.enumValueTitles
        self.primary_zone = primary_zone
        # The ID of the tenant.
        self.tenant_mode = tenant_mode
        # Alibaba Cloud CLI
        self.tenant_name = tenant_name
        # The memory size of the tenant, in GB.   
        # 
        # > <br>The memory size of a single tenant cannot exceed that of the corresponding cluster. <br>For example, if the specification of the cluster is 14 CPU cores and 70 GB of memory, the memory size of the tenant cannot exceed 70 GB.
        self.time_zone = time_zone
        # $.parameters[11].schema.description
        self.unit_num = unit_num
        # $.parameters[12].schema.description
        self.user_vswitch_id = user_vswitch_id
        # The time zone of the tenant.  For more information, see [DescribeTimeZones](https://help.aliyun.com/document_detail/410361.html).
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
        # WB01144930
        self.request_id = request_id
        # You can call this operation to create a tenant.
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


class CreateTenantSecurityIpGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips
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
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CreateTenantSecurityIpGroupResponseBodySecurityIpGroup(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips
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
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CreateTenantSecurityIpGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_group: CreateTenantSecurityIpGroupResponseBodySecurityIpGroup = None,
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
            temp_model = CreateTenantSecurityIpGroupResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class CreateTenantSecurityIpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTenantSecurityIpGroupResponseBody = None,
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
            temp_model = CreateTenantSecurityIpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTenantUserRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        encryption_type: str = None,
        instance_id: str = None,
        roles: str = None,
        tenant_id: str = None,
        user_name: str = None,
        user_password: str = None,
        user_type: str = None,
    ):
        # The description of the database.
        self.description = description
        # 加密方式。
        self.encryption_type = encryption_type
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id
        # The role of the user account.  In Oracle mode, this parameter unspecified is left unspecified.  In MySQL mode, the super administrator account has ALL PRIVILEGES, and you can leave this parameter unspecified.  You need to specify the account information for a general user account. By default, the account information is a JSON array that contains the information of the role and the schema (Oracle mode) or database (MySQL mode).  Valid values: ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES. ReadOnly: a role that has only the read-only privilege SELECT. DDL: a role that has DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW. DML: a role that has DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW.
        self.roles = roles
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The name of the database account.  You cannot use reserved keywords, such as SYS and root.
        self.user_name = user_name
        # The password of the database account.  It must be 10 to 32 characters in length and contain three types of the following characters: uppercase letters, lowercase letters, digits, and special characters. The special characters are ! @ # $ % \ ^ \ & \ * ( ) _ + - =\
        self.user_password = user_password
        # The type of the database account. Valid values: Admin: the super administrator account. Normal: a general account.
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
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
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
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
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
        # The name of the database.
        self.database = database
        # The role of the account.  In Oracle mode, a role is a schema-level role. Valid values: - ReadWrite: a role that has the read and write privileges, including CREATE TABLE, CREATE VIEW, CREATE PROCEDURE, CREATE SYNONYM, CREATE SEQUENCE, CREATE TRIGGER, CREATE TYPE, CREATE SESSION, EXECUTE ANY PROCEDURE, CREATE ANY OUTLINE, ALTER ANY OUTLINE, DROP ANY OUTLINE, CREATE ANY PROCEDURE, ALTER ANY PROCEDURE, DROP ANY PROCEDURE, CREATE ANY SEQUENCE, ALTER ANY SEQUENCE, DROP ANY SEQUENCE, CREATE ANY TYPE, ALTER ANY TYPE, DROP ANY TYPE, SYSKM, CREATE ANY TRIGGER, ALTER ANY TRIGGER, DROP ANY TRIGGER, CREATE PROFILE, ALTER PROFILE, and DROP PROFILE. - ReadOnly: a role that has only the read-only privilege SELECT.
        # In MySQL mode, a role is a database-level role. Valid values: - ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES. - ReadOnly: a role that has only the read-only privilege SELECT. - DDL: a role that has the DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW. - DML: a role that has the DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW. 
        # * By default, an Oracle account has the read and write privileges on its own schema, which are not listed here.
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
        # The roles of the accounts.
        self.roles = roles
        # The name of the database account.
        self.user_name = user_name
        # The status of the database account. Valid values:  - Locked: The account is locked. - ONLINE: The account is unlocked. The default status of a new account is ONLINE after it is created.
        self.user_status = user_status
        # The type of the database account. Valid values:  - Admin: the super administrator account. - Normal: a general account.
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
        # The request ID.
        self.request_id = request_id
        # The list of database accounts in the tenant.
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
        # The total count, which takes effect in a pagination query.
        self.page_number = page_number
        # Contact the administrator.
        self.page_size = page_size
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.project_id = project_id
        # Indicates whether the call is successful.
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
        # The operation that you want to perform. Set the value to **DeleteOmsOpenAPIProject**.
        self.code = code
        # The error description (old).
        self.level = level
        # The error code (new).
        self.message = message
        # The page number, which takes effect in a pagination query.
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
        # You can call this operation to delete a data synchronization project.
        self.advice = advice
        # Indicates whether the project has been deleted.
        self.code = code
        self.cost = cost
        self.data = data
        # The suggestions (new).
        self.error_detail = error_detail
        # A system error occurred.
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        # The page number, which takes effect in a pagination query.
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
        # The name of the IP address whitelist group.    
        # It must be 2 to 32 characters in length, start with a lowercase letter, end with a lowercase letter or digit, and contain only lowercase letters, digits, and underscores (_).
        self.instance_id = instance_id
        # The information of the deleted IP whitelist group.
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
        # Example 1
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


class DeleteTenantSecurityIpGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
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
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DeleteTenantSecurityIpGroupResponseBodySecurityIpGroup(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
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
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DeleteTenantSecurityIpGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_group: DeleteTenantSecurityIpGroupResponseBodySecurityIpGroup = None,
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
            temp_model = DeleteTenantSecurityIpGroupResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class DeleteTenantSecurityIpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTenantSecurityIpGroupResponseBody = None,
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
            temp_model = DeleteTenantSecurityIpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTenantUsersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tenant_id: str = None,
        users: str = None,
    ):
        # Example 1
        self.instance_id = instance_id
        # $.parameters[4].schema.enumValueTitles
        self.tenant_id = tenant_id
        # $.parameters[2].schema.example
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
        # DeleteTenantUsers
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
        # You can call this operation to delete one or more tenants from an OceanBase cluster.
        self.instance_id = instance_id
        # ```
        # http(s)://[Endpoint]/?Action=DeleteTenants
        # &TenantIds=["ob2mr3oae0****", "ob2mr3oae1****"]
        # &InstanceId=ob317v4uif****\
        # &Common request parameters
        # ```
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
        # The search value.
        self.accept_language = accept_language
        # {
        #   "UserName":testUser
        # }
        self.db_name = db_name
        # zh-CN
        self.end_time = end_time
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.filter_condition = filter_condition
        # The number of rows to return on each page.    
        # - Maximum value: 100   
        # - Default value: 10
        self.node_ip = node_ip
        # desc
        self.page_number = page_number
        # The start time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.page_size = page_size
        # 1
        self.sqlid = sqlid
        # The search keyword.
        self.search_key_word = search_key_word
        # The ID of the tenant.
        self.search_parameter = search_parameter
        # Utilization above threshold
        self.search_rule = search_rule
        # 10
        self.search_value = search_value
        # The end time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.sort_column = sort_column
        # The request time, in ms.
        self.sort_order = sort_order
        # The total count.
        self.start_time = start_time
        # Alibaba Cloud CLI
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
        # The search value.
        self.accept_language = accept_language
        # {
        #   "UserName":testUser
        # }
        self.db_name = db_name
        # zh-CN
        self.end_time = end_time
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.filter_condition_shrink = filter_condition_shrink
        # The number of rows to return on each page.    
        # - Maximum value: 100   
        # - Default value: 10
        self.node_ip = node_ip
        # desc
        self.page_number = page_number
        # The start time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.page_size = page_size
        # 1
        self.sqlid = sqlid
        # The search keyword.
        self.search_key_word = search_key_word
        # The ID of the tenant.
        self.search_parameter = search_parameter
        # Utilization above threshold
        self.search_rule = search_rule
        # 10
        self.search_value = search_value
        # The end time of the time range for querying suspicious SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.sort_column = sort_column
        # The request time, in ms.
        self.sort_order = sort_order
        # The total count.
        self.start_time = start_time
        # Alibaba Cloud CLI
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
        # {"name":"DescribeAnomalySQLList","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":60000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeAnomalySQLList\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-09-13T15:40:43Z\"},{\"name\":\"DbName\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"SearchKeyWord\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"update\"},{\"name\":\"SearchParameter\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SearchRule\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\">\"},{\"name\":\"SearchValue\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"0.01\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"NodeIp\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"i-bp19y05uq6xpacyqnlrc\"},{\"name\":\"AcceptLanguage\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"zh-CN\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"FilterCondition\",\"position\":\"Body\",\"style\":\"json\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"enumValueTitles\":{\"UserName\":\"UserName\",\"Event\":\"Event\",\"SQLType\":\"SQLType\",\"ClientIp\":\"ClientIp\"},\"title\":\"\",\"description\":\"\",\"example\":\"{\\n  \\\"UserName\\\":testUser\\n}\"},{\"name\":\"SortColumn\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SortOrder\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"enumValueTitles\":{\"{     \\\"dbname\\\":test,     \\\"SQLType\\\":null\\t\\t }\":\"{     \\\"dbname\\\":test,     \\\"SQLType\\\":null\\t\\t }\"},\"title\":\"\",\"description\":\"\",\"example\":\"desc\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"TotalCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"2\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"AnomalySQLList\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\" \",\"children\":[{\"name\":\"Key\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"DiagnosisRule\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\"},{\"name\":\"SQLText\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC\"},{\"name\":\"Suggestion\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"database1\"},{\"name\":\"RequestTimeUTCString\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2022-01-11T07:08:00Z\"},{\"name\":\"CpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"50.13\"},{\"name\":\"SQLId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"99E9D3BF****B486239E6C7BC79B****\"},{\"name\":\"Diagnosis\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\"},{\"name\":\"RequestTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"50.00\"},{\"name\":\"Executions\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"89043\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tester\"}],\"title\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{\"2014\":[{\"code\":\"2014\",\"defaultError\":false,\"errorCode\":\"InternalError\",\"errorMessage\":\"The request processing has failed due to some unknown error.\",\"errorMessageCn\":\"\",\"type\":\"user\"}]}"}
        self.db_name = db_name
        self.diagnosis = diagnosis
        # The list of suspicious SQL statements.
        self.diagnosis_rule = diagnosis_rule
        self.executions = executions
        # The average CPU time, in ms.
        self.key = key
        self.request_time = request_time
        self.request_time_utcstring = request_time_utcstring
        self.sqlid = sqlid
        # ```
        # http(s)://[Endpoint]/?Action=DescribeAnomalySQLList
        # &TenantId=t2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-06-13 15:40:43
        # &DbName=testdb
        # &SearchKeyWord=update
        # &SearchParameter=cputime
        # &SearchRule=>
        # &SearchValue=0.01
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &NodeIp=i-bp19y05uq6xpacyqnlrc
        # &AcceptLanguage=zh-CN
        # &PageSize=10
        # &PageNumber=1
        # &SortColumn=cputime
        # &SortOrder=desc
        # &Common request parameters
        # ```
        self.sqltext = sqltext
        # {
        #     "TotalCount": 2,
        #     "RequestId": "473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E",
        #     "AnomalySQLList": [
        #         {
        #             "Key": 1,
        #             "DiagnosisRule": "Utilization above threshold",
        #             "SQLText": "SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC",
        #             "Suggestion": "Check your business scenarios, data distribution changes, request surges, and execution plan changes.",
        #             "DbName": "database1",
        #             "RequestTimeUTCString": "2022-01-11T07:08:00Z",
        #             "SQLId": "99E9D3BF****B486239E6C7BC79B****",
        #             "Diagnosis": "Total number of executions = 80199, Average CPU time = 6.8 ms, Overall CPU utilization = 87%",
        #             "RequestTime": 1641884880000,
        #             "Executions": 89043,
        #             "UserName": "tester"
        #         }
        #     ]
        # }
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
        # The diagnostic rule.
        self.anomaly_sqllist = anomaly_sqllist
        # The sorting rule.
        self.request_id = request_id
        # The SQL text.
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
        # The CPU resources available.
        self.instance_id = instance_id
        # ```
        # http(s)://[Endpoint]/?Action=DescribeAvailableCpuResource
        # &InstanceId=ob317v4uif****\
        # &TenantId=ob2mr3oae0****\
        # &ModifyType=update
        # &Common request parameters
        # ```
        self.modify_type = modify_type
        # The operation that you want to perform.   
        # Set the value to **DescribeAvailableCpuResource**.
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
        # The available memory size.
        self.cpu_num = cpu_num
        # The ID of the region.
        self.instance_id = instance_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The number of resource units in the tenant.
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
        # You can call this operation to query the available memory resource of an OceanBase Database tenant.
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
        # ```
        # http(s)://[Endpoint]/?Action=DescribeAvailableMemResource
        # &InstanceId=ob317v4uif****\
        # &TenantId=ob2mr3oae0****\
        # &UnitNum=2
        # &CpuNum=14
        # &Common request parameters
        # ```
        self.data = data
        # The number of CPU cores.
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
        series: str = None,
        tenant_mode: str = None,
    ):
        # 实例的系列  - normal（默认）：标准集群版（云盘）  - normal_ssd：标准集群版（本地盘） - history：历史库集群版。
        self.series = series
        # The return result of the request.
        self.tenant_mode = tenant_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.series is not None:
            result['Series'] = self.series
        if self.tenant_mode is not None:
            result['TenantMode'] = self.tenant_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('TenantMode') is not None:
            self.tenant_mode = m.get('TenantMode')
        return self


class DescribeCharsetResponseBodyCharset(TeaModel):
    def __init__(
        self,
        charset: str = None,
        collations: List[str] = None,
    ):
        # DescribeCharset
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
        # ```
        # http(s)://[Endpoint]/?Action=DescribeCharset
        # &TenantMode=Oracle
        # &Common request parameters
        # ```
        self.charset = charset
        # The operation that you want to perform.   
        # Set the value to **DescribeCharset**.
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
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.database_name = database_name
        # The return result of the request.
        self.page_number = page_number
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.page_size = page_size
        # The information about the database tables.
        self.search_key = search_key
        # The request ID.
        self.tenant_id = tenant_id
        # The role of the account.    
        # In MySQL mode, a role is a database-level role. Valid values:  
        # - ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES.  
        # - ReadOnly: a role that has only the read-only privilege SELECT.   
        # - DDL: a role that has the DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW.   
        # - DML: a role that has the DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW.
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
        # The request ID.
        self.role = role
        # Example 1
        self.user_name = user_name
        # The type of the account. Valid values:  - Admin: the super administrator account. - Normal: a general account.
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
        instance_id: str = None,
        required_size: float = None,
        status: str = None,
        tables: List[DescribeDatabasesResponseBodyDatabasesTables] = None,
        tenant_id: str = None,
        users: List[DescribeDatabasesResponseBodyDatabasesUsers] = None,
    ):
        self.collation = collation
        # Specifies whether to return the information of tables in the database.   
        # Default value: false.
        self.create_time = create_time
        self.data_size = data_size
        # The number of the page to return.   
        # - Start value: 1   
        # - Default value: 1
        self.database_name = database_name
        # The return result of the request.
        self.db_type = db_type
        # The name of the database.
        self.description = description
        # The status of the database. Valid values:    
        # - ONLINE: The database is running.  
        # - DELETING: The database is being deleted.
        self.encoding = encoding
        self.instance_id = instance_id
        self.required_size = required_size
        # The list of databases in the tenant.
        self.status = status
        self.tables = tables
        self.tenant_id = tenant_id
        # The name of the database table.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        # The ID of the tenant.
        self.databases = databases
        self.request_id = request_id
        # The search keyword.
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
        # The size of the data disk, in GB.
        self.instance_id = instance_id
        # The information about the storage resources of the cluster.
        self.page_number = page_number
        # The server with the highest disk usage.
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
        # The series of the OceanBase cluster. Valid values:   
        # - NORMAL: the high availability edition.   
        # - BASIC: the basic edition.
        self.total_cpu = total_cpu
        # The type of the storage disk where the cluster is deployed. 
        # 
        # The default value is cloud_essd_pl1, which indicates an ESSD cloud disk.
        self.unit_cpu = unit_cpu
        # Indicates whether automatic upgrade of the OBServer version is enabled.
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
        # The ID of the OceanBase cluster.
        self.data_used_size = data_used_size
        # The time in UTC when the cluster expires.
        self.max_disk_used_ob_server = max_disk_used_ob_server
        # The maximum disk usage, in percentage.
        self.max_disk_used_percent = max_disk_used_percent
        # The data replica distribution mode of the cluster. Valid values: 
        # - n: indicates the single-IDC mode. 
        # - n-n: indicates the dual-IDC mode. 
        # - n-n-n: indicates the multi-IDC mode. 
        # 
        # > <br>The integer n represents the number of OBServer nodes in each IDC.
        self.total_disk_size = total_disk_size
        # The list of zones.
        self.unit_disk_size = unit_disk_size
        # The specifications of the cluster.  You can specify one of the following four plans:    
        # - 8C32G: indicates 8 CPU cores and 32 GB of memory. 
        # - 14C70G: indicates 14 CPU cores and 70 GB of memory. 
        # - 30C180G: indicates 30 CPU cores and 180 GB of memory. 
        # - 62C400G: indicates 62 CPU cores and 400 GB of memory.
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
        # The ID of the region.
        self.total_disk_size = total_disk_size
        # The request ID.
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
        # Indicates whether trusted ECS instances are used.
        self.total_memory = total_memory
        # The log disk space of each replica node in the cluster. Unit: GB.
        self.unit_memory = unit_memory
        # The time in UTC when the cluster was created.
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
        # The information of the OceanBase cluster.
        self.cpu = cpu
        # The number of the page to return. 
        # - Start value: 1  
        # - Default value: 1
        self.disk_size = disk_size
        # The server with the highest disk usage.
        self.log_disk_size = log_disk_size
        # The name of the OceanBase cluster.
        self.memory = memory
        # The number of CPU cores used in the cluster.
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
        enable_isolation_optimization: bool = None,
        enable_upgrade_log_disk: bool = None,
        expire_time: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_role: str = None,
        is_latest_ob_version: bool = None,
        is_trust_ecs: bool = None,
        isolation_optimization: bool = None,
        maintain_time: str = None,
        node_num: str = None,
        ob_rpm_version: str = None,
        pay_type: str = None,
        resource: DescribeInstanceResponseBodyInstanceResource = None,
        series: str = None,
        status: str = None,
        version: str = None,
        zones: List[str] = None,
    ):
        # The operation that you want to perform. <br>Set the value to **DescribeInstance**.
        self.auto_renewal = auto_renewal
        # Example 1
        self.auto_upgrade_ob_version = auto_upgrade_ob_version
        self.available_zones = available_zones
        # Indicates whether the log disk specifications can be upgraded.
        self.create_time = create_time
        # The total number of CPU cores of the cluster.
        self.data_merge_time = data_merge_time
        # Alibaba Cloud CLI
        self.deploy_mode = deploy_mode
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.deploy_type = deploy_type
        # The total storage space of the cluster, in GB.
        self.disk_type = disk_type
        self.enable_isolation_optimization = enable_isolation_optimization
        self.enable_upgrade_log_disk = enable_upgrade_log_disk
        # The information of the OceanBase cluster.
        self.expire_time = expire_time
        # The detailed information of the OBServer version.
        self.instance_class = instance_class
        # The information about the log disk space of the cluster.
        self.instance_id = instance_id
        # Indicates whether automatic upgrade of the OBServer version is enabled.
        self.instance_name = instance_name
        self.instance_role = instance_role
        self.is_latest_ob_version = is_latest_ob_version
        # The information about the CPU resources of the cluster.
        self.is_trust_ecs = is_trust_ecs
        self.isolation_optimization = isolation_optimization
        # The time when the major compaction of cluster data is performed.
        self.maintain_time = maintain_time
        self.node_num = node_num
        self.ob_rpm_version = ob_rpm_version
        # The list of zones.
        self.pay_type = pay_type
        # The size of used memory in the cluster, in GB.
        self.resource = resource
        # Indicates whether the OBServer version is the latest.
        self.series = series
        # The information about cluster resources.
        self.status = status
        # You can call this operation to query the detailed information of an OceanBase cluster.
        self.version = version
        self.zones = zones

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
        if self.enable_isolation_optimization is not None:
            result['EnableIsolationOptimization'] = self.enable_isolation_optimization
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
        if self.instance_role is not None:
            result['InstanceRole'] = self.instance_role
        if self.is_latest_ob_version is not None:
            result['IsLatestObVersion'] = self.is_latest_ob_version
        if self.is_trust_ecs is not None:
            result['IsTrustEcs'] = self.is_trust_ecs
        if self.isolation_optimization is not None:
            result['IsolationOptimization'] = self.isolation_optimization
        if self.maintain_time is not None:
            result['MaintainTime'] = self.maintain_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
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
        if self.zones is not None:
            result['Zones'] = self.zones
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
        if m.get('EnableIsolationOptimization') is not None:
            self.enable_isolation_optimization = m.get('EnableIsolationOptimization')
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
        if m.get('InstanceRole') is not None:
            self.instance_role = m.get('InstanceRole')
        if m.get('IsLatestObVersion') is not None:
            self.is_latest_ob_version = m.get('IsLatestObVersion')
        if m.get('IsTrustEcs') is not None:
            self.is_trust_ecs = m.get('IsTrustEcs')
        if m.get('IsolationOptimization') is not None:
            self.isolation_optimization = m.get('IsolationOptimization')
        if m.get('MaintainTime') is not None:
            self.maintain_time = m.get('MaintainTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
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
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance: DescribeInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # The log disk space of each replica node in the cluster. Unit: GB.
        self.instance = instance
        # The total log disk space of the cluster, in GB.
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
        # The ID of the zone.
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
        # DescribeInstanceCreatableZone
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
        # Indicates whether the cluster is deployed in the zone.
        self.request_id = request_id
        # The operation that you want to perform.   
        # Set the value to **DescribeInstanceCreatableZone**.
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


class DescribeInstanceSecurityConfigsRequest(TeaModel):
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


class DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigsSecurityConfigs(TeaModel):
    def __init__(
        self,
        config_description: str = None,
        config_group: str = None,
        config_name: str = None,
        risk: bool = None,
        risk_description: str = None,
    ):
        self.config_description = config_description
        self.config_group = config_group
        self.config_name = config_name
        self.risk = risk
        self.risk_description = risk_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_group is not None:
            result['ConfigGroup'] = self.config_group
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.risk is not None:
            result['Risk'] = self.risk
        if self.risk_description is not None:
            result['RiskDescription'] = self.risk_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigGroup') is not None:
            self.config_group = m.get('ConfigGroup')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('Risk') is not None:
            self.risk = m.get('Risk')
        if m.get('RiskDescription') is not None:
            self.risk_description = m.get('RiskDescription')
        return self


class DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigs(TeaModel):
    def __init__(
        self,
        security_configs: List[DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigsSecurityConfigs] = None,
        total_check_count: int = None,
        total_risk_count: int = None,
    ):
        self.security_configs = security_configs
        self.total_check_count = total_check_count
        self.total_risk_count = total_risk_count

    def validate(self):
        if self.security_configs:
            for k in self.security_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SecurityConfigs'] = []
        if self.security_configs is not None:
            for k in self.security_configs:
                result['SecurityConfigs'].append(k.to_map() if k else None)
        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count
        if self.total_risk_count is not None:
            result['TotalRiskCount'] = self.total_risk_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_configs = []
        if m.get('SecurityConfigs') is not None:
            for k in m.get('SecurityConfigs'):
                temp_model = DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigsSecurityConfigs()
                self.security_configs.append(temp_model.from_map(k))
        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')
        if m.get('TotalRiskCount') is not None:
            self.total_risk_count = m.get('TotalRiskCount')
        return self


class DescribeInstanceSecurityConfigsResponseBody(TeaModel):
    def __init__(
        self,
        instance_security_configs: DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigs = None,
        request_id: str = None,
    ):
        self.instance_security_configs = instance_security_configs
        self.request_id = request_id

    def validate(self):
        if self.instance_security_configs:
            self.instance_security_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_security_configs is not None:
            result['InstanceSecurityConfigs'] = self.instance_security_configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSecurityConfigs') is not None:
            temp_model = DescribeInstanceSecurityConfigsResponseBodyInstanceSecurityConfigs()
            self.instance_security_configs = temp_model.from_map(m['InstanceSecurityConfigs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceSecurityConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceSecurityConfigsResponseBody = None,
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
            temp_model = DescribeInstanceSecurityConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTagsRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        tags: str = None,
    ):
        # The list of tags.
        self.instance_ids = instance_ids
        # The returned response.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class DescribeInstanceTagsResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag: str = None,
    ):
        # You can call this operation to view the tag value of a cluster.
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeInstanceTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_resources: List[DescribeInstanceTagsResponseBodyTagResources] = None,
    ):
        # The resource ID.
        self.request_id = request_id
        # The request ID.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeInstanceTagsResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeInstanceTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceTagsResponseBody = None,
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
            temp_model = DescribeInstanceTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTenantModesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The operation that you want to perform.   
        # Set the value to **DescribeInstanceTenantModes**.
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
        # The status of the node.
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
        # Indicates whether the migration can be canceled.   
        # This field is valid only for units that are being manually immigrated or emigrated.
        self.enable_cancel_migrate_unit = enable_cancel_migrate_unit
        # The return result of the request.
        self.enable_migrate_unit = enable_migrate_unit
        # The return result of the request.
        self.manual_migrate = manual_migrate
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.node_id = node_id
        # Alibaba Cloud CLI
        self.unit_cpu = unit_cpu
        # The operation that you want to perform.   
        # Set the value to **DescribeInstanceTopology**.
        self.unit_data_size = unit_data_size
        # The topology of the cluster.
        self.unit_id = unit_id
        # The ID of the tenant.
        self.unit_memory = unit_memory
        # You can call this operation to query the topology of an OceanBase cluster.
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
        # The maximum disk usage, in percentage.
        self.is_primary_tenant_zone = is_primary_tenant_zone
        # The server with the highest disk usage.
        self.tenant_zone_id = tenant_zone_id
        # The information of zones.
        self.tenant_zone_role = tenant_zone_role
        # The information about the storage resources.
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
        # The server with the highest disk usage.
        self.primary_zone_deploy_type = primary_zone_deploy_type
        # The information about the memory resources of the node.
        self.tenant_cpu = tenant_cpu
        # The name of the tenant.
        self.tenant_deploy_type = tenant_deploy_type
        # The size of used memory of the node, in GB.
        self.tenant_id = tenant_id
        # The total storage space of the node, in GB.
        self.tenant_memory = tenant_memory
        # The size of used storage space of the node, in GB.
        self.tenant_mode = tenant_mode
        # The total memory size of the node, in GB.
        self.tenant_name = tenant_name
        # The size of used memory of the node, in GB.
        self.tenant_status = tenant_status
        # The number of CPU cores of the tenant.
        self.tenant_unit_num = tenant_unit_num
        # The information about the storage resources of the node.
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
        # The size of used storage space of the node, in GB.
        self.total_cpu = total_cpu
        # Indicates whether migration can be performed.
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
        # The deployment type of the primary zone.
        self.total_disk_size = total_disk_size
        # The status of the tenant.   
        # - PENDING_CREATE: The tenant is being created.   
        # - RESTORE: The tenant is being recovered.   
        # - ONLINE: The tenant is running.   
        # - SPEC_MODIFYING: The specification of the tenant is being modified.   
        # - ALLOCATING_INTERNET_ADDRESS: An Internet address is being allocated.   
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The Internet address is being disabled.   
        # - PRIMARY_ZONE_MODIFYING: The tenant is switching to a new primary zone.   
        # - PARAMETER_MODIFYING: Parameters are being modified.   
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.
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
        # The ID of the replica node.
        self.total_memory = total_memory
        # The information of node resources.
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
        # The memory size of the tenant, in GB.
        self.cpu = cpu
        # The information about the CPU resources of the node.
        self.disk_size = disk_size
        # The role to access the zone. Valid values:   
        #  - ReadWrite: a role that has the read and write privileges.
        #  - ReadOnly: a role that has only the read-only privilege.
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
        # The information of zones.
        self.node_copy_id = node_copy_id
        # The ID of the resource unit.
        self.node_id = node_id
        # The ID of the node.
        self.node_resource = node_resource
        # The ID of the OBServer where the resource unit resides.
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
        # DescribeInstanceTopology
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
        # The ID of the region.
        self.nodes = nodes
        # The zone information of the cluster.
        self.region = region
        # The information about the memory resources of the node.
        self.zone_disk = zone_disk
        # The information of the tenant.
        self.zone_id = zone_id
        # Example 1
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
        # The total number of CPU cores for the node.
        self.tenants = tenants
        # The information about resource units.
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
        # The number of CPU cores used by the node.
        self.instance_topology = instance_topology
        # The information about the CPU resources of the node.
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
        # The number of CPU cores used in the cluster.
        self.instance_id = instance_id
        # The size of used memory in the cluster, in GB.
        self.instance_name = instance_name
        # The total memory size of the cluster, in GB.
        self.page_number = page_number
        # The information about the memory resources of the cluster.
        self.page_size = page_size
        # The number of CPU cores of each replica node in the cluster.
        self.resource_group_id = resource_group_id
        # The memory size of each replica node in the cluster, in GB.
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
        # The name of the OceanBase cluster.    
        # It must be 1 to 20 characters in length.   
        # If this parameter is not specified, the value is the instance ID of the cluster by default.
        self.total_cpu = total_cpu
        # The data replica distribution mode of the cluster. Valid values:    
        # 
        # - n: indicates the single-IDC mode.  
        # - n-n: indicates the dual-IDC mode.  
        # - n-n-n: indicates the multi-IDC mode. The integer n represents the number of OBServer nodes in each IDC.
        self.unit_cpu = unit_cpu
        # The search keyword.
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
        # The request ID.
        self.total_disk_size = total_disk_size
        # Example 1
        self.unit_disk_size = unit_disk_size
        # $.parameters[7].schema.example
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
        # The number of CPU cores of the cluster.
        self.total_memory = total_memory
        # The size of used storage space of the cluster, in GB.
        self.unit_memory = unit_memory
        # The size of used memory in the cluster, in GB.
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
        # Indicates whether new nodes can be added.
        self.cpu = cpu
        # The time elapsed since the expiration of the cluster, in seconds.
        self.disk_size = disk_size
        # The status of the cluster. Valid values:   
        # - PENDING_CREATE: The cluster is being created.  
        # - ONLINE: The cluster is running.  
        # - TENANT_CREATING: The tenant is being created.  
        # - TENANT_SPEC_MODIFYING: The tenant specifications are being modified.  
        # - EXPANDING: Nodes are being added to the cluster to increase its capacity.  
        # - REDUCING: Nodes are being removed from the cluster to reduce its capacity.  
        # - SPEC_UPGRADING: The service plan is being upgraded.  
        # - DISK_UPGRADING: The storage space is being expanded.  
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.  
        # - PARAMETER_MODIFYING: Parameters are being modified.  
        # - SSL_MODIFYING: The SSL certificate is being changed.  
        # - PREPAID_EXPIRE_CLOSED: The payment is overdue. This parameter is valid for a cluster whose billing method is set to PREPAY.  
        # - ARREARS_CLOSED: The payment is overdue. This parameter is valid for a cluster whose billing method is set to POSTPAY.  
        # - PENDING_DELETE: The cluster is being deleted.   
        # Generally, the cluster is in the ONLINE state.
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
        instance_role: str = None,
        instance_type: str = None,
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
        # The time in UTC when the cluster expires.
        self.available_zones = available_zones
        # The storage space of each replica node in the cluster, in GB.
        self.commodity_code = commodity_code
        # The product code of the OceanBase cluster.   
        # - oceanbase_oceanbasepre_public_cn: indicates an OceanBase cluster that is billed based on the subscription plan and that is deployed in a China site.  
        # - oceanbase_oceanbasepost_public_cn: indicates an OceanBase cluster that is billed based on the pay-as-you-go plan and that is deployed in a China site.  
        # - oceanbase_obpre_public_intl: indicates an OceanBase cluster that is billed based on the subscription plan and that is deployed in an international site.
        self.cpu = cpu
        # The number of OceanBase clusters queried.
        self.create_time = create_time
        # The request ID.
        self.deploy_mode = deploy_mode
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.deploy_type = deploy_type
        # The information about the memory resources of the cluster.
        self.disk_size = disk_size
        # The number of CPU cores used in the cluster.
        self.disk_type = disk_type
        # The ID of the OceanBase cluster.
        self.enable_upgrade_nodes = enable_upgrade_nodes
        # The whitelist information of the cluster.
        self.expire_seconds = expire_seconds
        # The information about the storage resources of the cluster.
        self.expire_time = expire_time
        # The instance type.
        self.instance_class = instance_class
        # The total storage space of the cluster, in GB.
        self.instance_id = instance_id
        # The return result of the request.
        self.instance_name = instance_name
        self.instance_role = instance_role
        # You can call this operation to obtain the list of OceanBase clusters.
        self.instance_type = instance_type
        # The return result of the request.
        self.maintain_time = maintain_time
        # The information about the CPU resources of the cluster.
        self.mem = mem
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.pay_type = pay_type
        # The type of the storage disk where the cluster is deployed.   
        # The default value is cloud_essd_pl1, which indicates an ESSD cloud disk.
        self.resource = resource
        # The number of OceanBase clusters queried.
        self.resource_group_id = resource_group_id
        # The number of the page to return.    
        # 
        # - Start value: 1 
        # - Default value: 1
        self.security_ips = security_ips
        # The billing method for the OceanBase cluster. Valid values:  
        # - PREPAY: the subscription billing method.  
        # - POSTPAY: the pay-as-you-go billing method.
        self.series = series
        # The number of resource units in the cluster.
        self.state = state
        # The number of resource units in the cluster.
        self.used_disk_size = used_disk_size
        # The total number of CPU cores of the cluster.
        self.version = version
        # vpcId
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
        if self.instance_role is not None:
            result['InstanceRole'] = self.instance_role
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
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
        if m.get('InstanceRole') is not None:
            self.instance_role = m.get('InstanceRole')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
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
        # The total storage space of the cluster, in GB.
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
        # $.parameters[7].schema.description
        self.end_time = end_time
        # The list of nodes.
        self.instance_id = instance_id
        # $.parameters[7].schema.enumValueTitles
        self.metrics = metrics
        # $.parameters[10].schema.description
        self.node_id_list = node_id_list
        # $.parameters[8].schema.example
        self.node_name = node_name
        # $.parameters[6].schema.description
        self.page_number = page_number
        # The ID of the tenant.
        self.page_size = page_size
        # $.parameters[9].schema.example
        self.start_time = start_time
        # $.parameters[6].schema.enumValueTitles
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
        # You can call this operation to query the detailed metrics information of an OceanBase Database node.
        self.request_id = request_id
        # ```
        # http(s)://[Endpoint]/?Action=DescribeNodeMetrics
        # &InstanceId=ob317v4uif****\
        # &PageSize=10
        # &PageNumber=1
        # &TenantId=ob2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &Metrics=tps
        # &NodeName=i-bp16niirq4zdmgvm****\
        # &NodeIdList=["i-bp19y05uq6xpacyqnlrc","i-bp1blcr3htr3g3u2vqvu","i-bp1392ikhayhr3hi4fli"]
        # &Common request parameters
        # ```
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


class DescribeOasAnomalySQLListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        current: int = None,
        db_name: str = None,
        end_time: str = None,
        filter_condition: str = None,
        instance_id: str = None,
        node_ip: str = None,
        page_size: int = None,
        search_key_word: str = None,
        search_param: str = None,
        search_rule: str = None,
        search_value: str = None,
        sql_id: str = None,
        sql_text_length: int = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.accept_language = accept_language
        self.current = current
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition = filter_condition
        self.instance_id = instance_id
        self.node_ip = node_ip
        self.page_size = page_size
        self.search_key_word = search_key_word
        self.search_param = search_param
        self.search_rule = search_rule
        self.search_value = search_value
        # SQL ID。
        self.sql_id = sql_id
        self.sql_text_length = sql_text_length
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
        if self.current is not None:
            result['Current'] = self.current
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_condition is not None:
            result['FilterCondition'] = self.filter_condition
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_param is not None:
            result['SearchParam'] = self.search_param
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text_length is not None:
            result['SqlTextLength'] = self.sql_text_length
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterCondition') is not None:
            self.filter_condition = m.get('FilterCondition')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParam') is not None:
            self.search_param = m.get('SearchParam')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlTextLength') is not None:
            self.sql_text_length = m.get('SqlTextLength')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOasAnomalySQLListResponseBodyData(TeaModel):
    def __init__(
        self,
        avg_cpu_time: float = None,
        avg_elapsed_time: float = None,
        avg_get_plan_time: float = None,
        cpu_time: float = None,
        db_name: str = None,
        diag_types: List[str] = None,
        diagnosis: str = None,
        executions: float = None,
        last_executed_time: float = None,
        risk_level: str = None,
        sql_id: str = None,
        sql_text_short: str = None,
        suggestion: str = None,
        sum_elapsed_time: str = None,
        user_name: str = None,
    ):
        self.avg_cpu_time = avg_cpu_time
        self.avg_elapsed_time = avg_elapsed_time
        self.avg_get_plan_time = avg_get_plan_time
        self.cpu_time = cpu_time
        self.db_name = db_name
        self.diag_types = diag_types
        self.diagnosis = diagnosis
        self.executions = executions
        self.last_executed_time = last_executed_time
        self.risk_level = risk_level
        # SQL ID。
        self.sql_id = sql_id
        self.sql_text_short = sql_text_short
        self.suggestion = suggestion
        self.sum_elapsed_time = sum_elapsed_time
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.avg_elapsed_time is not None:
            result['AvgElapsedTime'] = self.avg_elapsed_time
        if self.avg_get_plan_time is not None:
            result['AvgGetPlanTime'] = self.avg_get_plan_time
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.diag_types is not None:
            result['DiagTypes'] = self.diag_types
        if self.diagnosis is not None:
            result['Diagnosis'] = self.diagnosis
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.last_executed_time is not None:
            result['LastExecutedTime'] = self.last_executed_time
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text_short is not None:
            result['SqlTextShort'] = self.sql_text_short
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.sum_elapsed_time is not None:
            result['SumElapsedTime'] = self.sum_elapsed_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('AvgElapsedTime') is not None:
            self.avg_elapsed_time = m.get('AvgElapsedTime')
        if m.get('AvgGetPlanTime') is not None:
            self.avg_get_plan_time = m.get('AvgGetPlanTime')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DiagTypes') is not None:
            self.diag_types = m.get('DiagTypes')
        if m.get('Diagnosis') is not None:
            self.diagnosis = m.get('Diagnosis')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('LastExecutedTime') is not None:
            self.last_executed_time = m.get('LastExecutedTime')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlTextShort') is not None:
            self.sql_text_short = m.get('SqlTextShort')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('SumElapsedTime') is not None:
            self.sum_elapsed_time = m.get('SumElapsedTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeOasAnomalySQLListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeOasAnomalySQLListResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.request_id = request_id
        self.total_count = total_count

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeOasAnomalySQLListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOasAnomalySQLListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOasAnomalySQLListResponseBody = None,
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
            temp_model = DescribeOasAnomalySQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOasSQLDetailsRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        instance_id: str = None,
        sql_id: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.db_name = db_name
        self.end_time = end_time
        self.instance_id = instance_id
        # SQL ID。
        self.sql_id = sql_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOasSQLDetailsResponseBodyData(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        fulltext: str = None,
        statement: str = None,
        tables: List[str] = None,
        user_name: str = None,
    ):
        self.db_name = db_name
        self.fulltext = fulltext
        self.statement = statement
        self.tables = tables
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
        if self.fulltext is not None:
            result['Fulltext'] = self.fulltext
        if self.statement is not None:
            result['Statement'] = self.statement
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('Fulltext') is not None:
            self.fulltext = m.get('Fulltext')
        if m.get('Statement') is not None:
            self.statement = m.get('Statement')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeOasSQLDetailsResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeOasSQLDetailsResponseBodyData = None,
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
            temp_model = DescribeOasSQLDetailsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOasSQLDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOasSQLDetailsResponseBody = None,
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
            temp_model = DescribeOasSQLDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOasSQLHistoryListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        db_name: str = None,
        end_time: str = None,
        instance_id: str = None,
        node_ip: str = None,
        sql_id: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.accept_language = accept_language
        self.db_name = db_name
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_ip = node_ip
        # SQL ID。
        self.sql_id = sql_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOasSQLHistoryListResponseBodyData(TeaModel):
    def __init__(
        self,
        avg_affected_rows: int = None,
        avg_application_wait_time: float = None,
        avg_block_cache_hit: int = None,
        avg_block_index_cache_hit: int = None,
        avg_bloom_filter_cache_hit: int = None,
        avg_concurrency_wait_time: float = None,
        avg_cpu_time: float = None,
        avg_decode_time: float = None,
        avg_disk_reads: int = None,
        avg_elapsed_time: float = None,
        avg_execute_time: float = None,
        avg_executor_rpc_count: float = None,
        avg_expected_worker_count: float = None,
        avg_get_plan_time: float = None,
        avg_logical_reads: int = None,
        avg_memstore_read_rows: int = None,
        avg_net_time: float = None,
        avg_net_wait_time: float = None,
        avg_partition_count: float = None,
        avg_queue_time: float = None,
        avg_return_rows: int = None,
        avg_row_cache_hit: int = None,
        avg_rpc_count: int = None,
        avg_schedule_time: float = None,
        avg_ssstore_read_rows: int = None,
        avg_used_worker_count: float = None,
        avg_user_io_wait_time: float = None,
        avg_wait_count: float = None,
        avg_wait_time: float = None,
        db_name: str = None,
        dist_plan_percentage: float = None,
        exec_ps: float = None,
        executions: int = None,
        fail_count: int = None,
        fail_percentage: float = None,
        local_plan_percentage: float = None,
        max_affected_rows: float = None,
        max_application_wait_time: float = None,
        max_concurrency_wait_time: float = None,
        max_cpu_time: float = None,
        max_disk_reads: float = None,
        max_elapsed_time: float = None,
        max_return_rows: float = None,
        max_user_io_wait_time: float = None,
        max_wait_time: float = None,
        miss_plan_percentage: float = None,
        miss_plans: int = None,
        remote_plan_percentage: float = None,
        remote_plans: int = None,
        ret_code_4012count: float = None,
        ret_code_4013count: float = None,
        ret_code_5001count: float = None,
        ret_code_5024count: float = None,
        ret_code_5167count: float = None,
        ret_code_5217count: float = None,
        ret_code_6002count: float = None,
        retry_count: int = None,
        sqlid: str = None,
        server: str = None,
        strong_consistency_percentage: float = None,
        sum_elapsed_time: float = None,
        sum_logical_reads: float = None,
        sum_wait_time: float = None,
        table_scan_percentage: float = None,
        timestamp: str = None,
        user_name: str = None,
        weak_consistency_percentage: float = None,
    ):
        self.avg_affected_rows = avg_affected_rows
        self.avg_application_wait_time = avg_application_wait_time
        self.avg_block_cache_hit = avg_block_cache_hit
        self.avg_block_index_cache_hit = avg_block_index_cache_hit
        self.avg_bloom_filter_cache_hit = avg_bloom_filter_cache_hit
        self.avg_concurrency_wait_time = avg_concurrency_wait_time
        self.avg_cpu_time = avg_cpu_time
        self.avg_decode_time = avg_decode_time
        self.avg_disk_reads = avg_disk_reads
        self.avg_elapsed_time = avg_elapsed_time
        self.avg_execute_time = avg_execute_time
        self.avg_executor_rpc_count = avg_executor_rpc_count
        self.avg_expected_worker_count = avg_expected_worker_count
        self.avg_get_plan_time = avg_get_plan_time
        self.avg_logical_reads = avg_logical_reads
        self.avg_memstore_read_rows = avg_memstore_read_rows
        self.avg_net_time = avg_net_time
        self.avg_net_wait_time = avg_net_wait_time
        self.avg_partition_count = avg_partition_count
        self.avg_queue_time = avg_queue_time
        self.avg_return_rows = avg_return_rows
        self.avg_row_cache_hit = avg_row_cache_hit
        self.avg_rpc_count = avg_rpc_count
        self.avg_schedule_time = avg_schedule_time
        self.avg_ssstore_read_rows = avg_ssstore_read_rows
        self.avg_used_worker_count = avg_used_worker_count
        self.avg_user_io_wait_time = avg_user_io_wait_time
        self.avg_wait_count = avg_wait_count
        self.avg_wait_time = avg_wait_time
        self.db_name = db_name
        self.dist_plan_percentage = dist_plan_percentage
        self.exec_ps = exec_ps
        self.executions = executions
        self.fail_count = fail_count
        self.fail_percentage = fail_percentage
        self.local_plan_percentage = local_plan_percentage
        self.max_affected_rows = max_affected_rows
        self.max_application_wait_time = max_application_wait_time
        self.max_concurrency_wait_time = max_concurrency_wait_time
        self.max_cpu_time = max_cpu_time
        self.max_disk_reads = max_disk_reads
        self.max_elapsed_time = max_elapsed_time
        self.max_return_rows = max_return_rows
        self.max_user_io_wait_time = max_user_io_wait_time
        self.max_wait_time = max_wait_time
        self.miss_plan_percentage = miss_plan_percentage
        self.miss_plans = miss_plans
        self.remote_plan_percentage = remote_plan_percentage
        self.remote_plans = remote_plans
        self.ret_code_4012count = ret_code_4012count
        self.ret_code_4013count = ret_code_4013count
        self.ret_code_5001count = ret_code_5001count
        self.ret_code_5024count = ret_code_5024count
        self.ret_code_5167count = ret_code_5167count
        self.ret_code_5217count = ret_code_5217count
        self.ret_code_6002count = ret_code_6002count
        self.retry_count = retry_count
        # SQL ID
        self.sqlid = sqlid
        self.server = server
        self.strong_consistency_percentage = strong_consistency_percentage
        self.sum_elapsed_time = sum_elapsed_time
        self.sum_logical_reads = sum_logical_reads
        self.sum_wait_time = sum_wait_time
        self.table_scan_percentage = table_scan_percentage
        self.timestamp = timestamp
        self.user_name = user_name
        self.weak_consistency_percentage = weak_consistency_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_affected_rows is not None:
            result['AvgAffectedRows'] = self.avg_affected_rows
        if self.avg_application_wait_time is not None:
            result['AvgApplicationWaitTime'] = self.avg_application_wait_time
        if self.avg_block_cache_hit is not None:
            result['AvgBlockCacheHit'] = self.avg_block_cache_hit
        if self.avg_block_index_cache_hit is not None:
            result['AvgBlockIndexCacheHit'] = self.avg_block_index_cache_hit
        if self.avg_bloom_filter_cache_hit is not None:
            result['AvgBloomFilterCacheHit'] = self.avg_bloom_filter_cache_hit
        if self.avg_concurrency_wait_time is not None:
            result['AvgConcurrencyWaitTime'] = self.avg_concurrency_wait_time
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.avg_decode_time is not None:
            result['AvgDecodeTime'] = self.avg_decode_time
        if self.avg_disk_reads is not None:
            result['AvgDiskReads'] = self.avg_disk_reads
        if self.avg_elapsed_time is not None:
            result['AvgElapsedTime'] = self.avg_elapsed_time
        if self.avg_execute_time is not None:
            result['AvgExecuteTime'] = self.avg_execute_time
        if self.avg_executor_rpc_count is not None:
            result['AvgExecutorRpcCount'] = self.avg_executor_rpc_count
        if self.avg_expected_worker_count is not None:
            result['AvgExpectedWorkerCount'] = self.avg_expected_worker_count
        if self.avg_get_plan_time is not None:
            result['AvgGetPlanTime'] = self.avg_get_plan_time
        if self.avg_logical_reads is not None:
            result['AvgLogicalReads'] = self.avg_logical_reads
        if self.avg_memstore_read_rows is not None:
            result['AvgMemstoreReadRows'] = self.avg_memstore_read_rows
        if self.avg_net_time is not None:
            result['AvgNetTime'] = self.avg_net_time
        if self.avg_net_wait_time is not None:
            result['AvgNetWaitTime'] = self.avg_net_wait_time
        if self.avg_partition_count is not None:
            result['AvgPartitionCount'] = self.avg_partition_count
        if self.avg_queue_time is not None:
            result['AvgQueueTime'] = self.avg_queue_time
        if self.avg_return_rows is not None:
            result['AvgReturnRows'] = self.avg_return_rows
        if self.avg_row_cache_hit is not None:
            result['AvgRowCacheHit'] = self.avg_row_cache_hit
        if self.avg_rpc_count is not None:
            result['AvgRpcCount'] = self.avg_rpc_count
        if self.avg_schedule_time is not None:
            result['AvgScheduleTime'] = self.avg_schedule_time
        if self.avg_ssstore_read_rows is not None:
            result['AvgSsstoreReadRows'] = self.avg_ssstore_read_rows
        if self.avg_used_worker_count is not None:
            result['AvgUsedWorkerCount'] = self.avg_used_worker_count
        if self.avg_user_io_wait_time is not None:
            result['AvgUserIoWaitTime'] = self.avg_user_io_wait_time
        if self.avg_wait_count is not None:
            result['AvgWaitCount'] = self.avg_wait_count
        if self.avg_wait_time is not None:
            result['AvgWaitTime'] = self.avg_wait_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.dist_plan_percentage is not None:
            result['DistPlanPercentage'] = self.dist_plan_percentage
        if self.exec_ps is not None:
            result['ExecPs'] = self.exec_ps
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.fail_percentage is not None:
            result['FailPercentage'] = self.fail_percentage
        if self.local_plan_percentage is not None:
            result['LocalPlanPercentage'] = self.local_plan_percentage
        if self.max_affected_rows is not None:
            result['MaxAffectedRows'] = self.max_affected_rows
        if self.max_application_wait_time is not None:
            result['MaxApplicationWaitTime'] = self.max_application_wait_time
        if self.max_concurrency_wait_time is not None:
            result['MaxConcurrencyWaitTime'] = self.max_concurrency_wait_time
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_disk_reads is not None:
            result['MaxDiskReads'] = self.max_disk_reads
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.max_return_rows is not None:
            result['MaxReturnRows'] = self.max_return_rows
        if self.max_user_io_wait_time is not None:
            result['MaxUserIoWaitTime'] = self.max_user_io_wait_time
        if self.max_wait_time is not None:
            result['MaxWaitTime'] = self.max_wait_time
        if self.miss_plan_percentage is not None:
            result['MissPlanPercentage'] = self.miss_plan_percentage
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.remote_plan_percentage is not None:
            result['RemotePlanPercentage'] = self.remote_plan_percentage
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.ret_code_4012count is not None:
            result['RetCode4012Count'] = self.ret_code_4012count
        if self.ret_code_4013count is not None:
            result['RetCode4013Count'] = self.ret_code_4013count
        if self.ret_code_5001count is not None:
            result['RetCode5001Count'] = self.ret_code_5001count
        if self.ret_code_5024count is not None:
            result['RetCode5024Count'] = self.ret_code_5024count
        if self.ret_code_5167count is not None:
            result['RetCode5167Count'] = self.ret_code_5167count
        if self.ret_code_5217count is not None:
            result['RetCode5217Count'] = self.ret_code_5217count
        if self.ret_code_6002count is not None:
            result['RetCode6002Count'] = self.ret_code_6002count
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.sqlid is not None:
            result['SQLId'] = self.sqlid
        if self.server is not None:
            result['Server'] = self.server
        if self.strong_consistency_percentage is not None:
            result['StrongConsistencyPercentage'] = self.strong_consistency_percentage
        if self.sum_elapsed_time is not None:
            result['SumElapsedTime'] = self.sum_elapsed_time
        if self.sum_logical_reads is not None:
            result['SumLogicalReads'] = self.sum_logical_reads
        if self.sum_wait_time is not None:
            result['SumWaitTime'] = self.sum_wait_time
        if self.table_scan_percentage is not None:
            result['TableScanPercentage'] = self.table_scan_percentage
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.weak_consistency_percentage is not None:
            result['WeakConsistencyPercentage'] = self.weak_consistency_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgAffectedRows') is not None:
            self.avg_affected_rows = m.get('AvgAffectedRows')
        if m.get('AvgApplicationWaitTime') is not None:
            self.avg_application_wait_time = m.get('AvgApplicationWaitTime')
        if m.get('AvgBlockCacheHit') is not None:
            self.avg_block_cache_hit = m.get('AvgBlockCacheHit')
        if m.get('AvgBlockIndexCacheHit') is not None:
            self.avg_block_index_cache_hit = m.get('AvgBlockIndexCacheHit')
        if m.get('AvgBloomFilterCacheHit') is not None:
            self.avg_bloom_filter_cache_hit = m.get('AvgBloomFilterCacheHit')
        if m.get('AvgConcurrencyWaitTime') is not None:
            self.avg_concurrency_wait_time = m.get('AvgConcurrencyWaitTime')
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('AvgDecodeTime') is not None:
            self.avg_decode_time = m.get('AvgDecodeTime')
        if m.get('AvgDiskReads') is not None:
            self.avg_disk_reads = m.get('AvgDiskReads')
        if m.get('AvgElapsedTime') is not None:
            self.avg_elapsed_time = m.get('AvgElapsedTime')
        if m.get('AvgExecuteTime') is not None:
            self.avg_execute_time = m.get('AvgExecuteTime')
        if m.get('AvgExecutorRpcCount') is not None:
            self.avg_executor_rpc_count = m.get('AvgExecutorRpcCount')
        if m.get('AvgExpectedWorkerCount') is not None:
            self.avg_expected_worker_count = m.get('AvgExpectedWorkerCount')
        if m.get('AvgGetPlanTime') is not None:
            self.avg_get_plan_time = m.get('AvgGetPlanTime')
        if m.get('AvgLogicalReads') is not None:
            self.avg_logical_reads = m.get('AvgLogicalReads')
        if m.get('AvgMemstoreReadRows') is not None:
            self.avg_memstore_read_rows = m.get('AvgMemstoreReadRows')
        if m.get('AvgNetTime') is not None:
            self.avg_net_time = m.get('AvgNetTime')
        if m.get('AvgNetWaitTime') is not None:
            self.avg_net_wait_time = m.get('AvgNetWaitTime')
        if m.get('AvgPartitionCount') is not None:
            self.avg_partition_count = m.get('AvgPartitionCount')
        if m.get('AvgQueueTime') is not None:
            self.avg_queue_time = m.get('AvgQueueTime')
        if m.get('AvgReturnRows') is not None:
            self.avg_return_rows = m.get('AvgReturnRows')
        if m.get('AvgRowCacheHit') is not None:
            self.avg_row_cache_hit = m.get('AvgRowCacheHit')
        if m.get('AvgRpcCount') is not None:
            self.avg_rpc_count = m.get('AvgRpcCount')
        if m.get('AvgScheduleTime') is not None:
            self.avg_schedule_time = m.get('AvgScheduleTime')
        if m.get('AvgSsstoreReadRows') is not None:
            self.avg_ssstore_read_rows = m.get('AvgSsstoreReadRows')
        if m.get('AvgUsedWorkerCount') is not None:
            self.avg_used_worker_count = m.get('AvgUsedWorkerCount')
        if m.get('AvgUserIoWaitTime') is not None:
            self.avg_user_io_wait_time = m.get('AvgUserIoWaitTime')
        if m.get('AvgWaitCount') is not None:
            self.avg_wait_count = m.get('AvgWaitCount')
        if m.get('AvgWaitTime') is not None:
            self.avg_wait_time = m.get('AvgWaitTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DistPlanPercentage') is not None:
            self.dist_plan_percentage = m.get('DistPlanPercentage')
        if m.get('ExecPs') is not None:
            self.exec_ps = m.get('ExecPs')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('FailPercentage') is not None:
            self.fail_percentage = m.get('FailPercentage')
        if m.get('LocalPlanPercentage') is not None:
            self.local_plan_percentage = m.get('LocalPlanPercentage')
        if m.get('MaxAffectedRows') is not None:
            self.max_affected_rows = m.get('MaxAffectedRows')
        if m.get('MaxApplicationWaitTime') is not None:
            self.max_application_wait_time = m.get('MaxApplicationWaitTime')
        if m.get('MaxConcurrencyWaitTime') is not None:
            self.max_concurrency_wait_time = m.get('MaxConcurrencyWaitTime')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxDiskReads') is not None:
            self.max_disk_reads = m.get('MaxDiskReads')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MaxReturnRows') is not None:
            self.max_return_rows = m.get('MaxReturnRows')
        if m.get('MaxUserIoWaitTime') is not None:
            self.max_user_io_wait_time = m.get('MaxUserIoWaitTime')
        if m.get('MaxWaitTime') is not None:
            self.max_wait_time = m.get('MaxWaitTime')
        if m.get('MissPlanPercentage') is not None:
            self.miss_plan_percentage = m.get('MissPlanPercentage')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('RemotePlanPercentage') is not None:
            self.remote_plan_percentage = m.get('RemotePlanPercentage')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetCode4012Count') is not None:
            self.ret_code_4012count = m.get('RetCode4012Count')
        if m.get('RetCode4013Count') is not None:
            self.ret_code_4013count = m.get('RetCode4013Count')
        if m.get('RetCode5001Count') is not None:
            self.ret_code_5001count = m.get('RetCode5001Count')
        if m.get('RetCode5024Count') is not None:
            self.ret_code_5024count = m.get('RetCode5024Count')
        if m.get('RetCode5167Count') is not None:
            self.ret_code_5167count = m.get('RetCode5167Count')
        if m.get('RetCode5217Count') is not None:
            self.ret_code_5217count = m.get('RetCode5217Count')
        if m.get('RetCode6002Count') is not None:
            self.ret_code_6002count = m.get('RetCode6002Count')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('SQLId') is not None:
            self.sqlid = m.get('SQLId')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StrongConsistencyPercentage') is not None:
            self.strong_consistency_percentage = m.get('StrongConsistencyPercentage')
        if m.get('SumElapsedTime') is not None:
            self.sum_elapsed_time = m.get('SumElapsedTime')
        if m.get('SumLogicalReads') is not None:
            self.sum_logical_reads = m.get('SumLogicalReads')
        if m.get('SumWaitTime') is not None:
            self.sum_wait_time = m.get('SumWaitTime')
        if m.get('TableScanPercentage') is not None:
            self.table_scan_percentage = m.get('TableScanPercentage')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WeakConsistencyPercentage') is not None:
            self.weak_consistency_percentage = m.get('WeakConsistencyPercentage')
        return self


class DescribeOasSQLHistoryListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeOasSQLHistoryListResponseBodyData] = None,
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
                temp_model = DescribeOasSQLHistoryListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOasSQLHistoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOasSQLHistoryListResponseBody = None,
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
            temp_model = DescribeOasSQLHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOasSQLPlansRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        db_name: str = None,
        end_time: str = None,
        instance_id: str = None,
        sql_id: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.accept_language = accept_language
        self.db_name = db_name
        self.end_time = end_time
        self.instance_id = instance_id
        # SQL ID。
        self.sql_id = sql_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOasSQLPlansResponseBodyDataPlanExplain(TeaModel):
    def __init__(
        self,
        plan_json_string: str = None,
    ):
        self.plan_json_string = plan_json_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_json_string is not None:
            result['PlanJsonString'] = self.plan_json_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PlanJsonString') is not None:
            self.plan_json_string = m.get('PlanJsonString')
        return self


class DescribeOasSQLPlansResponseBodyDataPlans(TeaModel):
    def __init__(
        self,
        avg_application_wait_time: float = None,
        avg_buffer_gets: float = None,
        avg_concurrency_wait_time: float = None,
        avg_cpu_time: float = None,
        avg_disk_reads: float = None,
        avg_disk_writes: float = None,
        avg_elapsed_time: float = None,
        avg_row_processed: float = None,
        avg_user_io_wait_time: float = None,
        collect_time_us: int = None,
        delayed_large_query_percentage: float = None,
        exec_ps: float = None,
        executions: int = None,
        first_load_time: str = None,
        first_load_time_us: int = None,
        hit_diagnosis: bool = None,
        hit_percentage: float = None,
        large_query_percentage: float = None,
        merged_version: int = None,
        ob_db_id: int = None,
        ob_server_id: int = None,
        outline_data: str = None,
        outline_id: int = None,
        plan_hash: str = None,
        plan_id: int = None,
        plan_size: int = None,
        plan_type: str = None,
        plan_union_hash: str = None,
        schema_version: int = None,
        server: str = None,
        server_id: int = None,
        table_scan: bool = None,
        timeout_percentage: float = None,
        uid: str = None,
    ):
        self.avg_application_wait_time = avg_application_wait_time
        self.avg_buffer_gets = avg_buffer_gets
        self.avg_concurrency_wait_time = avg_concurrency_wait_time
        self.avg_cpu_time = avg_cpu_time
        self.avg_disk_reads = avg_disk_reads
        self.avg_disk_writes = avg_disk_writes
        self.avg_elapsed_time = avg_elapsed_time
        self.avg_row_processed = avg_row_processed
        self.avg_user_io_wait_time = avg_user_io_wait_time
        self.collect_time_us = collect_time_us
        self.delayed_large_query_percentage = delayed_large_query_percentage
        self.exec_ps = exec_ps
        self.executions = executions
        self.first_load_time = first_load_time
        self.first_load_time_us = first_load_time_us
        self.hit_diagnosis = hit_diagnosis
        self.hit_percentage = hit_percentage
        self.large_query_percentage = large_query_percentage
        self.merged_version = merged_version
        self.ob_db_id = ob_db_id
        # server  ID。
        self.ob_server_id = ob_server_id
        self.outline_data = outline_data
        # Outline ID。
        self.outline_id = outline_id
        self.plan_hash = plan_hash
        self.plan_id = plan_id
        self.plan_size = plan_size
        self.plan_type = plan_type
        self.plan_union_hash = plan_union_hash
        self.schema_version = schema_version
        self.server = server
        self.server_id = server_id
        self.table_scan = table_scan
        self.timeout_percentage = timeout_percentage
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_application_wait_time is not None:
            result['AvgApplicationWaitTime'] = self.avg_application_wait_time
        if self.avg_buffer_gets is not None:
            result['AvgBufferGets'] = self.avg_buffer_gets
        if self.avg_concurrency_wait_time is not None:
            result['AvgConcurrencyWaitTime'] = self.avg_concurrency_wait_time
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.avg_disk_reads is not None:
            result['AvgDiskReads'] = self.avg_disk_reads
        if self.avg_disk_writes is not None:
            result['AvgDiskWrites'] = self.avg_disk_writes
        if self.avg_elapsed_time is not None:
            result['AvgElapsedTime'] = self.avg_elapsed_time
        if self.avg_row_processed is not None:
            result['AvgRowProcessed'] = self.avg_row_processed
        if self.avg_user_io_wait_time is not None:
            result['AvgUserIoWaitTime'] = self.avg_user_io_wait_time
        if self.collect_time_us is not None:
            result['CollectTimeUs'] = self.collect_time_us
        if self.delayed_large_query_percentage is not None:
            result['DelayedLargeQueryPercentage'] = self.delayed_large_query_percentage
        if self.exec_ps is not None:
            result['ExecPs'] = self.exec_ps
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.first_load_time is not None:
            result['FirstLoadTime'] = self.first_load_time
        if self.first_load_time_us is not None:
            result['FirstLoadTimeUs'] = self.first_load_time_us
        if self.hit_diagnosis is not None:
            result['HitDiagnosis'] = self.hit_diagnosis
        if self.hit_percentage is not None:
            result['HitPercentage'] = self.hit_percentage
        if self.large_query_percentage is not None:
            result['LargeQueryPercentage'] = self.large_query_percentage
        if self.merged_version is not None:
            result['MergedVersion'] = self.merged_version
        if self.ob_db_id is not None:
            result['ObDbId'] = self.ob_db_id
        if self.ob_server_id is not None:
            result['ObServerId'] = self.ob_server_id
        if self.outline_data is not None:
            result['OutlineData'] = self.outline_data
        if self.outline_id is not None:
            result['OutlineId'] = self.outline_id
        if self.plan_hash is not None:
            result['PlanHash'] = self.plan_hash
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_size is not None:
            result['PlanSize'] = self.plan_size
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        if self.plan_union_hash is not None:
            result['PlanUnionHash'] = self.plan_union_hash
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.server is not None:
            result['Server'] = self.server
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.table_scan is not None:
            result['TableScan'] = self.table_scan
        if self.timeout_percentage is not None:
            result['TimeoutPercentage'] = self.timeout_percentage
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgApplicationWaitTime') is not None:
            self.avg_application_wait_time = m.get('AvgApplicationWaitTime')
        if m.get('AvgBufferGets') is not None:
            self.avg_buffer_gets = m.get('AvgBufferGets')
        if m.get('AvgConcurrencyWaitTime') is not None:
            self.avg_concurrency_wait_time = m.get('AvgConcurrencyWaitTime')
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('AvgDiskReads') is not None:
            self.avg_disk_reads = m.get('AvgDiskReads')
        if m.get('AvgDiskWrites') is not None:
            self.avg_disk_writes = m.get('AvgDiskWrites')
        if m.get('AvgElapsedTime') is not None:
            self.avg_elapsed_time = m.get('AvgElapsedTime')
        if m.get('AvgRowProcessed') is not None:
            self.avg_row_processed = m.get('AvgRowProcessed')
        if m.get('AvgUserIoWaitTime') is not None:
            self.avg_user_io_wait_time = m.get('AvgUserIoWaitTime')
        if m.get('CollectTimeUs') is not None:
            self.collect_time_us = m.get('CollectTimeUs')
        if m.get('DelayedLargeQueryPercentage') is not None:
            self.delayed_large_query_percentage = m.get('DelayedLargeQueryPercentage')
        if m.get('ExecPs') is not None:
            self.exec_ps = m.get('ExecPs')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FirstLoadTime') is not None:
            self.first_load_time = m.get('FirstLoadTime')
        if m.get('FirstLoadTimeUs') is not None:
            self.first_load_time_us = m.get('FirstLoadTimeUs')
        if m.get('HitDiagnosis') is not None:
            self.hit_diagnosis = m.get('HitDiagnosis')
        if m.get('HitPercentage') is not None:
            self.hit_percentage = m.get('HitPercentage')
        if m.get('LargeQueryPercentage') is not None:
            self.large_query_percentage = m.get('LargeQueryPercentage')
        if m.get('MergedVersion') is not None:
            self.merged_version = m.get('MergedVersion')
        if m.get('ObDbId') is not None:
            self.ob_db_id = m.get('ObDbId')
        if m.get('ObServerId') is not None:
            self.ob_server_id = m.get('ObServerId')
        if m.get('OutlineData') is not None:
            self.outline_data = m.get('OutlineData')
        if m.get('OutlineId') is not None:
            self.outline_id = m.get('OutlineId')
        if m.get('PlanHash') is not None:
            self.plan_hash = m.get('PlanHash')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanSize') is not None:
            self.plan_size = m.get('PlanSize')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        if m.get('PlanUnionHash') is not None:
            self.plan_union_hash = m.get('PlanUnionHash')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('TableScan') is not None:
            self.table_scan = m.get('TableScan')
        if m.get('TimeoutPercentage') is not None:
            self.timeout_percentage = m.get('TimeoutPercentage')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeOasSQLPlansResponseBodyData(TeaModel):
    def __init__(
        self,
        avg_cpu_time: float = None,
        bounded: bool = None,
        executions: int = None,
        first_load_time: str = None,
        hit_diagnosis: bool = None,
        hit_percentage: float = None,
        merged_version: int = None,
        plan_explain: DescribeOasSQLPlansResponseBodyDataPlanExplain = None,
        plan_hash: str = None,
        plan_type: str = None,
        plan_union_hash: str = None,
        plans: List[DescribeOasSQLPlansResponseBodyDataPlans] = None,
        query_sql: str = None,
    ):
        self.avg_cpu_time = avg_cpu_time
        self.bounded = bounded
        self.executions = executions
        self.first_load_time = first_load_time
        self.hit_diagnosis = hit_diagnosis
        self.hit_percentage = hit_percentage
        self.merged_version = merged_version
        self.plan_explain = plan_explain
        self.plan_hash = plan_hash
        self.plan_type = plan_type
        self.plan_union_hash = plan_union_hash
        self.plans = plans
        self.query_sql = query_sql

    def validate(self):
        if self.plan_explain:
            self.plan_explain.validate()
        if self.plans:
            for k in self.plans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.bounded is not None:
            result['Bounded'] = self.bounded
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.first_load_time is not None:
            result['FirstLoadTime'] = self.first_load_time
        if self.hit_diagnosis is not None:
            result['HitDiagnosis'] = self.hit_diagnosis
        if self.hit_percentage is not None:
            result['HitPercentage'] = self.hit_percentage
        if self.merged_version is not None:
            result['MergedVersion'] = self.merged_version
        if self.plan_explain is not None:
            result['PlanExplain'] = self.plan_explain.to_map()
        if self.plan_hash is not None:
            result['PlanHash'] = self.plan_hash
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        if self.plan_union_hash is not None:
            result['PlanUnionHash'] = self.plan_union_hash
        result['Plans'] = []
        if self.plans is not None:
            for k in self.plans:
                result['Plans'].append(k.to_map() if k else None)
        if self.query_sql is not None:
            result['QuerySql'] = self.query_sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('Bounded') is not None:
            self.bounded = m.get('Bounded')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FirstLoadTime') is not None:
            self.first_load_time = m.get('FirstLoadTime')
        if m.get('HitDiagnosis') is not None:
            self.hit_diagnosis = m.get('HitDiagnosis')
        if m.get('HitPercentage') is not None:
            self.hit_percentage = m.get('HitPercentage')
        if m.get('MergedVersion') is not None:
            self.merged_version = m.get('MergedVersion')
        if m.get('PlanExplain') is not None:
            temp_model = DescribeOasSQLPlansResponseBodyDataPlanExplain()
            self.plan_explain = temp_model.from_map(m['PlanExplain'])
        if m.get('PlanHash') is not None:
            self.plan_hash = m.get('PlanHash')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        if m.get('PlanUnionHash') is not None:
            self.plan_union_hash = m.get('PlanUnionHash')
        self.plans = []
        if m.get('Plans') is not None:
            for k in m.get('Plans'):
                temp_model = DescribeOasSQLPlansResponseBodyDataPlans()
                self.plans.append(temp_model.from_map(k))
        if m.get('QuerySql') is not None:
            self.query_sql = m.get('QuerySql')
        return self


class DescribeOasSQLPlansResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeOasSQLPlansResponseBodyData] = None,
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
                temp_model = DescribeOasSQLPlansResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOasSQLPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOasSQLPlansResponseBody = None,
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
            temp_model = DescribeOasSQLPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOasSlowSQLListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        db_name: str = None,
        end_time: str = None,
        filter_condition: str = None,
        instance_id: str = None,
        node_ip: str = None,
        search_key_word: str = None,
        search_param: str = None,
        search_rule: str = None,
        search_value: str = None,
        sql_id: str = None,
        sql_text_length: int = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.accept_language = accept_language
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition = filter_condition
        self.instance_id = instance_id
        self.node_ip = node_ip
        self.search_key_word = search_key_word
        self.search_param = search_param
        self.search_rule = search_rule
        self.search_value = search_value
        self.sql_id = sql_id
        self.sql_text_length = sql_text_length
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_param is not None:
            result['SearchParam'] = self.search_param
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text_length is not None:
            result['SqlTextLength'] = self.sql_text_length
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParam') is not None:
            self.search_param = m.get('SearchParam')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlTextLength') is not None:
            self.sql_text_length = m.get('SqlTextLength')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOasSlowSQLListResponseBodyData(TeaModel):
    def __init__(
        self,
        avg_affected_rows: float = None,
        avg_application_wait_time: float = None,
        avg_block_cache_hit: float = None,
        avg_block_index_cache_hit: float = None,
        avg_bloom_filter_cache_hit: float = None,
        avg_concurrency_wait_time: float = None,
        avg_cpu_time: float = None,
        avg_decode_time: float = None,
        avg_disk_reads: float = None,
        avg_elapsed_time: float = None,
        avg_execute_time: float = None,
        avg_executor_rpc_count: float = None,
        avg_expected_worker_count: float = None,
        avg_get_plan_time: float = None,
        avg_logical_reads: float = None,
        avg_memstore_read_rows: float = None,
        avg_net_time: float = None,
        avg_net_wait_time: float = None,
        avg_partition_count: float = None,
        avg_queue_time: float = None,
        avg_return_rows: float = None,
        avg_row_cache_hit: float = None,
        avg_rpc_count: float = None,
        avg_schedule_time: float = None,
        avg_ssstore_read_rows: float = None,
        avg_used_worker_count: float = None,
        avg_user_io_wait_time: float = None,
        avg_wait_count: float = None,
        avg_wait_time: float = None,
        client_ip: str = None,
        db_name: str = None,
        dist_plan_percentage: float = None,
        exec_ps: float = None,
        executions: float = None,
        fail_count: float = None,
        fail_percentage: float = None,
        inner: bool = None,
        local_plan_percentage: float = None,
        max_affected_rows: float = None,
        max_application_wait_time: float = None,
        max_concurrency_wait_time: float = None,
        max_cpu_time: float = None,
        max_disk_reads: float = None,
        max_elapsed_time: float = None,
        max_return_rows: float = None,
        max_user_io_wait_time: float = None,
        max_wait_time: float = None,
        miss_plan_percentage: float = None,
        miss_plans: float = None,
        remote_plan_percentage: float = None,
        remote_plans: float = None,
        ret_code_4012count: int = None,
        ret_code_4013count: int = None,
        ret_code_5001count: int = None,
        ret_code_5024count: int = None,
        ret_code_5167count: int = None,
        ret_code_5217count: int = None,
        ret_code_6002count: int = None,
        retry_count: float = None,
        rpc_count: float = None,
        server: str = None,
        server_ip: str = None,
        server_port: int = None,
        sql_id: str = None,
        sql_text_short: str = None,
        sql_type: str = None,
        strong_consistency_percentage: float = None,
        sum_elapsed_time: float = None,
        sum_logical_reads: float = None,
        sum_wait_time: float = None,
        table_scan_percentage: float = None,
        total_wait_time: float = None,
        user_name: str = None,
        wait_event: str = None,
        weak_consistency_percentage: float = None,
    ):
        self.avg_affected_rows = avg_affected_rows
        self.avg_application_wait_time = avg_application_wait_time
        self.avg_block_cache_hit = avg_block_cache_hit
        self.avg_block_index_cache_hit = avg_block_index_cache_hit
        self.avg_bloom_filter_cache_hit = avg_bloom_filter_cache_hit
        self.avg_concurrency_wait_time = avg_concurrency_wait_time
        self.avg_cpu_time = avg_cpu_time
        self.avg_decode_time = avg_decode_time
        self.avg_disk_reads = avg_disk_reads
        self.avg_elapsed_time = avg_elapsed_time
        self.avg_execute_time = avg_execute_time
        self.avg_executor_rpc_count = avg_executor_rpc_count
        self.avg_expected_worker_count = avg_expected_worker_count
        self.avg_get_plan_time = avg_get_plan_time
        self.avg_logical_reads = avg_logical_reads
        self.avg_memstore_read_rows = avg_memstore_read_rows
        self.avg_net_time = avg_net_time
        self.avg_net_wait_time = avg_net_wait_time
        self.avg_partition_count = avg_partition_count
        self.avg_queue_time = avg_queue_time
        self.avg_return_rows = avg_return_rows
        self.avg_row_cache_hit = avg_row_cache_hit
        self.avg_rpc_count = avg_rpc_count
        self.avg_schedule_time = avg_schedule_time
        self.avg_ssstore_read_rows = avg_ssstore_read_rows
        self.avg_used_worker_count = avg_used_worker_count
        self.avg_user_io_wait_time = avg_user_io_wait_time
        self.avg_wait_count = avg_wait_count
        self.avg_wait_time = avg_wait_time
        self.client_ip = client_ip
        self.db_name = db_name
        self.dist_plan_percentage = dist_plan_percentage
        self.exec_ps = exec_ps
        self.executions = executions
        self.fail_count = fail_count
        self.fail_percentage = fail_percentage
        self.inner = inner
        self.local_plan_percentage = local_plan_percentage
        self.max_affected_rows = max_affected_rows
        self.max_application_wait_time = max_application_wait_time
        self.max_concurrency_wait_time = max_concurrency_wait_time
        self.max_cpu_time = max_cpu_time
        self.max_disk_reads = max_disk_reads
        self.max_elapsed_time = max_elapsed_time
        self.max_return_rows = max_return_rows
        self.max_user_io_wait_time = max_user_io_wait_time
        self.max_wait_time = max_wait_time
        self.miss_plan_percentage = miss_plan_percentage
        self.miss_plans = miss_plans
        self.remote_plan_percentage = remote_plan_percentage
        self.remote_plans = remote_plans
        self.ret_code_4012count = ret_code_4012count
        self.ret_code_4013count = ret_code_4013count
        self.ret_code_5001count = ret_code_5001count
        self.ret_code_5024count = ret_code_5024count
        self.ret_code_5167count = ret_code_5167count
        self.ret_code_5217count = ret_code_5217count
        self.ret_code_6002count = ret_code_6002count
        self.retry_count = retry_count
        self.rpc_count = rpc_count
        self.server = server
        self.server_ip = server_ip
        self.server_port = server_port
        # SQL ID。
        self.sql_id = sql_id
        self.sql_text_short = sql_text_short
        self.sql_type = sql_type
        self.strong_consistency_percentage = strong_consistency_percentage
        self.sum_elapsed_time = sum_elapsed_time
        self.sum_logical_reads = sum_logical_reads
        self.sum_wait_time = sum_wait_time
        self.table_scan_percentage = table_scan_percentage
        self.total_wait_time = total_wait_time
        self.user_name = user_name
        self.wait_event = wait_event
        self.weak_consistency_percentage = weak_consistency_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_affected_rows is not None:
            result['AvgAffectedRows'] = self.avg_affected_rows
        if self.avg_application_wait_time is not None:
            result['AvgApplicationWaitTime'] = self.avg_application_wait_time
        if self.avg_block_cache_hit is not None:
            result['AvgBlockCacheHit'] = self.avg_block_cache_hit
        if self.avg_block_index_cache_hit is not None:
            result['AvgBlockIndexCacheHit'] = self.avg_block_index_cache_hit
        if self.avg_bloom_filter_cache_hit is not None:
            result['AvgBloomFilterCacheHit'] = self.avg_bloom_filter_cache_hit
        if self.avg_concurrency_wait_time is not None:
            result['AvgConcurrencyWaitTime'] = self.avg_concurrency_wait_time
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.avg_decode_time is not None:
            result['AvgDecodeTime'] = self.avg_decode_time
        if self.avg_disk_reads is not None:
            result['AvgDiskReads'] = self.avg_disk_reads
        if self.avg_elapsed_time is not None:
            result['AvgElapsedTime'] = self.avg_elapsed_time
        if self.avg_execute_time is not None:
            result['AvgExecuteTime'] = self.avg_execute_time
        if self.avg_executor_rpc_count is not None:
            result['AvgExecutorRpcCount'] = self.avg_executor_rpc_count
        if self.avg_expected_worker_count is not None:
            result['AvgExpectedWorkerCount'] = self.avg_expected_worker_count
        if self.avg_get_plan_time is not None:
            result['AvgGetPlanTime'] = self.avg_get_plan_time
        if self.avg_logical_reads is not None:
            result['AvgLogicalReads'] = self.avg_logical_reads
        if self.avg_memstore_read_rows is not None:
            result['AvgMemstoreReadRows'] = self.avg_memstore_read_rows
        if self.avg_net_time is not None:
            result['AvgNetTime'] = self.avg_net_time
        if self.avg_net_wait_time is not None:
            result['AvgNetWaitTime'] = self.avg_net_wait_time
        if self.avg_partition_count is not None:
            result['AvgPartitionCount'] = self.avg_partition_count
        if self.avg_queue_time is not None:
            result['AvgQueueTime'] = self.avg_queue_time
        if self.avg_return_rows is not None:
            result['AvgReturnRows'] = self.avg_return_rows
        if self.avg_row_cache_hit is not None:
            result['AvgRowCacheHit'] = self.avg_row_cache_hit
        if self.avg_rpc_count is not None:
            result['AvgRpcCount'] = self.avg_rpc_count
        if self.avg_schedule_time is not None:
            result['AvgScheduleTime'] = self.avg_schedule_time
        if self.avg_ssstore_read_rows is not None:
            result['AvgSsstoreReadRows'] = self.avg_ssstore_read_rows
        if self.avg_used_worker_count is not None:
            result['AvgUsedWorkerCount'] = self.avg_used_worker_count
        if self.avg_user_io_wait_time is not None:
            result['AvgUserIoWaitTime'] = self.avg_user_io_wait_time
        if self.avg_wait_count is not None:
            result['AvgWaitCount'] = self.avg_wait_count
        if self.avg_wait_time is not None:
            result['AvgWaitTime'] = self.avg_wait_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.dist_plan_percentage is not None:
            result['DistPlanPercentage'] = self.dist_plan_percentage
        if self.exec_ps is not None:
            result['ExecPs'] = self.exec_ps
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.fail_percentage is not None:
            result['FailPercentage'] = self.fail_percentage
        if self.inner is not None:
            result['Inner'] = self.inner
        if self.local_plan_percentage is not None:
            result['LocalPlanPercentage'] = self.local_plan_percentage
        if self.max_affected_rows is not None:
            result['MaxAffectedRows'] = self.max_affected_rows
        if self.max_application_wait_time is not None:
            result['MaxApplicationWaitTime'] = self.max_application_wait_time
        if self.max_concurrency_wait_time is not None:
            result['MaxConcurrencyWaitTime'] = self.max_concurrency_wait_time
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_disk_reads is not None:
            result['MaxDiskReads'] = self.max_disk_reads
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.max_return_rows is not None:
            result['MaxReturnRows'] = self.max_return_rows
        if self.max_user_io_wait_time is not None:
            result['MaxUserIoWaitTime'] = self.max_user_io_wait_time
        if self.max_wait_time is not None:
            result['MaxWaitTime'] = self.max_wait_time
        if self.miss_plan_percentage is not None:
            result['MissPlanPercentage'] = self.miss_plan_percentage
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.remote_plan_percentage is not None:
            result['RemotePlanPercentage'] = self.remote_plan_percentage
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.ret_code_4012count is not None:
            result['RetCode4012Count'] = self.ret_code_4012count
        if self.ret_code_4013count is not None:
            result['RetCode4013Count'] = self.ret_code_4013count
        if self.ret_code_5001count is not None:
            result['RetCode5001Count'] = self.ret_code_5001count
        if self.ret_code_5024count is not None:
            result['RetCode5024Count'] = self.ret_code_5024count
        if self.ret_code_5167count is not None:
            result['RetCode5167Count'] = self.ret_code_5167count
        if self.ret_code_5217count is not None:
            result['RetCode5217Count'] = self.ret_code_5217count
        if self.ret_code_6002count is not None:
            result['RetCode6002Count'] = self.ret_code_6002count
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.rpc_count is not None:
            result['RpcCount'] = self.rpc_count
        if self.server is not None:
            result['Server'] = self.server
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text_short is not None:
            result['SqlTextShort'] = self.sql_text_short
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.strong_consistency_percentage is not None:
            result['StrongConsistencyPercentage'] = self.strong_consistency_percentage
        if self.sum_elapsed_time is not None:
            result['SumElapsedTime'] = self.sum_elapsed_time
        if self.sum_logical_reads is not None:
            result['SumLogicalReads'] = self.sum_logical_reads
        if self.sum_wait_time is not None:
            result['SumWaitTime'] = self.sum_wait_time
        if self.table_scan_percentage is not None:
            result['TableScanPercentage'] = self.table_scan_percentage
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.wait_event is not None:
            result['WaitEvent'] = self.wait_event
        if self.weak_consistency_percentage is not None:
            result['WeakConsistencyPercentage'] = self.weak_consistency_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgAffectedRows') is not None:
            self.avg_affected_rows = m.get('AvgAffectedRows')
        if m.get('AvgApplicationWaitTime') is not None:
            self.avg_application_wait_time = m.get('AvgApplicationWaitTime')
        if m.get('AvgBlockCacheHit') is not None:
            self.avg_block_cache_hit = m.get('AvgBlockCacheHit')
        if m.get('AvgBlockIndexCacheHit') is not None:
            self.avg_block_index_cache_hit = m.get('AvgBlockIndexCacheHit')
        if m.get('AvgBloomFilterCacheHit') is not None:
            self.avg_bloom_filter_cache_hit = m.get('AvgBloomFilterCacheHit')
        if m.get('AvgConcurrencyWaitTime') is not None:
            self.avg_concurrency_wait_time = m.get('AvgConcurrencyWaitTime')
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('AvgDecodeTime') is not None:
            self.avg_decode_time = m.get('AvgDecodeTime')
        if m.get('AvgDiskReads') is not None:
            self.avg_disk_reads = m.get('AvgDiskReads')
        if m.get('AvgElapsedTime') is not None:
            self.avg_elapsed_time = m.get('AvgElapsedTime')
        if m.get('AvgExecuteTime') is not None:
            self.avg_execute_time = m.get('AvgExecuteTime')
        if m.get('AvgExecutorRpcCount') is not None:
            self.avg_executor_rpc_count = m.get('AvgExecutorRpcCount')
        if m.get('AvgExpectedWorkerCount') is not None:
            self.avg_expected_worker_count = m.get('AvgExpectedWorkerCount')
        if m.get('AvgGetPlanTime') is not None:
            self.avg_get_plan_time = m.get('AvgGetPlanTime')
        if m.get('AvgLogicalReads') is not None:
            self.avg_logical_reads = m.get('AvgLogicalReads')
        if m.get('AvgMemstoreReadRows') is not None:
            self.avg_memstore_read_rows = m.get('AvgMemstoreReadRows')
        if m.get('AvgNetTime') is not None:
            self.avg_net_time = m.get('AvgNetTime')
        if m.get('AvgNetWaitTime') is not None:
            self.avg_net_wait_time = m.get('AvgNetWaitTime')
        if m.get('AvgPartitionCount') is not None:
            self.avg_partition_count = m.get('AvgPartitionCount')
        if m.get('AvgQueueTime') is not None:
            self.avg_queue_time = m.get('AvgQueueTime')
        if m.get('AvgReturnRows') is not None:
            self.avg_return_rows = m.get('AvgReturnRows')
        if m.get('AvgRowCacheHit') is not None:
            self.avg_row_cache_hit = m.get('AvgRowCacheHit')
        if m.get('AvgRpcCount') is not None:
            self.avg_rpc_count = m.get('AvgRpcCount')
        if m.get('AvgScheduleTime') is not None:
            self.avg_schedule_time = m.get('AvgScheduleTime')
        if m.get('AvgSsstoreReadRows') is not None:
            self.avg_ssstore_read_rows = m.get('AvgSsstoreReadRows')
        if m.get('AvgUsedWorkerCount') is not None:
            self.avg_used_worker_count = m.get('AvgUsedWorkerCount')
        if m.get('AvgUserIoWaitTime') is not None:
            self.avg_user_io_wait_time = m.get('AvgUserIoWaitTime')
        if m.get('AvgWaitCount') is not None:
            self.avg_wait_count = m.get('AvgWaitCount')
        if m.get('AvgWaitTime') is not None:
            self.avg_wait_time = m.get('AvgWaitTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DistPlanPercentage') is not None:
            self.dist_plan_percentage = m.get('DistPlanPercentage')
        if m.get('ExecPs') is not None:
            self.exec_ps = m.get('ExecPs')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('FailPercentage') is not None:
            self.fail_percentage = m.get('FailPercentage')
        if m.get('Inner') is not None:
            self.inner = m.get('Inner')
        if m.get('LocalPlanPercentage') is not None:
            self.local_plan_percentage = m.get('LocalPlanPercentage')
        if m.get('MaxAffectedRows') is not None:
            self.max_affected_rows = m.get('MaxAffectedRows')
        if m.get('MaxApplicationWaitTime') is not None:
            self.max_application_wait_time = m.get('MaxApplicationWaitTime')
        if m.get('MaxConcurrencyWaitTime') is not None:
            self.max_concurrency_wait_time = m.get('MaxConcurrencyWaitTime')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxDiskReads') is not None:
            self.max_disk_reads = m.get('MaxDiskReads')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MaxReturnRows') is not None:
            self.max_return_rows = m.get('MaxReturnRows')
        if m.get('MaxUserIoWaitTime') is not None:
            self.max_user_io_wait_time = m.get('MaxUserIoWaitTime')
        if m.get('MaxWaitTime') is not None:
            self.max_wait_time = m.get('MaxWaitTime')
        if m.get('MissPlanPercentage') is not None:
            self.miss_plan_percentage = m.get('MissPlanPercentage')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('RemotePlanPercentage') is not None:
            self.remote_plan_percentage = m.get('RemotePlanPercentage')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetCode4012Count') is not None:
            self.ret_code_4012count = m.get('RetCode4012Count')
        if m.get('RetCode4013Count') is not None:
            self.ret_code_4013count = m.get('RetCode4013Count')
        if m.get('RetCode5001Count') is not None:
            self.ret_code_5001count = m.get('RetCode5001Count')
        if m.get('RetCode5024Count') is not None:
            self.ret_code_5024count = m.get('RetCode5024Count')
        if m.get('RetCode5167Count') is not None:
            self.ret_code_5167count = m.get('RetCode5167Count')
        if m.get('RetCode5217Count') is not None:
            self.ret_code_5217count = m.get('RetCode5217Count')
        if m.get('RetCode6002Count') is not None:
            self.ret_code_6002count = m.get('RetCode6002Count')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('RpcCount') is not None:
            self.rpc_count = m.get('RpcCount')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlTextShort') is not None:
            self.sql_text_short = m.get('SqlTextShort')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StrongConsistencyPercentage') is not None:
            self.strong_consistency_percentage = m.get('StrongConsistencyPercentage')
        if m.get('SumElapsedTime') is not None:
            self.sum_elapsed_time = m.get('SumElapsedTime')
        if m.get('SumLogicalReads') is not None:
            self.sum_logical_reads = m.get('SumLogicalReads')
        if m.get('SumWaitTime') is not None:
            self.sum_wait_time = m.get('SumWaitTime')
        if m.get('TableScanPercentage') is not None:
            self.table_scan_percentage = m.get('TableScanPercentage')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WaitEvent') is not None:
            self.wait_event = m.get('WaitEvent')
        if m.get('WeakConsistencyPercentage') is not None:
            self.weak_consistency_percentage = m.get('WeakConsistencyPercentage')
        return self


class DescribeOasSlowSQLListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeOasSlowSQLListResponseBodyData] = None,
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
                temp_model = DescribeOasSlowSQLListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOasSlowSQLListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOasSlowSQLListResponseBody = None,
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
            temp_model = DescribeOasSlowSQLListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOasTopSQLListRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        db_name: str = None,
        end_time: str = None,
        filter_condition: str = None,
        instance_id: str = None,
        node_ip: str = None,
        search_key_word: str = None,
        search_param: str = None,
        search_rule: str = None,
        search_value: str = None,
        sql_id: str = None,
        sql_text_length: int = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.accept_language = accept_language
        self.db_name = db_name
        self.end_time = end_time
        self.filter_condition = filter_condition
        self.instance_id = instance_id
        self.node_ip = node_ip
        self.search_key_word = search_key_word
        self.search_param = search_param
        self.search_rule = search_rule
        self.search_value = search_value
        self.sql_id = sql_id
        self.sql_text_length = sql_text_length
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.search_key_word is not None:
            result['SearchKeyWord'] = self.search_key_word
        if self.search_param is not None:
            result['SearchParam'] = self.search_param
        if self.search_rule is not None:
            result['SearchRule'] = self.search_rule
        if self.search_value is not None:
            result['SearchValue'] = self.search_value
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text_length is not None:
            result['SqlTextLength'] = self.sql_text_length
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('SearchKeyWord') is not None:
            self.search_key_word = m.get('SearchKeyWord')
        if m.get('SearchParam') is not None:
            self.search_param = m.get('SearchParam')
        if m.get('SearchRule') is not None:
            self.search_rule = m.get('SearchRule')
        if m.get('SearchValue') is not None:
            self.search_value = m.get('SearchValue')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlTextLength') is not None:
            self.sql_text_length = m.get('SqlTextLength')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeOasTopSQLListResponseBodyData(TeaModel):
    def __init__(
        self,
        avg_affected_rows: float = None,
        avg_application_wait_time: float = None,
        avg_block_cache_hit: float = None,
        avg_block_index_cache_hit: float = None,
        avg_bloom_filter_cache_hit: float = None,
        avg_concurrency_wait_time: float = None,
        avg_cpu_time: float = None,
        avg_decode_time: float = None,
        avg_disk_reads: float = None,
        avg_elapsed_time: float = None,
        avg_execute_time: float = None,
        avg_executor_rpc_count: float = None,
        avg_expected_worker_count: float = None,
        avg_get_plan_time: float = None,
        avg_logical_reads: float = None,
        avg_memstore_read_rows: float = None,
        avg_net_time: float = None,
        avg_net_wait_time: float = None,
        avg_partition_count: float = None,
        avg_queue_time: float = None,
        avg_return_rows: float = None,
        avg_row_cache_hit: float = None,
        avg_rpc_count: float = None,
        avg_schedule_time: float = None,
        avg_ssstore_read_rows: float = None,
        avg_used_worker_count: float = None,
        avg_user_io_wait_time: float = None,
        avg_wait_count: float = None,
        avg_wait_time: float = None,
        client_ip: str = None,
        cpu_percentage: float = None,
        db_name: str = None,
        dist_plan_percentage: float = None,
        exec_ps: float = None,
        executions: float = None,
        fail_count: float = None,
        fail_percentage: float = None,
        inner: bool = None,
        local_plan_percentage: float = None,
        max_affected_rows: float = None,
        max_application_wait_time: float = None,
        max_concurrency_wait_time: float = None,
        max_cpu_time: float = None,
        max_disk_reads: float = None,
        max_elapsed_time: float = None,
        max_return_rows: float = None,
        max_user_io_wait_time: float = None,
        max_wait_time: float = None,
        miss_plan_percentage: float = None,
        miss_plans: float = None,
        remote_plan_percentage: float = None,
        remote_plans: float = None,
        ret_code_4012count: int = None,
        ret_code_4013count: int = None,
        ret_code_5001count: int = None,
        ret_code_5024count: int = None,
        ret_code_5167count: int = None,
        ret_code_5217count: int = None,
        ret_code_6002count: int = None,
        retry_count: float = None,
        rpc_count: float = None,
        server: str = None,
        server_ip: str = None,
        server_port: int = None,
        sql_id: str = None,
        sql_text_short: str = None,
        sql_type: str = None,
        strong_consistency_percentage: float = None,
        sum_elapsed_time: float = None,
        sum_logical_reads: float = None,
        sum_wait_time: float = None,
        table_scan_percentage: float = None,
        total_wait_time: float = None,
        user_name: str = None,
        wait_event: str = None,
        weak_consistency_percentage: float = None,
    ):
        self.avg_affected_rows = avg_affected_rows
        self.avg_application_wait_time = avg_application_wait_time
        self.avg_block_cache_hit = avg_block_cache_hit
        self.avg_block_index_cache_hit = avg_block_index_cache_hit
        self.avg_bloom_filter_cache_hit = avg_bloom_filter_cache_hit
        self.avg_concurrency_wait_time = avg_concurrency_wait_time
        self.avg_cpu_time = avg_cpu_time
        self.avg_decode_time = avg_decode_time
        self.avg_disk_reads = avg_disk_reads
        self.avg_elapsed_time = avg_elapsed_time
        self.avg_execute_time = avg_execute_time
        self.avg_executor_rpc_count = avg_executor_rpc_count
        self.avg_expected_worker_count = avg_expected_worker_count
        self.avg_get_plan_time = avg_get_plan_time
        self.avg_logical_reads = avg_logical_reads
        self.avg_memstore_read_rows = avg_memstore_read_rows
        self.avg_net_time = avg_net_time
        self.avg_net_wait_time = avg_net_wait_time
        self.avg_partition_count = avg_partition_count
        self.avg_queue_time = avg_queue_time
        self.avg_return_rows = avg_return_rows
        self.avg_row_cache_hit = avg_row_cache_hit
        self.avg_rpc_count = avg_rpc_count
        self.avg_schedule_time = avg_schedule_time
        self.avg_ssstore_read_rows = avg_ssstore_read_rows
        self.avg_used_worker_count = avg_used_worker_count
        self.avg_user_io_wait_time = avg_user_io_wait_time
        self.avg_wait_count = avg_wait_count
        self.avg_wait_time = avg_wait_time
        self.client_ip = client_ip
        self.cpu_percentage = cpu_percentage
        self.db_name = db_name
        self.dist_plan_percentage = dist_plan_percentage
        self.exec_ps = exec_ps
        self.executions = executions
        self.fail_count = fail_count
        self.fail_percentage = fail_percentage
        self.inner = inner
        self.local_plan_percentage = local_plan_percentage
        self.max_affected_rows = max_affected_rows
        self.max_application_wait_time = max_application_wait_time
        self.max_concurrency_wait_time = max_concurrency_wait_time
        self.max_cpu_time = max_cpu_time
        self.max_disk_reads = max_disk_reads
        self.max_elapsed_time = max_elapsed_time
        self.max_return_rows = max_return_rows
        self.max_user_io_wait_time = max_user_io_wait_time
        self.max_wait_time = max_wait_time
        self.miss_plan_percentage = miss_plan_percentage
        self.miss_plans = miss_plans
        self.remote_plan_percentage = remote_plan_percentage
        self.remote_plans = remote_plans
        self.ret_code_4012count = ret_code_4012count
        self.ret_code_4013count = ret_code_4013count
        self.ret_code_5001count = ret_code_5001count
        self.ret_code_5024count = ret_code_5024count
        self.ret_code_5167count = ret_code_5167count
        self.ret_code_5217count = ret_code_5217count
        self.ret_code_6002count = ret_code_6002count
        self.retry_count = retry_count
        self.rpc_count = rpc_count
        self.server = server
        self.server_ip = server_ip
        self.server_port = server_port
        # SQL ID。
        self.sql_id = sql_id
        self.sql_text_short = sql_text_short
        self.sql_type = sql_type
        self.strong_consistency_percentage = strong_consistency_percentage
        self.sum_elapsed_time = sum_elapsed_time
        self.sum_logical_reads = sum_logical_reads
        self.sum_wait_time = sum_wait_time
        self.table_scan_percentage = table_scan_percentage
        self.total_wait_time = total_wait_time
        self.user_name = user_name
        self.wait_event = wait_event
        self.weak_consistency_percentage = weak_consistency_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_affected_rows is not None:
            result['AvgAffectedRows'] = self.avg_affected_rows
        if self.avg_application_wait_time is not None:
            result['AvgApplicationWaitTime'] = self.avg_application_wait_time
        if self.avg_block_cache_hit is not None:
            result['AvgBlockCacheHit'] = self.avg_block_cache_hit
        if self.avg_block_index_cache_hit is not None:
            result['AvgBlockIndexCacheHit'] = self.avg_block_index_cache_hit
        if self.avg_bloom_filter_cache_hit is not None:
            result['AvgBloomFilterCacheHit'] = self.avg_bloom_filter_cache_hit
        if self.avg_concurrency_wait_time is not None:
            result['AvgConcurrencyWaitTime'] = self.avg_concurrency_wait_time
        if self.avg_cpu_time is not None:
            result['AvgCpuTime'] = self.avg_cpu_time
        if self.avg_decode_time is not None:
            result['AvgDecodeTime'] = self.avg_decode_time
        if self.avg_disk_reads is not None:
            result['AvgDiskReads'] = self.avg_disk_reads
        if self.avg_elapsed_time is not None:
            result['AvgElapsedTime'] = self.avg_elapsed_time
        if self.avg_execute_time is not None:
            result['AvgExecuteTime'] = self.avg_execute_time
        if self.avg_executor_rpc_count is not None:
            result['AvgExecutorRpcCount'] = self.avg_executor_rpc_count
        if self.avg_expected_worker_count is not None:
            result['AvgExpectedWorkerCount'] = self.avg_expected_worker_count
        if self.avg_get_plan_time is not None:
            result['AvgGetPlanTime'] = self.avg_get_plan_time
        if self.avg_logical_reads is not None:
            result['AvgLogicalReads'] = self.avg_logical_reads
        if self.avg_memstore_read_rows is not None:
            result['AvgMemstoreReadRows'] = self.avg_memstore_read_rows
        if self.avg_net_time is not None:
            result['AvgNetTime'] = self.avg_net_time
        if self.avg_net_wait_time is not None:
            result['AvgNetWaitTime'] = self.avg_net_wait_time
        if self.avg_partition_count is not None:
            result['AvgPartitionCount'] = self.avg_partition_count
        if self.avg_queue_time is not None:
            result['AvgQueueTime'] = self.avg_queue_time
        if self.avg_return_rows is not None:
            result['AvgReturnRows'] = self.avg_return_rows
        if self.avg_row_cache_hit is not None:
            result['AvgRowCacheHit'] = self.avg_row_cache_hit
        if self.avg_rpc_count is not None:
            result['AvgRpcCount'] = self.avg_rpc_count
        if self.avg_schedule_time is not None:
            result['AvgScheduleTime'] = self.avg_schedule_time
        if self.avg_ssstore_read_rows is not None:
            result['AvgSsstoreReadRows'] = self.avg_ssstore_read_rows
        if self.avg_used_worker_count is not None:
            result['AvgUsedWorkerCount'] = self.avg_used_worker_count
        if self.avg_user_io_wait_time is not None:
            result['AvgUserIoWaitTime'] = self.avg_user_io_wait_time
        if self.avg_wait_count is not None:
            result['AvgWaitCount'] = self.avg_wait_count
        if self.avg_wait_time is not None:
            result['AvgWaitTime'] = self.avg_wait_time
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.cpu_percentage is not None:
            result['CpuPercentage'] = self.cpu_percentage
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.dist_plan_percentage is not None:
            result['DistPlanPercentage'] = self.dist_plan_percentage
        if self.exec_ps is not None:
            result['ExecPs'] = self.exec_ps
        if self.executions is not None:
            result['Executions'] = self.executions
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.fail_percentage is not None:
            result['FailPercentage'] = self.fail_percentage
        if self.inner is not None:
            result['Inner'] = self.inner
        if self.local_plan_percentage is not None:
            result['LocalPlanPercentage'] = self.local_plan_percentage
        if self.max_affected_rows is not None:
            result['MaxAffectedRows'] = self.max_affected_rows
        if self.max_application_wait_time is not None:
            result['MaxApplicationWaitTime'] = self.max_application_wait_time
        if self.max_concurrency_wait_time is not None:
            result['MaxConcurrencyWaitTime'] = self.max_concurrency_wait_time
        if self.max_cpu_time is not None:
            result['MaxCpuTime'] = self.max_cpu_time
        if self.max_disk_reads is not None:
            result['MaxDiskReads'] = self.max_disk_reads
        if self.max_elapsed_time is not None:
            result['MaxElapsedTime'] = self.max_elapsed_time
        if self.max_return_rows is not None:
            result['MaxReturnRows'] = self.max_return_rows
        if self.max_user_io_wait_time is not None:
            result['MaxUserIoWaitTime'] = self.max_user_io_wait_time
        if self.max_wait_time is not None:
            result['MaxWaitTime'] = self.max_wait_time
        if self.miss_plan_percentage is not None:
            result['MissPlanPercentage'] = self.miss_plan_percentage
        if self.miss_plans is not None:
            result['MissPlans'] = self.miss_plans
        if self.remote_plan_percentage is not None:
            result['RemotePlanPercentage'] = self.remote_plan_percentage
        if self.remote_plans is not None:
            result['RemotePlans'] = self.remote_plans
        if self.ret_code_4012count is not None:
            result['RetCode4012Count'] = self.ret_code_4012count
        if self.ret_code_4013count is not None:
            result['RetCode4013Count'] = self.ret_code_4013count
        if self.ret_code_5001count is not None:
            result['RetCode5001Count'] = self.ret_code_5001count
        if self.ret_code_5024count is not None:
            result['RetCode5024Count'] = self.ret_code_5024count
        if self.ret_code_5167count is not None:
            result['RetCode5167Count'] = self.ret_code_5167count
        if self.ret_code_5217count is not None:
            result['RetCode5217Count'] = self.ret_code_5217count
        if self.ret_code_6002count is not None:
            result['RetCode6002Count'] = self.ret_code_6002count
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.rpc_count is not None:
            result['RpcCount'] = self.rpc_count
        if self.server is not None:
            result['Server'] = self.server
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_port is not None:
            result['ServerPort'] = self.server_port
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text_short is not None:
            result['SqlTextShort'] = self.sql_text_short
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.strong_consistency_percentage is not None:
            result['StrongConsistencyPercentage'] = self.strong_consistency_percentage
        if self.sum_elapsed_time is not None:
            result['SumElapsedTime'] = self.sum_elapsed_time
        if self.sum_logical_reads is not None:
            result['SumLogicalReads'] = self.sum_logical_reads
        if self.sum_wait_time is not None:
            result['SumWaitTime'] = self.sum_wait_time
        if self.table_scan_percentage is not None:
            result['TableScanPercentage'] = self.table_scan_percentage
        if self.total_wait_time is not None:
            result['TotalWaitTime'] = self.total_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.wait_event is not None:
            result['WaitEvent'] = self.wait_event
        if self.weak_consistency_percentage is not None:
            result['WeakConsistencyPercentage'] = self.weak_consistency_percentage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgAffectedRows') is not None:
            self.avg_affected_rows = m.get('AvgAffectedRows')
        if m.get('AvgApplicationWaitTime') is not None:
            self.avg_application_wait_time = m.get('AvgApplicationWaitTime')
        if m.get('AvgBlockCacheHit') is not None:
            self.avg_block_cache_hit = m.get('AvgBlockCacheHit')
        if m.get('AvgBlockIndexCacheHit') is not None:
            self.avg_block_index_cache_hit = m.get('AvgBlockIndexCacheHit')
        if m.get('AvgBloomFilterCacheHit') is not None:
            self.avg_bloom_filter_cache_hit = m.get('AvgBloomFilterCacheHit')
        if m.get('AvgConcurrencyWaitTime') is not None:
            self.avg_concurrency_wait_time = m.get('AvgConcurrencyWaitTime')
        if m.get('AvgCpuTime') is not None:
            self.avg_cpu_time = m.get('AvgCpuTime')
        if m.get('AvgDecodeTime') is not None:
            self.avg_decode_time = m.get('AvgDecodeTime')
        if m.get('AvgDiskReads') is not None:
            self.avg_disk_reads = m.get('AvgDiskReads')
        if m.get('AvgElapsedTime') is not None:
            self.avg_elapsed_time = m.get('AvgElapsedTime')
        if m.get('AvgExecuteTime') is not None:
            self.avg_execute_time = m.get('AvgExecuteTime')
        if m.get('AvgExecutorRpcCount') is not None:
            self.avg_executor_rpc_count = m.get('AvgExecutorRpcCount')
        if m.get('AvgExpectedWorkerCount') is not None:
            self.avg_expected_worker_count = m.get('AvgExpectedWorkerCount')
        if m.get('AvgGetPlanTime') is not None:
            self.avg_get_plan_time = m.get('AvgGetPlanTime')
        if m.get('AvgLogicalReads') is not None:
            self.avg_logical_reads = m.get('AvgLogicalReads')
        if m.get('AvgMemstoreReadRows') is not None:
            self.avg_memstore_read_rows = m.get('AvgMemstoreReadRows')
        if m.get('AvgNetTime') is not None:
            self.avg_net_time = m.get('AvgNetTime')
        if m.get('AvgNetWaitTime') is not None:
            self.avg_net_wait_time = m.get('AvgNetWaitTime')
        if m.get('AvgPartitionCount') is not None:
            self.avg_partition_count = m.get('AvgPartitionCount')
        if m.get('AvgQueueTime') is not None:
            self.avg_queue_time = m.get('AvgQueueTime')
        if m.get('AvgReturnRows') is not None:
            self.avg_return_rows = m.get('AvgReturnRows')
        if m.get('AvgRowCacheHit') is not None:
            self.avg_row_cache_hit = m.get('AvgRowCacheHit')
        if m.get('AvgRpcCount') is not None:
            self.avg_rpc_count = m.get('AvgRpcCount')
        if m.get('AvgScheduleTime') is not None:
            self.avg_schedule_time = m.get('AvgScheduleTime')
        if m.get('AvgSsstoreReadRows') is not None:
            self.avg_ssstore_read_rows = m.get('AvgSsstoreReadRows')
        if m.get('AvgUsedWorkerCount') is not None:
            self.avg_used_worker_count = m.get('AvgUsedWorkerCount')
        if m.get('AvgUserIoWaitTime') is not None:
            self.avg_user_io_wait_time = m.get('AvgUserIoWaitTime')
        if m.get('AvgWaitCount') is not None:
            self.avg_wait_count = m.get('AvgWaitCount')
        if m.get('AvgWaitTime') is not None:
            self.avg_wait_time = m.get('AvgWaitTime')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CpuPercentage') is not None:
            self.cpu_percentage = m.get('CpuPercentage')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DistPlanPercentage') is not None:
            self.dist_plan_percentage = m.get('DistPlanPercentage')
        if m.get('ExecPs') is not None:
            self.exec_ps = m.get('ExecPs')
        if m.get('Executions') is not None:
            self.executions = m.get('Executions')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('FailPercentage') is not None:
            self.fail_percentage = m.get('FailPercentage')
        if m.get('Inner') is not None:
            self.inner = m.get('Inner')
        if m.get('LocalPlanPercentage') is not None:
            self.local_plan_percentage = m.get('LocalPlanPercentage')
        if m.get('MaxAffectedRows') is not None:
            self.max_affected_rows = m.get('MaxAffectedRows')
        if m.get('MaxApplicationWaitTime') is not None:
            self.max_application_wait_time = m.get('MaxApplicationWaitTime')
        if m.get('MaxConcurrencyWaitTime') is not None:
            self.max_concurrency_wait_time = m.get('MaxConcurrencyWaitTime')
        if m.get('MaxCpuTime') is not None:
            self.max_cpu_time = m.get('MaxCpuTime')
        if m.get('MaxDiskReads') is not None:
            self.max_disk_reads = m.get('MaxDiskReads')
        if m.get('MaxElapsedTime') is not None:
            self.max_elapsed_time = m.get('MaxElapsedTime')
        if m.get('MaxReturnRows') is not None:
            self.max_return_rows = m.get('MaxReturnRows')
        if m.get('MaxUserIoWaitTime') is not None:
            self.max_user_io_wait_time = m.get('MaxUserIoWaitTime')
        if m.get('MaxWaitTime') is not None:
            self.max_wait_time = m.get('MaxWaitTime')
        if m.get('MissPlanPercentage') is not None:
            self.miss_plan_percentage = m.get('MissPlanPercentage')
        if m.get('MissPlans') is not None:
            self.miss_plans = m.get('MissPlans')
        if m.get('RemotePlanPercentage') is not None:
            self.remote_plan_percentage = m.get('RemotePlanPercentage')
        if m.get('RemotePlans') is not None:
            self.remote_plans = m.get('RemotePlans')
        if m.get('RetCode4012Count') is not None:
            self.ret_code_4012count = m.get('RetCode4012Count')
        if m.get('RetCode4013Count') is not None:
            self.ret_code_4013count = m.get('RetCode4013Count')
        if m.get('RetCode5001Count') is not None:
            self.ret_code_5001count = m.get('RetCode5001Count')
        if m.get('RetCode5024Count') is not None:
            self.ret_code_5024count = m.get('RetCode5024Count')
        if m.get('RetCode5167Count') is not None:
            self.ret_code_5167count = m.get('RetCode5167Count')
        if m.get('RetCode5217Count') is not None:
            self.ret_code_5217count = m.get('RetCode5217Count')
        if m.get('RetCode6002Count') is not None:
            self.ret_code_6002count = m.get('RetCode6002Count')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('RpcCount') is not None:
            self.rpc_count = m.get('RpcCount')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerPort') is not None:
            self.server_port = m.get('ServerPort')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlTextShort') is not None:
            self.sql_text_short = m.get('SqlTextShort')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StrongConsistencyPercentage') is not None:
            self.strong_consistency_percentage = m.get('StrongConsistencyPercentage')
        if m.get('SumElapsedTime') is not None:
            self.sum_elapsed_time = m.get('SumElapsedTime')
        if m.get('SumLogicalReads') is not None:
            self.sum_logical_reads = m.get('SumLogicalReads')
        if m.get('SumWaitTime') is not None:
            self.sum_wait_time = m.get('SumWaitTime')
        if m.get('TableScanPercentage') is not None:
            self.table_scan_percentage = m.get('TableScanPercentage')
        if m.get('TotalWaitTime') is not None:
            self.total_wait_time = m.get('TotalWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WaitEvent') is not None:
            self.wait_event = m.get('WaitEvent')
        if m.get('WeakConsistencyPercentage') is not None:
            self.weak_consistency_percentage = m.get('WeakConsistencyPercentage')
        return self


class DescribeOasTopSQLListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeOasTopSQLListResponseBodyData] = None,
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
                temp_model = DescribeOasTopSQLListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeOasTopSQLListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOasTopSQLListResponseBody = None,
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
            temp_model = DescribeOasTopSQLListResponseBody()
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
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size
        # The project ID.
        self.project_id = project_id
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
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
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace
        # The ID of the data source.
        self.endpoint_id = endpoint_id
        # The type of the data source. Valid values: `MYSQL`, `MARIADB`, `OB_MYSQL`, `OB_MYSQL_CE`, `OB_ORACLE`, `ORACLE`, `DB2_LUW`, `KAFKA`, `ROCKETMQ`, `DATAHUB`, `SYBASE`, `LOGPROXY`, `ADB`, `DBP_OP_ROUTE`, `DMS`, `IDB`, and `TIDB`.
        self.endpoint_type = endpoint_type
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
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
        # The number of projects that use this label.
        self.count = count
        # The creator. This parameter value is returned only when you log on as the administrator.
        self.creator = creator
        # The ID of a label.
        self.id = id
        # The name of the label.
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
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace
        # The ID of the data source.
        self.endpoint_id = endpoint_id
        # The type of the data source. Valid values: `MYSQL`, `MARIADB`, `OB_MYSQL`, `OB_MYSQL_CE`, `OB_ORACLE`, `ORACLE`, `DB2_LUW`, `KAFKA`, `ROCKETMQ`, `DATAHUB`, `SYBASE`, `LOGPROXY`, `ADB`, `DBP_OP_ROUTE`, `DMS`, `IDB`, and `TIDB`.
        self.endpoint_type = endpoint_type
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
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
        # The error code.
        self.code = code
        # Valid values: CRITICAL, ERROR, and WARN.
        self.level = level
        # The error message.
        self.message = message
        # The suggestions (new).
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
        # The error code, such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.error_code = error_code
        # The error details.
        self.error_details = error_details
        # The error message.
        self.error_msg = error_msg
        # The error related parameters.
        self.error_param = error_param
        # The time when the error occurred.
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
        # The estimated maximum time remained, in seconds.
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec
        # The estimated amount of data to migrate.
        self.estimated_total_count = estimated_total_count
        # The amount of data migrated.
        self.finished_count = finished_count
        # finishedCount / estimatedTotalCount
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
        # The estimated total number of rows.
        self.capacity = capacity
        # The checkpoint. The value is a unix timestamp in seconds.
        self.checkpoint = checkpoint
        # The full synchronization progress.
        self.connector_full_progress_overview = connector_full_progress_overview
        # The resource deployment ID.
        self.deploy_id = deploy_id
        # The read/write throughput of the destination data source, in bytes per second.
        self.dst_iops = dst_iops
        # The read/write RPS of the destination data source.
        self.dst_rps = dst_rps
        # The read/write RPS baseline of the destination data source.
        self.dst_rps_ref = dst_rps_ref
        # The read/write RT per record of the destination data source, in ms.
        self.dst_rt = dst_rt
        # The read/write RT baseline of the destination data source.
        self.dst_rt_ref = dst_rt_ref
        # The checkpoint collection time. The value is a unix timestamp in seconds.
        self.gmt = gmt
        # The amount of inconsistent data found during full verification.
        self.inconsistencies = inconsistencies
        # The checkpoint in incremental synchronization. The value is a unix timestamp in seconds.
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint
        # The job ID.
        self.job_id = job_id
        # The number of migrated rows.
        self.processed_records = processed_records
        # A sub-status that indicates whether this step is skipped.
        self.skipped = skipped
        # The read throughput of the source data source, in bytes per second.
        self.src_iops = src_iops
        # The read throughput baseline of the source data source.
        self.src_iops_ref = src_iops_ref
        # The read requests per second (RPS) of the source data source.
        self.src_rps = src_rps
        # The read RPS baseline of the source data source.
        self.src_rps_ref = src_rps_ref
        # The read response time (RT) per record of the source data source, in ms.
        self.src_rt = src_rt
        # The read RT baseline of the source data source.
        self.src_rt_ref = src_rt_ref
        # A sub-status that indicates whether the checker has completed full verification.
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
        # The estimated time remained.
        self.estimated_remaining_seconds = estimated_remaining_seconds
        # The additional information. The value is a JSON string.
        self.extra_info = extra_info
        # The end time, in the format of "2020-05-22T17:04:18".
        self.finish_time = finish_time
        # Indicates whether the current step must be confirmed by the user, rather than scheduled in the backend.
        self.interactive = interactive
        # The start time, in the format of "2020-05-22T17:04:18".
        self.start_time = start_time
        # The description of the step, for example, schema migration, full migration, full verification, incremental log pull, incremental synchronization, or incremental verification.
        self.step_description = step_description
        # The step details. The value is a JSON string.
        self.step_info = step_info
        # The step name. Valid values: struct_migration, full_migration, full_validation, incr_log_pull, incr_sync/incr_validation, PRE_CHECK, PREPARE, STRUCT_MIGRATION, INDEX_MIGRATION, STRUCT_SYNC, FULL_MIGRATION, APP_SWITCH, REVERSE_INCR_SYNC, FULL_VALIDATION, INCR_LOG_PULL, INCR_SYNC, INCR_VALIDATION, SYNC_PREPARE, SYNC_INCR_LOG_PULL, CONNECTOR_FULL_SYNC, or CONNECTOR_INCR_SYNC.
        self.step_name = step_name
        # The sequence of steps.
        self.step_order = step_order
        # The step progress.
        self.step_progress = step_progress
        # The step status. Valid values: INIT, RUNNING, FAILED, FINISHED, SUSPEND, and MONITORING. The value MONITORING indicates the continuous monitoring of incremental synchronization and incremental verification.
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
        # The list of distribution key columns.
        self.distributed_keys = distributed_keys
        # The lifecycle of the table.
        self.partition_life_cycle = partition_life_cycle
        # The partitioning expression.
        self.partition_statement = partition_statement
        # The list of primary key columns.
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
        # The schema of the ADB table. If the destination data source is ADB, you need to configure additional information for schema synchronization.
        self.adb_table_schema = adb_table_schema
        # The list of filter columns, which are the columns to be synchronized.
        self.filter_columns = filter_columns
        # The name of the mapped-to table or topic. If the destination data source is a database, this parameter specifies the name of the mapped-to table. If the destination data source is a message queue system, this parameter specifies the name of the mapped-to topic.
        self.mapped_name = mapped_name
        # The list of sharding key columns. This parameter applies to scenarios where the destination data source is a message queue system.
        self.shard_columns = shard_columns
        # The ID of the table. This parameter takes effect when the source data source is IDB.
        self.table_id = table_id
        # The name of the table.
        self.table_name = table_name
        # Valid values: DATABASE and TABLE.
        self.type = type
        # The row filter conditions.
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
        # The ID of the database. This parameter takes effect when the source data source is IDB.
        self.database_id = database_id
        # The name of the database.
        self.database_name = database_name
        # The mapped-to database. This parameter takes effect when the destination data source is a database.
        self.mapped_name = mapped_name
        # The settings for the target table objects in the current database.
        self.tables = tables
        # The mapped-to tenant. This parameter takes effect when the source data source is OceanBase Database.
        self.tenant_name = tenant_name
        # Valid values: DATABASE and TABLE.
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
        # The table mapping in the source data source, which is a conventional mapping scheme and takes effect only when Mode is set to NORMAL.
        self.databases = databases
        # The mapping type. Valid values: \"NORMAL\" and \"WHITE_AND_BLACK_LIST\".
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
        # The list of data types of incremental data synchronized in incremental synchronization.
        self.record_type_list = record_type_list
        # The start time for incremental synchronization. The value is a timestamp in seconds.
        self.start_timestamp = start_timestamp
        # The retention time of logs when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_log_kept_hour = store_log_kept_hour
        # Indicates whether intra-transaction sequencing is enabled when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_transaction_enabled = store_transaction_enabled
        # Valid values: STRUCT, FULL, and INCR.
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
        # Indicates whether full migration is enabled.
        self.enable_full_sync = enable_full_sync
        # Indicates whether incremental synchronization is enabled.
        self.enable_incr_sync = enable_incr_sync
        # Indicates whether schema synchronization is enabled.
        self.enable_struct_sync = enable_struct_sync
        # The settings of incremental synchronization steps.
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
        # The business system identifier, which is optional and is a specific field of the Post message.
        self.business_name = business_name
        # The settings of the destination data source.
        self.dest_config = dest_config
        # A collection of label IDs.
        self.labels = labels
        # The project ID.
        self.project_id = project_id
        # The name of the project.
        self.project_name = project_name
        # The project owner.
        self.project_owner = project_owner
        # The settings of the source data source.
        self.source_config = source_config
        # The detailed project steps.
        self.steps = steps
        # The mappings for the synchronization objects.
        self.transfer_mapping = transfer_mapping
        # The settings of synchronization steps
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
        # The error code (new).
        self.code = code
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.level = level
        # The error description (new).
        self.message = message
        # The suggestions (new).
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
        # The suggestions (old).
        self.advice = advice
        # The error code (old).
        self.code = code
        # The time spent in processing the request, in seconds.
        self.cost = cost
        # The business data returned.
        self.data = data
        # The error details.
        self.error_detail = error_detail
        # The error description (old).
        self.message = message
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success
        # The total count, which takes effect in a pagination query.
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
        # The read RT baseline of the source data source.
        self.page_number = page_number
        # The read/write RPS baseline of the destination data source.
        self.page_size = page_size
        # The read/write RT baseline of the destination data source.
        self.project_id = project_id
        # The read RT baseline of the source data source.
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
        # The suggestions (old).
        self.code = code
        # Contact the administrator.
        self.level = level
        # A sub-status that indicates whether the checker has completed full verification.
        self.message = message
        # The amount of data migrated.
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
        # The job ID.
        self.error_code = error_code
        # Schema migration
        self.error_details = error_details
        # The resource deployment ID.
        self.error_msg = error_msg
        # The error code (new).
        self.error_param = error_param
        # The additional information. The value is a JSON string.
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
        # A sub-status that indicates whether this step is skipped.
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec
        # The read RPS baseline of the source data source.
        self.estimated_total_count = estimated_total_count
        # The read/write RT per record of the destination data source, in ms.
        self.finished_count = finished_count
        # The business data returned.
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
        # The total count, which takes effect in a pagination query.
        self.capacity = capacity
        # The operation that you want to perform. Set the value to **DescribeOmsOpenAPIProjectSteps**.
        self.checkpoint = checkpoint
        # The error code, such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.connector_full_progress_overview = connector_full_progress_overview
        # The page size, which takes effect in a pagination query.
        self.deploy_id = deploy_id
        # The error description (old).
        self.dst_iops = dst_iops
        # The estimated amount of data to migrate.
        self.dst_rps = dst_rps
        # The step progress.
        self.dst_rps_ref = dst_rps_ref
        # The read requests per second (RPS) of the source data source.
        self.dst_rt = dst_rt
        # A system error occurred.
        self.dst_rt_ref = dst_rt_ref
        # The full synchronization progress.
        self.gmt = gmt
        # The read/write throughput of the destination data source, in bytes per second.
        self.inconsistencies = inconsistencies
        # The read throughput of the source data source, in bytes per second.
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint
        # The error code (old).
        self.job_id = job_id
        # The error related parameters.
        self.processed_records = processed_records
        # The time spent in processing the request, in seconds.
        self.skipped = skipped
        # finishedCount / estimatedTotalCount
        self.src_iops = src_iops
        # The end time, in the format of "2020-05-22T17:04:18".
        self.src_iops_ref = src_iops_ref
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.src_rps = src_rps
        # The checkpoint. The value is a unix timestamp in seconds.
        self.src_rps_ref = src_rps_ref
        # The error code.
        self.src_rt = src_rt
        # The checkpoint collection time. The value is a unix timestamp in seconds.
        self.src_rt_ref = src_rt_ref
        # The read/write RPS of the destination data source.
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
        # The request ID.
        self.estimated_remaining_seconds = estimated_remaining_seconds
        # A system error occurred.
        self.extra_info = extra_info
        # $.parameters[3].schema.example
        self.finish_time = finish_time
        # $.parameters[5].schema.description
        self.interactive = interactive
        # The error details.
        self.start_time = start_time
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.step_description = step_description
        # The error related parameters.
        self.step_info = step_info
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.step_name = step_name
        # DescribeOmsOpenAPIProjectSteps
        self.step_order = step_order
        # cn-hangzhou
        self.step_progress = step_progress
        # Indicates whether the call is successful.
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
        # The error details.
        self.code = code
        # Valid values: CRITICAL, ERROR, and WARN.
        self.level = level
        # A system error occurred.
        self.message = message
        # Contact the administrator.
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
        # The error related parameters.
        self.advice = advice
        # The error code (old), such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.code = code
        # The step end time, in the format of "yyyy-MM-ddTHH:mm:ss".
        self.cost = cost
        # Indicates whether the current step must be confirmed by the user, rather than scheduled in the backend.
        self.data = data
        # The step details. The value is a JSON string.
        self.error_detail = error_detail
        # A system error occurred.
        self.message = message
        # The additional information. The value is a JSON string.
        self.page_number = page_number
        # The step start time, in the format of "yyyy-MM-ddTHH:mm:ss".
        self.page_size = page_size
        # The time when the error occurred.
        self.request_id = request_id
        # The read throughput baseline of the source data source.
        self.success = success
        # The estimated remaining time. This parameter takes effect in full synchronization.
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
        # - When the value is set to True, the throttling information in the database is queried based on the SQL ID.   
        # - When the value is set to False, the bound index or execution plan in the database is queried based on the SQL ID.
        self.database_name = database_name
        # SQLID.
        self.instance_id = instance_id
        # The ID of the tenant.
        self.is_concurrent_limit = is_concurrent_limit
        # false
        self.sqlid = sqlid
        # The name of the database.
        self.table_name = table_name
        # The name of the tenant.    
        # It must start with a letter or an underscore (_), and contain 2 to 20 characters, which can be uppercase letters, lowercase letters, digits, and underscores (_). It cannot be set to SYS.
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
        table_name: str = None,
    ):
        self.bind_index = bind_index
        # You can call this operation to query the outline binding information or throttling information of an SQL statement in the database based on an SQLID.
        self.bind_plan = bind_plan
        self.max_concurrent = max_concurrent
        # {"name":"DescribeOutlineBinding","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeOutlineBinding\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"TableName\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"pay_online\"},{\"name\":\"DatabaseName\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"IsConcurrentLimit\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Boolean\",\"title\":\"\",\"description\":\"\",\"example\":\"false\"},{\"name\":\"InstanceId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"ob317v4uif****\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"OutlineBinding\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Object\",\"children\":[{\"name\":\"BindPlan\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"PHY_TABLE_SCAN | bmsql_order_line | 40 ******\"},{\"name\":\"OutlineId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"OutlineID\",\"description\":\"OutlineID。\",\"example\":\"-1\"},{\"name\":\"BindIndex\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"PRIMARY\"},{\"name\":\"MaxConcurrent\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"2\"}],\"title\":\"\",\"description\":\"\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C\"}],\"title\":\"\",\"description\":\"\"}","errors":"{\"2014\":[{\"code\":\"2014\",\"defaultError\":false,\"errorCode\":\"InternalError\",\"errorMessage\":\"The request processing has failed due to some unknown error.\",\"errorMessageCn\":\"\",\"type\":\"user\"}]}"}
        self.outline_id = outline_id
        # 表名称
        self.table_name = table_name

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
        if self.table_name is not None:
            result['TableName'] = self.table_name
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
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeOutlineBindingResponseBody(TeaModel):
    def __init__(
        self,
        outline_binding: DescribeOutlineBindingResponseBodyOutlineBinding = None,
        request_id: str = None,
    ):
        # ```
        # http(s)://[Endpoint]/?Action=DescribeOutlineBinding
        # &TenantId=t2mr3oae0****\
        # &TableName=pay_online
        # &DatabaseName=testdb
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &IsConcurrentLimit=false
        # &InstanceId=ob317v4uif****\
        # &Common request parameters
        # ```
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
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.dimension = dimension
        # Alibaba Cloud CLI
        self.dimension_value = dimension_value
        # 498529
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
        readonly: bool = None,
        rejected_value: List[str] = None,
        value_type: str = None,
    ):
        # DescribeParameters
        self.acceptable_value = acceptable_value
        # The ID of the OceanBase cluster.
        self.current_value = current_value
        # ```
        # http(s)://[Endpoint]/?Action=DescribeParameters
        # &InstanceId=ob317v4uif****\
        # &Dimension=TENANT
        # &DimensionValue=ob2mr3oae0****\
        # &Common request parameters
        # ```
        self.default_value = default_value
        # The description of the parameter.
        self.description = description
        # The request ID.
        self.name = name
        # The name of the parameter.
        self.need_reboot = need_reboot
        # 参数是否只读
        self.readonly = readonly
        # {
        #     "RequestId": "EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C",
        #     "Parameters": [
        #         {
        #             "Description": "The maximum delay allowed in weak-consistency reads.",
        #             "ValueType": "CAPACITY",
        #             "CurrentValue": "600",
        #             "NeedReboot": false,
        #             "Name": "connect_timeout",
        #             "DefaultValue": "600s",
        #             "RejectedValue": [
        #                 "1s"
        #             ],
        #             "AcceptableValue": [
        #                 "1s"
        #             ]
        #         }
        #     ]
        # }
        self.rejected_value = rejected_value
        # The invalid value range of the parameter.    
        # It is an array with two string elements, which represents a range. The first element represents the minimum value and the second element represents the maximum value.
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
        if self.readonly is not None:
            result['Readonly'] = self.readonly
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
        if m.get('Readonly') is not None:
            self.readonly = m.get('Readonly')
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
        # Indicates whether a restart is required for changes to the parameter to take effect. Valid values:   
        # - true: A restart is required.   
        # - false: A restart is not required.
        self.parameters = parameters
        # The return result of the request.
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
        # The value of the parameter after the modification.
        self.dimension = dimension
        # The list of parameter modification records.
        self.dimension_value = dimension_value
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.end_time = end_time
        # The name of the parameter.
        self.instance_id = instance_id
        # Default value: 10.
        self.page_number = page_number
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.page_size = page_size
        # You can call this operation to query the modification history of cluster or tenant parameters.
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
        # The request ID.
        self.create_time = create_time
        # ```
        # http(s)://[Endpoint]/?Action=DescribeParametersHistory
        # &InstanceId=ob317v4uif****\
        # &Dimension=TENANT
        # &DimensionValue=ob2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &PageSize=10
        # &PageNumber=1
        # &Common request parameters
        # ```
        self.dimension_value = dimension_value
        # You can call this operation to query the modification history of cluster or tenant parameters.
        self.name = name
        self.new_value = new_value
        # The start time of the time range for querying the parameter modification history.
        self.old_value = old_value
        # -\
        self.status = status
        # The name of the parameter.
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
        # The end time for the query of parameter modification history.
        self.page_number = page_number
        # The number of rows to return on each page.   
        # - Maximum value: 100   
        # - Default value: 10
        self.parameters = parameters
        # The list of parameter modification records.
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
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.request_id = request_id
        # The time when the parameter modification took effect.
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
        # The return result of the request.
        self.instance_id = instance_id
        # The ID of the OceanBase cluster.
        self.sqlid = sqlid
        # The index recommended for the SQL statement after calculation by the diagnostic system.   
        # - If the recommended index is the primary key, PRIMARY is returned.  
        # - If an index created by the user is recommended, the index name is returned.   
        # The system recommends only one index for an SQL statement. You can call the DescribeIndexes operation to view the indexes of a table.
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
        # Example 1
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
        # The information about the recommended index.
        self.recommend_index = recommend_index
        # The tenant mode.   Valid values:  
        # Oracle   
        # MySQL
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
        # The SQL text.
        self.sqlid = sqlid
        # SQLID.
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
        # {"name":"DescribeSQLDetails","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeSQLDetails\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"SQLDetails\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\"  \",\"children\":[{\"name\":\"SQLText\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tester\"}],\"title\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{}"}
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
        # The operation that you want to perform.   
        # Set the value to **DescribeSQLDetails**.
        self.request_id = request_id
        # ```
        # http(s)://[Endpoint]/?Action=DescribeSQLDetails
        # &TenantId=t2mr3oae0****\
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &Common request parameters
        # ```
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
        # The number of block index cache hits.
        self.end_time = end_time
        # The end time in UTC +0.
        self.page_number = page_number
        # The end time.
        self.page_size = page_size
        # The number of block index cache hits.
        self.sqlid = sqlid
        # The maximum response time.
        self.start_time = start_time
        # The average CPU time.
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
        # The wait time of the client.
        self.affected_rows = affected_rows
        # The IP address of the client.
        self.app_wait_time = app_wait_time
        # The number of logical reads.
        self.block_cache_hit = block_cache_hit
        # The number of block index cache hits.
        self.block_index_cache_hit = block_index_cache_hit
        # The username.
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        # The number of remote plans.
        self.client_ip = client_ip
        # The number of block cache hits.
        self.concurrency_wait_time = concurrency_wait_time
        # The page number.
        self.cpu_time = cpu_time
        # The number of retries.
        self.db_name = db_name
        # The number of rows read from the disk.
        self.decode_time = decode_time
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.disk_read = disk_read
        # The number of row cache hits.
        self.elapsed_time = elapsed_time
        # The maximum CPU time.
        self.end_time = end_time
        # The number of rows read from the memory.
        self.end_time_utcstring = end_time_utcstring
        # The number of rows returned.
        self.event = event
        # The queuing time.
        self.exec_per_second = exec_per_second
        # The execution history of the SQL statement.
        self.execute_time = execute_time
        # The wait time in concurrent execution.
        self.executions = executions
        # Example 1
        self.fail_times = fail_times
        # The number of RPCs.
        self.get_plan_time = get_plan_time
        # The number of rows affected.
        self.iowait_time = iowait_time
        self.logical_read = logical_read
        # The number of row cache hits.
        self.max_cpu_time = max_cpu_time
        # The scheduling duration.
        self.max_elapsed_time = max_elapsed_time
        # The operation that you want to perform.   
        # Set the value to **DescribeSQLHistoryList**.
        self.memstore_read_row_count = memstore_read_row_count
        # The number of Bloom filter cache hits.
        self.miss_plans = miss_plans
        # The return result of the request.
        self.net_wait_time = net_wait_time
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.node_ip = node_ip
        self.queue_time = queue_time
        # The quantity.
        self.rpccount = rpccount
        # The list.
        self.remote_plans = remote_plans
        # The number of executions.
        self.retry_count = retry_count
        # The I/O wait time.
        self.return_rows = return_rows
        # {"name":"DescribeSQLHistoryList","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeSQLHistoryList\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-09-13T15:40:43Z\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"SQLID\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"SQLHistoryList\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Object\",\"children\":[{\"name\":\"List\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\"  \",\"children\":[{\"name\":\"ExecPerSecond\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"163.0\"},{\"name\":\"MaxCpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"257.967\"},{\"name\":\"BlockCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"14\"},{\"name\":\"DecodeTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"RemotePlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"RPCCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NetWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"DiskRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NodeIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"i-bp18qljorblo8es*****\"},{\"name\":\"ConcurrencyWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"MemstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"527\"},{\"name\":\"AppWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"ElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"76.382\"},{\"name\":\"MissPlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"AffectedRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"ScheduleTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"Event\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"mysql response wait client\"},{\"name\":\"TotalWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"10.966\"},{\"name\":\"ReturnRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"ExecuteTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"61.044\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tester\"},{\"name\":\"Executions\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"89403\"},{\"name\":\"GetPlanTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.052\"},{\"name\":\"CpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"50.13\"},{\"name\":\"MaxElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"260.44\"},{\"name\":\"BlockIndexCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"4\"},{\"name\":\"EndTimeUTCString\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-12-28T02:08:18Z\"},{\"name\":\"EndTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-12-28T02:08:18Z\"},{\"name\":\"RetryCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"ClientIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"1*2.***.1*3.***\"},{\"name\":\"BloomFilterCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"IOWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"FailTimes\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"QueueTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"title\":\"\",\"description\":\"\",\"example\":\"15.275\"},{\"name\":\"RowCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"LogicalRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"19\"},{\"name\":\"SsstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"43086\"}],\"title\":\"\"},{\"name\":\"Count\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"}],\"title\":\"\",\"description\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{\"2014\":[{\"code\":\"2014\",\"defaultError\":false,\"errorCode\":\"InternalError\",\"errorMessage\":\"The request processing has failed due to some unknown error.\",\"errorMessageCn\":\"\",\"type\":\"user\"}]}"}
        self.row_cache_hit = row_cache_hit
        # The end time of the time range for querying the SQL execution history.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.schedule_time = schedule_time
        self.ssstore_read_row_count = ssstore_read_row_count
        # The average response time.
        self.total_wait_time = total_wait_time
        # The network latency.
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
        # The I/O wait time.
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
        # The IP address of the client.
        self.request_id = request_id
        # The number of Bloom filter cache hits.
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
        # The time when the plan was loaded for the first time, .
        self.sqlid = sqlid
        # The time when the plan was loaded for the first time, .
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
        # The time when the plan was bound.
        self.avg_execution_ms = avg_execution_ms
        # The time when the plan was loaded for the first time, in UTC +0.
        self.avg_execution_time_ms = avg_execution_time_ms
        self.first_load_time = first_load_time
        # Example 1
        self.first_load_time_utcstring = first_load_time_utcstring
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.hit_count = hit_count
        # The unique identifier of the SQL execution plan in the diagnostic system.
        self.merged_version = merged_version
        # The complete execution plan of the SQL statement.
        self.node_ip = node_ip
        # The information about the plan.
        self.outline_data = outline_data
        # SQLID.
        self.outline_id = outline_id
        # The ID of the SQL execution plan in the database.
        self.outline_time = outline_time
        # The major compaction version.
        self.outline_time_utcstring = outline_time_utcstring
        # The information about the execution plan.
        self.plan_full = plan_full
        # OutlineID.
        self.plan_id = plan_id
        self.plan_info = plan_info
        # The return result of the request.
        self.plan_union_hash = plan_union_hash
        # The request ID.
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
        # The return result of the request.
        self.request_id = request_id
        # master
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


class DescribeSQLSamplesRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end_time: str = None,
        instance_id: str = None,
        sql_id: str = None,
        start_time: str = None,
        tenant_id: str = None,
    ):
        self.db_name = db_name
        self.end_time = end_time
        self.instance_id = instance_id
        # SQL ID。
        self.sql_id = sql_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeSQLSamplesResponseBodyData(TeaModel):
    def __init__(
        self,
        affected_rows: float = None,
        application_wait_time: float = None,
        block_cache_hit: float = None,
        block_index_cache_hit: float = None,
        bloom_filter_cache_hit: float = None,
        client_ip: str = None,
        client_port: str = None,
        concurrency_wait_time: float = None,
        consistency_level: str = None,
        cpu_time: float = None,
        db_name: str = None,
        decode_time: float = None,
        disk_reads: float = None,
        elapsed_time: float = None,
        execute_time: float = None,
        executor_rpc: float = None,
        expected_worker_count: float = None,
        get_plan_time: float = None,
        hit_plan: float = None,
        inner: bool = None,
        memstore_read_rows: float = None,
        net_time: float = None,
        net_wait_time: float = None,
        ob_db_id: float = None,
        ob_server_id: float = None,
        ob_user_id: float = None,
        partition_count: float = None,
        plan_id: float = None,
        plan_type: str = None,
        queue_time: float = None,
        request_id: str = None,
        request_time: str = None,
        ret_code: float = None,
        retry_count: float = None,
        return_rows: float = None,
        row_cache_hit: float = None,
        rpc_count: float = None,
        schedule_time: float = None,
        server: str = None,
        sql_type: str = None,
        ssstore_read_rows: float = None,
        statement: str = None,
        table_scan: float = None,
        trace_id: str = None,
        trans_hash: str = None,
        used_worker_count: float = None,
        user_io_wait_time: float = None,
        user_name: str = None,
        wait_count: float = None,
        wait_event: str = None,
        wait_time: float = None,
    ):
        self.affected_rows = affected_rows
        self.application_wait_time = application_wait_time
        self.block_cache_hit = block_cache_hit
        self.block_index_cache_hit = block_index_cache_hit
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        self.client_ip = client_ip
        self.client_port = client_port
        self.concurrency_wait_time = concurrency_wait_time
        self.consistency_level = consistency_level
        self.cpu_time = cpu_time
        self.db_name = db_name
        self.decode_time = decode_time
        self.disk_reads = disk_reads
        self.elapsed_time = elapsed_time
        self.execute_time = execute_time
        self.executor_rpc = executor_rpc
        self.expected_worker_count = expected_worker_count
        self.get_plan_time = get_plan_time
        self.hit_plan = hit_plan
        self.inner = inner
        self.memstore_read_rows = memstore_read_rows
        self.net_time = net_time
        self.net_wait_time = net_wait_time
        self.ob_db_id = ob_db_id
        # server  ID。
        self.ob_server_id = ob_server_id
        self.ob_user_id = ob_user_id
        self.partition_count = partition_count
        self.plan_id = plan_id
        self.plan_type = plan_type
        self.queue_time = queue_time
        self.request_id = request_id
        self.request_time = request_time
        self.ret_code = ret_code
        self.retry_count = retry_count
        self.return_rows = return_rows
        self.row_cache_hit = row_cache_hit
        self.rpc_count = rpc_count
        self.schedule_time = schedule_time
        self.server = server
        self.sql_type = sql_type
        self.ssstore_read_rows = ssstore_read_rows
        self.statement = statement
        self.table_scan = table_scan
        self.trace_id = trace_id
        # transaction hash。
        self.trans_hash = trans_hash
        self.used_worker_count = used_worker_count
        self.user_io_wait_time = user_io_wait_time
        self.user_name = user_name
        self.wait_count = wait_count
        self.wait_event = wait_event
        self.wait_time = wait_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_rows is not None:
            result['AffectedRows'] = self.affected_rows
        if self.application_wait_time is not None:
            result['ApplicationWaitTime'] = self.application_wait_time
        if self.block_cache_hit is not None:
            result['BlockCacheHit'] = self.block_cache_hit
        if self.block_index_cache_hit is not None:
            result['BlockIndexCacheHit'] = self.block_index_cache_hit
        if self.bloom_filter_cache_hit is not None:
            result['BloomFilterCacheHit'] = self.bloom_filter_cache_hit
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_port is not None:
            result['ClientPort'] = self.client_port
        if self.concurrency_wait_time is not None:
            result['ConcurrencyWaitTime'] = self.concurrency_wait_time
        if self.consistency_level is not None:
            result['ConsistencyLevel'] = self.consistency_level
        if self.cpu_time is not None:
            result['CpuTime'] = self.cpu_time
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.decode_time is not None:
            result['DecodeTime'] = self.decode_time
        if self.disk_reads is not None:
            result['DiskReads'] = self.disk_reads
        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.executor_rpc is not None:
            result['ExecutorRpc'] = self.executor_rpc
        if self.expected_worker_count is not None:
            result['ExpectedWorkerCount'] = self.expected_worker_count
        if self.get_plan_time is not None:
            result['GetPlanTime'] = self.get_plan_time
        if self.hit_plan is not None:
            result['HitPlan'] = self.hit_plan
        if self.inner is not None:
            result['Inner'] = self.inner
        if self.memstore_read_rows is not None:
            result['MemstoreReadRows'] = self.memstore_read_rows
        if self.net_time is not None:
            result['NetTime'] = self.net_time
        if self.net_wait_time is not None:
            result['NetWaitTime'] = self.net_wait_time
        if self.ob_db_id is not None:
            result['ObDbId'] = self.ob_db_id
        if self.ob_server_id is not None:
            result['ObServerId'] = self.ob_server_id
        if self.ob_user_id is not None:
            result['ObUserId'] = self.ob_user_id
        if self.partition_count is not None:
            result['PartitionCount'] = self.partition_count
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.plan_type is not None:
            result['PlanType'] = self.plan_type
        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.return_rows is not None:
            result['ReturnRows'] = self.return_rows
        if self.row_cache_hit is not None:
            result['RowCacheHit'] = self.row_cache_hit
        if self.rpc_count is not None:
            result['RpcCount'] = self.rpc_count
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.server is not None:
            result['Server'] = self.server
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.ssstore_read_rows is not None:
            result['SsstoreReadRows'] = self.ssstore_read_rows
        if self.statement is not None:
            result['Statement'] = self.statement
        if self.table_scan is not None:
            result['TableScan'] = self.table_scan
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        if self.trans_hash is not None:
            result['TransHash'] = self.trans_hash
        if self.used_worker_count is not None:
            result['UsedWorkerCount'] = self.used_worker_count
        if self.user_io_wait_time is not None:
            result['UserIoWaitTime'] = self.user_io_wait_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.wait_count is not None:
            result['WaitCount'] = self.wait_count
        if self.wait_event is not None:
            result['WaitEvent'] = self.wait_event
        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedRows') is not None:
            self.affected_rows = m.get('AffectedRows')
        if m.get('ApplicationWaitTime') is not None:
            self.application_wait_time = m.get('ApplicationWaitTime')
        if m.get('BlockCacheHit') is not None:
            self.block_cache_hit = m.get('BlockCacheHit')
        if m.get('BlockIndexCacheHit') is not None:
            self.block_index_cache_hit = m.get('BlockIndexCacheHit')
        if m.get('BloomFilterCacheHit') is not None:
            self.bloom_filter_cache_hit = m.get('BloomFilterCacheHit')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientPort') is not None:
            self.client_port = m.get('ClientPort')
        if m.get('ConcurrencyWaitTime') is not None:
            self.concurrency_wait_time = m.get('ConcurrencyWaitTime')
        if m.get('ConsistencyLevel') is not None:
            self.consistency_level = m.get('ConsistencyLevel')
        if m.get('CpuTime') is not None:
            self.cpu_time = m.get('CpuTime')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DecodeTime') is not None:
            self.decode_time = m.get('DecodeTime')
        if m.get('DiskReads') is not None:
            self.disk_reads = m.get('DiskReads')
        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('ExecutorRpc') is not None:
            self.executor_rpc = m.get('ExecutorRpc')
        if m.get('ExpectedWorkerCount') is not None:
            self.expected_worker_count = m.get('ExpectedWorkerCount')
        if m.get('GetPlanTime') is not None:
            self.get_plan_time = m.get('GetPlanTime')
        if m.get('HitPlan') is not None:
            self.hit_plan = m.get('HitPlan')
        if m.get('Inner') is not None:
            self.inner = m.get('Inner')
        if m.get('MemstoreReadRows') is not None:
            self.memstore_read_rows = m.get('MemstoreReadRows')
        if m.get('NetTime') is not None:
            self.net_time = m.get('NetTime')
        if m.get('NetWaitTime') is not None:
            self.net_wait_time = m.get('NetWaitTime')
        if m.get('ObDbId') is not None:
            self.ob_db_id = m.get('ObDbId')
        if m.get('ObServerId') is not None:
            self.ob_server_id = m.get('ObServerId')
        if m.get('ObUserId') is not None:
            self.ob_user_id = m.get('ObUserId')
        if m.get('PartitionCount') is not None:
            self.partition_count = m.get('PartitionCount')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PlanType') is not None:
            self.plan_type = m.get('PlanType')
        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('ReturnRows') is not None:
            self.return_rows = m.get('ReturnRows')
        if m.get('RowCacheHit') is not None:
            self.row_cache_hit = m.get('RowCacheHit')
        if m.get('RpcCount') is not None:
            self.rpc_count = m.get('RpcCount')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('SsstoreReadRows') is not None:
            self.ssstore_read_rows = m.get('SsstoreReadRows')
        if m.get('Statement') is not None:
            self.statement = m.get('Statement')
        if m.get('TableScan') is not None:
            self.table_scan = m.get('TableScan')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        if m.get('TransHash') is not None:
            self.trans_hash = m.get('TransHash')
        if m.get('UsedWorkerCount') is not None:
            self.used_worker_count = m.get('UsedWorkerCount')
        if m.get('UserIoWaitTime') is not None:
            self.user_io_wait_time = m.get('UserIoWaitTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WaitCount') is not None:
            self.wait_count = m.get('WaitCount')
        if m.get('WaitEvent') is not None:
            self.wait_event = m.get('WaitEvent')
        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')
        return self


class DescribeSQLSamplesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DescribeSQLSamplesResponseBodyData] = None,
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
                temp_model = DescribeSQLSamplesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSQLSamplesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSQLSamplesResponseBody = None,
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
            temp_model = DescribeSQLSamplesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIpGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the OceanBase cluster.
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
        # The request ID.
        self.request_id = request_id
        self.security_ip_groups = security_ip_groups
        # Example 1
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
        # The number of RPCs.
        self.end_time = end_time
        # The maximum response time.
        self.page_number = page_number
        # The number of plan misses.
        self.page_size = page_size
        # The wait time for network.
        self.sqlid = sqlid
        # The I/O wait time.
        self.start_time = start_time
        # The ID of the tenant.
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
        get_plan_time: float = None,
        iowait_time: float = None,
        logical_read: float = None,
        max_cpu_time: float = None,
        max_elapsed_time: float = None,
        memstore_read_row_count: float = None,
        miss_plans: float = None,
        net_wait_time: float = None,
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
        # The wait event.
        self.affected_rows = affected_rows
        # The number of row cache hits.
        self.app_wait_time = app_wait_time
        # The average CPU time.
        self.block_cache_hit = block_cache_hit
        # The number of rows to return on each page.  
        # - Maximum value: 100   
        # - Default value: 10
        self.block_index_cache_hit = block_index_cache_hit
        # The number of executions.
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        # The number of retries.
        self.client_ip = client_ip
        # $.parameters[6].schema.example
        self.concurrency_wait_time = concurrency_wait_time
        # $.parameters[6].schema.enumValueTitles
        self.cpu_time = cpu_time
        # The IP address of the node.
        self.db_name = db_name
        # $.parameters[7].schema.description
        self.decode_time = decode_time
        # SQLID.
        self.disk_read = disk_read
        # The queuing time.
        self.elapsed_time = elapsed_time
        self.end_time_utcstring = end_time_utcstring
        # The internal wait time.
        self.event = event
        # The number of failures.
        self.exec_per_second = exec_per_second
        # The request ID.
        self.execute_time = execute_time
        # The maximum CPU time.
        self.executions = executions
        # The number of rows returned.
        self.fail_times = fail_times
        # Example 1
        self.get_plan_time = get_plan_time
        # $.parameters[7].schema.enumValueTitles
        self.iowait_time = iowait_time
        # The quantity.
        self.logical_read = logical_read
        # DescribeSlowSQLHistoryList
        self.max_cpu_time = max_cpu_time
        # ```
        # http(s)://[Endpoint]/?Action=DescribeSlowSQLHistoryList
        # &TenantId=t384tolsj****\
        # &StartTime=2021-12-14T02:34:49Z
        # &EndTime=2021-12-14T08:34:49Z
        # &SQLId=8D6E84735C0****1823D199E2CA1****\
        # &PageNumber=1
        # &PageSize=10
        # &Common request parameters
        # ```
        self.max_elapsed_time = max_elapsed_time
        # The wait time of the client.
        self.memstore_read_row_count = memstore_read_row_count
        # The number of rows read from the disk.
        self.miss_plans = miss_plans
        # $.parameters[7].schema.example
        self.net_wait_time = net_wait_time
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.node_ip = node_ip
        # $.parameters[6].schema.description
        self.queue_time = queue_time
        # The end time.
        self.rpccount = rpccount
        # The time to wait for decoding.
        self.remote_plans = remote_plans
        # The number of block index cache hits.
        self.retry_count = retry_count
        # The number of executions per second.
        self.return_rows = return_rows
        # The execution history of the slow SQL statement.
        self.row_cache_hit = row_cache_hit
        # You can call this operation to query the execution history of an SQL statement by SQL ID that is determined as a slow SQL statement during a specified period of time.
        self.schedule_time = schedule_time
        # The return result of the request.
        self.sql_id = sql_id
        # The IP address of the client.
        self.sql_type = sql_type
        # The scheduling duration.
        self.ssstore_read_row_count = ssstore_read_row_count
        # The return result of the request.
        self.tenant_name = tenant_name
        self.total_wait_time = total_wait_time
        # The number of physical reads.
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
        # The SQL ID, which uniquely identifies an SQL statement.
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
        # The end time of the time range for querying the execution history of the slow SQL statement.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.request_id = request_id
        # Hard parsing time。
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
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.db_name = db_name
        self.end_time = end_time
        # The filter condition.
        self.filter_condition = filter_condition
        # The number of plan misses.
        self.node_ip = node_ip
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.page_number = page_number
        # The return result of the request.
        self.page_size = page_size
        # The internal wait time.
        self.sqlid = sqlid
        # Alibaba Cloud CLI
        self.search_key_word = search_key_word
        # The IP address of the database node.
        self.search_parameter = search_parameter
        # The queuing time.
        self.search_rule = search_rule
        # The list of slow SQL statements.
        self.search_value = search_value
        # The number of rows to return on each page.  
        # - Maximum value: 100  
        # - Default value: 10
        self.sort_column = sort_column
        # The average CPU time.
        self.sort_order = sort_order
        # The list of slow SQL statements.
        self.start_time = start_time
        # The number of logical reads.
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
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.db_name = db_name
        self.end_time = end_time
        # The filter condition.
        self.filter_condition_shrink = filter_condition_shrink
        # The number of plan misses.
        self.node_ip = node_ip
        # The number of the page to return.    
        # - Start value: 1   
        # - Default value: 1
        self.page_number = page_number
        # The return result of the request.
        self.page_size = page_size
        # The internal wait time.
        self.sqlid = sqlid
        # Alibaba Cloud CLI
        self.search_key_word = search_key_word
        # The IP address of the database node.
        self.search_parameter = search_parameter
        # The queuing time.
        self.search_rule = search_rule
        # The list of slow SQL statements.
        self.search_value = search_value
        # The number of rows to return on each page.  
        # - Maximum value: 100  
        # - Default value: 10
        self.sort_column = sort_column
        # The average CPU time.
        self.sort_order = sort_order
        # The list of slow SQL statements.
        self.start_time = start_time
        # The number of logical reads.
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
        # The username.
        self.affected_rows = affected_rows
        # The average response time.
        self.app_wait_time = app_wait_time
        # The wait time in concurrent execution.
        self.block_cache_hit = block_cache_hit
        # The request ID.
        self.block_index_cache_hit = block_index_cache_hit
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        # ```
        # http(s)://[Endpoint]/?Action=DescribeSlowSQLList
        # &TenantId=t2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &DbName=testdb
        # &SearchKeyWord=update
        # &SearchParameter=cputime
        # &SearchRule=>
        # &SearchValue=0.01
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &NodeIp=i-bp18qljorblo8es*****\
        # &PageNumber=10
        # &PageSize=1
        # &SortColumn=cputime
        # &SortOrder=desc
        # &Common request parameters
        # ```
        self.client_ip = client_ip
        # The sorted column.
        self.concurrency_wait_time = concurrency_wait_time
        # The wait event.
        self.cpu_time = cpu_time
        # The search value.
        self.db_name = db_name
        # The time spent in hard parsing.
        self.decode_time = decode_time
        # The IP address of the client.
        self.disk_read = disk_read
        # The search rule.
        self.elapsed_time = elapsed_time
        # The number of row cache hits.
        self.event = event
        # The total count.
        self.exec_per_second = exec_per_second
        # The number of block cache hits.
        self.execute_time = execute_time
        # The IP address of the node.
        self.executions = executions
        # {"name":"DescribeSlowSQLList","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"GET|POST","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeSlowSQLList\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"t2mr3oae0****\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-09-13T15:40:43Z\"},{\"name\":\"DbName\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"SearchKeyWord\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"update\"},{\"name\":\"SearchParameter\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SearchRule\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\">\"},{\"name\":\"SearchValue\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"0.01\"},{\"name\":\"SQLId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"NodeIp\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"i-bp18qljorblo8es*****\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"FilterCondition\",\"position\":\"Body\",\"style\":\"json\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"[dbName:sys]\"},{\"name\":\"SortColumn\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"cputime\"},{\"name\":\"SortOrder\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"desc\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"TotalCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"title\":\"\",\"description\":\"\",\"example\":\"2\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"473469C7-AA6F-4DC5-B3DB-A3DC0DE3C83E\"},{\"name\":\"SlowSQLList\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Array\",\"subType\":\"Object\",\"description\":\"  \",\"children\":[{\"name\":\"Key\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"ExecPerSecond\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"163.0\"},{\"name\":\"SQLText\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"SELECT  ****   FROM ****   WHERE **** = ? AND **** = ?   ORDER BY **** ASC\"},{\"name\":\"MaxCpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"257.967\"},{\"name\":\"BlockCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"14\"},{\"name\":\"DecodeTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"RemotePlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"RPCCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NetWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"DiskRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"NodeIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"i-bp18qljorblo8es*****\"},{\"name\":\"ConcurrencyWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"MemstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"527\"},{\"name\":\"DbName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"testdb\"},{\"name\":\"AppWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"ElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"76.382\"},{\"name\":\"MissPlans\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"AffectedRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"ScheduleTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"Event\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"mysql response wait client\"},{\"name\":\"TotalWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"10.966\"},{\"name\":\"ReturnRows\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"ExecuteTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"61.044\"},{\"name\":\"UserName\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"tester\"},{\"name\":\"Executions\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"89403\"},{\"name\":\"GetPlanTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.052\"},{\"name\":\"CpuTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"50.13\"},{\"name\":\"MaxElapsedTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"260.044\"},{\"name\":\"SQLType\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"BlockIndexCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"4\"},{\"name\":\"RetryCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"SQLId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"SQLID。\",\"example\":\"8D6E84****0B8FB1823D199E2CA1****\"},{\"name\":\"ClientIp\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"1*2.***.1*3.***\"},{\"name\":\"BloomFilterCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"IOWaitTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"0.0\"},{\"name\":\"FailTimes\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"QueueTime\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Float\",\"description\":\"\",\"example\":\"15.275\"},{\"name\":\"RowCacheHit\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"0\"},{\"name\":\"LogicalRead\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"19\"},{\"name\":\"SsstoreReadRowCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Long\",\"description\":\"\",\"example\":\"43086\"}],\"title\":\"\"}],\"title\":\"\",\"description\":\"\"}","errors":"{}"}
        self.fail_times = fail_times
        # The number of Bloom filter cache hits.
        self.get_plan_time = get_plan_time
        # You can call this operation to query the list of slow SQL statements
        self.iowait_time = iowait_time
        # The scheduling duration.
        self.key = key
        self.logical_read = logical_read
        # The name of the database.
        self.max_cpu_time = max_cpu_time
        # The sequence number of the returned SQL statement.
        self.max_elapsed_time = max_elapsed_time
        # The number of logical reads.
        self.memstore_read_row_count = memstore_read_row_count
        # The number of RPCs.
        self.miss_plans = miss_plans
        # The search parameter.
        self.net_wait_time = net_wait_time
        # The number of failures.
        self.node_ip = node_ip
        self.queue_time = queue_time
        # The maximum response time.
        self.rpccount = rpccount
        # The search keyword.
        self.remote_plans = remote_plans
        # The number of physical reads.
        self.retry_count = retry_count
        # The wait time of the client.
        self.return_rows = return_rows
        self.row_cache_hit = row_cache_hit
        # Example 1
        self.sqlid = sqlid
        # The network latency.
        self.sqltext = sqltext
        # SQLID.
        self.sqltype = sqltype
        # The internal execution time.
        self.schedule_time = schedule_time
        self.ssstore_read_row_count = ssstore_read_row_count
        # The SQL ID, which uniquely identifies an SQL statement.
        self.total_wait_time = total_wait_time
        # The number of executions.
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
        # The SQL text.
        self.request_id = request_id
        # The sorting rule.
        self.slow_sqllist = slow_sqllist
        # The name of the database.
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
        # The status of the Internet address for accessing the tenant. Valid values:   
        # - CLOSED: The address is disabled.   
        # - ALLOCATING_INTERNET_ADDRESS: An address is being applied for.   
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The address is being disabled.   
        # - ONLINE: The address is in service.
        self.instance_id = instance_id
        # Indicates whether to enable transaction splitting.
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
        address_type: str = None,
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
        transaction_split: bool = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The primary zone of the tenant.
        self.address_type = address_type
        # 是否开启事务拆分
        self.connection_role = connection_role
        # The Internet address for accessing the tenant.
        self.connection_zones = connection_zones
        # The ID of the VPC.
        self.internet_address = internet_address
        # 实例系列
        self.internet_address_status = internet_address_status
        # 实例类型
        self.internet_port = internet_port
        # The deployment type of the cluster. Valid values:  
        # - multiple: multi-IDC deployment   
        # - single: single-IDC deployment   
        # - dual: dual-IDC deployment
        self.intranet_address = intranet_address
        # PayCore business database
        self.intranet_address_master_zone_id = intranet_address_master_zone_id
        # The total number of CPU cores of the tenant.
        self.intranet_address_slave_zone_id = intranet_address_slave_zone_id
        # 付费类型
        self.intranet_address_status = intranet_address_status
        # The ID of the tenant.
        self.intranet_port = intranet_port
        # The primary zone corresponding to the address for accessing the tenant.
        self.transaction_split = transaction_split
        # The connection access information of the tenant.
        self.v_switch_id = v_switch_id
        # The service mode of the connection address. Valid values:  
        # ReadWrite: provides strong-consistency read and write services.   
        # ReadOnly: provides the read-only service to ensure ultimate consistency of data.   
        # Clog: provides transaction log services.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
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
        if self.transaction_split is not None:
            result['TransactionSplit'] = self.transaction_split
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
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
        if m.get('TransactionSplit') is not None:
            self.transaction_split = m.get('TransactionSplit')
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
        # The data replica distribution mode of the tenant.    
        # 
        # - For the high availability version, N-N-N indicates the three-zone mode, and N-N indicates the dual-zone or single-zone mode.
        # - For the basic version, N indicates the single-zone mode. 
        # 
        # > <br>N represents the number of nodes in a single zone.
        self.total_cpu = total_cpu
        # The zone corresponding to the tenant connection.
        self.unit_cpu = unit_cpu
        # The tenant mode.   
        # Valid values: 
        # Oracle   
        # MySQL
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
        # The total memory size of the tenant, in GB.
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
        # The information about the memory resources of the tenant.
        self.total_memory = total_memory
        # The time when the tenant was created.
        self.unit_memory = unit_memory
        # The status of the Internet address for accessing the tenant. Valid values:   
        # Closed: The address is disabled.   
        # - ALLOCATING_INTERNET_ADDRESS: An address is being applied for.   
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The address is being disabled.   
        # - ONLINE: The address is in service.
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
        # The enabling status of the Clog service.  
        # CLOSED: The Clog service is disabled.  
        # - ONLINE: The Clog service is running.
        self.cpu = cpu
        # The status of the intranet address for accessing the tenant.  
        # The value ONLINE indicates that the address is in service.
        self.disk_size = disk_size
        # The description of the tenant.
        self.memory = memory
        # Alibaba Cloud CLI
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
        # 是否允许开启读写分离地址
        self.region = region
        # The intranet port for accessing the tenant.
        self.tenant_zone_id = tenant_zone_id
        # The character set.
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
        available_zones: List[str] = None,
        charset: str = None,
        clog_service_status: str = None,
        collation: str = None,
        create_time: str = None,
        deploy_mode: str = None,
        deploy_type: str = None,
        description: str = None,
        disk_type: str = None,
        enable_binlog_service: bool = None,
        enable_clog_service: bool = None,
        enable_internet_address_service: bool = None,
        enable_read_write_split: bool = None,
        instance_type: str = None,
        master_intranet_address_zone: str = None,
        pay_type: str = None,
        primary_zone: str = None,
        primary_zone_deploy_type: str = None,
        series: str = None,
        status: str = None,
        tenant_connections: List[DescribeTenantResponseBodyTenantTenantConnections] = None,
        tenant_id: str = None,
        tenant_mode: str = None,
        tenant_name: str = None,
        tenant_resource: DescribeTenantResponseBodyTenantTenantResource = None,
        tenant_zones: List[DescribeTenantResponseBodyTenantTenantZones] = None,
        vpc_id: str = None,
    ):
        # DescribeTenant
        self.available_zones = available_zones
        # The number of CPU cores in each resource unit of the tenant.
        self.charset = charset
        # 地址类型
        self.clog_service_status = clog_service_status
        # The request ID.
        self.collation = collation
        # You can call this operation to create a single tenant in a specific cluster.
        self.create_time = create_time
        # The list of zones.
        self.deploy_mode = deploy_mode
        # The series of the instance.
        self.deploy_type = deploy_type
        # Indicates whether to enable read/write splitting endpoint.
        self.description = description
        # You can call this operation to query the information of a specific tenant in a specific cluster.
        self.disk_type = disk_type
        # 是否可以申请Binlog服务
        self.enable_binlog_service = enable_binlog_service
        # The intranet address for accessing the tenant.
        self.enable_clog_service = enable_clog_service
        # The deployment type of the primary zone.
        self.enable_internet_address_service = enable_internet_address_service
        self.enable_read_write_split = enable_read_write_split
        # {
        #     "RequestId": "EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C",
        #     "Tenant": {
        #         "TenantId": "t33h8y08k****",
        #         "TenantName": "pay_online",
        #         "TenantMode": "Oracle",
        #         "VpcId": "vpc-bp1d2q3mhg9i23ofi****",
        #         "Status": "ONLINE",
        #         "PrimaryZone": "cn-hangzhou-i",
        #         "DeployType": "multiple",
        #         "DeployMode": "1-1-1",
        #         "Description": "PayCore business database",
        #         "CreateTime": "2021-09-17 15:52:17",
        #         "TenantResource": {
        #             "UnitNum": 1,
        #             "Cpu": {
        #                 "UsedCpu": 8,
        #                 "TotalCpu": 10,
        #                 "UnitCpu": 8
        #             },
        #             "Memory": {
        #                 "UsedMemory": 30,
        #                 "TotalMemory": 64,
        #                 "UnitMemory": 32
        #             },
        #             "DiskSize": {
        #                 "UsedDiskSize": 86
        #             }
        #         },
        #         "TenantConnections": [
        #             {
        #                 "ConnectionRole": "ReadWrite",
        #                 "IntranetAddress": "t32a7ru5u****.oceanbase.aliyuncs.com",
        #                 "IntranetPort": 3306,
        #                 "InternetAddress": "t32a7ru5u****mo.oceanbase.aliyuncs.com",
        #                 "InternetPort": 3306,
        #                 "VpcId": "vpc-bp1qiail1asmfe23t****",
        #                 "VSwitchId": "vsw-bp11k1aypnzu1l3whi****",
        #                 "IntranetAddressMasterZoneId": "cn-hangzhou-i",
        #                 "IntranetAddressSlaveZoneId": "cn-hangzhou-j",
        #                 "IntranetAddressStatus": "ONLINE",
        #                 "ConnectionZones": [
        #                     "cn-hangzhou-i"
        #                 ],
        #                 "InternetAddressStatus": "CLOSED"
        #             }
        #         ],
        #         "TenantZones": [
        #             {
        #                 "TenantZoneId": "cn-hangzhou-i",
        #                 "Region": "cn-hangzhou",
        #                 "TenantZoneRole": "ReadOnly"
        #             }
        #         ],
        #         "ClogServiceStatus": "CLOSED"
        #     }
        # }
        self.instance_type = instance_type
        # ```
        # http(s)://[Endpoint]/?Action=DescribeTenant
        # &InstanceId=ob317v4uif****\
        # &TenantId=ob2mr3oae0****\
        # &Common request parameters
        # ```
        self.master_intranet_address_zone = master_intranet_address_zone
        self.pay_type = pay_type
        # The type of the payment.
        self.primary_zone = primary_zone
        # Example 1
        self.primary_zone_deploy_type = primary_zone_deploy_type
        # <DescribeTenantResponse>
        #     <RequestId>EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C</RequestId>
        #     <Tenant>
        #         <TenantId>t33h8y08k****</TenantId>
        #         <TenantName>pay_online</TenantName>
        #         <TenantMode>Oracle</TenantMode>
        #         <VpcId>vpc-bp1d2q3mhg9i23ofi****</VpcId>
        #         <Status>ONLINE</Status>
        #         <PrimaryZone>cn-hangzhou-i</PrimaryZone>
        #         <DeployType>multiple</DeployType>
        #         <DeployMode>1-1-1</DeployMode>
        #         <Description>PayCore business database</Description>
        #         <CreateTime>2021-09-17 15:52:17</CreateTime>
        #         <TenantResource>
        #             <UnitNum>1</UnitNum>
        #             <Cpu>
        #                 <UsedCpu>8</UsedCpu>
        #                 <TotalCpu>10</TotalCpu>
        #                 <UnitCpu>8</UnitCpu>
        #             </Cpu>
        #             <Memory>
        #                 <UsedMemory>30</UsedMemory>
        #                 <TotalMemory>64</TotalMemory>
        #                 <UnitMemory>32</UnitMemory>
        #             </Memory>
        #             <DiskSize>
        #                 <UsedDiskSize>86</UsedDiskSize>
        #             </DiskSize>
        #         </TenantResource>
        #         <TenantConnections>
        #             <ConnectionRole>ReadWrite</ConnectionRole>
        #             <IntranetAddress>t32a7ru5u****.oceanbase.aliyuncs.com</IntranetAddress>
        #             <IntranetPort>3306</IntranetPort>
        #             <InternetAddress>t32a7ru5u****mo.oceanbase.aliyuncs.com</InternetAddress>
        #             <InternetPort>3306</InternetPort>
        #             <VpcId>vpc-bp1qiail1asmfe23t****</VpcId>
        #             <VSwitchId>vsw-bp11k1aypnzu1l3whi****</VSwitchId>
        #             <IntranetAddressMasterZoneId>cn-hangzhou-i</IntranetAddressMasterZoneId>
        #             <IntranetAddressSlaveZoneId>cn-hangzhou-j</IntranetAddressSlaveZoneId>
        #             <IntranetAddressStatus>ONLINE</IntranetAddressStatus>
        #             <ConnectionZones>cn-hangzhou-i</ConnectionZones>
        #             <InternetAddressStatus>CLOSED</InternetAddressStatus>
        #         </TenantConnections>
        #         <TenantZones>
        #             <TenantZoneId>cn-hangzhou-i</TenantZoneId>
        #             <Region>cn-hangzhou</Region>
        #             <TenantZoneRole>ReadOnly</TenantZoneRole>
        #         </TenantZones>
        #         <ClogServiceStatus>CLOSED</ClogServiceStatus>
        #     </Tenant>
        # </DescribeTenantResponse>
        self.series = series
        # The character set.
        self.status = status
        # The status of the tenant.   
        # - PENDING_CREATE: The tenant is being created.   
        # - RESTORE: The tenant is being recovered.   
        # - ONLINE: The tenant is running.   
        # - SPEC_MODIFYING: The specification of the tenant is being modified.   
        # - ALLOCATING_INTERNET_ADDRESS: An Internet address is being allocated.  
        # - PENDING_OFFLINE_INTERNET_ADDRESS: The Internet address is being disabled.  
        # - PRIMARY_ZONE_MODIFYING: The tenant is switching to a new primary zone.  
        # - PARAMETER_MODIFYING: Parameters are being modified.   
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.
        self.tenant_connections = tenant_connections
        # The region where the zone of the tenant resides.
        self.tenant_id = tenant_id
        # The enabling status of the clog service.  
        # - CLOSED: The clog service is disabled.  
        # - ONLINE: The clog service is running.
        self.tenant_mode = tenant_mode
        # The request type of the zone of the tenant.  ReadWrite: The zone supports data reads and writes. ReadOnly: The zone supports only data reads. For a high availability cluster with multiple IDCs, the primary zone provides ReadWrite services, and the standby zone provides ReadOnly services. For a high availability cluster with a single IDC, all zones provide ReadWrite services.
        self.tenant_name = tenant_name
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.tenant_resource = tenant_resource
        # The standby zone corresponding to the address for accessing the tenant.
        self.tenant_zones = tenant_zones
        # Indicates whether the clog service is available. To enable the clog service, submit a ticket.
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
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones
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
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.enable_binlog_service is not None:
            result['EnableBinlogService'] = self.enable_binlog_service
        if self.enable_clog_service is not None:
            result['EnableClogService'] = self.enable_clog_service
        if self.enable_internet_address_service is not None:
            result['EnableInternetAddressService'] = self.enable_internet_address_service
        if self.enable_read_write_split is not None:
            result['EnableReadWriteSplit'] = self.enable_read_write_split
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.master_intranet_address_zone is not None:
            result['MasterIntranetAddressZone'] = self.master_intranet_address_zone
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.primary_zone_deploy_type is not None:
            result['PrimaryZoneDeployType'] = self.primary_zone_deploy_type
        if self.series is not None:
            result['Series'] = self.series
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
        if m.get('AvailableZones') is not None:
            self.available_zones = m.get('AvailableZones')
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
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('EnableBinlogService') is not None:
            self.enable_binlog_service = m.get('EnableBinlogService')
        if m.get('EnableClogService') is not None:
            self.enable_clog_service = m.get('EnableClogService')
        if m.get('EnableInternetAddressService') is not None:
            self.enable_internet_address_service = m.get('EnableInternetAddressService')
        if m.get('EnableReadWriteSplit') is not None:
            self.enable_read_write_split = m.get('EnableReadWriteSplit')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MasterIntranetAddressZone') is not None:
            self.master_intranet_address_zone = m.get('MasterIntranetAddressZone')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('PrimaryZoneDeployType') is not None:
            self.primary_zone_deploy_type = m.get('PrimaryZoneDeployType')
        if m.get('Series') is not None:
            self.series = m.get('Series')
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
        # The zone information of the tenant.
        self.request_id = request_id
        # The ID of the zone.
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
        # 2021-06-13T15:40:43Z
        self.instance_id = instance_id
        # {"name":"DescribeTenantMetrics","product":"OceanBasePro","version":"2019-09-01","path":"/","deprecated":0,"method":"POST|GET","protocol":"HTTP|HTTPS","hidden":0,"timeout":10000,"parameter_type":"Single","params":"[{\"name\":\"Action\",\"position\":\"Query\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"description\":\"\",\"example\":\"DescribeTenantMetrics\"},{\"name\":\"InstanceId\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"ob317v4uif****\"},{\"name\":\"PageSize\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"10\"},{\"name\":\"PageNumber\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"1\"},{\"name\":\"TenantName\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":true,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"pay_online\"},{\"name\":\"StartTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:40:43Z\"},{\"name\":\"EndTime\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"2021-06-13T15:45:43Z\"},{\"name\":\"Metrics\",\"position\":\"Body\",\"required\":true,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tps\"},{\"name\":\"TenantId\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":true,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"tfafd34fs****\"},{\"name\":\"TenantIdList\",\"position\":\"Body\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"[tdak3nac****,tdakc42df****]\"}]","response_headers":"[]","response":"{\"type\":\"Object\",\"children\":[{\"name\":\"TotalCount\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"Integer\",\"title\":\"\",\"description\":\"\",\"example\":\"9\"},{\"name\":\"RequestId\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C\"},{\"name\":\"TenantMetrics\",\"required\":false,\"checkBlank\":false,\"visibility\":\"Public\",\"deprecated\":false,\"type\":\"String\",\"title\":\"\",\"description\":\"\",\"example\":\"\\\"Metrics\\\":[ {\\\"request_queue_rt\\\":0.0,\\\"TimeStamp\\\":\\\"2022-02-23T01:58:00Z\\\"}]\"}],\"title\":\"\",\"description\":\"\"}","errors":"{}"}
        self.metrics = metrics
        # The ID of the OceanBase cluster.
        self.page_number = page_number
        # tfafd34fs****\
        self.page_size = page_size
        # Example 1
        self.start_time = start_time
        self.tenant_id = tenant_id
        self.tenant_id_list = tenant_id_list
        # 2021-06-13T15:45:43Z
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


class DescribeTenantSecurityConfigsRequest(TeaModel):
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


class DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigsSecurityConfigs(TeaModel):
    def __init__(
        self,
        config_description: str = None,
        config_group: str = None,
        config_name: str = None,
        risk: bool = None,
        risk_description: str = None,
    ):
        self.config_description = config_description
        self.config_group = config_group
        self.config_name = config_name
        self.risk = risk
        self.risk_description = risk_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_description is not None:
            result['ConfigDescription'] = self.config_description
        if self.config_group is not None:
            result['ConfigGroup'] = self.config_group
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.risk is not None:
            result['Risk'] = self.risk
        if self.risk_description is not None:
            result['RiskDescription'] = self.risk_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigDescription') is not None:
            self.config_description = m.get('ConfigDescription')
        if m.get('ConfigGroup') is not None:
            self.config_group = m.get('ConfigGroup')
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('Risk') is not None:
            self.risk = m.get('Risk')
        if m.get('RiskDescription') is not None:
            self.risk_description = m.get('RiskDescription')
        return self


class DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigs(TeaModel):
    def __init__(
        self,
        risk_count: int = None,
        security_configs: List[DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigsSecurityConfigs] = None,
        tenant_id: str = None,
        tenant_name: str = None,
    ):
        self.risk_count = risk_count
        self.security_configs = security_configs
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name

    def validate(self):
        if self.security_configs:
            for k in self.security_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        result['SecurityConfigs'] = []
        if self.security_configs is not None:
            for k in self.security_configs:
                result['SecurityConfigs'].append(k.to_map() if k else None)
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        self.security_configs = []
        if m.get('SecurityConfigs') is not None:
            for k in m.get('SecurityConfigs'):
                temp_model = DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigsSecurityConfigs()
                self.security_configs.append(temp_model.from_map(k))
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class DescribeTenantSecurityConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        tenant_security_configs: List[DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigs] = None,
        total_check_count: int = None,
        total_risk_count: int = None,
    ):
        self.tenant_security_configs = tenant_security_configs
        self.total_check_count = total_check_count
        self.total_risk_count = total_risk_count

    def validate(self):
        if self.tenant_security_configs:
            for k in self.tenant_security_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TenantSecurityConfigs'] = []
        if self.tenant_security_configs is not None:
            for k in self.tenant_security_configs:
                result['TenantSecurityConfigs'].append(k.to_map() if k else None)
        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count
        if self.total_risk_count is not None:
            result['TotalRiskCount'] = self.total_risk_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tenant_security_configs = []
        if m.get('TenantSecurityConfigs') is not None:
            for k in m.get('TenantSecurityConfigs'):
                temp_model = DescribeTenantSecurityConfigsResponseBodyConfigsTenantSecurityConfigs()
                self.tenant_security_configs.append(temp_model.from_map(k))
        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')
        if m.get('TotalRiskCount') is not None:
            self.total_risk_count = m.get('TotalRiskCount')
        return self


class DescribeTenantSecurityConfigsResponseBody(TeaModel):
    def __init__(
        self,
        configs: DescribeTenantSecurityConfigsResponseBodyConfigs = None,
        request_id: str = None,
    ):
        self.configs = configs
        self.request_id = request_id

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            temp_model = DescribeTenantSecurityConfigsResponseBodyConfigs()
            self.configs = temp_model.from_map(m['Configs'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeTenantSecurityConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantSecurityConfigsResponseBody = None,
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
            temp_model = DescribeTenantSecurityConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantSecurityIpGroupsRequest(TeaModel):
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


class DescribeTenantSecurityIpGroupsResponseBodySecurityIpGroups(TeaModel):
    def __init__(
        self,
        security_ip_group_name: str = None,
        security_ip_group_type: str = None,
        security_ips: str = None,
        tenant_id: str = None,
    ):
        self.security_ip_group_name = security_ip_group_name
        self.security_ip_group_type = security_ip_group_type
        self.security_ips = security_ips
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ip_group_type is not None:
            result['SecurityIpGroupType'] = self.security_ip_group_type
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIpGroupType') is not None:
            self.security_ip_group_type = m.get('SecurityIpGroupType')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeTenantSecurityIpGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_groups: List[DescribeTenantSecurityIpGroupsResponseBodySecurityIpGroups] = None,
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
                temp_model = DescribeTenantSecurityIpGroupsResponseBodySecurityIpGroups()
                self.security_ip_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTenantSecurityIpGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantSecurityIpGroupsResponseBody = None,
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
            temp_model = DescribeTenantSecurityIpGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTenantTagsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tags: str = None,
        tenant_ids: str = None,
    ):
        self.instance_id = instance_id
        self.tags = tags
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
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenant_ids is not None:
            result['TenantIds'] = self.tenant_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TenantIds') is not None:
            self.tenant_ids = m.get('TenantIds')
        return self


class DescribeTenantTagsResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DescribeTenantTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_resources: List[DescribeTenantTagsResponseBodyTagResources] = None,
    ):
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = DescribeTenantTagsResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class DescribeTenantTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTenantTagsResponseBody = None,
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
            temp_model = DescribeTenantTagsResponseBody()
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
        # The database privileges of the account.
        self.page_number = page_number
        # The return result of the request.
        self.page_size = page_size
        # The return result of the request.
        self.search_key = search_key
        # The return result of the request.
        self.tenant_id = tenant_id
        # The operation that you want to perform.   
        # Set the value to **DescribeTenantUsers**.
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
        instance_id: str = None,
        tenant_id: str = None,
        user_name: str = None,
        user_status: str = None,
        user_type: str = None,
    ):
        self.databases = databases
        self.description = description
        # 所属集群Id
        self.instance_id = instance_id
        # 所属租户Id
        self.tenant_id = tenant_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
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
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
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
        # The name of the database account.
        self.request_id = request_id
        # The type of the database account. Valid values:    
        # - Admin: the super administrator account.   
        # - NORMAL: a general account.
        self.tenant_users = tenant_users
        # The role of the account.   
        # In Oracle mode, a role is a schema-level role. Valid values:  
        # - ReadWrite: a role that has the read and write privileges, including: CREATE TABLE, CREATE VIEW, CREATE PROCEDURE, CREATE SYNONYM, CREATE SEQUENCE, CREATE TRIGGER, CREATE TYPE, CREATE SESSION, EXECUTE ANY PROCEDURE, CREATE ANY OUTLINE, ALTER ANY OUTLINE, DROP ANY OUTLINE, CREATE ANY PROCEDURE, ALTER ANY PROCEDURE, DROP ANY PROCEDURE, CREATE ANY SEQUENCE, ALTER ANY SEQUENCE, DROP ANY SEQUENCE, CREATE ANY TYPE, ALTER ANY TYPE, DROP ANY TYPE, SYSKM, CREATE ANY TRIGGER, ALTER ANY TRIGGER, DROP ANY TRIGGER, CREATE PROFILE, ALTER PROFILE, and DROP PROFILE.  
        # - ReadOnly: a role that has only the read-only privilege SELECT.
        # In MySQL mode, a role is a database-level role. Valid values: 
        # - ReadWrite: a role that has the read and write privileges, namely ALL PRIVILEGES.   
        # - ReadOnly: a role that has only the read-only privilege SELECT.   
        # - DDL: a role that has the DDL privileges such as CREATE, DROP, ALTER, SHOW VIEW, and CREATE VIEW.   
        # - DML: a role that has the DML privileges such as SELECT, INSERT, UPDATE, DELETE, and SHOW VIEW.   
        # 
        # > <br>By default, an Oracle account has the read and write privileges on its own schema, which are not listed here.
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
        # The zone information of the tenant.
        self.instance_id = instance_id
        # The return result of the request.
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
        # Example 1
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
        # Indicates whether a read-only connection needs to be created for the zone.
        self.request_id = request_id
        # The request ID.
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
        # The number of used disks of the tenant.
        self.instance_id = instance_id
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
        self.page_number = page_number
        # You can call this operation to query the tenants in an OceanBase cluster.
        self.page_size = page_size
        # The primary zone of the tenant.
        self.search_key = search_key
        # Alibaba Cloud CLI
        self.tenant_id = tenant_id
        # The information of tenants.
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
        # The total number of CPU cores of the tenant.
        self.cpu = cpu
        # The number of CPU cores in each resource unit of the tenant.
        self.create_time = create_time
        # The search keyword.
        self.deploy_mode = deploy_mode
        # The name of the tenant.   
        # It must start with a letter or an underscore (_), and contain 2 to 20 characters, which can be uppercase letters, lowercase letters, digits, and underscores (_).  It cannot be set to sys.
        self.deploy_type = deploy_type
        # Example 1
        self.description = description
        # The number of the page to return.   
        # Start value: 1
        # - Default value: 1
        self.mem = mem
        # The return result of the request.
        self.primary_zone = primary_zone
        # The status of the tenant.  <br>
        # - PENDING_CREATE: The tenant is being created.
        # - RESTORE: The tenant is being recovered.
        # - ONLINE: The tenant is running.
        # - SPEC_MODIFYING: The specification of the tenant is being modified.
        # ALLOCATING_INTERNET_ADDRESS: An Internet address is being allocated.
        # PENDING_OFFLINE_INTERNET_ADDRESS: The Internet address is being disabled.
        # - PRIMARY_ZONE_MODIFYING: The tenant is switching to a new primary zone.
        # - PARAMETER_MODIFYING: Parameters are being modified.
        # - WHITE_LIST_MODIFYING: The whitelist is being modified.
        self.status = status
        # You can call this operation to query the tenants in an OceanBase cluster.
        self.tenant_id = tenant_id
        # {
        #     "TotalCount": 1,
        #     "RequestId": "EE205C00-30E4-XXXX-XXXX-87E3A8A2AA0C",
        #     "Tenants": [
        #         {
        #             "VpcId": "vpc-bp1d2q3mhg9i23ofi****",
        #             "Status": "ONLINE",
        #             "PrimaryZone": "cn-hangzhou-i",
        #             "DeployType": "multiple",
        #             "DeployMode": "1-1-1",
        #             "CreateTime": "2021-09-17 15:52:17.0",
        #             "TenantName": "pay_online",
        #             "Mem": 20,
        #             "Cpu": 10,
        #             "Description": "PayCore business database",
        #             "TenantMode": "Oracle",
        #             "TenantId": "t33h8y08k****",
        #             "UnitCpu": 5,
        #             "UnitMem": 10,
        #             "UnitNum": 2,
        #             "UsedDiskSize": 10
        #         }
        #     ]
        # }
        self.tenant_mode = tenant_mode
        # The information of tenants.
        self.tenant_name = tenant_name
        self.unit_cpu = unit_cpu
        self.unit_mem = unit_mem
        self.unit_num = unit_num
        self.used_disk_size = used_disk_size
        # The time when the tenant was created.
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
        # The ID of the tenant.
        self.request_id = request_id
        # The ID of the OceanBase cluster.
        self.tenants = tenants
        # The total memory size of the tenant, in GB.
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
        # Example 1
        self.description = description
        # The operation that you want to perform.   
        # Set the value to **DescribeTimeZones**.
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
        # The list of time zones.
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
        # DescribeTimeZones
        self.request_id = request_id
        # The description of the time zone.
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
        # The number of block index cache hits.
        self.db_name = db_name
        # The SQL type.
        self.end_time = end_time
        # The average number of logical reads of the SQL statement during the specified period of time.   
        # The value covers the numbers of reads of different caches and the number of disk I/Os. It is an important metric for measuring the SQL filtering performance.   
        # 
        # > <br> A higher ratio of the number of logical reads to the number of returned rows indicates poorer filtering performance. General causes include non-standard content written by SQL statements, non-standard table indexes created, and non-standard SQL execution plans.
        self.filter_condition = filter_condition
        # The number of failures.
        self.node_ip = node_ip
        # The queuing time, in ms.
        self.page_number = page_number
        # The number of row cache hits.
        self.page_size = page_size
        # The I/O wait time, in ms.
        self.sqlid = sqlid
        # The number of retries.
        self.search_key_word = search_key_word
        # SQLID.
        self.search_parameter = search_parameter
        # The IP address of the client.
        self.search_rule = search_rule
        # The number of Bloom filter cache hits.
        self.search_value = search_value
        # The number of rows read from the disk.
        self.sort_column = sort_column
        # The list of top SQL statements.
        self.sort_order = sort_order
        # The maximum response time, in ms.
        self.start_time = start_time
        # The average CPU time, in ms.
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
        # The number of block index cache hits.
        self.db_name = db_name
        # The SQL type.
        self.end_time = end_time
        # The average number of logical reads of the SQL statement during the specified period of time.   
        # The value covers the numbers of reads of different caches and the number of disk I/Os. It is an important metric for measuring the SQL filtering performance.   
        # 
        # > <br> A higher ratio of the number of logical reads to the number of returned rows indicates poorer filtering performance. General causes include non-standard content written by SQL statements, non-standard table indexes created, and non-standard SQL execution plans.
        self.filter_condition_shrink = filter_condition_shrink
        # The number of failures.
        self.node_ip = node_ip
        # The queuing time, in ms.
        self.page_number = page_number
        # The number of row cache hits.
        self.page_size = page_size
        # The I/O wait time, in ms.
        self.sqlid = sqlid
        # The number of retries.
        self.search_key_word = search_key_word
        # SQLID.
        self.search_parameter = search_parameter
        # The IP address of the client.
        self.search_rule = search_rule
        # The number of Bloom filter cache hits.
        self.search_value = search_value
        # The number of rows read from the disk.
        self.sort_column = sort_column
        # The list of top SQL statements.
        self.sort_order = sort_order
        # The maximum response time, in ms.
        self.start_time = start_time
        # The average CPU time, in ms.
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
        # The internal wait time, in ms.
        self.affected_rows = affected_rows
        # The wait time in concurrent execution, in ms.
        self.app_wait_time = app_wait_time
        # The average CPU time, in ms.
        self.block_cache_hit = block_cache_hit
        # $.parameters[16].schema.example
        self.block_index_cache_hit = block_index_cache_hit
        # $.parameters[14].schema.enumValueTitles
        self.bloom_filter_cache_hit = bloom_filter_cache_hit
        # $.parameters[14].schema.description
        self.client_ip = client_ip
        # The number of rows returned.
        self.concurrency_wait_time = concurrency_wait_time
        # The maximum CPU time, in ms.
        self.cpu_time = cpu_time
        # The number of remote plans.
        self.db_name = db_name
        # The number of rows to return on each page.   
        # - Maximum value: 100   
        # - Default value: 10
        self.decode_time = decode_time
        # The IP address of the client.
        self.disk_read = disk_read
        # The sorting rule.
        self.elapsed_time = elapsed_time
        # The number of rows read from the disk.
        self.event = event
        # The operation that you want to perform.   
        # Set the value to **DescribeTopSQLList**.
        self.exec_per_second = exec_per_second
        # The number of rows read from the memory.
        self.execute_time = execute_time
        # The number of executions per second.
        self.executions = executions
        # $.parameters[12].schema.description
        self.fail_times = fail_times
        # The queuing time, in ms.
        self.get_plan_time = get_plan_time
        # $.parameters[15].schema.example
        self.iowait_time = iowait_time
        # The name of the database.
        self.key = key
        # You can call this operation to query SQL execution performance data collected by the diagnostic system.
        self.logical_read = logical_read
        # SQLID.
        self.max_cpu_time = max_cpu_time
        # The sequence number of the returned SQL statement.
        self.max_elapsed_time = max_elapsed_time
        # The name of the database.
        self.memstore_read_row_count = memstore_read_row_count
        # The total count.
        self.miss_plans = miss_plans
        # The end time of the time range for querying TOP SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.net_wait_time = net_wait_time
        # The username.
        self.node_ip = node_ip
        # $.parameters[12].schema.enumValueTitles
        self.queue_time = queue_time
        # The start time of the time range for querying TOP SQL statements.   
        # The value must be UTC time in the format of YYYY-MM-DDThh:mm:ssZ.
        self.rpccount = rpccount
        # The return result of the request.
        self.remote_plans = remote_plans
        # $.parameters[13].schema.description
        self.retry_count = retry_count
        # The wait event.
        self.return_rows = return_rows
        # ```
        # http(s)://[Endpoint]/?Action=DescribeTopSQLList
        # &TenantId=t2mr3oae0****\
        # &StartTime=2021-06-13 15:40:43
        # &EndTime=2021-09-13 15:40:43
        # &DbName=testdb
        # &SearchKeyWord=update
        # &SearchParameter=cputime
        # &SearchRule=>
        # &SearchValue=0.01
        # &SQLId=8D6E84****0B8FB1823D199E2CA1****\
        # &NodeIp=i-bp19y05uq6xpacyqnlrc
        # &PageNumber=1
        # &PageSize=10
        # &SortColumn=cputime
        # &SortOrder=desc
        # &Common request parameters
        # ```
        self.row_cache_hit = row_cache_hit
        # $.parameters[13].schema.example
        self.sqlid = sqlid
        # The list of top SQL statements.
        self.sqltext = sqltext
        # The request ID.
        self.sqltype = sqltype
        # The search keyword.
        self.schedule_time = schedule_time
        self.ssstore_read_row_count = ssstore_read_row_count
        # -\
        self.total_wait_time = total_wait_time
        # The number of Bloom filter cache hits.
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
        # Alibaba Cloud CLI
        self.request_id = request_id
        # The I/O wait time, in ms.
        self.top_sqllist = top_sqllist
        # It is an online CLI tool that allows you to quickly retrieve and debug APIs. It can dynamically generate executable SDK code samples.
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
        # The operation that you want to perform.   
        # Set the value to **DescribeZones**.
        self.deploy_type = deploy_type
        # The deployment mode.
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
        # ```
        # http(s)://[Endpoint]/?Action=DescribeZones
        # &Series=normal
        # &DeployType=single
        # &Common request parameters
        # ```
        self.request_id = request_id
        # You can call this operation to learn of zones where a cluster can be created in an Alibaba Cloud region.
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


class KillProcessListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        session_list: str = None,
        tenant_id: str = None,
    ):
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id
        # The list of the sessions that need to be closed.
        self.session_list = session_list
        # The ID of the tenant.
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
        if self.session_list is not None:
            result['SessionList'] = self.session_list
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SessionList') is not None:
            self.session_list = m.get('SessionList')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class KillProcessListResponseBodyData(TeaModel):
    def __init__(
        self,
        client_ip: str = None,
        command: str = None,
        database: str = None,
        error_message: str = None,
        execute_time: str = None,
        server_ip: str = None,
        session_id: int = None,
        sql_text: str = None,
        status: str = None,
        tenant_id: str = None,
        user: str = None,
    ):
        # The client IP address.
        self.client_ip = client_ip
        # The start command for the container of the application.
        self.command = command
        # The name of the database.
        self.database = database
        # The error message.
        self.error_message = error_message
        # Execution time (UTC+8). If it is left empty, it means to execute immediately.
        self.execute_time = execute_time
        # The IP address of the server.
        self.server_ip = server_ip
        # The ID of the session.
        self.session_id = session_id
        # The SQL statement.
        self.sql_text = sql_text
        # The status of the task.
        self.status = status
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The database username.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.command is not None:
            result['Command'] = self.command
        if self.database is not None:
            result['Database'] = self.database
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.execute_time is not None:
            result['ExecuteTime'] = self.execute_time
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExecuteTime') is not None:
            self.execute_time = m.get('ExecuteTime')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class KillProcessListResponseBody(TeaModel):
    def __init__(
        self,
        data: List[KillProcessListResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
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
                temp_model = KillProcessListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KillProcessListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillProcessListResponseBody = None,
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
            temp_model = KillProcessListResponseBody()
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
        # Example 1
        self.database_name = database_name
        self.description = description
        # The description of the database.
        self.instance_id = instance_id
        # The operation that you want to perform.   
        # Set the value to **ModifyDatabaseDescription**.
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
        # The ID of the tenant.
        self.database_name = database_name
        # The account information.
        self.instance_id = instance_id
        # A list of usernames and their respective roles.
        self.tenant_id = tenant_id
        # The ID of the OceanBase cluster.
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
        # Example 1
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
        # The name of the database.
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
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.instance_id = instance_id
        # The ID of the OceanBase cluster.
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
        # The name of the OceanBase cluster.
        self.instance_name = instance_name
        # The operation that you want to perform.   
        # Set the value to **ModifyInstanceName**.
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


class ModifyInstanceNodeNumRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_num: str = None,
    ):
        self.instance_id = instance_id
        self.node_num = node_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        return self


class ModifyInstanceNodeNumResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceNodeNumResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyInstanceNodeNumResponseBodyData = None,
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
            temp_model = ModifyInstanceNodeNumResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceNodeNumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceNodeNumResponseBody = None,
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
            temp_model = ModifyInstanceNodeNumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        disk_size: int = None,
        instance_class: str = None,
        instance_id: str = None,
    ):
        self.disk_size = disk_size
        self.instance_class = instance_class
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyInstanceSpecResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyInstanceSpecResponseBodyData = None,
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
            temp_model = ModifyInstanceSpecResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceSpecResponseBody = None,
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
            temp_model = ModifyInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTagsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tags: str = None,
    ):
        # The tags.
        self.instance_id = instance_id
        # You can call this operation to modify the value of the cluster tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ModifyInstanceTagsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceTagsResponseBody = None,
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
            temp_model = ModifyInstanceTagsResponseBody()
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
        # The ID of the OceanBase cluster.
        self.dimension = dimension
        # The cause of the modification failure.
        self.dimension_value = dimension_value
        # Alibaba Cloud CLI
        self.instance_id = instance_id
        # The resource ID of the parameter type.    
        # You can leave this parameter unspecified when you call this operation to modify cluster parameters. In the case of tenant parameters, pass the tenant ID.
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
        # The operation that you want to perform.   
        # Set the value to **ModifyParameters**.
        self.request_id = request_id
        # Example 1
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
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id
        # The information of the IP address whitelist group.
        self.security_ip_group_name = security_ip_group_name
        # The list of IP addresses and CIDR blocks in the whitelist.   
        # It is a JSON array. Each object in the array is an IP address or CIDR block. You can specify at most 40 IP addresses or CIDR blocks.
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
        # The request ID.
        self.request_id = request_id
        # Example 1
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
        # The primary zone of the tenant.    
        # It is one of the zones in which the cluster is deployed.
        self.instance_id = instance_id
        # ```
        # http(s)://[Endpoint]/?Action=ModifyTenantPrimaryZone
        # &TenantId=ob2mr3oae0****\
        # &InstanceId=ob317v4uif****\
        # &PrimaryZone=cn-hangzhou-h
        # &Common request parameters
        # ```
        self.master_intranet_address_zone = master_intranet_address_zone
        # The switching mode.
        self.modify_type = modify_type
        # The ID of the vSwitch.
        self.primary_zone = primary_zone
        # Example 1
        self.primary_zone_deploy_type = primary_zone_deploy_type
        # The return result of the request.
        self.tenant_id = tenant_id
        # The request ID.
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
        # The memory size of the tenant, in GB.
        self.cpu = cpu
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantResource**.
        self.instance_id = instance_id
        # The ID of the tenant.
        self.memory = memory
        # The information about the CPU resources of the tenant.
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


class ModifyTenantSecurityIpGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips
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
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantSecurityIpGroupResponseBodySecurityIpGroup(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        security_ip_group_name: str = None,
        security_ips: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.security_ip_group_name = security_ip_group_name
        self.security_ips = security_ips
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
        if self.security_ip_group_name is not None:
            result['SecurityIpGroupName'] = self.security_ip_group_name
        if self.security_ips is not None:
            result['SecurityIps'] = self.security_ips
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SecurityIpGroupName') is not None:
            self.security_ip_group_name = m.get('SecurityIpGroupName')
        if m.get('SecurityIps') is not None:
            self.security_ips = m.get('SecurityIps')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantSecurityIpGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_ip_group: ModifyTenantSecurityIpGroupResponseBodySecurityIpGroup = None,
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
            temp_model = ModifyTenantSecurityIpGroupResponseBodySecurityIpGroup()
            self.security_ip_group = temp_model.from_map(m['SecurityIpGroup'])
        return self


class ModifyTenantSecurityIpGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantSecurityIpGroupResponseBody = None,
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
            temp_model = ModifyTenantSecurityIpGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantTagsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tags: str = None,
        tenant_id: str = None,
    ):
        self.instance_id = instance_id
        self.tags = tags
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
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ModifyTenantTagsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
    ):
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTenantTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyTenantTagsResponseBody = None,
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
            temp_model = ModifyTenantTagsResponseBody()
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
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantUserDescription**.
        self.description = description
        # The ID of the OceanBase cluster.
        self.instance_id = instance_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The description of the database.
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
        # You can call this operation to modify the description of a specified account in a tenant.
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
        encryption_type: str = None,
        instance_id: str = None,
        tenant_id: str = None,
        user_name: str = None,
        user_password: str = None,
    ):
        # 加密方式。
        self.encryption_type = encryption_type
        self.instance_id = instance_id
        # ```
        # http(s)://[Endpoint]/?Action=ModifyTenantUserPassword
        # &UserName=pay_test
        # &TenantId=ob2mr3oae0****\
        # &UserPassword=!Aliyun4Oceanbase
        # &InstanceId=ob317v4uif****\
        # &Common request parameters
        # ```
        self.tenant_id = tenant_id
        # The ID of the OceanBase cluster.
        self.user_name = user_name
        # You can call this operation to change the logon password of a specified account in a tenant.
        self.user_password = user_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encryption_type is not None:
            result['EncryptionType'] = self.encryption_type
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
        if m.get('EncryptionType') is not None:
            self.encryption_type = m.get('EncryptionType')
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
        # The type of the privilege modification operation.   
        # Valid values:  
        # update: updates all privileges. This is the default value.  
        # add: adds a privilege.  
        # delete: deletes a privilege.
        self.instance_id = instance_id
        # The name of the table.
        self.modify_type = modify_type
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantUserRoles**.
        self.tenant_id = tenant_id
        # The role of the database account.
        self.user_name = user_name
        # The type of the account. Valid values:   
        # - Admin: the super administrator account.   
        # - Normal: a general account.
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
        # ```
        # http(s)://[Endpoint]/?Action=ModifyTenantUserRoles
        # &UserName=pay_test
        # &TenantId=ob2mr3oae0****\
        # &UserRole=[{"Database":"20210824160559","Role":"readwrite"}]
        # &InstanceId=ob317v4uif****\
        # &ModifyType=update
        # &Common request parameters
        # ```
        self.database = database
        self.is_success = is_success
        # You can call this operation to modify the database privileges of a specified account in a tenant.
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
        # The name of the database (MySQL mode) or schema (Oracle mode).
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
        # The ID of the tenant.
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
        # The operation that you want to perform.   
        # Set the value to **ModifyTenantUserStatus**.
        self.instance_id = instance_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The list of database accounts in the tenant.
        self.user_name = user_name
        # The status of the database account. Valid values:   
        # - Locked: The account is locked. 
        # - Online: The account is unlocked.
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
        # Example 1
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
        # The total count, which takes effect in a pagination query.
        self.page_number = page_number
        # Contact the administrator.
        self.page_size = page_size
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.project_id = project_id
        # Indicates whether the call is successful.
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
        # The operation that you want to perform. Set the value to **ReleaseOmsOpenAPIProject**.
        self.code = code
        # The error description (old).
        self.level = level
        # The error code (new).
        self.message = message
        # The page number, which takes effect in a pagination query.
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
        # You can call this operation to release a data synchronization project.
        self.advice = advice
        # Indicates whether the project is released.
        self.code = code
        self.cost = cost
        self.data = data
        # The suggestions (new).
        self.error_detail = error_detail
        # A system error occurred.
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        # The page number, which takes effect in a pagination query.
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
        # The total count, which takes effect in a pagination query.
        self.page_number = page_number
        # Contact the administrator.
        self.page_size = page_size
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.project_id = project_id
        # Indicates whether the call is successful.
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
        # The operation that you want to perform. Set the value to **ResetOmsOpenAPIProject**.
        self.code = code
        # The error description (old).
        self.level = level
        # The error code (new).
        self.message = message
        # The page number, which takes effect in a pagination query.
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
        # You can call this operation to reset a data synchronization project.
        self.advice = advice
        # Indicates whether the resetting is successful.
        self.code = code
        self.cost = cost
        self.data = data
        # The suggestions (new).
        self.error_detail = error_detail
        # A system error occurred.
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        # The page number, which takes effect in a pagination query.
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
        # Contact the administrator.
        self.page_number = page_number
        # Indicates whether the call is successful.
        self.page_size = page_size
        # Contact the administrator.
        self.project_id = project_id
        # The suggestions (old).
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
        # The suggestions (new).
        self.code = code
        # The operation that you want to perform. Set the value to **ResumeOmsOpenAPIProject**.
        self.level = level
        # The error description (old).
        self.message = message
        # The error code (new).
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
        # The request ID.
        self.advice = advice
        # The page number, which takes effect in a pagination query.
        self.code = code
        self.cost = cost
        self.data = data
        # The page number, which takes effect in a pagination query.
        self.error_detail = error_detail
        # The error details.
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        # Example 1
        self.request_id = request_id
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
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
        # Alibaba Cloud provides SDKs in different languages to help you quickly integrate Alibaba Cloud products and services by using APIs. We recommend that you use an SDK to call APIs. In this way, you do not need to sign for verification.
        self.begin_time = begin_time
        # It is an Alibaba Cloud asset management and configuration tool, with which you can manage multiple Alibaba Cloud products and services by using commands. It is easy to use and a good helper in migration to cloud.
        self.end_time = end_time
        # Contact the administrator.
        self.max_point_num = max_point_num
        # The business data returned.
        self.metric = metric
        # The information about the object.
        self.page_number = page_number
        # A millisecond-level timestamp.
        self.page_size = page_size
        # The value corresponding to the time.
        self.project_id = project_id
        # The name of the metric.
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
        # connector data point
        self.data_points = data_points
        self.metric = metric
        # metric tags
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
        # The information about the object.
        self.code = code
        # The error code (old).
        self.level = level
        # The ID of the project to query.
        self.message = message
        # The error description (new).
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
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.advice = advice
        # The business data returned.
        self.code = code
        # The request ID.
        self.cost = cost
        self.data = data
        # A system error occurred.
        self.error_detail = error_detail
        # The suggestions (old).
        self.message = message
        # The error code (new).
        self.page_number = page_number
        # The page number, which takes effect in a pagination query.
        self.page_size = page_size
        # The time spent in processing the request, in seconds.
        self.request_id = request_id
        # The total count, which takes effect in a pagination query.
        self.success = success
        # The error details.
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
        # The types of destination data sources.
        self.dest_db_types = dest_db_types
        # The list of labels.
        self.label_ids = label_ids
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size
        # The keyword for fuzzy search. A fuzzy search is performed based on the project ID and name.
        self.search_key = search_key
        # The types of source data sources.
        self.source_db_types = source_db_types
        # The list of project statuses.
        self.status_list = status_list
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
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
        # The types of destination data sources.
        self.dest_db_types_shrink = dest_db_types_shrink
        # The list of labels.
        self.label_ids_shrink = label_ids_shrink
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size
        # The keyword for fuzzy search. A fuzzy search is performed based on the project ID and name.
        self.search_key = search_key
        # The types of source data sources.
        self.source_db_types_shrink = source_db_types_shrink
        # The list of project statuses.
        self.status_list_shrink = status_list_shrink
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
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
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace
        # The ID of the data source.
        self.endpoint_id = endpoint_id
        # The type of the data source. Valid values: MYSQL, MARIADB, OB_MYSQL, OB_MYSQL_CE, OB_ORACLE, ORACLE, DB2_LUW, KAFKA, ROCKETMQ, DATAHUB, SYBASE, LOGPROXY, ADB, DBP_OP_ROUTE, DMS, IDB, and TIDB.
        self.endpoint_type = endpoint_type
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, and RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
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
        # The number of projects that use this label.
        self.count = count
        # The creator. This parameter value is returned only when you log on as the administrator.
        self.creator = creator
        # The ID of a label.
        self.id = id
        # The name of the label.
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
        # Indicates whether message tracing is enabled when the destination data source is RocketMQ.
        self.enable_msg_trace = enable_msg_trace
        # The ID of the data source.
        self.endpoint_id = endpoint_id
        # The type of the data source. Valid values: `MYSQL`, `MARIADB`, `OB_MYSQL`, `OB_MYSQL_CE`, `OB_ORACLE`, `ORACLE`, `DB2_LUW`, `KAFKA`, `ROCKETMQ`, `DATAHUB`, `SYBASE`, `LOGPROXY`, `ADB`, `DBP_OP_ROUTE`, `DMS`, `IDB`, and `TIDB`.
        self.endpoint_type = endpoint_type
        # The tag of the Post message when the destination data source is RocketMQ.
        self.msg_tags = msg_tags
        # The partitioned index, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ, and the partitioning mode is set to ONE.
        self.partition = partition
        # The partitioning mode, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: ONE, HASH, and TABLE.
        self.partition_mode = partition_mode
        # The producer group of the Post message when the destination data source is RocketMQ.
        self.producer_group = producer_group
        # The timeout period in seconds for a single Post message when the destination data source is RocketMQ.
        self.send_msg_timeout = send_msg_timeout
        # Indicates whether message sequencing is enabled when the destination data source is DataHub.
        self.sequence_enable = sequence_enable
        # The start time of the sequence, which must be specified if the destination data source is DataHub and message sequencing is enabled. The value is a timestamp in seconds.
        self.sequence_start_timestamp = sequence_start_timestamp
        # The text serialization type, which must be specified if the destination data source is a message queue system, such as Kafka, DataHub, or RocketMQ. Valid values: Default, DefaultExtendColumnType, Canal, Dataworks, and SharePlex.
        self.serializer_type = serializer_type
        # The type of the topic to which the Post message belongs when the destination data source is DataHub. Valid values: Tuple and Blob.
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
        # The error code.
        self.code = code
        # Valid values: CRITICAL, ERROR, and WARN.
        self.level = level
        # The error message.
        self.message = message
        # The suggestions.
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
        # The error code, such as AUTHENTICATION_ERROR, PARAM_ERROR, PARAM_ERROR_MESSAGE, NOT_IMPLEMENTED_ERROR, SHARD_COLUMNS_CONFLICT_MESSAGE, FAILED_PARSE_TOKEN_MESSAGE, CONNECT_CHECK_ERROR, NOT_SUPPORT_ERROR, CE_NOT_SUPPORT_ERROR, NOT_FOUND_ERROR, SHARDING_COLUMN_NOT_INCLUDED_ERROR, INNER_ERROR, DB_QUERY_ERROR, DATAHUB_QUERY_ERROR, USER_LACK_SYS_PRIV_ERROR, USER_LACK_TABLE_PRIV_ERROR, RM_API_ERROR, RM_TASK_ERROR, CM_API_ERROR, CM_API_NOT_SUCCESS, BAGUALU_API_ERROR, IDB_API_ERROR, SUPERVISOR_API_ERROR, OCP_API_ERROR, OCP_SERVICE_ERROR, OCP_QUERY_VERSION_FAILED, OCP_VERSION_INCORRECT_ERROR, OCP_VERSION_NOT_SUPPORTED_ERROR, OCP_API_USER_PASSWORD_INCORRECT_ERROR, OBSCHEMA_ERROR, EXECUTOR_THREAD_POOL_BUSY, NO_TABLE_SELECTED, NO_VIEW_SELECTED, SOURCE_CRAWLER_START_FAILED, SOURCE_CRAWLER_START_FAILED_DATA_EXPIRED, SOURCE_CRAWLER_START_TIMEOUT, DEST_WRITER_START_FAILED, WRITER_UNKNOWN_STATUS, DRC_TOPIC_EXISTS_ERROR, TOPIC_EMPTY_ERROR, REACH_WRITER_LIMIT_ERROR, FOUND_NO_FEASIBLE_STORE_ERROR, TOO_MANY_STORES_FOR_SUBTOPIC, TIMEOUT_EXCEPTION, KIPP_API_ERROR, KIPP_API_RESOURCE_NOT_FOUND, KIPP_API_INVALID_PARAM, KIPP_API_UNKNOWN_ERROR, KIPP_API_INTERNAL_ERROR, KIPP_API_SERVICE_UNAVAILABLE, OMS_AGENT_API_ERROR, KMS_API_ERROR, OMS_ENCRYPT_API_ERROR, OMS_DECRYPT_API_ERROR, ALIYUN_SDK_ERROR, YAOCHI_API_ERROR, RESOURCE_WITHOUT_STOCK_ERROR, RESOURCE_NO_AVAILABLE_ZONE, CM_SDK_ERROR, MIGRATION_PROJECT_STEP_PRECHECK_FAILED, PRE_CHECK_ERROR, FAILURES_CORRECT_ERROR, EXECUTE_DDL_FAILURE, EXECUTE_DDL_UNSUPPORTED_OR_FAILURE, STRUCT_RECORD_DDL_NOT_FOUND, STRUCT_RECORD_INDEX_NOT_FOUND, STRUCT_RECORD_NOT_FOUND, STRUCT_RECORD_NOT_FOUND_IN_DBCAT, SCHEMA_OBJECT_TYPE_NOT_SUPPORT_ERROR, POLAR_MYSQL_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_NETWORK_TYPE_NOT_SUPPORT_ERROR, RDS_VPC_NETWORK_NOT_SUPPORT_ERROR, DB_TYPE_NOT_SUPPORT_ERROR, SYNC_TYPE_NOT_SUPPORT_ERROR, SLAVE_OPERATION_STEP_NOT_SUPPORT_ERROR, BYTE_USED_TYPE_NOT_SUPPORT_ERROR, MANY_TO_ONE_SCHEMA_TABLE_REVERSE_INCR_NOT_SUPPORT_ERROR, DUPLICATE_SCHEMA_TABLE_ERROR, OMS_STEP_NOT_SUPPORT_ERROR, ORACLE_DATABASE_ROLE_NOT_SUPPORT_ERROR, OLD_PRE_CHECK_NOT_SUPPORT_ERROR, SCHEMA_ONE_TO_MANY_NOT_SUPPORT_ERROR, PROJECT_NOT_FOUND_ERROR, ENDPOINT_NOT_FOUND_ERROR, ENDPOINT_NAME_ALREADY_EXIST_ERROR, ENDPOINT_QUERY_ERROR, ENDPOINT_SQL_QUERY_ERROR, PROJECT_NAME_ALREADY_EXIST_ERROR, CHECKER_NOT_FOUND_ERROR, CHECKER_FAILED_ERROR, CHECKER_STATUS_UNEXPECTED_ERROR, CHECKER_NO_TASK_TYPE_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR, WORKER_INSTANCE_ALLOCATING_ERROR, LOG_SERVICE_TOPIC_NOT_FOUND_ERROR, CLUSTER_NOT_FOUND_ERROR, TENANT_NOT_FOUND_ERROR, DATABASE_NOT_FOUND_ERROR, TABLE_NOT_FOUND_ERROR, COLUMN_NOT_FOUND_ERROR, TABLE_META_NOT_FOUND_ERROR, SYBASE_CHARSET_NOT_FOUND_ERROR, OCP_NOT_FOUND_ERROR, REGION_NOT_FOUND_ERROR, OCP_ALREADY_EXIST_ERROR, ALARM_CHANNEL_NAME_ALREADY_EXIST_ERROR, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_RESPONSE, SEND_MARKDOWN_TEXT_TO_WEBHOOK_FAILED_EXCEPTION_STATUS, LABEL_ALREADY_EXIST_ERROR, LABEL_NOT_EXIST_ERROR, OCP_ALREADY_USED_ERROR, REGION_INFO_INCONSISTENT_ERROR, OCP_NAME_EMPTY_ERROR, MASTER_SLAVE_ENDPOINT_NAME_INCONSISTENT_ERROR, LOG_FILE_NOT_FOUND_ERROR, OPERATION_NOT_ALLOWED_ERROR, PROJECT_OPERATION_NOT_ALLOWED_ERROR, PROJECT_RELEASE_FAILED, STRUCT_MIGRATION_RETRY_NOT_ALLOWED_ERROR, WORKER_INSTANCE_OPERATION_NOT_ALLOWED_ERROR, USER_OPERATION_NOT_ALLOWED_ERROR, OCP_NAME_OR_REGION_NOT_ALLOWED_UPDATE, UPDATE_CONFIG_WITH_NEWLINE_NOT_ALLOWED, EXIST_UNRELEASED_PROJECT_ERROR, EXIST_UNRELEASED_TOPIC_ERROR, LABEL_CREATE_NOT_ALLOWED_ERROR, LABEL_UPDATE_NOT_ALLOWED_ERROR, LABEL_DELETE_NOT_ALLOWED_ERROR, TOPIC_NAME_INVALID_ERROR, INVALID_STATUS_ERROR, INVALID_CSV_HEAD_ERROR, INVALID_CSV_BODY_ERROR, DUPLICATE_SCHEMA_TABLE_SETTING_ERROR, PROJECT_INVALID_STATUS_ERROR, PROJECT_INVALID_CONNECTOR_COUNT_ERROR, WORKER_INSTANCE_INVALID_STATUS_ERROR, LOG_SERVICE_INVALID_STATUS_ERROR, STEP_INVALID_STATUS_ERROR, UPDATE_ALLOW_DEST_TABLE_NOT_EMPTY_NOT_ALLOWED_ERROR, EXIST_INCONSISTENCY_ERROR, OMS_SWITCH_SUBSTEP_FAILED_ERROR, ENDPOINT_ID_INVALID_ERROR, DB_QUERY_VERSION_EMPTY_ERROR, ENDPOINT_NAME_INVALID_ERROR, ENDPOINT_SCHEMA_NOT_ALLOWED_ERROR, ENDPOINT_SCHEMA_CHAR_NOT_ALLOWED_ERROR, NAME_HAS_SPACE_EXCEPTION, CONFIG_CONVERT_VALUE_ERROR, CONFIG_VALUE_EXCEEDS_LIMIT_ERROR, CONFIG_KEY_NOT_FOUND_KEY_ERROR, CONFIG_VALUE_NOT_EMPTY_ERROR, SCHEMA_HAS_CONVERT_INFO, TIME_SERIES_QUERY_SERVICE_ERROR, ETL_VERIFY_ERROR, ETL_SYNTAX_UNSUPPORTED, ETL_FIELD_NOTFOUND, ETL_FAILED_PARSE_SQL, ETL_VAL_TYPE_ERROR, NOT_SUPPORT_GENERATE_COLUMNS, NOT_SUPPORT_UPDATE_ETL, LOCK_FAILED, OMS_USER_EXIST_ERROR, OMS_USER_NOT_FOUND_ERROR, OMS_USER_NAME_LENGTH_CONSTRAINT, OMS_USER_PASSWORD_ERROR, USER_NAME_OR_PASSWORD_ERROR, OMS_USER_PASSWORD_VALIDATION_ERROR, OMS_USER_PASSWORD_DEFAULT_ERROR, OMS_USER_PERMISSION_DENIED_ERROR, OMS_USER_EDIT_ADMIN_ROLE_INFO_PERMISSION_DENIED_ERROR, OMS_USER_ILLEGAL_DELETED_ERROR, CONNECTOR_TASK_NOT_FOUND_ERROR, CONNECTOR_TASK_NUM_LIMIT_ERROR, CONNECTOR_TASK_DELETE_ERROR, METRIC_SERVICE_ERROR, SYNC_PROJECT_TYPE_INVALID_ERROR, SYNC_SHARDING_COLUMNS_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_INVALID_ERROR, SYNC_PROJECT_PRODUCER_GROUP_LIMIT_EXCEEDS_ERROR, SYNC_PROJECT_COMPLEMENT_CONFIG_ERROR, META_SCHEMA_CREATE_FAILED, RESUME_STEP_FAILED, SCHEMA_INCONSISTENCY, SCHEMA_CASCADE_MAPPING_NOT_SUPPORT_ERROR, SCHEMA_NOT_EXISTED, SCHEMA_EXISTED, SCHEMA_NOT_EXIST, BLACK_LIST_MATCH_ALL, BLACK_LIST_CONTAIN_NON_WHITE_SCHEMA, BLACK_WHITE_LIST_PARAM_INVALID_ERROR, OPERATOR_ERROR, OPERATOR_DIMENSION_NOT_SUPPORT, OPERATOR_PULL_LOG_ERROR, OPERATOR_UPDATE_CONFIG_NOT_SUPPORT, KAFKA_CREATE_TOPIC_ERROR, KAFKA_QUERY_TOPIC_ERROR, KAFKA_BUILD_PROPERTIES_ERROR, ROCKETMQ_CREATE_TOPIC_ERROR, ROCKETMQ_QUERY_TOPIC_ERROR, SYNC_OBJECT_EMPTY_ERROR, WRITER_NUMBER_NOT_UNIQUE, WRITER_NOT_ACTIVE, PROJECT_NAME_DUPLICATE_ERROR, EMPTY_FAILED_STRUCT_MIGRATION_TABLES_ERROR, LOGIC_TABLE_NOT_SUPPORT_UPDATE_OBJECT_ERROR, LOGIC_REQUEST_ERROR, LOGIC_DTO_BUILD_ERROR, UNEXPECTED_REMOTE_API_RESULT, OCEANBASE_USER_UNEXPECTED, STORE_CREATE_FAILED_ERROR, STORE_START_FAILED, STORE_NOT_PULL_LOG_ERROR, ALL_HOSTS_STATUS_ERROR, WORKER_ECS_NOT_FOUND_ERROR, WORKER_ECS_NOT_FOUND_FOR_USER_ERROR, WORKER_POD_NOT_FOUND_ERROR, WORKER_POD_NOT_FOUND_FOR_USER_ERROR, WORKER_INSTANCE_NOT_FOUND_ERROR_V2, and WORKER_INSTANCE_NOT_FOUND_FOR_USER_ERROR.
        self.error_code = error_code
        # The error details.
        self.error_details = error_details
        # The error message.
        self.error_msg = error_msg
        # The error related parameters.
        self.error_param = error_param
        # The time when the error occurred.
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
        # The estimated maximum time remained, in seconds.
        self.estimated_remaining_time_of_sec = estimated_remaining_time_of_sec
        # The estimated amount of data to migrate.
        self.estimated_total_count = estimated_total_count
        # The amount of data migrated.
        self.finished_count = finished_count
        # finishedCount / estimatedTotalCount
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
        # The estimated total number of rows.
        self.capacity = capacity
        # The checkpoint. The value is a unix timestamp in seconds.
        self.checkpoint = checkpoint
        # The full synchronization progress.
        self.connector_full_progress_overview = connector_full_progress_overview
        # The resource deployment ID.
        self.deploy_id = deploy_id
        # The read/write throughput of the destination data source, in bytes per second.
        self.dst_iops = dst_iops
        # The read/write RPS of the destination data source.
        self.dst_rps = dst_rps
        # The read/write RPS baseline of the destination data source.
        self.dst_rps_ref = dst_rps_ref
        # The read/write RT per record of the destination data source, in ms.
        self.dst_rt = dst_rt
        # The read/write RT baseline of the destination data source.
        self.dst_rt_ref = dst_rt_ref
        # The checkpoint collection time. The value is a unix timestamp in seconds.
        self.gmt = gmt
        # The amount of inconsistent data found during full verification.
        self.inconsistencies = inconsistencies
        # The checkpoint in incremental synchronization. The value is a unix timestamp in seconds.
        self.incr_timestamp_checkpoint = incr_timestamp_checkpoint
        # The ID of the current job of the step.
        self.job_id = job_id
        # The number of migrated rows.
        self.processed_records = processed_records
        # A sub-status that indicates whether this step is skipped.
        self.skipped = skipped
        # The read throughput of the source data source, in bytes per second.
        self.src_iops = src_iops
        # The read throughput baseline of the source data source.
        self.src_iops_ref = src_iops_ref
        # The read requests per second (RPS) of the source data source.
        self.src_rps = src_rps
        # The read RPS baseline of the source data source.
        self.src_rps_ref = src_rps_ref
        # The read response time (RT) per record of the source data source, in ms.
        self.src_rt = src_rt
        # The read RT baseline of the source data source.
        self.src_rt_ref = src_rt_ref
        # A sub-status that indicates whether the checker has completed full verification.
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
        # The estimated time remained.
        self.estimated_remaining_seconds = estimated_remaining_seconds
        # The additional information. The value is a JSON string.
        self.extra_info = extra_info
        # The end time, in the format of "2020-05-22T17:04:18".
        self.finish_time = finish_time
        # Indicates whether the current step must be confirmed by the user, rather than scheduled in the backend.
        self.interactive = interactive
        # The start time, in the format of "2020-05-22T17:04:18".
        self.start_time = start_time
        # The description of the step, for example, schema migration, full migration, full verification, incremental log pull, incremental synchronization, or incremental verification.
        self.step_description = step_description
        # The step details. The value is a JSON string.
        self.step_info = step_info
        # The step name. Valid values: struct_migration, full_migration, full_validation, incr_log_pull, incr_sync/incr_validation, PRE_CHECK, PREPARE, STRUCT_MIGRATION, INDEX_MIGRATION, STRUCT_SYNC, FULL_MIGRATION, APP_SWITCH, REVERSE_INCR_SYNC, FULL_VALIDATION, INCR_LOG_PULL, INCR_SYNC, INCR_VALIDATION, SYNC_PREPARE, SYNC_INCR_LOG_PULL, CONNECTOR_FULL_SYNC, or CONNECTOR_INCR_SYNC.
        self.step_name = step_name
        # The sequence of steps.
        self.step_order = step_order
        # The step progress.
        self.step_progress = step_progress
        # The step status. Valid values: INIT, RUNNING, FAILED, FINISHED, SUSPEND, and MONITORING. The value MONITORING indicates the continuous monitoring of incremental synchronization and incremental verification.
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
        # The list of distribution key columns.
        self.distributed_keys = distributed_keys
        # The lifecycle of the table.
        self.partition_life_cycle = partition_life_cycle
        # The partitioning expression.
        self.partition_statement = partition_statement
        # The list of primary key columns.
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
        # The schema of the ADB table. If the destination data source is ADB, you need to configure additional information for schema synchronization.
        self.adb_table_schema = adb_table_schema
        # The list of filter columns, which are the columns to be synchronized.
        self.filter_columns = filter_columns
        # The name of the mapped-to table or topic. If the destination data source is a database, this parameter specifies the name of the mapped-to table. If the destination data source is a message queue system, this parameter specifies the name of the mapped-to topic.
        self.mapped_name = mapped_name
        # The list of sharding key columns. This parameter applies to scenarios where the destination data source is a message queue system.
        self.shard_columns = shard_columns
        # The ID of the table. This parameter takes effect when the source data source is IDB.
        self.table_id = table_id
        # The name of the table.
        self.table_name = table_name
        # DATABASE, TABLE
        self.type = type
        # The row filter conditions.
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
        # The ID of the database. This parameter takes effect when the source data source is IDB.
        self.database_id = database_id
        # The name of the database.
        self.database_name = database_name
        # The mapped-to database. This parameter takes effect when the destination data source is a database.
        self.mapped_name = mapped_name
        # The settings for the target table objects in the current database.
        self.tables = tables
        # The mapped-to tenant. This parameter takes effect when the source data source is OceanBase Database.
        self.tenant_name = tenant_name
        # DATABASE, TABLE
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
        # The table mapping in the source data source, which is a conventional mapping scheme and takes effect only when Mode is set to NORMAL.
        self.databases = databases
        # The mapping type. Valid values: \"NORMAL\" and \"WHITE_AND_BLACK_LIST\".
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
        # The list of data types of incremental data synchronized in incremental synchronization.
        self.record_type_list = record_type_list
        # The start time for incremental synchronization. The value is a timestamp in seconds.
        self.start_timestamp = start_timestamp
        # The retention time of logs when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_log_kept_hour = store_log_kept_hour
        # Indicates whether intra-transaction sequencing is enabled when incremental synchronization is enabled and the incremental log pull component is Store.
        self.store_transaction_enabled = store_transaction_enabled
        # STRUCT, FULL, INCR
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
        # Indicates whether full migration is enabled.
        self.enable_full_sync = enable_full_sync
        # Indicates whether incremental synchronization is enabled.
        self.enable_incr_sync = enable_incr_sync
        # Indicates whether schema synchronization is enabled.
        self.enable_struct_sync = enable_struct_sync
        # The settings of incremental synchronization steps.
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
        # The business system identifier, which is optional and is a specific field of the Post message.
        self.business_name = business_name
        # The settings of the destination data source.
        self.dest_config = dest_config
        # A collection of label IDs.
        self.labels = labels
        # The project ID.
        self.project_id = project_id
        # The name of the project.
        self.project_name = project_name
        # The project owner.
        self.project_owner = project_owner
        # The settings of the source data source.
        self.source_config = source_config
        # The detailed project steps.
        self.steps = steps
        # The mappings for the synchronization objects.
        self.transfer_mapping = transfer_mapping
        # The settings of synchronization steps
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
        # The error code (new).
        self.code = code
        # The error level. Valid values: CRITICAL, ERROR, and WARN.
        self.level = level
        # The error description (new).
        self.message = message
        # The suggestions (new).
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
        # The suggestions (old).
        self.advice = advice
        # The error code (old).
        self.code = code
        # The time spent in processing the request, in seconds.
        self.cost = cost
        # The business data returned.
        self.data = data
        # The error details.
        self.error_detail = error_detail
        # The error description (old).
        self.message = message
        # The page number, which takes effect in a pagination query.
        self.page_number = page_number
        # The page size, which takes effect in a pagination query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success
        # The total count, which takes effect in a pagination query.
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
        # Contact the administrator.
        self.page_number = page_number
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
        self.page_size = page_size
        # The page number, which takes effect in a pagination query.
        self.project_id = project_id
        # The total count, which takes effect in a pagination query.
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
        # The error description (old).
        self.code = code
        # The error code (new).
        self.level = level
        # The page number, which takes effect in a pagination query.
        self.message = message
        # The error details.
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
        # The request ID.
        self.code = code
        self.cost = cost
        self.data = data
        # The operation that you want to perform. Set the value to **StartOmsOpenAPIProject**.
        self.error_detail = error_detail
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        # The suggestions (new).
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
        # The suggestions (old).
        self.page_number = page_number
        # Contact the administrator.
        self.page_size = page_size
        # The total count, which takes effect in a pagination query.
        self.project_id = project_id
        # Alibaba Cloud CLI
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
        # The time spent in processing the request, in seconds.
        self.code = code
        # The error code (old).
        self.level = level
        # The project ID.
        self.message = message
        # The error description (new).
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
        # Indicates whether the project is paused.
        self.advice = advice
        # The page size, which takes effect in a pagination query.
        self.code = code
        self.cost = cost
        self.data = data
        # A system error occurred.
        self.error_detail = error_detail
        # The page size, which takes effect in a pagination query.
        self.message = message
        # Pause a data synchronization project
        self.page_number = page_number
        self.page_size = page_size
        # A system error occurred.
        self.request_id = request_id
        # The ID of the migration instance. Generally, if you want to create a project on a public cloud, you must first purchase a migration instance.
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


class SwitchoverInstanceRequest(TeaModel):
    def __init__(
        self,
        forced: bool = None,
        instance_id: str = None,
        target_instance_id: str = None,
    ):
        self.forced = forced
        self.instance_id = instance_id
        self.target_instance_id = target_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.forced is not None:
            result['Forced'] = self.forced
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Forced') is not None:
            self.forced = m.get('Forced')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        return self


class SwitchoverInstanceResponseBodyData(TeaModel):
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


class SwitchoverInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: SwitchoverInstanceResponseBodyData = None,
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
            temp_model = SwitchoverInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchoverInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchoverInstanceResponseBody = None,
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
            temp_model = SwitchoverInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


