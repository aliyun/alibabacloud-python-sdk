# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DescribeDBInstanceForDmsRequest(TeaModel):
    def __init__(
        self,
        host: str = None,
        port: int = None,
    ):
        self.host = host
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeDBInstanceForDmsResponseBodyInstance(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        ali_uid: str = None,
        port: str = None,
        bid: str = None,
        vpc_cloud_instance_id: str = None,
        v_switch_id: str = None,
        description: str = None,
        db_type: str = None,
        version: str = None,
        connection_string: str = None,
        region: str = None,
        instance_network_type: str = None,
        db_instance_name: str = None,
        vpc_ip: str = None,
    ):
        self.vpc_id = vpc_id
        self.ali_uid = ali_uid
        self.port = port
        self.bid = bid
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        self.v_switch_id = v_switch_id
        self.description = description
        self.db_type = db_type
        self.version = version
        self.connection_string = connection_string
        self.region = region
        self.instance_network_type = instance_network_type
        self.db_instance_name = db_instance_name
        self.vpc_ip = vpc_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.port is not None:
            result['Port'] = self.port
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.description is not None:
            result['Description'] = self.description
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.version is not None:
            result['Version'] = self.version
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.vpc_ip is not None:
            result['VpcIp'] = self.vpc_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('VpcIp') is not None:
            self.vpc_ip = m.get('VpcIp')
        return self


class DescribeDBInstanceForDmsResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        count: int = None,
        instance: DescribeDBInstanceForDmsResponseBodyInstance = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.count = count
        self.instance = instance

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.count is not None:
            result['Count'] = self.count
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Instance') is not None:
            temp_model = DescribeDBInstanceForDmsResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        return self


class DescribeDBInstanceForDmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceForDmsResponseBody = None,
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
            temp_model = DescribeDBInstanceForDmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceSecurityIpsRequest(TeaModel):
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


class DescribeDBInstanceSecurityIpsResponseBodyResult(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        white_list: List[str] = None,
    ):
        self.group_name = group_name
        self.white_list = white_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class DescribeDBInstanceSecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        count: int = None,
        result: List[DescribeDBInstanceSecurityIpsResponseBodyResult] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.count = count
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.count is not None:
            result['Count'] = self.count
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = DescribeDBInstanceSecurityIpsResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class DescribeDBInstanceSecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceSecurityIpsResponseBody = None,
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
            temp_model = DescribeDBInstanceSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstancesForDmsRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
    ):
        self.ali_uid = ali_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        return self


class DescribeDBInstancesForDmsResponseBodyInstances(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        ali_uid: str = None,
        port: str = None,
        bid: str = None,
        vpc_cloud_instance_id: str = None,
        v_switch_id: str = None,
        description: str = None,
        db_type: str = None,
        version: str = None,
        connection_string: str = None,
        region: str = None,
        instance_network_type: str = None,
        db_instance_name: str = None,
        vpc_ip: str = None,
    ):
        self.vpc_id = vpc_id
        self.ali_uid = ali_uid
        self.port = port
        self.bid = bid
        self.vpc_cloud_instance_id = vpc_cloud_instance_id
        self.v_switch_id = v_switch_id
        self.description = description
        self.db_type = db_type
        self.version = version
        self.connection_string = connection_string
        self.region = region
        self.instance_network_type = instance_network_type
        self.db_instance_name = db_instance_name
        self.vpc_ip = vpc_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.port is not None:
            result['Port'] = self.port
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.vpc_cloud_instance_id is not None:
            result['VpcCloudInstanceId'] = self.vpc_cloud_instance_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.description is not None:
            result['Description'] = self.description
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.version is not None:
            result['Version'] = self.version
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type
        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name
        if self.vpc_ip is not None:
            result['VpcIp'] = self.vpc_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('VpcCloudInstanceId') is not None:
            self.vpc_cloud_instance_id = m.get('VpcCloudInstanceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')
        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')
        if m.get('VpcIp') is not None:
            self.vpc_ip = m.get('VpcIp')
        return self


class DescribeDBInstancesForDmsResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        code: str = None,
        message: str = None,
        count: int = None,
        instances: List[DescribeDBInstancesForDmsResponseBodyInstances] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.code = code
        self.message = message
        self.count = count
        self.instances = instances

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.count is not None:
            result['Count'] = self.count
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeDBInstancesForDmsResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class DescribeDBInstancesForDmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstancesForDmsResponseBody = None,
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
            temp_model = DescribeDBInstancesForDmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDBInstanceSecurityIpsRequest(TeaModel):
    def __init__(
        self,
        ali_uid: int = None,
        instance_id: str = None,
        group_name: str = None,
        while_list: str = None,
    ):
        self.ali_uid = ali_uid
        self.instance_id = instance_id
        self.group_name = group_name
        self.while_list = while_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.while_list is not None:
            result['WhileList'] = self.while_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('WhileList') is not None:
            self.while_list = m.get('WhileList')
        return self


class ModifyDBInstanceSecurityIpsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDBInstanceSecurityIpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDBInstanceSecurityIpsResponseBody = None,
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
            temp_model = ModifyDBInstanceSecurityIpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


