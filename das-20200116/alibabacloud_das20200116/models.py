# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class DataResultValue(TeaModel):
    def __init__(
        self,
        sql_id: str = None,
        error_code: str = None,
        count: int = None,
    ):
        self.sql_id = sql_id
        self.error_code = error_code
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class AddHDMInstanceRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        flush_account: str = None,
        instance_alias: str = None,
        instance_area: str = None,
        instance_id: str = None,
        ip: str = None,
        network_type: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        username: str = None,
        vpc_id: str = None,
        context: str = None,
    ):
        self.engine = engine
        self.flush_account = flush_account
        self.instance_alias = instance_alias
        self.instance_area = instance_area
        self.instance_id = instance_id
        self.ip = ip
        self.network_type = network_type
        self.password = password
        self.port = port
        self.region = region
        self.username = username
        # VPC ID。
        self.vpc_id = vpc_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.flush_account is not None:
            result['FlushAccount'] = self.flush_account
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.username is not None:
            result['Username'] = self.username
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('FlushAccount') is not None:
            self.flush_account = m.get('FlushAccount')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class AddHDMInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        caller_uid: str = None,
        code: int = None,
        error: str = None,
        instance_id: str = None,
        ip: str = None,
        owner_id: str = None,
        port: int = None,
        role: str = None,
        tenant_id: str = None,
        token: str = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        self.caller_uid = caller_uid
        self.code = code
        self.error = error
        self.instance_id = instance_id
        self.ip = ip
        self.owner_id = owner_id
        self.port = port
        self.role = role
        self.tenant_id = tenant_id
        self.token = token
        self.uuid = uuid
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.code is not None:
            result['Code'] = self.code
        if self.error is not None:
            result['Error'] = self.error
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.token is not None:
            result['Token'] = self.token
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class AddHDMInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: AddHDMInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AddHDMInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class AddHDMInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddHDMInstanceResponseBody = None,
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
            temp_model = AddHDMInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAdamBenchTaskRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        dst_instance_id: str = None,
        dst_super_account: str = None,
        dst_super_password: str = None,
        rate: int = None,
        request_duration: int = None,
        request_start_time: int = None,
        src_engine: str = None,
        src_engine_version: str = None,
        src_max_qps: float = None,
        src_mean_qps: float = None,
        src_sql_oss_addr: str = None,
    ):
        self.description = description
        self.dst_instance_id = dst_instance_id
        self.dst_super_account = dst_super_account
        self.dst_super_password = dst_super_password
        self.rate = rate
        self.request_duration = request_duration
        self.request_start_time = request_start_time
        self.src_engine = src_engine
        self.src_engine_version = src_engine_version
        self.src_max_qps = src_max_qps
        self.src_mean_qps = src_mean_qps
        self.src_sql_oss_addr = src_sql_oss_addr

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_id is not None:
            result['DstInstanceId'] = self.dst_instance_id
        if self.dst_super_account is not None:
            result['DstSuperAccount'] = self.dst_super_account
        if self.dst_super_password is not None:
            result['DstSuperPassword'] = self.dst_super_password
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time
        if self.src_engine is not None:
            result['SrcEngine'] = self.src_engine
        if self.src_engine_version is not None:
            result['SrcEngineVersion'] = self.src_engine_version
        if self.src_max_qps is not None:
            result['SrcMaxQps'] = self.src_max_qps
        if self.src_mean_qps is not None:
            result['SrcMeanQps'] = self.src_mean_qps
        if self.src_sql_oss_addr is not None:
            result['SrcSqlOssAddr'] = self.src_sql_oss_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceId') is not None:
            self.dst_instance_id = m.get('DstInstanceId')
        if m.get('DstSuperAccount') is not None:
            self.dst_super_account = m.get('DstSuperAccount')
        if m.get('DstSuperPassword') is not None:
            self.dst_super_password = m.get('DstSuperPassword')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')
        if m.get('SrcEngine') is not None:
            self.src_engine = m.get('SrcEngine')
        if m.get('SrcEngineVersion') is not None:
            self.src_engine_version = m.get('SrcEngineVersion')
        if m.get('SrcMaxQps') is not None:
            self.src_max_qps = m.get('SrcMaxQps')
        if m.get('SrcMeanQps') is not None:
            self.src_mean_qps = m.get('SrcMeanQps')
        if m.get('SrcSqlOssAddr') is not None:
            self.src_sql_oss_addr = m.get('SrcSqlOssAddr')
        return self


class CreateAdamBenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class CreateAdamBenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAdamBenchTaskResponseBody = None,
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
            temp_model = CreateAdamBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCacheAnalysisJobRequest(TeaModel):
    def __init__(
        self,
        backup_set_id: str = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.backup_set_id = backup_set_id
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.db = db
        self.encoding = encoding
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.node_id = node_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateCacheAnalysisJobResponseBodyDataBigKeys(TeaModel):
    def __init__(
        self,
        key_info: List[CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class CreateCacheAnalysisJobResponseBodyData(TeaModel):
    def __init__(
        self,
        big_keys: CreateCacheAnalysisJobResponseBodyDataBigKeys = None,
        instance_id: str = None,
        job_id: str = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
    ):
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.job_id = job_id
        self.message = message
        self.node_id = node_id
        self.task_state = task_state

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = CreateCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class CreateCacheAnalysisJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateCacheAnalysisJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = CreateCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCacheAnalysisJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCacheAnalysisJobResponseBody = None,
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
            temp_model = CreateCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudBenchTasksRequest(TeaModel):
    def __init__(
        self,
        amount: str = None,
        backup_id: str = None,
        backup_time: str = None,
        client_type: str = None,
        description: str = None,
        dst_connection_string: str = None,
        dst_instance_id: str = None,
        dst_port: str = None,
        dst_super_account: str = None,
        dst_super_password: str = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        end_state: str = None,
        gateway_vpc_id: str = None,
        gateway_vpc_ip: str = None,
        rate: str = None,
        request_duration: str = None,
        request_end_time: str = None,
        request_start_time: str = None,
        smart_pressure_time: str = None,
        src_instance_id: str = None,
        src_public_ip: str = None,
        src_super_account: str = None,
        src_super_password: str = None,
        task_type: str = None,
        work_dir: str = None,
    ):
        self.amount = amount
        self.backup_id = backup_id
        self.backup_time = backup_time
        self.client_type = client_type
        self.description = description
        self.dst_connection_string = dst_connection_string
        self.dst_instance_id = dst_instance_id
        self.dst_port = dst_port
        self.dst_super_account = dst_super_account
        self.dst_super_password = dst_super_password
        self.dst_type = dst_type
        self.dts_job_class = dts_job_class
        self.dts_job_id = dts_job_id
        self.end_state = end_state
        self.gateway_vpc_id = gateway_vpc_id
        self.gateway_vpc_ip = gateway_vpc_ip
        self.rate = rate
        self.request_duration = request_duration
        self.request_end_time = request_end_time
        self.request_start_time = request_start_time
        self.smart_pressure_time = smart_pressure_time
        self.src_instance_id = src_instance_id
        self.src_public_ip = src_public_ip
        self.src_super_account = src_super_account
        self.src_super_password = src_super_password
        self.task_type = task_type
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_connection_string is not None:
            result['DstConnectionString'] = self.dst_connection_string
        if self.dst_instance_id is not None:
            result['DstInstanceId'] = self.dst_instance_id
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_super_account is not None:
            result['DstSuperAccount'] = self.dst_super_account
        if self.dst_super_password is not None:
            result['DstSuperPassword'] = self.dst_super_password
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.gateway_vpc_id is not None:
            result['GatewayVpcId'] = self.gateway_vpc_id
        if self.gateway_vpc_ip is not None:
            result['GatewayVpcIp'] = self.gateway_vpc_ip
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.request_end_time is not None:
            result['RequestEndTime'] = self.request_end_time
        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.src_instance_id is not None:
            result['SrcInstanceId'] = self.src_instance_id
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.src_super_account is not None:
            result['SrcSuperAccount'] = self.src_super_account
        if self.src_super_password is not None:
            result['SrcSuperPassword'] = self.src_super_password
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstConnectionString') is not None:
            self.dst_connection_string = m.get('DstConnectionString')
        if m.get('DstInstanceId') is not None:
            self.dst_instance_id = m.get('DstInstanceId')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstSuperAccount') is not None:
            self.dst_super_account = m.get('DstSuperAccount')
        if m.get('DstSuperPassword') is not None:
            self.dst_super_password = m.get('DstSuperPassword')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('GatewayVpcId') is not None:
            self.gateway_vpc_id = m.get('GatewayVpcId')
        if m.get('GatewayVpcIp') is not None:
            self.gateway_vpc_ip = m.get('GatewayVpcIp')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('RequestEndTime') is not None:
            self.request_end_time = m.get('RequestEndTime')
        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('SrcInstanceId') is not None:
            self.src_instance_id = m.get('SrcInstanceId')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('SrcSuperAccount') is not None:
            self.src_super_account = m.get('SrcSuperAccount')
        if m.get('SrcSuperPassword') is not None:
            self.src_super_password = m.get('SrcSuperPassword')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class CreateCloudBenchTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        task_ids: List[str] = None,
    ):
        self.task_ids = task_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_ids is not None:
            result['taskIds'] = self.task_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskIds') is not None:
            self.task_ids = m.get('taskIds')
        return self


class CreateCloudBenchTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateCloudBenchTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = CreateCloudBenchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCloudBenchTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCloudBenchTasksResponseBody = None,
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
            temp_model = CreateCloudBenchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiagnosticReportRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateDiagnosticReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class CreateDiagnosticReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDiagnosticReportResponseBody = None,
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
            temp_model = CreateDiagnosticReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKillInstanceSessionTaskRequest(TeaModel):
    def __init__(
        self,
        db_user: str = None,
        db_user_password: str = None,
        ignored_users: str = None,
        instance_id: str = None,
        kill_all_sessions: str = None,
        node_id: str = None,
        session_ids: str = None,
    ):
        self.db_user = db_user
        self.db_user_password = db_user_password
        self.ignored_users = ignored_users
        self.instance_id = instance_id
        self.kill_all_sessions = kill_all_sessions
        self.node_id = node_id
        self.session_ids = session_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_user is not None:
            result['DbUser'] = self.db_user
        if self.db_user_password is not None:
            result['DbUserPassword'] = self.db_user_password
        if self.ignored_users is not None:
            result['IgnoredUsers'] = self.ignored_users
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.kill_all_sessions is not None:
            result['KillAllSessions'] = self.kill_all_sessions
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.session_ids is not None:
            result['SessionIds'] = self.session_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')
        if m.get('DbUserPassword') is not None:
            self.db_user_password = m.get('DbUserPassword')
        if m.get('IgnoredUsers') is not None:
            self.ignored_users = m.get('IgnoredUsers')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KillAllSessions') is not None:
            self.kill_all_sessions = m.get('KillAllSessions')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('SessionIds') is not None:
            self.session_ids = m.get('SessionIds')
        return self


class CreateKillInstanceSessionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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


class CreateKillInstanceSessionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKillInstanceSessionTaskResponseBody = None,
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
            temp_model = CreateKillInstanceSessionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRequestDiagnosisRequest(TeaModel):
    def __init__(
        self,
        database: str = None,
        instance_id: str = None,
        node_id: str = None,
        sql: str = None,
    ):
        self.database = database
        self.instance_id = instance_id
        self.node_id = node_id
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['Database'] = self.database
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.sql is not None:
            result['Sql'] = self.sql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        return self


class CreateRequestDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class CreateRequestDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRequestDiagnosisResponseBody = None,
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
            temp_model = CreateRequestDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCloudBenchTaskRequest(TeaModel):
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


class DeleteCloudBenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class DeleteCloudBenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCloudBenchTaskResponseBody = None,
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
            temp_model = DeleteCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStopGatewayRequest(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
    ):
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


class DeleteStopGatewayResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class DeleteStopGatewayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStopGatewayResponseBody = None,
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
            temp_model = DeleteStopGatewayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAutoScalingConfigRequest(TeaModel):
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


class DescribeAutoScalingConfigResponseBodyDataBandwidth(TeaModel):
    def __init__(
        self,
        bandwidth_usage_lower_threshold: int = None,
        bandwidth_usage_upper_threshold: int = None,
        downgrade: bool = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        self.bandwidth_usage_lower_threshold = bandwidth_usage_lower_threshold
        self.bandwidth_usage_upper_threshold = bandwidth_usage_upper_threshold
        self.downgrade = downgrade
        self.observation_window_size = observation_window_size
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_usage_lower_threshold is not None:
            result['BandwidthUsageLowerThreshold'] = self.bandwidth_usage_lower_threshold
        if self.bandwidth_usage_upper_threshold is not None:
            result['BandwidthUsageUpperThreshold'] = self.bandwidth_usage_upper_threshold
        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade
        if self.observation_window_size is not None:
            result['ObservationWindowSize'] = self.observation_window_size
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthUsageLowerThreshold') is not None:
            self.bandwidth_usage_lower_threshold = m.get('BandwidthUsageLowerThreshold')
        if m.get('BandwidthUsageUpperThreshold') is not None:
            self.bandwidth_usage_upper_threshold = m.get('BandwidthUsageUpperThreshold')
        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')
        if m.get('ObservationWindowSize') is not None:
            self.observation_window_size = m.get('ObservationWindowSize')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        return self


class DescribeAutoScalingConfigResponseBodyDataResource(TeaModel):
    def __init__(
        self,
        cpu_step: int = None,
        cpu_usage_upper_threshold: int = None,
        downgrade_observation_window_size: str = None,
        enable: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        self.cpu_step = cpu_step
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        self.downgrade_observation_window_size = downgrade_observation_window_size
        self.enable = enable
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_step is not None:
            result['CpuStep'] = self.cpu_step
        if self.cpu_usage_upper_threshold is not None:
            result['CpuUsageUpperThreshold'] = self.cpu_usage_upper_threshold
        if self.downgrade_observation_window_size is not None:
            result['DowngradeObservationWindowSize'] = self.downgrade_observation_window_size
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.upgrade_observation_window_size is not None:
            result['UpgradeObservationWindowSize'] = self.upgrade_observation_window_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuStep') is not None:
            self.cpu_step = m.get('CpuStep')
        if m.get('CpuUsageUpperThreshold') is not None:
            self.cpu_usage_upper_threshold = m.get('CpuUsageUpperThreshold')
        if m.get('DowngradeObservationWindowSize') is not None:
            self.downgrade_observation_window_size = m.get('DowngradeObservationWindowSize')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('UpgradeObservationWindowSize') is not None:
            self.upgrade_observation_window_size = m.get('UpgradeObservationWindowSize')
        return self


class DescribeAutoScalingConfigResponseBodyDataShard(TeaModel):
    def __init__(
        self,
        downgrade: bool = None,
        downgrade_observation_window_size: str = None,
        max_shards: int = None,
        mem_usage_lower_threshold: int = None,
        mem_usage_upper_threshold: int = None,
        min_shards: int = None,
        upgrade: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        self.downgrade = downgrade
        self.downgrade_observation_window_size = downgrade_observation_window_size
        self.max_shards = max_shards
        self.mem_usage_lower_threshold = mem_usage_lower_threshold
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        self.min_shards = min_shards
        self.upgrade = upgrade
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade
        if self.downgrade_observation_window_size is not None:
            result['DowngradeObservationWindowSize'] = self.downgrade_observation_window_size
        if self.max_shards is not None:
            result['MaxShards'] = self.max_shards
        if self.mem_usage_lower_threshold is not None:
            result['MemUsageLowerThreshold'] = self.mem_usage_lower_threshold
        if self.mem_usage_upper_threshold is not None:
            result['MemUsageUpperThreshold'] = self.mem_usage_upper_threshold
        if self.min_shards is not None:
            result['MinShards'] = self.min_shards
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        if self.upgrade_observation_window_size is not None:
            result['UpgradeObservationWindowSize'] = self.upgrade_observation_window_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')
        if m.get('DowngradeObservationWindowSize') is not None:
            self.downgrade_observation_window_size = m.get('DowngradeObservationWindowSize')
        if m.get('MaxShards') is not None:
            self.max_shards = m.get('MaxShards')
        if m.get('MemUsageLowerThreshold') is not None:
            self.mem_usage_lower_threshold = m.get('MemUsageLowerThreshold')
        if m.get('MemUsageUpperThreshold') is not None:
            self.mem_usage_upper_threshold = m.get('MemUsageUpperThreshold')
        if m.get('MinShards') is not None:
            self.min_shards = m.get('MinShards')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        if m.get('UpgradeObservationWindowSize') is not None:
            self.upgrade_observation_window_size = m.get('UpgradeObservationWindowSize')
        return self


class DescribeAutoScalingConfigResponseBodyDataSpec(TeaModel):
    def __init__(
        self,
        cool_down_time: str = None,
        cpu_usage_upper_threshold: int = None,
        downgrade: bool = None,
        max_read_only_nodes: int = None,
        max_spec: str = None,
        mem_usage_upper_threshold: int = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        self.cool_down_time = cool_down_time
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        self.downgrade = downgrade
        self.max_read_only_nodes = max_read_only_nodes
        self.max_spec = max_spec
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        self.observation_window_size = observation_window_size
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cool_down_time is not None:
            result['CoolDownTime'] = self.cool_down_time
        if self.cpu_usage_upper_threshold is not None:
            result['CpuUsageUpperThreshold'] = self.cpu_usage_upper_threshold
        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade
        if self.max_read_only_nodes is not None:
            result['MaxReadOnlyNodes'] = self.max_read_only_nodes
        if self.max_spec is not None:
            result['MaxSpec'] = self.max_spec
        if self.mem_usage_upper_threshold is not None:
            result['MemUsageUpperThreshold'] = self.mem_usage_upper_threshold
        if self.observation_window_size is not None:
            result['ObservationWindowSize'] = self.observation_window_size
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoolDownTime') is not None:
            self.cool_down_time = m.get('CoolDownTime')
        if m.get('CpuUsageUpperThreshold') is not None:
            self.cpu_usage_upper_threshold = m.get('CpuUsageUpperThreshold')
        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')
        if m.get('MaxReadOnlyNodes') is not None:
            self.max_read_only_nodes = m.get('MaxReadOnlyNodes')
        if m.get('MaxSpec') is not None:
            self.max_spec = m.get('MaxSpec')
        if m.get('MemUsageUpperThreshold') is not None:
            self.mem_usage_upper_threshold = m.get('MemUsageUpperThreshold')
        if m.get('ObservationWindowSize') is not None:
            self.observation_window_size = m.get('ObservationWindowSize')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        return self


class DescribeAutoScalingConfigResponseBodyDataStorage(TeaModel):
    def __init__(
        self,
        disk_usage_upper_threshold: int = None,
        max_storage: int = None,
        upgrade: bool = None,
    ):
        self.disk_usage_upper_threshold = disk_usage_upper_threshold
        self.max_storage = max_storage
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_usage_upper_threshold is not None:
            result['DiskUsageUpperThreshold'] = self.disk_usage_upper_threshold
        if self.max_storage is not None:
            result['MaxStorage'] = self.max_storage
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskUsageUpperThreshold') is not None:
            self.disk_usage_upper_threshold = m.get('DiskUsageUpperThreshold')
        if m.get('MaxStorage') is not None:
            self.max_storage = m.get('MaxStorage')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        return self


class DescribeAutoScalingConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        bandwidth: DescribeAutoScalingConfigResponseBodyDataBandwidth = None,
        resource: DescribeAutoScalingConfigResponseBodyDataResource = None,
        shard: DescribeAutoScalingConfigResponseBodyDataShard = None,
        spec: DescribeAutoScalingConfigResponseBodyDataSpec = None,
        storage: DescribeAutoScalingConfigResponseBodyDataStorage = None,
    ):
        self.bandwidth = bandwidth
        self.resource = resource
        self.shard = shard
        self.spec = spec
        self.storage = storage

    def validate(self):
        if self.bandwidth:
            self.bandwidth.validate()
        if self.resource:
            self.resource.validate()
        if self.shard:
            self.shard.validate()
        if self.spec:
            self.spec.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth.to_map()
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.shard is not None:
            result['Shard'] = self.shard.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            temp_model = DescribeAutoScalingConfigResponseBodyDataBandwidth()
            self.bandwidth = temp_model.from_map(m['Bandwidth'])
        if m.get('Resource') is not None:
            temp_model = DescribeAutoScalingConfigResponseBodyDataResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('Shard') is not None:
            temp_model = DescribeAutoScalingConfigResponseBodyDataShard()
            self.shard = temp_model.from_map(m['Shard'])
        if m.get('Spec') is not None:
            temp_model = DescribeAutoScalingConfigResponseBodyDataSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Storage') is not None:
            temp_model = DescribeAutoScalingConfigResponseBodyDataStorage()
            self.storage = temp_model.from_map(m['Storage'])
        return self


class DescribeAutoScalingConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeAutoScalingConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeAutoScalingConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAutoScalingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAutoScalingConfigResponseBody = None,
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
            temp_model = DescribeAutoScalingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_id: str = None,
    ):
        self.instance_id = instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.db = db
        self.encoding = encoding
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.node_id = node_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobResponseBodyDataBigKeys(TeaModel):
    def __init__(
        self,
        key_info: List[DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        key_num: int = None,
        prefix: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.key_num = key_num
        self.prefix = prefix
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.key_num is not None:
            result['KeyNum'] = self.key_num
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('KeyNum') is not None:
            self.key_num = m.get('KeyNum')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes(TeaModel):
    def __init__(
        self,
        prefix: List[DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix] = None,
    ):
        self.prefix = prefix

    def validate(self):
        if self.prefix:
            for k in self.prefix:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Prefix'] = []
        if self.prefix is not None:
            for k in self.prefix:
                result['Prefix'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prefix = []
        if m.get('Prefix') is not None:
            for k in m.get('Prefix'):
                temp_model = DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix()
                self.prefix.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobResponseBodyData(TeaModel):
    def __init__(
        self,
        big_keys: DescribeCacheAnalysisJobResponseBodyDataBigKeys = None,
        instance_id: str = None,
        job_id: str = None,
        key_prefixes: DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
    ):
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.job_id = job_id
        self.key_prefixes = key_prefixes
        self.message = message
        self.node_id = node_id
        self.task_state = task_state

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.key_prefixes:
            self.key_prefixes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.key_prefixes is not None:
            result['KeyPrefixes'] = self.key_prefixes.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('KeyPrefixes') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes()
            self.key_prefixes = temp_model.from_map(m['KeyPrefixes'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class DescribeCacheAnalysisJobResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCacheAnalysisJobResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCacheAnalysisJobResponseBody = None,
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
            temp_model = DescribeCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisJobsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time

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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        bytes: int = None,
        count: int = None,
        db: int = None,
        encoding: str = None,
        expiration_time_millis: int = None,
        key: str = None,
        node_id: str = None,
        type: str = None,
    ):
        self.bytes = bytes
        self.count = count
        self.db = db
        self.encoding = encoding
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.node_id = node_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.count is not None:
            result['Count'] = self.count
        if self.db is not None:
            result['Db'] = self.db
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys(TeaModel):
    def __init__(
        self,
        key_info: List[DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo] = None,
    ):
        self.key_info = key_info

    def validate(self):
        if self.key_info:
            for k in self.key_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeyInfo'] = []
        if self.key_info is not None:
            for k in self.key_info:
                result['KeyInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_info = []
        if m.get('KeyInfo') is not None:
            for k in m.get('KeyInfo'):
                temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo()
                self.key_info.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob(TeaModel):
    def __init__(
        self,
        big_keys: DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys = None,
        instance_id: str = None,
        job_id: str = None,
        message: str = None,
        node_id: str = None,
        task_state: str = None,
    ):
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.job_id = job_id
        self.message = message
        self.node_id = node_id
        self.task_state = task_state

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        cache_analysis_job: List[DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob] = None,
    ):
        self.cache_analysis_job = cache_analysis_job

    def validate(self):
        if self.cache_analysis_job:
            for k in self.cache_analysis_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CacheAnalysisJob'] = []
        if self.cache_analysis_job is not None:
            for k in self.cache_analysis_job:
                result['CacheAnalysisJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cache_analysis_job = []
        if m.get('CacheAnalysisJob') is not None:
            for k in m.get('CacheAnalysisJob'):
                temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJob()
                self.cache_analysis_job.append(temp_model.from_map(k))
        return self


class DescribeCacheAnalysisJobsResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: DescribeCacheAnalysisJobsResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCacheAnalysisJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCacheAnalysisJobsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeCacheAnalysisJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCacheAnalysisJobsResponseBody = None,
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
            temp_model = DescribeCacheAnalysisJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudBenchTasksRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
        status: str = None,
        task_type: str = None,
    ):
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time
        self.status = status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks(TeaModel):
    def __init__(
        self,
        archive_job_id: str = None,
        archive_oss_table_name: str = None,
        archive_state: int = None,
        backup_id: str = None,
        backup_type: str = None,
        bench_step: str = None,
        bench_step_status: str = None,
        client_gateway_id: str = None,
        client_type: str = None,
        description: str = None,
        dst_instance_uuid: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        dts_job_state: int = None,
        dts_job_status: str = None,
        ecs_instance_id: str = None,
        end_state: str = None,
        error_code: str = None,
        error_message: str = None,
        external: str = None,
        rate: int = None,
        request_duration: int = None,
        smart_pressure_time: int = None,
        source: str = None,
        sql_complete_reuse: str = None,
        src_instance_area: str = None,
        src_instance_uuid: str = None,
        src_public_ip: str = None,
        state: str = None,
        status: str = None,
        table_schema: str = None,
        task_id: str = None,
        task_type: str = None,
        topic: str = None,
        user_id: str = None,
        version: str = None,
        work_dir: str = None,
    ):
        self.archive_job_id = archive_job_id
        self.archive_oss_table_name = archive_oss_table_name
        self.archive_state = archive_state
        self.backup_id = backup_id
        self.backup_type = backup_type
        self.bench_step = bench_step
        self.bench_step_status = bench_step_status
        self.client_gateway_id = client_gateway_id
        self.client_type = client_type
        self.description = description
        self.dst_instance_uuid = dst_instance_uuid
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.dst_type = dst_type
        self.dts_job_class = dts_job_class
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.dts_job_state = dts_job_state
        self.dts_job_status = dts_job_status
        self.ecs_instance_id = ecs_instance_id
        self.end_state = end_state
        self.error_code = error_code
        self.error_message = error_message
        self.external = external
        self.rate = rate
        self.request_duration = request_duration
        self.smart_pressure_time = smart_pressure_time
        self.source = source
        self.sql_complete_reuse = sql_complete_reuse
        self.src_instance_area = src_instance_area
        self.src_instance_uuid = src_instance_uuid
        self.src_public_ip = src_public_ip
        self.state = state
        self.status = status
        self.table_schema = table_schema
        self.task_id = task_id
        self.task_type = task_type
        self.topic = topic
        self.user_id = user_id
        self.version = version
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_job_id is not None:
            result['ArchiveJobId'] = self.archive_job_id
        if self.archive_oss_table_name is not None:
            result['ArchiveOssTableName'] = self.archive_oss_table_name
        if self.archive_state is not None:
            result['ArchiveState'] = self.archive_state
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bench_step is not None:
            result['BenchStep'] = self.bench_step
        if self.bench_step_status is not None:
            result['BenchStepStatus'] = self.bench_step_status
        if self.client_gateway_id is not None:
            result['ClientGatewayId'] = self.client_gateway_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_uuid is not None:
            result['DstInstanceUuid'] = self.dst_instance_uuid
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dts_job_state is not None:
            result['DtsJobState'] = self.dts_job_state
        if self.dts_job_status is not None:
            result['DtsJobStatus'] = self.dts_job_status
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.external is not None:
            result['External'] = self.external
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.source is not None:
            result['Source'] = self.source
        if self.sql_complete_reuse is not None:
            result['SqlCompleteReuse'] = self.sql_complete_reuse
        if self.src_instance_area is not None:
            result['SrcInstanceArea'] = self.src_instance_area
        if self.src_instance_uuid is not None:
            result['SrcInstanceUuid'] = self.src_instance_uuid
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveJobId') is not None:
            self.archive_job_id = m.get('ArchiveJobId')
        if m.get('ArchiveOssTableName') is not None:
            self.archive_oss_table_name = m.get('ArchiveOssTableName')
        if m.get('ArchiveState') is not None:
            self.archive_state = m.get('ArchiveState')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BenchStep') is not None:
            self.bench_step = m.get('BenchStep')
        if m.get('BenchStepStatus') is not None:
            self.bench_step_status = m.get('BenchStepStatus')
        if m.get('ClientGatewayId') is not None:
            self.client_gateway_id = m.get('ClientGatewayId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceUuid') is not None:
            self.dst_instance_uuid = m.get('DstInstanceUuid')
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DtsJobState') is not None:
            self.dts_job_state = m.get('DtsJobState')
        if m.get('DtsJobStatus') is not None:
            self.dts_job_status = m.get('DtsJobStatus')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SqlCompleteReuse') is not None:
            self.sql_complete_reuse = m.get('SqlCompleteReuse')
        if m.get('SrcInstanceArea') is not None:
            self.src_instance_area = m.get('SrcInstanceArea')
        if m.get('SrcInstanceUuid') is not None:
            self.src_instance_uuid = m.get('SrcInstanceUuid')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudBenchTasksResponseBodyDataList(TeaModel):
    def __init__(
        self,
        cloudbench_tasks: List[DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks] = None,
    ):
        self.cloudbench_tasks = cloudbench_tasks

    def validate(self):
        if self.cloudbench_tasks:
            for k in self.cloudbench_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cloudbenchTasks'] = []
        if self.cloudbench_tasks is not None:
            for k in self.cloudbench_tasks:
                result['cloudbenchTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloudbench_tasks = []
        if m.get('cloudbenchTasks') is not None:
            for k in m.get('cloudbenchTasks'):
                temp_model = DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks()
                self.cloudbench_tasks.append(temp_model.from_map(k))
        return self


class DescribeCloudBenchTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: DescribeCloudBenchTasksResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = DescribeCloudBenchTasksResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCloudBenchTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCloudBenchTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeCloudBenchTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudBenchTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudBenchTasksResponseBody = None,
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
            temp_model = DescribeCloudBenchTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudbenchTaskRequest(TeaModel):
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


class DescribeCloudbenchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        archive_job_id: str = None,
        archive_oss_table_name: str = None,
        archive_state: int = None,
        backup_id: str = None,
        backup_type: str = None,
        bench_step: str = None,
        bench_step_status: str = None,
        client_gateway_id: str = None,
        client_type: str = None,
        description: str = None,
        dst_instance_uuid: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        dts_job_state: int = None,
        dts_job_status: str = None,
        ecs_instance_id: str = None,
        end_state: str = None,
        error_code: str = None,
        error_message: str = None,
        external: str = None,
        rate: int = None,
        request_duration: int = None,
        smart_pressure_time: int = None,
        source: str = None,
        sql_complete_reuse: str = None,
        src_instance_area: str = None,
        src_instance_uuid: str = None,
        src_public_ip: str = None,
        state: str = None,
        status: str = None,
        table_schema: str = None,
        task_id: str = None,
        task_type: str = None,
        topic: str = None,
        user_id: str = None,
        version: str = None,
        work_dir: str = None,
    ):
        self.archive_job_id = archive_job_id
        self.archive_oss_table_name = archive_oss_table_name
        self.archive_state = archive_state
        self.backup_id = backup_id
        self.backup_type = backup_type
        self.bench_step = bench_step
        self.bench_step_status = bench_step_status
        self.client_gateway_id = client_gateway_id
        self.client_type = client_type
        self.description = description
        self.dst_instance_uuid = dst_instance_uuid
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.dst_type = dst_type
        self.dts_job_class = dts_job_class
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.dts_job_state = dts_job_state
        self.dts_job_status = dts_job_status
        self.ecs_instance_id = ecs_instance_id
        self.end_state = end_state
        self.error_code = error_code
        self.error_message = error_message
        self.external = external
        self.rate = rate
        self.request_duration = request_duration
        self.smart_pressure_time = smart_pressure_time
        self.source = source
        self.sql_complete_reuse = sql_complete_reuse
        self.src_instance_area = src_instance_area
        self.src_instance_uuid = src_instance_uuid
        self.src_public_ip = src_public_ip
        self.state = state
        self.status = status
        self.table_schema = table_schema
        self.task_id = task_id
        self.task_type = task_type
        self.topic = topic
        self.user_id = user_id
        self.version = version
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_job_id is not None:
            result['ArchiveJobId'] = self.archive_job_id
        if self.archive_oss_table_name is not None:
            result['ArchiveOssTableName'] = self.archive_oss_table_name
        if self.archive_state is not None:
            result['ArchiveState'] = self.archive_state
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.bench_step is not None:
            result['BenchStep'] = self.bench_step
        if self.bench_step_status is not None:
            result['BenchStepStatus'] = self.bench_step_status
        if self.client_gateway_id is not None:
            result['ClientGatewayId'] = self.client_gateway_id
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.description is not None:
            result['Description'] = self.description
        if self.dst_instance_uuid is not None:
            result['DstInstanceUuid'] = self.dst_instance_uuid
        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip
        if self.dst_port is not None:
            result['DstPort'] = self.dst_port
        if self.dst_type is not None:
            result['DstType'] = self.dst_type
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dts_job_state is not None:
            result['DtsJobState'] = self.dts_job_state
        if self.dts_job_status is not None:
            result['DtsJobStatus'] = self.dts_job_status
        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id
        if self.end_state is not None:
            result['EndState'] = self.end_state
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.external is not None:
            result['External'] = self.external
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration
        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time
        if self.source is not None:
            result['Source'] = self.source
        if self.sql_complete_reuse is not None:
            result['SqlCompleteReuse'] = self.sql_complete_reuse
        if self.src_instance_area is not None:
            result['SrcInstanceArea'] = self.src_instance_area
        if self.src_instance_uuid is not None:
            result['SrcInstanceUuid'] = self.src_instance_uuid
        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip
        if self.state is not None:
            result['State'] = self.state
        if self.status is not None:
            result['Status'] = self.status
        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.version is not None:
            result['Version'] = self.version
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveJobId') is not None:
            self.archive_job_id = m.get('ArchiveJobId')
        if m.get('ArchiveOssTableName') is not None:
            self.archive_oss_table_name = m.get('ArchiveOssTableName')
        if m.get('ArchiveState') is not None:
            self.archive_state = m.get('ArchiveState')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BenchStep') is not None:
            self.bench_step = m.get('BenchStep')
        if m.get('BenchStepStatus') is not None:
            self.bench_step_status = m.get('BenchStepStatus')
        if m.get('ClientGatewayId') is not None:
            self.client_gateway_id = m.get('ClientGatewayId')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DstInstanceUuid') is not None:
            self.dst_instance_uuid = m.get('DstInstanceUuid')
        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')
        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')
        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DtsJobState') is not None:
            self.dts_job_state = m.get('DtsJobState')
        if m.get('DtsJobStatus') is not None:
            self.dts_job_status = m.get('DtsJobStatus')
        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')
        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')
        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SqlCompleteReuse') is not None:
            self.sql_complete_reuse = m.get('SqlCompleteReuse')
        if m.get('SrcInstanceArea') is not None:
            self.src_instance_area = m.get('SrcInstanceArea')
        if m.get('SrcInstanceUuid') is not None:
            self.src_instance_uuid = m.get('SrcInstanceUuid')
        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudbenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCloudbenchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeCloudbenchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudbenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudbenchTaskResponseBody = None,
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
            temp_model = DescribeCloudbenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudbenchTaskConfigRequest(TeaModel):
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


class DescribeCloudbenchTaskConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        archive_folder: str = None,
        bench_cmd: str = None,
        client_jar_path: str = None,
        jar_on_oss: str = None,
        load_cmd: str = None,
        meta_file_name: str = None,
        meta_file_on_oss: str = None,
        meta_file_path: str = None,
        parse_cmd: str = None,
        parse_file_path: str = None,
        rocks_db_path: str = None,
        sql_file_name: str = None,
        sql_file_on_oss: str = None,
        sql_file_path: str = None,
        task_id: str = None,
        user_id: str = None,
        work_dir: str = None,
    ):
        self.archive_folder = archive_folder
        self.bench_cmd = bench_cmd
        self.client_jar_path = client_jar_path
        self.jar_on_oss = jar_on_oss
        self.load_cmd = load_cmd
        self.meta_file_name = meta_file_name
        self.meta_file_on_oss = meta_file_on_oss
        self.meta_file_path = meta_file_path
        self.parse_cmd = parse_cmd
        self.parse_file_path = parse_file_path
        self.rocks_db_path = rocks_db_path
        self.sql_file_name = sql_file_name
        self.sql_file_on_oss = sql_file_on_oss
        self.sql_file_path = sql_file_path
        self.task_id = task_id
        self.user_id = user_id
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_folder is not None:
            result['ArchiveFolder'] = self.archive_folder
        if self.bench_cmd is not None:
            result['BenchCmd'] = self.bench_cmd
        if self.client_jar_path is not None:
            result['ClientJarPath'] = self.client_jar_path
        if self.jar_on_oss is not None:
            result['JarOnOss'] = self.jar_on_oss
        if self.load_cmd is not None:
            result['LoadCmd'] = self.load_cmd
        if self.meta_file_name is not None:
            result['MetaFileName'] = self.meta_file_name
        if self.meta_file_on_oss is not None:
            result['MetaFileOnOss'] = self.meta_file_on_oss
        if self.meta_file_path is not None:
            result['MetaFilePath'] = self.meta_file_path
        if self.parse_cmd is not None:
            result['ParseCmd'] = self.parse_cmd
        if self.parse_file_path is not None:
            result['ParseFilePath'] = self.parse_file_path
        if self.rocks_db_path is not None:
            result['RocksDbPath'] = self.rocks_db_path
        if self.sql_file_name is not None:
            result['SqlFileName'] = self.sql_file_name
        if self.sql_file_on_oss is not None:
            result['SqlFileOnOss'] = self.sql_file_on_oss
        if self.sql_file_path is not None:
            result['SqlFilePath'] = self.sql_file_path
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveFolder') is not None:
            self.archive_folder = m.get('ArchiveFolder')
        if m.get('BenchCmd') is not None:
            self.bench_cmd = m.get('BenchCmd')
        if m.get('ClientJarPath') is not None:
            self.client_jar_path = m.get('ClientJarPath')
        if m.get('JarOnOss') is not None:
            self.jar_on_oss = m.get('JarOnOss')
        if m.get('LoadCmd') is not None:
            self.load_cmd = m.get('LoadCmd')
        if m.get('MetaFileName') is not None:
            self.meta_file_name = m.get('MetaFileName')
        if m.get('MetaFileOnOss') is not None:
            self.meta_file_on_oss = m.get('MetaFileOnOss')
        if m.get('MetaFilePath') is not None:
            self.meta_file_path = m.get('MetaFilePath')
        if m.get('ParseCmd') is not None:
            self.parse_cmd = m.get('ParseCmd')
        if m.get('ParseFilePath') is not None:
            self.parse_file_path = m.get('ParseFilePath')
        if m.get('RocksDbPath') is not None:
            self.rocks_db_path = m.get('RocksDbPath')
        if m.get('SqlFileName') is not None:
            self.sql_file_name = m.get('SqlFileName')
        if m.get('SqlFileOnOss') is not None:
            self.sql_file_on_oss = m.get('SqlFileOnOss')
        if m.get('SqlFilePath') is not None:
            self.sql_file_path = m.get('SqlFilePath')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')
        return self


class DescribeCloudbenchTaskConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeCloudbenchTaskConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeCloudbenchTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCloudbenchTaskConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudbenchTaskConfigResponseBody = None,
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
            temp_model = DescribeCloudbenchTaskConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosticReportListRequest(TeaModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        end_time: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeDiagnosticReportListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class DescribeDiagnosticReportListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosticReportListResponseBody = None,
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
            temp_model = DescribeDiagnosticReportListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHotBigKeysRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotBigKeysResponseBodyDataBigKeysBigKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
        size: int = None,
    ):
        self.db = db
        self.key = key
        self.key_type = key_type
        self.node_id = node_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeHotBigKeysResponseBodyDataBigKeys(TeaModel):
    def __init__(
        self,
        big_key: List[DescribeHotBigKeysResponseBodyDataBigKeysBigKey] = None,
    ):
        self.big_key = big_key

    def validate(self):
        if self.big_key:
            for k in self.big_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BigKey'] = []
        if self.big_key is not None:
            for k in self.big_key:
                result['BigKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.big_key = []
        if m.get('BigKey') is not None:
            for k in m.get('BigKey'):
                temp_model = DescribeHotBigKeysResponseBodyDataBigKeysBigKey()
                self.big_key.append(temp_model.from_map(k))
        return self


class DescribeHotBigKeysResponseBodyDataHotKeysHotKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        lfu: int = None,
        node_id: str = None,
    ):
        self.db = db
        self.hot = hot
        self.key = key
        self.key_type = key_type
        self.lfu = lfu
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.lfu is not None:
            result['Lfu'] = self.lfu
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Lfu') is not None:
            self.lfu = m.get('Lfu')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotBigKeysResponseBodyDataHotKeys(TeaModel):
    def __init__(
        self,
        hot_key: List[DescribeHotBigKeysResponseBodyDataHotKeysHotKey] = None,
    ):
        self.hot_key = hot_key

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeHotBigKeysResponseBodyDataHotKeysHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeHotBigKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        big_key_msg: str = None,
        big_keys: DescribeHotBigKeysResponseBodyDataBigKeys = None,
        hot_key_msg: str = None,
        hot_keys: DescribeHotBigKeysResponseBodyDataHotKeys = None,
    ):
        self.big_key_msg = big_key_msg
        self.big_keys = big_keys
        self.hot_key_msg = hot_key_msg
        self.hot_keys = hot_keys

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()
        if self.hot_keys:
            self.hot_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.big_key_msg is not None:
            result['BigKeyMsg'] = self.big_key_msg
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.hot_key_msg is not None:
            result['HotKeyMsg'] = self.hot_key_msg
        if self.hot_keys is not None:
            result['HotKeys'] = self.hot_keys.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BigKeyMsg') is not None:
            self.big_key_msg = m.get('BigKeyMsg')
        if m.get('BigKeys') is not None:
            temp_model = DescribeHotBigKeysResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('HotKeyMsg') is not None:
            self.hot_key_msg = m.get('HotKeyMsg')
        if m.get('HotKeys') is not None:
            temp_model = DescribeHotBigKeysResponseBodyDataHotKeys()
            self.hot_keys = temp_model.from_map(m['HotKeys'])
        return self


class DescribeHotBigKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeHotBigKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeHotBigKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHotBigKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHotBigKeysResponseBody = None,
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
            temp_model = DescribeHotBigKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHotKeysRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeHotKeysResponseBodyDataHotKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        size: int = None,
    ):
        self.db = db
        self.hot = hot
        self.key = key
        self.key_type = key_type
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeHotKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        hot_key: List[DescribeHotKeysResponseBodyDataHotKey] = None,
    ):
        self.hot_key = hot_key

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeHotKeysResponseBodyDataHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeHotKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeHotKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeHotKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHotKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHotKeysResponseBody = None,
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
            temp_model = DescribeHotKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceDasProRequest(TeaModel):
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


class DescribeInstanceDasProResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class DescribeInstanceDasProResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceDasProResponseBody = None,
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
            temp_model = DescribeInstanceDasProResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopBigKeysRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        end_time: str = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: str = None,
    ):
        self.console_context = console_context
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_id = node_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopBigKeysResponseBodyDataBigKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        key: str = None,
        key_type: str = None,
        node_id: str = None,
        size: int = None,
    ):
        self.db = db
        self.key = key
        self.key_type = key_type
        self.node_id = node_id
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class DescribeTopBigKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        big_key: List[DescribeTopBigKeysResponseBodyDataBigKey] = None,
    ):
        self.big_key = big_key

    def validate(self):
        if self.big_key:
            for k in self.big_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BigKey'] = []
        if self.big_key is not None:
            for k in self.big_key:
                result['BigKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.big_key = []
        if m.get('BigKey') is not None:
            for k in m.get('BigKey'):
                temp_model = DescribeTopBigKeysResponseBodyDataBigKey()
                self.big_key.append(temp_model.from_map(k))
        return self


class DescribeTopBigKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeTopBigKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeTopBigKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTopBigKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTopBigKeysResponseBody = None,
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
            temp_model = DescribeTopBigKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTopHotKeysRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        end_time: str = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: str = None,
    ):
        self.console_context = console_context
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_id = node_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeTopHotKeysResponseBodyDataHotKey(TeaModel):
    def __init__(
        self,
        db: int = None,
        hot: str = None,
        key: str = None,
        key_type: str = None,
        lfu: int = None,
        node_id: str = None,
    ):
        self.db = db
        self.hot = hot
        self.key = key
        self.key_type = key_type
        self.lfu = lfu
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key is not None:
            result['Key'] = self.key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.lfu is not None:
            result['Lfu'] = self.lfu
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('Lfu') is not None:
            self.lfu = m.get('Lfu')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeTopHotKeysResponseBodyData(TeaModel):
    def __init__(
        self,
        hot_key: List[DescribeTopHotKeysResponseBodyDataHotKey] = None,
    ):
        self.hot_key = hot_key

    def validate(self):
        if self.hot_key:
            for k in self.hot_key:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HotKey'] = []
        if self.hot_key is not None:
            for k in self.hot_key:
                result['HotKey'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_key = []
        if m.get('HotKey') is not None:
            for k in m.get('HotKey'):
                temp_model = DescribeTopHotKeysResponseBodyDataHotKey()
                self.hot_key.append(temp_model.from_map(k))
        return self


class DescribeTopHotKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DescribeTopHotKeysResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DescribeTopHotKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTopHotKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTopHotKeysResponseBody = None,
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
            temp_model = DescribeTopHotKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAllSqlConcurrencyControlRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableAllSqlConcurrencyControlRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class DisableAllSqlConcurrencyControlRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAllSqlConcurrencyControlRulesResponseBody = None,
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
            temp_model = DisableAllSqlConcurrencyControlRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAutoResourceOptimizeRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_ids: str = None,
    ):
        self.console_context = console_context
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DisableAutoResourceOptimizeRulesResponseBodyDataConfigFailInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        error_message: str = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.error_message = error_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableAutoResourceOptimizeRulesResponseBodyDataConfigSuccessInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableAutoResourceOptimizeRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        config_fail_instance_count: int = None,
        config_fail_instance_list: List[DisableAutoResourceOptimizeRulesResponseBodyDataConfigFailInstanceList] = None,
        config_success_instance_count: int = None,
        config_success_instance_list: List[DisableAutoResourceOptimizeRulesResponseBodyDataConfigSuccessInstanceList] = None,
        total_instance_count: int = None,
    ):
        self.config_fail_instance_count = config_fail_instance_count
        self.config_fail_instance_list = config_fail_instance_list
        self.config_success_instance_count = config_success_instance_count
        self.config_success_instance_list = config_success_instance_list
        self.total_instance_count = total_instance_count

    def validate(self):
        if self.config_fail_instance_list:
            for k in self.config_fail_instance_list:
                if k:
                    k.validate()
        if self.config_success_instance_list:
            for k in self.config_success_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_fail_instance_count is not None:
            result['ConfigFailInstanceCount'] = self.config_fail_instance_count
        result['ConfigFailInstanceList'] = []
        if self.config_fail_instance_list is not None:
            for k in self.config_fail_instance_list:
                result['ConfigFailInstanceList'].append(k.to_map() if k else None)
        if self.config_success_instance_count is not None:
            result['ConfigSuccessInstanceCount'] = self.config_success_instance_count
        result['ConfigSuccessInstanceList'] = []
        if self.config_success_instance_list is not None:
            for k in self.config_success_instance_list:
                result['ConfigSuccessInstanceList'].append(k.to_map() if k else None)
        if self.total_instance_count is not None:
            result['TotalInstanceCount'] = self.total_instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFailInstanceCount') is not None:
            self.config_fail_instance_count = m.get('ConfigFailInstanceCount')
        self.config_fail_instance_list = []
        if m.get('ConfigFailInstanceList') is not None:
            for k in m.get('ConfigFailInstanceList'):
                temp_model = DisableAutoResourceOptimizeRulesResponseBodyDataConfigFailInstanceList()
                self.config_fail_instance_list.append(temp_model.from_map(k))
        if m.get('ConfigSuccessInstanceCount') is not None:
            self.config_success_instance_count = m.get('ConfigSuccessInstanceCount')
        self.config_success_instance_list = []
        if m.get('ConfigSuccessInstanceList') is not None:
            for k in m.get('ConfigSuccessInstanceList'):
                temp_model = DisableAutoResourceOptimizeRulesResponseBodyDataConfigSuccessInstanceList()
                self.config_success_instance_list.append(temp_model.from_map(k))
        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')
        return self


class DisableAutoResourceOptimizeRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DisableAutoResourceOptimizeRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DisableAutoResourceOptimizeRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableAutoResourceOptimizeRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAutoResourceOptimizeRulesResponseBody = None,
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
            temp_model = DisableAutoResourceOptimizeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableAutoThrottleRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_ids: str = None,
    ):
        self.console_context = console_context
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class DisableAutoThrottleRulesResponseBodyDataConfigFailInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        error_message: str = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.error_message = error_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableAutoThrottleRulesResponseBodyDataConfigSuccessInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DisableAutoThrottleRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        config_fail_instance_count: int = None,
        config_fail_instance_list: List[DisableAutoThrottleRulesResponseBodyDataConfigFailInstanceList] = None,
        config_success_instance_count: int = None,
        config_success_instance_list: List[DisableAutoThrottleRulesResponseBodyDataConfigSuccessInstanceList] = None,
        total_instance_count: int = None,
    ):
        self.config_fail_instance_count = config_fail_instance_count
        self.config_fail_instance_list = config_fail_instance_list
        self.config_success_instance_count = config_success_instance_count
        self.config_success_instance_list = config_success_instance_list
        self.total_instance_count = total_instance_count

    def validate(self):
        if self.config_fail_instance_list:
            for k in self.config_fail_instance_list:
                if k:
                    k.validate()
        if self.config_success_instance_list:
            for k in self.config_success_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_fail_instance_count is not None:
            result['ConfigFailInstanceCount'] = self.config_fail_instance_count
        result['ConfigFailInstanceList'] = []
        if self.config_fail_instance_list is not None:
            for k in self.config_fail_instance_list:
                result['ConfigFailInstanceList'].append(k.to_map() if k else None)
        if self.config_success_instance_count is not None:
            result['ConfigSuccessInstanceCount'] = self.config_success_instance_count
        result['ConfigSuccessInstanceList'] = []
        if self.config_success_instance_list is not None:
            for k in self.config_success_instance_list:
                result['ConfigSuccessInstanceList'].append(k.to_map() if k else None)
        if self.total_instance_count is not None:
            result['TotalInstanceCount'] = self.total_instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFailInstanceCount') is not None:
            self.config_fail_instance_count = m.get('ConfigFailInstanceCount')
        self.config_fail_instance_list = []
        if m.get('ConfigFailInstanceList') is not None:
            for k in m.get('ConfigFailInstanceList'):
                temp_model = DisableAutoThrottleRulesResponseBodyDataConfigFailInstanceList()
                self.config_fail_instance_list.append(temp_model.from_map(k))
        if m.get('ConfigSuccessInstanceCount') is not None:
            self.config_success_instance_count = m.get('ConfigSuccessInstanceCount')
        self.config_success_instance_list = []
        if m.get('ConfigSuccessInstanceList') is not None:
            for k in m.get('ConfigSuccessInstanceList'):
                temp_model = DisableAutoThrottleRulesResponseBodyDataConfigSuccessInstanceList()
                self.config_success_instance_list.append(temp_model.from_map(k))
        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')
        return self


class DisableAutoThrottleRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DisableAutoThrottleRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = DisableAutoThrottleRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableAutoThrottleRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableAutoThrottleRulesResponseBody = None,
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
            temp_model = DisableAutoThrottleRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableDasProRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_id: str = None,
    ):
        self.instance_id = instance_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DisableDasProResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class DisableDasProResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableDasProResponseBody = None,
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
            temp_model = DisableDasProResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstanceDasConfigRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        instance_id: str = None,
        scale_type: str = None,
    ):
        self.engine = engine
        self.instance_id = instance_id
        self.scale_type = scale_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scale_type is not None:
            result['ScaleType'] = self.scale_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScaleType') is not None:
            self.scale_type = m.get('ScaleType')
        return self


class DisableInstanceDasConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class DisableInstanceDasConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableInstanceDasConfigResponseBody = None,
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
            temp_model = DisableInstanceDasConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableSqlConcurrencyControlRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        item_id: int = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class DisableSqlConcurrencyControlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class DisableSqlConcurrencyControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableSqlConcurrencyControlResponseBody = None,
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
            temp_model = DisableSqlConcurrencyControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableDasProRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        sql_retention: int = None,
        user_id: str = None,
    ):
        self.instance_id = instance_id
        self.sql_retention = sql_retention
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_retention is not None:
            result['SqlRetention'] = self.sql_retention
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlRetention') is not None:
            self.sql_retention = m.get('SqlRetention')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class EnableDasProResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class EnableDasProResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableDasProResponseBody = None,
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
            temp_model = EnableDasProResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSqlConcurrencyControlRequest(TeaModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        console_context: str = None,
        instance_id: str = None,
        max_concurrency: int = None,
        sql_keywords: str = None,
        sql_type: str = None,
    ):
        self.concurrency_control_time = concurrency_control_time
        self.console_context = console_context
        self.instance_id = instance_id
        self.max_concurrency = max_concurrency
        self.sql_keywords = sql_keywords
        self.sql_type = sql_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class EnableSqlConcurrencyControlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class EnableSqlConcurrencyControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableSqlConcurrencyControlResponseBody = None,
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
            temp_model = EnableSqlConcurrencyControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncErrorRequestListByCodeRequest(TeaModel):
    def __init__(
        self,
        end: int = None,
        error_code: str = None,
        instance_id: str = None,
        node_id: str = None,
        start: int = None,
    ):
        self.end = end
        self.error_code = error_code
        self.instance_id = instance_id
        self.node_id = node_id
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetAsyncErrorRequestListByCodeResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        sql_id: str = None,
    ):
        self.instance_id = instance_id
        # SQL ID。
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        return self


class GetAsyncErrorRequestListByCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        complete: bool = None,
        fail: bool = None,
        is_finish: bool = None,
        result: List[GetAsyncErrorRequestListByCodeResponseBodyDataResult] = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.complete = complete
        self.fail = fail
        self.is_finish = is_finish
        self.result = result
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

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
        if self.complete is not None:
            result['complete'] = self.complete
        if self.fail is not None:
            result['fail'] = self.fail
        if self.is_finish is not None:
            result['isFinish'] = self.is_finish
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.result_id is not None:
            result['resultId'] = self.result_id
        if self.state is not None:
            result['state'] = self.state
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('complete') is not None:
            self.complete = m.get('complete')
        if m.get('fail') is not None:
            self.fail = m.get('fail')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetAsyncErrorRequestListByCodeResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetAsyncErrorRequestListByCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAsyncErrorRequestListByCodeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetAsyncErrorRequestListByCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncErrorRequestListByCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncErrorRequestListByCodeResponseBody = None,
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
            temp_model = GetAsyncErrorRequestListByCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncErrorRequestStatByCodeRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end: int = None,
        instance_id: str = None,
        node_id: str = None,
        start: int = None,
    ):
        self.db_name = db_name
        self.end = end
        self.instance_id = instance_id
        self.node_id = node_id
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetAsyncErrorRequestStatByCodeResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        count: int = None,
        error_code: str = None,
        instance_id: str = None,
    ):
        self.count = count
        self.error_code = error_code
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self


class GetAsyncErrorRequestStatByCodeResponseBodyData(TeaModel):
    def __init__(
        self,
        complete: bool = None,
        fail: bool = None,
        is_finish: bool = None,
        result: List[GetAsyncErrorRequestStatByCodeResponseBodyDataResult] = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.complete = complete
        self.fail = fail
        self.is_finish = is_finish
        self.result = result
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

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
        if self.complete is not None:
            result['complete'] = self.complete
        if self.fail is not None:
            result['fail'] = self.fail
        if self.is_finish is not None:
            result['isFinish'] = self.is_finish
        result['result'] = []
        if self.result is not None:
            for k in self.result:
                result['result'].append(k.to_map() if k else None)
        if self.result_id is not None:
            result['resultId'] = self.result_id
        if self.state is not None:
            result['state'] = self.state
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('complete') is not None:
            self.complete = m.get('complete')
        if m.get('fail') is not None:
            self.fail = m.get('fail')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        self.result = []
        if m.get('result') is not None:
            for k in m.get('result'):
                temp_model = GetAsyncErrorRequestStatByCodeResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetAsyncErrorRequestStatByCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAsyncErrorRequestStatByCodeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetAsyncErrorRequestStatByCodeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncErrorRequestStatByCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncErrorRequestStatByCodeResponseBody = None,
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
            temp_model = GetAsyncErrorRequestStatByCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncErrorRequestStatResultRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end: int = None,
        instance_id: str = None,
        node_id: str = None,
        sql_id_list: str = None,
        start: int = None,
    ):
        self.db_name = db_name
        self.end = end
        self.instance_id = instance_id
        self.node_id = node_id
        self.sql_id_list = sql_id_list
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.sql_id_list is not None:
            result['SqlIdList'] = self.sql_id_list
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('SqlIdList') is not None:
            self.sql_id_list = m.get('SqlIdList')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetAsyncErrorRequestStatResultResponseBodyData(TeaModel):
    def __init__(
        self,
        complete: bool = None,
        fail: bool = None,
        is_finish: bool = None,
        result: Dict[str, DataResultValue] = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.complete = complete
        self.fail = fail
        self.is_finish = is_finish
        self.result = result
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete is not None:
            result['complete'] = self.complete
        if self.fail is not None:
            result['fail'] = self.fail
        if self.is_finish is not None:
            result['isFinish'] = self.is_finish
        result['result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['result'][k] = v.to_map()
        if self.result_id is not None:
            result['resultId'] = self.result_id
        if self.state is not None:
            result['state'] = self.state
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('complete') is not None:
            self.complete = m.get('complete')
        if m.get('fail') is not None:
            self.fail = m.get('fail')
        if m.get('isFinish') is not None:
            self.is_finish = m.get('isFinish')
        self.result = {}
        if m.get('result') is not None:
            for k, v in m.get('result').items():
                temp_model = DataResultValue()
                self.result[k] = temp_model.from_map(v)
        if m.get('resultId') is not None:
            self.result_id = m.get('resultId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetAsyncErrorRequestStatResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAsyncErrorRequestStatResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetAsyncErrorRequestStatResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAsyncErrorRequestStatResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncErrorRequestStatResultResponseBody = None,
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
            temp_model = GetAsyncErrorRequestStatResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoResourceOptimizeRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_ids: str = None,
    ):
        self.console_context = console_context
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class GetAutoResourceOptimizeRulesResponseBodyDataEnableAutoResourceOptimizeList(TeaModel):
    def __init__(
        self,
        auto_defragment: bool = None,
        das_pro_on: bool = None,
        instance_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
        user_id: str = None,
    ):
        self.auto_defragment = auto_defragment
        self.das_pro_on = das_pro_on
        self.instance_id = instance_id
        self.table_fragmentation_ratio = table_fragmentation_ratio
        self.table_space_size = table_space_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment
        if self.das_pro_on is not None:
            result['DasProOn'] = self.das_pro_on
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio
        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')
        if m.get('DasProOn') is not None:
            self.das_pro_on = m.get('DasProOn')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')
        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAutoResourceOptimizeRulesResponseBodyDataHasEnableRuleButNotDasProList(TeaModel):
    def __init__(
        self,
        auto_defragment: bool = None,
        das_pro_on: bool = None,
        instance_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
        user_id: str = None,
    ):
        self.auto_defragment = auto_defragment
        self.das_pro_on = das_pro_on
        self.instance_id = instance_id
        self.table_fragmentation_ratio = table_fragmentation_ratio
        self.table_space_size = table_space_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment
        if self.das_pro_on is not None:
            result['DasProOn'] = self.das_pro_on
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio
        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')
        if m.get('DasProOn') is not None:
            self.das_pro_on = m.get('DasProOn')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')
        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAutoResourceOptimizeRulesResponseBodyDataTurnOffAutoResourceOptimizeList(TeaModel):
    def __init__(
        self,
        auto_defragment: bool = None,
        das_pro_on: bool = None,
        instance_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
        user_id: str = None,
    ):
        self.auto_defragment = auto_defragment
        self.das_pro_on = das_pro_on
        self.instance_id = instance_id
        self.table_fragmentation_ratio = table_fragmentation_ratio
        self.table_space_size = table_space_size
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment
        if self.das_pro_on is not None:
            result['DasProOn'] = self.das_pro_on
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio
        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')
        if m.get('DasProOn') is not None:
            self.das_pro_on = m.get('DasProOn')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')
        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetAutoResourceOptimizeRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        enable_auto_resource_optimize_count: int = None,
        enable_auto_resource_optimize_list: List[GetAutoResourceOptimizeRulesResponseBodyDataEnableAutoResourceOptimizeList] = None,
        has_enable_rule_but_not_das_pro_count: int = None,
        has_enable_rule_but_not_das_pro_list: List[GetAutoResourceOptimizeRulesResponseBodyDataHasEnableRuleButNotDasProList] = None,
        never_enable_auto_resource_optimize_or_released_instance_count: int = None,
        never_enable_auto_resource_optimize_or_released_instance_id_list: List[str] = None,
        total_auto_resource_optimize_rules_count: int = None,
        turn_off_auto_resource_optimize_count: int = None,
        turn_off_auto_resource_optimize_list: List[GetAutoResourceOptimizeRulesResponseBodyDataTurnOffAutoResourceOptimizeList] = None,
    ):
        self.enable_auto_resource_optimize_count = enable_auto_resource_optimize_count
        self.enable_auto_resource_optimize_list = enable_auto_resource_optimize_list
        self.has_enable_rule_but_not_das_pro_count = has_enable_rule_but_not_das_pro_count
        self.has_enable_rule_but_not_das_pro_list = has_enable_rule_but_not_das_pro_list
        self.never_enable_auto_resource_optimize_or_released_instance_count = never_enable_auto_resource_optimize_or_released_instance_count
        self.never_enable_auto_resource_optimize_or_released_instance_id_list = never_enable_auto_resource_optimize_or_released_instance_id_list
        self.total_auto_resource_optimize_rules_count = total_auto_resource_optimize_rules_count
        self.turn_off_auto_resource_optimize_count = turn_off_auto_resource_optimize_count
        self.turn_off_auto_resource_optimize_list = turn_off_auto_resource_optimize_list

    def validate(self):
        if self.enable_auto_resource_optimize_list:
            for k in self.enable_auto_resource_optimize_list:
                if k:
                    k.validate()
        if self.has_enable_rule_but_not_das_pro_list:
            for k in self.has_enable_rule_but_not_das_pro_list:
                if k:
                    k.validate()
        if self.turn_off_auto_resource_optimize_list:
            for k in self.turn_off_auto_resource_optimize_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_auto_resource_optimize_count is not None:
            result['EnableAutoResourceOptimizeCount'] = self.enable_auto_resource_optimize_count
        result['EnableAutoResourceOptimizeList'] = []
        if self.enable_auto_resource_optimize_list is not None:
            for k in self.enable_auto_resource_optimize_list:
                result['EnableAutoResourceOptimizeList'].append(k.to_map() if k else None)
        if self.has_enable_rule_but_not_das_pro_count is not None:
            result['HasEnableRuleButNotDasProCount'] = self.has_enable_rule_but_not_das_pro_count
        result['HasEnableRuleButNotDasProList'] = []
        if self.has_enable_rule_but_not_das_pro_list is not None:
            for k in self.has_enable_rule_but_not_das_pro_list:
                result['HasEnableRuleButNotDasProList'].append(k.to_map() if k else None)
        if self.never_enable_auto_resource_optimize_or_released_instance_count is not None:
            result['NeverEnableAutoResourceOptimizeOrReleasedInstanceCount'] = self.never_enable_auto_resource_optimize_or_released_instance_count
        if self.never_enable_auto_resource_optimize_or_released_instance_id_list is not None:
            result['NeverEnableAutoResourceOptimizeOrReleasedInstanceIdList'] = self.never_enable_auto_resource_optimize_or_released_instance_id_list
        if self.total_auto_resource_optimize_rules_count is not None:
            result['TotalAutoResourceOptimizeRulesCount'] = self.total_auto_resource_optimize_rules_count
        if self.turn_off_auto_resource_optimize_count is not None:
            result['TurnOffAutoResourceOptimizeCount'] = self.turn_off_auto_resource_optimize_count
        result['TurnOffAutoResourceOptimizeList'] = []
        if self.turn_off_auto_resource_optimize_list is not None:
            for k in self.turn_off_auto_resource_optimize_list:
                result['TurnOffAutoResourceOptimizeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutoResourceOptimizeCount') is not None:
            self.enable_auto_resource_optimize_count = m.get('EnableAutoResourceOptimizeCount')
        self.enable_auto_resource_optimize_list = []
        if m.get('EnableAutoResourceOptimizeList') is not None:
            for k in m.get('EnableAutoResourceOptimizeList'):
                temp_model = GetAutoResourceOptimizeRulesResponseBodyDataEnableAutoResourceOptimizeList()
                self.enable_auto_resource_optimize_list.append(temp_model.from_map(k))
        if m.get('HasEnableRuleButNotDasProCount') is not None:
            self.has_enable_rule_but_not_das_pro_count = m.get('HasEnableRuleButNotDasProCount')
        self.has_enable_rule_but_not_das_pro_list = []
        if m.get('HasEnableRuleButNotDasProList') is not None:
            for k in m.get('HasEnableRuleButNotDasProList'):
                temp_model = GetAutoResourceOptimizeRulesResponseBodyDataHasEnableRuleButNotDasProList()
                self.has_enable_rule_but_not_das_pro_list.append(temp_model.from_map(k))
        if m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceCount') is not None:
            self.never_enable_auto_resource_optimize_or_released_instance_count = m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceCount')
        if m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceIdList') is not None:
            self.never_enable_auto_resource_optimize_or_released_instance_id_list = m.get('NeverEnableAutoResourceOptimizeOrReleasedInstanceIdList')
        if m.get('TotalAutoResourceOptimizeRulesCount') is not None:
            self.total_auto_resource_optimize_rules_count = m.get('TotalAutoResourceOptimizeRulesCount')
        if m.get('TurnOffAutoResourceOptimizeCount') is not None:
            self.turn_off_auto_resource_optimize_count = m.get('TurnOffAutoResourceOptimizeCount')
        self.turn_off_auto_resource_optimize_list = []
        if m.get('TurnOffAutoResourceOptimizeList') is not None:
            for k in m.get('TurnOffAutoResourceOptimizeList'):
                temp_model = GetAutoResourceOptimizeRulesResponseBodyDataTurnOffAutoResourceOptimizeList()
                self.turn_off_auto_resource_optimize_list.append(temp_model.from_map(k))
        return self


class GetAutoResourceOptimizeRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAutoResourceOptimizeRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetAutoResourceOptimizeRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutoResourceOptimizeRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoResourceOptimizeRulesResponseBody = None,
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
            temp_model = GetAutoResourceOptimizeRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoThrottleRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_ids: str = None,
    ):
        self.console_context = console_context
        self.instance_ids = instance_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class GetAutoThrottleRulesResponseBodyDataEnableAutoThrottleList(TeaModel):
    def __init__(
        self,
        abnormal_duration: float = None,
        active_sessions: int = None,
        allow_throttle_end_time: str = None,
        allow_throttle_start_time: str = None,
        auto_kill_session: bool = None,
        cpu_session_relation: str = None,
        cpu_usage: float = None,
        instance_id: str = None,
        max_throttle_time: float = None,
        user_id: str = None,
        visible: bool = None,
    ):
        self.abnormal_duration = abnormal_duration
        self.active_sessions = active_sessions
        self.allow_throttle_end_time = allow_throttle_end_time
        self.allow_throttle_start_time = allow_throttle_start_time
        self.auto_kill_session = auto_kill_session
        self.cpu_session_relation = cpu_session_relation
        self.cpu_usage = cpu_usage
        self.instance_id = instance_id
        self.max_throttle_time = max_throttle_time
        self.user_id = user_id
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_duration is not None:
            result['AbnormalDuration'] = self.abnormal_duration
        if self.active_sessions is not None:
            result['ActiveSessions'] = self.active_sessions
        if self.allow_throttle_end_time is not None:
            result['AllowThrottleEndTime'] = self.allow_throttle_end_time
        if self.allow_throttle_start_time is not None:
            result['AllowThrottleStartTime'] = self.allow_throttle_start_time
        if self.auto_kill_session is not None:
            result['AutoKillSession'] = self.auto_kill_session
        if self.cpu_session_relation is not None:
            result['CpuSessionRelation'] = self.cpu_session_relation
        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_throttle_time is not None:
            result['MaxThrottleTime'] = self.max_throttle_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalDuration') is not None:
            self.abnormal_duration = m.get('AbnormalDuration')
        if m.get('ActiveSessions') is not None:
            self.active_sessions = m.get('ActiveSessions')
        if m.get('AllowThrottleEndTime') is not None:
            self.allow_throttle_end_time = m.get('AllowThrottleEndTime')
        if m.get('AllowThrottleStartTime') is not None:
            self.allow_throttle_start_time = m.get('AllowThrottleStartTime')
        if m.get('AutoKillSession') is not None:
            self.auto_kill_session = m.get('AutoKillSession')
        if m.get('CpuSessionRelation') is not None:
            self.cpu_session_relation = m.get('CpuSessionRelation')
        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxThrottleTime') is not None:
            self.max_throttle_time = m.get('MaxThrottleTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class GetAutoThrottleRulesResponseBodyDataTurnOffAutoThrottleList(TeaModel):
    def __init__(
        self,
        abnormal_duration: float = None,
        active_sessions: int = None,
        allow_throttle_end_time: str = None,
        allow_throttle_start_time: str = None,
        auto_kill_session: bool = None,
        cpu_session_relation: str = None,
        cpu_usage: float = None,
        instance_id: str = None,
        max_throttle_time: float = None,
        user_id: str = None,
        visible: bool = None,
    ):
        self.abnormal_duration = abnormal_duration
        self.active_sessions = active_sessions
        self.allow_throttle_end_time = allow_throttle_end_time
        self.allow_throttle_start_time = allow_throttle_start_time
        self.auto_kill_session = auto_kill_session
        self.cpu_session_relation = cpu_session_relation
        self.cpu_usage = cpu_usage
        self.instance_id = instance_id
        self.max_throttle_time = max_throttle_time
        self.user_id = user_id
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_duration is not None:
            result['AbnormalDuration'] = self.abnormal_duration
        if self.active_sessions is not None:
            result['ActiveSessions'] = self.active_sessions
        if self.allow_throttle_end_time is not None:
            result['AllowThrottleEndTime'] = self.allow_throttle_end_time
        if self.allow_throttle_start_time is not None:
            result['AllowThrottleStartTime'] = self.allow_throttle_start_time
        if self.auto_kill_session is not None:
            result['AutoKillSession'] = self.auto_kill_session
        if self.cpu_session_relation is not None:
            result['CpuSessionRelation'] = self.cpu_session_relation
        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_throttle_time is not None:
            result['MaxThrottleTime'] = self.max_throttle_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalDuration') is not None:
            self.abnormal_duration = m.get('AbnormalDuration')
        if m.get('ActiveSessions') is not None:
            self.active_sessions = m.get('ActiveSessions')
        if m.get('AllowThrottleEndTime') is not None:
            self.allow_throttle_end_time = m.get('AllowThrottleEndTime')
        if m.get('AllowThrottleStartTime') is not None:
            self.allow_throttle_start_time = m.get('AllowThrottleStartTime')
        if m.get('AutoKillSession') is not None:
            self.auto_kill_session = m.get('AutoKillSession')
        if m.get('CpuSessionRelation') is not None:
            self.cpu_session_relation = m.get('CpuSessionRelation')
        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxThrottleTime') is not None:
            self.max_throttle_time = m.get('MaxThrottleTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class GetAutoThrottleRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        enable_auto_throttle_count: int = None,
        enable_auto_throttle_list: List[GetAutoThrottleRulesResponseBodyDataEnableAutoThrottleList] = None,
        never_enable_auto_throttle_or_released_instance_count: int = None,
        never_enable_auto_throttle_or_released_instance_id_list: List[str] = None,
        total_auto_throttle_rules_count: int = None,
        turn_off_auto_throttle_count: int = None,
        turn_off_auto_throttle_list: List[GetAutoThrottleRulesResponseBodyDataTurnOffAutoThrottleList] = None,
    ):
        self.enable_auto_throttle_count = enable_auto_throttle_count
        self.enable_auto_throttle_list = enable_auto_throttle_list
        self.never_enable_auto_throttle_or_released_instance_count = never_enable_auto_throttle_or_released_instance_count
        self.never_enable_auto_throttle_or_released_instance_id_list = never_enable_auto_throttle_or_released_instance_id_list
        self.total_auto_throttle_rules_count = total_auto_throttle_rules_count
        self.turn_off_auto_throttle_count = turn_off_auto_throttle_count
        self.turn_off_auto_throttle_list = turn_off_auto_throttle_list

    def validate(self):
        if self.enable_auto_throttle_list:
            for k in self.enable_auto_throttle_list:
                if k:
                    k.validate()
        if self.turn_off_auto_throttle_list:
            for k in self.turn_off_auto_throttle_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_auto_throttle_count is not None:
            result['EnableAutoThrottleCount'] = self.enable_auto_throttle_count
        result['EnableAutoThrottleList'] = []
        if self.enable_auto_throttle_list is not None:
            for k in self.enable_auto_throttle_list:
                result['EnableAutoThrottleList'].append(k.to_map() if k else None)
        if self.never_enable_auto_throttle_or_released_instance_count is not None:
            result['NeverEnableAutoThrottleOrReleasedInstanceCount'] = self.never_enable_auto_throttle_or_released_instance_count
        if self.never_enable_auto_throttle_or_released_instance_id_list is not None:
            result['NeverEnableAutoThrottleOrReleasedInstanceIdList'] = self.never_enable_auto_throttle_or_released_instance_id_list
        if self.total_auto_throttle_rules_count is not None:
            result['TotalAutoThrottleRulesCount'] = self.total_auto_throttle_rules_count
        if self.turn_off_auto_throttle_count is not None:
            result['TurnOffAutoThrottleCount'] = self.turn_off_auto_throttle_count
        result['TurnOffAutoThrottleList'] = []
        if self.turn_off_auto_throttle_list is not None:
            for k in self.turn_off_auto_throttle_list:
                result['TurnOffAutoThrottleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutoThrottleCount') is not None:
            self.enable_auto_throttle_count = m.get('EnableAutoThrottleCount')
        self.enable_auto_throttle_list = []
        if m.get('EnableAutoThrottleList') is not None:
            for k in m.get('EnableAutoThrottleList'):
                temp_model = GetAutoThrottleRulesResponseBodyDataEnableAutoThrottleList()
                self.enable_auto_throttle_list.append(temp_model.from_map(k))
        if m.get('NeverEnableAutoThrottleOrReleasedInstanceCount') is not None:
            self.never_enable_auto_throttle_or_released_instance_count = m.get('NeverEnableAutoThrottleOrReleasedInstanceCount')
        if m.get('NeverEnableAutoThrottleOrReleasedInstanceIdList') is not None:
            self.never_enable_auto_throttle_or_released_instance_id_list = m.get('NeverEnableAutoThrottleOrReleasedInstanceIdList')
        if m.get('TotalAutoThrottleRulesCount') is not None:
            self.total_auto_throttle_rules_count = m.get('TotalAutoThrottleRulesCount')
        if m.get('TurnOffAutoThrottleCount') is not None:
            self.turn_off_auto_throttle_count = m.get('TurnOffAutoThrottleCount')
        self.turn_off_auto_throttle_list = []
        if m.get('TurnOffAutoThrottleList') is not None:
            for k in m.get('TurnOffAutoThrottleList'):
                temp_model = GetAutoThrottleRulesResponseBodyDataTurnOffAutoThrottleList()
                self.turn_off_auto_throttle_list.append(temp_model.from_map(k))
        return self


class GetAutoThrottleRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAutoThrottleRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetAutoThrottleRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutoThrottleRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutoThrottleRulesResponseBody = None,
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
            temp_model = GetAutoThrottleRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventContentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        span_id: str = None,
        context: str = None,
    ):
        self.instance_id = instance_id
        self.span_id = span_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class GetAutonomousNotifyEventContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutonomousNotifyEventContentResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventsInRangeRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        event_context: str = None,
        instance_id: str = None,
        level: str = None,
        min_level: str = None,
        node_id: str = None,
        page_offset: str = None,
        page_size: str = None,
        start_time: str = None,
        context: str = None,
    ):
        self.end_time = end_time
        self.event_context = event_context
        self.instance_id = instance_id
        self.level = level
        self.min_level = min_level
        self.node_id = node_id
        self.page_offset = page_offset
        self.page_size = page_size
        self.start_time = start_time
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.level is not None:
            result['Level'] = self.level
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageOffset') is not None:
            self.page_offset = m.get('PageOffset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutonomousNotifyEventsInRangeResponseBodyDataList(TeaModel):
    def __init__(
        self,
        t: List[str] = None,
    ):
        self.t = t

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.t is not None:
            result['T'] = self.t
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('T') is not None:
            self.t = m.get('T')
        return self


class GetAutonomousNotifyEventsInRangeResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: GetAutonomousNotifyEventsInRangeResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('List') is not None:
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAutonomousNotifyEventsInRangeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetAutonomousNotifyEventsInRangeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventsInRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAutonomousNotifyEventsInRangeResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventsInRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDasProServiceUsageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_id: str = None,
    ):
        self.instance_id = instance_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetDasProServiceUsageResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_instance_id: str = None,
        custins_id: int = None,
        engine: str = None,
        expire_time: int = None,
        instance_alias: str = None,
        instance_id: str = None,
        ip: str = None,
        is_spare: bool = None,
        port: int = None,
        region: str = None,
        service_unit_id: str = None,
        sql_retention: str = None,
        start_time: int = None,
        storage_free_quota_in_mb: float = None,
        storage_used: int = None,
        user_id: str = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        self.commodity_instance_id = commodity_instance_id
        self.custins_id = custins_id
        self.engine = engine
        self.expire_time = expire_time
        self.instance_alias = instance_alias
        self.instance_id = instance_id
        self.ip = ip
        self.is_spare = is_spare
        self.port = port
        self.region = region
        self.service_unit_id = service_unit_id
        self.sql_retention = sql_retention
        self.start_time = start_time
        self.storage_free_quota_in_mb = storage_free_quota_in_mb
        self.storage_used = storage_used
        self.user_id = user_id
        self.uuid = uuid
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_instance_id is not None:
            result['commodityInstanceId'] = self.commodity_instance_id
        if self.custins_id is not None:
            result['custinsId'] = self.custins_id
        if self.engine is not None:
            result['engine'] = self.engine
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.instance_alias is not None:
            result['instanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.ip is not None:
            result['ip'] = self.ip
        if self.is_spare is not None:
            result['isSpare'] = self.is_spare
        if self.port is not None:
            result['port'] = self.port
        if self.region is not None:
            result['region'] = self.region
        if self.service_unit_id is not None:
            result['serviceUnitId'] = self.service_unit_id
        if self.sql_retention is not None:
            result['sqlRetention'] = self.sql_retention
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.storage_free_quota_in_mb is not None:
            result['storageFreeQuotaInMB'] = self.storage_free_quota_in_mb
        if self.storage_used is not None:
            result['storageUsed'] = self.storage_used
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commodityInstanceId') is not None:
            self.commodity_instance_id = m.get('commodityInstanceId')
        if m.get('custinsId') is not None:
            self.custins_id = m.get('custinsId')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('instanceAlias') is not None:
            self.instance_alias = m.get('instanceAlias')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('isSpare') is not None:
            self.is_spare = m.get('isSpare')
        if m.get('port') is not None:
            self.port = m.get('port')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('serviceUnitId') is not None:
            self.service_unit_id = m.get('serviceUnitId')
        if m.get('sqlRetention') is not None:
            self.sql_retention = m.get('sqlRetention')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('storageFreeQuotaInMB') is not None:
            self.storage_free_quota_in_mb = m.get('storageFreeQuotaInMB')
        if m.get('storageUsed') is not None:
            self.storage_used = m.get('storageUsed')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self


class GetDasProServiceUsageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetDasProServiceUsageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetDasProServiceUsageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDasProServiceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDasProServiceUsageResponseBody = None,
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
            temp_model = GetDasProServiceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEndpointSwitchTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.task_id = task_id
        self.uid = uid
        self.user_id = user_id
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetEndpointSwitchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        db_link_id: int = None,
        err_msg: str = None,
        ori_uuid: str = None,
        status: str = None,
        task_id: str = None,
        uuid: str = None,
    ):
        self.account_id = account_id
        self.db_link_id = db_link_id
        self.err_msg = err_msg
        self.ori_uuid = ori_uuid
        self.status = status
        self.task_id = task_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.db_link_id is not None:
            result['DbLinkId'] = self.db_link_id
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.ori_uuid is not None:
            result['OriUuid'] = self.ori_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DbLinkId') is not None:
            self.db_link_id = m.get('DbLinkId')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('OriUuid') is not None:
            self.ori_uuid = m.get('OriUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEndpointSwitchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEndpointSwitchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetEndpointSwitchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetEndpointSwitchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEndpointSwitchTaskResponseBody = None,
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
            temp_model = GetEndpointSwitchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErrorRequestSampleRequest(TeaModel):
    def __init__(
        self,
        db_name: str = None,
        end: int = None,
        instance_id: str = None,
        node_id: str = None,
        sql_id: str = None,
        start: int = None,
    ):
        self.db_name = db_name
        self.end = end
        self.instance_id = instance_id
        self.node_id = node_id
        self.sql_id = sql_id
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetErrorRequestSampleResponseBodyData(TeaModel):
    def __init__(
        self,
        database: str = None,
        error_code: str = None,
        instance_id: str = None,
        origin_host: str = None,
        sql: str = None,
        sql_id: str = None,
        tables: List[str] = None,
        timestamp: int = None,
        user: str = None,
    ):
        self.database = database
        self.error_code = error_code
        self.instance_id = instance_id
        self.origin_host = origin_host
        self.sql = sql
        # SQL ID。
        self.sql_id = sql_id
        self.tables = tables
        self.timestamp = timestamp
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database is not None:
            result['database'] = self.database
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.origin_host is not None:
            result['originHost'] = self.origin_host
        if self.sql is not None:
            result['sql'] = self.sql
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.tables is not None:
            result['tables'] = self.tables
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('originHost') is not None:
            self.origin_host = m.get('originHost')
        if m.get('sql') is not None:
            self.sql = m.get('sql')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('tables') is not None:
            self.tables = m.get('tables')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class GetErrorRequestSampleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetErrorRequestSampleResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetErrorRequestSampleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetErrorRequestSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErrorRequestSampleResponseBody = None,
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
            temp_model = GetErrorRequestSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventSubscriptionRequest(TeaModel):
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


class GetEventSubscriptionResponseBodyDataContactGroups(TeaModel):
    def __init__(
        self,
        contacts: str = None,
        description: str = None,
        name: str = None,
        user_id: str = None,
    ):
        self.contacts = contacts
        self.description = description
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contacts is not None:
            result['contacts'] = self.contacts
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetEventSubscriptionResponseBodyDataContacts(TeaModel):
    def __init__(
        self,
        dingtalk_hook: str = None,
        email: str = None,
        groups: List[str] = None,
        is_cms_reduplicated: bool = None,
        name: str = None,
        phone: str = None,
        user_id: str = None,
    ):
        self.dingtalk_hook = dingtalk_hook
        self.email = email
        self.groups = groups
        self.is_cms_reduplicated = is_cms_reduplicated
        self.name = name
        self.phone = phone
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dingtalk_hook is not None:
            result['dingtalkHook'] = self.dingtalk_hook
        if self.email is not None:
            result['email'] = self.email
        if self.groups is not None:
            result['groups'] = self.groups
        if self.is_cms_reduplicated is not None:
            result['isCmsReduplicated'] = self.is_cms_reduplicated
        if self.name is not None:
            result['name'] = self.name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dingtalkHook') is not None:
            self.dingtalk_hook = m.get('dingtalkHook')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('groups') is not None:
            self.groups = m.get('groups')
        if m.get('isCmsReduplicated') is not None:
            self.is_cms_reduplicated = m.get('isCmsReduplicated')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetEventSubscriptionResponseBodyData(TeaModel):
    def __init__(
        self,
        active: int = None,
        channel_type: str = None,
        contact_group_name: str = None,
        contact_groups: List[GetEventSubscriptionResponseBodyDataContactGroups] = None,
        contact_name: str = None,
        contacts: List[GetEventSubscriptionResponseBodyDataContacts] = None,
        event_context: str = None,
        event_send_group: List[str] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
        min_interval: str = None,
        user_id: str = None,
    ):
        self.active = active
        self.channel_type = channel_type
        self.contact_group_name = contact_group_name
        self.contact_groups = contact_groups
        self.contact_name = contact_name
        self.contacts = contacts
        self.event_context = event_context
        self.event_send_group = event_send_group
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.instance_id = instance_id
        self.lang = lang
        self.level = level
        self.min_interval = min_interval
        self.user_id = user_id

    def validate(self):
        if self.contact_groups:
            for k in self.contact_groups:
                if k:
                    k.validate()
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.channel_type is not None:
            result['channelType'] = self.channel_type
        if self.contact_group_name is not None:
            result['contactGroupName'] = self.contact_group_name
        result['contactGroups'] = []
        if self.contact_groups is not None:
            for k in self.contact_groups:
                result['contactGroups'].append(k.to_map() if k else None)
        if self.contact_name is not None:
            result['contactName'] = self.contact_name
        result['contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['contacts'].append(k.to_map() if k else None)
        if self.event_context is not None:
            result['eventContext'] = self.event_context
        if self.event_send_group is not None:
            result['eventSendGroup'] = self.event_send_group
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.id is not None:
            result['id'] = self.id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lang is not None:
            result['lang'] = self.lang
        if self.level is not None:
            result['level'] = self.level
        if self.min_interval is not None:
            result['minInterval'] = self.min_interval
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')
        if m.get('contactGroupName') is not None:
            self.contact_group_name = m.get('contactGroupName')
        self.contact_groups = []
        if m.get('contactGroups') is not None:
            for k in m.get('contactGroups'):
                temp_model = GetEventSubscriptionResponseBodyDataContactGroups()
                self.contact_groups.append(temp_model.from_map(k))
        if m.get('contactName') is not None:
            self.contact_name = m.get('contactName')
        self.contacts = []
        if m.get('contacts') is not None:
            for k in m.get('contacts'):
                temp_model = GetEventSubscriptionResponseBodyDataContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('eventContext') is not None:
            self.event_context = m.get('eventContext')
        if m.get('eventSendGroup') is not None:
            self.event_send_group = m.get('eventSendGroup')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('minInterval') is not None:
            self.min_interval = m.get('minInterval')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class GetEventSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetEventSubscriptionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetEventSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEventSubscriptionResponseBody = None,
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
            temp_model = GetEventSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFullRequestOriginStatByInstanceIdRequest(TeaModel):
    def __init__(
        self,
        asc: bool = None,
        end: int = None,
        instance_id: str = None,
        node_id: str = None,
        order_by: str = None,
        page_no: int = None,
        page_size: int = None,
        role: str = None,
        sql_type: str = None,
        start: int = None,
        user_id: str = None,
    ):
        self.asc = asc
        self.end = end
        self.instance_id = instance_id
        self.node_id = node_id
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.role = role
        self.sql_type = sql_type
        self.start = start
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['Asc'] = self.asc
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role is not None:
            result['Role'] = self.role
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start is not None:
            result['Start'] = self.start
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetFullRequestOriginStatByInstanceIdResponseBodyDataList(TeaModel):
    def __init__(
        self,
        avg_examined_rows: float = None,
        avg_fetch_rows: int = None,
        avg_lock_wait_time: float = None,
        avg_logical_read: float = None,
        avg_physical_async_read: int = None,
        avg_physical_sync_read: float = None,
        avg_returned_rows: float = None,
        avg_rows: int = None,
        avg_rt: float = None,
        avg_sql_count: int = None,
        avg_updated_rows: float = None,
        count: int = None,
        count_rate: float = None,
        database: str = None,
        error_count: int = None,
        examined_rows: int = None,
        fetch_rows: int = None,
        ip: str = None,
        key: str = None,
        lock_wait_time: float = None,
        logical_read: int = None,
        origin_host: str = None,
        physical_async_read: int = None,
        physical_sync_read: int = None,
        port: int = None,
        rows: int = None,
        rt_greater_than_one_second_count: int = None,
        rt_rate: float = None,
        sql_count: int = None,
        sum_updated_rows: int = None,
        version: int = None,
        vpc_id: str = None,
    ):
        self.avg_examined_rows = avg_examined_rows
        self.avg_fetch_rows = avg_fetch_rows
        self.avg_lock_wait_time = avg_lock_wait_time
        self.avg_logical_read = avg_logical_read
        self.avg_physical_async_read = avg_physical_async_read
        self.avg_physical_sync_read = avg_physical_sync_read
        self.avg_returned_rows = avg_returned_rows
        self.avg_rows = avg_rows
        self.avg_rt = avg_rt
        self.avg_sql_count = avg_sql_count
        self.avg_updated_rows = avg_updated_rows
        self.count = count
        self.count_rate = count_rate
        self.database = database
        self.error_count = error_count
        self.examined_rows = examined_rows
        self.fetch_rows = fetch_rows
        self.ip = ip
        self.key = key
        self.lock_wait_time = lock_wait_time
        self.logical_read = logical_read
        self.origin_host = origin_host
        self.physical_async_read = physical_async_read
        self.physical_sync_read = physical_sync_read
        self.port = port
        self.rows = rows
        self.rt_greater_than_one_second_count = rt_greater_than_one_second_count
        self.rt_rate = rt_rate
        self.sql_count = sql_count
        self.sum_updated_rows = sum_updated_rows
        self.version = version
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_examined_rows is not None:
            result['AvgExaminedRows'] = self.avg_examined_rows
        if self.avg_fetch_rows is not None:
            result['AvgFetchRows'] = self.avg_fetch_rows
        if self.avg_lock_wait_time is not None:
            result['AvgLockWaitTime'] = self.avg_lock_wait_time
        if self.avg_logical_read is not None:
            result['AvgLogicalRead'] = self.avg_logical_read
        if self.avg_physical_async_read is not None:
            result['AvgPhysicalAsyncRead'] = self.avg_physical_async_read
        if self.avg_physical_sync_read is not None:
            result['AvgPhysicalSyncRead'] = self.avg_physical_sync_read
        if self.avg_returned_rows is not None:
            result['AvgReturnedRows'] = self.avg_returned_rows
        if self.avg_rows is not None:
            result['AvgRows'] = self.avg_rows
        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt
        if self.avg_sql_count is not None:
            result['AvgSqlCount'] = self.avg_sql_count
        if self.avg_updated_rows is not None:
            result['AvgUpdatedRows'] = self.avg_updated_rows
        if self.count is not None:
            result['Count'] = self.count
        if self.count_rate is not None:
            result['CountRate'] = self.count_rate
        if self.database is not None:
            result['Database'] = self.database
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.examined_rows is not None:
            result['ExaminedRows'] = self.examined_rows
        if self.fetch_rows is not None:
            result['FetchRows'] = self.fetch_rows
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.key is not None:
            result['Key'] = self.key
        if self.lock_wait_time is not None:
            result['LockWaitTime'] = self.lock_wait_time
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host
        if self.physical_async_read is not None:
            result['PhysicalAsyncRead'] = self.physical_async_read
        if self.physical_sync_read is not None:
            result['PhysicalSyncRead'] = self.physical_sync_read
        if self.port is not None:
            result['Port'] = self.port
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.rt_greater_than_one_second_count is not None:
            result['RtGreaterThanOneSecondCount'] = self.rt_greater_than_one_second_count
        if self.rt_rate is not None:
            result['RtRate'] = self.rt_rate
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.sum_updated_rows is not None:
            result['SumUpdatedRows'] = self.sum_updated_rows
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgExaminedRows') is not None:
            self.avg_examined_rows = m.get('AvgExaminedRows')
        if m.get('AvgFetchRows') is not None:
            self.avg_fetch_rows = m.get('AvgFetchRows')
        if m.get('AvgLockWaitTime') is not None:
            self.avg_lock_wait_time = m.get('AvgLockWaitTime')
        if m.get('AvgLogicalRead') is not None:
            self.avg_logical_read = m.get('AvgLogicalRead')
        if m.get('AvgPhysicalAsyncRead') is not None:
            self.avg_physical_async_read = m.get('AvgPhysicalAsyncRead')
        if m.get('AvgPhysicalSyncRead') is not None:
            self.avg_physical_sync_read = m.get('AvgPhysicalSyncRead')
        if m.get('AvgReturnedRows') is not None:
            self.avg_returned_rows = m.get('AvgReturnedRows')
        if m.get('AvgRows') is not None:
            self.avg_rows = m.get('AvgRows')
        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')
        if m.get('AvgSqlCount') is not None:
            self.avg_sql_count = m.get('AvgSqlCount')
        if m.get('AvgUpdatedRows') is not None:
            self.avg_updated_rows = m.get('AvgUpdatedRows')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CountRate') is not None:
            self.count_rate = m.get('CountRate')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('ExaminedRows') is not None:
            self.examined_rows = m.get('ExaminedRows')
        if m.get('FetchRows') is not None:
            self.fetch_rows = m.get('FetchRows')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('LockWaitTime') is not None:
            self.lock_wait_time = m.get('LockWaitTime')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')
        if m.get('PhysicalAsyncRead') is not None:
            self.physical_async_read = m.get('PhysicalAsyncRead')
        if m.get('PhysicalSyncRead') is not None:
            self.physical_sync_read = m.get('PhysicalSyncRead')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('RtGreaterThanOneSecondCount') is not None:
            self.rt_greater_than_one_second_count = m.get('RtGreaterThanOneSecondCount')
        if m.get('RtRate') is not None:
            self.rt_rate = m.get('RtRate')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('SumUpdatedRows') is not None:
            self.sum_updated_rows = m.get('SumUpdatedRows')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetFullRequestOriginStatByInstanceIdResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetFullRequestOriginStatByInstanceIdResponseBodyDataList] = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetFullRequestOriginStatByInstanceIdResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetFullRequestOriginStatByInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetFullRequestOriginStatByInstanceIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetFullRequestOriginStatByInstanceIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFullRequestOriginStatByInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFullRequestOriginStatByInstanceIdResponseBody = None,
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
            temp_model = GetFullRequestOriginStatByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFullRequestSampleByInstanceIdRequest(TeaModel):
    def __init__(
        self,
        end: int = None,
        instance_id: str = None,
        role: str = None,
        sql_id: str = None,
        start: int = None,
        user_id: str = None,
    ):
        self.end = end
        self.instance_id = instance_id
        self.role = role
        # SQL ID。
        self.sql_id = sql_id
        self.start = start
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.role is not None:
            result['Role'] = self.role
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.start is not None:
            result['Start'] = self.start
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetFullRequestSampleByInstanceIdResponseBodyData(TeaModel):
    def __init__(
        self,
        database: str = None,
        frows: int = None,
        lock_wait_time: float = None,
        logical_read: float = None,
        origin_host: str = None,
        physical_async_read: float = None,
        physical_sync_read: float = None,
        rows: int = None,
        rows_examined: int = None,
        rows_returned: int = None,
        rt: float = None,
        scan_rows: int = None,
        scnt: int = None,
        sql: str = None,
        sql_id: str = None,
        sql_type: str = None,
        timestamp: int = None,
        update_rows: int = None,
        user: str = None,
    ):
        self.database = database
        self.frows = frows
        self.lock_wait_time = lock_wait_time
        self.logical_read = logical_read
        self.origin_host = origin_host
        self.physical_async_read = physical_async_read
        self.physical_sync_read = physical_sync_read
        self.rows = rows
        self.rows_examined = rows_examined
        self.rows_returned = rows_returned
        self.rt = rt
        self.scan_rows = scan_rows
        self.scnt = scnt
        self.sql = sql
        # SQL ID。
        self.sql_id = sql_id
        self.sql_type = sql_type
        self.timestamp = timestamp
        self.update_rows = update_rows
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
        if self.frows is not None:
            result['Frows'] = self.frows
        if self.lock_wait_time is not None:
            result['LockWaitTime'] = self.lock_wait_time
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host
        if self.physical_async_read is not None:
            result['PhysicalAsyncRead'] = self.physical_async_read
        if self.physical_sync_read is not None:
            result['PhysicalSyncRead'] = self.physical_sync_read
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.rows_examined is not None:
            result['RowsExamined'] = self.rows_examined
        if self.rows_returned is not None:
            result['RowsReturned'] = self.rows_returned
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.scan_rows is not None:
            result['ScanRows'] = self.scan_rows
        if self.scnt is not None:
            result['Scnt'] = self.scnt
        if self.sql is not None:
            result['Sql'] = self.sql
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.update_rows is not None:
            result['UpdateRows'] = self.update_rows
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('Frows') is not None:
            self.frows = m.get('Frows')
        if m.get('LockWaitTime') is not None:
            self.lock_wait_time = m.get('LockWaitTime')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')
        if m.get('PhysicalAsyncRead') is not None:
            self.physical_async_read = m.get('PhysicalAsyncRead')
        if m.get('PhysicalSyncRead') is not None:
            self.physical_sync_read = m.get('PhysicalSyncRead')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('RowsExamined') is not None:
            self.rows_examined = m.get('RowsExamined')
        if m.get('RowsReturned') is not None:
            self.rows_returned = m.get('RowsReturned')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('ScanRows') is not None:
            self.scan_rows = m.get('ScanRows')
        if m.get('Scnt') is not None:
            self.scnt = m.get('Scnt')
        if m.get('Sql') is not None:
            self.sql = m.get('Sql')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('UpdateRows') is not None:
            self.update_rows = m.get('UpdateRows')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class GetFullRequestSampleByInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetFullRequestSampleByInstanceIdResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetFullRequestSampleByInstanceIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFullRequestSampleByInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFullRequestSampleByInstanceIdResponseBody = None,
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
            temp_model = GetFullRequestSampleByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFullRequestStatResultByInstanceIdRequest(TeaModel):
    def __init__(
        self,
        asc: bool = None,
        db_name: str = None,
        end: int = None,
        instance_id: str = None,
        keyword: str = None,
        node_id: str = None,
        order_by: str = None,
        origin_host: str = None,
        page_no: int = None,
        page_size: int = None,
        role: str = None,
        sql_id: str = None,
        sql_type: str = None,
        start: int = None,
        user_id: str = None,
    ):
        self.asc = asc
        self.db_name = db_name
        self.end = end
        self.instance_id = instance_id
        self.keyword = keyword
        self.node_id = node_id
        self.order_by = order_by
        self.origin_host = origin_host
        self.page_no = page_no
        self.page_size = page_size
        self.role = role
        self.sql_id = sql_id
        self.sql_type = sql_type
        self.start = start
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['Asc'] = self.asc
        if self.db_name is not None:
            result['DbName'] = self.db_name
        if self.end is not None:
            result['End'] = self.end
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.origin_host is not None:
            result['OriginHost'] = self.origin_host
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.role is not None:
            result['Role'] = self.role
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start is not None:
            result['Start'] = self.start
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OriginHost') is not None:
            self.origin_host = m.get('OriginHost')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetFullRequestStatResultByInstanceIdResponseBodyDataResultList(TeaModel):
    def __init__(
        self,
        avg_examined_rows: float = None,
        avg_fetch_rows: int = None,
        avg_lock_wait_time: float = None,
        avg_logical_read: float = None,
        avg_physical_async_read: int = None,
        avg_physical_sync_read: int = None,
        avg_returned_rows: float = None,
        avg_rt: float = None,
        avg_sql_count: int = None,
        avg_updated_rows: int = None,
        count: int = None,
        count_rate: float = None,
        database: str = None,
        error_count: int = None,
        examined_rows: int = None,
        fetch_rows: int = None,
        ip: str = None,
        lock_wait_time: float = None,
        logical_read: int = None,
        physical_async_read: int = None,
        physical_sync_read: int = None,
        port: int = None,
        psql: str = None,
        rows: int = None,
        rt_greater_than_one_second_count: int = None,
        rt_rate: float = None,
        sql_count: int = None,
        sql_id: str = None,
        sum_updated_rows: int = None,
        tables: List[str] = None,
        version: int = None,
        vpc_id: str = None,
    ):
        self.avg_examined_rows = avg_examined_rows
        self.avg_fetch_rows = avg_fetch_rows
        self.avg_lock_wait_time = avg_lock_wait_time
        self.avg_logical_read = avg_logical_read
        self.avg_physical_async_read = avg_physical_async_read
        self.avg_physical_sync_read = avg_physical_sync_read
        self.avg_returned_rows = avg_returned_rows
        self.avg_rt = avg_rt
        self.avg_sql_count = avg_sql_count
        self.avg_updated_rows = avg_updated_rows
        self.count = count
        self.count_rate = count_rate
        self.database = database
        self.error_count = error_count
        self.examined_rows = examined_rows
        self.fetch_rows = fetch_rows
        self.ip = ip
        self.lock_wait_time = lock_wait_time
        self.logical_read = logical_read
        self.physical_async_read = physical_async_read
        self.physical_sync_read = physical_sync_read
        self.port = port
        self.psql = psql
        self.rows = rows
        self.rt_greater_than_one_second_count = rt_greater_than_one_second_count
        self.rt_rate = rt_rate
        self.sql_count = sql_count
        # SQL ID。
        self.sql_id = sql_id
        self.sum_updated_rows = sum_updated_rows
        self.tables = tables
        self.version = version
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_examined_rows is not None:
            result['AvgExaminedRows'] = self.avg_examined_rows
        if self.avg_fetch_rows is not None:
            result['AvgFetchRows'] = self.avg_fetch_rows
        if self.avg_lock_wait_time is not None:
            result['AvgLockWaitTime'] = self.avg_lock_wait_time
        if self.avg_logical_read is not None:
            result['AvgLogicalRead'] = self.avg_logical_read
        if self.avg_physical_async_read is not None:
            result['AvgPhysicalAsyncRead'] = self.avg_physical_async_read
        if self.avg_physical_sync_read is not None:
            result['AvgPhysicalSyncRead'] = self.avg_physical_sync_read
        if self.avg_returned_rows is not None:
            result['AvgReturnedRows'] = self.avg_returned_rows
        if self.avg_rt is not None:
            result['AvgRt'] = self.avg_rt
        if self.avg_sql_count is not None:
            result['AvgSqlCount'] = self.avg_sql_count
        if self.avg_updated_rows is not None:
            result['AvgUpdatedRows'] = self.avg_updated_rows
        if self.count is not None:
            result['Count'] = self.count
        if self.count_rate is not None:
            result['CountRate'] = self.count_rate
        if self.database is not None:
            result['Database'] = self.database
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.examined_rows is not None:
            result['ExaminedRows'] = self.examined_rows
        if self.fetch_rows is not None:
            result['FetchRows'] = self.fetch_rows
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.lock_wait_time is not None:
            result['LockWaitTime'] = self.lock_wait_time
        if self.logical_read is not None:
            result['LogicalRead'] = self.logical_read
        if self.physical_async_read is not None:
            result['PhysicalAsyncRead'] = self.physical_async_read
        if self.physical_sync_read is not None:
            result['PhysicalSyncRead'] = self.physical_sync_read
        if self.port is not None:
            result['Port'] = self.port
        if self.psql is not None:
            result['Psql'] = self.psql
        if self.rows is not None:
            result['Rows'] = self.rows
        if self.rt_greater_than_one_second_count is not None:
            result['RtGreaterThanOneSecondCount'] = self.rt_greater_than_one_second_count
        if self.rt_rate is not None:
            result['RtRate'] = self.rt_rate
        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sum_updated_rows is not None:
            result['SumUpdatedRows'] = self.sum_updated_rows
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.version is not None:
            result['Version'] = self.version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgExaminedRows') is not None:
            self.avg_examined_rows = m.get('AvgExaminedRows')
        if m.get('AvgFetchRows') is not None:
            self.avg_fetch_rows = m.get('AvgFetchRows')
        if m.get('AvgLockWaitTime') is not None:
            self.avg_lock_wait_time = m.get('AvgLockWaitTime')
        if m.get('AvgLogicalRead') is not None:
            self.avg_logical_read = m.get('AvgLogicalRead')
        if m.get('AvgPhysicalAsyncRead') is not None:
            self.avg_physical_async_read = m.get('AvgPhysicalAsyncRead')
        if m.get('AvgPhysicalSyncRead') is not None:
            self.avg_physical_sync_read = m.get('AvgPhysicalSyncRead')
        if m.get('AvgReturnedRows') is not None:
            self.avg_returned_rows = m.get('AvgReturnedRows')
        if m.get('AvgRt') is not None:
            self.avg_rt = m.get('AvgRt')
        if m.get('AvgSqlCount') is not None:
            self.avg_sql_count = m.get('AvgSqlCount')
        if m.get('AvgUpdatedRows') is not None:
            self.avg_updated_rows = m.get('AvgUpdatedRows')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CountRate') is not None:
            self.count_rate = m.get('CountRate')
        if m.get('Database') is not None:
            self.database = m.get('Database')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('ExaminedRows') is not None:
            self.examined_rows = m.get('ExaminedRows')
        if m.get('FetchRows') is not None:
            self.fetch_rows = m.get('FetchRows')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('LockWaitTime') is not None:
            self.lock_wait_time = m.get('LockWaitTime')
        if m.get('LogicalRead') is not None:
            self.logical_read = m.get('LogicalRead')
        if m.get('PhysicalAsyncRead') is not None:
            self.physical_async_read = m.get('PhysicalAsyncRead')
        if m.get('PhysicalSyncRead') is not None:
            self.physical_sync_read = m.get('PhysicalSyncRead')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Psql') is not None:
            self.psql = m.get('Psql')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        if m.get('RtGreaterThanOneSecondCount') is not None:
            self.rt_greater_than_one_second_count = m.get('RtGreaterThanOneSecondCount')
        if m.get('RtRate') is not None:
            self.rt_rate = m.get('RtRate')
        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SumUpdatedRows') is not None:
            self.sum_updated_rows = m.get('SumUpdatedRows')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetFullRequestStatResultByInstanceIdResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        list: List[GetFullRequestStatResultByInstanceIdResponseBodyDataResultList] = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetFullRequestStatResultByInstanceIdResponseBodyDataResultList()
                self.list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetFullRequestStatResultByInstanceIdResponseBodyData(TeaModel):
    def __init__(
        self,
        fail: bool = None,
        is_finish: bool = None,
        result: GetFullRequestStatResultByInstanceIdResponseBodyDataResult = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.fail = fail
        self.is_finish = is_finish
        self.result = result
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.result_id is not None:
            result['ResultId'] = self.result_id
        if self.state is not None:
            result['State'] = self.state
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')
        if m.get('Result') is not None:
            temp_model = GetFullRequestStatResultByInstanceIdResponseBodyDataResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetFullRequestStatResultByInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetFullRequestStatResultByInstanceIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetFullRequestStatResultByInstanceIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFullRequestStatResultByInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFullRequestStatResultByInstanceIdResponseBody = None,
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
            temp_model = GetFullRequestStatResultByInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMAliyunResourceSyncResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        uid: str = None,
        user_id: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.task_id = task_id
        self.uid = uid
        self.user_id = user_id
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(
        self,
        err_msg: str = None,
        resource_type: str = None,
        success: bool = None,
        sync_count: int = None,
    ):
        self.err_msg = err_msg
        self.resource_type = resource_type
        self.success = success
        self.sync_count = sync_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        return self


class GetHDMAliyunResourceSyncResultResponseBodyDataSubResults(TeaModel):
    def __init__(
        self,
        resource_sync_sub_result: List[GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult] = None,
    ):
        self.resource_sync_sub_result = resource_sync_sub_result

    def validate(self):
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_sync_sub_result = []
        if m.get('ResourceSyncSubResult') is not None:
            for k in m.get('ResourceSyncSubResult'):
                temp_model = GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMAliyunResourceSyncResultResponseBodyData(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        results: str = None,
        sub_results: GetHDMAliyunResourceSyncResultResponseBodyDataSubResults = None,
        sync_status: str = None,
    ):
        self.error_msg = error_msg
        self.results = results
        self.sub_results = sub_results
        self.sync_status = sync_status

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('SubResults') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        return self


class GetHDMAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHDMAliyunResourceSyncResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetHDMAliyunResourceSyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHDMAliyunResourceSyncResultResponseBody = None,
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
            temp_model = GetHDMAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMLastAliyunResourceSyncResultRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        user_id: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.uid = uid
        self.user_id = user_id
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(
        self,
        err_msg: str = None,
        resource_type: str = None,
        success: bool = None,
        sync_count: int = None,
    ):
        self.err_msg = err_msg
        self.resource_type = resource_type
        self.success = success
        self.sync_count = sync_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults(TeaModel):
    def __init__(
        self,
        resource_sync_sub_result: List[GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult] = None,
    ):
        self.resource_sync_sub_result = resource_sync_sub_result

    def validate(self):
        if self.resource_sync_sub_result:
            for k in self.resource_sync_sub_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceSyncSubResult'] = []
        if self.resource_sync_sub_result is not None:
            for k in self.resource_sync_sub_result:
                result['ResourceSyncSubResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_sync_sub_result = []
        if m.get('ResourceSyncSubResult') is not None:
            for k in m.get('ResourceSyncSubResult'):
                temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult()
                self.resource_sync_sub_result.append(temp_model.from_map(k))
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyData(TeaModel):
    def __init__(
        self,
        error_msg: str = None,
        results: str = None,
        sub_results: GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults = None,
        sync_status: str = None,
    ):
        self.error_msg = error_msg
        self.results = results
        self.sub_results = sub_results
        self.sync_status = sync_status

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.results is not None:
            result['Results'] = self.results
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('SubResults') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHDMLastAliyunResourceSyncResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class GetHDMLastAliyunResourceSyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHDMLastAliyunResourceSyncResultResponseBody = None,
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
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceInspectionsRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        engine: str = None,
        instance_area: str = None,
        page_no: str = None,
        page_size: str = None,
        resource_group_id: str = None,
        search_map: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.engine = engine
        self.instance_area = instance_area
        self.page_no = page_no
        self.page_size = page_size
        self.resource_group_id = resource_group_id
        self.search_map = search_map
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.search_map is not None:
            result['SearchMap'] = self.search_map
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SearchMap') is not None:
            self.search_map = m.get('SearchMap')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetInstanceInspectionsResponseBodyDataListAutoFunction(TeaModel):
    def __init__(
        self,
        auto_index: int = None,
        auto_limited_sql: int = None,
        auto_resource_optimize: int = None,
        auto_scale: int = None,
        event_subscription: int = None,
    ):
        self.auto_index = auto_index
        self.auto_limited_sql = auto_limited_sql
        self.auto_resource_optimize = auto_resource_optimize
        self.auto_scale = auto_scale
        self.event_subscription = event_subscription

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_index is not None:
            result['AutoIndex'] = self.auto_index
        if self.auto_limited_sql is not None:
            result['AutoLimitedSql'] = self.auto_limited_sql
        if self.auto_resource_optimize is not None:
            result['AutoResourceOptimize'] = self.auto_resource_optimize
        if self.auto_scale is not None:
            result['AutoScale'] = self.auto_scale
        if self.event_subscription is not None:
            result['EventSubscription'] = self.event_subscription
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIndex') is not None:
            self.auto_index = m.get('AutoIndex')
        if m.get('AutoLimitedSql') is not None:
            self.auto_limited_sql = m.get('AutoLimitedSql')
        if m.get('AutoResourceOptimize') is not None:
            self.auto_resource_optimize = m.get('AutoResourceOptimize')
        if m.get('AutoScale') is not None:
            self.auto_scale = m.get('AutoScale')
        if m.get('EventSubscription') is not None:
            self.event_subscription = m.get('EventSubscription')
        return self


class GetInstanceInspectionsResponseBodyDataListInstance(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        category: str = None,
        cpu: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_alias: str = None,
        instance_area: str = None,
        instance_class: str = None,
        instance_id: str = None,
        memory: int = None,
        network_type: str = None,
        node_id: str = None,
        region: str = None,
        storage: int = None,
        uuid: str = None,
        vpc_id: str = None,
    ):
        self.account_id = account_id
        self.category = category
        self.cpu = cpu
        self.engine = engine
        self.engine_version = engine_version
        self.instance_alias = instance_alias
        self.instance_area = instance_area
        self.instance_class = instance_class
        self.instance_id = instance_id
        self.memory = memory
        self.network_type = network_type
        self.node_id = node_id
        self.region = region
        self.storage = storage
        self.uuid = uuid
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.category is not None:
            result['Category'] = self.category
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.region is not None:
            result['Region'] = self.region
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetInstanceInspectionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        auto_function: GetInstanceInspectionsResponseBodyDataListAutoFunction = None,
        data: Dict[str, Any] = None,
        enable_das_pro: int = None,
        end_time: int = None,
        gmt_create: int = None,
        instance: GetInstanceInspectionsResponseBodyDataListInstance = None,
        score: int = None,
        score_map: Dict[str, Any] = None,
        start_time: int = None,
        state: int = None,
        task_type: int = None,
    ):
        self.auto_function = auto_function
        self.data = data
        self.enable_das_pro = enable_das_pro
        self.end_time = end_time
        self.gmt_create = gmt_create
        self.instance = instance
        self.score = score
        self.score_map = score_map
        self.start_time = start_time
        self.state = state
        self.task_type = task_type

    def validate(self):
        if self.auto_function:
            self.auto_function.validate()
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_function is not None:
            result['AutoFunction'] = self.auto_function.to_map()
        if self.data is not None:
            result['Data'] = self.data
        if self.enable_das_pro is not None:
            result['EnableDasPro'] = self.enable_das_pro
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.score is not None:
            result['Score'] = self.score
        if self.score_map is not None:
            result['ScoreMap'] = self.score_map
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoFunction') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataListAutoFunction()
            self.auto_function = temp_model.from_map(m['AutoFunction'])
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('EnableDasPro') is not None:
            self.enable_das_pro = m.get('EnableDasPro')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Instance') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataListInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ScoreMap') is not None:
            self.score_map = m.get('ScoreMap')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetInstanceInspectionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: List[GetInstanceInspectionsResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetInstanceInspectionsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetInstanceInspectionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceInspectionsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetInstanceInspectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceInspectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceInspectionsResponseBody = None,
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
            temp_model = GetInstanceInspectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceSqlOptimizeStatisticRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        filter_enable: str = None,
        instance_id: str = None,
        node_id: str = None,
        start_time: str = None,
        threshold: str = None,
        use_merging: str = None,
    ):
        self.end_time = end_time
        self.filter_enable = filter_enable
        self.instance_id = instance_id
        self.node_id = node_id
        self.start_time = start_time
        self.threshold = threshold
        self.use_merging = use_merging

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.filter_enable is not None:
            result['FilterEnable'] = self.filter_enable
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.use_merging is not None:
            result['UseMerging'] = self.use_merging
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FilterEnable') is not None:
            self.filter_enable = m.get('FilterEnable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('UseMerging') is not None:
            self.use_merging = m.get('UseMerging')
        return self


class GetInstanceSqlOptimizeStatisticResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        improvement: float = None,
    ):
        self.count = count
        self.improvement = improvement

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.improvement is not None:
            result['improvement'] = self.improvement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('improvement') is not None:
            self.improvement = m.get('improvement')
        return self


class GetInstanceSqlOptimizeStatisticResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstanceSqlOptimizeStatisticResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetInstanceSqlOptimizeStatisticResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceSqlOptimizeStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceSqlOptimizeStatisticResponseBody = None,
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
            temp_model = GetInstanceSqlOptimizeStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKillInstanceSessionTaskResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        task_id: str = None,
    ):
        self.instance_id = instance_id
        self.node_id = node_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetKillInstanceSessionTaskResultResponseBodyDataResult(TeaModel):
    def __init__(
        self,
        active: bool = None,
        command: str = None,
        db: str = None,
        host: str = None,
        id: int = None,
        info: str = None,
        reason: str = None,
        state: str = None,
        task_id: str = None,
        time: int = None,
        user: str = None,
    ):
        self.active = active
        self.command = command
        self.db = db
        self.host = host
        self.id = id
        self.info = info
        self.reason = reason
        self.state = state
        self.task_id = task_id
        self.time = time
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.command is not None:
            result['Command'] = self.command
        if self.db is not None:
            result['Db'] = self.db
        if self.host is not None:
            result['Host'] = self.host
        if self.id is not None:
            result['Id'] = self.id
        if self.info is not None:
            result['Info'] = self.info
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.state is not None:
            result['State'] = self.state
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.time is not None:
            result['Time'] = self.time
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class GetKillInstanceSessionTaskResultResponseBodyData(TeaModel):
    def __init__(
        self,
        ignored_user_session_count: int = None,
        instance_id: str = None,
        kill_fail_count: int = None,
        kill_success_count: int = None,
        result: List[GetKillInstanceSessionTaskResultResponseBodyDataResult] = None,
        sessions: List[int] = None,
        task_id: str = None,
        task_state: str = None,
        user_id: str = None,
    ):
        self.ignored_user_session_count = ignored_user_session_count
        self.instance_id = instance_id
        self.kill_fail_count = kill_fail_count
        self.kill_success_count = kill_success_count
        self.result = result
        self.sessions = sessions
        self.task_id = task_id
        self.task_state = task_state
        self.user_id = user_id

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
        if self.ignored_user_session_count is not None:
            result['IgnoredUserSessionCount'] = self.ignored_user_session_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.kill_fail_count is not None:
            result['KillFailCount'] = self.kill_fail_count
        if self.kill_success_count is not None:
            result['KillSuccessCount'] = self.kill_success_count
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.sessions is not None:
            result['Sessions'] = self.sessions
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoredUserSessionCount') is not None:
            self.ignored_user_session_count = m.get('IgnoredUserSessionCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KillFailCount') is not None:
            self.kill_fail_count = m.get('KillFailCount')
        if m.get('KillSuccessCount') is not None:
            self.kill_success_count = m.get('KillSuccessCount')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetKillInstanceSessionTaskResultResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Sessions') is not None:
            self.sessions = m.get('Sessions')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetKillInstanceSessionTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetKillInstanceSessionTaskResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetKillInstanceSessionTaskResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetKillInstanceSessionTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetKillInstanceSessionTaskResultResponseBody = None,
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
            temp_model = GetKillInstanceSessionTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPartitionsHeatmapRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        time_range: str = None,
        type: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.time_range = time_range
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPartitionsHeatmapResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class GetPartitionsHeatmapResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPartitionsHeatmapResponseBody = None,
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
            temp_model = GetPartitionsHeatmapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeDataStatsRequest(TeaModel):
    def __init__(
        self,
        asc: str = None,
        db_names: str = None,
        engine: str = None,
        instance_ids: str = None,
        keywords: str = None,
        logical_operator: str = None,
        only_optimized_sql: str = None,
        order_by: str = None,
        page_no: str = None,
        page_size: str = None,
        rules: str = None,
        sql_ids: str = None,
        tag_names: str = None,
        time: str = None,
    ):
        self.asc = asc
        self.db_names = db_names
        self.engine = engine
        self.instance_ids = instance_ids
        self.keywords = keywords
        self.logical_operator = logical_operator
        self.only_optimized_sql = only_optimized_sql
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.rules = rules
        self.sql_ids = sql_ids
        self.tag_names = tag_names
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['Asc'] = self.asc
        if self.db_names is not None:
            result['DbNames'] = self.db_names
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator
        if self.only_optimized_sql is not None:
            result['OnlyOptimizedSql'] = self.only_optimized_sql
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.sql_ids is not None:
            result['SqlIds'] = self.sql_ids
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')
        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')
        if m.get('OnlyOptimizedSql') is not None:
            self.only_optimized_sql = m.get('OnlyOptimizedSql')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('SqlIds') is not None:
            self.sql_ids = m.get('SqlIds')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetQueryOptimizeDataStatsResponseBodyDataListRuleList(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQueryOptimizeDataStatsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        avg_lock_time: float = None,
        avg_query_time: float = None,
        avg_rows_affected: float = None,
        avg_rows_examined: float = None,
        avg_rows_sent: float = None,
        count: int = None,
        dbname: str = None,
        instance_id: str = None,
        max_lock_time: float = None,
        max_query_time: float = None,
        max_rows_affected: int = None,
        max_rows_examined: int = None,
        max_rows_sent: int = None,
        psql: str = None,
        rule_list: List[GetQueryOptimizeDataStatsResponseBodyDataListRuleList] = None,
        sql_id: str = None,
        sql_sample: str = None,
        sql_type: str = None,
    ):
        self.avg_lock_time = avg_lock_time
        self.avg_query_time = avg_query_time
        self.avg_rows_affected = avg_rows_affected
        self.avg_rows_examined = avg_rows_examined
        self.avg_rows_sent = avg_rows_sent
        self.count = count
        self.dbname = dbname
        self.instance_id = instance_id
        self.max_lock_time = max_lock_time
        self.max_query_time = max_query_time
        self.max_rows_affected = max_rows_affected
        self.max_rows_examined = max_rows_examined
        self.max_rows_sent = max_rows_sent
        self.psql = psql
        self.rule_list = rule_list
        self.sql_id = sql_id
        self.sql_sample = sql_sample
        self.sql_type = sql_type

    def validate(self):
        if self.rule_list:
            for k in self.rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avg_lock_time is not None:
            result['AvgLockTime'] = self.avg_lock_time
        if self.avg_query_time is not None:
            result['AvgQueryTime'] = self.avg_query_time
        if self.avg_rows_affected is not None:
            result['AvgRowsAffected'] = self.avg_rows_affected
        if self.avg_rows_examined is not None:
            result['AvgRowsExamined'] = self.avg_rows_examined
        if self.avg_rows_sent is not None:
            result['AvgRowsSent'] = self.avg_rows_sent
        if self.count is not None:
            result['Count'] = self.count
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_lock_time is not None:
            result['MaxLockTime'] = self.max_lock_time
        if self.max_query_time is not None:
            result['MaxQueryTime'] = self.max_query_time
        if self.max_rows_affected is not None:
            result['MaxRowsAffected'] = self.max_rows_affected
        if self.max_rows_examined is not None:
            result['MaxRowsExamined'] = self.max_rows_examined
        if self.max_rows_sent is not None:
            result['MaxRowsSent'] = self.max_rows_sent
        if self.psql is not None:
            result['Psql'] = self.psql
        result['RuleList'] = []
        if self.rule_list is not None:
            for k in self.rule_list:
                result['RuleList'].append(k.to_map() if k else None)
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_sample is not None:
            result['SqlSample'] = self.sql_sample
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgLockTime') is not None:
            self.avg_lock_time = m.get('AvgLockTime')
        if m.get('AvgQueryTime') is not None:
            self.avg_query_time = m.get('AvgQueryTime')
        if m.get('AvgRowsAffected') is not None:
            self.avg_rows_affected = m.get('AvgRowsAffected')
        if m.get('AvgRowsExamined') is not None:
            self.avg_rows_examined = m.get('AvgRowsExamined')
        if m.get('AvgRowsSent') is not None:
            self.avg_rows_sent = m.get('AvgRowsSent')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxLockTime') is not None:
            self.max_lock_time = m.get('MaxLockTime')
        if m.get('MaxQueryTime') is not None:
            self.max_query_time = m.get('MaxQueryTime')
        if m.get('MaxRowsAffected') is not None:
            self.max_rows_affected = m.get('MaxRowsAffected')
        if m.get('MaxRowsExamined') is not None:
            self.max_rows_examined = m.get('MaxRowsExamined')
        if m.get('MaxRowsSent') is not None:
            self.max_rows_sent = m.get('MaxRowsSent')
        if m.get('Psql') is not None:
            self.psql = m.get('Psql')
        self.rule_list = []
        if m.get('RuleList') is not None:
            for k in m.get('RuleList'):
                temp_model = GetQueryOptimizeDataStatsResponseBodyDataListRuleList()
                self.rule_list.append(temp_model.from_map(k))
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlSample') is not None:
            self.sql_sample = m.get('SqlSample')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        return self


class GetQueryOptimizeDataStatsResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetQueryOptimizeDataStatsResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeDataStatsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeDataStatsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQueryOptimizeDataStatsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetQueryOptimizeDataStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeDataStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryOptimizeDataStatsResponseBody = None,
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
            temp_model = GetQueryOptimizeDataStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeDataTopRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        instance_ids: str = None,
        tag_names: str = None,
        time: str = None,
        type: str = None,
    ):
        self.engine = engine
        self.instance_ids = instance_ids
        self.tag_names = tag_names
        self.time = time
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        if self.time is not None:
            result['Time'] = self.time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQueryOptimizeDataTopResponseBodyDataList(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        type: str = None,
        value: float = None,
    ):
        self.instance_id = instance_id
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetQueryOptimizeDataTopResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetQueryOptimizeDataTopResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeDataTopResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeDataTopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQueryOptimizeDataTopResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetQueryOptimizeDataTopResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeDataTopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryOptimizeDataTopResponseBody = None,
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
            temp_model = GetQueryOptimizeDataTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeDataTrendRequest(TeaModel):
    def __init__(
        self,
        end: str = None,
        engine: str = None,
        instance_ids: str = None,
        start: str = None,
        tag_names: str = None,
    ):
        self.end = end
        self.engine = engine
        self.instance_ids = instance_ids
        self.start = start
        self.tag_names = tag_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.start is not None:
            result['Start'] = self.start
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        return self


class GetQueryOptimizeDataTrendResponseBodyDataList(TeaModel):
    def __init__(
        self,
        kpi: str = None,
        timestamp: int = None,
        value: float = None,
    ):
        self.kpi = kpi
        self.timestamp = timestamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kpi is not None:
            result['Kpi'] = self.kpi
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Kpi') is not None:
            self.kpi = m.get('Kpi')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetQueryOptimizeDataTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetQueryOptimizeDataTrendResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeDataTrendResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeDataTrendResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQueryOptimizeDataTrendResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetQueryOptimizeDataTrendResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeDataTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryOptimizeDataTrendResponseBody = None,
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
            temp_model = GetQueryOptimizeDataTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeExecErrorSampleRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        instance_id: str = None,
        sql_id: str = None,
        time: str = None,
    ):
        self.engine = engine
        self.instance_id = instance_id
        self.sql_id = sql_id
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetQueryOptimizeExecErrorSampleResponseBodyDataList(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        error_code: str = None,
        orig_host: str = None,
        sql_id: str = None,
        sql_text: str = None,
        timestamp: int = None,
        user: str = None,
    ):
        self.dbname = dbname
        self.error_code = error_code
        self.orig_host = orig_host
        self.sql_id = sql_id
        self.sql_text = sql_text
        self.timestamp = timestamp
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.orig_host is not None:
            result['OrigHost'] = self.orig_host
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('OrigHost') is not None:
            self.orig_host = m.get('OrigHost')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class GetQueryOptimizeExecErrorSampleResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetQueryOptimizeExecErrorSampleResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeExecErrorSampleResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeExecErrorSampleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQueryOptimizeExecErrorSampleResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetQueryOptimizeExecErrorSampleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeExecErrorSampleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryOptimizeExecErrorSampleResponseBody = None,
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
            temp_model = GetQueryOptimizeExecErrorSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeExecErrorStatsRequest(TeaModel):
    def __init__(
        self,
        asc: str = None,
        db_names: str = None,
        engine: str = None,
        instance_ids: str = None,
        keywords: str = None,
        logical_operator: str = None,
        order_by: str = None,
        page_no: str = None,
        page_size: str = None,
        time: str = None,
    ):
        self.asc = asc
        self.db_names = db_names
        self.engine = engine
        self.instance_ids = instance_ids
        self.keywords = keywords
        self.logical_operator = logical_operator
        self.order_by = order_by
        self.page_no = page_no
        self.page_size = page_size
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asc is not None:
            result['Asc'] = self.asc
        if self.db_names is not None:
            result['DbNames'] = self.db_names
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.logical_operator is not None:
            result['LogicalOperator'] = self.logical_operator
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')
        if m.get('DbNames') is not None:
            self.db_names = m.get('DbNames')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('LogicalOperator') is not None:
            self.logical_operator = m.get('LogicalOperator')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class GetQueryOptimizeExecErrorStatsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        dbname: str = None,
        error_code: str = None,
        error_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        sql_id: str = None,
        sql_text: str = None,
    ):
        self.dbname = dbname
        self.error_code = error_code
        self.error_count = error_count
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.sql_id = sql_id
        self.sql_text = sql_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbname is not None:
            result['Dbname'] = self.dbname
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dbname') is not None:
            self.dbname = m.get('Dbname')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        return self


class GetQueryOptimizeExecErrorStatsResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetQueryOptimizeExecErrorStatsResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeExecErrorStatsResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeExecErrorStatsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQueryOptimizeExecErrorStatsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetQueryOptimizeExecErrorStatsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeExecErrorStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryOptimizeExecErrorStatsResponseBody = None,
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
            temp_model = GetQueryOptimizeExecErrorStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeRuleListRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        instance_ids: str = None,
        tag_names: str = None,
    ):
        self.engine = engine
        self.instance_ids = instance_ids
        self.tag_names = tag_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        return self


class GetQueryOptimizeRuleListResponseBodyDataList(TeaModel):
    def __init__(
        self,
        name: str = None,
        rule_id: str = None,
        type: str = None,
    ):
        self.name = name
        self.rule_id = rule_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetQueryOptimizeRuleListResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetQueryOptimizeRuleListResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeRuleListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeRuleListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQueryOptimizeRuleListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetQueryOptimizeRuleListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeRuleListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryOptimizeRuleListResponseBody = None,
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
            temp_model = GetQueryOptimizeRuleListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueryOptimizeSolutionRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        rule_ids: str = None,
        sql_id: str = None,
    ):
        self.engine = engine
        self.rule_ids = rule_ids
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        return self


class GetQueryOptimizeSolutionResponseBodyDataList(TeaModel):
    def __init__(
        self,
        level: str = None,
        rule_id: str = None,
        solution: str = None,
        solution_ext: str = None,
    ):
        self.level = level
        self.rule_id = rule_id
        self.solution = solution
        self.solution_ext = solution_ext

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['Level'] = self.level
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.solution is not None:
            result['Solution'] = self.solution
        if self.solution_ext is not None:
            result['SolutionExt'] = self.solution_ext
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('Solution') is not None:
            self.solution = m.get('Solution')
        if m.get('SolutionExt') is not None:
            self.solution_ext = m.get('SolutionExt')
        return self


class GetQueryOptimizeSolutionResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetQueryOptimizeSolutionResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['Extra'] = self.extra
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetQueryOptimizeSolutionResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetQueryOptimizeSolutionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetQueryOptimizeSolutionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetQueryOptimizeSolutionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueryOptimizeSolutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueryOptimizeSolutionResponseBody = None,
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
            temp_model = GetQueryOptimizeSolutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRedisAllSessionRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetRedisAllSessionResponseBodyDataSessions(TeaModel):
    def __init__(
        self,
        addr: str = None,
        age: str = None,
        client: str = None,
        client_desc: str = None,
        cmd: str = None,
        db: int = None,
        events: str = None,
        fd: int = None,
        flags: str = None,
        id: int = None,
        idle: int = None,
        multi: int = None,
        name: str = None,
        node_id: str = None,
        obl: int = None,
        oll: int = None,
        omem: int = None,
        psub: int = None,
        qbuf: int = None,
        qbuf_free: int = None,
        sub: int = None,
    ):
        self.addr = addr
        self.age = age
        self.client = client
        self.client_desc = client_desc
        self.cmd = cmd
        self.db = db
        self.events = events
        self.fd = fd
        self.flags = flags
        self.id = id
        self.idle = idle
        self.multi = multi
        self.name = name
        self.node_id = node_id
        self.obl = obl
        self.oll = oll
        self.omem = omem
        self.psub = psub
        self.qbuf = qbuf
        self.qbuf_free = qbuf_free
        self.sub = sub

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.addr is not None:
            result['Addr'] = self.addr
        if self.age is not None:
            result['Age'] = self.age
        if self.client is not None:
            result['Client'] = self.client
        if self.client_desc is not None:
            result['ClientDesc'] = self.client_desc
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.db is not None:
            result['Db'] = self.db
        if self.events is not None:
            result['Events'] = self.events
        if self.fd is not None:
            result['Fd'] = self.fd
        if self.flags is not None:
            result['Flags'] = self.flags
        if self.id is not None:
            result['Id'] = self.id
        if self.idle is not None:
            result['Idle'] = self.idle
        if self.multi is not None:
            result['Multi'] = self.multi
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.obl is not None:
            result['Obl'] = self.obl
        if self.oll is not None:
            result['Oll'] = self.oll
        if self.omem is not None:
            result['Omem'] = self.omem
        if self.psub is not None:
            result['Psub'] = self.psub
        if self.qbuf is not None:
            result['Qbuf'] = self.qbuf
        if self.qbuf_free is not None:
            result['QbufFree'] = self.qbuf_free
        if self.sub is not None:
            result['Sub'] = self.sub
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Addr') is not None:
            self.addr = m.get('Addr')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('Client') is not None:
            self.client = m.get('Client')
        if m.get('ClientDesc') is not None:
            self.client_desc = m.get('ClientDesc')
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('Fd') is not None:
            self.fd = m.get('Fd')
        if m.get('Flags') is not None:
            self.flags = m.get('Flags')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Idle') is not None:
            self.idle = m.get('Idle')
        if m.get('Multi') is not None:
            self.multi = m.get('Multi')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Obl') is not None:
            self.obl = m.get('Obl')
        if m.get('Oll') is not None:
            self.oll = m.get('Oll')
        if m.get('Omem') is not None:
            self.omem = m.get('Omem')
        if m.get('Psub') is not None:
            self.psub = m.get('Psub')
        if m.get('Qbuf') is not None:
            self.qbuf = m.get('Qbuf')
        if m.get('QbufFree') is not None:
            self.qbuf_free = m.get('QbufFree')
        if m.get('Sub') is not None:
            self.sub = m.get('Sub')
        return self


class GetRedisAllSessionResponseBodyDataSourceStats(TeaModel):
    def __init__(
        self,
        count: str = None,
        ids: List[int] = None,
        key: str = None,
    ):
        self.count = count
        self.ids = ids
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class GetRedisAllSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        sessions: List[GetRedisAllSessionResponseBodyDataSessions] = None,
        source_stats: List[GetRedisAllSessionResponseBodyDataSourceStats] = None,
        timestamp: int = None,
        total: int = None,
    ):
        self.sessions = sessions
        self.source_stats = source_stats
        self.timestamp = timestamp
        self.total = total

    def validate(self):
        if self.sessions:
            for k in self.sessions:
                if k:
                    k.validate()
        if self.source_stats:
            for k in self.source_stats:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sessions'] = []
        if self.sessions is not None:
            for k in self.sessions:
                result['Sessions'].append(k.to_map() if k else None)
        result['SourceStats'] = []
        if self.source_stats is not None:
            for k in self.source_stats:
                result['SourceStats'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sessions = []
        if m.get('Sessions') is not None:
            for k in m.get('Sessions'):
                temp_model = GetRedisAllSessionResponseBodyDataSessions()
                self.sessions.append(temp_model.from_map(k))
        self.source_stats = []
        if m.get('SourceStats') is not None:
            for k in m.get('SourceStats'):
                temp_model = GetRedisAllSessionResponseBodyDataSourceStats()
                self.source_stats.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetRedisAllSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetRedisAllSessionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetRedisAllSessionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRedisAllSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRedisAllSessionResponseBody = None,
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
            temp_model = GetRedisAllSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRequestDiagnosisPageRequest(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        node_id: str = None,
        page_no: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.node_id = node_id
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time

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
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetRequestDiagnosisPageResponseBodyDataList(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        db_schema: str = None,
        engine: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message_id: str = None,
        param: str = None,
        result: str = None,
        sql_id: str = None,
        state: int = None,
        uuid: str = None,
    ):
        self.account_id = account_id
        self.db_schema = db_schema
        self.engine = engine
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.message_id = message_id
        self.param = param
        self.result = result
        self.sql_id = sql_id
        self.state = state
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.db_schema is not None:
            result['dbSchema'] = self.db_schema
        if self.engine is not None:
            result['engine'] = self.engine
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.param is not None:
            result['param'] = self.param
        if self.result is not None:
            result['result'] = self.result
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.state is not None:
            result['state'] = self.state
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('dbSchema') is not None:
            self.db_schema = m.get('dbSchema')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('param') is not None:
            self.param = m.get('param')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetRequestDiagnosisPageResponseBodyData(TeaModel):
    def __init__(
        self,
        extra: str = None,
        list: List[GetRequestDiagnosisPageResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.extra = extra
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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
        if self.extra is not None:
            result['extra'] = self.extra
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GetRequestDiagnosisPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetRequestDiagnosisPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRequestDiagnosisPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetRequestDiagnosisPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRequestDiagnosisPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRequestDiagnosisPageResponseBody = None,
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
            temp_model = GetRequestDiagnosisPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRequestDiagnosisResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        message_id: str = None,
        node_id: str = None,
        source: str = None,
        sql_id: str = None,
    ):
        self.instance_id = instance_id
        self.message_id = message_id
        self.node_id = node_id
        self.source = source
        self.sql_id = sql_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.source is not None:
            result['Source'] = self.source
        if self.sql_id is not None:
            result['SqlId'] = self.sql_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SqlId') is not None:
            self.sql_id = m.get('SqlId')
        return self


class GetRequestDiagnosisResultResponseBodyData(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        db_schema: str = None,
        engine: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message_id: str = None,
        param: str = None,
        result: str = None,
        sql_id: str = None,
        state: int = None,
        uuid: str = None,
    ):
        self.account_id = account_id
        self.db_schema = db_schema
        self.engine = engine
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.message_id = message_id
        self.param = param
        self.result = result
        self.sql_id = sql_id
        self.state = state
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.db_schema is not None:
            result['dbSchema'] = self.db_schema
        if self.engine is not None:
            result['engine'] = self.engine
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.message_id is not None:
            result['messageId'] = self.message_id
        if self.param is not None:
            result['param'] = self.param
        if self.result is not None:
            result['result'] = self.result
        if self.sql_id is not None:
            result['sqlId'] = self.sql_id
        if self.state is not None:
            result['state'] = self.state
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('dbSchema') is not None:
            self.db_schema = m.get('dbSchema')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')
        if m.get('param') is not None:
            self.param = m.get('param')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class GetRequestDiagnosisResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRequestDiagnosisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetRequestDiagnosisResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRequestDiagnosisResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRequestDiagnosisResultResponseBody = None,
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
            temp_model = GetRequestDiagnosisResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRunningSqlConcurrencyControlRulesRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules(TeaModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        instance_id: str = None,
        item_id: int = None,
        keywords_hash: str = None,
        max_concurrency: str = None,
        sql_keywords: str = None,
        sql_type: str = None,
        start_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        self.concurrency_control_time = concurrency_control_time
        self.instance_id = instance_id
        self.item_id = item_id
        self.keywords_hash = keywords_hash
        self.max_concurrency = max_concurrency
        self.sql_keywords = sql_keywords
        self.sql_type = sql_type
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.keywords_hash is not None:
            result['KeywordsHash'] = self.keywords_hash
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('KeywordsHash') is not None:
            self.keywords_hash = m.get('KeywordsHash')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyDataList(TeaModel):
    def __init__(
        self,
        running_rules: List[GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules] = None,
    ):
        self.running_rules = running_rules

    def validate(self):
        if self.running_rules:
            for k in self.running_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['runningRules'] = []
        if self.running_rules is not None:
            for k in self.running_rules:
                result['runningRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.running_rules = []
        if m.get('runningRules') is not None:
            for k in m.get('runningRules'):
                temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyDataListRunningRules()
                self.running_rules.append(temp_model.from_map(k))
        return self


class GetRunningSqlConcurrencyControlRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        list: GetRunningSqlConcurrencyControlRulesResponseBodyDataList = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetRunningSqlConcurrencyControlRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetRunningSqlConcurrencyControlRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRunningSqlConcurrencyControlRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRunningSqlConcurrencyControlRulesResponseBody = None,
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
            temp_model = GetRunningSqlConcurrencyControlRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlConcurrencyControlKeywordsFromSqlTextRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        sql_text: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.sql_text = sql_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sql_text is not None:
            result['SqlText'] = self.sql_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SqlText') is not None:
            self.sql_text = m.get('SqlText')
        return self


class GetSqlConcurrencyControlKeywordsFromSqlTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class GetSqlConcurrencyControlKeywordsFromSqlTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSqlConcurrencyControlKeywordsFromSqlTextResponseBody = None,
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
            temp_model = GetSqlConcurrencyControlKeywordsFromSqlTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlConcurrencyControlRulesHistoryRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules(TeaModel):
    def __init__(
        self,
        concurrency_control_time: int = None,
        instance_id: str = None,
        item_id: int = None,
        keywords_hash: str = None,
        max_concurrency: int = None,
        sql_keywords: str = None,
        sql_type: str = None,
        start_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        self.concurrency_control_time = concurrency_control_time
        self.instance_id = instance_id
        self.item_id = item_id
        self.keywords_hash = keywords_hash
        self.max_concurrency = max_concurrency
        self.sql_keywords = sql_keywords
        self.sql_type = sql_type
        self.start_time = start_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency_control_time is not None:
            result['ConcurrencyControlTime'] = self.concurrency_control_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.keywords_hash is not None:
            result['KeywordsHash'] = self.keywords_hash
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.sql_keywords is not None:
            result['SqlKeywords'] = self.sql_keywords
        if self.sql_type is not None:
            result['SqlType'] = self.sql_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrencyControlTime') is not None:
            self.concurrency_control_time = m.get('ConcurrencyControlTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('KeywordsHash') is not None:
            self.keywords_hash = m.get('KeywordsHash')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('SqlKeywords') is not None:
            self.sql_keywords = m.get('SqlKeywords')
        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyDataList(TeaModel):
    def __init__(
        self,
        rules: List[GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules] = None,
    ):
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
        result['rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rules = []
        if m.get('rules') is not None:
            for k in m.get('rules'):
                temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyDataListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        list: GetSqlConcurrencyControlRulesHistoryResponseBodyDataList = None,
        total: int = None,
    ):
        self.list = list
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list is not None:
            result['List'] = self.list.to_map()
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSqlConcurrencyControlRulesHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSqlConcurrencyControlRulesHistoryResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSqlConcurrencyControlRulesHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSqlConcurrencyControlRulesHistoryResponseBody = None,
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
            temp_model = GetSqlConcurrencyControlRulesHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlOptimizeAdviceRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        end_dt: str = None,
        engine: str = None,
        instance_ids: str = None,
        start_dt: str = None,
    ):
        self.console_context = console_context
        self.end_dt = end_dt
        self.engine = engine
        self.instance_ids = instance_ids
        self.start_dt = start_dt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.end_dt is not None:
            result['EndDt'] = self.end_dt
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.start_dt is not None:
            result['StartDt'] = self.start_dt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('EndDt') is not None:
            self.end_dt = m.get('EndDt')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('StartDt') is not None:
            self.start_dt = m.get('StartDt')
        return self


class GetSqlOptimizeAdviceResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        download_url: str = None,
        expire_time: str = None,
        status: str = None,
        status_code: str = None,
        task_id: str = None,
    ):
        self.create_time = create_time
        self.download_url = download_url
        self.expire_time = expire_time
        self.status = status
        self.status_code = status_code
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.status is not None:
            result['Status'] = self.status
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetSqlOptimizeAdviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSqlOptimizeAdviceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = GetSqlOptimizeAdviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSqlOptimizeAdviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSqlOptimizeAdviceResponseBody = None,
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
            temp_model = GetSqlOptimizeAdviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KillInstanceAllSessionRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
    ):
        self.console_context = console_context
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class KillInstanceAllSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class KillInstanceAllSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KillInstanceAllSessionResponseBody = None,
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
            temp_model = KillInstanceAllSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAutoScalingConfigRequestBandwidth(TeaModel):
    def __init__(
        self,
        apply: bool = None,
        bandwidth_usage_lower_threshold: int = None,
        bandwidth_usage_upper_threshold: int = None,
        downgrade: bool = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        self.apply = apply
        self.bandwidth_usage_lower_threshold = bandwidth_usage_lower_threshold
        self.bandwidth_usage_upper_threshold = bandwidth_usage_upper_threshold
        self.downgrade = downgrade
        self.observation_window_size = observation_window_size
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply is not None:
            result['Apply'] = self.apply
        if self.bandwidth_usage_lower_threshold is not None:
            result['BandwidthUsageLowerThreshold'] = self.bandwidth_usage_lower_threshold
        if self.bandwidth_usage_upper_threshold is not None:
            result['BandwidthUsageUpperThreshold'] = self.bandwidth_usage_upper_threshold
        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade
        if self.observation_window_size is not None:
            result['ObservationWindowSize'] = self.observation_window_size
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')
        if m.get('BandwidthUsageLowerThreshold') is not None:
            self.bandwidth_usage_lower_threshold = m.get('BandwidthUsageLowerThreshold')
        if m.get('BandwidthUsageUpperThreshold') is not None:
            self.bandwidth_usage_upper_threshold = m.get('BandwidthUsageUpperThreshold')
        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')
        if m.get('ObservationWindowSize') is not None:
            self.observation_window_size = m.get('ObservationWindowSize')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        return self


class ModifyAutoScalingConfigRequestResource(TeaModel):
    def __init__(
        self,
        apply: bool = None,
        cpu_usage_upper_threshold: int = None,
        downgrade_observation_window_size: str = None,
        enable: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        self.apply = apply
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        self.downgrade_observation_window_size = downgrade_observation_window_size
        self.enable = enable
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply is not None:
            result['Apply'] = self.apply
        if self.cpu_usage_upper_threshold is not None:
            result['CpuUsageUpperThreshold'] = self.cpu_usage_upper_threshold
        if self.downgrade_observation_window_size is not None:
            result['DowngradeObservationWindowSize'] = self.downgrade_observation_window_size
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.upgrade_observation_window_size is not None:
            result['UpgradeObservationWindowSize'] = self.upgrade_observation_window_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')
        if m.get('CpuUsageUpperThreshold') is not None:
            self.cpu_usage_upper_threshold = m.get('CpuUsageUpperThreshold')
        if m.get('DowngradeObservationWindowSize') is not None:
            self.downgrade_observation_window_size = m.get('DowngradeObservationWindowSize')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('UpgradeObservationWindowSize') is not None:
            self.upgrade_observation_window_size = m.get('UpgradeObservationWindowSize')
        return self


class ModifyAutoScalingConfigRequestShard(TeaModel):
    def __init__(
        self,
        apply: bool = None,
        downgrade: bool = None,
        downgrade_observation_window_size: str = None,
        max_shards: int = None,
        mem_usage_lower_threshold: int = None,
        mem_usage_upper_threshold: int = None,
        min_shards: int = None,
        upgrade: bool = None,
        upgrade_observation_window_size: str = None,
    ):
        self.apply = apply
        self.downgrade = downgrade
        self.downgrade_observation_window_size = downgrade_observation_window_size
        self.max_shards = max_shards
        self.mem_usage_lower_threshold = mem_usage_lower_threshold
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        self.min_shards = min_shards
        self.upgrade = upgrade
        self.upgrade_observation_window_size = upgrade_observation_window_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply is not None:
            result['Apply'] = self.apply
        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade
        if self.downgrade_observation_window_size is not None:
            result['DowngradeObservationWindowSize'] = self.downgrade_observation_window_size
        if self.max_shards is not None:
            result['MaxShards'] = self.max_shards
        if self.mem_usage_lower_threshold is not None:
            result['MemUsageLowerThreshold'] = self.mem_usage_lower_threshold
        if self.mem_usage_upper_threshold is not None:
            result['MemUsageUpperThreshold'] = self.mem_usage_upper_threshold
        if self.min_shards is not None:
            result['MinShards'] = self.min_shards
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        if self.upgrade_observation_window_size is not None:
            result['UpgradeObservationWindowSize'] = self.upgrade_observation_window_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')
        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')
        if m.get('DowngradeObservationWindowSize') is not None:
            self.downgrade_observation_window_size = m.get('DowngradeObservationWindowSize')
        if m.get('MaxShards') is not None:
            self.max_shards = m.get('MaxShards')
        if m.get('MemUsageLowerThreshold') is not None:
            self.mem_usage_lower_threshold = m.get('MemUsageLowerThreshold')
        if m.get('MemUsageUpperThreshold') is not None:
            self.mem_usage_upper_threshold = m.get('MemUsageUpperThreshold')
        if m.get('MinShards') is not None:
            self.min_shards = m.get('MinShards')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        if m.get('UpgradeObservationWindowSize') is not None:
            self.upgrade_observation_window_size = m.get('UpgradeObservationWindowSize')
        return self


class ModifyAutoScalingConfigRequestSpec(TeaModel):
    def __init__(
        self,
        apply: bool = None,
        cool_down_time: str = None,
        cpu_usage_upper_threshold: int = None,
        downgrade: bool = None,
        max_read_only_nodes: int = None,
        max_spec: str = None,
        mem_usage_upper_threshold: int = None,
        observation_window_size: str = None,
        upgrade: bool = None,
    ):
        self.apply = apply
        self.cool_down_time = cool_down_time
        self.cpu_usage_upper_threshold = cpu_usage_upper_threshold
        self.downgrade = downgrade
        self.max_read_only_nodes = max_read_only_nodes
        self.max_spec = max_spec
        self.mem_usage_upper_threshold = mem_usage_upper_threshold
        self.observation_window_size = observation_window_size
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply is not None:
            result['Apply'] = self.apply
        if self.cool_down_time is not None:
            result['CoolDownTime'] = self.cool_down_time
        if self.cpu_usage_upper_threshold is not None:
            result['CpuUsageUpperThreshold'] = self.cpu_usage_upper_threshold
        if self.downgrade is not None:
            result['Downgrade'] = self.downgrade
        if self.max_read_only_nodes is not None:
            result['MaxReadOnlyNodes'] = self.max_read_only_nodes
        if self.max_spec is not None:
            result['MaxSpec'] = self.max_spec
        if self.mem_usage_upper_threshold is not None:
            result['MemUsageUpperThreshold'] = self.mem_usage_upper_threshold
        if self.observation_window_size is not None:
            result['ObservationWindowSize'] = self.observation_window_size
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')
        if m.get('CoolDownTime') is not None:
            self.cool_down_time = m.get('CoolDownTime')
        if m.get('CpuUsageUpperThreshold') is not None:
            self.cpu_usage_upper_threshold = m.get('CpuUsageUpperThreshold')
        if m.get('Downgrade') is not None:
            self.downgrade = m.get('Downgrade')
        if m.get('MaxReadOnlyNodes') is not None:
            self.max_read_only_nodes = m.get('MaxReadOnlyNodes')
        if m.get('MaxSpec') is not None:
            self.max_spec = m.get('MaxSpec')
        if m.get('MemUsageUpperThreshold') is not None:
            self.mem_usage_upper_threshold = m.get('MemUsageUpperThreshold')
        if m.get('ObservationWindowSize') is not None:
            self.observation_window_size = m.get('ObservationWindowSize')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        return self


class ModifyAutoScalingConfigRequestStorage(TeaModel):
    def __init__(
        self,
        apply: bool = None,
        disk_usage_upper_threshold: int = None,
        max_storage: int = None,
        upgrade: bool = None,
    ):
        self.apply = apply
        self.disk_usage_upper_threshold = disk_usage_upper_threshold
        self.max_storage = max_storage
        self.upgrade = upgrade

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply is not None:
            result['Apply'] = self.apply
        if self.disk_usage_upper_threshold is not None:
            result['DiskUsageUpperThreshold'] = self.disk_usage_upper_threshold
        if self.max_storage is not None:
            result['MaxStorage'] = self.max_storage
        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apply') is not None:
            self.apply = m.get('Apply')
        if m.get('DiskUsageUpperThreshold') is not None:
            self.disk_usage_upper_threshold = m.get('DiskUsageUpperThreshold')
        if m.get('MaxStorage') is not None:
            self.max_storage = m.get('MaxStorage')
        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')
        return self


class ModifyAutoScalingConfigRequest(TeaModel):
    def __init__(
        self,
        bandwidth: ModifyAutoScalingConfigRequestBandwidth = None,
        instance_id: str = None,
        resource: ModifyAutoScalingConfigRequestResource = None,
        shard: ModifyAutoScalingConfigRequestShard = None,
        spec: ModifyAutoScalingConfigRequestSpec = None,
        storage: ModifyAutoScalingConfigRequestStorage = None,
    ):
        self.bandwidth = bandwidth
        self.instance_id = instance_id
        self.resource = resource
        self.shard = shard
        self.spec = spec
        self.storage = storage

    def validate(self):
        if self.bandwidth:
            self.bandwidth.validate()
        if self.resource:
            self.resource.validate()
        if self.shard:
            self.shard.validate()
        if self.spec:
            self.spec.validate()
        if self.storage:
            self.storage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        if self.shard is not None:
            result['Shard'] = self.shard.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.storage is not None:
            result['Storage'] = self.storage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            temp_model = ModifyAutoScalingConfigRequestBandwidth()
            self.bandwidth = temp_model.from_map(m['Bandwidth'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resource') is not None:
            temp_model = ModifyAutoScalingConfigRequestResource()
            self.resource = temp_model.from_map(m['Resource'])
        if m.get('Shard') is not None:
            temp_model = ModifyAutoScalingConfigRequestShard()
            self.shard = temp_model.from_map(m['Shard'])
        if m.get('Spec') is not None:
            temp_model = ModifyAutoScalingConfigRequestSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Storage') is not None:
            temp_model = ModifyAutoScalingConfigRequestStorage()
            self.storage = temp_model.from_map(m['Storage'])
        return self


class ModifyAutoScalingConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAutoScalingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyAutoScalingConfigResponseBody = None,
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
            temp_model = ModifyAutoScalingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCloudBenchTaskRequest(TeaModel):
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


class RunCloudBenchTaskResponseBodyDataPreCheckItem(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        name: str = None,
        order: int = None,
        status: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.name = name
        self.order = order
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
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class RunCloudBenchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        pre_check_item: List[RunCloudBenchTaskResponseBodyDataPreCheckItem] = None,
    ):
        self.pre_check_item = pre_check_item

    def validate(self):
        if self.pre_check_item:
            for k in self.pre_check_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PreCheckItem'] = []
        if self.pre_check_item is not None:
            for k in self.pre_check_item:
                result['PreCheckItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pre_check_item = []
        if m.get('PreCheckItem') is not None:
            for k in m.get('PreCheckItem'):
                temp_model = RunCloudBenchTaskResponseBodyDataPreCheckItem()
                self.pre_check_item.append(temp_model.from_map(k))
        return self


class RunCloudBenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: RunCloudBenchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = RunCloudBenchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RunCloudBenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCloudBenchTaskResponseBody = None,
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
            temp_model = RunCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetEventSubscriptionRequest(TeaModel):
    def __init__(
        self,
        active: str = None,
        channel_type: str = None,
        contact_group_name: str = None,
        contact_name: str = None,
        dispatch_rule: str = None,
        event_context: str = None,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
        min_interval: str = None,
        severity: str = None,
    ):
        self.active = active
        self.channel_type = channel_type
        self.contact_group_name = contact_group_name
        self.contact_name = contact_name
        self.dispatch_rule = dispatch_rule
        self.event_context = event_context
        self.instance_id = instance_id
        self.lang = lang
        self.level = level
        self.min_interval = min_interval
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.level is not None:
            result['Level'] = self.level
        if self.min_interval is not None:
            result['MinInterval'] = self.min_interval
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('DispatchRule') is not None:
            self.dispatch_rule = m.get('DispatchRule')
        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinInterval') is not None:
            self.min_interval = m.get('MinInterval')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class SetEventSubscriptionResponseBodyData(TeaModel):
    def __init__(
        self,
        active: int = None,
        channel_type: str = None,
        contact_group_name: str = None,
        contact_name: str = None,
        event_context: str = None,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
        min_interval: int = None,
        user_id: str = None,
    ):
        self.active = active
        self.channel_type = channel_type
        self.contact_group_name = contact_group_name
        self.contact_name = contact_name
        self.event_context = event_context
        self.instance_id = instance_id
        self.lang = lang
        self.level = level
        self.min_interval = min_interval
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['active'] = self.active
        if self.channel_type is not None:
            result['channelType'] = self.channel_type
        if self.contact_group_name is not None:
            result['contactGroupName'] = self.contact_group_name
        if self.contact_name is not None:
            result['contactName'] = self.contact_name
        if self.event_context is not None:
            result['eventContext'] = self.event_context
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.lang is not None:
            result['lang'] = self.lang
        if self.level is not None:
            result['level'] = self.level
        if self.min_interval is not None:
            result['minInterval'] = self.min_interval
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')
        if m.get('contactGroupName') is not None:
            self.contact_group_name = m.get('contactGroupName')
        if m.get('contactName') is not None:
            self.contact_name = m.get('contactName')
        if m.get('eventContext') is not None:
            self.event_context = m.get('eventContext')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('minInterval') is not None:
            self.min_interval = m.get('minInterval')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class SetEventSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SetEventSubscriptionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = SetEventSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetEventSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetEventSubscriptionResponseBody = None,
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
            temp_model = SetEventSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopCloudBenchTaskRequest(TeaModel):
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


class StopCloudBenchTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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


class StopCloudBenchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopCloudBenchTaskResponseBody = None,
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
            temp_model = StopCloudBenchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncHDMAliyunResourceRequest(TeaModel):
    def __init__(
        self,
        async_: str = None,
        resource_types: str = None,
        uid: str = None,
        user_id: str = None,
        wait_for_modify_security_ips: str = None,
        context: str = None,
        access_key: str = None,
        signature: str = None,
        skip_auth: str = None,
        timestamp: str = None,
    ):
        self.async_ = async_
        self.resource_types = resource_types
        self.uid = uid
        self.user_id = user_id
        self.wait_for_modify_security_ips = wait_for_modify_security_ips
        self.context = context
        self.access_key = access_key
        self.signature = signature
        self.skip_auth = skip_auth
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.wait_for_modify_security_ips is not None:
            result['WaitForModifySecurityIps'] = self.wait_for_modify_security_ips
        if self.context is not None:
            result['__context'] = self.context
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('WaitForModifySecurityIps') is not None:
            self.wait_for_modify_security_ips = m.get('WaitForModifySecurityIps')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class SyncHDMAliyunResourceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
        synchro: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
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
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class SyncHDMAliyunResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncHDMAliyunResourceResponseBody = None,
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
            temp_model = SyncHDMAliyunResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoResourceOptimizeRulesAsyncRequest(TeaModel):
    def __init__(
        self,
        console_context: str = None,
        instance_ids: str = None,
        result_id: str = None,
        table_fragmentation_ratio: float = None,
        table_space_size: float = None,
    ):
        self.console_context = console_context
        self.instance_ids = instance_ids
        self.result_id = result_id
        self.table_fragmentation_ratio = table_fragmentation_ratio
        self.table_space_size = table_space_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.result_id is not None:
            result['ResultId'] = self.result_id
        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio
        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')
        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')
        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')
        return self


class UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        error_message: str = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.error_message = error_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponse(TeaModel):
    def __init__(
        self,
        config_fail_instance_count: int = None,
        config_fail_instance_list: List[UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList] = None,
        config_success_instance_count: int = None,
        config_success_instance_list: List[UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList] = None,
        total_instance_count: int = None,
    ):
        self.config_fail_instance_count = config_fail_instance_count
        self.config_fail_instance_list = config_fail_instance_list
        self.config_success_instance_count = config_success_instance_count
        self.config_success_instance_list = config_success_instance_list
        self.total_instance_count = total_instance_count

    def validate(self):
        if self.config_fail_instance_list:
            for k in self.config_fail_instance_list:
                if k:
                    k.validate()
        if self.config_success_instance_list:
            for k in self.config_success_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_fail_instance_count is not None:
            result['ConfigFailInstanceCount'] = self.config_fail_instance_count
        result['ConfigFailInstanceList'] = []
        if self.config_fail_instance_list is not None:
            for k in self.config_fail_instance_list:
                result['ConfigFailInstanceList'].append(k.to_map() if k else None)
        if self.config_success_instance_count is not None:
            result['ConfigSuccessInstanceCount'] = self.config_success_instance_count
        result['ConfigSuccessInstanceList'] = []
        if self.config_success_instance_list is not None:
            for k in self.config_success_instance_list:
                result['ConfigSuccessInstanceList'].append(k.to_map() if k else None)
        if self.total_instance_count is not None:
            result['TotalInstanceCount'] = self.total_instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFailInstanceCount') is not None:
            self.config_fail_instance_count = m.get('ConfigFailInstanceCount')
        self.config_fail_instance_list = []
        if m.get('ConfigFailInstanceList') is not None:
            for k in m.get('ConfigFailInstanceList'):
                temp_model = UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList()
                self.config_fail_instance_list.append(temp_model.from_map(k))
        if m.get('ConfigSuccessInstanceCount') is not None:
            self.config_success_instance_count = m.get('ConfigSuccessInstanceCount')
        self.config_success_instance_list = []
        if m.get('ConfigSuccessInstanceList') is not None:
            for k in m.get('ConfigSuccessInstanceList'):
                temp_model = UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList()
                self.config_success_instance_list.append(temp_model.from_map(k))
        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')
        return self


class UpdateAutoResourceOptimizeRulesAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        complete: bool = None,
        config_response: UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponse = None,
        fail: bool = None,
        is_finish: bool = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.complete = complete
        self.config_response = config_response
        self.fail = fail
        self.is_finish = is_finish
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

    def validate(self):
        if self.config_response:
            self.config_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete is not None:
            result['Complete'] = self.complete
        if self.config_response is not None:
            result['ConfigResponse'] = self.config_response.to_map()
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish
        if self.result_id is not None:
            result['ResultId'] = self.result_id
        if self.state is not None:
            result['State'] = self.state
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')
        if m.get('ConfigResponse') is not None:
            temp_model = UpdateAutoResourceOptimizeRulesAsyncResponseBodyDataConfigResponse()
            self.config_response = temp_model.from_map(m['ConfigResponse'])
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')
        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class UpdateAutoResourceOptimizeRulesAsyncResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: UpdateAutoResourceOptimizeRulesAsyncResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = UpdateAutoResourceOptimizeRulesAsyncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutoResourceOptimizeRulesAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAutoResourceOptimizeRulesAsyncResponseBody = None,
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
            temp_model = UpdateAutoResourceOptimizeRulesAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoSqlOptimizeStatusRequest(TeaModel):
    def __init__(
        self,
        instances: str = None,
        status: int = None,
    ):
        self.instances = instances
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateAutoSqlOptimizeStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        success: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutoSqlOptimizeStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateAutoSqlOptimizeStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = UpdateAutoSqlOptimizeStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutoSqlOptimizeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAutoSqlOptimizeStatusResponseBody = None,
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
            temp_model = UpdateAutoSqlOptimizeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoThrottleRulesAsyncRequest(TeaModel):
    def __init__(
        self,
        abnormal_duration: float = None,
        active_sessions: int = None,
        allow_throttle_end_time: str = None,
        allow_throttle_start_time: str = None,
        auto_kill_session: bool = None,
        console_context: str = None,
        cpu_session_relation: str = None,
        cpu_usage: float = None,
        instance_ids: str = None,
        max_throttle_time: float = None,
        result_id: str = None,
    ):
        self.abnormal_duration = abnormal_duration
        self.active_sessions = active_sessions
        self.allow_throttle_end_time = allow_throttle_end_time
        self.allow_throttle_start_time = allow_throttle_start_time
        self.auto_kill_session = auto_kill_session
        self.console_context = console_context
        self.cpu_session_relation = cpu_session_relation
        self.cpu_usage = cpu_usage
        self.instance_ids = instance_ids
        self.max_throttle_time = max_throttle_time
        self.result_id = result_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abnormal_duration is not None:
            result['AbnormalDuration'] = self.abnormal_duration
        if self.active_sessions is not None:
            result['ActiveSessions'] = self.active_sessions
        if self.allow_throttle_end_time is not None:
            result['AllowThrottleEndTime'] = self.allow_throttle_end_time
        if self.allow_throttle_start_time is not None:
            result['AllowThrottleStartTime'] = self.allow_throttle_start_time
        if self.auto_kill_session is not None:
            result['AutoKillSession'] = self.auto_kill_session
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context
        if self.cpu_session_relation is not None:
            result['CpuSessionRelation'] = self.cpu_session_relation
        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.max_throttle_time is not None:
            result['MaxThrottleTime'] = self.max_throttle_time
        if self.result_id is not None:
            result['ResultId'] = self.result_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalDuration') is not None:
            self.abnormal_duration = m.get('AbnormalDuration')
        if m.get('ActiveSessions') is not None:
            self.active_sessions = m.get('ActiveSessions')
        if m.get('AllowThrottleEndTime') is not None:
            self.allow_throttle_end_time = m.get('AllowThrottleEndTime')
        if m.get('AllowThrottleStartTime') is not None:
            self.allow_throttle_start_time = m.get('AllowThrottleStartTime')
        if m.get('AutoKillSession') is not None:
            self.auto_kill_session = m.get('AutoKillSession')
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')
        if m.get('CpuSessionRelation') is not None:
            self.cpu_session_relation = m.get('CpuSessionRelation')
        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MaxThrottleTime') is not None:
            self.max_throttle_time = m.get('MaxThrottleTime')
        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')
        return self


class UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        error_message: str = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.error_message = error_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList(TeaModel):
    def __init__(
        self,
        config_success: bool = None,
        instance_id: str = None,
    ):
        self.config_success = config_success
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_success is not None:
            result['ConfigSuccess'] = self.config_success
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigSuccess') is not None:
            self.config_success = m.get('ConfigSuccess')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponse(TeaModel):
    def __init__(
        self,
        config_fail_instance_count: int = None,
        config_fail_instance_list: List[UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList] = None,
        config_success_instance_count: int = None,
        config_success_instance_list: List[UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList] = None,
        total_instance_count: int = None,
    ):
        self.config_fail_instance_count = config_fail_instance_count
        self.config_fail_instance_list = config_fail_instance_list
        self.config_success_instance_count = config_success_instance_count
        self.config_success_instance_list = config_success_instance_list
        self.total_instance_count = total_instance_count

    def validate(self):
        if self.config_fail_instance_list:
            for k in self.config_fail_instance_list:
                if k:
                    k.validate()
        if self.config_success_instance_list:
            for k in self.config_success_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_fail_instance_count is not None:
            result['ConfigFailInstanceCount'] = self.config_fail_instance_count
        result['ConfigFailInstanceList'] = []
        if self.config_fail_instance_list is not None:
            for k in self.config_fail_instance_list:
                result['ConfigFailInstanceList'].append(k.to_map() if k else None)
        if self.config_success_instance_count is not None:
            result['ConfigSuccessInstanceCount'] = self.config_success_instance_count
        result['ConfigSuccessInstanceList'] = []
        if self.config_success_instance_list is not None:
            for k in self.config_success_instance_list:
                result['ConfigSuccessInstanceList'].append(k.to_map() if k else None)
        if self.total_instance_count is not None:
            result['TotalInstanceCount'] = self.total_instance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigFailInstanceCount') is not None:
            self.config_fail_instance_count = m.get('ConfigFailInstanceCount')
        self.config_fail_instance_list = []
        if m.get('ConfigFailInstanceList') is not None:
            for k in m.get('ConfigFailInstanceList'):
                temp_model = UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigFailInstanceList()
                self.config_fail_instance_list.append(temp_model.from_map(k))
        if m.get('ConfigSuccessInstanceCount') is not None:
            self.config_success_instance_count = m.get('ConfigSuccessInstanceCount')
        self.config_success_instance_list = []
        if m.get('ConfigSuccessInstanceList') is not None:
            for k in m.get('ConfigSuccessInstanceList'):
                temp_model = UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponseConfigSuccessInstanceList()
                self.config_success_instance_list.append(temp_model.from_map(k))
        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')
        return self


class UpdateAutoThrottleRulesAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        complete: bool = None,
        config_response: UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponse = None,
        fail: bool = None,
        is_finish: bool = None,
        result_id: str = None,
        state: str = None,
        timestamp: int = None,
    ):
        self.complete = complete
        self.config_response = config_response
        self.fail = fail
        self.is_finish = is_finish
        self.result_id = result_id
        self.state = state
        self.timestamp = timestamp

    def validate(self):
        if self.config_response:
            self.config_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.complete is not None:
            result['Complete'] = self.complete
        if self.config_response is not None:
            result['ConfigResponse'] = self.config_response.to_map()
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.is_finish is not None:
            result['IsFinish'] = self.is_finish
        if self.result_id is not None:
            result['ResultId'] = self.result_id
        if self.state is not None:
            result['State'] = self.state
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')
        if m.get('ConfigResponse') is not None:
            temp_model = UpdateAutoThrottleRulesAsyncResponseBodyDataConfigResponse()
            self.config_response = temp_model.from_map(m['ConfigResponse'])
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('IsFinish') is not None:
            self.is_finish = m.get('IsFinish')
        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class UpdateAutoThrottleRulesAsyncResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: UpdateAutoThrottleRulesAsyncResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = UpdateAutoThrottleRulesAsyncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutoThrottleRulesAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAutoThrottleRulesAsyncResponseBody = None,
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
            temp_model = UpdateAutoThrottleRulesAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


