# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ConfigurationSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ConfigurationSynchronizationJobRequestInitialization(TeaModel):
    def __init__(
        self,
        data_load: bool = None,
        structure_load: bool = None,
    ):
        self.data_load = data_load
        self.structure_load = structure_load

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_load is not None:
            result['DataLoad'] = self.data_load
        if self.structure_load is not None:
            result['StructureLoad'] = self.structure_load
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLoad') is not None:
            self.data_load = m.get('DataLoad')
        if m.get('StructureLoad') is not None:
            self.structure_load = m.get('StructureLoad')
        return self


class ConfigurationSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ConfigurationSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: ConfigurationSynchronizationJobRequestDestinationEndpoint = None,
        initialization: ConfigurationSynchronizationJobRequestInitialization = None,
        source_endpoint: ConfigurationSynchronizationJobRequestSourceEndpoint = None,
        owner_id: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_object: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.initialization = initialization
        self.source_endpoint = source_endpoint
        self.owner_id = owner_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_object = synchronization_object

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.initialization:
            self.initialization.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.initialization is not None:
            result['Initialization'] = self.initialization.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.synchronization_object is not None:
            result['SynchronizationObject'] = self.synchronization_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigurationSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('Initialization') is not None:
            temp_model = ConfigurationSynchronizationJobRequestInitialization()
            self.initialization = temp_model.from_map(m['Initialization'])
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigurationSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('SynchronizationObject') is not None:
            self.synchronization_object = m.get('SynchronizationObject')
        return self


class ConfigurationSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigurationSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigurationSynchronizationJobResponseBody = None,
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
            temp_model = ConfigurationSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureMigrationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        data_base_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        user_name: str = None,
    ):
        self.data_base_name = data_base_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.password = password
        self.port = port
        self.region = region
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureMigrationJobRequestMigrationMode(TeaModel):
    def __init__(
        self,
        data_intialization: bool = None,
        data_synchronization: bool = None,
        structure_intialization: bool = None,
    ):
        self.data_intialization = data_intialization
        self.data_synchronization = data_synchronization
        self.structure_intialization = structure_intialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_intialization is not None:
            result['DataIntialization'] = self.data_intialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_intialization is not None:
            result['StructureIntialization'] = self.structure_intialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIntialization') is not None:
            self.data_intialization = m.get('DataIntialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureIntialization') is not None:
            self.structure_intialization = m.get('StructureIntialization')
        return self


class ConfigureMigrationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        role: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.owner_id = owner_id
        self.password = password
        self.port = port
        self.region = region
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region is not None:
            result['Region'] = self.region
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureMigrationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: ConfigureMigrationJobRequestDestinationEndpoint = None,
        migration_mode: ConfigureMigrationJobRequestMigrationMode = None,
        source_endpoint: ConfigureMigrationJobRequestSourceEndpoint = None,
        checkpoint: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_object: str = None,
        migration_reserved: str = None,
        owner_id: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.source_endpoint = source_endpoint
        self.checkpoint = checkpoint
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_object = migration_object
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigureMigrationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = ConfigureMigrationJobRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureMigrationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ConfigureMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigureMigrationJobResponseBody = None,
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
            temp_model = ConfigureMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSubscriptionInstanceRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: str = None,
        role: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ConfigureSubscriptionInstanceRequestSubscriptionDataType(TeaModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        self.ddl = ddl
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['DDL'] = self.ddl
        if self.dml is not None:
            result['DML'] = self.dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        return self


class ConfigureSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: ConfigureSubscriptionInstanceRequestSourceEndpoint = None,
        subscription_data_type: ConfigureSubscriptionInstanceRequestSubscriptionDataType = None,
        owner_id: str = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_object: str = None,
    ):
        self.source_endpoint = source_endpoint
        self.subscription_data_type = subscription_data_type
        self.owner_id = owner_id
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.subscription_object = subscription_object

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('SubscriptionDataType') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionObject') is not None:
            self.subscription_object = m.get('SubscriptionObject')
        return self


class ConfigureSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigureSubscriptionInstanceResponseBody = None,
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
            temp_model = ConfigureSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        password: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.password = password
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureSynchronizationJobRequestPartitionKey(TeaModel):
    def __init__(
        self,
        modify_time_day: bool = None,
        modify_time_hour: bool = None,
        modify_time_minute: bool = None,
        modify_time_month: bool = None,
        modify_time_year: bool = None,
    ):
        self.modify_time_day = modify_time_day
        self.modify_time_hour = modify_time_hour
        self.modify_time_minute = modify_time_minute
        self.modify_time_month = modify_time_month
        self.modify_time_year = modify_time_year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time_day is not None:
            result['ModifyTime_Day'] = self.modify_time_day
        if self.modify_time_hour is not None:
            result['ModifyTime_Hour'] = self.modify_time_hour
        if self.modify_time_minute is not None:
            result['ModifyTime_Minute'] = self.modify_time_minute
        if self.modify_time_month is not None:
            result['ModifyTime_Month'] = self.modify_time_month
        if self.modify_time_year is not None:
            result['ModifyTime_Year'] = self.modify_time_year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime_Day') is not None:
            self.modify_time_day = m.get('ModifyTime_Day')
        if m.get('ModifyTime_Hour') is not None:
            self.modify_time_hour = m.get('ModifyTime_Hour')
        if m.get('ModifyTime_Minute') is not None:
            self.modify_time_minute = m.get('ModifyTime_Minute')
        if m.get('ModifyTime_Month') is not None:
            self.modify_time_month = m.get('ModifyTime_Month')
        if m.get('ModifyTime_Year') is not None:
            self.modify_time_year = m.get('ModifyTime_Year')
        return self


class ConfigureSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        owner_id: str = None,
        password: str = None,
        port: str = None,
        role: str = None,
        user_name: str = None,
    ):
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.owner_id = owner_id
        self.password = password
        self.port = port
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: ConfigureSynchronizationJobRequestDestinationEndpoint = None,
        partition_key: ConfigureSynchronizationJobRequestPartitionKey = None,
        source_endpoint: ConfigureSynchronizationJobRequestSourceEndpoint = None,
        checkpoint: str = None,
        data_initialization: bool = None,
        migration_reserved: str = None,
        owner_id: str = None,
        structure_initialization: bool = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.partition_key = partition_key
        self.source_endpoint = source_endpoint
        self.checkpoint = checkpoint
        self.data_initialization = data_initialization
        self.migration_reserved = migration_reserved
        self.owner_id = owner_id
        self.structure_initialization = structure_initialization
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_objects = synchronization_objects

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.partition_key:
            self.partition_key.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('PartitionKey') is not None:
            temp_model = ConfigureSynchronizationJobRequestPartitionKey()
            self.partition_key = temp_model.from_map(m['PartitionKey'])
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        return self


class ConfigureSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfigureSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigureSynchronizationJobResponseBody = None,
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
            temp_model = ConfigureSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMigrationJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        migration_job_class: str = None,
        owner_id: str = None,
        region: str = None,
    ):
        self.client_token = client_token
        self.migration_job_class = migration_job_class
        self.owner_id = owner_id
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        migration_job_id: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.migration_job_id = migration_job_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMigrationJobResponseBody = None,
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
            temp_model = CreateMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        region: str = None,
        used_time: int = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.pay_type = pay_type
        self.period = period
        self.region = region
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.region is not None:
            result['Region'] = self.region
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class CreateSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        subscription_instance_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.subscription_instance_id = subscription_instance_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSubscriptionInstanceResponseBody = None,
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
            temp_model = CreateSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class CreateSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: CreateSynchronizationJobRequestDestinationEndpoint = None,
        source_endpoint: CreateSynchronizationJobRequestSourceEndpoint = None,
        client_token: str = None,
        dest_region: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        source_region: str = None,
        synchronization_job_class: str = None,
        used_time: int = None,
        network_type: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.source_endpoint = source_endpoint
        self.client_token = client_token
        self.dest_region = dest_region
        self.owner_id = owner_id
        self.pay_type = pay_type
        self.period = period
        self.source_region = source_region
        self.synchronization_job_class = synchronization_job_class
        self.used_time = used_time
        self.network_type = network_type

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.network_type is not None:
            result['networkType'] = self.network_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('SourceEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        return self


class CreateSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        synchronization_job_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class CreateSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSynchronizationJobResponseBody = None,
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
            temp_model = CreateSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMigrationJobRequest(TeaModel):
    def __init__(
        self,
        migration_job_id: str = None,
        owner_id: str = None,
    ):
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DeleteMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMigrationJobResponseBody = None,
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
            temp_model = DeleteMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DeleteSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSubscriptionInstanceResponseBody = None,
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
            temp_model = DeleteSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        synchronization_job_id: str = None,
    ):
        self.owner_id = owner_id
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DeleteSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSynchronizationJobResponseBody = None,
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
            temp_model = DeleteSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescirbeMigrationJobsRequest(TeaModel):
    def __init__(
        self,
        migration_job_name: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.migration_job_name = migration_job_name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization(TeaModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        self.database_name = database_name
        self.table_list = table_list
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableList') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for k in self.synchronous_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k in self.synchronous_object:
                result['SynchronousObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k in m.get('SynchronousObject'):
                temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck(TeaModel):
    def __init__(
        self,
        percent: str = None,
        status: str = None,
    ):
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJob(TeaModel):
    def __init__(
        self,
        data_initialization: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization = None,
        data_synchronization: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization = None,
        destination_endpoint: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint = None,
        migration_job_class: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        migration_mode: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode = None,
        migration_object: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject = None,
        pay_type: str = None,
        precheck: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck = None,
        source_endpoint: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint = None,
        structure_initialization: DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.destination_endpoint = destination_endpoint
        self.migration_job_class = migration_job_class
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_job_status = migration_job_status
        self.migration_mode = migration_mode
        self.migration_object = migration_object
        self.pay_type = pay_type
        self.precheck = precheck
        self.source_endpoint = source_endpoint
        self.structure_initialization = structure_initialization

    def validate(self):
        if self.data_initialization:
            self.data_initialization.validate()
        if self.data_synchronization:
            self.data_synchronization.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.migration_object:
            self.migration_object.validate()
        if self.precheck:
            self.precheck.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization:
            self.structure_initialization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization.to_map()
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.migration_job_id is not None:
            result['MigrationJobID'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_job_status is not None:
            result['MigrationJobStatus'] = self.migration_job_status
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object.to_map()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.precheck is not None:
            result['Precheck'] = self.precheck.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization()
            self.data_initialization = temp_model.from_map(m['DataInitialization'])
        if m.get('DataSynchronization') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization()
            self.data_synchronization = temp_model.from_map(m['DataSynchronization'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('MigrationJobID') is not None:
            self.migration_job_id = m.get('MigrationJobID')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')
        if m.get('MigrationMode') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('MigrationObject') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject()
            self.migration_object = temp_model.from_map(m['MigrationObject'])
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Precheck') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck()
            self.precheck = temp_model.from_map(m['Precheck'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitialization') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization()
            self.structure_initialization = temp_model.from_map(m['StructureInitialization'])
        return self


class DescirbeMigrationJobsResponseBodyMigrationJobs(TeaModel):
    def __init__(
        self,
        migration_job: List[DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJob] = None,
    ):
        self.migration_job = migration_job

    def validate(self):
        if self.migration_job:
            for k in self.migration_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MigrationJob'] = []
        if self.migration_job is not None:
            for k in self.migration_job:
                result['MigrationJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migration_job = []
        if m.get('MigrationJob') is not None:
            for k in m.get('MigrationJob'):
                temp_model = DescirbeMigrationJobsResponseBodyMigrationJobsMigrationJob()
                self.migration_job.append(temp_model.from_map(k))
        return self


class DescirbeMigrationJobsResponseBody(TeaModel):
    def __init__(
        self,
        migration_jobs: DescirbeMigrationJobsResponseBodyMigrationJobs = None,
        page_number: int = None,
        page_record_count: int = None,
        total_record_count: int = None,
    ):
        self.migration_jobs = migration_jobs
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count

    def validate(self):
        if self.migration_jobs:
            self.migration_jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_jobs is not None:
            result['MigrationJobs'] = self.migration_jobs.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobs') is not None:
            temp_model = DescirbeMigrationJobsResponseBodyMigrationJobs()
            self.migration_jobs = temp_model.from_map(m['MigrationJobs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescirbeMigrationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescirbeMigrationJobsResponseBody = None,
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
            temp_model = DescirbeMigrationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInitializationStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        synchronization_job_id: str = None,
    ):
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeInitializationStatusResponseBodyDataInitializationDetails(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
        total_row_num: str = None,
        used_time: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.finish_row_num = finish_row_num
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name
        self.total_row_num = total_row_num
        self.used_time = used_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_row_num is not None:
            result['FinishRowNum'] = self.finish_row_num
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TotalRowNum') is not None:
            self.total_row_num = m.get('TotalRowNum')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class DescribeInitializationStatusResponseBodyDataSynchronizationDetails(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInitializationStatusResponseBodyStructureInitializationDetails(TeaModel):
    def __init__(
        self,
        constraints: List[DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints] = None,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.constraints = constraints
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        if self.constraints:
            for k in self.constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Constraints'] = []
        if self.constraints is not None:
            for k in self.constraints:
                result['Constraints'].append(k.to_map() if k else None)
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constraints = []
        if m.get('Constraints') is not None:
            for k in m.get('Constraints'):
                temp_model = DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints()
                self.constraints.append(temp_model.from_map(k))
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeInitializationStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_details: List[DescribeInitializationStatusResponseBodyDataInitializationDetails] = None,
        data_synchronization_details: List[DescribeInitializationStatusResponseBodyDataSynchronizationDetails] = None,
        structure_initialization_details: List[DescribeInitializationStatusResponseBodyStructureInitializationDetails] = None,
    ):
        self.data_initialization_details = data_initialization_details
        self.data_synchronization_details = data_synchronization_details
        self.structure_initialization_details = structure_initialization_details

    def validate(self):
        if self.data_initialization_details:
            for k in self.data_initialization_details:
                if k:
                    k.validate()
        if self.data_synchronization_details:
            for k in self.data_synchronization_details:
                if k:
                    k.validate()
        if self.structure_initialization_details:
            for k in self.structure_initialization_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataInitializationDetails'] = []
        if self.data_initialization_details is not None:
            for k in self.data_initialization_details:
                result['DataInitializationDetails'].append(k.to_map() if k else None)
        result['DataSynchronizationDetails'] = []
        if self.data_synchronization_details is not None:
            for k in self.data_synchronization_details:
                result['DataSynchronizationDetails'].append(k.to_map() if k else None)
        result['StructureInitializationDetails'] = []
        if self.structure_initialization_details is not None:
            for k in self.structure_initialization_details:
                result['StructureInitializationDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_initialization_details = []
        if m.get('DataInitializationDetails') is not None:
            for k in m.get('DataInitializationDetails'):
                temp_model = DescribeInitializationStatusResponseBodyDataInitializationDetails()
                self.data_initialization_details.append(temp_model.from_map(k))
        self.data_synchronization_details = []
        if m.get('DataSynchronizationDetails') is not None:
            for k in m.get('DataSynchronizationDetails'):
                temp_model = DescribeInitializationStatusResponseBodyDataSynchronizationDetails()
                self.data_synchronization_details.append(temp_model.from_map(k))
        self.structure_initialization_details = []
        if m.get('StructureInitializationDetails') is not None:
            for k in m.get('StructureInitializationDetails'):
                temp_model = DescribeInitializationStatusResponseBodyStructureInitializationDetails()
                self.structure_initialization_details.append(temp_model.from_map(k))
        return self


class DescribeInitializationStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInitializationStatusResponseBody = None,
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
            temp_model = DescribeInitializationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobDetailRequestMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeMigrationJobDetailRequest(TeaModel):
    def __init__(
        self,
        migration_mode: DescribeMigrationJobDetailRequestMigrationMode = None,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.migration_mode = migration_mode
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        if self.migration_mode:
            self.migration_mode.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobDetailRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        migration_time: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
        total_row_num: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.finish_row_num = finish_row_num
        self.migration_time = migration_time
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name
        self.total_row_num = total_row_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_row_num is not None:
            result['FinishRowNum'] = self.finish_row_num
        if self.migration_time is not None:
            result['MigrationTime'] = self.migration_time
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')
        if m.get('MigrationTime') is not None:
            self.migration_time = m.get('MigrationTime')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('TotalRowNum') is not None:
            self.total_row_num = m.get('TotalRowNum')
        return self


class DescribeMigrationJobDetailResponseBodyDataInitializationDetailList(TeaModel):
    def __init__(
        self,
        data_initialization_detail: List[DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail] = None,
    ):
        self.data_initialization_detail = data_initialization_detail

    def validate(self):
        if self.data_initialization_detail:
            for k in self.data_initialization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataInitializationDetail'] = []
        if self.data_initialization_detail is not None:
            for k in self.data_initialization_detail:
                result['DataInitializationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_initialization_detail = []
        if m.get('DataInitializationDetail') is not None:
            for k in m.get('DataInitializationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail()
                self.data_initialization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        return self


class DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList(TeaModel):
    def __init__(
        self,
        data_synchronization_detail: List[DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail] = None,
    ):
        self.data_synchronization_detail = data_synchronization_detail

    def validate(self):
        if self.data_synchronization_detail:
            for k in self.data_synchronization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSynchronizationDetail'] = []
        if self.data_synchronization_detail is not None:
            for k in self.data_synchronization_detail:
                result['DataSynchronizationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_synchronization_detail = []
        if m.get('DataSynchronizationDetail') is not None:
            for k in m.get('DataSynchronizationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailListDataSynchronizationDetail()
                self.data_synchronization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail(TeaModel):
    def __init__(
        self,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList(TeaModel):
    def __init__(
        self,
        structure_initialization_detail: List[DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail] = None,
    ):
        self.structure_initialization_detail = structure_initialization_detail

    def validate(self):
        if self.structure_initialization_detail:
            for k in self.structure_initialization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StructureInitializationDetail'] = []
        if self.structure_initialization_detail is not None:
            for k in self.structure_initialization_detail:
                result['StructureInitializationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.structure_initialization_detail = []
        if m.get('StructureInitializationDetail') is not None:
            for k in m.get('StructureInitializationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintListStructureInitializationDetail()
                self.structure_initialization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail(TeaModel):
    def __init__(
        self,
        constraint_list: DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList = None,
        destination_owner_dbname: str = None,
        error_message: str = None,
        object_definition: str = None,
        object_name: str = None,
        object_type: str = None,
        source_owner_dbname: str = None,
        status: str = None,
    ):
        self.constraint_list = constraint_list
        self.destination_owner_dbname = destination_owner_dbname
        self.error_message = error_message
        self.object_definition = object_definition
        self.object_name = object_name
        self.object_type = object_type
        self.source_owner_dbname = source_owner_dbname
        self.status = status

    def validate(self):
        if self.constraint_list:
            self.constraint_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_list is not None:
            result['ConstraintList'] = self.constraint_list.to_map()
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList()
            self.constraint_list = temp_model.from_map(m['ConstraintList'])
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList(TeaModel):
    def __init__(
        self,
        structure_initialization_detail: List[DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail] = None,
    ):
        self.structure_initialization_detail = structure_initialization_detail

    def validate(self):
        if self.structure_initialization_detail:
            for k in self.structure_initialization_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StructureInitializationDetail'] = []
        if self.structure_initialization_detail is not None:
            for k in self.structure_initialization_detail:
                result['StructureInitializationDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.structure_initialization_detail = []
        if m.get('StructureInitializationDetail') is not None:
            for k in m.get('StructureInitializationDetail'):
                temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetail()
                self.structure_initialization_detail.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_detail_list: DescribeMigrationJobDetailResponseBodyDataInitializationDetailList = None,
        data_synchronization_detail_list: DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList = None,
        page_number: int = None,
        page_record_count: int = None,
        structure_initialization_detail_list: DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList = None,
        total_record_count: int = None,
    ):
        self.data_initialization_detail_list = data_initialization_detail_list
        self.data_synchronization_detail_list = data_synchronization_detail_list
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.structure_initialization_detail_list = structure_initialization_detail_list
        self.total_record_count = total_record_count

    def validate(self):
        if self.data_initialization_detail_list:
            self.data_initialization_detail_list.validate()
        if self.data_synchronization_detail_list:
            self.data_synchronization_detail_list.validate()
        if self.structure_initialization_detail_list:
            self.structure_initialization_detail_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization_detail_list is not None:
            result['DataInitializationDetailList'] = self.data_initialization_detail_list.to_map()
        if self.data_synchronization_detail_list is not None:
            result['DataSynchronizationDetailList'] = self.data_synchronization_detail_list.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.structure_initialization_detail_list is not None:
            result['StructureInitializationDetailList'] = self.structure_initialization_detail_list.to_map()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyDataInitializationDetailList()
            self.data_initialization_detail_list = temp_model.from_map(m['DataInitializationDetailList'])
        if m.get('DataSynchronizationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList()
            self.data_synchronization_detail_list = temp_model.from_map(m['DataSynchronizationDetailList'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('StructureInitializationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList()
            self.structure_initialization_detail_list = temp_model.from_map(m['StructureInitializationDetailList'])
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeMigrationJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMigrationJobDetailResponseBody = None,
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
            temp_model = DescribeMigrationJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
    ):
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeMigrationJobStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.checkpoint = checkpoint
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        oracle_sid: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.oracle_sid = oracle_sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.oracle_sid is not None:
            result['oracleSID'] = self.oracle_sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('oracleSID') is not None:
            self.oracle_sid = m.get('oracleSID')
        return self


class DescribeMigrationJobStatusResponseBodyMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['dataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['dataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['structureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataInitialization') is not None:
            self.data_initialization = m.get('dataInitialization')
        if m.get('dataSynchronization') is not None:
            self.data_synchronization = m.get('dataSynchronization')
        if m.get('structureInitialization') is not None:
            self.structure_initialization = m.get('structureInitialization')
        return self


class DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_item: List[DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem] = None,
    ):
        self.check_item = check_item

    def validate(self):
        if self.check_item:
            for k in self.check_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItem'] = []
        if self.check_item is not None:
            for k in self.check_item:
                result['CheckItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_item = []
        if m.get('CheckItem') is not None:
            for k in m.get('CheckItem'):
                temp_model = DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem()
                self.check_item.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        oracle_sid: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.oracle_sid = oracle_sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.oracle_sid is not None:
            result['oracleSID'] = self.oracle_sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('oracleSID') is not None:
            self.oracle_sid = m.get('oracleSID')
        return self


class DescribeMigrationJobStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_status: DescribeMigrationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus = None,
        destination_endpoint: DescribeMigrationJobStatusResponseBodyDestinationEndpoint = None,
        migration_job_class: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        migration_mode: DescribeMigrationJobStatusResponseBodyMigrationMode = None,
        migration_object: str = None,
        pay_type: str = None,
        precheck_status: DescribeMigrationJobStatusResponseBodyPrecheckStatus = None,
        source_endpoint: DescribeMigrationJobStatusResponseBodySourceEndpoint = None,
        structure_initialization_status: DescribeMigrationJobStatusResponseBodyStructureInitializationStatus = None,
    ):
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.destination_endpoint = destination_endpoint
        self.migration_job_class = migration_job_class
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_job_status = migration_job_status
        self.migration_mode = migration_mode
        self.migration_object = migration_object
        self.pay_type = pay_type
        self.precheck_status = precheck_status
        self.source_endpoint = source_endpoint
        self.structure_initialization_status = structure_initialization_status

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_job_status is not None:
            result['MigrationJobStatus'] = self.migration_job_status
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeMigrationJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMigrationJobStatusResponseBody = None,
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
            temp_model = DescribeMigrationJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobsRequest(TeaModel):
    def __init__(
        self,
        migration_job_name: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.migration_job_name = migration_job_name
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization(TeaModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode(TeaModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        self.database_name = database_name
        self.table_list = table_list
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableList') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for k in self.synchronous_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k in self.synchronous_object:
                result['SynchronousObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k in m.get('SynchronousObject'):
                temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck(TeaModel):
    def __init__(
        self,
        percent: str = None,
        status: str = None,
    ):
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        oracle_sid: str = None,
        port: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
        self.port = port
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob(TeaModel):
    def __init__(
        self,
        data_initialization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization = None,
        data_synchronization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization = None,
        destination_endpoint: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint = None,
        migration_job_class: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        migration_mode: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode = None,
        migration_object: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject = None,
        pay_type: str = None,
        precheck: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck = None,
        source_endpoint: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint = None,
        structure_initialization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization = None,
    ):
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.destination_endpoint = destination_endpoint
        self.migration_job_class = migration_job_class
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_job_status = migration_job_status
        self.migration_mode = migration_mode
        self.migration_object = migration_object
        self.pay_type = pay_type
        self.precheck = precheck
        self.source_endpoint = source_endpoint
        self.structure_initialization = structure_initialization

    def validate(self):
        if self.data_initialization:
            self.data_initialization.validate()
        if self.data_synchronization:
            self.data_synchronization.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.migration_object:
            self.migration_object.validate()
        if self.precheck:
            self.precheck.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization:
            self.structure_initialization.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization.to_map()
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.migration_job_id is not None:
            result['MigrationJobID'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_job_status is not None:
            result['MigrationJobStatus'] = self.migration_job_status
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object.to_map()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.precheck is not None:
            result['Precheck'] = self.precheck.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization()
            self.data_initialization = temp_model.from_map(m['DataInitialization'])
        if m.get('DataSynchronization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization()
            self.data_synchronization = temp_model.from_map(m['DataSynchronization'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('MigrationJobID') is not None:
            self.migration_job_id = m.get('MigrationJobID')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('MigrationObject') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject()
            self.migration_object = temp_model.from_map(m['MigrationObject'])
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Precheck') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck()
            self.precheck = temp_model.from_map(m['Precheck'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitialization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization()
            self.structure_initialization = temp_model.from_map(m['StructureInitialization'])
        return self


class DescribeMigrationJobsResponseBodyMigrationJobs(TeaModel):
    def __init__(
        self,
        migration_job: List[DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob] = None,
    ):
        self.migration_job = migration_job

    def validate(self):
        if self.migration_job:
            for k in self.migration_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MigrationJob'] = []
        if self.migration_job is not None:
            for k in self.migration_job:
                result['MigrationJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migration_job = []
        if m.get('MigrationJob') is not None:
            for k in m.get('MigrationJob'):
                temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob()
                self.migration_job.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobsResponseBody(TeaModel):
    def __init__(
        self,
        migration_jobs: DescribeMigrationJobsResponseBodyMigrationJobs = None,
        page_number: int = None,
        page_record_count: int = None,
        total_record_count: int = None,
    ):
        self.migration_jobs = migration_jobs
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count

    def validate(self):
        if self.migration_jobs:
            self.migration_jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_jobs is not None:
            result['MigrationJobs'] = self.migration_jobs.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobs') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobs()
            self.migration_jobs = temp_model.from_map(m['MigrationJobs'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeMigrationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeMigrationJobsResponseBody = None,
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
            temp_model = DescribeMigrationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType(TeaModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        self.ddl = ddl
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['DDL'] = self.ddl
        if self.dml is not None:
            result['DML'] = self.dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        self.database_name = database_name
        self.table_list = table_list
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableList') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for k in self.synchronous_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k in self.synchronous_object:
                result['SynchronousObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k in m.get('SynchronousObject'):
                temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        begin_timestamp: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        end_timestamp: str = None,
        error_message: str = None,
        pay_type: str = None,
        source_endpoint: DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint = None,
        status: str = None,
        subscription_data_type: DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_object: DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject = None,
    ):
        self.begin_timestamp = begin_timestamp
        self.consumption_checkpoint = consumption_checkpoint
        self.consumption_client = consumption_client
        self.end_timestamp = end_timestamp
        self.error_message = error_message
        self.pay_type = pay_type
        self.source_endpoint = source_endpoint
        self.status = status
        self.subscription_data_type = subscription_data_type
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.subscription_object = subscription_object

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_object:
            self.subscription_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionObject') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject()
            self.subscription_object = temp_model.from_map(m['SubscriptionObject'])
        return self


class DescribeSubscriptionInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSubscriptionInstanceStatusResponseBody = None,
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
            temp_model = DescribeSubscriptionInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        subscription_instance_name: str = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.subscription_instance_name = subscription_instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType(TeaModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        self.ddl = ddl
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl is not None:
            result['DDL'] = self.ddl
        if self.dml is not None:
            result['DML'] = self.dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        self.database_name = database_name
        self.table_list = table_list
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('TableList') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for k in self.synchronous_object:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k in self.synchronous_object:
                result['SynchronousObject'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k in m.get('SynchronousObject'):
                temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance(TeaModel):
    def __init__(
        self,
        begin_timestamp: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        end_timestamp: str = None,
        error_message: str = None,
        pay_type: str = None,
        source_endpoint: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint = None,
        status: str = None,
        subscription_data_type: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_object: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject = None,
    ):
        self.begin_timestamp = begin_timestamp
        self.consumption_checkpoint = consumption_checkpoint
        self.consumption_client = consumption_client
        self.end_timestamp = end_timestamp
        self.error_message = error_message
        self.pay_type = pay_type
        self.source_endpoint = source_endpoint
        self.status = status
        self.subscription_data_type = subscription_data_type
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.subscription_object = subscription_object

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_object:
            self.subscription_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionObject') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject()
            self.subscription_object = temp_model.from_map(m['SubscriptionObject'])
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstances(TeaModel):
    def __init__(
        self,
        subscription_instance: List[DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance] = None,
    ):
        self.subscription_instance = subscription_instance

    def validate(self):
        if self.subscription_instance:
            for k in self.subscription_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubscriptionInstance'] = []
        if self.subscription_instance is not None:
            for k in self.subscription_instance:
                result['SubscriptionInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_instance = []
        if m.get('SubscriptionInstance') is not None:
            for k in m.get('SubscriptionInstance'):
                temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance()
                self.subscription_instance.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstancesResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_record_count: int = None,
        subscription_instances: DescribeSubscriptionInstancesResponseBodySubscriptionInstances = None,
        total_record_count: int = None,
    ):
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.subscription_instances = subscription_instances
        self.total_record_count = total_record_count

    def validate(self):
        if self.subscription_instances:
            self.subscription_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.subscription_instances is not None:
            result['SubscriptionInstances'] = self.subscription_instances.to_map()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('SubscriptionInstances') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstances()
            self.subscription_instances = temp_model.from_map(m['SubscriptionInstances'])
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSubscriptionInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSubscriptionInstancesResponseBody = None,
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
            temp_model = DescribeSubscriptionInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionObjectModifyStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class DescribeSubscriptionObjectModifyStatusResponseBodyDetailCheckItem(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSubscriptionObjectModifyStatusResponseBodyDetail(TeaModel):
    def __init__(
        self,
        check_item: List[DescribeSubscriptionObjectModifyStatusResponseBodyDetailCheckItem] = None,
    ):
        self.check_item = check_item

    def validate(self):
        if self.check_item:
            for k in self.check_item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckItem'] = []
        if self.check_item is not None:
            for k in self.check_item:
                result['CheckItem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_item = []
        if m.get('CheckItem') is not None:
            for k in m.get('CheckItem'):
                temp_model = DescribeSubscriptionObjectModifyStatusResponseBodyDetailCheckItem()
                self.check_item.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionObjectModifyStatusResponseBody(TeaModel):
    def __init__(
        self,
        detail: DescribeSubscriptionObjectModifyStatusResponseBodyDetail = None,
        percent: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            temp_model = DescribeSubscriptionObjectModifyStatusResponseBodyDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSubscriptionObjectModifyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSubscriptionObjectModifyStatusResponseBody = None,
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
            temp_model = DescribeSubscriptionObjectModifyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        synchronization_job_id: str = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.checkpoint = checkpoint
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSynchronizationJobStatusResponseBodyPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['FLOW'] = self.flow
        if self.rps is not None:
            result['RPS'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        return self


class DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationJobStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes(TeaModel):
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


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes(TeaModel):
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


class DescribeSynchronizationJobStatusResponseBodySynchronizationObjects(TeaModel):
    def __init__(
        self,
        new_schema_name: str = None,
        schema_name: str = None,
        table_excludes: List[DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes] = None,
        table_includes: List[DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes] = None,
    ):
        self.new_schema_name = new_schema_name
        self.schema_name = schema_name
        self.table_excludes = table_excludes
        self.table_includes = table_includes

    def validate(self):
        if self.table_excludes:
            for k in self.table_excludes:
                if k:
                    k.validate()
        if self.table_includes:
            for k in self.table_includes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        result['TableExcludes'] = []
        if self.table_excludes is not None:
            for k in self.table_excludes:
                result['TableExcludes'].append(k.to_map() if k else None)
        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k in self.table_includes:
                result['TableIncludes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        self.table_excludes = []
        if m.get('TableExcludes') is not None:
            for k in m.get('TableExcludes'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k))
        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k in m.get('TableIncludes'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        checkpoint: str = None,
        data_initialization: str = None,
        data_initialization_status: DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus = None,
        delay: str = None,
        destination_endpoint: DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint = None,
        error_message: str = None,
        expire_time: str = None,
        pay_type: str = None,
        performance: DescribeSynchronizationJobStatusResponseBodyPerformance = None,
        precheck_status: DescribeSynchronizationJobStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        source_endpoint: DescribeSynchronizationJobStatusResponseBodySourceEndpoint = None,
        status: str = None,
        structure_initialization: str = None,
        structure_initialization_status: DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus = None,
        synchronization_job_class: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: List[DescribeSynchronizationJobStatusResponseBodySynchronizationObjects] = None,
    ):
        self.checkpoint = checkpoint
        self.data_initialization = data_initialization
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.delay = delay
        self.destination_endpoint = destination_endpoint
        self.error_message = error_message
        self.expire_time = expire_time
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.request_id = request_id
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization = structure_initialization
        self.structure_initialization_status = structure_initialization_status
        self.synchronization_job_class = synchronization_job_class
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_objects = synchronization_objects

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.synchronization_objects:
            for k in self.synchronization_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k in m.get('SynchronizationObjects'):
                temp_model = DescribeSynchronizationJobStatusResponseBodySynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSynchronizationJobStatusResponseBody = None,
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
            temp_model = DescribeSynchronizationJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        page_num: int = None,
        page_size: int = None,
        synchronization_job_name: str = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.page_num = page_num
        self.page_size = page_size
        self.synchronization_job_name = synchronization_job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance(TeaModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        self.flow = flow
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flow is not None:
            result['FLOW'] = self.flow
        if self.rps is not None:
            result['RPS'] = self.rps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes(TeaModel):
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


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes(TeaModel):
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


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects(TeaModel):
    def __init__(
        self,
        new_schema_name: str = None,
        schema_name: str = None,
        table_excludes: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes] = None,
        table_includes: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes] = None,
    ):
        self.new_schema_name = new_schema_name
        self.schema_name = schema_name
        self.table_excludes = table_excludes
        self.table_includes = table_includes

    def validate(self):
        if self.table_excludes:
            for k in self.table_excludes:
                if k:
                    k.validate()
        if self.table_includes:
            for k in self.table_includes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name
        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name
        result['TableExcludes'] = []
        if self.table_excludes is not None:
            for k in self.table_excludes:
                result['TableExcludes'].append(k.to_map() if k else None)
        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k in self.table_includes:
                result['TableIncludes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')
        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')
        self.table_excludes = []
        if m.get('TableExcludes') is not None:
            for k in m.get('TableExcludes'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k))
        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k in m.get('TableIncludes'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstances(TeaModel):
    def __init__(
        self,
        data_initialization: str = None,
        data_initialization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus = None,
        delay: str = None,
        destination_endpoint: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint = None,
        error_message: str = None,
        expire_time: str = None,
        pay_type: str = None,
        performance: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance = None,
        precheck_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus = None,
        source_endpoint: DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint = None,
        status: str = None,
        structure_initialization: str = None,
        structure_initialization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus = None,
        synchronization_job_class: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects] = None,
    ):
        self.data_initialization = data_initialization
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.delay = delay
        self.destination_endpoint = destination_endpoint
        self.error_message = error_message
        self.expire_time = expire_time
        self.pay_type = pay_type
        self.performance = performance
        self.precheck_status = precheck_status
        self.source_endpoint = source_endpoint
        self.status = status
        self.structure_initialization = structure_initialization
        self.structure_initialization_status = structure_initialization_status
        self.synchronization_job_class = synchronization_job_class
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_objects = synchronization_objects

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.synchronization_objects:
            for k in self.synchronization_objects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k in m.get('SynchronizationObjects'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        synchronization_instances: List[DescribeSynchronizationJobsResponseBodySynchronizationInstances] = None,
        total_record_count: int = None,
    ):
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.synchronization_instances = synchronization_instances
        self.total_record_count = total_record_count

    def validate(self):
        if self.synchronization_instances:
            for k in self.synchronization_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SynchronizationInstances'] = []
        if self.synchronization_instances is not None:
            for k in self.synchronization_instances:
                result['SynchronizationInstances'].append(k.to_map() if k else None)
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.synchronization_instances = []
        if m.get('SynchronizationInstances') is not None:
            for k in m.get('SynchronizationInstances'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstances()
                self.synchronization_instances.append(temp_model.from_map(k))
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSynchronizationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSynchronizationJobsResponseBody = None,
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
            temp_model = DescribeSynchronizationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationObjectModifyStatusRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        owner_id: str = None,
        task_id: str = None,
    ):
        self.client_token = client_token
        self.owner_id = owner_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        self.delay = delay
        self.error_message = error_message
        self.percent = percent
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        self.check_status = check_status
        self.error_message = error_message
        self.item_name = item_name
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus(TeaModel):
    def __init__(
        self,
        detail: List[DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        self.detail = detail
        self.percent = percent
        self.status = status

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.percent = percent
        self.progress = progress
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBody(TeaModel):
    def __init__(
        self,
        data_initialization_status: DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus = None,
        error_message: str = None,
        precheck_status: DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        status: str = None,
        structure_initialization_status: DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus = None,
    ):
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.error_message = error_message
        self.precheck_status = precheck_status
        self.request_id = request_id
        self.status = status
        self.structure_initialization_status = structure_initialization_status

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeSynchronizationObjectModifyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSynchronizationObjectModifyStatusResponseBody = None,
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
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyConsumptionTimestampRequest(TeaModel):
    def __init__(
        self,
        consumption_timestamp: str = None,
        owner_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.consumption_timestamp = consumption_timestamp
        self.owner_id = owner_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumption_timestamp is not None:
            result['ConsumptionTimestamp'] = self.consumption_timestamp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumptionTimestamp') is not None:
            self.consumption_timestamp = m.get('ConsumptionTimestamp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class ModifyConsumptionTimestampResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyConsumptionTimestampResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyConsumptionTimestampResponseBody = None,
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
            temp_model = ModifyConsumptionTimestampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMigrationObjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        migration_job_id: str = None,
        migration_object: str = None,
        owner_id: str = None,
    ):
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.migration_object = migration_object
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ModifyMigrationObjectResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyMigrationObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyMigrationObjectResponseBody = None,
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
            temp_model = ModifyMigrationObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubscriptionObjectRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        subscription_instance_id: str = None,
        subscription_object: str = None,
    ):
        self.owner_id = owner_id
        self.subscription_instance_id = subscription_instance_id
        self.subscription_object = subscription_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('SubscriptionObject') is not None:
            self.subscription_object = m.get('SubscriptionObject')
        return self


class ModifySubscriptionObjectResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifySubscriptionObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySubscriptionObjectResponseBody = None,
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
            temp_model = ModifySubscriptionObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySynchronizationObjectRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        synchronization_job_id: str = None,
        synchronization_objects: str = None,
    ):
        self.owner_id = owner_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_objects = synchronization_objects

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        return self


class ModifySynchronizationObjectResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ModifySynchronizationObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifySynchronizationObjectResponseBody = None,
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
            temp_model = ModifySynchronizationObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMigrationJobRequest(TeaModel):
    def __init__(
        self,
        migration_job_id: str = None,
        owner_id: str = None,
    ):
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StartMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartMigrationJobResponseBody = None,
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
            temp_model = StartMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        subscription_instance_id: str = None,
    ):
        self.owner_id = owner_id
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        return self


class StartSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
        task_id: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StartSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSubscriptionInstanceResponseBody = None,
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
            temp_model = StartSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        synchronization_job_id: str = None,
    ):
        self.owner_id = owner_id
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class StartSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSynchronizationJobResponseBody = None,
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
            temp_model = StartSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMigrationJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
    ):
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class StopMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopMigrationJobResponseBody = None,
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
            temp_model = StopMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendMigrationJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
    ):
        self.client_token = client_token
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class SuspendMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendMigrationJobResponseBody = None,
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
            temp_model = SuspendMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        synchronization_job_id: str = None,
    ):
        self.owner_id = owner_id
        self.synchronization_job_id = synchronization_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        return self


class SuspendSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SuspendSynchronizationJobResponseBody = None,
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
            temp_model = SuspendSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


