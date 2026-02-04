# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeMigrationJobStatusResponseBody(DaraModel):
    def __init__(
        self,
        data_initialization_status: main_models.DescribeMigrationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus = None,
        destination_endpoint: main_models.DescribeMigrationJobStatusResponseBodyDestinationEndpoint = None,
        err_code: str = None,
        err_message: str = None,
        migration_job_class: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        migration_mode: main_models.DescribeMigrationJobStatusResponseBodyMigrationMode = None,
        migration_object: str = None,
        pay_type: str = None,
        precheck_status: main_models.DescribeMigrationJobStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        source_endpoint: main_models.DescribeMigrationJobStatusResponseBodySourceEndpoint = None,
        structure_initialization_status: main_models.DescribeMigrationJobStatusResponseBodyStructureInitializationStatus = None,
        success: str = None,
        task_id: str = None,
    ):
        # The status of full data migration.
        self.data_initialization_status = data_initialization_status
        # The status of incremental data migration.
        self.data_synchronization_status = data_synchronization_status
        # The connection settings of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The specification of the data migration instance. Valid values: **small**, **medium**, **large**, **xlarge**, and **2xlarge**. For more information, see [Specifications of data migration instances](https://help.aliyun.com/document_detail/26606.html).
        self.migration_job_class = migration_job_class
        # The ID of the data migration instance.
        self.migration_job_id = migration_job_id
        # The name of the data migration task.
        self.migration_job_name = migration_job_name
        # The status of the data migration task. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **Migrating**: The task is migrating data.
        # *   **Suspending**: The task is paused.
        # *   **MigrationFailed**: The task failed to migrate data.
        # *   **Finished**: The task is completed.
        self.migration_job_status = migration_job_status
        # The migration types.
        self.migration_mode = migration_mode
        # The objects that are migrated by the task.
        self.migration_object = migration_object
        # The billing method of the data migration instance. The value is **PostPaid** (pay-as-you-go).
        self.pay_type = pay_type
        # The precheck details.
        self.precheck_status = precheck_status
        # The ID of the request.
        self.request_id = request_id
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The status of schema migration.
        self.structure_initialization_status = structure_initialization_status
        # Indicates whether the call was successful.
        self.success = success
        self.task_id = task_id

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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()

        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()

        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeMigrationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeMigrationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')

        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')

        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')

        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')

        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeMigrationJobStatusResponseBodyMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('MigrationObject') is not None:
            self.migration_object = m.get('MigrationObject')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeMigrationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeMigrationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeMigrationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeMigrationJobStatusResponseBodyStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if schema migration failed.
        self.error_message = error_message
        # The progress of schema migration. Unit: %.
        self.percent = percent
        # The number of tables whose schemas have been migrated.
        self.progress = progress
        # The status of schema migration. Valid values:
        # 
        # *   **NotStarted**: Schema migration is not started.
        # *   **Migrating**: Schema migration is in progress.
        # *   **Failed**: Schema migration failed.
        # *   **Finished**: Schema migration is completed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobStatusResponseBodySourceEndpoint(DaraModel):
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
        # The name of the database to which the migration object in the source instance belongs.
        self.database_name = database_name
        # The database type of the source instance.
        self.engine_name = engine_name
        # The endpoint of the source instance.
        self.ip = ip
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        # 
        # *   **RDS**: ApsaraDB RDS instance
        # *   **ECS**: self-managed database that is hosted on Elastic Compute Service (ECS)
        # *   **LocalInstance**: self-managed database with a public IP address
        # *   **Express**: self-managed database that is connected over Express Connect, VPN Gateway, or Smart Access Gateway
        # *   **MongoDB**: ApsaraDB for MongoDB instance
        # *   **POLARDB**: PolarDB for MySQL cluster (available only for the China site)
        self.instance_type = instance_type
        # The database service port of the source instance.
        self.port = port
        # The database account of the source instance.
        self.user_name = user_name
        # The SID of the Oracle database.
        # 
        # >  This parameter is returned only if the database type of the source instance is **Oracle**.
        self.oracle_sid = oracle_sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobStatusResponseBodyPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: main_models.DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail = None,
        percent: str = None,
        status: str = None,
    ):
        # The result of each precheck item.
        self.detail = detail
        # The precheck progress. Unit: %.
        self.percent = percent
        # The precheck status. Valid values:
        # 
        # *   **NotStarted**
        # *   **Suspending**:
        # *   **Checking**
        # *   **Failed**
        # *   **Finished**
        self.status = status

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeMigrationJobStatusResponseBodyPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_item: List[main_models.DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem] = None,
    ):
        self.check_item = check_item

    def validate(self):
        if self.check_item:
            for v1 in self.check_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckItem'] = []
        if self.check_item is not None:
            for k1 in self.check_item:
                result['CheckItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_item = []
        if m.get('CheckItem') is not None:
            for k1 in m.get('CheckItem'):
                temp_model = main_models.DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem()
                self.check_item.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobStatusResponseBodyPrecheckStatusDetailCheckItem(DaraModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        # The precheck result. Valid values:
        # 
        # *   **Success**: The task passed the precheck.
        # *   **Failed**: The task failed to pass the precheck.
        self.check_status = check_status
        # The error message returned if the task failed to pass the precheck.
        # 
        # >  This parameter is returned only if the return value of the **CheckStatus** parameter is **Failed**.
        self.error_message = error_message
        # The name of the precheck item.
        self.item_name = item_name
        # The method to fix the precheck failure.
        # 
        # >  This parameter is returned only if the return value of the **CheckStatus** parameter is **Failed**.
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobStatusResponseBodyMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        # Indicates whether full data migration is performed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.data_initialization = data_initialization
        # Indicates whether incremental data migration is performed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.data_synchronization = data_synchronization
        # Indicates whether schema migration is performed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.structure_initialization = structure_initialization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobStatusResponseBodyDestinationEndpoint(DaraModel):
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
        # The name of the database to which the migration object in the destination instance belongs.
        self.database_name = database_name
        # The database type of the destination instance.
        self.engine_name = engine_name
        # The endpoint of the destination instance.
        self.ip = ip
        # The ID of the destination instance.
        self.instance_id = instance_id
        # The type of the destination instance.
        self.instance_type = instance_type
        # The database service port of the destination instance.
        self.port = port
        # The database account of the destination instance.
        self.user_name = user_name
        # The system ID (SID) of the Oracle database.
        # 
        # >  This parameter is returned only if the database type of the destination instance is **Oracle**.
        self.oracle_sid = oracle_sid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobStatusResponseBodyDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The UNIX timestamp generated when the latest incremental data is migrated. Unit: seconds.
        self.checkpoint = checkpoint
        # The latency of incremental data migration. Unit: seconds.
        self.delay = delay
        # The error message returned if incremental data migration failed.
        self.error_message = error_message
        # The progress of incremental data migration. Unit: %.
        self.percent = percent
        # The status of incremental data migration. Valid values:
        # 
        # *   **NotStarted**: Incremental data migration is not started.
        # *   **Migrating**: Incremental data migration is in progress.
        # *   **Failed**: Incremental data migration failed.
        # *   **Finished**: Incremental data migration is completed.
        # *   **Catched**: Incremental data migration is not delayed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobStatusResponseBodyDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if full data migration failed.
        self.error_message = error_message
        # The migration progress. Unit: %.
        self.percent = percent
        # The number of records that have been migrated during full data migration.
        self.progress = progress
        # The status of full data migration. Valid values:
        # 
        # *   **NotStarted**: Full data migration is not started.
        # *   **Migrating**: Full data migration is in progress.
        # *   **Failed**: Full data migration failed.
        # *   **Finished**: Full data migration is completed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

