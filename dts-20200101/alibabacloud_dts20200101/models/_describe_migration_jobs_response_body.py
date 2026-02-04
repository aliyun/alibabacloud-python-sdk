# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeMigrationJobsResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        migration_jobs: main_models.DescribeMigrationJobsResponseBodyMigrationJobs = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The list of data migration instances and the details of each instance.
        self.migration_jobs = migration_jobs
        # The page number of the returned page.
        self.page_number = page_number
        # The maximum number of entries that can be displayed on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success
        # The total number of data migration instances that belong to your Alibaba Cloud account.
        self.total_record_count = total_record_count

    def validate(self):
        if self.migration_jobs:
            self.migration_jobs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.migration_jobs is not None:
            result['MigrationJobs'] = self.migration_jobs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('MigrationJobs') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobs()
            self.migration_jobs = temp_model.from_map(m.get('MigrationJobs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeMigrationJobsResponseBodyMigrationJobs(DaraModel):
    def __init__(
        self,
        migration_job: List[main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob] = None,
    ):
        self.migration_job = migration_job

    def validate(self):
        if self.migration_job:
            for v1 in self.migration_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MigrationJob'] = []
        if self.migration_job is not None:
            for k1 in self.migration_job:
                result['MigrationJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.migration_job = []
        if m.get('MigrationJob') is not None:
            for k1 in m.get('MigrationJob'):
                temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob()
                self.migration_job.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJob(DaraModel):
    def __init__(
        self,
        data_initialization: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization = None,
        data_synchronization: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization = None,
        destination_endpoint: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint = None,
        instance_create_time: str = None,
        job_create_time: str = None,
        migration_job_class: str = None,
        migration_job_id: str = None,
        migration_job_name: str = None,
        migration_job_status: str = None,
        migration_mode: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode = None,
        migration_object: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject = None,
        pay_type: str = None,
        precheck: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck = None,
        source_endpoint: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint = None,
        structure_initialization: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization = None,
        tags: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags = None,
    ):
        # The details of full data migration.
        self.data_initialization = data_initialization
        # The details of incremental data migration.
        self.data_synchronization = data_synchronization
        # The connection settings of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The time when the data migration instance was created. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.instance_create_time = instance_create_time
        # The time when the data migration task was created. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.job_create_time = job_create_time
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
        self.precheck = precheck
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The details of schema migration.
        self.structure_initialization = structure_initialization
        # The collection of tags.
        self.tags = tags

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
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_initialization is not None:
            result['DataInitialization'] = self.data_initialization.to_map()

        if self.data_synchronization is not None:
            result['DataSynchronization'] = self.data_synchronization.to_map()

        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time

        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time

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

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization()
            self.data_initialization = temp_model.from_map(m.get('DataInitialization'))

        if m.get('DataSynchronization') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization()
            self.data_synchronization = temp_model.from_map(m.get('DataSynchronization'))

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')

        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')

        if m.get('MigrationJobClass') is not None:
            self.migration_job_class = m.get('MigrationJobClass')

        if m.get('MigrationJobID') is not None:
            self.migration_job_id = m.get('MigrationJobID')

        if m.get('MigrationJobName') is not None:
            self.migration_job_name = m.get('MigrationJobName')

        if m.get('MigrationJobStatus') is not None:
            self.migration_job_status = m.get('MigrationJobStatus')

        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('MigrationObject') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject()
            self.migration_object = temp_model.from_map(m.get('MigrationObject'))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Precheck') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck()
            self.precheck = temp_model.from_map(m.get('Precheck'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('StructureInitialization') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization()
            self.structure_initialization = temp_model.from_map(m.get('StructureInitialization'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value that corresponds to the tag key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobStructureInitialization(DaraModel):
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

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobSourceEndpoint(DaraModel):
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
        # The name of the database to which the migration object in the source instance belongs.
        self.database_name = database_name
        # The database type of the source instance.
        self.engine_name = engine_name
        # The endpoint of the source instance.
        self.ip = ip
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
        # This parameter is returned only if the database type of the source instance is **Oracle**.
        self.oracle_sid = oracle_sid
        # The database service port of the source instance.
        self.port = port
        # The database account of the source instance.
        self.user_name = user_name

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

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobPrecheck(DaraModel):
    def __init__(
        self,
        percent: str = None,
        status: str = None,
    ):
        # The precheck progress. Unit: %.
        self.percent = percent
        # The precheck result. Valid values:
        # 
        # *   **Success**: The task passed the precheck.
        # *   **Failed**: The task failed to pass the precheck.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObject(DaraModel):
    def __init__(
        self,
        synchronous_object: List[main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for v1 in self.synchronous_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k1 in self.synchronous_object:
                result['SynchronousObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k1 in m.get('SynchronousObject'):
                temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k1))

        return self

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObject(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        # The name of the database to which the migration object in the source instance belongs.
        self.database_name = database_name
        # The names of the migrated tables.
        self.table_list = table_list
        # Indicates whether an entire database is migrated. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m.get('TableList'))

        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')

        return self

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationObjectSynchronousObjectTableList(DaraModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobMigrationMode(DaraModel):
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

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDestinationEndpoint(DaraModel):
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
        # This parameter is returned only if the database type of the destination instance is **Oracle**.
        self.oracle_sid = oracle_sid
        # The database service port of the destination instance.
        self.port = port
        # The database account of the destination instance.
        self.user_name = user_name

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

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataSynchronization(DaraModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
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

class DescribeMigrationJobsResponseBodyMigrationJobsMigrationJobDataInitialization(DaraModel):
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

