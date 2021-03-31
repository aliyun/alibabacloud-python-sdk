# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AccessHDMInstanceRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
        instance_area: str = None,
        instance_id: str = None,
        ip: str = None,
        port: str = None,
        engine: str = None,
        username: str = None,
        password: str = None,
        instance_alias: str = None,
        network_type: str = None,
        vpc_id: str = None,
        region: str = None,
        caller_bid: str = None,
        owner_id: str = None,
        tenant_id: str = None,
        owner_id_signature: str = None,
        caller_type: str = None,
        caller_uid: str = None,
        target: str = None,
        product: str = None,
        external: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id
        self.instance_area = instance_area
        self.instance_id = instance_id
        self.ip = ip
        self.port = port
        self.engine = engine
        self.username = username
        self.password = password
        self.instance_alias = instance_alias
        self.network_type = network_type
        self.vpc_id = vpc_id
        self.region = region
        self.caller_bid = caller_bid
        self.owner_id = owner_id
        self.tenant_id = tenant_id
        self.owner_id_signature = owner_id_signature
        self.caller_type = caller_type
        self.caller_uid = caller_uid
        self.target = target
        self.product = product
        self.external = external

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region is not None:
            result['Region'] = self.region
        if self.caller_bid is not None:
            result['CallerBid'] = self.caller_bid
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.owner_id_signature is not None:
            result['OwnerIdSignature'] = self.owner_id_signature
        if self.caller_type is not None:
            result['CallerType'] = self.caller_type
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.target is not None:
            result['Target'] = self.target
        if self.product is not None:
            result['Product'] = self.product
        if self.external is not None:
            result['External'] = self.external
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('CallerBid') is not None:
            self.caller_bid = m.get('CallerBid')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('OwnerIdSignature') is not None:
            self.owner_id_signature = m.get('OwnerIdSignature')
        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('External') is not None:
            self.external = m.get('External')
        return self


class AccessHDMInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AccessHDMInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AccessHDMInstanceResponseBody = None,
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
            temp_model = AccessHDMInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddHDMInstanceRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
        instance_area: str = None,
        instance_id: str = None,
        ip: str = None,
        port: str = None,
        engine: str = None,
        username: str = None,
        password: str = None,
        instance_alias: str = None,
        network_type: str = None,
        vpc_id: str = None,
        region: str = None,
        flush_account: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id
        self.instance_area = instance_area
        self.instance_id = instance_id
        self.ip = ip
        self.port = port
        self.engine = engine
        self.username = username
        self.password = password
        self.instance_alias = instance_alias
        self.network_type = network_type
        self.vpc_id = vpc_id
        self.region = region
        self.flush_account = flush_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.username is not None:
            result['Username'] = self.username
        if self.password is not None:
            result['Password'] = self.password
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.region is not None:
            result['Region'] = self.region
        if self.flush_account is not None:
            result['FlushAccount'] = self.flush_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('FlushAccount') is not None:
            self.flush_account = m.get('FlushAccount')
        return self


class AddHDMInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        token: str = None,
        ip: str = None,
        caller_uid: str = None,
        instance_id: str = None,
        port: int = None,
        owner_id: str = None,
        uuid: str = None,
        error: str = None,
        code: int = None,
        role: str = None,
        tenant_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.token = token
        self.ip = ip
        self.caller_uid = caller_uid
        self.instance_id = instance_id
        self.port = port
        self.owner_id = owner_id
        self.uuid = uuid
        self.error = error
        self.code = code
        self.role = role
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.token is not None:
            result['Token'] = self.token
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.error is not None:
            result['Error'] = self.error
        if self.code is not None:
            result['Code'] = self.code
        if self.role is not None:
            result['Role'] = self.role
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AddHDMInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        synchro: str = None,
        data: AddHDMInstanceResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.synchro = synchro
        self.data = data
        self.code = code
        self.success = success

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            temp_model = AddHDMInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddHDMInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddHDMInstanceResponseBody = None,
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
            temp_model = AddHDMInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCacheAnalysisJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        backup_set_id: str = None,
    ):
        self.instance_id = instance_id
        self.node_id = node_id
        self.backup_set_id = backup_set_id

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
        if self.backup_set_id is not None:
            result['BackupSetId'] = self.backup_set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('BackupSetId') is not None:
            self.backup_set_id = m.get('BackupSetId')
        return self


class CreateCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
        db: int = None,
        expiration_time_millis: int = None,
        key: str = None,
        encoding: str = None,
        bytes: int = None,
        node_id: str = None,
        count: int = None,
    ):
        self.type = type
        self.db = db
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.encoding = encoding
        self.bytes = bytes
        self.node_id = node_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.db is not None:
            result['Db'] = self.db
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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
        task_state: str = None,
        job_id: str = None,
        message: str = None,
        big_keys: CreateCacheAnalysisJobResponseBodyDataBigKeys = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.task_state = task_state
        self.job_id = job_id
        self.message = message
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('BigKeys') is not None:
            temp_model = CreateCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateCacheAnalysisJobResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: CreateCacheAnalysisJobResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCacheAnalysisJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCacheAnalysisJobResponseBody = None,
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
            temp_model = CreateCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiagnosticReportRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
        dbinstance_id: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id
        self.dbinstance_id = dbinstance_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class CreateDiagnosticReportResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDiagnosticReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDiagnosticReportResponseBody = None,
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
            temp_model = CreateDiagnosticReportResponseBody()
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


class DescribeCacheAnalysisJobResponseBodyDataKeyPrefixesPrefix(TeaModel):
    def __init__(
        self,
        key_num: int = None,
        type: str = None,
        bytes: int = None,
        prefix: str = None,
        count: int = None,
    ):
        self.key_num = key_num
        self.type = type
        self.bytes = bytes
        self.prefix = prefix
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_num is not None:
            result['KeyNum'] = self.key_num
        if self.type is not None:
            result['Type'] = self.type
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyNum') is not None:
            self.key_num = m.get('KeyNum')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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


class DescribeCacheAnalysisJobResponseBodyDataBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
        db: int = None,
        expiration_time_millis: int = None,
        key: str = None,
        encoding: str = None,
        bytes: int = None,
        node_id: str = None,
        count: int = None,
    ):
        self.type = type
        self.db = db
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.encoding = encoding
        self.bytes = bytes
        self.node_id = node_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.db is not None:
            result['Db'] = self.db
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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


class DescribeCacheAnalysisJobResponseBodyData(TeaModel):
    def __init__(
        self,
        task_state: str = None,
        job_id: str = None,
        key_prefixes: DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes = None,
        message: str = None,
        big_keys: DescribeCacheAnalysisJobResponseBodyDataBigKeys = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.task_state = task_state
        self.job_id = job_id
        self.key_prefixes = key_prefixes
        self.message = message
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        if self.key_prefixes:
            self.key_prefixes.validate()
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.key_prefixes is not None:
            result['KeyPrefixes'] = self.key_prefixes.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('KeyPrefixes') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataKeyPrefixes()
            self.key_prefixes = temp_model.from_map(m['KeyPrefixes'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyDataBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeCacheAnalysisJobResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeCacheAnalysisJobResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCacheAnalysisJobResponseBody = None,
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
            temp_model = DescribeCacheAnalysisJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCacheAnalysisJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_no = page_no
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
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeysKeyInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
        db: int = None,
        expiration_time_millis: int = None,
        key: str = None,
        encoding: str = None,
        bytes: int = None,
        node_id: str = None,
        count: int = None,
    ):
        self.type = type
        self.db = db
        self.expiration_time_millis = expiration_time_millis
        self.key = key
        self.encoding = encoding
        self.bytes = bytes
        self.node_id = node_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.db is not None:
            result['Db'] = self.db
        if self.expiration_time_millis is not None:
            result['ExpirationTimeMillis'] = self.expiration_time_millis
        if self.key is not None:
            result['Key'] = self.key
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.bytes is not None:
            result['Bytes'] = self.bytes
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('ExpirationTimeMillis') is not None:
            self.expiration_time_millis = m.get('ExpirationTimeMillis')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('Bytes') is not None:
            self.bytes = m.get('Bytes')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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
        task_state: str = None,
        job_id: str = None,
        message: str = None,
        big_keys: DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys = None,
        instance_id: str = None,
        node_id: str = None,
    ):
        self.task_state = task_state
        self.job_id = job_id
        self.message = message
        self.big_keys = big_keys
        self.instance_id = instance_id
        self.node_id = node_id

    def validate(self):
        if self.big_keys:
            self.big_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.big_keys is not None:
            result['BigKeys'] = self.big_keys.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('BigKeys') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataListCacheAnalysisJobBigKeys()
            self.big_keys = temp_model.from_map(m['BigKeys'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
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
        list: DescribeCacheAnalysisJobsResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        extra: str = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.extra = extra
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeCacheAnalysisJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: DescribeCacheAnalysisJobsResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeCacheAnalysisJobsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeCacheAnalysisJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeCacheAnalysisJobsResponseBody = None,
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
            temp_model = DescribeCacheAnalysisJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiagnosticReportListRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
        dbinstance_id: str = None,
        page_no: str = None,
        page_size: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id
        self.dbinstance_id = dbinstance_id
        self.page_no = page_no
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeDiagnosticReportListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeDiagnosticReportListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiagnosticReportListResponseBody = None,
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
            temp_model = DescribeDiagnosticReportListResponseBody()
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
        key: str = None,
        db: int = None,
        hot: str = None,
        key_type: str = None,
        size: int = None,
    ):
        self.key = key
        self.db = db
        self.hot = hot
        self.key_type = key_type
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.db is not None:
            result['Db'] = self.db
        if self.hot is not None:
            result['Hot'] = self.hot
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Db') is not None:
            self.db = m.get('Db')
        if m.get('Hot') is not None:
            self.hot = m.get('Hot')
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
        message: str = None,
        request_id: str = None,
        data: DescribeHotKeysResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeHotKeysResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeHotKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHotKeysResponseBody = None,
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
            temp_model = DescribeHotKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventContentRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        instance_id: str = None,
        span_id: str = None,
    ):
        self.context = context
        self.instance_id = instance_id
        self.span_id = span_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['__context'] = self.context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        return self


class GetAutonomousNotifyEventContentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventContentResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventDetailRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        instance_id: str = None,
        span_id: str = None,
    ):
        self.context = context
        self.instance_id = instance_id
        self.span_id = span_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['__context'] = self.context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.span_id is not None:
            result['SpanId'] = self.span_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')
        return self


class GetAutonomousNotifyEventDetailResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventDetailResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventsRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        node_id: str = None,
        event_context: str = None,
        level: str = None,
        min_level: str = None,
        page_offset: str = None,
        page_size: str = None,
    ):
        self.context = context
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.node_id = node_id
        self.event_context = event_context
        self.level = level
        self.min_level = min_level
        self.page_offset = page_offset
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['__context'] = self.context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.level is not None:
            result['Level'] = self.level
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        if m.get('PageOffset') is not None:
            self.page_offset = m.get('PageOffset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetAutonomousNotifyEventsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventsResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutonomousNotifyEventsInRangeRequest(TeaModel):
    def __init__(
        self,
        context: str = None,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        node_id: str = None,
        event_context: str = None,
        level: str = None,
        min_level: str = None,
        page_offset: str = None,
        page_size: str = None,
    ):
        self.context = context
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.node_id = node_id
        self.event_context = event_context
        self.level = level
        self.min_level = min_level
        self.page_offset = page_offset
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['__context'] = self.context
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.event_context is not None:
            result['EventContext'] = self.event_context
        if self.level is not None:
            result['Level'] = self.level
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        if self.page_offset is not None:
            result['PageOffset'] = self.page_offset
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('EventContext') is not None:
            self.event_context = m.get('EventContext')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        if m.get('PageOffset') is not None:
            self.page_offset = m.get('PageOffset')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
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
        list: GetAutonomousNotifyEventsInRangeResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        extra: str = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.extra = extra
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('List') is not None:
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetAutonomousNotifyEventsInRangeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAutonomousNotifyEventsInRangeResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAutonomousNotifyEventsInRangeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutonomousNotifyEventsInRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutonomousNotifyEventsInRangeResponseBody = None,
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
            temp_model = GetAutonomousNotifyEventsInRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoResourceOptimizeConfigRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        user_id: str = None,
        instance_id: str = None,
        context: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.user_id = user_id
        self.instance_id = instance_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetAutoResourceOptimizeConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAutoResourceOptimizeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAutoResourceOptimizeConfigResponseBody = None,
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
            temp_model = GetAutoResourceOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEndpointSwitchTaskRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
        task_id: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetEndpointSwitchTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        uuid: str = None,
        ori_uuid: str = None,
        account_id: str = None,
        err_msg: str = None,
        task_id: str = None,
        db_link_id: int = None,
    ):
        self.status = status
        self.uuid = uuid
        self.ori_uuid = ori_uuid
        self.account_id = account_id
        self.err_msg = err_msg
        self.task_id = task_id
        self.db_link_id = db_link_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.ori_uuid is not None:
            result['OriUuid'] = self.ori_uuid
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.db_link_id is not None:
            result['DbLinkId'] = self.db_link_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('OriUuid') is not None:
            self.ori_uuid = m.get('OriUuid')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('DbLinkId') is not None:
            self.db_link_id = m.get('DbLinkId')
        return self


class GetEndpointSwitchTaskResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        synchro: str = None,
        data: GetEndpointSwitchTaskResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.synchro = synchro
        self.data = data
        self.code = code
        self.success = success

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            temp_model = GetEndpointSwitchTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEndpointSwitchTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEndpointSwitchTaskResponseBody = None,
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
            temp_model = GetEndpointSwitchTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventOverviewRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: str = None,
        end_time: str = None,
        min_level: str = None,
    ):
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.min_level = min_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.min_level is not None:
            result['MinLevel'] = self.min_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MinLevel') is not None:
            self.min_level = m.get('MinLevel')
        return self


class GetEventOverviewResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetEventOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetEventOverviewResponseBody = None,
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
            temp_model = GetEventOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMAliyunResourceSyncResultRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
        task_id: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetHDMAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(
        self,
        sync_count: int = None,
        resource_type: str = None,
        success: bool = None,
        err_msg: str = None,
    ):
        self.sync_count = sync_count
        self.resource_type = resource_type
        self.success = success
        self.err_msg = err_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
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
        sync_status: str = None,
        error_msg: str = None,
        sub_results: GetHDMAliyunResourceSyncResultResponseBodyDataSubResults = None,
        results: str = None,
    ):
        self.sync_status = sync_status
        self.error_msg = error_msg
        self.sub_results = sub_results
        self.results = results

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('SubResults') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('Results') is not None:
            self.results = m.get('Results')
        return self


class GetHDMAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        synchro: str = None,
        data: GetHDMAliyunResourceSyncResultResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.synchro = synchro
        self.data = data
        self.code = code
        self.success = success

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            temp_model = GetHDMAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHDMAliyunResourceSyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHDMAliyunResourceSyncResultResponseBody = None,
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
            temp_model = GetHDMAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHDMLastAliyunResourceSyncResultRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResultsResourceSyncSubResult(TeaModel):
    def __init__(
        self,
        sync_count: int = None,
        resource_type: str = None,
        success: bool = None,
        err_msg: str = None,
    ):
        self.sync_count = sync_count
        self.resource_type = resource_type
        self.success = success
        self.err_msg = err_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sync_count is not None:
            result['SyncCount'] = self.sync_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.success is not None:
            result['Success'] = self.success
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SyncCount') is not None:
            self.sync_count = m.get('SyncCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
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
        sync_status: str = None,
        error_msg: str = None,
        sub_results: GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults = None,
        results: str = None,
    ):
        self.sync_status = sync_status
        self.error_msg = error_msg
        self.sub_results = sub_results
        self.results = results

    def validate(self):
        if self.sub_results:
            self.sub_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.sub_results is not None:
            result['SubResults'] = self.sub_results.to_map()
        if self.results is not None:
            result['Results'] = self.results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('SubResults') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyDataSubResults()
            self.sub_results = temp_model.from_map(m['SubResults'])
        if m.get('Results') is not None:
            self.results = m.get('Results')
        return self


class GetHDMLastAliyunResourceSyncResultResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        synchro: str = None,
        data: GetHDMLastAliyunResourceSyncResultResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.synchro = synchro
        self.data = data
        self.code = code
        self.success = success

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
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHDMLastAliyunResourceSyncResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHDMLastAliyunResourceSyncResultResponseBody = None,
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
            temp_model = GetHDMLastAliyunResourceSyncResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceInspectionsRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        start_time: str = None,
        end_time: str = None,
        page_no: str = None,
        page_size: str = None,
        instance_area: str = None,
        search_map: str = None,
    ):
        self.engine = engine
        self.start_time = start_time
        self.end_time = end_time
        self.page_no = page_no
        self.page_size = page_size
        self.instance_area = instance_area
        self.search_map = search_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.search_map is not None:
            result['SearchMap'] = self.search_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('SearchMap') is not None:
            self.search_map = m.get('SearchMap')
        return self


class GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        uuid: str = None,
        instance_area: str = None,
        instance_class: str = None,
        region: str = None,
        account_id: str = None,
        network_type: str = None,
        engine: str = None,
        instance_id: str = None,
        node_id: str = None,
        engine_version: str = None,
    ):
        self.vpc_id = vpc_id
        self.uuid = uuid
        self.instance_area = instance_area
        self.instance_class = instance_class
        self.region = region
        self.account_id = account_id
        self.network_type = network_type
        self.engine = engine
        self.instance_id = instance_id
        self.node_id = node_id
        self.engine_version = engine_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.region is not None:
            result['Region'] = self.region
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        return self


class GetInstanceInspectionsResponseBodyDataListBaseInspection(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        data: str = None,
        instance: GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance = None,
        score_map: str = None,
        gmt_create: int = None,
        score: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.data = data
        self.instance = instance
        self.score_map = score_map
        self.gmt_create = gmt_create
        self.score = score

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.data is not None:
            result['Data'] = self.data
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.score_map is not None:
            result['ScoreMap'] = self.score_map
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.score is not None:
            result['Score'] = self.score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Instance') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataListBaseInspectionInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('ScoreMap') is not None:
            self.score_map = m.get('ScoreMap')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        return self


class GetInstanceInspectionsResponseBodyDataList(TeaModel):
    def __init__(
        self,
        base_inspection: List[GetInstanceInspectionsResponseBodyDataListBaseInspection] = None,
    ):
        self.base_inspection = base_inspection

    def validate(self):
        if self.base_inspection:
            for k in self.base_inspection:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BaseInspection'] = []
        if self.base_inspection is not None:
            for k in self.base_inspection:
                result['BaseInspection'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.base_inspection = []
        if m.get('BaseInspection') is not None:
            for k in m.get('BaseInspection'):
                temp_model = GetInstanceInspectionsResponseBodyDataListBaseInspection()
                self.base_inspection.append(temp_model.from_map(k))
        return self


class GetInstanceInspectionsResponseBodyData(TeaModel):
    def __init__(
        self,
        list: GetInstanceInspectionsResponseBodyDataList = None,
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
            self.list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('List') is not None:
            temp_model = GetInstanceInspectionsResponseBodyDataList()
            self.list = temp_model.from_map(m['List'])
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
        message: str = None,
        request_id: str = None,
        data: GetInstanceInspectionsResponseBodyData = None,
        code: str = None,
        success: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetInstanceInspectionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInstanceInspectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceInspectionsResponseBody = None,
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
            temp_model = GetInstanceInspectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceOptimizeHistoryListRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        user_id: str = None,
        instance_id: str = None,
        page: int = None,
        page_size: int = None,
        context: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.user_id = user_id
        self.instance_id = instance_id
        self.page = page
        self.page_size = page_size
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class GetResourceOptimizeHistoryListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResourceOptimizeHistoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetResourceOptimizeHistoryListResponseBody = None,
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
            temp_model = GetResourceOptimizeHistoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopOrRollbackOptimizeTaskRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        user_id: str = None,
        instance_id: str = None,
        task_type: str = None,
        task_uuid: str = None,
        stop_or_rollback: str = None,
        context: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.user_id = user_id
        self.instance_id = instance_id
        self.task_type = task_type
        self.task_uuid = task_uuid
        self.stop_or_rollback = stop_or_rollback
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.stop_or_rollback is not None:
            result['StopOrRollback'] = self.stop_or_rollback
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('StopOrRollback') is not None:
            self.stop_or_rollback = m.get('StopOrRollback')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class StopOrRollbackOptimizeTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopOrRollbackOptimizeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopOrRollbackOptimizeTaskResponseBody = None,
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
            temp_model = StopOrRollbackOptimizeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncHDMAliyunResourceRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        timestamp: str = None,
        context: str = None,
        skip_auth: str = None,
        user_id: str = None,
        async_: str = None,
        wait_for_modify_security_ips: str = None,
        resource_types: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.timestamp = timestamp
        self.context = context
        self.skip_auth = skip_auth
        self.user_id = user_id
        self.async_ = async_
        self.wait_for_modify_security_ips = wait_for_modify_security_ips
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.signature is not None:
            result['signature'] = self.signature
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.context is not None:
            result['__context'] = self.context
        if self.skip_auth is not None:
            result['skipAuth'] = self.skip_auth
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.wait_for_modify_security_ips is not None:
            result['WaitForModifySecurityIps'] = self.wait_for_modify_security_ips
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        if m.get('skipAuth') is not None:
            self.skip_auth = m.get('skipAuth')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('WaitForModifySecurityIps') is not None:
            self.wait_for_modify_security_ips = m.get('WaitForModifySecurityIps')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class SyncHDMAliyunResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncHDMAliyunResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncHDMAliyunResourceResponseBody = None,
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
            temp_model = SyncHDMAliyunResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TurnOffAutoResourceOptimizeRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        user_id: str = None,
        instance_id: str = None,
        context: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.user_id = user_id
        self.instance_id = instance_id
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class TurnOffAutoResourceOptimizeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TurnOffAutoResourceOptimizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TurnOffAutoResourceOptimizeResponseBody = None,
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
            temp_model = TurnOffAutoResourceOptimizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAutoResourceOptimizeConfigRequest(TeaModel):
    def __init__(
        self,
        uid: str = None,
        access_key: str = None,
        signature: str = None,
        user_id: str = None,
        instance_id: str = None,
        auto_defragment: int = None,
        table_space_size: float = None,
        table_fragmentation_ratio: float = None,
        auto_duplicate_index_delete: int = None,
        context: str = None,
    ):
        self.uid = uid
        self.access_key = access_key
        self.signature = signature
        self.user_id = user_id
        self.instance_id = instance_id
        self.auto_defragment = auto_defragment
        self.table_space_size = table_space_size
        self.table_fragmentation_ratio = table_fragmentation_ratio
        self.auto_duplicate_index_delete = auto_duplicate_index_delete
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.auto_defragment is not None:
            result['AutoDefragment'] = self.auto_defragment
        if self.table_space_size is not None:
            result['TableSpaceSize'] = self.table_space_size
        if self.table_fragmentation_ratio is not None:
            result['TableFragmentationRatio'] = self.table_fragmentation_ratio
        if self.auto_duplicate_index_delete is not None:
            result['AutoDuplicateIndexDelete'] = self.auto_duplicate_index_delete
        if self.context is not None:
            result['__context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AutoDefragment') is not None:
            self.auto_defragment = m.get('AutoDefragment')
        if m.get('TableSpaceSize') is not None:
            self.table_space_size = m.get('TableSpaceSize')
        if m.get('TableFragmentationRatio') is not None:
            self.table_fragmentation_ratio = m.get('TableFragmentationRatio')
        if m.get('AutoDuplicateIndexDelete') is not None:
            self.auto_duplicate_index_delete = m.get('AutoDuplicateIndexDelete')
        if m.get('__context') is not None:
            self.context = m.get('__context')
        return self


class UpdateAutoResourceOptimizeConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        synchro: str = None,
        data: str = None,
        code: str = None,
        success: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.synchro = synchro
        self.data = data
        self.code = code
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
        if self.message is not None:
            result['Message'] = self.message
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAutoResourceOptimizeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAutoResourceOptimizeConfigResponseBody = None,
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
            temp_model = UpdateAutoResourceOptimizeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


