# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSynchronizationJobsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        synchronization_instances: List[main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstances] = None,
        total_record_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The maximum number of records that can be displayed on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The list of data synchronization instances and the details of each instance.
        self.synchronization_instances = synchronization_instances
        # The total number of data synchronization instances that meet the specified conditions under the Alibaba Cloud account.
        self.total_record_count = total_record_count

    def validate(self):
        if self.synchronization_instances:
            for v1 in self.synchronization_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SynchronizationInstances'] = []
        if self.synchronization_instances is not None:
            for k1 in self.synchronization_instances:
                result['SynchronizationInstances'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('SynchronizationInstances'):
                temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstances()
                self.synchronization_instances.append(temp_model.from_map(k1))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstances(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_initialization: str = None,
        data_initialization_status: main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus = None,
        delay: str = None,
        destination_endpoint: main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint = None,
        error_message: str = None,
        expire_time: str = None,
        instance_create_time: str = None,
        job_create_time: str = None,
        pay_type: str = None,
        performance: main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance = None,
        precheck_status: main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus = None,
        source_endpoint: main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint = None,
        status: str = None,
        structure_initialization: str = None,
        structure_initialization_status: main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus = None,
        synchronization_direction: str = None,
        synchronization_job_class: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: List[main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects] = None,
        tags: List[main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags] = None,
    ):
        # The time when the synchronization task was created, in the format of <i>yyyy-MM-dd HH:mm:ss</i>.0 (UTC+8).
        self.create_time = create_time
        # Indicates whether initial full data synchronization is performed. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.data_initialization = data_initialization
        # The status of initial full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The status of incremental data synchronization.
        # > This parameter set and its contained parameters have been discontinued.
        self.data_synchronization_status = data_synchronization_status
        # The synchronization latency, in seconds.
        self.delay = delay
        # The connection information of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The error message returned when data synchronization fails.
        self.error_message = error_message
        # The expiration time of the synchronization instance, in the format of <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        # > This parameter is returned only when the value of the **PayType** parameter is **PrePaid**.
        self.expire_time = expire_time
        # The time when the synchronization instance was created, in the format of <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.instance_create_time = instance_create_time
        # The time when the synchronization task was created, in the format of <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z (UTC).
        self.job_create_time = job_create_time
        # The billing method of the synchronization instance. Valid values:
        # - **PrePaid**: subscription.
        # - **PostPaid**: pay-as-you-go.
        self.pay_type = pay_type
        # The overview information of the synchronization link.
        self.performance = performance
        # The precheck status.
        self.precheck_status = precheck_status
        # The connection information of the source instance.
        self.source_endpoint = source_endpoint
        # The status of the synchronization instance. Valid values:
        # - **NotStarted**: not started.
        # - **Prechecking**: running the precheck.
        # - **PrecheckFailed**: precheck failed.
        # - **Initializating**: performing initial synchronization.
        # - **InitializeFailed**: initial synchronization failed.
        # - **Synchronizing**: synchronizing.
        # - **Failed**: synchronization failed.
        # - **Suspending**: paused.
        # - **Modifying**: modifying synchronization objects.
        # - **Finished**: completed.
        self.status = status
        # Indicates whether initial schema synchronization is performed. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.structure_initialization = structure_initialization
        # The status of initial schema synchronization.
        self.structure_initialization_status = structure_initialization_status
        # The synchronization direction. Valid values:
        # - **Forward**: forward.
        # - **Reverse**: reverse.
        self.synchronization_direction = synchronization_direction
        # The specification of the synchronization link.
        self.synchronization_job_class = synchronization_job_class
        # The instance ID of the data synchronization instance.
        self.synchronization_job_id = synchronization_job_id
        # The name of the synchronization instance.
        self.synchronization_job_name = synchronization_job_name
        # The synchronization objects.
        self.synchronization_objects = synchronization_objects
        # The tag collection.
        self.tags = tags

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
            for v1 in self.synchronization_objects:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time

        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time

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

        if self.synchronization_direction is not None:
            result['SynchronizationDirection'] = self.synchronization_direction

        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class

        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id

        if self.synchronization_job_name is not None:
            result['SynchronizationJobName'] = self.synchronization_job_name

        result['SynchronizationObjects'] = []
        if self.synchronization_objects is not None:
            for k1 in self.synchronization_objects:
                result['SynchronizationObjects'].append(k1.to_map() if k1 else None)

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')

        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        if m.get('SynchronizationDirection') is not None:
            self.synchronization_direction = m.get('SynchronizationDirection')

        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')

        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')

        if m.get('SynchronizationJobName') is not None:
            self.synchronization_job_name = m.get('SynchronizationJobName')

        self.synchronization_objects = []
        if m.get('SynchronizationObjects') is not None:
            for k1 in m.get('SynchronizationObjects'):
                temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k1))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesTags(DaraModel):
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

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjects(DaraModel):
    def __init__(
        self,
        new_schema_name: str = None,
        schema_name: str = None,
        table_excludes: List[main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes] = None,
        table_includes: List[main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes] = None,
    ):
        # The name of the database to which the objects are mapped in the destination database.
        self.new_schema_name = new_schema_name
        # The name of the database to be synchronized.
        self.schema_name = schema_name
        # The tables that are excluded from the database to be synchronized. These tables are not synchronized.
        self.table_excludes = table_excludes
        # The tables to be synchronized.
        self.table_includes = table_includes

    def validate(self):
        if self.table_excludes:
            for v1 in self.table_excludes:
                 if v1:
                    v1.validate()
        if self.table_includes:
            for v1 in self.table_includes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        result['TableExcludes'] = []
        if self.table_excludes is not None:
            for k1 in self.table_excludes:
                result['TableExcludes'].append(k1.to_map() if k1 else None)

        result['TableIncludes'] = []
        if self.table_includes is not None:
            for k1 in self.table_includes:
                result['TableIncludes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        self.table_excludes = []
        if m.get('TableExcludes') is not None:
            for k1 in m.get('TableExcludes'):
                temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k1))

        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k1 in m.get('TableIncludes'):
                temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k1))

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableIncludes(DaraModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        # The name of the table to be synchronized.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSynchronizationObjectsTableExcludes(DaraModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        # The name of the excluded table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned when initial schema synchronization fails.
        self.error_message = error_message
        # The progress of initial schema synchronization, in percentage.
        self.percent = percent
        # The number of tables for which initial schema synchronization has been completed.
        self.progress = progress
        # The status of initial schema synchronization. Valid values:
        # - **NotStarted**: not started.
        # - **Migrating**: in progress.
        # - **Failed**: failed.
        # - **Finished**: completed.
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

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesSourceEndpoint(DaraModel):
    def __init__(
        self,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
    ):
        # The database type of the source instance.
        self.engine_name = engine_name
        # The endpoint of the source instance.
        self.ip = ip
        # The instance ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        # The execution details of each precheck item.
        self.detail = detail
        # The overall progress of the precheck, in percentage.
        self.percent = percent
        # The precheck result. Valid values:
        # - **Success**: passed.
        # - **Failed**: failed.
        self.status = status

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_status: str = None,
        error_message: str = None,
        item_name: str = None,
        repair_method: str = None,
    ):
        # The check result. Valid values:
        # - **Success**: passed.
        # - **Failed**: failed.
        self.check_status = check_status
        # The error message returned when the precheck fails.
        # > This parameter is returned only when the value of the **CheckStatus** parameter is **Failed**.
        self.error_message = error_message
        # The precheck item.
        self.item_name = item_name
        # The repair method when the precheck fails.
        # > This parameter is returned only when the value of the **CheckStatus** parameter is **Failed**.
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

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The volume of data synchronized per second, in MB/s.
        self.flow = flow
        # The number of SQL statements synchronized per second, including BEGIN, COMMIT, DML statements (INSERT, DELETE, and UPDATE), and DDL statements.
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDestinationEndpoint(DaraModel):
    def __init__(
        self,
        engine_name: str = None,
        ip: str = None,
        instance_id: str = None,
        instance_type: str = None,
        port: str = None,
        user_name: str = None,
    ):
        # The database type of the destination instance.
        self.engine_name = engine_name
        # The endpoint of the destination instance.
        self.ip = ip
        # The instance ID of the destination instance.
        self.instance_id = instance_id
        # The type of the destination instance.
        self.instance_type = instance_type
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        delay: str = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The synchronization latency of incremental data synchronization.
        # > This parameter has been discontinued.
        self.delay = delay
        # The error message returned when incremental data synchronization fails.
        # > This parameter has been discontinued.
        self.error_message = error_message
        # The progress of incremental data synchronization.
        # > This parameter has been discontinued.
        self.percent = percent
        # The status of incremental data synchronization.
        # > This parameter has been discontinued.
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

class DescribeSynchronizationJobsResponseBodySynchronizationInstancesDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned when initial full data synchronization fails.
        self.error_message = error_message
        # The progress of initial full data synchronization, in percentage.
        self.percent = percent
        # The number of records that have been synchronized during initial full data synchronization.
        self.progress = progress
        # The status of initial full data synchronization. Valid values:
        # - **NotStarted**: not started.
        # - **Migrating**: in progress.
        # - **Failed**: failed.
        # - **Finished**: completed.
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

