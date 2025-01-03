# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AllocateInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        net_type: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The prefix of the endpoint. Set the parameter to the prefix of the value of **ConnectionString**.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The network type of the endpoint to be applied for. Set the value to Public.
        # 
        # This parameter is required.
        self.net_type = net_type
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class AllocateInstancePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        # The name of the instance.
        self.instance_name = instance_name
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AllocateInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AllocateInstancePublicConnectionResponseBody = None,
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
            temp_model = AllocateInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCreateDBInstanceRequest(TeaModel):
    def __init__(
        self,
        cache_size: int = None,
        charge_type: str = None,
        client_token: str = None,
        connection_string: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        engine: str = None,
        engine_version: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        security_iplist: str = None,
        used_time: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.cache_size = cache_size
        # This parameter is required.
        self.charge_type = charge_type
        self.client_token = client_token
        self.connection_string = connection_string
        # The specifications of the instance. Valid values:
        # 
        # *   **selectdb.xlarge**: 4 CPU cores and 32 GB of memory.
        # *   **selectdb.2xlarge**: 8 CPU cores and 64 GB of memory.
        # *   **selectdb.4xlarge**: 16 CPU cores and 128 GB of memory.
        # *   **selectdb.8xlarge**: 32 CPU cores and 256 GB of memory.
        # *   **selectdb.16xlarge**: 64 CPU cores and 512 GB of memory.
        # *   **selectdb.24xlarge**: 96 CPU cores and 768 GB of memory.
        # *   **selectdb.32xlarge**: 128 CPU cores and 1,024 GB of memory.
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        self.dbinstance_description = dbinstance_description
        # The database engine of the instance.
        self.engine = engine
        # The version of the database engine.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.period = period
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.security_iplist = security_iplist
        # The subscription duration of the instance. Valid values:
        # 
        # *   If Period is set to Year, valid values of UsedTime are 1, 2, 3, 4, and 5.
        # *   If Period is set to Month, valid values of UsedTime are 1 to 12.
        # 
        # >  This parameter takes effect and is required only if ChargeType is set to Prepaid.
        self.used_time = used_time
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckCreateDBInstanceResponseBody(TeaModel):
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


class CheckCreateDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckCreateDBInstanceResponseBody = None,
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
            temp_model = CheckCreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CheckServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        has_service_linked_role: bool = None,
        request_id: str = None,
    ):
        self.has_service_linked_role = has_service_linked_role
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_service_linked_role is not None:
            result['HasServiceLinkedRole'] = self.has_service_linked_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasServiceLinkedRole') is not None:
            self.has_service_linked_role = m.get('HasServiceLinkedRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckServiceLinkedRoleResponseBody = None,
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
            temp_model = CheckServiceLinkedRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBClusterRequest(TeaModel):
    def __init__(
        self,
        cache_size: str = None,
        charge_type: str = None,
        dbcluster_class: str = None,
        dbcluster_description: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        engine_version: str = None,
        period: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        used_time: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.cache_size = cache_size
        # This parameter is required.
        self.charge_type = charge_type
        # This parameter is required.
        self.dbcluster_class = dbcluster_class
        # This parameter is required.
        self.dbcluster_description = dbcluster_description
        # 代表资源一级ID的资源属性字段
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database engine of the instance.
        self.engine = engine
        # This parameter is required.
        self.engine_version = engine_version
        self.period = period
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.used_time = used_time
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbcluster_description is not None:
            result['DBClusterDescription'] = self.dbcluster_description
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBClusterDescription') is not None:
            self.dbcluster_description = m.get('DBClusterDescription')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        dbinstance_id: str = None,
        order_id: int = None,
    ):
        self.cluster_id = cluster_id
        self.dbinstance_id = dbinstance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateDBClusterResponseBodyData = None,
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
            temp_model = CreateDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBClusterResponseBody = None,
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
            temp_model = CreateDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBInstanceRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateDBInstanceRequest(TeaModel):
    def __init__(
        self,
        cache_size: int = None,
        charge_type: str = None,
        client_token: str = None,
        connection_string: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        engine: str = None,
        engine_version: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        security_iplist: str = None,
        tag: List[CreateDBInstanceRequestTag] = None,
        used_time: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.cache_size = cache_size
        # This parameter is required.
        self.charge_type = charge_type
        self.client_token = client_token
        self.connection_string = connection_string
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        self.dbinstance_description = dbinstance_description
        # The type of the database. Default value: **selectdb**.
        self.engine = engine
        # This parameter is required.
        self.engine_version = engine_version
        self.period = period
        # This parameter is required.
        self.region_id = region_id
        # 代表资源组的资源属性字段
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.security_iplist = security_iplist
        self.tag = tag
        self.used_time = used_time
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDBInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        cache_size: int = None,
        charge_type: str = None,
        client_token: str = None,
        connection_string: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        engine: str = None,
        engine_version: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        security_iplist: str = None,
        tag_shrink: str = None,
        used_time: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # This parameter is required.
        self.cache_size = cache_size
        # This parameter is required.
        self.charge_type = charge_type
        self.client_token = client_token
        self.connection_string = connection_string
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        self.dbinstance_description = dbinstance_description
        # The type of the database. Default value: **selectdb**.
        self.engine = engine
        # This parameter is required.
        self.engine_version = engine_version
        self.period = period
        # This parameter is required.
        self.region_id = region_id
        # 代表资源组的资源属性字段
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.security_iplist = security_iplist
        self.tag_shrink = tag_shrink
        self.used_time = used_time
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # VPC ID。
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateDBInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        order_id: int = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateDBInstanceResponseBodyData = None,
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
            temp_model = CreateDBInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDBInstanceResponseBody = None,
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
            temp_model = CreateDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateElasticRuleRequest(TeaModel):
    def __init__(
        self,
        cluster_class: str = None,
        cluster_id: str = None,
        db_instance_id: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cluster_class = cluster_class
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # This parameter is required.
        self.elastic_rule_start_time = elastic_rule_start_time
        # This parameter is required.
        self.execution_period = execution_period
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_class is not None:
            result['ClusterClass'] = self.cluster_class
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.elastic_rule_start_time is not None:
            result['ElasticRuleStartTime'] = self.elastic_rule_start_time
        if self.execution_period is not None:
            result['ExecutionPeriod'] = self.execution_period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterClass') is not None:
            self.cluster_class = m.get('ClusterClass')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ElasticRuleStartTime') is not None:
            self.elastic_rule_start_time = m.get('ElasticRuleStartTime')
        if m.get('ExecutionPeriod') is not None:
            self.execution_period = m.get('ExecutionPeriod')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateElasticRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_class: str = None,
        cluster_id: str = None,
        db_instance_id: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        rule_id: int = None,
    ):
        self.cluster_class = cluster_class
        self.cluster_id = cluster_id
        self.db_instance_id = db_instance_id
        self.elastic_rule_start_time = elastic_rule_start_time
        self.execution_period = execution_period
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_class is not None:
            result['ClusterClass'] = self.cluster_class
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.elastic_rule_start_time is not None:
            result['ElasticRuleStartTime'] = self.elastic_rule_start_time
        if self.execution_period is not None:
            result['ExecutionPeriod'] = self.execution_period
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterClass') is not None:
            self.cluster_class = m.get('ClusterClass')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ElasticRuleStartTime') is not None:
            self.elastic_rule_start_time = m.get('ElasticRuleStartTime')
        if m.get('ExecutionPeriod') is not None:
            self.execution_period = m.get('ExecutionPeriod')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateElasticRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateElasticRuleResponseBodyData = None,
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
            temp_model = CreateElasticRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateElasticRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateElasticRuleResponseBody = None,
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
            temp_model = CreateElasticRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleForSelectDBRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateServiceLinkedRoleForSelectDBResponseBody(TeaModel):
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


class CreateServiceLinkedRoleForSelectDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceLinkedRoleForSelectDBResponseBody = None,
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
            temp_model = CreateServiceLinkedRoleForSelectDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # 代表资源一级ID的资源属性字段
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id
        # 代表资源组的资源属性字段
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        order_id: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DeleteDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteDBClusterResponseBodyData = None,
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
            temp_model = DeleteDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBClusterResponseBody = None,
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
            temp_model = DeleteDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBInstanceRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteDBInstanceResponseBody(TeaModel):
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


class DeleteDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDBInstanceResponseBody = None,
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
            temp_model = DeleteDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteElasticRuleRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_instance_id: str = None,
        product: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.db_instance_id = db_instance_id
        self.product = product
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteElasticRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteElasticRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteElasticRuleResponseBody = None,
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
            temp_model = DeleteElasticRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAllDBInstanceClassRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeAllDBInstanceClassResponseBodyClassCodeList(TeaModel):
    def __init__(
        self,
        class_code: str = None,
        cpu_cores: int = None,
        default_storage_in_gb: int = None,
        max_storage_in_gb: int = None,
        memory_in_gb: int = None,
        min_storage_in_gb: int = None,
        step_storage_in_gb: int = None,
    ):
        self.class_code = class_code
        self.cpu_cores = cpu_cores
        self.default_storage_in_gb = default_storage_in_gb
        self.max_storage_in_gb = max_storage_in_gb
        # The memory size.
        self.memory_in_gb = memory_in_gb
        self.min_storage_in_gb = min_storage_in_gb
        self.step_storage_in_gb = step_storage_in_gb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_code is not None:
            result['ClassCode'] = self.class_code
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.default_storage_in_gb is not None:
            result['DefaultStorageInGB'] = self.default_storage_in_gb
        if self.max_storage_in_gb is not None:
            result['MaxStorageInGB'] = self.max_storage_in_gb
        if self.memory_in_gb is not None:
            result['MemoryInGB'] = self.memory_in_gb
        if self.min_storage_in_gb is not None:
            result['MinStorageInGB'] = self.min_storage_in_gb
        if self.step_storage_in_gb is not None:
            result['StepStorageInGB'] = self.step_storage_in_gb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('DefaultStorageInGB') is not None:
            self.default_storage_in_gb = m.get('DefaultStorageInGB')
        if m.get('MaxStorageInGB') is not None:
            self.max_storage_in_gb = m.get('MaxStorageInGB')
        if m.get('MemoryInGB') is not None:
            self.memory_in_gb = m.get('MemoryInGB')
        if m.get('MinStorageInGB') is not None:
            self.min_storage_in_gb = m.get('MinStorageInGB')
        if m.get('StepStorageInGB') is not None:
            self.step_storage_in_gb = m.get('StepStorageInGB')
        return self


class DescribeAllDBInstanceClassResponseBody(TeaModel):
    def __init__(
        self,
        class_code_list: List[DescribeAllDBInstanceClassResponseBodyClassCodeList] = None,
        request_id: str = None,
    ):
        # The instance specifications.
        self.class_code_list = class_code_list
        self.request_id = request_id

    def validate(self):
        if self.class_code_list:
            for k in self.class_code_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClassCodeList'] = []
        if self.class_code_list is not None:
            for k in self.class_code_list:
                result['ClassCodeList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.class_code_list = []
        if m.get('ClassCodeList') is not None:
            for k in m.get('ClassCodeList'):
                temp_model = DescribeAllDBInstanceClassResponseBodyClassCodeList()
                self.class_code_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAllDBInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAllDBInstanceClassResponseBody = None,
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
            temp_model = DescribeAllDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterConfigRequest(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
    ):
        # The configuration file to be modified.
        # 
        # *   For a compute cluster, set the value to be.conf.
        # *   For a frontend (FE) cluster, set the value to fe.conf.
        # 
        # This parameter is required.
        self.config_key = config_key
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDBClusterConfigResponseBodyDataParams(TeaModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        is_dynamic: int = None,
        is_user_modifiable: int = None,
        name: str = None,
        optional: str = None,
        param_category: str = None,
        value: str = None,
    ):
        # The comments on the parameter.
        self.comment = comment
        # The default value of the parameter.
        self.default_value = default_value
        # Indicates whether the parameter immediately takes effect without requiring a restart.
        self.is_dynamic = is_dynamic
        # Indicates whether the parameter is modifiable.
        self.is_user_modifiable = is_user_modifiable
        # The name of the parameter.
        self.name = name
        # The value range of the parameter.
        self.optional = optional
        # The category of the parameter.
        self.param_category = param_category
        # The current value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.is_dynamic is not None:
            result['IsDynamic'] = self.is_dynamic
        if self.is_user_modifiable is not None:
            result['IsUserModifiable'] = self.is_user_modifiable
        if self.name is not None:
            result['Name'] = self.name
        if self.optional is not None:
            result['Optional'] = self.optional
        if self.param_category is not None:
            result['ParamCategory'] = self.param_category
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('IsDynamic') is not None:
            self.is_dynamic = m.get('IsDynamic')
        if m.get('IsUserModifiable') is not None:
            self.is_user_modifiable = m.get('IsUserModifiable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Optional') is not None:
            self.optional = m.get('Optional')
        if m.get('ParamCategory') is not None:
            self.param_category = m.get('ParamCategory')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBClusterConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        db_instance_id: str = None,
        db_instance_name: str = None,
        params: List[DescribeDBClusterConfigResponseBodyDataParams] = None,
        task_id: int = None,
    ):
        # The cluster ID.
        self.db_cluster_id = db_cluster_id
        # The numeric ID of the instance.
        self.db_instance_id = db_instance_id
        # The instance ID.
        self.db_instance_name = db_instance_name
        # The details about each parameter returned.
        self.params = params
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.params:
            for k in self.params:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        result['Params'] = []
        if self.params is not None:
            for k in self.params:
                result['Params'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        self.params = []
        if m.get('Params') is not None:
            for k in m.get('Params'):
                temp_model = DescribeDBClusterConfigResponseBodyDataParams()
                self.params.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDBClusterConfigResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: DescribeDBClusterConfigResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) authentication failed.
        self.access_denied_detail = access_denied_detail
        # The information returned.
        self.data = data
        # The dynamic code. This parameter is not returned.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not returned.
        self.dynamic_message = dynamic_message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = DescribeDBClusterConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterConfigResponseBody = None,
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
            temp_model = DescribeDBClusterConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBClusterConfigChangeLogsRequest(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        end_time: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        self.config_key = config_key
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The end of the time range to query.
        # 
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDBClusterConfigChangeLogsResponseBodyDataParamChangeLogs(TeaModel):
    def __init__(
        self,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        is_applied: bool = None,
        name: str = None,
        new_value: str = None,
        old_value: str = None,
    ):
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        # The ID of the change log.
        self.id = id
        # Indicates whether the modification has taken effect.
        self.is_applied = is_applied
        # The parameter name.
        self.name = name
        self.new_value = new_value
        self.old_value = old_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.is_applied is not None:
            result['IsApplied'] = self.is_applied
        if self.name is not None:
            result['Name'] = self.name
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsApplied') is not None:
            self.is_applied = m.get('IsApplied')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        return self


class DescribeDBClusterConfigChangeLogsResponseBodyData(TeaModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        db_instance_id: str = None,
        db_instance_name: str = None,
        param_change_logs: List[DescribeDBClusterConfigChangeLogsResponseBodyDataParamChangeLogs] = None,
        task_id: int = None,
    ):
        self.db_cluster_id = db_cluster_id
        self.db_instance_id = db_instance_id
        self.db_instance_name = db_instance_name
        # The parameter change logs.
        self.param_change_logs = param_change_logs
        # The task ID.
        self.task_id = task_id

    def validate(self):
        if self.param_change_logs:
            for k in self.param_change_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        result['ParamChangeLogs'] = []
        if self.param_change_logs is not None:
            for k in self.param_change_logs:
                result['ParamChangeLogs'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        self.param_change_logs = []
        if m.get('ParamChangeLogs') is not None:
            for k in m.get('ParamChangeLogs'):
                temp_model = DescribeDBClusterConfigChangeLogsResponseBodyDataParamChangeLogs()
                self.param_change_logs.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeDBClusterConfigChangeLogsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: DescribeDBClusterConfigChangeLogsResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The returned data.
        self.data = data
        # The dynamic code. This parameter is not returned.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not returned.
        self.dynamic_message = dynamic_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = DescribeDBClusterConfigChangeLogsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBClusterConfigChangeLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBClusterConfigChangeLogsResponseBody = None,
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
            temp_model = DescribeDBClusterConfigChangeLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInstanceAttributeResponseBodyDBClusterList(TeaModel):
    def __init__(
        self,
        cache_storage_size_gb: str = None,
        cache_storage_type: str = None,
        charge_type: str = None,
        cpu_cores: int = None,
        created_time: str = None,
        db_cluster_class: str = None,
        db_cluster_id: str = None,
        db_cluster_name: str = None,
        db_instance_name: str = None,
        memory: int = None,
        modified_time: str = None,
        performance_level: str = None,
        scaling_rules_enable: bool = None,
        start_time: str = None,
        status: str = None,
    ):
        # The cache size. Unit: GB.
        self.cache_storage_size_gb = cache_storage_size_gb
        # The cache type.
        self.cache_storage_type = cache_storage_type
        # The billing method of the cluster. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.charge_type = charge_type
        # The number of CPU cores.
        self.cpu_cores = cpu_cores
        # The time when the cluster was created.
        self.created_time = created_time
        # The specifications of the cluster. Valid values:
        # 
        # *   **selectdb.xlarge**: 4 CPU cores and 32 GB of memory.
        # *   **selectdb.2xlarge**: 8 CPU cores and 64 GB of memory.
        # *   **selectdb.4xlarge**: 16 CPU cores and 128 GB of memory.
        # *   **selectdb.8xlarge**: 32 CPU cores and 256 GB of memory.
        # *   **selectdb.16xlarge**: 64 CPU cores and 512 GB of memory.
        # *   **selectdb.24xlarge**: 96 CPU cores and 768 GB of memory.
        # *   **selectdb.32xlarge**: 128 CPU cores and 1,024 GB of memory.
        self.db_cluster_class = db_cluster_class
        # The ID of the cluster.
        self.db_cluster_id = db_cluster_id
        # The name of the cluster.
        self.db_cluster_name = db_cluster_name
        # The instance name.
        self.db_instance_name = db_instance_name
        # The memory size.
        self.memory = memory
        # The modified time.
        self.modified_time = modified_time
        # The performance level.
        self.performance_level = performance_level
        self.scaling_rules_enable = scaling_rules_enable
        # The time when the cluster started.
        self.start_time = start_time
        # The state of the cluster. Valid values:
        # 
        # *   **CREATING**: The cluster is being created.
        # *   **ACTIVATION**: The cluster is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the cluster is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the cluster is being changed and the cluster is write-locked.
        # *   **DELETING**: The cluster is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_storage_size_gb is not None:
            result['CacheStorageSizeGB'] = self.cache_storage_size_gb
        if self.cache_storage_type is not None:
            result['CacheStorageType'] = self.cache_storage_type
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cpu_cores is not None:
            result['CpuCores'] = self.cpu_cores
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.db_cluster_class is not None:
            result['DbClusterClass'] = self.db_cluster_class
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.db_cluster_name is not None:
            result['DbClusterName'] = self.db_cluster_name
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.scaling_rules_enable is not None:
            result['ScalingRulesEnable'] = self.scaling_rules_enable
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheStorageSizeGB') is not None:
            self.cache_storage_size_gb = m.get('CacheStorageSizeGB')
        if m.get('CacheStorageType') is not None:
            self.cache_storage_type = m.get('CacheStorageType')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CpuCores') is not None:
            self.cpu_cores = m.get('CpuCores')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DbClusterClass') is not None:
            self.db_cluster_class = m.get('DbClusterClass')
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('DbClusterName') is not None:
            self.db_cluster_name = m.get('DbClusterName')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('ScalingRulesEnable') is not None:
            self.scaling_rules_enable = m.get('ScalingRulesEnable')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDBInstanceAttributeResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        can_upgrade_versions: List[str] = None,
        charge_type: str = None,
        create_time: str = None,
        dbcluster_list: List[DescribeDBInstanceAttributeResponseBodyDBClusterList] = None,
        dbinstance_id: str = None,
        description: str = None,
        engine: str = None,
        engine_minor_version: str = None,
        engine_version: str = None,
        expire_time: str = None,
        gmt_modified: str = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_endtime: str = None,
        maintain_starttime: str = None,
        object_store_size: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_cpu: int = None,
        resource_group_id: str = None,
        status: str = None,
        storage_size: int = None,
        sub_domain: str = None,
        tags: List[DescribeDBInstanceAttributeResponseBodyTags] = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The information returned.
        self.can_upgrade_versions = can_upgrade_versions
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.charge_type = charge_type
        # The time when the instance was created.
        self.create_time = create_time
        # The information about each cluster returned.
        self.dbcluster_list = dbcluster_list
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The description of the instance.
        self.description = description
        # The database engine of the instance.
        self.engine = engine
        # The minor kernel version number of the instance.
        self.engine_minor_version = engine_minor_version
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The time when the instance expires.
        self.expire_time = expire_time
        # The time when the instance was last modified, such as when you restarted the instance or applied for a public endpoint for the instance. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mmZ format. The time must be in UTC.
        self.gmt_modified = gmt_modified
        # The lock mode of the instance. Set the value to **lock**, which specifies that the instance is locked when it automatically expires or has an overdue payment.
        self.lock_mode = lock_mode
        # The reason why the instance is locked.
        self.lock_reason = lock_reason
        # The end time of the instance maintenance window.
        self.maintain_endtime = maintain_endtime
        # The start time of the instance maintenance window.
        self.maintain_starttime = maintain_starttime
        # The storage capacity of the instance.
        self.object_store_size = object_store_size
        # The Region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The number of CPU cores of the instance.
        self.resource_cpu = resource_cpu
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The state of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the instance is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the instance is being changed and the instance is write-locked.
        # *   **DELETING**: The instance is being deleted.
        self.status = status
        # The cache size.
        self.storage_size = storage_size
        # The subdomain zone ID.
        self.sub_domain = sub_domain
        # The tags that are added to the instances. Each tag is a key-value pair that consists of two parts: TagKey and TagValue. Format: `{"key1":"value1"}`.
        self.tags = tags
        # The VPC ID.
        self.vpc_id = vpc_id
        # The Zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.dbcluster_list:
            for k in self.dbcluster_list:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_upgrade_versions is not None:
            result['CanUpgradeVersions'] = self.can_upgrade_versions
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['DBClusterList'] = []
        if self.dbcluster_list is not None:
            for k in self.dbcluster_list:
                result['DBClusterList'].append(k.to_map() if k else None)
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_minor_version is not None:
            result['EngineMinorVersion'] = self.engine_minor_version
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_endtime is not None:
            result['MaintainEndtime'] = self.maintain_endtime
        if self.maintain_starttime is not None:
            result['MaintainStarttime'] = self.maintain_starttime
        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_cpu is not None:
            result['ResourceCpu'] = self.resource_cpu
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanUpgradeVersions') is not None:
            self.can_upgrade_versions = m.get('CanUpgradeVersions')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.dbcluster_list = []
        if m.get('DBClusterList') is not None:
            for k in m.get('DBClusterList'):
                temp_model = DescribeDBInstanceAttributeResponseBodyDBClusterList()
                self.dbcluster_list.append(temp_model.from_map(k))
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineMinorVersion') is not None:
            self.engine_minor_version = m.get('EngineMinorVersion')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndtime') is not None:
            self.maintain_endtime = m.get('MaintainEndtime')
        if m.get('MaintainStarttime') is not None:
            self.maintain_starttime = m.get('MaintainStarttime')
        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceCpu') is not None:
            self.resource_cpu = m.get('ResourceCpu')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDBInstanceAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceAttributeResponseBody = None,
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
            temp_model = DescribeDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceNetInfoRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port that is used to connect to the BE cluster.
        self.port = port
        # The protocol of the port.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_string: str = None,
        ip: str = None,
        net_type: str = None,
        port_list: List[DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList] = None,
        user_visible: bool = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
        vswitch_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The connection string of the BE cluster.
        self.connection_string = connection_string
        # The IP address of the BE cluster.
        self.ip = ip
        # The network type of the BE cluster.
        self.net_type = net_type
        self.port_list = port_list
        # Indicates whether the network information is visible to users.
        self.user_visible = user_visible
        # VPC ID
        self.vpc_id = vpc_id
        # The VPC ID.
        self.vpc_instance_id = vpc_instance_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.port_list:
            for k in self.port_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.net_type is not None:
            result['NetType'] = self.net_type
        result['PortList'] = []
        if self.port_list is not None:
            for k in self.port_list:
                result['PortList'].append(k.to_map() if k else None)
        if self.user_visible is not None:
            result['UserVisible'] = self.user_visible
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        self.port_list = []
        if m.get('PortList') is not None:
            for k in m.get('PortList'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfosPortList()
                self.port_list.append(temp_model.from_map(k))
        if m.get('UserVisible') is not None:
            self.user_visible = m.get('UserVisible')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList(TeaModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port that is used to connect to the instance.
        self.port = port
        # The protocol of the port. Valid values:
        # 
        # *   **HttpPort**: HTTP port.
        # *   **MySQLPort**: MySQL port.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        return self


class DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        connection_string: str = None,
        ip: str = None,
        net_type: str = None,
        port_list: List[DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList] = None,
        user_visible: bool = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
        vswitch_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The connection string of the instance.
        self.connection_string = connection_string
        # The IP address of the instance.
        self.ip = ip
        # The network type of the instance. Valid values:
        # 
        # *   **VPC**: indicates a virtual private cloud (VPC)-connected instance.
        # *   **PUBLIC**: indicates an Internet-connected instance.
        self.net_type = net_type
        # The ports.
        self.port_list = port_list
        # Indicates whether the network information is visible to users. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.user_visible = user_visible
        # The VPC ID.
        self.vpc_id = vpc_id
        # The ID of the VPC-connected instance.
        self.vpc_instance_id = vpc_instance_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.port_list:
            for k in self.port_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.net_type is not None:
            result['NetType'] = self.net_type
        result['PortList'] = []
        if self.port_list is not None:
            for k in self.port_list:
                result['PortList'].append(k.to_map() if k else None)
        if self.user_visible is not None:
            result['UserVisible'] = self.user_visible
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        self.port_list = []
        if m.get('PortList') is not None:
            for k in m.get('PortList'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfosPortList()
                self.port_list.append(temp_model.from_map(k))
        if m.get('UserVisible') is not None:
            self.user_visible = m.get('UserVisible')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeDBInstanceNetInfoResponseBody(TeaModel):
    def __init__(
        self,
        dbclusters_net_infos: List[DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos] = None,
        dbinstance_net_infos: List[DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos] = None,
        request_id: str = None,
    ):
        # The network information about the backend (BE) clusters.
        self.dbclusters_net_infos = dbclusters_net_infos
        # The network information about the instance.
        self.dbinstance_net_infos = dbinstance_net_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbclusters_net_infos:
            for k in self.dbclusters_net_infos:
                if k:
                    k.validate()
        if self.dbinstance_net_infos:
            for k in self.dbinstance_net_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DBClustersNetInfos'] = []
        if self.dbclusters_net_infos is not None:
            for k in self.dbclusters_net_infos:
                result['DBClustersNetInfos'].append(k.to_map() if k else None)
        result['DBInstanceNetInfos'] = []
        if self.dbinstance_net_infos is not None:
            for k in self.dbinstance_net_infos:
                result['DBInstanceNetInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbclusters_net_infos = []
        if m.get('DBClustersNetInfos') is not None:
            for k in m.get('DBClustersNetInfos'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBClustersNetInfos()
                self.dbclusters_net_infos.append(temp_model.from_map(k))
        self.dbinstance_net_infos = []
        if m.get('DBInstanceNetInfos') is not None:
            for k in m.get('DBInstanceNetInfos'):
                temp_model = DescribeDBInstanceNetInfoResponseBodyDBInstanceNetInfos()
                self.dbinstance_net_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDBInstanceNetInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstanceNetInfoResponseBody = None,
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
            temp_model = DescribeDBInstanceNetInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeDBInstancesRequest(TeaModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_ids: str = None,
        dbinstance_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        tag: List[DescribeDBInstancesRequestTag] = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID. Separate multiple instance IDs with commas (,).
        self.dbinstance_ids = dbinstance_ids
        # The state of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the instance is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the instance is being changed and the instance is write-locked.
        # *   **DELETING**: The instance is being deleted.
        self.dbinstance_status = dbinstance_status
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDBInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesShrinkRequest(TeaModel):
    def __init__(
        self,
        dbinstance_description: str = None,
        dbinstance_ids: str = None,
        dbinstance_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
        tag_shrink: str = None,
    ):
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID. Separate multiple instance IDs with commas (,).
        self.dbinstance_ids = dbinstance_ids
        # The state of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the instance is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the instance is being changed and the instance is write-locked.
        # *   **DELETING**: The instance is being deleted.
        self.dbinstance_status = dbinstance_status
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_size = page_size
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description
        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids
        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')
        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')
        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        return self


class DescribeDBInstancesResponseBodyItemsTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDBInstancesResponseBodyItems(TeaModel):
    def __init__(
        self,
        category: str = None,
        charge_type: str = None,
        cluster_count: int = None,
        dbinstance_id: str = None,
        description: str = None,
        engine: str = None,
        engine_version: str = None,
        expire_time: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instance_used_type: str = None,
        is_deleted: bool = None,
        lock_mode: int = None,
        lock_reason: str = None,
        maintain_end_time_str: str = None,
        maintain_endtime: str = None,
        maintain_start_time_str: str = None,
        maintain_starttime: str = None,
        object_store_size: int = None,
        parent_instance: str = None,
        region_id: str = None,
        resource_cpu: int = None,
        resource_group_id: str = None,
        resource_memory: int = None,
        scale_max: int = None,
        scale_min: int = None,
        scale_replica: int = None,
        status: str = None,
        storage_size: int = None,
        storage_type: str = None,
        tags: List[DescribeDBInstancesResponseBodyItemsTags] = None,
        tenant_cluster_id: str = None,
        tenant_token: str = None,
        tenant_user_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
        connection_string: str = None,
    ):
        # The edition of the instance. Default value: basic.
        self.category = category
        # The billing method of the instance. Valid values:
        # 
        # *   **Postpaid**: pay-as-you-go.
        # *   **Prepaid**: subscription.
        self.charge_type = charge_type
        # The total number of clusters.
        self.cluster_count = cluster_count
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The description of the instance.
        self.description = description
        # The database engine of the instance.
        self.engine = engine
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The time when the cluster expires.
        # 
        # >  A specific value is returned only for subscription clusters whose billing method is **Prepaid**. For pay-as-you-go clusters whose billing method is **Postpaid**, no value is returned.
        self.expire_time = expire_time
        # The time when the task was created. The time is displayed in UTC.
        self.gmt_created = gmt_created
        # The time when the task was last modified. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The type of the instance.
        self.instance_used_type = instance_used_type
        # Indicates whether the instance is deleted. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_deleted = is_deleted
        # The lock mode of the instance.
        self.lock_mode = lock_mode
        # The reason why the instance is locked.
        self.lock_reason = lock_reason
        # The end timestamp of the maintenance window.
        self.maintain_end_time_str = maintain_end_time_str
        # The end time of the instance maintenance window.
        self.maintain_endtime = maintain_endtime
        # The start timestamp of the maintenance window.
        self.maintain_start_time_str = maintain_start_time_str
        # The start time of the instance maintenance window.
        self.maintain_starttime = maintain_starttime
        # The storage capacity of the instance. Unit: GB.
        self.object_store_size = object_store_size
        # The time when the instance was created.
        self.parent_instance = parent_instance
        # The region ID.
        self.region_id = region_id
        # The number of CPU cores of the instance.
        self.resource_cpu = resource_cpu
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The memory capacity of the instance.
        self.resource_memory = resource_memory
        # The maximum number of RCUs.
        self.scale_max = scale_max
        # The minimum number of RDS capacity units (RCUs).
        self.scale_min = scale_min
        # This parameter is not returned.
        self.scale_replica = scale_replica
        # The state of the instance. Valid values:
        # 
        # *   **CREATING**: The instance is being created.
        # *   **ACTIVATION**: The instance is running.
        # *   **RESOURCE_CHANGING**: The resource configuration of the instance is being changed.
        # *   **ORDER_PREPARING**: The order is being confirmed.
        # *   **READONLY_RESOURCE_CHANGING**: The resource configuration of the instance is being changed and the instance is write-locked.
        # *   **DELETING**: The instance is being deleted.
        self.status = status
        # The cache size.
        self.storage_size = storage_size
        # The storage type of the instance.
        self.storage_type = storage_type
        # The details about each tag returned.
        self.tags = tags
        # The ID of the cluster that is monitored by Managed Service for Prometheus.
        self.tenant_cluster_id = tenant_cluster_id
        # The token that is used to access Managed Service for Prometheus.
        self.tenant_token = tenant_token
        # The ID of the account that uses Managed Service for Prometheus.
        self.tenant_user_id = tenant_user_id
        # The virtual private cloud (VPC) ID.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id
        # The connection string of the instance.
        self.connection_string = connection_string

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_used_type is not None:
            result['InstanceUsedType'] = self.instance_used_type
        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.maintain_end_time_str is not None:
            result['MaintainEndTimeStr'] = self.maintain_end_time_str
        if self.maintain_endtime is not None:
            result['MaintainEndtime'] = self.maintain_endtime
        if self.maintain_start_time_str is not None:
            result['MaintainStartTimeStr'] = self.maintain_start_time_str
        if self.maintain_starttime is not None:
            result['MaintainStarttime'] = self.maintain_starttime
        if self.object_store_size is not None:
            result['ObjectStoreSize'] = self.object_store_size
        if self.parent_instance is not None:
            result['ParentInstance'] = self.parent_instance
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_cpu is not None:
            result['ResourceCpu'] = self.resource_cpu
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_memory is not None:
            result['ResourceMemory'] = self.resource_memory
        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max
        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min
        if self.scale_replica is not None:
            result['ScaleReplica'] = self.scale_replica
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_cluster_id is not None:
            result['TenantClusterId'] = self.tenant_cluster_id
        if self.tenant_token is not None:
            result['TenantToken'] = self.tenant_token
        if self.tenant_user_id is not None:
            result['TenantUserId'] = self.tenant_user_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.connection_string is not None:
            result['connectionString'] = self.connection_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceUsedType') is not None:
            self.instance_used_type = m.get('InstanceUsedType')
        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('MaintainEndTimeStr') is not None:
            self.maintain_end_time_str = m.get('MaintainEndTimeStr')
        if m.get('MaintainEndtime') is not None:
            self.maintain_endtime = m.get('MaintainEndtime')
        if m.get('MaintainStartTimeStr') is not None:
            self.maintain_start_time_str = m.get('MaintainStartTimeStr')
        if m.get('MaintainStarttime') is not None:
            self.maintain_starttime = m.get('MaintainStarttime')
        if m.get('ObjectStoreSize') is not None:
            self.object_store_size = m.get('ObjectStoreSize')
        if m.get('ParentInstance') is not None:
            self.parent_instance = m.get('ParentInstance')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceCpu') is not None:
            self.resource_cpu = m.get('ResourceCpu')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceMemory') is not None:
            self.resource_memory = m.get('ResourceMemory')
        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')
        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')
        if m.get('ScaleReplica') is not None:
            self.scale_replica = m.get('ScaleReplica')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDBInstancesResponseBodyItemsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantClusterId') is not None:
            self.tenant_cluster_id = m.get('TenantClusterId')
        if m.get('TenantToken') is not None:
            self.tenant_token = m.get('TenantToken')
        if m.get('TenantUserId') is not None:
            self.tenant_user_id = m.get('TenantUserId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('connectionString') is not None:
            self.connection_string = m.get('connectionString')
        return self


class DescribeDBInstancesResponseBody(TeaModel):
    def __init__(
        self,
        items: List[DescribeDBInstancesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The details about each instance returned.
        self.items = items
        # The number of entries per page. Valid values:
        # 
        # *   **30** (default)
        # *   **50**\
        # *   **100**\
        self.page_number = page_number
        # The page number.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeDBInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeDBInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDBInstancesResponseBody = None,
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
            temp_model = DescribeDBInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeElasticRulesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_instance_id: str = None,
        product: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.db_instance_id = db_instance_id
        self.product = product
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeElasticRulesResponseBodyDataRules(TeaModel):
    def __init__(
        self,
        cluster_class: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        rule_id: int = None,
    ):
        self.cluster_class = cluster_class
        self.elastic_rule_start_time = elastic_rule_start_time
        self.execution_period = execution_period
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_class is not None:
            result['ClusterClass'] = self.cluster_class
        if self.elastic_rule_start_time is not None:
            result['ElasticRuleStartTime'] = self.elastic_rule_start_time
        if self.execution_period is not None:
            result['ExecutionPeriod'] = self.execution_period
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterClass') is not None:
            self.cluster_class = m.get('ClusterClass')
        if m.get('ElasticRuleStartTime') is not None:
            self.elastic_rule_start_time = m.get('ElasticRuleStartTime')
        if m.get('ExecutionPeriod') is not None:
            self.execution_period = m.get('ExecutionPeriod')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DescribeElasticRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_instance_id: str = None,
        rules: List[DescribeElasticRulesResponseBodyDataRules] = None,
    ):
        self.cluster_id = cluster_id
        self.db_instance_id = db_instance_id
        self.rules = rules

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeElasticRulesResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeElasticRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: DescribeElasticRulesResponseBodyData = None,
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
            temp_model = DescribeElasticRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeElasticRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeElasticRulesResponseBody = None,
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
            temp_model = DescribeElasticRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityIPListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSecurityIPListResponseBodyGroupItems(TeaModel):
    def __init__(
        self,
        aecurity_iptype: str = None,
        group_name: str = None,
        group_tag: str = None,
        security_iplist: str = None,
        whitelist_net_type: str = None,
    ):
        # The IP address type. Valid values:
        # 
        # *   ipv4
        # *   ipv6 (not supported)
        self.aecurity_iptype = aecurity_iptype
        # The name of the whitelist.
        self.group_name = group_name
        # The tag of the whitelist.
        self.group_tag = group_tag
        # The IP addresses in the whitelist. Multiple IP addresses are separated by commas (,).
        self.security_iplist = security_iplist
        # The network type of the whitelist.
        self.whitelist_net_type = whitelist_net_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aecurity_iptype is not None:
            result['AecurityIPType'] = self.aecurity_iptype
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AecurityIPType') is not None:
            self.aecurity_iptype = m.get('AecurityIPType')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')
        return self


class DescribeSecurityIPListResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_items: List[DescribeSecurityIPListResponseBodyGroupItems] = None,
        request_id: str = None,
    ):
        # The instance ID.
        self.dbinstance_name = dbinstance_name
        # The details about each IP address whitelist returned.
        self.group_items = group_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.group_items:
            for k in self.group_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        result['GroupItems'] = []
        if self.group_items is not None:
            for k in self.group_items:
                result['GroupItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        self.group_items = []
        if m.get('GroupItems') is not None:
            for k in m.get('GroupItems'):
                temp_model = DescribeSecurityIPListResponseBodyGroupItems()
                self.group_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSecurityIPListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSecurityIPListResponseBody = None,
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
            temp_model = DescribeSecurityIPListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnDisableScalingRulesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_instance_id: str = None,
        product: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        scaling_rules_enable: bool = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.db_instance_id = db_instance_id
        self.product = product
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.scaling_rules_enable = scaling_rules_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scaling_rules_enable is not None:
            result['ScalingRulesEnable'] = self.scaling_rules_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ScalingRulesEnable') is not None:
            self.scaling_rules_enable = m.get('ScalingRulesEnable')
        return self


class EnDisableScalingRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_instance_id: str = None,
        scaling_rules_enable: bool = None,
    ):
        self.cluster_id = cluster_id
        self.db_instance_id = db_instance_id
        self.scaling_rules_enable = scaling_rules_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.scaling_rules_enable is not None:
            result['ScalingRulesEnable'] = self.scaling_rules_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ScalingRulesEnable') is not None:
            self.scaling_rules_enable = m.get('ScalingRulesEnable')
        return self


class EnDisableScalingRulesResponseBody(TeaModel):
    def __init__(
        self,
        data: EnDisableScalingRulesResponseBodyData = None,
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
            temp_model = EnDisableScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnDisableScalingRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnDisableScalingRulesResponseBody = None,
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
            temp_model = EnDisableScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCreateBEClusterInquiryRequest(TeaModel):
    def __init__(
        self,
        cache_size: int = None,
        charge_type: str = None,
        commodity_code: str = None,
        compute_size: int = None,
        db_instance_id: str = None,
        pre_cache_size: int = None,
        pre_compute_size: int = None,
        pricing_cycle: str = None,
        quantity: int = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The size of the elastic cache.
        self.cache_size = cache_size
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The commodity code.
        # 
        # Valid values:
        # 
        # *   selectdb_pre_public_intl: subscription commodity on the international site (alibabacloud.com)
        # *   selectdb_go_public_cn: pay-as-you-go commodity on the China site (aliyun.com)
        # *   selectdb_go_public_intl: pay-as-you-go commodity on the international site (alibabacloud.com)
        # *   selectdb_pre_public_cn: subscription commodity on the China site (aliyun.com).
        self.commodity_code = commodity_code
        # The number of elastic CPU cores.
        self.compute_size = compute_size
        # The instance ID.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # The size of the reserved cache.
        self.pre_cache_size = pre_cache_size
        # The number of reserved CPU cores.
        self.pre_compute_size = pre_compute_size
        # The billing cycle.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Minute
        # *   Hour
        # *   Day
        # 
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # The number of clusters to be created.
        # 
        # This parameter is required.
        self.quantity = quantity
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_size is not None:
            result['ComputeSize'] = self.compute_size
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.pre_cache_size is not None:
            result['PreCacheSize'] = self.pre_cache_size
        if self.pre_compute_size is not None:
            result['PreComputeSize'] = self.pre_compute_size
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeSize') is not None:
            self.compute_size = m.get('ComputeSize')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('PreCacheSize') is not None:
            self.pre_cache_size = m.get('PreCacheSize')
        if m.get('PreComputeSize') is not None:
            self.pre_compute_size = m.get('PreComputeSize')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetCreateBEClusterInquiryResponseBodyData(TeaModel):
    def __init__(
        self,
        currency: str = None,
        trade_amount: str = None,
    ):
        # The currency.
        self.currency = currency
        # The amount of money.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class GetCreateBEClusterInquiryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetCreateBEClusterInquiryResponseBodyData = None,
        request_id: str = None,
    ):
        # The information returned.
        self.data = data
        # The request ID.
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
            temp_model = GetCreateBEClusterInquiryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCreateBEClusterInquiryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCreateBEClusterInquiryResponseBody = None,
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
            temp_model = GetCreateBEClusterInquiryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModifyBEClusterInquiryRequest(TeaModel):
    def __init__(
        self,
        cache_size: int = None,
        charge_type: str = None,
        cluster_id: str = None,
        commodity_code: str = None,
        compute_size: int = None,
        db_instance_id: str = None,
        pre_cache_size: int = None,
        pre_compute_size: int = None,
        pricing_cycle: str = None,
        quantity: int = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The size of the elastic cache.
        self.cache_size = cache_size
        # The billing method.
        # 
        # Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The cluster ID.
        self.cluster_id = cluster_id
        # The commodity code.
        # 
        # Valid values:
        # 
        # *   selectdb_pre_public_intl: subscription commodity on the international site (alibabacloud.com)
        # *   selectdb_go_public_cn: pay-as-you-go commodity on the China site (aliyun.com)
        # *   selectdb_go_public_intl: pay-as-you-go commodity on the international site (alibabacloud.com)
        # *   selectdb_pre_public_cn: subscription commodity on the China site (aliyun.com).
        # 
        # This parameter is required.
        self.commodity_code = commodity_code
        # The number of elastic CPU cores.
        self.compute_size = compute_size
        # The instance ID.
        # 
        # This parameter is required.
        self.db_instance_id = db_instance_id
        # The size of the reserved cache.
        self.pre_cache_size = pre_cache_size
        # The number of reserved CPU cores.
        self.pre_compute_size = pre_compute_size
        # The billing cycle.
        # 
        # Valid values:
        # 
        # *   Month
        # *   Year
        # *   Minute
        # *   Hour
        # *   Day
        # 
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # The number of clusters whose specifications are to be changed.
        # 
        # This parameter is required.
        self.quantity = quantity
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.compute_size is not None:
            result['ComputeSize'] = self.compute_size
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.pre_cache_size is not None:
            result['PreCacheSize'] = self.pre_cache_size
        if self.pre_compute_size is not None:
            result['PreComputeSize'] = self.pre_compute_size
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ComputeSize') is not None:
            self.compute_size = m.get('ComputeSize')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('PreCacheSize') is not None:
            self.pre_cache_size = m.get('PreCacheSize')
        if m.get('PreComputeSize') is not None:
            self.pre_compute_size = m.get('PreComputeSize')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetModifyBEClusterInquiryResponseBodyData(TeaModel):
    def __init__(
        self,
        currency: str = None,
        trade_amount: str = None,
    ):
        # The currency.
        self.currency = currency
        # The amount of money.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class GetModifyBEClusterInquiryResponseBody(TeaModel):
    def __init__(
        self,
        data: GetModifyBEClusterInquiryResponseBodyData = None,
        request_id: str = None,
    ):
        # The information returned.
        self.data = data
        # The request ID.
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
            temp_model = GetModifyBEClusterInquiryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetModifyBEClusterInquiryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModifyBEClusterInquiryResponseBody = None,
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
            temp_model = GetModifyBEClusterInquiryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBEClusterAttributeRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        instance_attribute_type: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        value: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The attribute type of the instance. Set this parameter to DBInstanceDescription.
        # 
        # This parameter is required.
        self.instance_attribute_type = instance_attribute_type
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The new name of the cluster.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_attribute_type is not None:
            result['InstanceAttributeType'] = self.instance_attribute_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceAttributeType') is not None:
            self.instance_attribute_type = m.get('InstanceAttributeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyBEClusterAttributeResponseBody(TeaModel):
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


class ModifyBEClusterAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyBEClusterAttributeResponseBody = None,
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
            temp_model = ModifyBEClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterRequest(TeaModel):
    def __init__(
        self,
        cache_size: str = None,
        dbcluster_class: str = None,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        engine: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The size of the reserved cache.
        self.cache_size = cache_size
        # This parameter is required.
        self.dbcluster_class = dbcluster_class
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database engine of the instance. Set the value to selectdb.
        self.engine = engine
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size
        if self.dbcluster_class is not None:
            result['DBClusterClass'] = self.dbcluster_class
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')
        if m.get('DBClusterClass') is not None:
            self.dbcluster_class = m.get('DBClusterClass')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ModifyDBClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        order_id: int = None,
    ):
        self.dbcluster_id = dbcluster_id
        self.dbinstance_id = dbinstance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        data: ModifyDBClusterResponseBodyData = None,
        request_id: str = None,
    ):
        # 代表资源一级ID的资源属性字段
        self.dbinstance_id = dbinstance_id
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Data') is not None:
            temp_model = ModifyDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterResponseBody = None,
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
            temp_model = ModifyDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBClusterConfigRequest(TeaModel):
    def __init__(
        self,
        config_key: str = None,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        parameters: str = None,
        region_id: str = None,
        switch_time_mode: str = None,
    ):
        # This parameter is required.
        self.config_key = config_key
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.parameters = parameters
        self.region_id = region_id
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_key is not None:
            result['ConfigKey'] = self.config_key
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class ModifyDBClusterConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        db_cluster_id: str = None,
        db_instance_id: str = None,
        db_instance_name: str = None,
        task_id: int = None,
    ):
        self.db_cluster_id = db_cluster_id
        self.db_instance_id = db_instance_id
        self.db_instance_name = db_instance_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_cluster_id is not None:
            result['DbClusterId'] = self.db_cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbClusterId') is not None:
            self.db_cluster_id = m.get('DbClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifyDBClusterConfigResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: ModifyDBClusterConfigResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        # The dynamic code. This parameter is not returned.
        self.dynamic_code = dynamic_code
        # The dynamic message. This parameter is not returned.
        self.dynamic_message = dynamic_message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Data') is not None:
            temp_model = ModifyDBClusterConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyDBClusterConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBClusterConfigResponseBody = None,
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
            temp_model = ModifyDBClusterConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        instance_attribute_type: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        value: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The instance parameter to be modified. Valid values:
        # 
        # *   **MaintainTime**: Modify the maintenance window of the instance in the hh:mm-hh:mm format.
        # *   **DBInstanceDescription**: Modify the description of the instance.
        # 
        # This parameter is required.
        self.instance_attribute_type = instance_attribute_type
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The new value of the instance parameter to be modified. Examples:
        # 
        # *   If InstanceAttributeType is set to MaintainTime, you can set Value to 00:00-06:00.
        # *   If InstanceAttributeType is set to DBInstanceDescription, you can set Value to testdb.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.instance_attribute_type is not None:
            result['InstanceAttributeType'] = self.instance_attribute_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('InstanceAttributeType') is not None:
            self.instance_attribute_type = m.get('InstanceAttributeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyDBInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ModifyDBInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDBInstanceAttributeResponseBody = None,
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
            temp_model = ModifyDBInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyElasticRuleRequest(TeaModel):
    def __init__(
        self,
        cluster_class: str = None,
        cluster_id: str = None,
        db_instance_id: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        product: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        rule_id: int = None,
    ):
        self.cluster_class = cluster_class
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.db_instance_id = db_instance_id
        self.elastic_rule_start_time = elastic_rule_start_time
        self.execution_period = execution_period
        self.product = product
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_class is not None:
            result['ClusterClass'] = self.cluster_class
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.elastic_rule_start_time is not None:
            result['ElasticRuleStartTime'] = self.elastic_rule_start_time
        if self.execution_period is not None:
            result['ExecutionPeriod'] = self.execution_period
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterClass') is not None:
            self.cluster_class = m.get('ClusterClass')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ElasticRuleStartTime') is not None:
            self.elastic_rule_start_time = m.get('ElasticRuleStartTime')
        if m.get('ExecutionPeriod') is not None:
            self.execution_period = m.get('ExecutionPeriod')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ModifyElasticRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_class: str = None,
        cluster_id: str = None,
        db_instance_id: str = None,
        elastic_rule_start_time: str = None,
        execution_period: str = None,
        rule_id: int = None,
    ):
        self.cluster_class = cluster_class
        self.cluster_id = cluster_id
        self.db_instance_id = db_instance_id
        self.elastic_rule_start_time = elastic_rule_start_time
        self.execution_period = execution_period
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_class is not None:
            result['ClusterClass'] = self.cluster_class
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.elastic_rule_start_time is not None:
            result['ElasticRuleStartTime'] = self.elastic_rule_start_time
        if self.execution_period is not None:
            result['ExecutionPeriod'] = self.execution_period
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterClass') is not None:
            self.cluster_class = m.get('ClusterClass')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('ElasticRuleStartTime') is not None:
            self.elastic_rule_start_time = m.get('ElasticRuleStartTime')
        if m.get('ExecutionPeriod') is not None:
            self.execution_period = m.get('ExecutionPeriod')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ModifyElasticRuleResponseBody(TeaModel):
    def __init__(
        self,
        data: ModifyElasticRuleResponseBodyData = None,
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
            temp_model = ModifyElasticRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyElasticRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyElasticRuleResponseBody = None,
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
            temp_model = ModifyElasticRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityIPListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        group_name: str = None,
        modify_mode: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        security_iplist: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the whitelist. Default value: **Default**.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The mode in which you want to modify the whitelist. Valid values:
        # 
        # *   **0**: overwrites the IP addresses in the whitelist.
        # *   **1**: adds IP addresses to the whitelist.
        # *   **2**: removes IP addresses from the whitelist.
        # 
        # This parameter is required.
        self.modify_mode = modify_mode
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The IP addresses in the whitelist of the instance. Separate multiple IP addresses with commas (,).
        # 
        # This parameter is required.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        return self


class ModifySecurityIPListResponseBody(TeaModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_name: str = None,
        group_tag: str = None,
        request_id: str = None,
        security_iplist: str = None,
        security_iptype: str = None,
        task_id: int = None,
        whitelist_net_type: str = None,
    ):
        # The name of the instance.
        self.dbinstance_name = dbinstance_name
        # The name of the whitelist.
        self.group_name = group_name
        # The tag of the whitelist.
        self.group_tag = group_tag
        # The request ID.
        self.request_id = request_id
        # The IP addresses in the whitelist of the instance. Multiple IP addresses are separated by commas (,).
        self.security_iplist = security_iplist
        # The IP address type.
        self.security_iptype = security_iptype
        # The task ID.
        self.task_id = task_id
        # The network type of the whitelist.
        self.whitelist_net_type = whitelist_net_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_tag is not None:
            result['GroupTag'] = self.group_tag
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.whitelist_net_type is not None:
            result['WhitelistNetType'] = self.whitelist_net_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupTag') is not None:
            self.group_tag = m.get('GroupTag')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WhitelistNetType') is not None:
            self.whitelist_net_type = m.get('WhitelistNetType')
        return self


class ModifySecurityIPListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySecurityIPListResponseBody = None,
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
            temp_model = ModifySecurityIPListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstancePublicConnectionRequest(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The connection string of the instance.
        # 
        # This parameter is required.
        self.connection_string = connection_string
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ReleaseInstancePublicConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ReleaseInstancePublicConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstancePublicConnectionResponseBody = None,
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
            temp_model = ReleaseInstancePublicConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # The database account of the instance.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the database account. Requirements:
        # 
        # *   The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # *   The following special characters can be used: ! @ # $ % ^ & \\* ( ) _ + - =\
        # *   The password must be 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ResetAccountPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ResetAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ResetAccountPasswordResponseBody = None,
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
            temp_model = ResetAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartDBClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_id: int = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The ID of the region in which the ApsaraDB for SelectDB instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RestartDBClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The instance ID.
        self.dbinstance_id = dbinstance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        return self


class RestartDBClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: RestartDBClusterResponseBodyData = None,
        request_id: str = None,
    ):
        # The information returned.
        self.data = data
        # The request ID.
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
            temp_model = RestartDBClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartDBClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartDBClusterResponseBody = None,
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
            temp_model = RestartDBClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartBEClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class StartBEClusterResponseBody(TeaModel):
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


class StartBEClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartBEClusterResponseBody = None,
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
            temp_model = StartBEClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopBEClusterRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbinstance_id: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class StopBEClusterResponseBody(TeaModel):
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


class StopBEClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopBEClusterResponseBody = None,
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
            temp_model = StopBEClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeDBInstanceEngineVersionRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        engine_version: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        switch_time_mode: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database engine version of the instance.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The update mode. If you do not specify this parameter, the system immediately updates the database engine version. If you set this parameter to 1, the system updates the database engine version during the maintenance window.
        self.switch_time_mode = switch_time_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.switch_time_mode is not None:
            result['SwitchTimeMode'] = self.switch_time_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SwitchTimeMode') is not None:
            self.switch_time_mode = m.get('SwitchTimeMode')
        return self


class UpgradeDBInstanceEngineVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpgradeDBInstanceEngineVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeDBInstanceEngineVersionResponseBody = None,
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
            temp_model = UpgradeDBInstanceEngineVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


