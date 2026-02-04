# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSynchronizationJobStatusResponseBody(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        data_initialization: str = None,
        data_initialization_status: main_models.DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus = None,
        delay: str = None,
        delay_millis: int = None,
        destination_endpoint: main_models.DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint = None,
        err_code: str = None,
        err_message: str = None,
        error_message: str = None,
        expire_time: str = None,
        pay_type: str = None,
        performance: main_models.DescribeSynchronizationJobStatusResponseBodyPerformance = None,
        precheck_status: main_models.DescribeSynchronizationJobStatusResponseBodyPrecheckStatus = None,
        request_id: str = None,
        source_endpoint: main_models.DescribeSynchronizationJobStatusResponseBodySourceEndpoint = None,
        status: str = None,
        structure_initialization: str = None,
        structure_initialization_status: main_models.DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus = None,
        success: str = None,
        synchronization_direction: str = None,
        synchronization_job_class: str = None,
        synchronization_job_id: str = None,
        synchronization_job_name: str = None,
        synchronization_objects: List[main_models.DescribeSynchronizationJobStatusResponseBodySynchronizationObjects] = None,
        task_id: str = None,
    ):
        # The UNIX timestamp generated when the latest data record was synchronized.
        # 
        # >  You can use a search engine to obtain a UNIX timestamp converter.
        self.checkpoint = checkpoint
        # Indicates whether full data synchronization is performed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.data_initialization = data_initialization
        # The status of full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The status of incremental data synchronization.
        self.data_synchronization_status = data_synchronization_status
        # The synchronization latency, in seconds.
        self.delay = delay
        # The synchronization delay, in milliseconds.
        self.delay_millis = delay_millis
        # The connection settings of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The error message returned if data synchronization failed.
        self.error_message = error_message
        # The time when the data synchronization instance expires. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        # 
        # >  This parameter is returned only if the return value of the **PayType** parameter is **PrePaid**.
        self.expire_time = expire_time
        # The billing method of the data synchronization instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.pay_type = pay_type
        # The performance of the data synchronization instance.
        self.performance = performance
        # The precheck status.
        self.precheck_status = precheck_status
        # The ID of the request.
        self.request_id = request_id
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The status of the data synchronization task. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **Initializing**: The task is performing initial synchronization.
        # *   **InitializeFailed**: Initial synchronization failed.
        # *   **Synchronizing**: The task is synchronizing data.
        # *   **Failed**: The task failed to synchronize data.
        # *   **Suspending**: The task is paused.
        # *   **Modifying**: The objects in the task are being modified.
        # *   **Finished**: The task is completed.
        self.status = status
        # Indicates whether schema synchronization is performed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.structure_initialization = structure_initialization
        # The status of schema synchronization.
        self.structure_initialization_status = structure_initialization_status
        # Indicates whether the call was successful.
        self.success = success
        # The synchronization direction. Valid values:
        # 
        # *   **Forward**
        # *   **Reverse**
        self.synchronization_direction = synchronization_direction
        # The specification of the data synchronization instance.
        self.synchronization_job_class = synchronization_job_class
        # The ID of the data synchronization instance.
        self.synchronization_job_id = synchronization_job_id
        # The name of the data synchronization task.
        self.synchronization_job_name = synchronization_job_name
        # The objects that are synchronized by the task.
        self.synchronization_objects = synchronization_objects
        self.task_id = task_id

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

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.delay_millis is not None:
            result['DelayMillis'] = self.delay_millis

        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

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

        if self.success is not None:
            result['Success'] = self.success

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

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DelayMillis') is not None:
            self.delay_millis = m.get('DelayMillis')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeSynchronizationJobStatusResponseBodyPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobStatusResponseBodyPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeSynchronizationJobStatusResponseBodySourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

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
                temp_model = main_models.DescribeSynchronizationJobStatusResponseBodySynchronizationObjects()
                self.synchronization_objects.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeSynchronizationJobStatusResponseBodySynchronizationObjects(DaraModel):
    def __init__(
        self,
        new_schema_name: str = None,
        schema_name: str = None,
        table_excludes: List[main_models.DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes] = None,
        table_includes: List[main_models.DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes] = None,
    ):
        # The database name that is used in the destination instance.
        self.new_schema_name = new_schema_name
        # The name of the synchronized database.
        self.schema_name = schema_name
        # The source tables that are excluded from the data synchronization task.
        self.table_excludes = table_excludes
        # The tables that are synchronized by the task.
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
                temp_model = main_models.DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes()
                self.table_excludes.append(temp_model.from_map(k1))

        self.table_includes = []
        if m.get('TableIncludes') is not None:
            for k1 in m.get('TableIncludes'):
                temp_model = main_models.DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes()
                self.table_includes.append(temp_model.from_map(k1))

        return self

class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableIncludes(DaraModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        # The name of the synchronized table.
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

class DescribeSynchronizationJobStatusResponseBodySynchronizationObjectsTableExcludes(DaraModel):
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

class DescribeSynchronizationJobStatusResponseBodyStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if schema synchronization failed.
        self.error_message = error_message
        # The progress of schema synchronization. Unit: %.
        self.percent = percent
        # The number of tables whose schemas have been synchronized.
        self.progress = progress
        # The status of schema synchronization. Valid values:
        # 
        # *   **NotStarted**: Schema synchronization is not started.
        # *   **Migrating**: Schema synchronization is in progress.
        # *   **Failed**: Schema synchronization failed.
        # *   **Finished**: Schema synchronization is completed.
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

class DescribeSynchronizationJobStatusResponseBodySourceEndpoint(DaraModel):
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
        # The ID of the source instance.
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

class DescribeSynchronizationJobStatusResponseBodyPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail] = None,
        percent: str = None,
        status: str = None,
    ):
        # The result of each precheck item.
        self.detail = detail
        # The precheck progress. Unit: %.
        self.percent = percent
        # The precheck result. Valid values:
        # 
        # *   **Success**: The task passed the precheck.
        # *   **Failed**: The task failed to pass the precheck.
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
                temp_model = main_models.DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSynchronizationJobStatusResponseBodyPrecheckStatusDetail(DaraModel):
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

class DescribeSynchronizationJobStatusResponseBodyPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The data traffic that is synchronized per second. Unit: MB/s.
        self.flow = flow
        # The number of times SQL statements are synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE.
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

class DescribeSynchronizationJobStatusResponseBodyDestinationEndpoint(DaraModel):
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
        # The ID of the destination instance.
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

class DescribeSynchronizationJobStatusResponseBodyDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        delay: str = None,
        delay_millis: int = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The UNIX timestamp generated when the latest data record was synchronized.
        self.checkpoint = checkpoint
        # The synchronization latency, in seconds.
        self.delay = delay
        # The synchronization latency, in milliseconds.
        self.delay_millis = delay_millis
        # The error message returned if incremental data synchronization failed.
        self.error_message = error_message
        # The progress of incremental data synchronization. Unit: %.
        self.percent = percent
        # The status of incremental data synchronization. Valid values:
        # 
        # *   **NotStarted**: Incremental data synchronization is not started.
        # *   **Migrating**: Incremental data synchronization is in progress.
        # *   **Failed**: Incremental data synchronization failed.
        # *   **Finished**: Incremental data synchronization is completed.
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

        if self.delay_millis is not None:
            result['DelayMillis'] = self.delay_millis

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

        if m.get('DelayMillis') is not None:
            self.delay_millis = m.get('DelayMillis')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSynchronizationJobStatusResponseBodyDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if full data synchronization failed.
        self.error_message = error_message
        # The progress of full data synchronization. Unit: %.
        self.percent = percent
        # The number of records that have been synchronized during full data synchronization.
        self.progress = progress
        # The status of full data synchronization. Valid values:
        # 
        # *   **NotStarted**: Full data synchronization is not started.
        # *   **Migrating**: Full data synchronization is in progress.
        # *   **Failed**: Full data synchronization failed.
        # *   **Finished**: Full data synchronization is completed.
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

