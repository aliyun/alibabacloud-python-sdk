# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddDatabaseRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        db_description: str = None,
        db_name: str = None,
        db_password: str = None,
        db_type: str = None,
        db_user_name: str = None,
        gateway_id: str = None,
        host: str = None,
        port: int = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.db_description = db_description
        self.db_name = db_name
        self.db_password = db_password
        self.db_type = db_type
        self.db_user_name = db_user_name
        # This parameter is required.
        self.gateway_id = gateway_id
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.port = port
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_user_name is not None:
            result['DbUserName'] = self.db_user_name
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbUserName') is not None:
            self.db_user_name = m.get('DbUserName')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddDatabaseResponseBodyDbInstance(TeaModel):
    def __init__(
        self,
        connect_host: str = None,
        connect_port: int = None,
        db_description: str = None,
        db_type: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        host: str = None,
        instance_id: str = None,
        instance_status: str = None,
        network_type: str = None,
        node_id: str = None,
        parent_id: str = None,
        port: int = None,
        region_id: str = None,
        service_type: str = None,
        user_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        # 连接使用的主机
        self.connect_host = connect_host
        self.connect_port = connect_port
        # 备注信息
        self.db_description = db_description
        # 数据库类型。
        self.db_type = db_type
        # 数据库所在网关ID。
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # 网关名称
        self.gateway_name = gateway_name
        # 通过网关所在宿主机去访问数据库的地址。
        # 
        # This parameter is required.
        self.host = host
        # 数据库实例ID
        self.instance_id = instance_id
        # 当前实例的状态
        self.instance_status = instance_status
        # 网络类型
        self.network_type = network_type
        # 节点的ID
        self.node_id = node_id
        # 归属主账号ID
        self.parent_id = parent_id
        # 通过网关所在宿主机去访问数据库的端口。
        # 
        # This parameter is required.
        self.port = port
        # 所在的地域编号
        # 
        # This parameter is required.
        self.region_id = region_id
        # 服务类型
        self.service_type = service_type
        # 用户ID
        self.user_id = user_id
        # VpcId
        self.vpc_id = vpc_id
        # VpcInstanceId
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_host is not None:
            result['ConnectHost'] = self.connect_host
        if self.connect_port is not None:
            result['ConnectPort'] = self.connect_port
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectHost') is not None:
            self.connect_host = m.get('ConnectHost')
        if m.get('ConnectPort') is not None:
            self.connect_port = m.get('ConnectPort')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class AddDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        db_instance: AddDatabaseResponseBodyDbInstance = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.db_instance = db_instance
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.db_instance:
            self.db_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.db_instance is not None:
            result['DbInstance'] = self.db_instance.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DbInstance') is not None:
            temp_model = AddDatabaseResponseBodyDbInstance()
            self.db_instance = temp_model.from_map(m['DbInstance'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDatabaseResponseBody = None,
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
            temp_model = AddDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDatabaseListRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        database_string: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.database_string = database_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.database_string is not None:
            result['DatabaseString'] = self.database_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DatabaseString') is not None:
            self.database_string = m.get('DatabaseString')
        return self


class AddDatabaseListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddDatabaseListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddDatabaseListResponseBody = None,
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
            temp_model = AddDatabaseListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDGEnabledResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckDGEnabledResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDGEnabledResponseBody = None,
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
            temp_model = CheckDGEnabledResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConnectDatabaseRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        db_password: str = None,
        db_type: str = None,
        db_user_name: str = None,
        gateway_id: str = None,
        host: str = None,
        port: int = None,
    ):
        self.db_name = db_name
        self.db_password = db_password
        self.db_type = db_type
        self.db_user_name = db_user_name
        # This parameter is required.
        self.gateway_id = gateway_id
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_user_name is not None:
            result['DbUserName'] = self.db_user_name
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbUserName') is not None:
            self.db_user_name = m.get('DbUserName')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ConnectDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConnectDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConnectDatabaseResponseBody = None,
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
            temp_model = ConnectDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_desc: str = None,
        gateway_name: str = None,
        region_id: str = None,
    ):
        self.gateway_desc = gateway_desc
        # This parameter is required.
        self.gateway_name = gateway_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_desc is not None:
            result['GatewayDesc'] = self.gateway_desc
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayDesc') is not None:
            self.gateway_desc = m.get('GatewayDesc')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayResponseBody = None,
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
            temp_model = CreateGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGatewayVerifyCodeRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
        # This parameter is required.
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        return self


class CreateGatewayVerifyCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGatewayVerifyCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGatewayVerifyCodeResponseBody = None,
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
            temp_model = CreateGatewayVerifyCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDatabaseRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # This parameter is required.
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


class DeleteDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDatabaseResponseBody = None,
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
            temp_model = DeleteDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
        # This parameter is required.
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        return self


class DeleteGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayResponseBody = None,
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
            temp_model = DeleteGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGatewayInstanceRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_instance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.gateway_id = gateway_id
        # This parameter is required.
        self.gateway_instance_id = gateway_instance_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_instance_id is not None:
            result['GatewayInstanceId'] = self.gateway_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayInstanceId') is not None:
            self.gateway_instance_id = m.get('GatewayInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteGatewayInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGatewayInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGatewayInstanceResponseBody = None,
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
            temp_model = DeleteGatewayInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_msg: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_msg = error_msg
        self.regions = regions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadGatewayProgramRequest(TeaModel):
    def __init__(
        self,
        dg_version: str = None,
        user_os: str = None,
    ):
        self.dg_version = dg_version
        self.user_os = user_os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dg_version is not None:
            result['DgVersion'] = self.dg_version
        if self.user_os is not None:
            result['UserOS'] = self.user_os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DgVersion') is not None:
            self.dg_version = m.get('DgVersion')
        if m.get('UserOS') is not None:
            self.user_os = m.get('UserOS')
        return self


class DownloadGatewayProgramResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DownloadGatewayProgramResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadGatewayProgramResponseBody = None,
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
            temp_model = DownloadGatewayProgramResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindUserGatewayByIdRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
        # This parameter is required.
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        return self


class FindUserGatewayByIdResponseBodyGateway(TeaModel):
    def __init__(
        self,
        creator_id: str = None,
        dg_version: str = None,
        exception_msg: str = None,
        gateway_desc: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        num_of_exception_instance: int = None,
        num_of_running_instance: int = None,
        region_id: str = None,
        status: str = None,
        user_id: str = None,
    ):
        self.creator_id = creator_id
        self.dg_version = dg_version
        self.exception_msg = exception_msg
        # 网关的描述
        self.gateway_desc = gateway_desc
        # 网关的编号
        self.gateway_id = gateway_id
        # 网关的名称
        # 
        # This parameter is required.
        self.gateway_name = gateway_name
        self.num_of_exception_instance = num_of_exception_instance
        self.num_of_running_instance = num_of_running_instance
        # 地域的编号
        self.region_id = region_id
        # 网关的状态
        self.status = status
        # 用户的编号
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.dg_version is not None:
            result['DgVersion'] = self.dg_version
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.gateway_desc is not None:
            result['GatewayDesc'] = self.gateway_desc
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.num_of_exception_instance is not None:
            result['NumOfExceptionInstance'] = self.num_of_exception_instance
        if self.num_of_running_instance is not None:
            result['NumOfRunningInstance'] = self.num_of_running_instance
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DgVersion') is not None:
            self.dg_version = m.get('DgVersion')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('GatewayDesc') is not None:
            self.gateway_desc = m.get('GatewayDesc')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('NumOfExceptionInstance') is not None:
            self.num_of_exception_instance = m.get('NumOfExceptionInstance')
        if m.get('NumOfRunningInstance') is not None:
            self.num_of_running_instance = m.get('NumOfRunningInstance')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class FindUserGatewayByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_msg: str = None,
        gateway: FindUserGatewayByIdResponseBodyGateway = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_msg = error_msg
        self.gateway = gateway
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.gateway:
            self.gateway.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.gateway is not None:
            result['Gateway'] = self.gateway.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Gateway') is not None:
            temp_model = FindUserGatewayByIdResponseBodyGateway()
            self.gateway = temp_model.from_map(m['Gateway'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FindUserGatewayByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindUserGatewayByIdResponseBody = None,
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
            temp_model = FindUserGatewayByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserDatabasesRequest(TeaModel):
    def __init__(
        self,
        db_type: str = None,
        gateway_id: str = None,
        host: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        port: int = None,
        region_id: str = None,
        search_key: str = None,
    ):
        self.db_type = db_type
        self.gateway_id = gateway_id
        self.host = host
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.port = port
        self.region_id = region_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetUserDatabasesResponseBodyDbInstanceListDbInstance(TeaModel):
    def __init__(
        self,
        connect_host: str = None,
        connect_port: int = None,
        db_description: str = None,
        db_type: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        gmt_create: int = None,
        host: str = None,
        instance_id: str = None,
        instance_status: str = None,
        network_type: str = None,
        node_id: str = None,
        parent_id: str = None,
        port: int = None,
        region_id: str = None,
        service_type: str = None,
        user_id: str = None,
        vpc_id: str = None,
        vpc_instance_id: str = None,
    ):
        # 连接使用的主机
        self.connect_host = connect_host
        self.connect_port = connect_port
        # 备注信息
        self.db_description = db_description
        # 数据库类型。
        self.db_type = db_type
        # 数据库所在网关ID。
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # 网关名称
        self.gateway_name = gateway_name
        # 创建时间
        self.gmt_create = gmt_create
        # 通过网关所在宿主机去访问数据库的地址。
        # 
        # This parameter is required.
        self.host = host
        # 数据库实例ID
        self.instance_id = instance_id
        # 当前实例的状态
        self.instance_status = instance_status
        # 网络类型
        self.network_type = network_type
        # 节点的ID
        self.node_id = node_id
        # 归属主账号ID
        self.parent_id = parent_id
        # 通过网关所在宿主机去访问数据库的端口。
        # 
        # This parameter is required.
        self.port = port
        # 所在的地域编号
        # 
        # This parameter is required.
        self.region_id = region_id
        # 服务类型
        self.service_type = service_type
        # 用户ID
        self.user_id = user_id
        # VpcId
        self.vpc_id = vpc_id
        # VpcInstanceId
        self.vpc_instance_id = vpc_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_host is not None:
            result['ConnectHost'] = self.connect_host
        if self.connect_port is not None:
            result['ConnectPort'] = self.connect_port
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectHost') is not None:
            self.connect_host = m.get('ConnectHost')
        if m.get('ConnectPort') is not None:
            self.connect_port = m.get('ConnectPort')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')
        return self


class GetUserDatabasesResponseBodyDbInstanceList(TeaModel):
    def __init__(
        self,
        db_instance: List[GetUserDatabasesResponseBodyDbInstanceListDbInstance] = None,
    ):
        self.db_instance = db_instance

    def validate(self):
        if self.db_instance:
            for k in self.db_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DbInstance'] = []
        if self.db_instance is not None:
            for k in self.db_instance:
                result['DbInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.db_instance = []
        if m.get('DbInstance') is not None:
            for k in m.get('DbInstance'):
                temp_model = GetUserDatabasesResponseBodyDbInstanceListDbInstance()
                self.db_instance.append(temp_model.from_map(k))
        return self


class GetUserDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        db_instance_list: GetUserDatabasesResponseBodyDbInstanceList = None,
        error_msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.count = count
        self.db_instance_list = db_instance_list
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.db_instance_list:
            self.db_instance_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.db_instance_list is not None:
            result['DbInstanceList'] = self.db_instance_list.to_map()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DbInstanceList') is not None:
            temp_model = GetUserDatabasesResponseBodyDbInstanceList()
            self.db_instance_list = temp_model.from_map(m['DbInstanceList'])
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserDatabasesResponseBody = None,
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
            temp_model = GetUserDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGatewayInstancesRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
        # This parameter is required.
        self.gateway_id = gateway_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        return self


class GetUserGatewayInstancesResponseBodyGatewayInstanceList(TeaModel):
    def __init__(
        self,
        connect_endpoint_type: str = None,
        current_daemon_version: str = None,
        current_version: str = None,
        end_point: str = None,
        gateway_id: str = None,
        gateway_instance_id: str = None,
        gateway_instance_status: str = None,
        last_update_time: int = None,
        local_ip: str = None,
        message: str = None,
        output_ip: str = None,
        region_id: str = None,
    ):
        # 连接类型
        self.connect_endpoint_type = connect_endpoint_type
        # 进程的版本号
        self.current_daemon_version = current_daemon_version
        # 版本号
        self.current_version = current_version
        # 端点地址
        self.end_point = end_point
        # 网关ID
        self.gateway_id = gateway_id
        # 代表资源一级ID的资源属性字段
        self.gateway_instance_id = gateway_instance_id
        self.gateway_instance_status = gateway_instance_status
        # 上次更新时间戳
        self.last_update_time = last_update_time
        # 本地IP地址
        self.local_ip = local_ip
        # 提示信息
        self.message = message
        # 主机
        self.output_ip = output_ip
        # 代表region的资源属性字段
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_endpoint_type is not None:
            result['ConnectEndpointType'] = self.connect_endpoint_type
        if self.current_daemon_version is not None:
            result['CurrentDaemonVersion'] = self.current_daemon_version
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_instance_id is not None:
            result['GatewayInstanceId'] = self.gateway_instance_id
        if self.gateway_instance_status is not None:
            result['GatewayInstanceStatus'] = self.gateway_instance_status
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.local_ip is not None:
            result['LocalIP'] = self.local_ip
        if self.message is not None:
            result['Message'] = self.message
        if self.output_ip is not None:
            result['OutputIP'] = self.output_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectEndpointType') is not None:
            self.connect_endpoint_type = m.get('ConnectEndpointType')
        if m.get('CurrentDaemonVersion') is not None:
            self.current_daemon_version = m.get('CurrentDaemonVersion')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayInstanceId') is not None:
            self.gateway_instance_id = m.get('GatewayInstanceId')
        if m.get('GatewayInstanceStatus') is not None:
            self.gateway_instance_status = m.get('GatewayInstanceStatus')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('LocalIP') is not None:
            self.local_ip = m.get('LocalIP')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OutputIP') is not None:
            self.output_ip = m.get('OutputIP')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetUserGatewayInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        error_msg: str = None,
        gateway_instance_list: List[GetUserGatewayInstancesResponseBodyGatewayInstanceList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_msg = error_msg
        self.gateway_instance_list = gateway_instance_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.gateway_instance_list:
            for k in self.gateway_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        result['GatewayInstanceList'] = []
        if self.gateway_instance_list is not None:
            for k in self.gateway_instance_list:
                result['GatewayInstanceList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        self.gateway_instance_list = []
        if m.get('GatewayInstanceList') is not None:
            for k in m.get('GatewayInstanceList'):
                temp_model = GetUserGatewayInstancesResponseBodyGatewayInstanceList()
                self.gateway_instance_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserGatewayInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserGatewayInstancesResponseBody = None,
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
            temp_model = GetUserGatewayInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGatewaysRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        search_key: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id
        self.search_key = search_key

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class GetUserGatewaysResponseBodyGatewayListGateway(TeaModel):
    def __init__(
        self,
        creator_id: str = None,
        dg_version: str = None,
        exception_msg: str = None,
        gateway_desc: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        num_of_exception_instance: int = None,
        num_of_running_instance: int = None,
        region_id: str = None,
        status: str = None,
        user_id: str = None,
    ):
        # 创建用户id
        self.creator_id = creator_id
        # 网关版本
        self.dg_version = dg_version
        # 网关异常信息
        self.exception_msg = exception_msg
        # 网关的描述
        self.gateway_desc = gateway_desc
        # 网关的编号
        self.gateway_id = gateway_id
        # 网关的名称
        # 
        # This parameter is required.
        self.gateway_name = gateway_name
        # 异常实例数量
        self.num_of_exception_instance = num_of_exception_instance
        # 运行中实例数量
        self.num_of_running_instance = num_of_running_instance
        # 地域的编号
        self.region_id = region_id
        # 网关的状态
        self.status = status
        # 用户的编号
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.dg_version is not None:
            result['DgVersion'] = self.dg_version
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.gateway_desc is not None:
            result['GatewayDesc'] = self.gateway_desc
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        if self.num_of_exception_instance is not None:
            result['NumOfExceptionInstance'] = self.num_of_exception_instance
        if self.num_of_running_instance is not None:
            result['NumOfRunningInstance'] = self.num_of_running_instance
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('DgVersion') is not None:
            self.dg_version = m.get('DgVersion')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('GatewayDesc') is not None:
            self.gateway_desc = m.get('GatewayDesc')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        if m.get('NumOfExceptionInstance') is not None:
            self.num_of_exception_instance = m.get('NumOfExceptionInstance')
        if m.get('NumOfRunningInstance') is not None:
            self.num_of_running_instance = m.get('NumOfRunningInstance')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserGatewaysResponseBodyGatewayList(TeaModel):
    def __init__(
        self,
        gateway: List[GetUserGatewaysResponseBodyGatewayListGateway] = None,
    ):
        self.gateway = gateway

    def validate(self):
        if self.gateway:
            for k in self.gateway:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Gateway'] = []
        if self.gateway is not None:
            for k in self.gateway:
                result['Gateway'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway = []
        if m.get('Gateway') is not None:
            for k in m.get('Gateway'):
                temp_model = GetUserGatewaysResponseBodyGatewayListGateway()
                self.gateway.append(temp_model.from_map(k))
        return self


class GetUserGatewaysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        error_msg: str = None,
        gateway_list: GetUserGatewaysResponseBodyGatewayList = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.error_msg = error_msg
        self.gateway_list = gateway_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.gateway_list:
            self.gateway_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.gateway_list is not None:
            result['GatewayList'] = self.gateway_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('GatewayList') is not None:
            temp_model = GetUserGatewaysResponseBodyGatewayList()
            self.gateway_list = temp_model.from_map(m['GatewayList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserGatewaysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserGatewaysResponseBody = None,
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
            temp_model = GetUserGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatabaseAccessPointRequest(TeaModel):
    def __init__(
        self,
        db_instance_id: str = None,
        gateway_id: str = None,
        host: str = None,
        page_number: str = None,
        page_size: str = None,
        port: int = None,
        region_id: str = None,
        search_key: str = None,
        vpc_id: str = None,
    ):
        self.db_instance_id = db_instance_id
        self.gateway_id = gateway_id
        self.host = host
        self.page_number = page_number
        self.page_size = page_size
        self.port = port
        self.region_id = region_id
        self.search_key = search_key
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.host is not None:
            result['Host'] = self.host
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListDatabaseAccessPointResponseBodyDbInstanceAccessPointList(TeaModel):
    def __init__(
        self,
        access_addr: str = None,
        access_port: int = None,
        db_instance_id: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        router_id: str = None,
        vpc_azone_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.access_addr = access_addr
        self.access_port = access_port
        self.db_instance_id = db_instance_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.router_id = router_id
        self.vpc_azone_id = vpc_azone_id
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_addr is not None:
            result['AccessAddr'] = self.access_addr
        if self.access_port is not None:
            result['AccessPort'] = self.access_port
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.router_id is not None:
            result['RouterId'] = self.router_id
        if self.vpc_azone_id is not None:
            result['VpcAzoneId'] = self.vpc_azone_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAddr') is not None:
            self.access_addr = m.get('AccessAddr')
        if m.get('AccessPort') is not None:
            self.access_port = m.get('AccessPort')
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RouterId') is not None:
            self.router_id = m.get('RouterId')
        if m.get('VpcAzoneId') is not None:
            self.vpc_azone_id = m.get('VpcAzoneId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class ListDatabaseAccessPointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        db_instance_access_point_list: List[ListDatabaseAccessPointResponseBodyDbInstanceAccessPointList] = None,
        error_msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.count = count
        self.db_instance_access_point_list = db_instance_access_point_list
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.db_instance_access_point_list:
            for k in self.db_instance_access_point_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['DbInstanceAccessPointList'] = []
        if self.db_instance_access_point_list is not None:
            for k in self.db_instance_access_point_list:
                result['DbInstanceAccessPointList'].append(k.to_map() if k else None)
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.db_instance_access_point_list = []
        if m.get('DbInstanceAccessPointList') is not None:
            for k in m.get('DbInstanceAccessPointList'):
                temp_model = ListDatabaseAccessPointResponseBodyDbInstanceAccessPointList()
                self.db_instance_access_point_list.append(temp_model.from_map(k))
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDatabaseAccessPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatabaseAccessPointResponseBody = None,
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
            temp_model = ListDatabaseAccessPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDatabaseRequest(TeaModel):
    def __init__(
        self,
        db_description: str = None,
        db_name: str = None,
        db_password: str = None,
        db_type: str = None,
        db_user_name: str = None,
        host: str = None,
        instance_id: str = None,
        port: int = None,
    ):
        self.db_description = db_description
        self.db_name = db_name
        self.db_password = db_password
        self.db_type = db_type
        self.db_user_name = db_user_name
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_user_name is not None:
            result['DbUserName'] = self.db_user_name
        if self.host is not None:
            result['Host'] = self.host
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbUserName') is not None:
            self.db_user_name = m.get('DbUserName')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class ModifyDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyDatabaseResponseBody = None,
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
            temp_model = ModifyDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_desc: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
    ):
        self.gateway_desc = gateway_desc
        # This parameter is required.
        self.gateway_id = gateway_id
        # This parameter is required.
        self.gateway_name = gateway_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_desc is not None:
            result['GatewayDesc'] = self.gateway_desc
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayDesc') is not None:
            self.gateway_desc = m.get('GatewayDesc')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')
        return self


class ModifyGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyGatewayResponseBody = None,
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
            temp_model = ModifyGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RetryDatabaseRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        db_description: str = None,
        db_name: str = None,
        db_password: str = None,
        db_type: str = None,
        db_user_name: str = None,
        gateway_id: str = None,
        host: str = None,
        port: int = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.db_description = db_description
        self.db_name = db_name
        self.db_password = db_password
        self.db_type = db_type
        self.db_user_name = db_user_name
        # This parameter is required.
        self.gateway_id = gateway_id
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.port = port
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.db_description is not None:
            result['DbDescription'] = self.db_description
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.db_password is not None:
            result['DbPassword'] = self.db_password
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.db_user_name is not None:
            result['DbUserName'] = self.db_user_name
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbDescription') is not None:
            self.db_description = m.get('DbDescription')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('DbPassword') is not None:
            self.db_password = m.get('DbPassword')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('DbUserName') is not None:
            self.db_user_name = m.get('DbUserName')
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RetryDatabaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RetryDatabaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RetryDatabaseResponseBody = None,
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
            temp_model = RetryDatabaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_instance_id: str = None,
    ):
        # This parameter is required.
        self.gateway_id = gateway_id
        self.gateway_instance_id = gateway_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.gateway_instance_id is not None:
            result['GatewayInstanceId'] = self.gateway_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('GatewayInstanceId') is not None:
            self.gateway_instance_id = m.get('GatewayInstanceId')
        return self


class StopGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
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
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopGatewayResponseBody = None,
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
            temp_model = StopGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


