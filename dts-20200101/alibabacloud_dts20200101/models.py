# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ConfigureDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_job_name: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_region: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_user_name: str = None,
        source_endpoint_password: str = None,
        source_endpoint_owner_id: str = None,
        source_endpoint_role: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_engine_name: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_port: str = None,
        destination_endpoint_data_base_name: str = None,
        destination_endpoint_user_name: str = None,
        destination_endpoint_password: str = None,
        structure_initialization: bool = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        db_list: str = None,
        reserve: str = None,
        checkpoint: str = None,
        owner_id: str = None,
        destination_endpoint_oracle_sid: str = None,
        job_type: str = None,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        delay_phone: str = None,
        delay_rule_time: int = None,
        delay_notice: bool = None,
        error_phone: str = None,
        error_notice: bool = None,
        synchronization_direction: str = None,
        region_id: str = None,
    ):
        self.dts_job_name = dts_job_name
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_user_name = source_endpoint_user_name
        self.source_endpoint_password = source_endpoint_password
        self.source_endpoint_owner_id = source_endpoint_owner_id
        self.source_endpoint_role = source_endpoint_role
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        self.destination_endpoint_region = destination_endpoint_region
        self.destination_endpoint_ip = destination_endpoint_ip
        self.destination_endpoint_port = destination_endpoint_port
        self.destination_endpoint_data_base_name = destination_endpoint_data_base_name
        self.destination_endpoint_user_name = destination_endpoint_user_name
        self.destination_endpoint_password = destination_endpoint_password
        self.structure_initialization = structure_initialization
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.db_list = db_list
        self.reserve = reserve
        self.checkpoint = checkpoint
        self.owner_id = owner_id
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        self.job_type = job_type
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.delay_phone = delay_phone
        self.delay_rule_time = delay_rule_time
        self.delay_notice = delay_notice
        self.error_phone = error_phone
        self.error_notice = error_notice
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.source_endpoint_owner_id is not None:
            result['SourceEndpointOwnerID'] = self.source_endpoint_owner_id
        if self.source_endpoint_role is not None:
            result['SourceEndpointRole'] = self.source_endpoint_role
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip
        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port
        if self.destination_endpoint_data_base_name is not None:
            result['DestinationEndpointDataBaseName'] = self.destination_endpoint_data_base_name
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.reserve is not None:
            result['Reserve'] = self.reserve
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.delay_phone is not None:
            result['DelayPhone'] = self.delay_phone
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.delay_notice is not None:
            result['DelayNotice'] = self.delay_notice
        if self.error_phone is not None:
            result['ErrorPhone'] = self.error_phone
        if self.error_notice is not None:
            result['ErrorNotice'] = self.error_notice
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('SourceEndpointOwnerID') is not None:
            self.source_endpoint_owner_id = m.get('SourceEndpointOwnerID')
        if m.get('SourceEndpointRole') is not None:
            self.source_endpoint_role = m.get('SourceEndpointRole')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')
        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')
        if m.get('DestinationEndpointDataBaseName') is not None:
            self.destination_endpoint_data_base_name = m.get('DestinationEndpointDataBaseName')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('Reserve') is not None:
            self.reserve = m.get('Reserve')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DelayPhone') is not None:
            self.delay_phone = m.get('DelayPhone')
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('DelayNotice') is not None:
            self.delay_notice = m.get('DelayNotice')
        if m.get('ErrorPhone') is not None:
            self.error_phone = m.get('ErrorPhone')
        if m.get('ErrorNotice') is not None:
            self.error_notice = m.get('ErrorNotice')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigureDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureDtsJobResponseBody = None,
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
            temp_model = ConfigureDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureMigrationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        instance_id: str = None,
        engine_name: str = None,
        region: str = None,
        ip: str = None,
        port: str = None,
        oracle_sid: str = None,
        database_name: str = None,
        user_name: str = None,
        password: str = None,
        owner_id: str = None,
        role: str = None,
    ):
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.engine_name = engine_name
        self.region = region
        self.ip = ip
        self.port = port
        self.oracle_sid = oracle_sid
        self.database_name = database_name
        self.user_name = user_name
        self.password = password
        self.owner_id = owner_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.region is not None:
            result['Region'] = self.region
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ConfigureMigrationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        instance_id: str = None,
        engine_name: str = None,
        region: str = None,
        ip: str = None,
        port: str = None,
        data_base_name: str = None,
        user_name: str = None,
        password: str = None,
        oracle_sid: str = None,
    ):
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.engine_name = engine_name
        self.region = region
        self.ip = ip
        self.port = port
        self.data_base_name = data_base_name
        self.user_name = user_name
        self.password = password
        self.oracle_sid = oracle_sid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.region is not None:
            result['Region'] = self.region
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        return self


class ConfigureMigrationJobRequestMigrationMode(TeaModel):
    def __init__(
        self,
        structure_intialization: bool = None,
        data_intialization: bool = None,
        data_synchronization: bool = None,
    ):
        self.structure_intialization = structure_intialization
        self.data_intialization = data_intialization
        self.data_synchronization = data_synchronization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.structure_intialization is not None:
            result['StructureIntialization'] = self.structure_intialization
        if self.data_intialization is not None:
            result['DataIntialization'] = self.data_intialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StructureIntialization') is not None:
            self.structure_intialization = m.get('StructureIntialization')
        if m.get('DataIntialization') is not None:
            self.data_intialization = m.get('DataIntialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        return self


class ConfigureMigrationJobRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: ConfigureMigrationJobRequestSourceEndpoint = None,
        destination_endpoint: ConfigureMigrationJobRequestDestinationEndpoint = None,
        migration_mode: ConfigureMigrationJobRequestMigrationMode = None,
        region_id: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_object: str = None,
        migration_reserved: str = None,
        checkpoint: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.source_endpoint = source_endpoint
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_object = migration_object
        self.migration_reserved = migration_reserved
        self.checkpoint = checkpoint
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureMigrationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigureMigrationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = ConfigureMigrationJobRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ConfigureMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureMigrationJobResponseBody = None,
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
            temp_model = ConfigureMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureMigrationJobAlertRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        migration_job_id: str = None,
        delay_alert_status: str = None,
        delay_alert_phone: str = None,
        error_alert_status: str = None,
        error_alert_phone: str = None,
        delay_over_seconds: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.delay_alert_status = delay_alert_status
        self.delay_alert_phone = delay_alert_phone
        self.error_alert_status = error_alert_status
        self.error_alert_phone = error_alert_phone
        self.delay_over_seconds = delay_over_seconds
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ConfigureMigrationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureMigrationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureMigrationJobAlertResponseBody = None,
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
            temp_model = ConfigureMigrationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSubscriptionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_job_name: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_region: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_user_name: str = None,
        source_endpoint_password: str = None,
        source_endpoint_owner_id: str = None,
        source_endpoint_role: str = None,
        db_list: str = None,
        reserve: str = None,
        checkpoint: str = None,
        subscription_instance_network_type: str = None,
        subscription_instance_vpcid: str = None,
        subscription_instance_vswitch_id: str = None,
        subscription_data_type_ddl: bool = None,
        subscription_data_type_dml: bool = None,
        delay_phone: str = None,
        delay_rule_time: int = None,
        delay_notice: bool = None,
        error_phone: str = None,
        error_notice: bool = None,
    ):
        self.region_id = region_id
        self.dts_job_name = dts_job_name
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_user_name = source_endpoint_user_name
        self.source_endpoint_password = source_endpoint_password
        self.source_endpoint_owner_id = source_endpoint_owner_id
        self.source_endpoint_role = source_endpoint_role
        self.db_list = db_list
        self.reserve = reserve
        self.checkpoint = checkpoint
        self.subscription_instance_network_type = subscription_instance_network_type
        self.subscription_instance_vpcid = subscription_instance_vpcid
        self.subscription_instance_vswitch_id = subscription_instance_vswitch_id
        self.subscription_data_type_ddl = subscription_data_type_ddl
        self.subscription_data_type_dml = subscription_data_type_dml
        self.delay_phone = delay_phone
        self.delay_rule_time = delay_rule_time
        self.delay_notice = delay_notice
        self.error_phone = error_phone
        self.error_notice = error_notice

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.source_endpoint_owner_id is not None:
            result['SourceEndpointOwnerID'] = self.source_endpoint_owner_id
        if self.source_endpoint_role is not None:
            result['SourceEndpointRole'] = self.source_endpoint_role
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.reserve is not None:
            result['Reserve'] = self.reserve
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.subscription_instance_network_type is not None:
            result['SubscriptionInstanceNetworkType'] = self.subscription_instance_network_type
        if self.subscription_instance_vpcid is not None:
            result['SubscriptionInstanceVPCId'] = self.subscription_instance_vpcid
        if self.subscription_instance_vswitch_id is not None:
            result['SubscriptionInstanceVSwitchId'] = self.subscription_instance_vswitch_id
        if self.subscription_data_type_ddl is not None:
            result['SubscriptionDataTypeDDL'] = self.subscription_data_type_ddl
        if self.subscription_data_type_dml is not None:
            result['SubscriptionDataTypeDML'] = self.subscription_data_type_dml
        if self.delay_phone is not None:
            result['DelayPhone'] = self.delay_phone
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.delay_notice is not None:
            result['DelayNotice'] = self.delay_notice
        if self.error_phone is not None:
            result['ErrorPhone'] = self.error_phone
        if self.error_notice is not None:
            result['ErrorNotice'] = self.error_notice
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('SourceEndpointOwnerID') is not None:
            self.source_endpoint_owner_id = m.get('SourceEndpointOwnerID')
        if m.get('SourceEndpointRole') is not None:
            self.source_endpoint_role = m.get('SourceEndpointRole')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('Reserve') is not None:
            self.reserve = m.get('Reserve')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('SubscriptionInstanceNetworkType') is not None:
            self.subscription_instance_network_type = m.get('SubscriptionInstanceNetworkType')
        if m.get('SubscriptionInstanceVPCId') is not None:
            self.subscription_instance_vpcid = m.get('SubscriptionInstanceVPCId')
        if m.get('SubscriptionInstanceVSwitchId') is not None:
            self.subscription_instance_vswitch_id = m.get('SubscriptionInstanceVSwitchId')
        if m.get('SubscriptionDataTypeDDL') is not None:
            self.subscription_data_type_ddl = m.get('SubscriptionDataTypeDDL')
        if m.get('SubscriptionDataTypeDML') is not None:
            self.subscription_data_type_dml = m.get('SubscriptionDataTypeDML')
        if m.get('DelayPhone') is not None:
            self.delay_phone = m.get('DelayPhone')
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('DelayNotice') is not None:
            self.delay_notice = m.get('DelayNotice')
        if m.get('ErrorPhone') is not None:
            self.error_phone = m.get('ErrorPhone')
        if m.get('ErrorNotice') is not None:
            self.error_notice = m.get('ErrorNotice')
        return self


class ConfigureSubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        dts_job_id: str = None,
        success: str = None,
        dts_instance_id: str = None,
        err_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.dts_job_id = dts_job_id
        self.success = success
        self.dts_instance_id = dts_instance_id
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.success is not None:
            result['Success'] = self.success
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureSubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSubscriptionResponseBody = None,
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
            temp_model = ConfigureSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSubscriptionInstanceRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        instance_id: str = None,
        ip: str = None,
        port: str = None,
        user_name: str = None,
        password: str = None,
        oracle_sid: str = None,
        database_name: str = None,
        owner_id: str = None,
        role: str = None,
    ):
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.oracle_sid = oracle_sid
        self.database_name = database_name
        self.owner_id = owner_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
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


class ConfigureSubscriptionInstanceRequestSubscriptionInstance(TeaModel):
    def __init__(
        self,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ConfigureSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: ConfigureSubscriptionInstanceRequestSourceEndpoint = None,
        subscription_data_type: ConfigureSubscriptionInstanceRequestSubscriptionDataType = None,
        subscription_instance: ConfigureSubscriptionInstanceRequestSubscriptionInstance = None,
        region_id: str = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_object: str = None,
        subscription_instance_network_type: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.source_endpoint = source_endpoint
        self.subscription_data_type = subscription_data_type
        self.subscription_instance = subscription_instance
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.subscription_instance_name = subscription_instance_name
        self.subscription_object = subscription_object
        self.subscription_instance_network_type = subscription_instance_network_type
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_instance:
            self.subscription_instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_instance is not None:
            result['SubscriptionInstance'] = self.subscription_instance.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object
        if self.subscription_instance_network_type is not None:
            result['SubscriptionInstanceNetworkType'] = self.subscription_instance_network_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('SubscriptionDataType') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionInstance') is not None:
            temp_model = ConfigureSubscriptionInstanceRequestSubscriptionInstance()
            self.subscription_instance = temp_model.from_map(m['SubscriptionInstance'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionObject') is not None:
            self.subscription_object = m.get('SubscriptionObject')
        if m.get('SubscriptionInstanceNetworkType') is not None:
            self.subscription_instance_network_type = m.get('SubscriptionInstanceNetworkType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ConfigureSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSubscriptionInstanceResponseBody = None,
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
            temp_model = ConfigureSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSubscriptionInstanceAlertRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        delay_alert_status: str = None,
        delay_alert_phone: str = None,
        error_alert_status: str = None,
        error_alert_phone: str = None,
        delay_over_seconds: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.delay_alert_status = delay_alert_status
        self.delay_alert_phone = delay_alert_phone
        self.error_alert_status = error_alert_status
        self.error_alert_phone = error_alert_phone
        self.delay_over_seconds = delay_over_seconds
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ConfigureSubscriptionInstanceAlertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureSubscriptionInstanceAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSubscriptionInstanceAlertResponseBody = None,
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
            temp_model = ConfigureSubscriptionInstanceAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        port: str = None,
        user_name: str = None,
        password: str = None,
        owner_id: str = None,
        role: str = None,
        database_name: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.owner_id = owner_id
        self.role = role
        self.database_name = database_name

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
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        return self


class ConfigureSynchronizationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        port: str = None,
        user_name: str = None,
        password: str = None,
        data_base_name: str = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.ip = ip
        self.port = port
        self.user_name = user_name
        self.password = password
        self.data_base_name = data_base_name

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
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.data_base_name is not None:
            result['DataBaseName'] = self.data_base_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('DataBaseName') is not None:
            self.data_base_name = m.get('DataBaseName')
        return self


class ConfigureSynchronizationJobRequestPartitionKey(TeaModel):
    def __init__(
        self,
        modify_time_year: bool = None,
        modify_time_month: bool = None,
        modify_time_day: bool = None,
        modify_time_hour: bool = None,
        modify_time_minute: bool = None,
    ):
        self.modify_time_year = modify_time_year
        self.modify_time_month = modify_time_month
        self.modify_time_day = modify_time_day
        self.modify_time_hour = modify_time_hour
        self.modify_time_minute = modify_time_minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time_year is not None:
            result['ModifyTime_Year'] = self.modify_time_year
        if self.modify_time_month is not None:
            result['ModifyTime_Month'] = self.modify_time_month
        if self.modify_time_day is not None:
            result['ModifyTime_Day'] = self.modify_time_day
        if self.modify_time_hour is not None:
            result['ModifyTime_Hour'] = self.modify_time_hour
        if self.modify_time_minute is not None:
            result['ModifyTime_Minute'] = self.modify_time_minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime_Year') is not None:
            self.modify_time_year = m.get('ModifyTime_Year')
        if m.get('ModifyTime_Month') is not None:
            self.modify_time_month = m.get('ModifyTime_Month')
        if m.get('ModifyTime_Day') is not None:
            self.modify_time_day = m.get('ModifyTime_Day')
        if m.get('ModifyTime_Hour') is not None:
            self.modify_time_hour = m.get('ModifyTime_Hour')
        if m.get('ModifyTime_Minute') is not None:
            self.modify_time_minute = m.get('ModifyTime_Minute')
        return self


class ConfigureSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: ConfigureSynchronizationJobRequestSourceEndpoint = None,
        destination_endpoint: ConfigureSynchronizationJobRequestDestinationEndpoint = None,
        partition_key: ConfigureSynchronizationJobRequestPartitionKey = None,
        region_id: str = None,
        synchronization_job_name: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        structure_initialization: bool = None,
        data_initialization: bool = None,
        synchronization_objects: str = None,
        migration_reserved: str = None,
        checkpoint: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.source_endpoint = source_endpoint
        self.destination_endpoint = destination_endpoint
        self.partition_key = partition_key
        self.region_id = region_id
        self.synchronization_job_name = synchronization_job_name
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.structure_initialization = structure_initialization
        self.data_initialization = data_initialization
        self.synchronization_objects = synchronization_objects
        self.migration_reserved = migration_reserved
        self.checkpoint = checkpoint
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.partition_key:
            self.partition_key.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        if self.migration_reserved is not None:
            result['MigrationReserved'] = self.migration_reserved
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = ConfigureSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('PartitionKey') is not None:
            temp_model = ConfigureSynchronizationJobRequestPartitionKey()
            self.partition_key = temp_model.from_map(m['PartitionKey'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        if m.get('MigrationReserved') is not None:
            self.migration_reserved = m.get('MigrationReserved')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ConfigureSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSynchronizationJobResponseBody = None,
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
            temp_model = ConfigureSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobAlertRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        delay_alert_status: str = None,
        delay_alert_phone: str = None,
        error_alert_status: str = None,
        error_alert_phone: str = None,
        delay_over_seconds: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.delay_alert_status = delay_alert_status
        self.delay_alert_phone = delay_alert_phone
        self.error_alert_status = error_alert_status
        self.error_alert_phone = error_alert_phone
        self.delay_over_seconds = delay_over_seconds
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ConfigureSynchronizationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureSynchronizationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSynchronizationJobAlertResponseBody = None,
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
            temp_model = ConfigureSynchronizationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureSynchronizationJobReplicatorCompareRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        synchronization_replicator_compare_enable: bool = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.synchronization_replicator_compare_enable = synchronization_replicator_compare_enable
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.synchronization_replicator_compare_enable is not None:
            result['SynchronizationReplicatorCompareEnable'] = self.synchronization_replicator_compare_enable
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('SynchronizationReplicatorCompareEnable') is not None:
            self.synchronization_replicator_compare_enable = m.get('SynchronizationReplicatorCompareEnable')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ConfigureSynchronizationJobReplicatorCompareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ConfigureSynchronizationJobReplicatorCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigureSynchronizationJobReplicatorCompareResponseBody = None,
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
            temp_model = ConfigureSynchronizationJobReplicatorCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        consumer_group_name: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_password = consumer_group_password
        self.consumer_group_user_name = consumer_group_user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        return self


class CreateConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
        consumer_group_id: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.consumer_group_id = consumer_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        return self


class CreateConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConsumerChannelResponseBody = None,
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
            temp_model = CreateConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        consumer_group_name: str = None,
        consumer_group_user_name: str = None,
        consumer_group_password: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_user_name = consumer_group_user_name
        self.consumer_group_password = consumer_group_password
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class CreateConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.consumer_group_id = consumer_group_id
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class CreateConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConsumerGroupResponseBody = None,
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
            temp_model = CreateConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDtsInstanceRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        instance_class: str = None,
        pay_type: str = None,
        period: str = None,
        sync_architecture: str = None,
        auto_start: bool = None,
        used_time: int = None,
        quantity: int = None,
        auto_pay: bool = None,
        type: str = None,
        database_count: int = None,
        source_region: str = None,
        destination_region: str = None,
        source_endpoint_engine_name: str = None,
        destination_endpoint_engine_name: str = None,
        compute_unit: int = None,
        region_id: str = None,
    ):
        self.job_id = job_id
        self.instance_class = instance_class
        self.pay_type = pay_type
        self.period = period
        self.sync_architecture = sync_architecture
        self.auto_start = auto_start
        self.used_time = used_time
        self.quantity = quantity
        self.auto_pay = auto_pay
        self.type = type
        self.database_count = database_count
        self.source_region = source_region
        self.destination_region = destination_region
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        self.compute_unit = compute_unit
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.sync_architecture is not None:
            result['SyncArchitecture'] = self.sync_architecture
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.type is not None:
            result['Type'] = self.type
        if self.database_count is not None:
            result['DatabaseCount'] = self.database_count
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name
        if self.compute_unit is not None:
            result['ComputeUnit'] = self.compute_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('SyncArchitecture') is not None:
            self.sync_architecture = m.get('SyncArchitecture')
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DatabaseCount') is not None:
            self.database_count = m.get('DatabaseCount')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')
        if m.get('ComputeUnit') is not None:
            self.compute_unit = m.get('ComputeUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateDtsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        job_id: str = None,
        err_message: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.job_id = job_id
        self.err_message = err_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateDtsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDtsInstanceResponseBody = None,
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
            temp_model = CreateDtsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        type: str = None,
        state: str = None,
        phone: str = None,
        delay_rule_time: int = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.type = type
        self.state = state
        self.phone = phone
        self.delay_rule_time = delay_rule_time
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.type is not None:
            result['Type'] = self.type
        if self.state is not None:
            result['State'] = self.state
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateJobMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        dts_job_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        code: str = None,
        dynamic_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.code = code
        self.dynamic_message = dynamic_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        return self


class CreateJobMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobMonitorRuleResponseBody = None,
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
            temp_model = CreateJobMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMigrationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        region: str = None,
        migration_job_class: str = None,
        owner_id: str = None,
        client_token: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.region = region
        self.migration_job_class = migration_job_class
        self.owner_id = owner_id
        self.client_token = client_token
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region is not None:
            result['Region'] = self.region
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class CreateMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        migration_job_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.migration_job_id = migration_job_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class CreateMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMigrationJobResponseBody = None,
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
            temp_model = CreateMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubscriptionInstanceRequestSourceEndpoint(TeaModel):
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


class CreateSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: CreateSubscriptionInstanceRequestSourceEndpoint = None,
        region_id: str = None,
        region: str = None,
        pay_type: str = None,
        period: str = None,
        used_time: int = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.source_endpoint = source_endpoint
        self.region_id = region_id
        self.region = region
        self.pay_type = pay_type
        self.period = period
        self.used_time = used_time
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region is not None:
            result['Region'] = self.region
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = CreateSubscriptionInstanceRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class CreateSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        subscription_instance_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.subscription_instance_id = subscription_instance_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class CreateSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSubscriptionInstanceResponseBody = None,
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
            temp_model = CreateSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class CreateSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        source_endpoint: CreateSynchronizationJobRequestSourceEndpoint = None,
        destination_endpoint: CreateSynchronizationJobRequestDestinationEndpoint = None,
        region_id: str = None,
        source_region: str = None,
        dest_region: str = None,
        topology: str = None,
        synchronization_job_class: str = None,
        pay_type: str = None,
        period: str = None,
        used_time: int = None,
        client_token: str = None,
        network_type: str = None,
        owner_id: str = None,
        account_id: str = None,
        dbinstance_count: int = None,
    ):
        self.source_endpoint = source_endpoint
        self.destination_endpoint = destination_endpoint
        self.region_id = region_id
        self.source_region = source_region
        self.dest_region = dest_region
        self.topology = topology
        self.synchronization_job_class = synchronization_job_class
        self.pay_type = pay_type
        self.period = period
        self.used_time = used_time
        self.client_token = client_token
        self.network_type = network_type
        self.owner_id = owner_id
        self.account_id = account_id
        self.dbinstance_count = dbinstance_count

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region
        if self.topology is not None:
            result['Topology'] = self.topology
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period is not None:
            result['Period'] = self.period
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.network_type is not None:
            result['networkType'] = self.network_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.dbinstance_count is not None:
            result['DBInstanceCount'] = self.dbinstance_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = CreateSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')
        if m.get('Topology') is not None:
            self.topology = m.get('Topology')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('DBInstanceCount') is not None:
            self.dbinstance_count = m.get('DBInstanceCount')
        return self


class CreateSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        synchronization_job_id: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.synchronization_job_id = synchronization_job_id
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class CreateSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSynchronizationJobResponseBody = None,
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
            temp_model = CreateSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        consumer_group_id: str = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.consumer_group_id = consumer_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')
        return self


class DeleteConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DeleteConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConsumerChannelResponseBody = None,
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
            temp_model = DeleteConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        consumer_group_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.consumer_group_id = consumer_group_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DeleteConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConsumerGroupResponseBody = None,
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
            temp_model = DeleteConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class DeleteDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDtsJobResponseBody = None,
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
            temp_model = DeleteDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMigrationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DeleteMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMigrationJobResponseBody = None,
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
            temp_model = DeleteMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DeleteSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSubscriptionInstanceResponseBody = None,
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
            temp_model = DeleteSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DeleteSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DeleteSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSynchronizationJobResponseBody = None,
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
            temp_model = DeleteSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectionStatusRequest(TeaModel):
    def __init__(
        self,
        source_endpoint_architecture: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_region: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_port: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_user_name: str = None,
        source_endpoint_password: str = None,
        destination_endpoint_instance_type: str = None,
        destination_endpoint_instance_id: str = None,
        destination_endpoint_engine_name: str = None,
        destination_endpoint_region: str = None,
        destination_endpoint_ip: str = None,
        destination_endpoint_port: str = None,
        destination_endpoint_database_name: str = None,
        destination_endpoint_user_name: str = None,
        destination_endpoint_password: str = None,
        destination_endpoint_oracle_sid: str = None,
        destination_endpoint_architecture: str = None,
        region_id: str = None,
    ):
        self.source_endpoint_architecture = source_endpoint_architecture
        self.source_endpoint_instance_type = source_endpoint_instance_type
        self.source_endpoint_instance_id = source_endpoint_instance_id
        self.source_endpoint_engine_name = source_endpoint_engine_name
        self.source_endpoint_region = source_endpoint_region
        self.source_endpoint_ip = source_endpoint_ip
        self.source_endpoint_port = source_endpoint_port
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        self.source_endpoint_database_name = source_endpoint_database_name
        self.source_endpoint_user_name = source_endpoint_user_name
        self.source_endpoint_password = source_endpoint_password
        self.destination_endpoint_instance_type = destination_endpoint_instance_type
        self.destination_endpoint_instance_id = destination_endpoint_instance_id
        self.destination_endpoint_engine_name = destination_endpoint_engine_name
        self.destination_endpoint_region = destination_endpoint_region
        self.destination_endpoint_ip = destination_endpoint_ip
        self.destination_endpoint_port = destination_endpoint_port
        self.destination_endpoint_database_name = destination_endpoint_database_name
        self.destination_endpoint_user_name = destination_endpoint_user_name
        self.destination_endpoint_password = destination_endpoint_password
        self.destination_endpoint_oracle_sid = destination_endpoint_oracle_sid
        self.destination_endpoint_architecture = destination_endpoint_architecture
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_endpoint_architecture is not None:
            result['SourceEndpointArchitecture'] = self.source_endpoint_architecture
        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type
        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id
        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip
        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port
        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid
        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name
        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name
        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password
        if self.destination_endpoint_instance_type is not None:
            result['DestinationEndpointInstanceType'] = self.destination_endpoint_instance_type
        if self.destination_endpoint_instance_id is not None:
            result['DestinationEndpointInstanceID'] = self.destination_endpoint_instance_id
        if self.destination_endpoint_engine_name is not None:
            result['DestinationEndpointEngineName'] = self.destination_endpoint_engine_name
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        if self.destination_endpoint_ip is not None:
            result['DestinationEndpointIP'] = self.destination_endpoint_ip
        if self.destination_endpoint_port is not None:
            result['DestinationEndpointPort'] = self.destination_endpoint_port
        if self.destination_endpoint_database_name is not None:
            result['DestinationEndpointDatabaseName'] = self.destination_endpoint_database_name
        if self.destination_endpoint_user_name is not None:
            result['DestinationEndpointUserName'] = self.destination_endpoint_user_name
        if self.destination_endpoint_password is not None:
            result['DestinationEndpointPassword'] = self.destination_endpoint_password
        if self.destination_endpoint_oracle_sid is not None:
            result['DestinationEndpointOracleSID'] = self.destination_endpoint_oracle_sid
        if self.destination_endpoint_architecture is not None:
            result['DestinationEndpointArchitecture'] = self.destination_endpoint_architecture
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceEndpointArchitecture') is not None:
            self.source_endpoint_architecture = m.get('SourceEndpointArchitecture')
        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')
        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')
        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')
        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')
        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')
        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')
        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')
        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')
        if m.get('DestinationEndpointInstanceType') is not None:
            self.destination_endpoint_instance_type = m.get('DestinationEndpointInstanceType')
        if m.get('DestinationEndpointInstanceID') is not None:
            self.destination_endpoint_instance_id = m.get('DestinationEndpointInstanceID')
        if m.get('DestinationEndpointEngineName') is not None:
            self.destination_endpoint_engine_name = m.get('DestinationEndpointEngineName')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        if m.get('DestinationEndpointIP') is not None:
            self.destination_endpoint_ip = m.get('DestinationEndpointIP')
        if m.get('DestinationEndpointPort') is not None:
            self.destination_endpoint_port = m.get('DestinationEndpointPort')
        if m.get('DestinationEndpointDatabaseName') is not None:
            self.destination_endpoint_database_name = m.get('DestinationEndpointDatabaseName')
        if m.get('DestinationEndpointUserName') is not None:
            self.destination_endpoint_user_name = m.get('DestinationEndpointUserName')
        if m.get('DestinationEndpointPassword') is not None:
            self.destination_endpoint_password = m.get('DestinationEndpointPassword')
        if m.get('DestinationEndpointOracleSID') is not None:
            self.destination_endpoint_oracle_sid = m.get('DestinationEndpointOracleSID')
        if m.get('DestinationEndpointArchitecture') is not None:
            self.destination_endpoint_architecture = m.get('DestinationEndpointArchitecture')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeConnectionStatusResponseBody(TeaModel):
    def __init__(
        self,
        source_connection_status: Dict[str, Any] = None,
        destination_connection_status: Dict[str, Any] = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.source_connection_status = source_connection_status
        self.destination_connection_status = destination_connection_status
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_connection_status is not None:
            result['SourceConnectionStatus'] = self.source_connection_status
        if self.destination_connection_status is not None:
            result['DestinationConnectionStatus'] = self.destination_connection_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceConnectionStatus') is not None:
            self.source_connection_status = m.get('SourceConnectionStatus')
        if m.get('DestinationConnectionStatus') is not None:
            self.destination_connection_status = m.get('DestinationConnectionStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DescribeConnectionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConnectionStatusResponseBody = None,
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
            temp_model = DescribeConnectionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        page_size: int = None,
        page_number: int = None,
        parent_channel_id: str = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.page_size = page_size
        self.page_number = page_number
        self.parent_channel_id = parent_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.parent_channel_id is not None:
            result['ParentChannelId'] = self.parent_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ParentChannelId') is not None:
            self.parent_channel_id = m.get('ParentChannelId')
        return self


class DescribeConsumerChannelResponseBodyConsumerChannels(TeaModel):
    def __init__(
        self,
        consumer_group_user_name: str = None,
        consumer_group_id: str = None,
        message_delay: int = None,
        consumer_group_name: str = None,
        consumption_checkpoint: str = None,
        unconsumed_data: int = None,
    ):
        self.consumer_group_user_name = consumer_group_user_name
        self.consumer_group_id = consumer_group_id
        self.message_delay = message_delay
        self.consumer_group_name = consumer_group_name
        self.consumption_checkpoint = consumption_checkpoint
        self.unconsumed_data = unconsumed_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id
        if self.message_delay is not None:
            result['MessageDelay'] = self.message_delay
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.unconsumed_data is not None:
            result['UnconsumedData'] = self.unconsumed_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')
        if m.get('MessageDelay') is not None:
            self.message_delay = m.get('MessageDelay')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('UnconsumedData') is not None:
            self.unconsumed_data = m.get('UnconsumedData')
        return self


class DescribeConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        page_record_count: int = None,
        success: str = None,
        total_record_count: int = None,
        err_message: str = None,
        page_number: int = None,
        consumer_channels: List[DescribeConsumerChannelResponseBodyConsumerChannels] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.page_record_count = page_record_count
        self.success = success
        self.total_record_count = total_record_count
        self.err_message = err_message
        self.page_number = page_number
        self.consumer_channels = consumer_channels

    def validate(self):
        if self.consumer_channels:
            for k in self.consumer_channels:
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['ConsumerChannels'] = []
        if self.consumer_channels is not None:
            for k in self.consumer_channels:
                result['ConsumerChannels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.consumer_channels = []
        if m.get('ConsumerChannels') is not None:
            for k in m.get('ConsumerChannels'):
                temp_model = DescribeConsumerChannelResponseBodyConsumerChannels()
                self.consumer_channels.append(temp_model.from_map(k))
        return self


class DescribeConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConsumerChannelResponseBody = None,
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
            temp_model = DescribeConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConsumerGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        page_num: int = None,
        subscription_instance_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.page_num = page_num
        self.subscription_instance_id = subscription_instance_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel(TeaModel):
    def __init__(
        self,
        consumer_group_user_name: str = None,
        consumer_group_id: str = None,
        message_delay: int = None,
        consumer_group_name: str = None,
        consumption_checkpoint: str = None,
        unconsumed_data: int = None,
    ):
        self.consumer_group_user_name = consumer_group_user_name
        self.consumer_group_id = consumer_group_id
        self.message_delay = message_delay
        self.consumer_group_name = consumer_group_name
        self.consumption_checkpoint = consumption_checkpoint
        self.unconsumed_data = unconsumed_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.message_delay is not None:
            result['MessageDelay'] = self.message_delay
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.unconsumed_data is not None:
            result['UnconsumedData'] = self.unconsumed_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('MessageDelay') is not None:
            self.message_delay = m.get('MessageDelay')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('UnconsumedData') is not None:
            self.unconsumed_data = m.get('UnconsumedData')
        return self


class DescribeConsumerGroupResponseBodyConsumerChannels(TeaModel):
    def __init__(
        self,
        describe_consumer_channel: List[DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel] = None,
    ):
        self.describe_consumer_channel = describe_consumer_channel

    def validate(self):
        if self.describe_consumer_channel:
            for k in self.describe_consumer_channel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DescribeConsumerChannel'] = []
        if self.describe_consumer_channel is not None:
            for k in self.describe_consumer_channel:
                result['DescribeConsumerChannel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.describe_consumer_channel = []
        if m.get('DescribeConsumerChannel') is not None:
            for k in m.get('DescribeConsumerChannel'):
                temp_model = DescribeConsumerGroupResponseBodyConsumerChannelsDescribeConsumerChannel()
                self.describe_consumer_channel.append(temp_model.from_map(k))
        return self


class DescribeConsumerGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        page_record_count: int = None,
        total_record_count: int = None,
        err_message: str = None,
        page_number: int = None,
        consumer_channels: DescribeConsumerGroupResponseBodyConsumerChannels = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count
        self.err_message = err_message
        self.page_number = page_number
        self.consumer_channels = consumer_channels

    def validate(self):
        if self.consumer_channels:
            self.consumer_channels.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.consumer_channels is not None:
            result['ConsumerChannels'] = self.consumer_channels.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ConsumerChannels') is not None:
            temp_model = DescribeConsumerGroupResponseBodyConsumerChannels()
            self.consumer_channels = temp_model.from_map(m['ConsumerChannels'])
        return self


class DescribeConsumerGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConsumerGroupResponseBody = None,
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
            temp_model = DescribeConsumerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDTSIPRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        source_endpoint_region: str = None,
        destination_endpoint_region: str = None,
    ):
        self.region_id = region_id
        self.source_endpoint_region = source_endpoint_region
        self.destination_endpoint_region = destination_endpoint_region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')
        return self


class DescribeDTSIPResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class DescribeDTSIPResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDTSIPResponseBody = None,
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
            temp_model = DescribeDTSIPResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDtsJobDetailRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDtsJobDetailResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        oracle_sid: str = None,
        ssl_solution_enum: str = None,
        ip: str = None,
        instance_id: str = None,
        role_name: str = None,
        instance_type: str = None,
        port: str = None,
        engine_name: str = None,
        region: str = None,
        database_name: str = None,
        aliyun_uid: str = None,
        user_name: str = None,
    ):
        self.oracle_sid = oracle_sid
        self.ssl_solution_enum = ssl_solution_enum
        self.ip = ip
        self.instance_id = instance_id
        self.role_name = role_name
        self.instance_type = instance_type
        self.port = port
        self.engine_name = engine_name
        self.region = region
        self.database_name = database_name
        self.aliyun_uid = aliyun_uid
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        if self.region is not None:
            result['Region'] = self.region
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeDtsJobDetailResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        ssl_solution_enum: str = None,
        oracle_sid: str = None,
        database_name: str = None,
        region: str = None,
        ip: str = None,
        instance_id: str = None,
        port: str = None,
        instance_type: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.ssl_solution_enum = ssl_solution_enum
        self.oracle_sid = oracle_sid
        self.database_name = database_name
        self.region = region
        self.ip = ip
        self.instance_id = instance_id
        self.port = port
        self.instance_type = instance_type
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.region is not None:
            result['Region'] = self.region
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeDtsJobDetailResponseBodyMigrationMode(TeaModel):
    def __init__(
        self,
        data_extract_transform_load: bool = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        self.data_extract_transform_load = data_extract_transform_load
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
        if self.data_extract_transform_load is not None:
            result['DataExtractTransformLoad'] = self.data_extract_transform_load
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataExtractTransformLoad') is not None:
            self.data_extract_transform_load = m.get('DataExtractTransformLoad')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        return self


class DescribeDtsJobDetailResponseBodySubscriptionHost(TeaModel):
    def __init__(
        self,
        vpc_host: str = None,
        public_host: str = None,
        private_host: str = None,
    ):
        self.vpc_host = vpc_host
        self.public_host = public_host
        self.private_host = private_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_host is not None:
            result['VpcHost'] = self.vpc_host
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcHost') is not None:
            self.vpc_host = m.get('VpcHost')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
        return self


class DescribeDtsJobDetailResponseBodySubscriptionDataType(TeaModel):
    def __init__(
        self,
        dml: bool = None,
        ddl: bool = None,
    ):
        self.dml = dml
        self.ddl = ddl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dml is not None:
            result['Dml'] = self.dml
        if self.ddl is not None:
            result['Ddl'] = self.ddl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dml') is not None:
            self.dml = m.get('Dml')
        if m.get('Ddl') is not None:
            self.ddl = m.get('Ddl')
        return self


class DescribeDtsJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        dts_job_name: str = None,
        finish_time: str = None,
        error_message: str = None,
        dts_job_id: str = None,
        create_time: str = None,
        pay_type: str = None,
        reserved: str = None,
        database_count: int = None,
        dts_job_class: str = None,
        end_timestamp: str = None,
        app_name: str = None,
        dest_net_type: str = None,
        subscribe_topic: str = None,
        dts_instance_id: str = None,
        request_id: str = None,
        code: int = None,
        checkpoint: int = None,
        delay: int = None,
        expire_time: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        consumption_client: str = None,
        db_object: str = None,
        dynamic_message: str = None,
        consumption_checkpoint: str = None,
        etl_calculator: str = None,
        http_status_code: int = None,
        begin_timestamp: str = None,
        group_id: str = None,
        synchronization_direction: str = None,
        dts_job_direction: str = None,
        source_endpoint: DescribeDtsJobDetailResponseBodySourceEndpoint = None,
        destination_endpoint: DescribeDtsJobDetailResponseBodyDestinationEndpoint = None,
        migration_mode: DescribeDtsJobDetailResponseBodyMigrationMode = None,
        subscription_host: DescribeDtsJobDetailResponseBodySubscriptionHost = None,
        subscription_data_type: DescribeDtsJobDetailResponseBodySubscriptionDataType = None,
    ):
        self.status = status
        self.dts_job_name = dts_job_name
        self.finish_time = finish_time
        self.error_message = error_message
        self.dts_job_id = dts_job_id
        self.create_time = create_time
        self.pay_type = pay_type
        self.reserved = reserved
        self.database_count = database_count
        self.dts_job_class = dts_job_class
        self.end_timestamp = end_timestamp
        self.app_name = app_name
        self.dest_net_type = dest_net_type
        self.subscribe_topic = subscribe_topic
        self.dts_instance_id = dts_instance_id
        self.request_id = request_id
        self.code = code
        self.checkpoint = checkpoint
        self.delay = delay
        self.expire_time = expire_time
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.consumption_client = consumption_client
        self.db_object = db_object
        self.dynamic_message = dynamic_message
        self.consumption_checkpoint = consumption_checkpoint
        self.etl_calculator = etl_calculator
        self.http_status_code = http_status_code
        self.begin_timestamp = begin_timestamp
        self.group_id = group_id
        self.synchronization_direction = synchronization_direction
        self.dts_job_direction = dts_job_direction
        self.source_endpoint = source_endpoint
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.subscription_host = subscription_host
        self.subscription_data_type = subscription_data_type

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.subscription_host:
            self.subscription_host.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.database_count is not None:
            result['DatabaseCount'] = self.database_count
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.dest_net_type is not None:
            result['DestNetType'] = self.dest_net_type
        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.etl_calculator is not None:
            result['EtlCalculator'] = self.etl_calculator
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.subscription_host is not None:
            result['SubscriptionHost'] = self.subscription_host.to_map()
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('DatabaseCount') is not None:
            self.database_count = m.get('DatabaseCount')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('DestNetType') is not None:
            self.dest_net_type = m.get('DestNetType')
        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('EtlCalculator') is not None:
            self.etl_calculator = m.get('EtlCalculator')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobDetailResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobDetailResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobDetailResponseBodyMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('SubscriptionHost') is not None:
            temp_model = DescribeDtsJobDetailResponseBodySubscriptionHost()
            self.subscription_host = temp_model.from_map(m['SubscriptionHost'])
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeDtsJobDetailResponseBodySubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        return self


class DescribeDtsJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDtsJobDetailResponseBody = None,
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
            temp_model = DescribeDtsJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDtsJobsRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        params: str = None,
        region: str = None,
        status: str = None,
        order_direction: str = None,
        order_column: str = None,
        tags: str = None,
        page_size: int = None,
        page_number: int = None,
        job_type: str = None,
        region_id: str = None,
        group_id: str = None,
    ):
        self.type = type
        self.params = params
        self.region = region
        self.status = status
        self.order_direction = order_direction
        self.order_column = order_column
        self.tags = tags
        self.page_size = page_size
        self.page_number = page_number
        self.job_type = job_type
        self.region_id = region_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.params is not None:
            result['Params'] = self.params
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction
        if self.order_column is not None:
            result['OrderColumn'] = self.order_column
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')
        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class DescribeDtsJobsResponseBodyDtsJobListTagList(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        error_message: str = None,
    ):
        self.status = status
        self.need_upgrade = need_upgrade
        self.percent = percent
        self.progress = progress
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint(TeaModel):
    def __init__(
        self,
        ssl_solution_enum: str = None,
        oracle_sid: str = None,
        region: str = None,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        port: str = None,
        instance_type: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.ssl_solution_enum = ssl_solution_enum
        self.oracle_sid = oracle_sid
        self.region = region
        self.database_name = database_name
        self.ip = ip
        self.instance_id = instance_id
        self.port = port
        self.instance_type = instance_type
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.region is not None:
            result['Region'] = self.region
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListMigrationMode(TeaModel):
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


class DescribeDtsJobsResponseBodyDtsJobListPerformance(TeaModel):
    def __init__(
        self,
        rps: str = None,
        flow: str = None,
    ):
        self.rps = rps
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rps is not None:
            result['Rps'] = self.rps
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_result: str = None,
        check_item_description: str = None,
        check_item: str = None,
        repair_method: str = None,
        failed_reason: str = None,
    ):
        self.check_result = check_result
        self.check_item_description = check_item_description
        self.check_item = check_item
        self.repair_method = repair_method
        self.failed_reason = failed_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('CheckItemDescription') is not None:
            self.check_item_description = m.get('CheckItemDescription')
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')
        return self


class DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        detail: List[DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail] = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.detail = detail

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
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        error_message: str = None,
    ):
        self.status = status
        self.need_upgrade = need_upgrade
        self.percent = percent
        self.progress = progress
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint(TeaModel):
    def __init__(
        self,
        ssl_solution_enum: str = None,
        oracle_sid: str = None,
        region: str = None,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        port: str = None,
        instance_type: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.ssl_solution_enum = ssl_solution_enum
        self.oracle_sid = oracle_sid
        self.region = region
        self.database_name = database_name
        self.ip = ip
        self.instance_id = instance_id
        self.port = port
        self.instance_type = instance_type
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.region is not None:
            result['Region'] = self.region
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode(TeaModel):
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


class DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance(TeaModel):
    def __init__(
        self,
        rps: str = None,
        flow: str = None,
    ):
        self.rps = rps
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rps is not None:
            result['Rps'] = self.rps
        if self.flow is not None:
            result['Flow'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rps') is not None:
            self.rps = m.get('Rps')
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail(TeaModel):
    def __init__(
        self,
        check_result: str = None,
        check_item_description: str = None,
        check_item: str = None,
        repair_method: str = None,
        failed_reason: str = None,
    ):
        self.check_result = check_result
        self.check_item_description = check_item_description
        self.check_item = check_item
        self.repair_method = repair_method
        self.failed_reason = failed_reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('CheckItemDescription') is not None:
            self.check_item_description = m.get('CheckItemDescription')
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        detail: List[DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail] = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.detail = detail

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
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint(TeaModel):
    def __init__(
        self,
        ssl_solution_enum: str = None,
        oracle_sid: str = None,
        region: str = None,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        port: str = None,
        instance_type: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.ssl_solution_enum = ssl_solution_enum
        self.oracle_sid = oracle_sid
        self.region = region
        self.database_name = database_name
        self.ip = ip
        self.instance_id = instance_id
        self.port = port
        self.instance_type = instance_type
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.region is not None:
            result['Region'] = self.region
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeDtsJobsResponseBodyDtsJobListReverseJob(TeaModel):
    def __init__(
        self,
        status: str = None,
        dts_job_name: str = None,
        delay: int = None,
        error_message: str = None,
        dts_job_id: str = None,
        expire_time: str = None,
        create_time: str = None,
        pay_type: str = None,
        reserved: str = None,
        db_object: str = None,
        dts_job_class: str = None,
        dts_instance_id: str = None,
        dts_job_direction: str = None,
        checkpoint: str = None,
        data_initialization_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus = None,
        data_synchronization_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus = None,
        destination_endpoint: DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint = None,
        migration_mode: DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode = None,
        performance: DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance = None,
        precheck_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus = None,
        source_endpoint: DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint = None,
        structure_initialization_status: DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus = None,
    ):
        self.status = status
        self.dts_job_name = dts_job_name
        self.delay = delay
        self.error_message = error_message
        self.dts_job_id = dts_job_id
        self.expire_time = expire_time
        self.create_time = create_time
        self.pay_type = pay_type
        self.reserved = reserved
        self.db_object = db_object
        self.dts_job_class = dts_job_class
        self.dts_instance_id = dts_instance_id
        self.dts_job_direction = dts_job_direction
        self.checkpoint = checkpoint
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.performance = performance
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
        if self.performance:
            self.performance.validate()
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
        if self.status is not None:
            result['Status'] = self.status
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('Performance') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint(TeaModel):
    def __init__(
        self,
        ssl_solution_enum: str = None,
        oracle_sid: str = None,
        region: str = None,
        database_name: str = None,
        ip: str = None,
        instance_id: str = None,
        port: str = None,
        instance_type: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.ssl_solution_enum = ssl_solution_enum
        self.oracle_sid = oracle_sid
        self.region = region
        self.database_name = database_name
        self.ip = ip
        self.instance_id = instance_id
        self.port = port
        self.instance_type = instance_type
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.region is not None:
            result['Region'] = self.region
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeDtsJobsResponseBodyDtsJobListRetryState(TeaModel):
    def __init__(
        self,
        retry_count: int = None,
        max_retry_time: int = None,
        err_message: str = None,
        retry_target: str = None,
        retry_time: int = None,
    ):
        self.retry_count = retry_count
        self.max_retry_time = max_retry_time
        self.err_message = err_message
        self.retry_target = retry_target
        self.retry_time = retry_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count
        if self.max_retry_time is not None:
            result['MaxRetryTime'] = self.max_retry_time
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.retry_target is not None:
            result['RetryTarget'] = self.retry_target
        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')
        if m.get('MaxRetryTime') is not None:
            self.max_retry_time = m.get('MaxRetryTime')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RetryTarget') is not None:
            self.retry_target = m.get('RetryTarget')
        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')
        return self


class DescribeDtsJobsResponseBodyDtsJobList(TeaModel):
    def __init__(
        self,
        status: str = None,
        dts_job_name: str = None,
        delay: int = None,
        error_message: str = None,
        expire_time: str = None,
        dts_job_id: str = None,
        create_time: str = None,
        pay_type: str = None,
        reserved: str = None,
        consumption_client: str = None,
        db_object: str = None,
        dts_job_class: str = None,
        consumption_checkpoint: str = None,
        end_timestamp: str = None,
        app_name: str = None,
        begin_timestamp: str = None,
        dts_instance_id: str = None,
        dts_job_direction: str = None,
        checkpoint: str = None,
        tag_list: List[DescribeDtsJobsResponseBodyDtsJobListTagList] = None,
        data_initialization_status: DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus = None,
        data_synchronization_status: DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus = None,
        data_etl_status: DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus = None,
        destination_endpoint: DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint = None,
        migration_mode: DescribeDtsJobsResponseBodyDtsJobListMigrationMode = None,
        performance: DescribeDtsJobsResponseBodyDtsJobListPerformance = None,
        precheck_status: DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus = None,
        reverse_job: DescribeDtsJobsResponseBodyDtsJobListReverseJob = None,
        source_endpoint: DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint = None,
        structure_initialization_status: DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus = None,
        retry_state: DescribeDtsJobsResponseBodyDtsJobListRetryState = None,
    ):
        self.status = status
        self.dts_job_name = dts_job_name
        self.delay = delay
        self.error_message = error_message
        self.expire_time = expire_time
        self.dts_job_id = dts_job_id
        self.create_time = create_time
        self.pay_type = pay_type
        self.reserved = reserved
        self.consumption_client = consumption_client
        self.db_object = db_object
        self.dts_job_class = dts_job_class
        self.consumption_checkpoint = consumption_checkpoint
        self.end_timestamp = end_timestamp
        self.app_name = app_name
        self.begin_timestamp = begin_timestamp
        self.dts_instance_id = dts_instance_id
        self.dts_job_direction = dts_job_direction
        self.checkpoint = checkpoint
        self.tag_list = tag_list
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.data_etl_status = data_etl_status
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.performance = performance
        self.precheck_status = precheck_status
        self.reverse_job = reverse_job
        self.source_endpoint = source_endpoint
        self.structure_initialization_status = structure_initialization_status
        self.retry_state = retry_state

    def validate(self):
        if self.tag_list:
            for k in self.tag_list:
                if k:
                    k.validate()
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.data_etl_status:
            self.data_etl_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.reverse_job:
            self.reverse_job.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.retry_state:
            self.retry_state.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.reserved is not None:
            result['Reserved'] = self.reserved
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.db_object is not None:
            result['DbObject'] = self.db_object
        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id
        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        result['TagList'] = []
        if self.tag_list is not None:
            for k in self.tag_list:
                result['TagList'].append(k.to_map() if k else None)
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.data_etl_status is not None:
            result['DataEtlStatus'] = self.data_etl_status.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.reverse_job is not None:
            result['ReverseJob'] = self.reverse_job.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        if self.retry_state is not None:
            result['RetryState'] = self.retry_state.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')
        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')
        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        self.tag_list = []
        if m.get('TagList') is not None:
            for k in m.get('TagList'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobListTagList()
                self.tag_list.append(temp_model.from_map(k))
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DataEtlStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus()
            self.data_etl_status = temp_model.from_map(m['DataEtlStatus'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('Performance') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('ReverseJob') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListReverseJob()
            self.reverse_job = temp_model.from_map(m['ReverseJob'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        if m.get('RetryState') is not None:
            temp_model = DescribeDtsJobsResponseBodyDtsJobListRetryState()
            self.retry_state = temp_model.from_map(m['RetryState'])
        return self


class DescribeDtsJobsResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        page_record_count: int = None,
        total_record_count: int = None,
        err_message: str = None,
        dynamic_message: str = None,
        page_number: int = None,
        dynamic_code: str = None,
        dts_job_list: List[DescribeDtsJobsResponseBodyDtsJobList] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.dts_job_list = dts_job_list

    def validate(self):
        if self.dts_job_list:
            for k in self.dts_job_list:
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        result['DtsJobList'] = []
        if self.dts_job_list is not None:
            for k in self.dts_job_list:
                result['DtsJobList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        self.dts_job_list = []
        if m.get('DtsJobList') is not None:
            for k in m.get('DtsJobList'):
                temp_model = DescribeDtsJobsResponseBodyDtsJobList()
                self.dts_job_list.append(temp_model.from_map(k))
        return self


class DescribeDtsJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDtsJobsResponseBody = None,
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
            temp_model = DescribeDtsJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointSwitchStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.task_id = task_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeEndpointSwitchStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.status = status
        self.error_message = error_message
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DescribeEndpointSwitchStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEndpointSwitchStatusResponseBody = None,
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
            temp_model = DescribeEndpointSwitchStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInitializationStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        page_size: int = None,
        page_num: int = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.page_size = page_size
        self.page_num = page_num
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeInitializationStatusResponseBodyDataInitializationDetails(TeaModel):
    def __init__(
        self,
        source_owner_dbname: str = None,
        status: str = None,
        used_time: str = None,
        table_name: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        destination_owner_dbname: str = None,
        total_row_num: str = None,
    ):
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.used_time = used_time
        self.table_name = table_name
        self.error_message = error_message
        self.finish_row_num = finish_row_num
        self.destination_owner_dbname = destination_owner_dbname
        self.total_row_num = total_row_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_row_num is not None:
            result['FinishRowNum'] = self.finish_row_num
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('TotalRowNum') is not None:
            self.total_row_num = m.get('TotalRowNum')
        return self


class DescribeInitializationStatusResponseBodyDataSynchronizationDetails(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_owner_dbname: str = None,
        table_name: str = None,
        error_message: str = None,
        destination_owner_dbname: str = None,
    ):
        self.status = status
        self.source_owner_dbname = source_owner_dbname
        self.table_name = table_name
        self.error_message = error_message
        self.destination_owner_dbname = destination_owner_dbname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        return self


class DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_owner_dbname: str = None,
        object_definition: str = None,
        object_type: str = None,
        error_message: str = None,
        destination_owner_dbname: str = None,
        object_name: str = None,
    ):
        self.status = status
        self.source_owner_dbname = source_owner_dbname
        self.object_definition = object_definition
        self.object_type = object_type
        self.error_message = error_message
        self.destination_owner_dbname = destination_owner_dbname
        self.object_name = object_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        return self


class DescribeInitializationStatusResponseBodyStructureInitializationDetails(TeaModel):
    def __init__(
        self,
        status: str = None,
        source_owner_dbname: str = None,
        object_definition: str = None,
        object_type: str = None,
        error_message: str = None,
        destination_owner_dbname: str = None,
        object_name: str = None,
        constraints: List[DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints] = None,
    ):
        self.status = status
        self.source_owner_dbname = source_owner_dbname
        self.object_definition = object_definition
        self.object_type = object_type
        self.error_message = error_message
        self.destination_owner_dbname = destination_owner_dbname
        self.object_name = object_name
        self.constraints = constraints

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
        if self.status is not None:
            result['Status'] = self.status
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        result['Constraints'] = []
        if self.constraints is not None:
            for k in self.constraints:
                result['Constraints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        self.constraints = []
        if m.get('Constraints') is not None:
            for k in m.get('Constraints'):
                temp_model = DescribeInitializationStatusResponseBodyStructureInitializationDetailsConstraints()
                self.constraints.append(temp_model.from_map(k))
        return self


class DescribeInitializationStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
        data_initialization_details: List[DescribeInitializationStatusResponseBodyDataInitializationDetails] = None,
        data_synchronization_details: List[DescribeInitializationStatusResponseBodyDataSynchronizationDetails] = None,
        structure_initialization_details: List[DescribeInitializationStatusResponseBodyStructureInitializationDetails] = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
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
        body: DescribeInitializationStatusResponseBody = None,
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
            temp_model = DescribeInitializationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobMonitorRuleRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeJobMonitorRuleResponseBodyMonitorRules(TeaModel):
    def __init__(
        self,
        type: str = None,
        delay_rule_time: int = None,
        state: str = None,
        phone: str = None,
    ):
        self.type = type
        self.delay_rule_time = delay_rule_time
        self.state = state
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time
        if self.state is not None:
            result['State'] = self.state
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class DescribeJobMonitorRuleResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        dts_job_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        code: str = None,
        dynamic_message: str = None,
        monitor_rules: List[DescribeJobMonitorRuleResponseBodyMonitorRules] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.code = code
        self.dynamic_message = dynamic_message
        self.monitor_rules = monitor_rules

    def validate(self):
        if self.monitor_rules:
            for k in self.monitor_rules:
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
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['MonitorRules'] = []
        if self.monitor_rules is not None:
            for k in self.monitor_rules:
                result['MonitorRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.monitor_rules = []
        if m.get('MonitorRules') is not None:
            for k in m.get('MonitorRules'):
                temp_model = DescribeJobMonitorRuleResponseBodyMonitorRules()
                self.monitor_rules.append(temp_model.from_map(k))
        return self


class DescribeJobMonitorRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJobMonitorRuleResponseBody = None,
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
            temp_model = DescribeJobMonitorRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobAlertRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        migration_job_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeMigrationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        migration_job_name: str = None,
        error_alert_status: str = None,
        err_code: str = None,
        success: str = None,
        error_alert_phone: str = None,
        err_message: str = None,
        delay_alert_status: str = None,
        delay_alert_phone: str = None,
        migration_job_id: str = None,
        delay_over_seconds: str = None,
    ):
        self.request_id = request_id
        self.migration_job_name = migration_job_name
        self.error_alert_status = error_alert_status
        self.err_code = err_code
        self.success = success
        self.error_alert_phone = error_alert_phone
        self.err_message = err_message
        self.delay_alert_status = delay_alert_status
        self.delay_alert_phone = delay_alert_phone
        self.migration_job_id = migration_job_id
        self.delay_over_seconds = delay_over_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        return self


class DescribeMigrationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationJobAlertResponseBody = None,
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
            temp_model = DescribeMigrationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobDetailRequestMigrationMode(TeaModel):
    def __init__(
        self,
        structure_initialization: bool = None,
        data_initialization: bool = None,
        data_synchronization: bool = None,
    ):
        self.structure_initialization = structure_initialization
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')
        return self


class DescribeMigrationJobDetailRequest(TeaModel):
    def __init__(
        self,
        migration_mode: DescribeMigrationJobDetailRequestMigrationMode = None,
        region_id: str = None,
        page_size: int = None,
        page_num: int = None,
        migration_job_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.migration_mode = migration_mode
        self.region_id = region_id
        self.page_size = page_size
        self.page_num = page_num
        self.migration_job_id = migration_job_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobDetailRequestMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeMigrationJobDetailResponseBodyDataInitializationDetailListDataInitializationDetail(TeaModel):
    def __init__(
        self,
        source_owner_dbname: str = None,
        status: str = None,
        table_name: str = None,
        error_message: str = None,
        finish_row_num: str = None,
        migration_time: str = None,
        destination_owner_dbname: str = None,
        total_row_num: str = None,
    ):
        self.source_owner_dbname = source_owner_dbname
        self.status = status
        self.table_name = table_name
        self.error_message = error_message
        self.finish_row_num = finish_row_num
        self.migration_time = migration_time
        self.destination_owner_dbname = destination_owner_dbname
        self.total_row_num = total_row_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.status is not None:
            result['Status'] = self.status
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.finish_row_num is not None:
            result['FinishRowNum'] = self.finish_row_num
        if self.migration_time is not None:
            result['MigrationTime'] = self.migration_time
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.total_row_num is not None:
            result['TotalRowNum'] = self.total_row_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FinishRowNum') is not None:
            self.finish_row_num = m.get('FinishRowNum')
        if m.get('MigrationTime') is not None:
            self.migration_time = m.get('MigrationTime')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
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
        status: str = None,
        source_owner_dbname: str = None,
        table_name: str = None,
        error_message: str = None,
        destination_owner_dbname: str = None,
    ):
        self.status = status
        self.source_owner_dbname = source_owner_dbname
        self.table_name = table_name
        self.error_message = error_message
        self.destination_owner_dbname = destination_owner_dbname

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.table_name is not None:
            result['TableName'] = self.table_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
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
        status: str = None,
        source_owner_dbname: str = None,
        object_definition: str = None,
        object_type: str = None,
        error_message: str = None,
        destination_owner_dbname: str = None,
        object_name: str = None,
    ):
        self.status = status
        self.source_owner_dbname = source_owner_dbname
        self.object_definition = object_definition
        self.object_type = object_type
        self.error_message = error_message
        self.destination_owner_dbname = destination_owner_dbname
        self.object_name = object_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
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
        status: str = None,
        source_owner_dbname: str = None,
        object_definition: str = None,
        object_type: str = None,
        error_message: str = None,
        destination_owner_dbname: str = None,
        object_name: str = None,
        constraint_list: DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList = None,
    ):
        self.status = status
        self.source_owner_dbname = source_owner_dbname
        self.object_definition = object_definition
        self.object_type = object_type
        self.error_message = error_message
        self.destination_owner_dbname = destination_owner_dbname
        self.object_name = object_name
        self.constraint_list = constraint_list

    def validate(self):
        if self.constraint_list:
            self.constraint_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.source_owner_dbname is not None:
            result['SourceOwnerDBName'] = self.source_owner_dbname
        if self.object_definition is not None:
            result['ObjectDefinition'] = self.object_definition
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.destination_owner_dbname is not None:
            result['DestinationOwnerDBName'] = self.destination_owner_dbname
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.constraint_list is not None:
            result['ConstraintList'] = self.constraint_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SourceOwnerDBName') is not None:
            self.source_owner_dbname = m.get('SourceOwnerDBName')
        if m.get('ObjectDefinition') is not None:
            self.object_definition = m.get('ObjectDefinition')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DestinationOwnerDBName') is not None:
            self.destination_owner_dbname = m.get('DestinationOwnerDBName')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('ConstraintList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailListStructureInitializationDetailConstraintList()
            self.constraint_list = temp_model.from_map(m['ConstraintList'])
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
        request_id: str = None,
        err_code: str = None,
        page_record_count: int = None,
        success: str = None,
        total_record_count: int = None,
        err_message: str = None,
        page_number: int = None,
        data_initialization_detail_list: DescribeMigrationJobDetailResponseBodyDataInitializationDetailList = None,
        data_synchronization_detail_list: DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList = None,
        structure_initialization_detail_list: DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.page_record_count = page_record_count
        self.success = success
        self.total_record_count = total_record_count
        self.err_message = err_message
        self.page_number = page_number
        self.data_initialization_detail_list = data_initialization_detail_list
        self.data_synchronization_detail_list = data_synchronization_detail_list
        self.structure_initialization_detail_list = structure_initialization_detail_list

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.data_initialization_detail_list is not None:
            result['DataInitializationDetailList'] = self.data_initialization_detail_list.to_map()
        if self.data_synchronization_detail_list is not None:
            result['DataSynchronizationDetailList'] = self.data_synchronization_detail_list.to_map()
        if self.structure_initialization_detail_list is not None:
            result['StructureInitializationDetailList'] = self.structure_initialization_detail_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DataInitializationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyDataInitializationDetailList()
            self.data_initialization_detail_list = temp_model.from_map(m['DataInitializationDetailList'])
        if m.get('DataSynchronizationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyDataSynchronizationDetailList()
            self.data_synchronization_detail_list = temp_model.from_map(m['DataSynchronizationDetailList'])
        if m.get('StructureInitializationDetailList') is not None:
            temp_model = DescribeMigrationJobDetailResponseBodyStructureInitializationDetailList()
            self.structure_initialization_detail_list = temp_model.from_map(m['StructureInitializationDetailList'])
        return self


class DescribeMigrationJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationJobDetailResponseBody = None,
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
            temp_model = DescribeMigrationJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobsRequestTag(TeaModel):
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


class DescribeMigrationJobsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        page_num: int = None,
        migration_job_name: str = None,
        owner_id: str = None,
        account_id: str = None,
        tag: List[DescribeMigrationJobsRequestTag] = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.page_num = page_num
        self.migration_job_name = migration_job_name
        self.owner_id = owner_id
        self.account_id = account_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeMigrationJobsRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        whole_database: str = None,
        table_list: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList = None,
    ):
        self.database_name = database_name
        self.whole_database = whole_database
        self.table_list = table_list

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
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        if m.get('TableList') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
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


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag(TeaModel):
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


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization(TeaModel):
    def __init__(
        self,
        percent: str = None,
        status: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.percent = percent
        self.status = status
        self.error_message = error_message
        self.progress = progress

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
            result['status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization(TeaModel):
    def __init__(
        self,
        delay: str = None,
        percent: str = None,
        status: str = None,
        error_message: str = None,
    ):
        self.delay = delay
        self.percent = percent
        self.status = status
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.status is not None:
            result['status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint(TeaModel):
    def __init__(
        self,
        oracle_sid: str = None,
        database_name: str = None,
        instance_id: str = None,
        port: str = None,
        ip: str = None,
        instance_type: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.oracle_sid = oracle_sid
        self.database_name = database_name
        self.instance_id = instance_id
        self.port = port
        self.ip = ip
        self.instance_type = instance_type
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
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


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
    ):
        self.status = status
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint(TeaModel):
    def __init__(
        self,
        oracle_sid: str = None,
        database_name: str = None,
        instance_id: str = None,
        port: str = None,
        ip: str = None,
        instance_type: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.oracle_sid = oracle_sid
        self.database_name = database_name
        self.instance_id = instance_id
        self.port = port
        self.ip = ip
        self.instance_type = instance_type
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization(TeaModel):
    def __init__(
        self,
        percent: str = None,
        status: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.percent = percent
        self.status = status
        self.error_message = error_message
        self.progress = progress

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
            result['status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob(TeaModel):
    def __init__(
        self,
        migration_job_name: str = None,
        migration_job_status: str = None,
        pay_type: str = None,
        migration_job_class: str = None,
        instance_create_time: str = None,
        migration_job_id: str = None,
        job_create_time: str = None,
        migration_object: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject = None,
        tags: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags = None,
        data_initialization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization = None,
        data_synchronization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization = None,
        destination_endpoint: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint = None,
        migration_mode: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode = None,
        precheck: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck = None,
        source_endpoint: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint = None,
        structure_initialization: DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization = None,
    ):
        self.migration_job_name = migration_job_name
        self.migration_job_status = migration_job_status
        self.pay_type = pay_type
        self.migration_job_class = migration_job_class
        self.instance_create_time = instance_create_time
        self.migration_job_id = migration_job_id
        self.job_create_time = job_create_time
        self.migration_object = migration_object
        self.tags = tags
        self.data_initialization = data_initialization
        self.data_synchronization = data_synchronization
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.precheck = precheck
        self.source_endpoint = source_endpoint
        self.structure_initialization = structure_initialization

    def validate(self):
        if self.migration_object:
            self.migration_object.validate()
        if self.tags:
            self.tags.validate()
        if self.data_initialization:
            self.data_initialization.validate()
        if self.data_synchronization:
            self.data_synchronization.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.migration_mode:
            self.migration_mode.validate()
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
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_job_status is not None:
            result['MigrationJobStatus'] = self.migration_job_status
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time
        if self.migration_job_id is not None:
            result['MigrationJobID'] = self.migration_job_id
        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization.to_map()
        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.precheck is not None:
            result['Precheck'] = self.precheck.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')
        if m.get('MigrationJobID') is not None:
            self.migration_job_id = m.get('MigrationJobID')
        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')
        if m.get('MigrationObject') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject()
            self.migration_object = temp_model.from_map(m['MigrationObject'])
        if m.get('Tags') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('DataInitialization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization()
            self.data_initialization = temp_model.from_map(m['DataInitialization'])
        if m.get('DataSynchronization') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization()
            self.data_synchronization = temp_model.from_map(m['DataSynchronization'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
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
        request_id: str = None,
        err_code: str = None,
        page_record_count: int = None,
        success: str = None,
        total_record_count: int = None,
        err_message: str = None,
        page_number: int = None,
        migration_jobs: DescribeMigrationJobsResponseBodyMigrationJobs = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.page_record_count = page_record_count
        self.success = success
        self.total_record_count = total_record_count
        self.err_message = err_message
        self.page_number = page_number
        self.migration_jobs = migration_jobs

    def validate(self):
        if self.migration_jobs:
            self.migration_jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.migration_jobs is not None:
            result['MigrationJobs'] = self.migration_jobs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('MigrationJobs') is not None:
            temp_model = DescribeMigrationJobsResponseBodyMigrationJobs()
            self.migration_jobs = temp_model.from_map(m['MigrationJobs'])
        return self


class DescribeMigrationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMigrationJobsResponseBody = None,
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
            temp_model = DescribeMigrationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMigrationJobStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        migration_job_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeMigrationJobStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        delay: str = None,
        error_message: str = None,
        checkpoint: str = None,
    ):
        self.status = status
        self.percent = percent
        self.delay = delay
        self.error_message = error_message
        self.checkpoint = checkpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        return self


class DescribeMigrationJobStatusResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        instance_id: str = None,
        ip: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        oracle_sid: str = None,
        engine_name: str = None,
    ):
        self.database_name = database_name
        self.instance_id = instance_id
        self.ip = ip
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.oracle_sid = oracle_sid
        self.engine_name = engine_name

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
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.oracle_sid is not None:
            result['oracleSID'] = self.oracle_sid
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('oracleSID') is not None:
            self.oracle_sid = m.get('oracleSID')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
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
        status: str = None,
        percent: str = None,
        detail: DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail = None,
    ):
        self.status = status
        self.percent = percent
        self.detail = detail

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('Detail') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail()
            self.detail = temp_model.from_map(m['Detail'])
        return self


class DescribeMigrationJobStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        instance_id: str = None,
        ip: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        oracle_sid: str = None,
        engine_name: str = None,
    ):
        self.database_name = database_name
        self.instance_id = instance_id
        self.ip = ip
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.oracle_sid = oracle_sid
        self.engine_name = engine_name

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
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.oracle_sid is not None:
            result['oracleSID'] = self.oracle_sid
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('oracleSID') is not None:
            self.oracle_sid = m.get('oracleSID')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeMigrationJobStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeMigrationJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        err_code: str = None,
        success: str = None,
        pay_type: str = None,
        err_message: str = None,
        migration_object: str = None,
        migration_job_id: str = None,
        task_id: str = None,
        migration_job_class: str = None,
        data_initialization_status: DescribeMigrationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus = None,
        destination_endpoint: DescribeMigrationJobStatusResponseBodyDestinationEndpoint = None,
        migration_mode: DescribeMigrationJobStatusResponseBodyMigrationMode = None,
        precheck_status: DescribeMigrationJobStatusResponseBodyPrecheckStatus = None,
        source_endpoint: DescribeMigrationJobStatusResponseBodySourceEndpoint = None,
        structure_initialization_status: DescribeMigrationJobStatusResponseBodyStructureInitializationStatus = None,
    ):
        self.request_id = request_id
        self.migration_job_name = migration_job_name
        self.migration_job_status = migration_job_status
        self.err_code = err_code
        self.success = success
        self.pay_type = pay_type
        self.err_message = err_message
        self.migration_object = migration_object
        self.migration_job_id = migration_job_id
        self.task_id = task_id
        self.migration_job_class = migration_job_class
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_job_status is not None:
            result['MigrationJobStatus'] = self.migration_job_status
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.migration_job_class is not None:
            result['MigrationJobClass'] = self.migration_job_class
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('MigrationMode') is not None:
            temp_model = DescribeMigrationJobStatusResponseBodyMigrationMode()
            self.migration_mode = temp_model.from_map(m['MigrationMode'])
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
        body: DescribeMigrationJobStatusResponseBody = None,
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
            temp_model = DescribeMigrationJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePreCheckStatusRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        page_no: str = None,
        page_size: str = None,
        job_code: str = None,
        struct_type: str = None,
        region_id: str = None,
        struct_phase: str = None,
        name: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.page_no = page_no
        self.page_size = page_size
        self.job_code = job_code
        self.struct_type = struct_type
        self.region_id = region_id
        self.struct_phase = struct_phase
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.job_code is not None:
            result['JobCode'] = self.job_code
        if self.struct_type is not None:
            result['StructType'] = self.struct_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.struct_phase is not None:
            result['StructPhase'] = self.struct_phase
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('JobCode') is not None:
            self.job_code = m.get('JobCode')
        if m.get('StructType') is not None:
            self.struct_type = m.get('StructType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StructPhase') is not None:
            self.struct_phase = m.get('StructPhase')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribePreCheckStatusResponseBodyJobProgressLogs(TeaModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        log_level: str = None,
        err_type: str = None,
    ):
        self.err_data = err_data
        self.err_msg = err_msg
        self.log_level = log_level
        self.err_type = err_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_data is not None:
            result['ErrData'] = self.err_data
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.err_type is not None:
            result['ErrType'] = self.err_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')
        return self


class DescribePreCheckStatusResponseBodyJobProgress(TeaModel):
    def __init__(
        self,
        skip: bool = None,
        finish_time: str = None,
        ignore_flag: str = None,
        delay_seconds: int = None,
        ddl_sql: str = None,
        state: str = None,
        boot_time: str = None,
        item: str = None,
        sub: str = None,
        total: int = None,
        target_names: str = None,
        can_skip: bool = None,
        names: str = None,
        err_detail: str = None,
        diff_row: int = None,
        job_id: str = None,
        source_schema: str = None,
        dest_schema: str = None,
        parent_obj: str = None,
        err_msg: str = None,
        order_num: int = None,
        repair_method: str = None,
        id: str = None,
        logs: List[DescribePreCheckStatusResponseBodyJobProgressLogs] = None,
    ):
        self.skip = skip
        self.finish_time = finish_time
        self.ignore_flag = ignore_flag
        self.delay_seconds = delay_seconds
        self.ddl_sql = ddl_sql
        self.state = state
        self.boot_time = boot_time
        self.item = item
        self.sub = sub
        self.total = total
        self.target_names = target_names
        self.can_skip = can_skip
        self.names = names
        self.err_detail = err_detail
        self.diff_row = diff_row
        self.job_id = job_id
        self.source_schema = source_schema
        self.dest_schema = dest_schema
        self.parent_obj = parent_obj
        self.err_msg = err_msg
        self.order_num = order_num
        self.repair_method = repair_method
        self.id = id
        self.logs = logs

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql
        if self.state is not None:
            result['State'] = self.state
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time
        if self.item is not None:
            result['Item'] = self.item
        if self.sub is not None:
            result['Sub'] = self.sub
        if self.total is not None:
            result['Total'] = self.total
        if self.target_names is not None:
            result['TargetNames'] = self.target_names
        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip
        if self.names is not None:
            result['Names'] = self.names
        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail
        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema
        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema
        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        if self.id is not None:
            result['Id'] = self.id
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('Sub') is not None:
            self.sub = m.get('Sub')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')
        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')
        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')
        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')
        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribePreCheckStatusResponseBodyJobProgressLogs()
                self.logs.append(temp_model.from_map(k))
        return self


class DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs(TeaModel):
    def __init__(
        self,
        err_data: str = None,
        err_msg: str = None,
        log_level: str = None,
        err_type: str = None,
    ):
        self.err_data = err_data
        self.err_msg = err_msg
        self.log_level = log_level
        self.err_type = err_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_data is not None:
            result['ErrData'] = self.err_data
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.err_type is not None:
            result['ErrType'] = self.err_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrData') is not None:
            self.err_data = m.get('ErrData')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('ErrType') is not None:
            self.err_type = m.get('ErrType')
        return self


class DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress(TeaModel):
    def __init__(
        self,
        skip: bool = None,
        finish_time: str = None,
        ignore_flag: str = None,
        delay_seconds: int = None,
        ddl_sql: str = None,
        state: str = None,
        boot_time: str = None,
        item: str = None,
        sub: str = None,
        total: int = None,
        target_names: str = None,
        can_skip: bool = None,
        names: str = None,
        err_detail: str = None,
        diff_row: int = None,
        job_id: str = None,
        source_schema: str = None,
        dest_schema: str = None,
        parent_obj: str = None,
        err_msg: str = None,
        order_num: int = None,
        repair_method: str = None,
        id: str = None,
        logs: List[DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs] = None,
    ):
        self.skip = skip
        self.finish_time = finish_time
        self.ignore_flag = ignore_flag
        self.delay_seconds = delay_seconds
        self.ddl_sql = ddl_sql
        self.state = state
        self.boot_time = boot_time
        self.item = item
        self.sub = sub
        self.total = total
        self.target_names = target_names
        self.can_skip = can_skip
        self.names = names
        self.err_detail = err_detail
        self.diff_row = diff_row
        self.job_id = job_id
        self.source_schema = source_schema
        self.dest_schema = dest_schema
        self.parent_obj = parent_obj
        self.err_msg = err_msg
        self.order_num = order_num
        self.repair_method = repair_method
        self.id = id
        self.logs = logs

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.ignore_flag is not None:
            result['IgnoreFlag'] = self.ignore_flag
        if self.delay_seconds is not None:
            result['DelaySeconds'] = self.delay_seconds
        if self.ddl_sql is not None:
            result['DdlSql'] = self.ddl_sql
        if self.state is not None:
            result['State'] = self.state
        if self.boot_time is not None:
            result['BootTime'] = self.boot_time
        if self.item is not None:
            result['Item'] = self.item
        if self.sub is not None:
            result['Sub'] = self.sub
        if self.total is not None:
            result['Total'] = self.total
        if self.target_names is not None:
            result['TargetNames'] = self.target_names
        if self.can_skip is not None:
            result['CanSkip'] = self.can_skip
        if self.names is not None:
            result['Names'] = self.names
        if self.err_detail is not None:
            result['ErrDetail'] = self.err_detail
        if self.diff_row is not None:
            result['DiffRow'] = self.diff_row
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.source_schema is not None:
            result['SourceSchema'] = self.source_schema
        if self.dest_schema is not None:
            result['DestSchema'] = self.dest_schema
        if self.parent_obj is not None:
            result['ParentObj'] = self.parent_obj
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        if self.id is not None:
            result['Id'] = self.id
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('IgnoreFlag') is not None:
            self.ignore_flag = m.get('IgnoreFlag')
        if m.get('DelaySeconds') is not None:
            self.delay_seconds = m.get('DelaySeconds')
        if m.get('DdlSql') is not None:
            self.ddl_sql = m.get('DdlSql')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('BootTime') is not None:
            self.boot_time = m.get('BootTime')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('Sub') is not None:
            self.sub = m.get('Sub')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TargetNames') is not None:
            self.target_names = m.get('TargetNames')
        if m.get('CanSkip') is not None:
            self.can_skip = m.get('CanSkip')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('ErrDetail') is not None:
            self.err_detail = m.get('ErrDetail')
        if m.get('DiffRow') is not None:
            self.diff_row = m.get('DiffRow')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('SourceSchema') is not None:
            self.source_schema = m.get('SourceSchema')
        if m.get('DestSchema') is not None:
            self.dest_schema = m.get('DestSchema')
        if m.get('ParentObj') is not None:
            self.parent_obj = m.get('ParentObj')
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgressLogs()
                self.logs.append(temp_model.from_map(k))
        return self


class DescribePreCheckStatusResponseBodySubDistributedJobStatus(TeaModel):
    def __init__(
        self,
        job_name: str = None,
        state: str = None,
        job_id: str = None,
        error_item: int = None,
        code: str = None,
        total: int = None,
        job_progress: List[DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress] = None,
    ):
        self.job_name = job_name
        self.state = state
        self.job_id = job_id
        self.error_item = error_item
        self.code = code
        self.total = total
        self.job_progress = job_progress

    def validate(self):
        if self.job_progress:
            for k in self.job_progress:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.state is not None:
            result['State'] = self.state
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.error_item is not None:
            result['ErrorItem'] = self.error_item
        if self.code is not None:
            result['Code'] = self.code
        if self.total is not None:
            result['Total'] = self.total
        result['JobProgress'] = []
        if self.job_progress is not None:
            for k in self.job_progress:
                result['JobProgress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ErrorItem') is not None:
            self.error_item = m.get('ErrorItem')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.job_progress = []
        if m.get('JobProgress') is not None:
            for k in m.get('JobProgress'):
                temp_model = DescribePreCheckStatusResponseBodySubDistributedJobStatusJobProgress()
                self.job_progress.append(temp_model.from_map(k))
        return self


class DescribePreCheckStatusResponseBody(TeaModel):
    def __init__(
        self,
        state: str = None,
        success: bool = None,
        page_record_count: int = None,
        total: int = None,
        http_status_code: int = None,
        request_id: str = None,
        job_name: str = None,
        job_id: str = None,
        error_item: int = None,
        total_record_count: int = None,
        code: str = None,
        page_number: int = None,
        job_progress: List[DescribePreCheckStatusResponseBodyJobProgress] = None,
        sub_distributed_job_status: List[DescribePreCheckStatusResponseBodySubDistributedJobStatus] = None,
    ):
        self.state = state
        self.success = success
        self.page_record_count = page_record_count
        self.total = total
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.job_name = job_name
        self.job_id = job_id
        self.error_item = error_item
        self.total_record_count = total_record_count
        self.code = code
        self.page_number = page_number
        self.job_progress = job_progress
        self.sub_distributed_job_status = sub_distributed_job_status

    def validate(self):
        if self.job_progress:
            for k in self.job_progress:
                if k:
                    k.validate()
        if self.sub_distributed_job_status:
            for k in self.sub_distributed_job_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.success is not None:
            result['Success'] = self.success
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total is not None:
            result['Total'] = self.total
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.error_item is not None:
            result['ErrorItem'] = self.error_item
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.code is not None:
            result['Code'] = self.code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['JobProgress'] = []
        if self.job_progress is not None:
            for k in self.job_progress:
                result['JobProgress'].append(k.to_map() if k else None)
        result['SubDistributedJobStatus'] = []
        if self.sub_distributed_job_status is not None:
            for k in self.sub_distributed_job_status:
                result['SubDistributedJobStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ErrorItem') is not None:
            self.error_item = m.get('ErrorItem')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.job_progress = []
        if m.get('JobProgress') is not None:
            for k in m.get('JobProgress'):
                temp_model = DescribePreCheckStatusResponseBodyJobProgress()
                self.job_progress.append(temp_model.from_map(k))
        self.sub_distributed_job_status = []
        if m.get('SubDistributedJobStatus') is not None:
            for k in m.get('SubDistributedJobStatus'):
                temp_model = DescribePreCheckStatusResponseBodySubDistributedJobStatus()
                self.sub_distributed_job_status.append(temp_model.from_map(k))
        return self


class DescribePreCheckStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePreCheckStatusResponseBody = None,
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
            temp_model = DescribePreCheckStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstanceAlertRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeSubscriptionInstanceAlertResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        error_alert_status: str = None,
        err_code: str = None,
        success: str = None,
        error_alert_phone: str = None,
        err_message: str = None,
        delay_alert_status: str = None,
        subscription_instance_name: str = None,
        delay_alert_phone: str = None,
        subscription_instance_id: str = None,
        delay_over_seconds: str = None,
    ):
        self.request_id = request_id
        self.error_alert_status = error_alert_status
        self.err_code = err_code
        self.success = success
        self.error_alert_phone = error_alert_phone
        self.err_message = err_message
        self.delay_alert_status = delay_alert_status
        self.subscription_instance_name = subscription_instance_name
        self.delay_alert_phone = delay_alert_phone
        self.subscription_instance_id = subscription_instance_id
        self.delay_over_seconds = delay_over_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        return self


class DescribeSubscriptionInstanceAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionInstanceAlertResponseBody = None,
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
            temp_model = DescribeSubscriptionInstanceAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstancesRequestTag(TeaModel):
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


class DescribeSubscriptionInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        page_num: int = None,
        subscription_instance_name: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
        tag: List[DescribeSubscriptionInstancesRequestTag] = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.page_num = page_num
        self.subscription_instance_name = subscription_instance_name
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSubscriptionInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
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
        whole_database: str = None,
        table_list: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList = None,
    ):
        self.database_name = database_name
        self.whole_database = whole_database
        self.table_list = table_list

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
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        if m.get('TableList') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
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


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag(TeaModel):
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


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        instance_id: str = None,
    ):
        self.instance_type = instance_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType(TeaModel):
    def __init__(
        self,
        dml: bool = None,
        ddl: bool = None,
    ):
        self.dml = dml
        self.ddl = ddl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dml is not None:
            result['DML'] = self.dml
        if self.ddl is not None:
            result['DDL'] = self.ddl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost(TeaModel):
    def __init__(
        self,
        vpchost: str = None,
        public_host: str = None,
        private_host: str = None,
    ):
        self.vpchost = vpchost
        self.public_host = public_host
        self.private_host = private_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpchost is not None:
            result['VPCHost'] = self.vpchost
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VPCHost') is not None:
            self.vpchost = m.get('VPCHost')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
        return self


class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        pay_type: str = None,
        consumption_client: str = None,
        consumption_checkpoint: str = None,
        end_timestamp: str = None,
        instance_create_time: str = None,
        begin_timestamp: str = None,
        subscribe_topic: str = None,
        subscription_instance_name: str = None,
        subscription_instance_id: str = None,
        job_create_time: str = None,
        subscription_object: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject = None,
        tags: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags = None,
        source_endpoint: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint = None,
        subscription_data_type: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType = None,
        subscription_host: DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost = None,
    ):
        self.status = status
        self.error_message = error_message
        self.pay_type = pay_type
        self.consumption_client = consumption_client
        self.consumption_checkpoint = consumption_checkpoint
        self.end_timestamp = end_timestamp
        self.instance_create_time = instance_create_time
        self.begin_timestamp = begin_timestamp
        self.subscribe_topic = subscribe_topic
        self.subscription_instance_name = subscription_instance_name
        self.subscription_instance_id = subscription_instance_id
        self.job_create_time = job_create_time
        self.subscription_object = subscription_object
        self.tags = tags
        self.source_endpoint = source_endpoint
        self.subscription_data_type = subscription_data_type
        self.subscription_host = subscription_host

    def validate(self):
        if self.subscription_object:
            self.subscription_object.validate()
        if self.tags:
            self.tags.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_host:
            self.subscription_host.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object.to_map()
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_host is not None:
            result['SubscriptionHost'] = self.subscription_host.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')
        if m.get('SubscriptionObject') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject()
            self.subscription_object = temp_model.from_map(m['SubscriptionObject'])
        if m.get('Tags') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionHost') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost()
            self.subscription_host = temp_model.from_map(m['SubscriptionHost'])
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
        request_id: str = None,
        err_code: str = None,
        page_record_count: int = None,
        success: str = None,
        total_record_count: int = None,
        err_message: str = None,
        page_number: int = None,
        subscription_instances: DescribeSubscriptionInstancesResponseBodySubscriptionInstances = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.page_record_count = page_record_count
        self.success = success
        self.total_record_count = total_record_count
        self.err_message = err_message
        self.page_number = page_number
        self.subscription_instances = subscription_instances

    def validate(self):
        if self.subscription_instances:
            self.subscription_instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.subscription_instances is not None:
            result['SubscriptionInstances'] = self.subscription_instances.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('SubscriptionInstances') is not None:
            temp_model = DescribeSubscriptionInstancesResponseBodySubscriptionInstances()
            self.subscription_instances = temp_model.from_map(m['SubscriptionInstances'])
        return self


class DescribeSubscriptionInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionInstancesResponseBody = None,
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
            temp_model = DescribeSubscriptionInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        instance_id: str = None,
    ):
        self.instance_type = instance_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType(TeaModel):
    def __init__(
        self,
        dml: bool = None,
        ddl: bool = None,
    ):
        self.dml = dml
        self.ddl = ddl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dml is not None:
            result['DML'] = self.dml
        if self.ddl is not None:
            result['DDL'] = self.ddl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DML') is not None:
            self.dml = m.get('DML')
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')
        return self


class DescribeSubscriptionInstanceStatusResponseBodySubscriptionHost(TeaModel):
    def __init__(
        self,
        vpchost: str = None,
        public_host: str = None,
        private_host: str = None,
    ):
        self.vpchost = vpchost
        self.public_host = public_host
        self.private_host = private_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpchost is not None:
            result['VPCHost'] = self.vpchost
        if self.public_host is not None:
            result['PublicHost'] = self.public_host
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VPCHost') is not None:
            self.vpchost = m.get('VPCHost')
        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')
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
        whole_database: str = None,
        table_list: DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList = None,
    ):
        self.database_name = database_name
        self.whole_database = whole_database
        self.table_list = table_list

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
        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database
        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        if m.get('TableList') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
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
        status: str = None,
        error_message: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
        pay_type: str = None,
        consumption_client: str = None,
        consumption_checkpoint: str = None,
        end_timestamp: str = None,
        begin_timestamp: str = None,
        request_id: str = None,
        subscribe_topic: str = None,
        subscription_instance_name: str = None,
        subscription_instance_id: str = None,
        task_id: str = None,
        source_endpoint: DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint = None,
        subscription_data_type: DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType = None,
        subscription_host: DescribeSubscriptionInstanceStatusResponseBodySubscriptionHost = None,
        subscription_object: DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject = None,
    ):
        self.status = status
        self.error_message = error_message
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.pay_type = pay_type
        self.consumption_client = consumption_client
        self.consumption_checkpoint = consumption_checkpoint
        self.end_timestamp = end_timestamp
        self.begin_timestamp = begin_timestamp
        self.request_id = request_id
        self.subscribe_topic = subscribe_topic
        self.subscription_instance_name = subscription_instance_name
        self.subscription_instance_id = subscription_instance_id
        self.task_id = task_id
        self.source_endpoint = source_endpoint
        self.subscription_data_type = subscription_data_type
        self.subscription_host = subscription_host
        self.subscription_object = subscription_object

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_host:
            self.subscription_host.validate()
        if self.subscription_object:
            self.subscription_object.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client
        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint
        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic
        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()
        if self.subscription_host is not None:
            result['SubscriptionHost'] = self.subscription_host.to_map()
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')
        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')
        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')
        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')
        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('SubscriptionDataType') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m['SubscriptionDataType'])
        if m.get('SubscriptionHost') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionHost()
            self.subscription_host = temp_model.from_map(m['SubscriptionHost'])
        if m.get('SubscriptionObject') is not None:
            temp_model = DescribeSubscriptionInstanceStatusResponseBodySubscriptionObject()
            self.subscription_object = temp_model.from_map(m['SubscriptionObject'])
        return self


class DescribeSubscriptionInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionInstanceStatusResponseBody = None,
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
            temp_model = DescribeSubscriptionInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubscriptionMetaRequest(TeaModel):
    def __init__(
        self,
        sid: str = None,
        dts_instance_id: str = None,
        sub_migration_job_ids: Dict[str, Any] = None,
        topics: Dict[str, Any] = None,
        region_id: str = None,
    ):
        self.sid = sid
        self.dts_instance_id = dts_instance_id
        self.sub_migration_job_ids = sub_migration_job_ids
        self.topics = topics
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.sub_migration_job_ids is not None:
            result['SubMigrationJobIds'] = self.sub_migration_job_ids
        if self.topics is not None:
            result['Topics'] = self.topics
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SubMigrationJobIds') is not None:
            self.sub_migration_job_ids = m.get('SubMigrationJobIds')
        if m.get('Topics') is not None:
            self.topics = m.get('Topics')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSubscriptionMetaShrinkRequest(TeaModel):
    def __init__(
        self,
        sid: str = None,
        dts_instance_id: str = None,
        sub_migration_job_ids_shrink: str = None,
        topics_shrink: str = None,
        region_id: str = None,
    ):
        self.sid = sid
        self.dts_instance_id = dts_instance_id
        self.sub_migration_job_ids_shrink = sub_migration_job_ids_shrink
        self.topics_shrink = topics_shrink
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.sub_migration_job_ids_shrink is not None:
            result['SubMigrationJobIds'] = self.sub_migration_job_ids_shrink
        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SubMigrationJobIds') is not None:
            self.sub_migration_job_ids_shrink = m.get('SubMigrationJobIds')
        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeSubscriptionMetaResponseBodySubscriptionMetaList(TeaModel):
    def __init__(
        self,
        sid: str = None,
        checkpoint: int = None,
        dproxy_url: str = None,
        dblist: str = None,
        topic: str = None,
    ):
        self.sid = sid
        self.checkpoint = checkpoint
        self.dproxy_url = dproxy_url
        self.dblist = dblist
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sid is not None:
            result['Sid'] = self.sid
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.dproxy_url is not None:
            result['DProxyUrl'] = self.dproxy_url
        if self.dblist is not None:
            result['DBList'] = self.dblist
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sid') is not None:
            self.sid = m.get('Sid')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DProxyUrl') is not None:
            self.dproxy_url = m.get('DProxyUrl')
        if m.get('DBList') is not None:
            self.dblist = m.get('DBList')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DescribeSubscriptionMetaResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
        subscription_meta_list: List[DescribeSubscriptionMetaResponseBodySubscriptionMetaList] = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.subscription_meta_list = subscription_meta_list

    def validate(self):
        if self.subscription_meta_list:
            for k in self.subscription_meta_list:
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
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        result['SubscriptionMetaList'] = []
        if self.subscription_meta_list is not None:
            for k in self.subscription_meta_list:
                result['SubscriptionMetaList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        self.subscription_meta_list = []
        if m.get('SubscriptionMetaList') is not None:
            for k in m.get('SubscriptionMetaList'):
                temp_model = DescribeSubscriptionMetaResponseBodySubscriptionMetaList()
                self.subscription_meta_list.append(temp_model.from_map(k))
        return self


class DescribeSubscriptionMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubscriptionMetaResponseBody = None,
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
            temp_model = DescribeSubscriptionMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobAlertRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeSynchronizationJobAlertResponseBody(TeaModel):
    def __init__(
        self,
        synchronization_job_name: str = None,
        error_alert_status: str = None,
        err_code: str = None,
        success: str = None,
        error_alert_phone: str = None,
        err_message: str = None,
        delay_alert_status: str = None,
        delay_alert_phone: str = None,
        delay_over_seconds: str = None,
        request_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
    ):
        self.synchronization_job_name = synchronization_job_name
        self.error_alert_status = error_alert_status
        self.err_code = err_code
        self.success = success
        self.error_alert_phone = error_alert_phone
        self.err_message = err_message
        self.delay_alert_status = delay_alert_status
        self.delay_alert_phone = delay_alert_phone
        self.delay_over_seconds = delay_over_seconds
        self.request_id = request_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone
        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')
        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        return self


class DescribeSynchronizationJobAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobAlertResponseBody = None,
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
            temp_model = DescribeSynchronizationJobAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobReplicatorCompareRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeSynchronizationJobReplicatorCompareResponseBody(TeaModel):
    def __init__(
        self,
        synchronization_replicator_compare_enable: bool = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.synchronization_replicator_compare_enable = synchronization_replicator_compare_enable
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronization_replicator_compare_enable is not None:
            result['SynchronizationReplicatorCompareEnable'] = self.synchronization_replicator_compare_enable
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronizationReplicatorCompareEnable') is not None:
            self.synchronization_replicator_compare_enable = m.get('SynchronizationReplicatorCompareEnable')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class DescribeSynchronizationJobReplicatorCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobReplicatorCompareResponseBody = None,
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
            temp_model = DescribeSynchronizationJobReplicatorCompareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobsRequestTag(TeaModel):
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


class DescribeSynchronizationJobsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_size: int = None,
        page_num: int = None,
        synchronization_job_name: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
        tag: List[DescribeSynchronizationJobsRequestTag] = None,
    ):
        self.region_id = region_id
        self.page_size = page_size
        self.page_num = page_num
        self.synchronization_job_name = synchronization_job_name
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeSynchronizationJobsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags(TeaModel):
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


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        delay: str = None,
        percent: str = None,
        error_message: str = None,
    ):
        self.status = status
        self.delay = delay
        self.percent = percent
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.instance_id = instance_id
        self.ip = ip
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance(TeaModel):
    def __init__(
        self,
        rps: str = None,
        flow: str = None,
    ):
        self.rps = rps
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rps is not None:
            result['RPS'] = self.rps
        if self.flow is not None:
            result['FLOW'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
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
        status: str = None,
        percent: str = None,
        detail: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail] = None,
    ):
        self.status = status
        self.percent = percent
        self.detail = detail

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
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.instance_id = instance_id
        self.ip = ip
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeSynchronizationJobsResponseBodySynchronizationInstances(TeaModel):
    def __init__(
        self,
        data_initialization: str = None,
        status: str = None,
        synchronization_job_name: str = None,
        delay: str = None,
        error_message: str = None,
        expire_time: str = None,
        create_time: str = None,
        pay_type: str = None,
        structure_initialization: str = None,
        synchronization_job_class: str = None,
        instance_create_time: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        job_create_time: str = None,
        tags: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags] = None,
        synchronization_objects: List[DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects] = None,
        data_initialization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus = None,
        destination_endpoint: DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint = None,
        performance: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance = None,
        precheck_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus = None,
        source_endpoint: DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint = None,
        structure_initialization_status: DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus = None,
    ):
        self.data_initialization = data_initialization
        self.status = status
        self.synchronization_job_name = synchronization_job_name
        self.delay = delay
        self.error_message = error_message
        self.expire_time = expire_time
        self.create_time = create_time
        self.pay_type = pay_type
        self.structure_initialization = structure_initialization
        self.synchronization_job_class = synchronization_job_class
        self.instance_create_time = instance_create_time
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.job_create_time = job_create_time
        self.tags = tags
        self.synchronization_objects = synchronization_objects
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.destination_endpoint = destination_endpoint
        self.performance = performance
        self.precheck_status = precheck_status
        self.source_endpoint = source_endpoint
        self.structure_initialization_status = structure_initialization_status

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.synchronization_objects:
            for k in self.synchronization_objects:
                if k:
                    k.validate()
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

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.status is not None:
            result['Status'] = self.status
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags()
                self.tags.append(temp_model.from_map(k))
        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k in m.get('SynchronizationObjects'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k))
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeSynchronizationJobsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        request_id: str = None,
        page_record_count: int = None,
        total_record_count: int = None,
        synchronization_instances: List[DescribeSynchronizationJobsResponseBodySynchronizationInstances] = None,
    ):
        self.page_number = page_number
        self.request_id = request_id
        self.page_record_count = page_record_count
        self.total_record_count = total_record_count
        self.synchronization_instances = synchronization_instances

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        result['SynchronizationInstances'] = []
        if self.synchronization_instances is not None:
            for k in self.synchronization_instances:
                result['SynchronizationInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        self.synchronization_instances = []
        if m.get('SynchronizationInstances') is not None:
            for k in m.get('SynchronizationInstances'):
                temp_model = DescribeSynchronizationJobsResponseBodySynchronizationInstances()
                self.synchronization_instances.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobsResponseBody = None,
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
            temp_model = DescribeSynchronizationJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        delay: str = None,
        percent: str = None,
        error_message: str = None,
        delay_millis: int = None,
        checkpoint: str = None,
    ):
        self.status = status
        self.delay = delay
        self.percent = percent
        self.error_message = error_message
        self.delay_millis = delay_millis
        self.checkpoint = checkpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.delay_millis is not None:
            result['DelayMillis'] = self.delay_millis
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('DelayMillis') is not None:
            self.delay_millis = m.get('DelayMillis')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        return self


class DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.instance_id = instance_id
        self.ip = ip
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeSynchronizationJobStatusResponseBodyPerformance(TeaModel):
    def __init__(
        self,
        rps: str = None,
        flow: str = None,
    ):
        self.rps = rps
        self.flow = flow

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rps is not None:
            result['RPS'] = self.rps
        if self.flow is not None:
            result['FLOW'] = self.flow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RPS') is not None:
            self.rps = m.get('RPS')
        if m.get('FLOW') is not None:
            self.flow = m.get('FLOW')
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
        status: str = None,
        percent: str = None,
        detail: List[DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail] = None,
    ):
        self.status = status
        self.percent = percent
        self.detail = detail

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
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusResponseBodySourceEndpoint(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        ip: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
        engine_name: str = None,
    ):
        self.instance_id = instance_id
        self.ip = ip
        self.instance_type = instance_type
        self.port = port
        self.user_name = user_name
        self.engine_name = engine_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.port is not None:
            result['Port'] = self.port
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.engine_name is not None:
            result['EngineName'] = self.engine_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')
        return self


class DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
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
        synchronization_job_name: str = None,
        status: str = None,
        data_initialization: str = None,
        delay: str = None,
        error_message: str = None,
        expire_time: str = None,
        err_code: str = None,
        success: str = None,
        structure_initialization: str = None,
        pay_type: str = None,
        err_message: str = None,
        synchronization_job_class: str = None,
        request_id: str = None,
        synchronization_job_id: str = None,
        delay_millis: int = None,
        synchronization_direction: str = None,
        task_id: str = None,
        checkpoint: str = None,
        data_initialization_status: DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus = None,
        destination_endpoint: DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint = None,
        performance: DescribeSynchronizationJobStatusResponseBodyPerformance = None,
        precheck_status: DescribeSynchronizationJobStatusResponseBodyPrecheckStatus = None,
        source_endpoint: DescribeSynchronizationJobStatusResponseBodySourceEndpoint = None,
        structure_initialization_status: DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus = None,
        synchronization_objects: List[DescribeSynchronizationJobStatusResponseBodySynchronizationObjects] = None,
    ):
        self.synchronization_job_name = synchronization_job_name
        self.status = status
        self.data_initialization = data_initialization
        self.delay = delay
        self.error_message = error_message
        self.expire_time = expire_time
        self.err_code = err_code
        self.success = success
        self.structure_initialization = structure_initialization
        self.pay_type = pay_type
        self.err_message = err_message
        self.synchronization_job_class = synchronization_job_class
        self.request_id = request_id
        self.synchronization_job_id = synchronization_job_id
        self.delay_millis = delay_millis
        self.synchronization_direction = synchronization_direction
        self.task_id = task_id
        self.checkpoint = checkpoint
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.destination_endpoint = destination_endpoint
        self.performance = performance
        self.precheck_status = precheck_status
        self.source_endpoint = source_endpoint
        self.structure_initialization_status = structure_initialization_status
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
        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name
        if self.status is not None:
            result['Status'] = self.status
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.delay_millis is not None:
            result['DelayMillis'] = self.delay_millis
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()
        if self.performance is not None:
            result['Performance'] = self.performance.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k in self.synchronization_objects:
                result['SynchronizationObjects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('DelayMillis') is not None:
            self.delay_millis = m.get('DelayMillis')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('DestinationEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m['DestinationEndpoint'])
        if m.get('Performance') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPerformance()
            self.performance = temp_model.from_map(m['Performance'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('SourceEndpoint') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
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
        body: DescribeSynchronizationJobStatusResponseBody = None,
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
            temp_model = DescribeSynchronizationJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationJobStatusListRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id_list_json_str: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id_list_json_str = synchronization_job_id_list_json_str
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id_list_json_str is not None:
            result['SynchronizationJobIdListJsonStr'] = self.synchronization_job_id_list_json_str
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobIdListJsonStr') is not None:
            self.synchronization_job_id_list_json_str = m.get('SynchronizationJobIdListJsonStr')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList(TeaModel):
    def __init__(
        self,
        status: str = None,
        synchronization_direction: str = None,
        checkpoint: str = None,
    ):
        self.status = status
        self.synchronization_direction = synchronization_direction
        self.checkpoint = checkpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')
        return self


class DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList(TeaModel):
    def __init__(
        self,
        synchronization_job_id: str = None,
        synchronization_direction_info_list: List[DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList] = None,
    ):
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction_info_list = synchronization_direction_info_list

    def validate(self):
        if self.synchronization_direction_info_list:
            for k in self.synchronization_direction_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        result['SynchronizationDirectionInfoList'] = []
        if self.synchronization_direction_info_list is not None:
            for k in self.synchronization_direction_info_list:
                result['SynchronizationDirectionInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        self.synchronization_direction_info_list = []
        if m.get('SynchronizationDirectionInfoList') is not None:
            for k in m.get('SynchronizationDirectionInfoList'):
                temp_model = DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusListSynchronizationDirectionInfoList()
                self.synchronization_direction_info_list.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        page_record_count: int = None,
        success: str = None,
        total_record_count: int = None,
        err_message: str = None,
        page_number: int = None,
        synchronization_job_list_status_list: List[DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList] = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.page_record_count = page_record_count
        self.success = success
        self.total_record_count = total_record_count
        self.err_message = err_message
        self.page_number = page_number
        self.synchronization_job_list_status_list = synchronization_job_list_status_list

    def validate(self):
        if self.synchronization_job_list_status_list:
            for k in self.synchronization_job_list_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.success is not None:
            result['Success'] = self.success
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['SynchronizationJobListStatusList'] = []
        if self.synchronization_job_list_status_list is not None:
            for k in self.synchronization_job_list_status_list:
                result['SynchronizationJobListStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.synchronization_job_list_status_list = []
        if m.get('SynchronizationJobListStatusList') is not None:
            for k in m.get('SynchronizationJobListStatusList'):
                temp_model = DescribeSynchronizationJobStatusListResponseBodySynchronizationJobListStatusList()
                self.synchronization_job_list_status_list.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationJobStatusListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationJobStatusListResponseBody = None,
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
            temp_model = DescribeSynchronizationJobStatusListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronizationObjectModifyStatusRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        task_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.task_id = task_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        delay: str = None,
        percent: str = None,
        error_message: str = None,
    ):
        self.status = status
        self.delay = delay
        self.percent = percent
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
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
        status: str = None,
        percent: str = None,
        detail: List[DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail] = None,
    ):
        self.status = status
        self.percent = percent
        self.detail = detail

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
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        result['Detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['Detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        self.detail = []
        if m.get('Detail') is not None:
            for k in m.get('Detail'):
                temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: str = None,
        error_message: str = None,
        progress: str = None,
    ):
        self.status = status
        self.percent = percent
        self.error_message = error_message
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class DescribeSynchronizationObjectModifyStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
        data_initialization_status: DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus = None,
        precheck_status: DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus = None,
        structure_initialization_status: DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus = None,
    ):
        self.status = status
        self.error_message = error_message
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.data_initialization_status = data_initialization_status
        self.data_synchronization_status = data_synchronization_status
        self.precheck_status = precheck_status
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
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()
        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()
        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DataInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m['DataInitializationStatus'])
        if m.get('DataSynchronizationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m['DataSynchronizationStatus'])
        if m.get('PrecheckStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m['PrecheckStatus'])
        if m.get('StructureInitializationStatus') is not None:
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m['StructureInitializationStatus'])
        return self


class DescribeSynchronizationObjectModifyStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSynchronizationObjectModifyStatusResponseBody = None,
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
            temp_model = DescribeSynchronizationObjectModifyStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IgnoreJobDetailRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_code: str = None,
        id: str = None,
        region_id: str = None,
        synchronization_direction: str = None,
        dts_instance_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.job_code = job_code
        self.id = id
        self.region_id = region_id
        self.synchronization_direction = synchronization_direction
        self.dts_instance_id = dts_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.job_code is not None:
            result['JobCode'] = self.job_code
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('JobCode') is not None:
            self.job_code = m.get('JobCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        return self


class IgnoreJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IgnoreJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IgnoreJobDetailResponseBody = None,
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
            temp_model = IgnoreJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitDtsRdsInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        endpoint_instance_type: str = None,
        endpoint_region: str = None,
        endpoint_instance_id: str = None,
        endpoint_cen_id: str = None,
    ):
        self.region_id = region_id
        self.endpoint_instance_type = endpoint_instance_type
        self.endpoint_region = endpoint_region
        self.endpoint_instance_id = endpoint_instance_id
        self.endpoint_cen_id = endpoint_cen_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.endpoint_instance_type is not None:
            result['EndpointInstanceType'] = self.endpoint_instance_type
        if self.endpoint_region is not None:
            result['EndpointRegion'] = self.endpoint_region
        if self.endpoint_instance_id is not None:
            result['EndpointInstanceId'] = self.endpoint_instance_id
        if self.endpoint_cen_id is not None:
            result['EndpointCenId'] = self.endpoint_cen_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('EndpointInstanceType') is not None:
            self.endpoint_instance_type = m.get('EndpointInstanceType')
        if m.get('EndpointRegion') is not None:
            self.endpoint_region = m.get('EndpointRegion')
        if m.get('EndpointInstanceId') is not None:
            self.endpoint_instance_id = m.get('EndpointInstanceId')
        if m.get('EndpointCenId') is not None:
            self.endpoint_cen_id = m.get('EndpointCenId')
        return self


class InitDtsRdsInstanceResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
        admin_account: str = None,
        admin_password: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.admin_account = admin_account
        self.admin_password = admin_password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.admin_account is not None:
            result['AdminAccount'] = self.admin_account
        if self.admin_password is not None:
            result['AdminPassword'] = self.admin_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('AdminAccount') is not None:
            self.admin_account = m.get('AdminAccount')
        if m.get('AdminPassword') is not None:
            self.admin_password = m.get('AdminPassword')
        return self


class InitDtsRdsInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitDtsRdsInstanceResponseBody = None,
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
            temp_model = InitDtsRdsInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.resource_id = resource_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        resource_type: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyConsumerChannelRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        consumer_group_id: str = None,
        consumer_group_password: str = None,
        consumer_group_user_name: str = None,
        consumer_group_name: str = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.dts_job_id = dts_job_id
        self.consumer_group_id = consumer_group_id
        self.consumer_group_password = consumer_group_password
        self.consumer_group_user_name = consumer_group_user_name
        self.consumer_group_name = consumer_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        return self


class ModifyConsumerChannelResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ModifyConsumerChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyConsumerChannelResponseBody = None,
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
            temp_model = ModifyConsumerChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyConsumerGroupPasswordRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_group_user_name: str = None,
        consumer_group_password: str = None,
        consumer_group_new_password: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.consumer_group_id = consumer_group_id
        self.consumer_group_name = consumer_group_name
        self.consumer_group_user_name = consumer_group_user_name
        self.consumer_group_password = consumer_group_password
        self.consumer_group_new_password = consumer_group_new_password
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.consumer_group_id is not None:
            result['ConsumerGroupID'] = self.consumer_group_id
        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name
        if self.consumer_group_user_name is not None:
            result['ConsumerGroupUserName'] = self.consumer_group_user_name
        if self.consumer_group_password is not None:
            result['ConsumerGroupPassword'] = self.consumer_group_password
        if self.consumer_group_new_password is not None:
            result['consumerGroupNewPassword'] = self.consumer_group_new_password
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('ConsumerGroupID') is not None:
            self.consumer_group_id = m.get('ConsumerGroupID')
        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')
        if m.get('ConsumerGroupUserName') is not None:
            self.consumer_group_user_name = m.get('ConsumerGroupUserName')
        if m.get('ConsumerGroupPassword') is not None:
            self.consumer_group_password = m.get('ConsumerGroupPassword')
        if m.get('consumerGroupNewPassword') is not None:
            self.consumer_group_new_password = m.get('consumerGroupNewPassword')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ModifyConsumerGroupPasswordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ModifyConsumerGroupPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyConsumerGroupPasswordResponseBody = None,
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
            temp_model = ModifyConsumerGroupPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyConsumptionTimestampRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        consumption_timestamp: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.consumption_timestamp = consumption_timestamp
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.consumption_timestamp is not None:
            result['ConsumptionTimestamp'] = self.consumption_timestamp
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('ConsumptionTimestamp') is not None:
            self.consumption_timestamp = m.get('ConsumptionTimestamp')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ModifyConsumptionTimestampResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ModifyConsumptionTimestampResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyConsumptionTimestampResponseBody = None,
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
            temp_model = ModifyConsumptionTimestampResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDtsJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        client_token: str = None,
        db_list: Dict[str, Any] = None,
        etl_operator_column_reference: str = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.client_token = client_token
        self.db_list = db_list
        self.etl_operator_column_reference = etl_operator_column_reference

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.etl_operator_column_reference is not None:
            result['EtlOperatorColumnReference'] = self.etl_operator_column_reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('EtlOperatorColumnReference') is not None:
            self.etl_operator_column_reference = m.get('EtlOperatorColumnReference')
        return self


class ModifyDtsJobShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        client_token: str = None,
        db_list_shrink: str = None,
        etl_operator_column_reference: str = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.client_token = client_token
        self.db_list_shrink = db_list_shrink
        self.etl_operator_column_reference = etl_operator_column_reference

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.db_list_shrink is not None:
            result['DbList'] = self.db_list_shrink
        if self.etl_operator_column_reference is not None:
            result['EtlOperatorColumnReference'] = self.etl_operator_column_reference
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbList') is not None:
            self.db_list_shrink = m.get('DbList')
        if m.get('EtlOperatorColumnReference') is not None:
            self.etl_operator_column_reference = m.get('EtlOperatorColumnReference')
        return self


class ModifyDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        dts_job_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: bool = None,
    ):
        self.status = status
        self.request_id = request_id
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ModifyDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDtsJobResponseBody = None,
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
            temp_model = ModifyDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDtsJobNameRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_job_name: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_job_name = dts_job_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDtsJobNameResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        code: str = None,
        dynamic_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.code = code
        self.dynamic_message = dynamic_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        return self


class ModifyDtsJobNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDtsJobNameResponseBody = None,
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
            temp_model = ModifyDtsJobNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDtsJobPasswordRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        user_name: str = None,
        password: str = None,
        endpoint: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.user_name = user_name
        self.password = password
        self.endpoint = endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDtsJobPasswordResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        code: str = None,
        dynamic_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.code = code
        self.dynamic_message = dynamic_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        return self


class ModifyDtsJobPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDtsJobPasswordResponseBody = None,
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
            temp_model = ModifyDtsJobPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubscriptionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        db_list: str = None,
        dts_job_id: str = None,
        subscription_data_type_ddl: bool = None,
        subscription_data_type_dml: bool = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.db_list = db_list
        self.dts_job_id = dts_job_id
        self.subscription_data_type_ddl = subscription_data_type_ddl
        self.subscription_data_type_dml = subscription_data_type_dml

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.db_list is not None:
            result['DbList'] = self.db_list
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.subscription_data_type_ddl is not None:
            result['SubscriptionDataTypeDDL'] = self.subscription_data_type_ddl
        if self.subscription_data_type_dml is not None:
            result['SubscriptionDataTypeDML'] = self.subscription_data_type_dml
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('SubscriptionDataTypeDDL') is not None:
            self.subscription_data_type_ddl = m.get('SubscriptionDataTypeDDL')
        if m.get('SubscriptionDataTypeDML') is not None:
            self.subscription_data_type_dml = m.get('SubscriptionDataTypeDML')
        return self


class ModifySubscriptionResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: str = None,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ModifySubscriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySubscriptionResponseBody = None,
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
            temp_model = ModifySubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySubscriptionObjectRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        subscription_object: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.subscription_object = subscription_object
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('SubscriptionObject') is not None:
            self.subscription_object = m.get('SubscriptionObject')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ModifySubscriptionObjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ModifySubscriptionObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySubscriptionObjectResponseBody = None,
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
            temp_model = ModifySubscriptionObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySynchronizationObjectRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_objects: str = None,
        synchronization_direction: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_objects = synchronization_objects
        self.synchronization_direction = synchronization_direction
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_objects is not None:
            result['SynchronizationObjects'] = self.synchronization_objects
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationObjects') is not None:
            self.synchronization_objects = m.get('SynchronizationObjects')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ModifySynchronizationObjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        task_id: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.task_id = task_id
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ModifySynchronizationObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySynchronizationObjectResponseBody = None,
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
            temp_model = ModifySynchronizationObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        charge_type: str = None,
        period: str = None,
        buy_count: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.charge_type = charge_type
        self.period = period
        self.buy_count = buy_count
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        end_time: str = None,
        request_id: str = None,
        err_code: str = None,
        dts_job_id: str = None,
        success: bool = None,
        err_message: str = None,
        charge_type: str = None,
        code: str = None,
        dynamic_message: str = None,
        instance_id: str = None,
    ):
        self.http_status_code = http_status_code
        self.end_time = end_time
        self.request_id = request_id
        self.err_code = err_code
        self.dts_job_id = dts_job_id
        self.success = success
        self.err_message = err_message
        self.charge_type = charge_type
        self.code = code
        self.dynamic_message = dynamic_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class ResetDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetDtsJobResponseBody = None,
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
            temp_model = ResetDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class ResetSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ResetSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetSynchronizationJobResponseBody = None,
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
            temp_model = ResetSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShieldPrecheckRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        dts_instance_id: str = None,
        precheck_items: str = None,
    ):
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id
        self.precheck_items = precheck_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.precheck_items is not None:
            result['PrecheckItems'] = self.precheck_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('PrecheckItems') is not None:
            self.precheck_items = m.get('PrecheckItems')
        return self


class ShieldPrecheckResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class ShieldPrecheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ShieldPrecheckResponseBody = None,
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
            temp_model = ShieldPrecheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SkipPreCheckRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        skip: bool = None,
        skip_pre_check_items: str = None,
        skip_pre_check_names: str = None,
        dts_job_id: str = None,
        region_id: str = None,
    ):
        self.job_id = job_id
        self.skip = skip
        self.skip_pre_check_items = skip_pre_check_items
        self.skip_pre_check_names = skip_pre_check_names
        self.dts_job_id = dts_job_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.skip is not None:
            result['Skip'] = self.skip
        if self.skip_pre_check_items is not None:
            result['SkipPreCheckItems'] = self.skip_pre_check_items
        if self.skip_pre_check_names is not None:
            result['SkipPreCheckNames'] = self.skip_pre_check_names
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Skip') is not None:
            self.skip = m.get('Skip')
        if m.get('SkipPreCheckItems') is not None:
            self.skip_pre_check_items = m.get('SkipPreCheckItems')
        if m.get('SkipPreCheckNames') is not None:
            self.skip_pre_check_names = m.get('SkipPreCheckNames')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SkipPreCheckResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        skip_names: str = None,
        code: str = None,
        schedule_job_id: str = None,
        dynamic_message: str = None,
        migration_job_id: str = None,
        skip_items: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.skip_names = skip_names
        self.code = code
        self.schedule_job_id = schedule_job_id
        self.dynamic_message = dynamic_message
        self.migration_job_id = migration_job_id
        self.skip_items = skip_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.skip_names is not None:
            result['SkipNames'] = self.skip_names
        if self.code is not None:
            result['Code'] = self.code
        if self.schedule_job_id is not None:
            result['ScheduleJobId'] = self.schedule_job_id
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.skip_items is not None:
            result['SkipItems'] = self.skip_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('SkipNames') is not None:
            self.skip_names = m.get('SkipNames')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ScheduleJobId') is not None:
            self.schedule_job_id = m.get('ScheduleJobId')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('SkipItems') is not None:
            self.skip_items = m.get('SkipItems')
        return self


class SkipPreCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SkipPreCheckResponseBody = None,
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
            temp_model = SkipPreCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class StartDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartDtsJobResponseBody = None,
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
            temp_model = StartDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMigrationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class StartMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class StartMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartMigrationJobResponseBody = None,
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
            temp_model = StartMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSubscriptionInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        subscription_instance_id: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.subscription_instance_id = subscription_instance_id
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class StartSubscriptionInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        task_id: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.task_id = task_id
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class StartSubscriptionInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartSubscriptionInstanceResponseBody = None,
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
            temp_model = StartSubscriptionInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class StartSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class StartSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartSynchronizationJobResponseBody = None,
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
            temp_model = StartSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class StopDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopDtsJobResponseBody = None,
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
            temp_model = StopDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopMigrationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        migration_job_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class StopMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class StopMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopMigrationJobResponseBody = None,
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
            temp_model = StopMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SummaryJobDetailRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        job_code: str = None,
        synchronization_direction: str = None,
        region_id: str = None,
        dts_instance_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.job_code = job_code
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id
        self.dts_instance_id = dts_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.job_code is not None:
            result['JobCode'] = self.job_code
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('JobCode') is not None:
            self.job_code = m.get('JobCode')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        return self


class SummaryJobDetailResponseBodyProgressSummaryDetails(TeaModel):
    def __init__(
        self,
        key: str = None,
        total_count: int = None,
        state: int = None,
    ):
        self.key = key
        self.total_count = total_count
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class SummaryJobDetailResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        code: str = None,
        request_id: str = None,
        success: bool = None,
        job_id: str = None,
        progress_summary_details: List[SummaryJobDetailResponseBodyProgressSummaryDetails] = None,
    ):
        self.http_status_code = http_status_code
        self.code = code
        self.request_id = request_id
        self.success = success
        self.job_id = job_id
        self.progress_summary_details = progress_summary_details

    def validate(self):
        if self.progress_summary_details:
            for k in self.progress_summary_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.job_id is not None:
            result['JobId'] = self.job_id
        result['ProgressSummaryDetails'] = []
        if self.progress_summary_details is not None:
            for k in self.progress_summary_details:
                result['ProgressSummaryDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        self.progress_summary_details = []
        if m.get('ProgressSummaryDetails') is not None:
            for k in m.get('ProgressSummaryDetails'):
                temp_model = SummaryJobDetailResponseBodyProgressSummaryDetails()
                self.progress_summary_details.append(temp_model.from_map(k))
        return self


class SummaryJobDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SummaryJobDetailResponseBody = None,
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
            temp_model = SummaryJobDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendDtsJobRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        dts_instance_id: str = None,
        synchronization_direction: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.dts_instance_id = dts_instance_id
        self.synchronization_direction = synchronization_direction
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SuspendDtsJobResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class SuspendDtsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendDtsJobResponseBody = None,
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
            temp_model = SuspendDtsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendMigrationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        migration_job_id: str = None,
        client_token: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.migration_job_id = migration_job_id
        self.client_token = client_token
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class SuspendMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class SuspendMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendMigrationJobResponseBody = None,
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
            temp_model = SuspendMigrationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendSynchronizationJobRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class SuspendSynchronizationJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class SuspendSynchronizationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendSynchronizationJobResponseBody = None,
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
            temp_model = SuspendSynchronizationJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchSynchronizationEndpointRequestEndpoint(TeaModel):
    def __init__(
        self,
        type: str = None,
        instance_type: str = None,
        instance_id: str = None,
        ip: str = None,
        port: str = None,
    ):
        self.type = type
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.ip = ip
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip is not None:
            result['IP'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class SwitchSynchronizationEndpointRequestSourceEndpoint(TeaModel):
    def __init__(
        self,
        owner_id: str = None,
        role: str = None,
    ):
        self.owner_id = owner_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class SwitchSynchronizationEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint: SwitchSynchronizationEndpointRequestEndpoint = None,
        source_endpoint: SwitchSynchronizationEndpointRequestSourceEndpoint = None,
        region_id: str = None,
        synchronization_job_id: str = None,
        synchronization_direction: str = None,
        owner_id: str = None,
        account_id: str = None,
    ):
        self.endpoint = endpoint
        self.source_endpoint = source_endpoint
        self.region_id = region_id
        self.synchronization_job_id = synchronization_job_id
        self.synchronization_direction = synchronization_direction
        self.owner_id = owner_id
        self.account_id = account_id

    def validate(self):
        if self.endpoint:
            self.endpoint.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint.to_map()
        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id
        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            temp_model = SwitchSynchronizationEndpointRequestEndpoint()
            self.endpoint = temp_model.from_map(m['Endpoint'])
        if m.get('SourceEndpoint') is not None:
            temp_model = SwitchSynchronizationEndpointRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m['SourceEndpoint'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')
        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        return self


class SwitchSynchronizationEndpointResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        task_id: str = None,
        success: str = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.task_id = task_id
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class SwitchSynchronizationEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SwitchSynchronizationEndpointResponseBody = None,
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
            temp_model = SwitchSynchronizationEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.resource_id = resource_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferInstanceClassRequest(TeaModel):
    def __init__(
        self,
        order_type: str = None,
        instance_class: str = None,
        region_id: str = None,
        dts_job_id: str = None,
    ):
        self.order_type = order_type
        self.instance_class = instance_class
        self.region_id = region_id
        self.dts_job_id = dts_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        return self


class TransferInstanceClassResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        http_status_code: int = None,
        request_id: str = None,
        dts_job_id: str = None,
        err_code: str = None,
        success: bool = None,
        charge_type: str = None,
        err_message: str = None,
        code: str = None,
        dynamic_message: str = None,
        instance_id: str = None,
    ):
        self.end_time = end_time
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.success = success
        self.charge_type = charge_type
        self.err_message = err_message
        self.code = code
        self.dynamic_message = dynamic_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class TransferInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferInstanceClassResponseBody = None,
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
            temp_model = TransferInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferPayTypeRequest(TeaModel):
    def __init__(
        self,
        dts_job_id: str = None,
        charge_type: str = None,
        period: str = None,
        buy_count: str = None,
        region_id: str = None,
    ):
        self.dts_job_id = dts_job_id
        self.charge_type = charge_type
        self.period = period
        self.buy_count = buy_count
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.period is not None:
            result['Period'] = self.period
        if self.buy_count is not None:
            result['BuyCount'] = self.buy_count
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('BuyCount') is not None:
            self.buy_count = m.get('BuyCount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class TransferPayTypeResponseBody(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        http_status_code: int = None,
        request_id: str = None,
        dts_job_id: str = None,
        err_code: str = None,
        success: bool = None,
        charge_type: str = None,
        err_message: str = None,
        code: str = None,
        dynamic_message: str = None,
        instance_id: str = None,
    ):
        self.end_time = end_time
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.dts_job_id = dts_job_id
        self.err_code = err_code
        self.success = success
        self.charge_type = charge_type
        self.err_message = err_message
        self.code = code
        self.dynamic_message = dynamic_message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class TransferPayTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferPayTypeResponseBody = None,
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
            temp_model = TransferPayTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
    ):
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeTwoWayRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_class: str = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.instance_class = instance_class
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpgradeTwoWayResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class UpgradeTwoWayResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeTwoWayResponseBody = None,
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
            temp_model = UpgradeTwoWayResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WhiteIpListRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        region: str = None,
        destination_region: str = None,
        region_id: str = None,
    ):
        self.type = type
        self.region = region
        self.destination_region = destination_region
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.region is not None:
            result['Region'] = self.region
        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class WhiteIpListResponseBody(TeaModel):
    def __init__(
        self,
        http_status_code: int = None,
        request_id: str = None,
        err_code: str = None,
        success: bool = None,
        err_message: str = None,
        ip_list: str = None,
        dynamic_message: str = None,
        dynamic_code: str = None,
    ):
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.err_code = err_code
        self.success = success
        self.err_message = err_message
        self.ip_list = ip_list
        self.dynamic_message = dynamic_message
        self.dynamic_code = dynamic_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.success is not None:
            result['Success'] = self.success
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        return self


class WhiteIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WhiteIpListResponseBody = None,
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
            temp_model = WhiteIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


