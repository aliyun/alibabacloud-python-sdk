# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ConfigureMigrationJobRequestDestinationEndpoint(TeaModel):
    def __init__(
        self,
        data_base_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        password: str = None,
        port: str = None,
        region: str = None,
        user_name: str = None,
    ):
        self.data_base_name = data_base_name
        self.engine_name = engine_name
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
        password: str = None,
        port: str = None,
        region: str = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.engine_name = engine_name
        self.ip = ip
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.oracle_sid = oracle_sid
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
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ConfigureMigrationJobRequest(TeaModel):
    def __init__(
        self,
        destination_endpoint: ConfigureMigrationJobRequestDestinationEndpoint = None,
        migration_mode: ConfigureMigrationJobRequestMigrationMode = None,
        source_endpoint: ConfigureMigrationJobRequestSourceEndpoint = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_object: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.migration_mode = migration_mode
        self.source_endpoint = source_endpoint
        self.migration_job_id = migration_job_id
        self.migration_job_name = migration_job_name
        self.migration_object = migration_object

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
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        if self.migration_job_name is not None:
            result['MigrationJobName'] = self.migration_job_name
        if self.migration_object is not None:
            result['MigrationObject'] = self.migration_object
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
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')
        return self


class ConfigureMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
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


class CreateMigrationJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        migration_job_class: str = None,
        region: str = None,
    ):
        self.client_token = client_token
        self.migration_job_class = migration_job_class
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
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class CreateMigrationJobResponseBody(TeaModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        migration_job_id: str = None,
        success: str = None,
    ):
        self.err_code = err_code
        self.err_message = err_message
        self.migration_job_id = migration_job_id
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


class CreateSynchronousJobRequest(TeaModel):
    def __init__(
        self,
        destination_instance_id: str = None,
        full_data_intialization: bool = None,
        source_instance_id: str = None,
        structure_intialization: bool = None,
        synchronous_job_name: str = None,
        synchronous_object_list: str = None,
        synchronous_speed_limit: str = None,
    ):
        self.destination_instance_id = destination_instance_id
        self.full_data_intialization = full_data_intialization
        self.source_instance_id = source_instance_id
        self.structure_intialization = structure_intialization
        self.synchronous_job_name = synchronous_job_name
        self.synchronous_object_list = synchronous_object_list
        self.synchronous_speed_limit = synchronous_speed_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_instance_id is not None:
            result['DestinationInstanceId'] = self.destination_instance_id
        if self.full_data_intialization is not None:
            result['FullDataIntialization'] = self.full_data_intialization
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.structure_intialization is not None:
            result['StructureIntialization'] = self.structure_intialization
        if self.synchronous_job_name is not None:
            result['SynchronousJobName'] = self.synchronous_job_name
        if self.synchronous_object_list is not None:
            result['SynchronousObjectList'] = self.synchronous_object_list
        if self.synchronous_speed_limit is not None:
            result['SynchronousSpeedLimit'] = self.synchronous_speed_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationInstanceId') is not None:
            self.destination_instance_id = m.get('DestinationInstanceId')
        if m.get('FullDataIntialization') is not None:
            self.full_data_intialization = m.get('FullDataIntialization')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('StructureIntialization') is not None:
            self.structure_intialization = m.get('StructureIntialization')
        if m.get('SynchronousJobName') is not None:
            self.synchronous_job_name = m.get('SynchronousJobName')
        if m.get('SynchronousObjectList') is not None:
            self.synchronous_object_list = m.get('SynchronousObjectList')
        if m.get('SynchronousSpeedLimit') is not None:
            self.synchronous_speed_limit = m.get('SynchronousSpeedLimit')
        return self


class CreateSynchronousJobResponseBody(TeaModel):
    def __init__(
        self,
        synchronous_job_id: str = None,
    ):
        self.synchronous_job_id = synchronous_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        return self


class CreateSynchronousJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSynchronousJobResponseBody = None,
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
            temp_model = CreateSynchronousJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMigrationJobRequest(TeaModel):
    def __init__(
        self,
        migration_job_id: str = None,
    ):
        self.migration_job_id = migration_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        return self


class DeleteMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteSynchronousJobRequest(TeaModel):
    def __init__(
        self,
        synchronous_job_id: str = None,
    ):
        self.synchronous_job_id = synchronous_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        return self


class DeleteSynchronousJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DescirbeMigrationJobsRequest(TeaModel):
    def __init__(
        self,
        migration_job_name: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        self.migration_job_name = migration_job_name
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
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')
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


class DescribeMigrationJobStatusRequest(TeaModel):
    def __init__(
        self,
        migration_job_id: str = None,
    ):
        self.migration_job_id = migration_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
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


class DescribeSynchronousJobConfigurationRequest(TeaModel):
    def __init__(
        self,
        synchronous_job_id: str = None,
    ):
        self.synchronous_job_id = synchronous_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        return self


class DescribeSynchronousJobConfigurationResponseBodySynchronousObjectListSynchronousObjectTableList(TeaModel):
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


class DescribeSynchronousJobConfigurationResponseBodySynchronousObjectListSynchronousObject(TeaModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: DescribeSynchronousJobConfigurationResponseBodySynchronousObjectListSynchronousObjectTableList = None,
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
            temp_model = DescribeSynchronousJobConfigurationResponseBodySynchronousObjectListSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m['TableList'])
        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')
        return self


class DescribeSynchronousJobConfigurationResponseBodySynchronousObjectList(TeaModel):
    def __init__(
        self,
        synchronous_object: List[DescribeSynchronousJobConfigurationResponseBodySynchronousObjectListSynchronousObject] = None,
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
                temp_model = DescribeSynchronousJobConfigurationResponseBodySynchronousObjectListSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k))
        return self


class DescribeSynchronousJobConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        destination_dbtype: str = None,
        destination_instance_id: str = None,
        full_data_intialization: str = None,
        source_dbtype: str = None,
        source_instance_id: str = None,
        structure_intialization: str = None,
        synchronous_job_id: str = None,
        synchronous_job_name: str = None,
        synchronous_object_list: DescribeSynchronousJobConfigurationResponseBodySynchronousObjectList = None,
        synchronous_speed_limit: str = None,
    ):
        self.create_time = create_time
        self.destination_dbtype = destination_dbtype
        self.destination_instance_id = destination_instance_id
        self.full_data_intialization = full_data_intialization
        self.source_dbtype = source_dbtype
        self.source_instance_id = source_instance_id
        self.structure_intialization = structure_intialization
        self.synchronous_job_id = synchronous_job_id
        self.synchronous_job_name = synchronous_job_name
        self.synchronous_object_list = synchronous_object_list
        self.synchronous_speed_limit = synchronous_speed_limit

    def validate(self):
        if self.synchronous_object_list:
            self.synchronous_object_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.destination_dbtype is not None:
            result['DestinationDBType'] = self.destination_dbtype
        if self.destination_instance_id is not None:
            result['DestinationInstanceId'] = self.destination_instance_id
        if self.full_data_intialization is not None:
            result['FullDataIntialization'] = self.full_data_intialization
        if self.source_dbtype is not None:
            result['SourceDBType'] = self.source_dbtype
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.structure_intialization is not None:
            result['StructureIntialization'] = self.structure_intialization
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        if self.synchronous_job_name is not None:
            result['SynchronousJobName'] = self.synchronous_job_name
        if self.synchronous_object_list is not None:
            result['SynchronousObjectList'] = self.synchronous_object_list.to_map()
        if self.synchronous_speed_limit is not None:
            result['SynchronousSpeedLimit'] = self.synchronous_speed_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DestinationDBType') is not None:
            self.destination_dbtype = m.get('DestinationDBType')
        if m.get('DestinationInstanceId') is not None:
            self.destination_instance_id = m.get('DestinationInstanceId')
        if m.get('FullDataIntialization') is not None:
            self.full_data_intialization = m.get('FullDataIntialization')
        if m.get('SourceDBType') is not None:
            self.source_dbtype = m.get('SourceDBType')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('StructureIntialization') is not None:
            self.structure_intialization = m.get('StructureIntialization')
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        if m.get('SynchronousJobName') is not None:
            self.synchronous_job_name = m.get('SynchronousJobName')
        if m.get('SynchronousObjectList') is not None:
            temp_model = DescribeSynchronousJobConfigurationResponseBodySynchronousObjectList()
            self.synchronous_object_list = temp_model.from_map(m['SynchronousObjectList'])
        if m.get('SynchronousSpeedLimit') is not None:
            self.synchronous_speed_limit = m.get('SynchronousSpeedLimit')
        return self


class DescribeSynchronousJobConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSynchronousJobConfigurationResponseBody = None,
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
            temp_model = DescribeSynchronousJobConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronousJobDetailsRequest(TeaModel):
    def __init__(
        self,
        synchronous_job_id: str = None,
    ):
        self.synchronous_job_id = synchronous_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        return self


class DescribeSynchronousJobDetailsResponseBodyPrecheckDetailsPrecheckDetail(TeaModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reson: str = None,
        repair_method: str = None,
    ):
        self.check_item = check_item
        self.check_item_description = check_item_description
        self.check_result = check_result
        self.failed_reson = failed_reson
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_item is not None:
            result['CheckItem'] = self.check_item
        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description
        if self.check_result is not None:
            result['CheckResult'] = self.check_result
        if self.failed_reson is not None:
            result['FailedReson'] = self.failed_reson
        if self.repair_method is not None:
            result['RepairMethod'] = self.repair_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')
        if m.get('CheckItemDescription') is not None:
            self.check_item_description = m.get('CheckItemDescription')
        if m.get('CheckResult') is not None:
            self.check_result = m.get('CheckResult')
        if m.get('FailedReson') is not None:
            self.failed_reson = m.get('FailedReson')
        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')
        return self


class DescribeSynchronousJobDetailsResponseBodyPrecheckDetails(TeaModel):
    def __init__(
        self,
        precheck_detail: List[DescribeSynchronousJobDetailsResponseBodyPrecheckDetailsPrecheckDetail] = None,
    ):
        self.precheck_detail = precheck_detail

    def validate(self):
        if self.precheck_detail:
            for k in self.precheck_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PrecheckDetail'] = []
        if self.precheck_detail is not None:
            for k in self.precheck_detail:
                result['PrecheckDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.precheck_detail = []
        if m.get('PrecheckDetail') is not None:
            for k in m.get('PrecheckDetail'):
                temp_model = DescribeSynchronousJobDetailsResponseBodyPrecheckDetailsPrecheckDetail()
                self.precheck_detail.append(temp_model.from_map(k))
        return self


class DescribeSynchronousJobDetailsResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        delay_second: str = None,
        destination_instance_id: str = None,
        error_message: str = None,
        full_data_intializatio_percent: str = None,
        full_data_intializatio_progress: str = None,
        full_data_intialization_status: str = None,
        increment_data_intializatio_delay: str = None,
        increment_data_intializatio_percent: str = None,
        increment_data_intialization_status: str = None,
        precheck_details: DescribeSynchronousJobDetailsResponseBodyPrecheckDetails = None,
        precheck_percent: str = None,
        precheck_status: str = None,
        source_instance_id: str = None,
        structure_intialization_percent: str = None,
        structure_intialization_progress: str = None,
        structure_intialization_status: str = None,
        synchronous_flow: str = None,
        synchronous_job_id: str = None,
        synchronous_job_name: str = None,
        synchronous_status: str = None,
        synchronous_tps: str = None,
    ):
        self.create_time = create_time
        self.delay_second = delay_second
        self.destination_instance_id = destination_instance_id
        self.error_message = error_message
        self.full_data_intializatio_percent = full_data_intializatio_percent
        self.full_data_intializatio_progress = full_data_intializatio_progress
        self.full_data_intialization_status = full_data_intialization_status
        self.increment_data_intializatio_delay = increment_data_intializatio_delay
        self.increment_data_intializatio_percent = increment_data_intializatio_percent
        self.increment_data_intialization_status = increment_data_intialization_status
        self.precheck_details = precheck_details
        self.precheck_percent = precheck_percent
        self.precheck_status = precheck_status
        self.source_instance_id = source_instance_id
        self.structure_intialization_percent = structure_intialization_percent
        self.structure_intialization_progress = structure_intialization_progress
        self.structure_intialization_status = structure_intialization_status
        self.synchronous_flow = synchronous_flow
        self.synchronous_job_id = synchronous_job_id
        self.synchronous_job_name = synchronous_job_name
        self.synchronous_status = synchronous_status
        self.synchronous_tps = synchronous_tps

    def validate(self):
        if self.precheck_details:
            self.precheck_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_second is not None:
            result['DelaySecond'] = self.delay_second
        if self.destination_instance_id is not None:
            result['DestinationInstanceId'] = self.destination_instance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.full_data_intializatio_percent is not None:
            result['FullDataIntializatioPercent'] = self.full_data_intializatio_percent
        if self.full_data_intializatio_progress is not None:
            result['FullDataIntializatioProgress'] = self.full_data_intializatio_progress
        if self.full_data_intialization_status is not None:
            result['FullDataIntializationStatus'] = self.full_data_intialization_status
        if self.increment_data_intializatio_delay is not None:
            result['IncrementDataIntializatioDelay'] = self.increment_data_intializatio_delay
        if self.increment_data_intializatio_percent is not None:
            result['IncrementDataIntializatioPercent'] = self.increment_data_intializatio_percent
        if self.increment_data_intialization_status is not None:
            result['IncrementDataIntializationStatus'] = self.increment_data_intialization_status
        if self.precheck_details is not None:
            result['PrecheckDetails'] = self.precheck_details.to_map()
        if self.precheck_percent is not None:
            result['PrecheckPercent'] = self.precheck_percent
        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.structure_intialization_percent is not None:
            result['StructureIntializationPercent'] = self.structure_intialization_percent
        if self.structure_intialization_progress is not None:
            result['StructureIntializationProgress'] = self.structure_intialization_progress
        if self.structure_intialization_status is not None:
            result['StructureIntializationStatus'] = self.structure_intialization_status
        if self.synchronous_flow is not None:
            result['SynchronousFlow'] = self.synchronous_flow
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        if self.synchronous_job_name is not None:
            result['SynchronousJobName'] = self.synchronous_job_name
        if self.synchronous_status is not None:
            result['SynchronousStatus'] = self.synchronous_status
        if self.synchronous_tps is not None:
            result['SynchronousTPS'] = self.synchronous_tps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelaySecond') is not None:
            self.delay_second = m.get('DelaySecond')
        if m.get('DestinationInstanceId') is not None:
            self.destination_instance_id = m.get('DestinationInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FullDataIntializatioPercent') is not None:
            self.full_data_intializatio_percent = m.get('FullDataIntializatioPercent')
        if m.get('FullDataIntializatioProgress') is not None:
            self.full_data_intializatio_progress = m.get('FullDataIntializatioProgress')
        if m.get('FullDataIntializationStatus') is not None:
            self.full_data_intialization_status = m.get('FullDataIntializationStatus')
        if m.get('IncrementDataIntializatioDelay') is not None:
            self.increment_data_intializatio_delay = m.get('IncrementDataIntializatioDelay')
        if m.get('IncrementDataIntializatioPercent') is not None:
            self.increment_data_intializatio_percent = m.get('IncrementDataIntializatioPercent')
        if m.get('IncrementDataIntializationStatus') is not None:
            self.increment_data_intialization_status = m.get('IncrementDataIntializationStatus')
        if m.get('PrecheckDetails') is not None:
            temp_model = DescribeSynchronousJobDetailsResponseBodyPrecheckDetails()
            self.precheck_details = temp_model.from_map(m['PrecheckDetails'])
        if m.get('PrecheckPercent') is not None:
            self.precheck_percent = m.get('PrecheckPercent')
        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('StructureIntializationPercent') is not None:
            self.structure_intialization_percent = m.get('StructureIntializationPercent')
        if m.get('StructureIntializationProgress') is not None:
            self.structure_intialization_progress = m.get('StructureIntializationProgress')
        if m.get('StructureIntializationStatus') is not None:
            self.structure_intialization_status = m.get('StructureIntializationStatus')
        if m.get('SynchronousFlow') is not None:
            self.synchronous_flow = m.get('SynchronousFlow')
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        if m.get('SynchronousJobName') is not None:
            self.synchronous_job_name = m.get('SynchronousJobName')
        if m.get('SynchronousStatus') is not None:
            self.synchronous_status = m.get('SynchronousStatus')
        if m.get('SynchronousTPS') is not None:
            self.synchronous_tps = m.get('SynchronousTPS')
        return self


class DescribeSynchronousJobDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSynchronousJobDetailsResponseBody = None,
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
            temp_model = DescribeSynchronousJobDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSynchronousJobListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_num: int = None,
        page_size: int = None,
        synchronous_job_name: str = None,
    ):
        self.instance_id = instance_id
        self.page_num = page_num
        self.page_size = page_size
        self.synchronous_job_name = synchronous_job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.synchronous_job_name is not None:
            result['SynchronousJobName'] = self.synchronous_job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SynchronousJobName') is not None:
            self.synchronous_job_name = m.get('SynchronousJobName')
        return self


class DescribeSynchronousJobListResponseBodySynchronousJobListSynchronousJob(TeaModel):
    def __init__(
        self,
        delay_second: str = None,
        destination_instance_id: str = None,
        error_message: str = None,
        full_data_intializatio_percent: str = None,
        full_data_intializatio_progress: str = None,
        full_data_intialization_status: str = None,
        increment_data_intializatio_delay: str = None,
        increment_data_intializatio_percent: str = None,
        increment_data_intialization_status: str = None,
        source_instance_id: str = None,
        structure_intialization_percent: str = None,
        structure_intialization_progress: str = None,
        structure_intialization_status: str = None,
        synchronous_flow: str = None,
        synchronous_job_id: str = None,
        synchronous_job_name: str = None,
        synchronous_status: str = None,
        synchronous_tps: str = None,
    ):
        self.delay_second = delay_second
        self.destination_instance_id = destination_instance_id
        self.error_message = error_message
        self.full_data_intializatio_percent = full_data_intializatio_percent
        self.full_data_intializatio_progress = full_data_intializatio_progress
        self.full_data_intialization_status = full_data_intialization_status
        self.increment_data_intializatio_delay = increment_data_intializatio_delay
        self.increment_data_intializatio_percent = increment_data_intializatio_percent
        self.increment_data_intialization_status = increment_data_intialization_status
        self.source_instance_id = source_instance_id
        self.structure_intialization_percent = structure_intialization_percent
        self.structure_intialization_progress = structure_intialization_progress
        self.structure_intialization_status = structure_intialization_status
        self.synchronous_flow = synchronous_flow
        self.synchronous_job_id = synchronous_job_id
        self.synchronous_job_name = synchronous_job_name
        self.synchronous_status = synchronous_status
        self.synchronous_tps = synchronous_tps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delay_second is not None:
            result['DelaySecond'] = self.delay_second
        if self.destination_instance_id is not None:
            result['DestinationInstanceId'] = self.destination_instance_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.full_data_intializatio_percent is not None:
            result['FullDataIntializatioPercent'] = self.full_data_intializatio_percent
        if self.full_data_intializatio_progress is not None:
            result['FullDataIntializatioProgress'] = self.full_data_intializatio_progress
        if self.full_data_intialization_status is not None:
            result['FullDataIntializationStatus'] = self.full_data_intialization_status
        if self.increment_data_intializatio_delay is not None:
            result['IncrementDataIntializatioDelay'] = self.increment_data_intializatio_delay
        if self.increment_data_intializatio_percent is not None:
            result['IncrementDataIntializatioPercent'] = self.increment_data_intializatio_percent
        if self.increment_data_intialization_status is not None:
            result['IncrementDataIntializationStatus'] = self.increment_data_intialization_status
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.structure_intialization_percent is not None:
            result['StructureIntializationPercent'] = self.structure_intialization_percent
        if self.structure_intialization_progress is not None:
            result['StructureIntializationProgress'] = self.structure_intialization_progress
        if self.structure_intialization_status is not None:
            result['StructureIntializationStatus'] = self.structure_intialization_status
        if self.synchronous_flow is not None:
            result['SynchronousFlow'] = self.synchronous_flow
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        if self.synchronous_job_name is not None:
            result['SynchronousJobName'] = self.synchronous_job_name
        if self.synchronous_status is not None:
            result['SynchronousStatus'] = self.synchronous_status
        if self.synchronous_tps is not None:
            result['SynchronousTPS'] = self.synchronous_tps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelaySecond') is not None:
            self.delay_second = m.get('DelaySecond')
        if m.get('DestinationInstanceId') is not None:
            self.destination_instance_id = m.get('DestinationInstanceId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FullDataIntializatioPercent') is not None:
            self.full_data_intializatio_percent = m.get('FullDataIntializatioPercent')
        if m.get('FullDataIntializatioProgress') is not None:
            self.full_data_intializatio_progress = m.get('FullDataIntializatioProgress')
        if m.get('FullDataIntializationStatus') is not None:
            self.full_data_intialization_status = m.get('FullDataIntializationStatus')
        if m.get('IncrementDataIntializatioDelay') is not None:
            self.increment_data_intializatio_delay = m.get('IncrementDataIntializatioDelay')
        if m.get('IncrementDataIntializatioPercent') is not None:
            self.increment_data_intializatio_percent = m.get('IncrementDataIntializatioPercent')
        if m.get('IncrementDataIntializationStatus') is not None:
            self.increment_data_intialization_status = m.get('IncrementDataIntializationStatus')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('StructureIntializationPercent') is not None:
            self.structure_intialization_percent = m.get('StructureIntializationPercent')
        if m.get('StructureIntializationProgress') is not None:
            self.structure_intialization_progress = m.get('StructureIntializationProgress')
        if m.get('StructureIntializationStatus') is not None:
            self.structure_intialization_status = m.get('StructureIntializationStatus')
        if m.get('SynchronousFlow') is not None:
            self.synchronous_flow = m.get('SynchronousFlow')
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        if m.get('SynchronousJobName') is not None:
            self.synchronous_job_name = m.get('SynchronousJobName')
        if m.get('SynchronousStatus') is not None:
            self.synchronous_status = m.get('SynchronousStatus')
        if m.get('SynchronousTPS') is not None:
            self.synchronous_tps = m.get('SynchronousTPS')
        return self


class DescribeSynchronousJobListResponseBodySynchronousJobList(TeaModel):
    def __init__(
        self,
        synchronous_job: List[DescribeSynchronousJobListResponseBodySynchronousJobListSynchronousJob] = None,
    ):
        self.synchronous_job = synchronous_job

    def validate(self):
        if self.synchronous_job:
            for k in self.synchronous_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SynchronousJob'] = []
        if self.synchronous_job is not None:
            for k in self.synchronous_job:
                result['SynchronousJob'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_job = []
        if m.get('SynchronousJob') is not None:
            for k in m.get('SynchronousJob'):
                temp_model = DescribeSynchronousJobListResponseBodySynchronousJobListSynchronousJob()
                self.synchronous_job.append(temp_model.from_map(k))
        return self


class DescribeSynchronousJobListResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_record_count: int = None,
        synchronous_job_list: DescribeSynchronousJobListResponseBodySynchronousJobList = None,
        total_record_count: int = None,
    ):
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.synchronous_job_list = synchronous_job_list
        self.total_record_count = total_record_count

    def validate(self):
        if self.synchronous_job_list:
            self.synchronous_job_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.synchronous_job_list is not None:
            result['SynchronousJobList'] = self.synchronous_job_list.to_map()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('SynchronousJobList') is not None:
            temp_model = DescribeSynchronousJobListResponseBodySynchronousJobList()
            self.synchronous_job_list = temp_model.from_map(m['SynchronousJobList'])
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        return self


class DescribeSynchronousJobListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSynchronousJobListResponseBody = None,
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
            temp_model = DescribeSynchronousJobListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMigrationJobRequest(TeaModel):
    def __init__(
        self,
        migration_job_id: str = None,
    ):
        self.migration_job_id = migration_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        return self


class StartMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StartSynchronousJobRequest(TeaModel):
    def __init__(
        self,
        synchronous_job_id: str = None,
    ):
        self.synchronous_job_id = synchronous_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        return self


class StartSynchronousJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class StopMigrationJobRequest(TeaModel):
    def __init__(
        self,
        migration_job_id: str = None,
    ):
        self.migration_job_id = migration_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        return self


class StopMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class SuspendMigrationJobRequest(TeaModel):
    def __init__(
        self,
        migration_job_id: str = None,
    ):
        self.migration_job_id = migration_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')
        return self


class SuspendMigrationJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class SuspendSynchronousJobRequest(TeaModel):
    def __init__(
        self,
        synchronous_job_id: str = None,
    ):
        self.synchronous_job_id = synchronous_job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.synchronous_job_id is not None:
            result['SynchronousJobId'] = self.synchronous_job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SynchronousJobId') is not None:
            self.synchronous_job_id = m.get('SynchronousJobId')
        return self


class SuspendSynchronousJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


