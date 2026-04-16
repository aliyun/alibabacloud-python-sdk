# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDtsJobsResponseBody(DaraModel):
    def __init__(
        self,
        dts_job_list: List[main_models.DescribeDtsJobsResponseBodyDtsJobList] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        etl_demo_list: List[main_models.DescribeDtsJobsResponseBodyEtlDemoList] = None,
        http_status_code: int = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: bool = None,
        total_record_count: int = None,
    ):
        # The Data Transmission Service (DTS) tasks and the details of each task.
        self.dts_job_list = dts_job_list
        # The dynamic error code. This parameter will be removed in the future.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. The value of this parameter is used to replace the **%s** variable in the value of the **ErrMessage** parameter.
        # 
        # >  For example, if the value of the **ErrMessage** parameter is **The Value of Input Parameter %s is not valid** and the value of the **DynamicMessage** parameter is **Type**, the specified **Type** parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The DTS tasks and the details of each task.
        self.etl_demo_list = etl_demo_list
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success
        # The total number of DTS tasks that meet the query condition.
        self.total_record_count = total_record_count

    def validate(self):
        if self.dts_job_list:
            for v1 in self.dts_job_list:
                 if v1:
                    v1.validate()
        if self.etl_demo_list:
            for v1 in self.etl_demo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DtsJobList'] = []
        if self.dts_job_list is not None:
            for k1 in self.dts_job_list:
                result['DtsJobList'].append(k1.to_map() if k1 else None)

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        result['EtlDemoList'] = []
        if self.etl_demo_list is not None:
            for k1 in self.etl_demo_list:
                result['EtlDemoList'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
        self.dts_job_list = []
        if m.get('DtsJobList') is not None:
            for k1 in m.get('DtsJobList'):
                temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobList()
                self.dts_job_list.append(temp_model.from_map(k1))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        self.etl_demo_list = []
        if m.get('EtlDemoList') is not None:
            for k1 in m.get('EtlDemoList'):
                temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoList()
                self.etl_demo_list.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

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

class DescribeDtsJobsResponseBodyEtlDemoList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        begin_timestamp: str = None,
        checkpoint: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        create_time: str = None,
        data_etl_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListDataEtlStatus = None,
        data_initialization_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListDataSynchronizationStatus = None,
        db_object: str = None,
        delay: int = None,
        destination_endpoint: main_models.DescribeDtsJobsResponseBodyEtlDemoListDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        end_timestamp: str = None,
        error_message: str = None,
        etl_safe_checkpoint: str = None,
        expire_time: str = None,
        job_type: str = None,
        migration_mode: main_models.DescribeDtsJobsResponseBodyEtlDemoListMigrationMode = None,
        origin_type: str = None,
        pay_type: str = None,
        performance: main_models.DescribeDtsJobsResponseBodyEtlDemoListPerformance = None,
        precheck_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatus = None,
        reserved: str = None,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
        retry_state: main_models.DescribeDtsJobsResponseBodyEtlDemoListRetryState = None,
        reverse_job: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJob = None,
        source_endpoint: main_models.DescribeDtsJobsResponseBodyEtlDemoListSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListStructureInitializationStatus = None,
        tag_list: List[main_models.DescribeDtsJobsResponseBodyEtlDemoListTagList] = None,
    ):
        # Indicates whether the **new** change tracking feature is used. 
        # 
        # > This parameter is returned only for change tracking instances of the new version.
        self.app_name = app_name
        # The start of the time range for change tracking. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.begin_timestamp = begin_timestamp
        # The start offset of incremental data migration or data synchronization. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.checkpoint = checkpoint
        # The consumption checkpoint of the change tracking instance. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.consumption_checkpoint = consumption_checkpoint
        # The downstream client information in the following format: <IP address of the downstream client>:<Random ID generated by DTS>.
        self.consumption_client = consumption_client
        # The time when the task was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:s*sZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The state of the ETL task. 
        # 
        # > This parameter collection is returned only if an ETL task is configured.
        self.data_etl_status = data_etl_status
        # The state of full data migration or initial full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The state of incremental data migration or synchronization.
        self.data_synchronization_status = data_synchronization_status
        # The objects of the data migration, data synchronization, or change tracking task. For more information, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        self.db_object = db_object
        # The latency of incremental data migration or synchronization. 
        # 
        # > If you query data migration tasks, the unit of this parameter is milliseconds. If you query data synchronization tasks, the unit of this parameter is seconds.
        self.delay = delay
        # The connection settings of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The ID of the data migration, data synchronization, or change tracking instance.
        self.dts_instance_id = dts_instance_id
        # The instance class. 
        # 
        # > For more information about the test performance of each instance class, see [Specifications of data migration instances](https://help.aliyun.com/document_detail/26606.html) and [Specifications of data synchronization instances](https://help.aliyun.com/document_detail/26605.html).
        self.dts_job_class = dts_job_class
        # The synchronization direction. Valid values:
        # 
        # - **Forward**
        # - **Reverse**
        # 
        # > This parameter is returned only if the topology of the data synchronization instance is two-way synchronization.
        self.dts_job_direction = dts_job_direction
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The name of the data migration, data synchronization, or change tracking task.
        self.dts_job_name = dts_job_name
        # The end of the time range for change tracking. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_timestamp = end_timestamp
        # The error message returned if the task failed.
        self.error_message = error_message
        # The checkpoint of the ETL task.
        self.etl_safe_checkpoint = etl_safe_checkpoint
        # The time when the instance expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # > This parameter is returned only if the returned value of **PayType** is **PrePaid**.
        self.expire_time = expire_time
        # The type of the DTS task. Valid values:
        # 
        # - **MIGRATION**: data migration task 
        # - **SYNC**: data synchronization task 
        # - **SUBSCRIBE**: change tracking task
        self.job_type = job_type
        # The migration types or initial synchronization types.
        self.migration_mode = migration_mode
        # The source of the task.
        # - **PTS**
        # - **DMS**
        # - **DTS**
        self.origin_type = origin_type
        # The billing method of the DTS instance. Valid values:
        # 
        # - **PrePaid**: subscription 
        # - **PostPaid**: pay-as-you-go
        self.pay_type = pay_type
        # The performance of the data migration or synchronization instance.
        self.performance = performance
        # The precheck state.
        self.precheck_status = precheck_status
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, for example, whether to automatically start a precheck. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        self.reserved = reserved
        # The name of the resource group.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The information about the retries performed by DTS due to an exception.
        self.retry_state = retry_state
        # The details of the data synchronization task in the reverse direction. 
        # 
        # > This parameter is returned only for two-way data synchronization tasks.
        self.reverse_job = reverse_job
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The state of the DTS instance. For more information about the valid values, see the description of the request parameter **Status**.
        self.status = status
        # The state of schema migration or initial schema synchronization.
        self.structure_initialization_status = structure_initialization_status
        # The tags of the task.
        self.tag_list = tag_list

    def validate(self):
        if self.data_etl_status:
            self.data_etl_status.validate()
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
        if self.retry_state:
            self.retry_state.validate()
        if self.reverse_job:
            self.reverse_job.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp

        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint

        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_etl_status is not None:
            result['DataEtlStatus'] = self.data_etl_status.to_map()

        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()

        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()

        if self.db_object is not None:
            result['DbObject'] = self.db_object

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id

        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class

        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.etl_safe_checkpoint is not None:
            result['EtlSafeCheckpoint'] = self.etl_safe_checkpoint

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()

        if self.origin_type is not None:
            result['OriginType'] = self.origin_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.performance is not None:
            result['Performance'] = self.performance.to_map()

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.resource_group_display_name is not None:
            result['ResourceGroupDisplayName'] = self.resource_group_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retry_state is not None:
            result['RetryState'] = self.retry_state.to_map()

        if self.reverse_job is not None:
            result['ReverseJob'] = self.reverse_job.to_map()

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')

        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')

        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataEtlStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListDataEtlStatus()
            self.data_etl_status = temp_model.from_map(m.get('DataEtlStatus'))

        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')

        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')

        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EtlSafeCheckpoint') is not None:
            self.etl_safe_checkpoint = m.get('EtlSafeCheckpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('OriginType') is not None:
            self.origin_type = m.get('OriginType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetryState') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListRetryState()
            self.retry_state = temp_model.from_map(m.get('RetryState'))

        if m.get('ReverseJob') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJob()
            self.reverse_job = temp_model.from_map(m.get('ReverseJob'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListTagList()
                self.tag_list.append(temp_model.from_map(k1))

        return self

class DescribeDtsJobsResponseBodyEtlDemoListTagList(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if schema migration or initial schema synchronization failed.
        self.error_message = error_message
        # The progress of schema migration or initial schema synchronization. Unit: percentage.
        self.percent = percent
        # The number of tables that have been migrated or synchronized during schema migration or initial schema synchronization.
        self.progress = progress
        # The state of schema migration or initial schema synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyEtlDemoListSourceEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database that contains the objects to be migrated from the source instance.
        self.database_name = database_name
        # The database engine of the source instance.
        self.engine_name = engine_name
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
        # The endpoint of the source instance.
        self.ip = ip
        # The SID of the Oracle database. 
        # 
        # > This parameter is returned only if the returned value of **EngineName** of the source instance is **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The port number of the source instance.
        self.port = port
        # The ID of the region in which the source instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **DISABLE**: SSL encryption is disabled. 
        # - **ENABLE_WITH_CERTIFICATE**: SSL encryption is enabled and the CA certificate is uploaded. 
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection with an AWS MongoDB Altas database. 
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection with a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJob(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        create_time: str = None,
        data_initialization_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataSynchronizationStatus = None,
        db_object: str = None,
        delay: int = None,
        destination_endpoint: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        error_message: str = None,
        etl_safe_checkpoint: str = None,
        expire_time: str = None,
        migration_mode: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobMigrationMode = None,
        pay_type: str = None,
        performance: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobPerformance = None,
        precheck_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatus = None,
        reserved: str = None,
        source_endpoint: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobStructureInitializationStatus = None,
    ):
        # The start offset of incremental data synchronization. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.checkpoint = checkpoint
        # The time when the task was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The state of initial full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The state of incremental data synchronization.
        self.data_synchronization_status = data_synchronization_status
        # The schema of the objects that you want to synchronize. The value is a JSON string and can contain regular expressions. For more information, see Objects of DTS tasks.
        self.db_object = db_object
        # The latency of incremental data synchronization. Unit: seconds.
        self.delay = delay
        # The connection settings of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The ID of the data synchronization instance.
        self.dts_instance_id = dts_instance_id
        # The instance class. 
        # 
        # > For more information about the test performance of each instance class, see [Specifications of data synchronization instances](https://help.aliyun.com/document_detail/26605.html).
        self.dts_job_class = dts_job_class
        # The synchronization direction. **Reverse** is returned.
        self.dts_job_direction = dts_job_direction
        # The ID of the synchronization task.
        self.dts_job_id = dts_job_id
        # The name of the data synchronization task.
        self.dts_job_name = dts_job_name
        # The error message returned if the task failed.
        self.error_message = error_message
        # The checkpoint of the ETL task.
        self.etl_safe_checkpoint = etl_safe_checkpoint
        # The time when the instance expires. The time follows the ISO 8601 standard in the* yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC. 
        # 
        # > This parameter is returned only if the returned value of **PayType** is **PrePaid**.
        self.expire_time = expire_time
        # The migration types or initial synchronization types.
        self.migration_mode = migration_mode
        # The billing method of the DTS instance. Valid values:
        # 
        # - **PrePaid**: subscription
        # - **PostPaid**: pay-as-you-go
        self.pay_type = pay_type
        # The performance of the data migration or synchronization instance.
        self.performance = performance
        # The precheck state.
        self.precheck_status = precheck_status
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, for example, whether to automatically start a precheck. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        self.reserved = reserved
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The state of the DTS instance. For more information about the valid values, see the description of the request parameter **Status**.
        self.status = status
        # The state of initial schema synchronization.
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
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()

        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()

        if self.db_object is not None:
            result['DbObject'] = self.db_object

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id

        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class

        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.etl_safe_checkpoint is not None:
            result['EtlSafeCheckpoint'] = self.etl_safe_checkpoint

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.performance is not None:
            result['Performance'] = self.performance.to_map()

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')

        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')

        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EtlSafeCheckpoint') is not None:
            self.etl_safe_checkpoint = m.get('EtlSafeCheckpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if initial schema synchronization failed.
        self.error_message = error_message
        # The progress of initial schema synchronization. Unit: percentage.
        self.percent = percent
        # The number of tables that have been synchronized during initial schema synchronization.
        self.progress = progress
        # The state of initial schema synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobSourceEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database that contains the objects to be migrated from the source instance.
        self.database_name = database_name
        # The database engine of the source instance.
        self.engine_name = engine_name
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
        # The endpoint of the source instance.
        self.ip = ip
        # The SID of the Oracle database. 
        # 
        # > This parameter is returned only if the returned value of **EngineName** of the source instance is **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The port number of the source instance.
        self.port = port
        # The ID of the region in which the source instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **DISABLE**: SSL encryption is disabled. 
        # - **ENABLE_WITH_CERTIFICATE**: SSL encryption is enabled and the CA certificate is uploaded. 
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection with an AWS MongoDB Altas database. 
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection with a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The result of each precheck item.
        self.detail = detail
        # The error message returned if the precheck failed.
        self.error_message = error_message
        # The precheck progress. Unit: percentage.
        self.percent = percent
        # The precheck state. Valid values:
        # 
        # - **NotStarted**: The precheck is not started. 
        # - **Suspending**: The precheck is paused. 
        # - **Checking**: The precheck is in progress. 
        # - **Failed**: The precheck failed. 
        # - **Finished**: The precheck is complete.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
                temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        # The name of the precheck item.
        self.check_item = check_item
        # The description of the precheck item.
        self.check_item_description = check_item_description
        # The precheck result. Valid values:
        # 
        # - **Success**
        # - **Failed**
        self.check_result = check_result
        # The error message returned if the task failed to pass the precheck. 
        # 
        # > This parameter is returned only if the returned value of **CheckResult** is **Failed**.
        self.failed_reason = failed_reason
        # The method to fix a precheck failure. 
        # 
        # > This parameter is returned only if the returned value of **CheckResult** is **Failed**.
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description

        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

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

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The size of data that is migrated or synchronized per second. Unit: MB/s.
        self.flow = flow
        # The number of times that SQL statements are migrated or synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE.
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow is not None:
            result['Flow'] = self.flow

        if self.rps is not None:
            result['Rps'] = self.rps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('Rps') is not None:
            self.rps = m.get('Rps')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        # Indicates whether full data migration or initial full data synchronization is performed. Valid values:
        # 
        # - **true**
        # - **false**
        self.data_initialization = data_initialization
        # Indicates whether incremental data migration or synchronization is performed. Valid values:
        # 
        # - **true**
        # - **false**
        self.data_synchronization = data_synchronization
        # Indicates whether schema migration or initial schema synchronization is performed. Valid values:
        # 
        # - **true**
        # - **false**
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

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobDestinationEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database that contains the synchronized objects in the destination instance.
        self.database_name = database_name
        # The database engine of the destination instance.
        self.engine_name = engine_name
        # The ID of the destination instance.
        self.instance_id = instance_id
        # The type of the destination instance.
        self.instance_type = instance_type
        # The endpoint of the destination instance.
        self.ip = ip
        # The SID of the Oracle database. 
        # 
        # > This parameter is returned only if the returned value of **EngineName** of the destination instance is **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The port number of the destination instance.
        self.port = port
        # The ID of the region in which the destination instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **DISABLE**: SSL encryption is disabled. 
        # - **ENABLE_WITH_CERTIFICATE**: SSL encryption is enabled and the CA certificate is uploaded. 
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection with an AWS MongoDB Altas database. 
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection with a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if incremental data synchronization failed.
        self.error_message = error_message
        # Indicates whether the instance needs to be upgraded. Valid values:
        # 
        # - **true**
        # - **false**
        # 
        # > To upgrade a DTS instance, call the [TransferInstanceClass](https://help.aliyun.com/document_detail/281093.html) operation.
        self.need_upgrade = need_upgrade
        # The progress of incremental data synchronization. Unit: percentage.
        self.percent = percent
        # The number of entries that have been migrated or synchronized during incremental data migration or synchronization.
        self.progress = progress
        # The state of incremental data synchronization.
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

        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade

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

        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListReverseJobDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if initial full data synchronization failed.
        self.error_message = error_message
        # The progress of initial full data synchronization. Unit: percentage.
        self.percent = percent
        # The number of entries that have been synchronized during initial full data synchronization.
        self.progress = progress
        # The state of initial full data synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyEtlDemoListRetryState(DaraModel):
    def __init__(
        self,
        err_message: str = None,
        job_id: str = None,
        max_retry_time: int = None,
        module: str = None,
        retry_count: int = None,
        retry_target: str = None,
        retry_time: int = None,
        retrying: bool = None,
    ):
        # The error message returned if these retries failed.
        self.err_message = err_message
        # The task ID.
        self.job_id = job_id
        # The maximum duration of a retry. Unit: seconds.
        self.max_retry_time = max_retry_time
        # The progress of the instance when DTS retries.
        self.module = module
        # The number of retries that have been performed.
        self.retry_count = retry_count
        # The object on which these retries are performed. Valid values:
        # 
        # - **srcDB**: the source database 
        # - **destDB**: the destination database 
        # - **inner_module**: an internal module of DTS
        self.retry_target = retry_target
        # The time that has elapsed from the time when the first retry starts. Unit: seconds.
        self.retry_time = retry_time
        # Indicates whether the task is being retried. Valid values:
        # 
        # - **true**
        # - **false**
        self.retrying = retrying

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.max_retry_time is not None:
            result['MaxRetryTime'] = self.max_retry_time

        if self.module is not None:
            result['Module'] = self.module

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        if self.retry_target is not None:
            result['RetryTarget'] = self.retry_target

        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time

        if self.retrying is not None:
            result['Retrying'] = self.retrying

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MaxRetryTime') is not None:
            self.max_retry_time = m.get('MaxRetryTime')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        if m.get('RetryTarget') is not None:
            self.retry_target = m.get('RetryTarget')

        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')

        if m.get('Retrying') is not None:
            self.retrying = m.get('Retrying')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The result of each precheck item.
        self.detail = detail
        # The error message returned if the precheck failed.
        self.error_message = error_message
        # The precheck progress. Unit: percentage.
        self.percent = percent
        # The precheck state. Valid values:
        # 
        # - **NotStarted**: The precheck is not started. 
        # - **Suspending**: The precheck is paused. 
        # - **Checking**: The precheck is in progress. 
        # - **Failed**: The precheck failed. 
        # - **Finished**: The precheck is complete.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
                temp_model = main_models.DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        # The name of the precheck item.
        self.check_item = check_item
        # The description of the precheck item.
        self.check_item_description = check_item_description
        # The precheck result. Valid values:
        # 
        # - **Success**
        # - **Failed**
        self.check_result = check_result
        # The error message returned if the task failed to pass the precheck. 
        # 
        # > This parameter is returned only if the returned value of **CheckResult** is **Failed**.
        self.failed_reason = failed_reason
        # The method to fix a precheck failure. 
        # 
        # > This parameter is returned only if the returned value of **CheckResult** is **Failed**.
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description

        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

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

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The size of data that is migrated or synchronized per second. Unit: MB/s.
        self.flow = flow
        # The number of times that SQL statements are migrated or synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE.
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow is not None:
            result['Flow'] = self.flow

        if self.rps is not None:
            result['Rps'] = self.rps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('Rps') is not None:
            self.rps = m.get('Rps')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        structure_initialization: bool = None,
    ):
        # Indicates whether full data migration or initial full data synchronization is performed. Valid values:
        # 
        # - **true**
        # - **false**
        self.data_initialization = data_initialization
        # Indicates whether incremental data migration or synchronization is performed. Valid values:
        # 
        # - **true**
        # - **false**
        self.data_synchronization = data_synchronization
        # Indicates whether schema migration or initial schema synchronization is performed. Valid values:
        # 
        # - **true**
        # - **false**
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

class DescribeDtsJobsResponseBodyEtlDemoListDestinationEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database that contains the migrated objects in the destination instance.
        self.database_name = database_name
        # The database engine of the destination instance.
        self.engine_name = engine_name
        # The ID of the destination instance.
        self.instance_id = instance_id
        # The type of the destination instance.
        self.instance_type = instance_type
        # The endpoint of the destination instance.
        self.ip = ip
        # The SID of the Oracle database. 
        # 
        # > This parameter is returned only if the returned value of **EngineName** of the destination instance is **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The port number of the destination instance.
        self.port = port
        # The ID of the region in which the destination instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **DISABLE**: SSL encryption is disabled. 
        # - **ENABLE_WITH_CERTIFICATE**: SSL encryption is enabled and the CA certificate is uploaded. 
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection with an AWS MongoDB Altas database. 
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection with a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if incremental data migration or synchronization failed.
        self.error_message = error_message
        # Indicates whether the instance needs to be upgraded. Valid values:
        # 
        # - **true**
        # - **false**
        # 
        # > To upgrade a DTS instance, call the [TransferInstanceClass](https://help.aliyun.com/document_detail/281093.html) operation.
        self.need_upgrade = need_upgrade
        # The progress of incremental data migration or synchronization. Unit: percentage.
        self.percent = percent
        # The number of entries that have been migrated or synchronized during incremental data migration or synchronization.
        self.progress = progress
        # The state of incremental data migration or synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete. 
        # - **Catched**: The task is not delayed.
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

        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade

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

        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyEtlDemoListDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if full data migration or initial full data synchronization failed.
        self.error_message = error_message
        # The progress of full data migration or initial full data synchronization. Unit: percentage.
        self.percent = percent
        # The number of entries that have been migrated or synchronized during full data migration or initial full data synchronization.
        self.progress = progress
        # The state of full data migration or initial full data synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyEtlDemoListDataEtlStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if the ETL task failed.
        self.error_message = error_message
        # The progress of the ETL task. Unit: percentage.
        self.percent = percent
        # The number of entries that have been processed by the ETL task.
        self.progress = progress
        # The state of the ETL task. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete. 
        # - **Catched**: The task is not delayed.
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

class DescribeDtsJobsResponseBodyDtsJobList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        begin_timestamp: str = None,
        checkpoint: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        cpu_usage: str = None,
        create_time: str = None,
        data_cloud_status: main_models.DescribeDtsJobsResponseBodyDtsJobListDataCloudStatus = None,
        data_etl_status: main_models.DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus = None,
        data_initialization_status: main_models.DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus = None,
        db_object: str = None,
        dedicated_cluster_id: str = None,
        delay: int = None,
        destination_endpoint: main_models.DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint = None,
        dts_bis_label: str = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        du_real_usage: str = None,
        du_usage: int = None,
        end_timestamp: str = None,
        error_details: List[main_models.DescribeDtsJobsResponseBodyDtsJobListErrorDetails] = None,
        error_message: str = None,
        etl_safe_checkpoint: str = None,
        expire_time: str = None,
        full_data_check_status: main_models.DescribeDtsJobsResponseBodyDtsJobListFullDataCheckStatus = None,
        inc_data_check_status: main_models.DescribeDtsJobsResponseBodyDtsJobListIncDataCheckStatus = None,
        insight_module: bool = None,
        job_type: str = None,
        max_du: float = None,
        mem_usage: str = None,
        migration_err_code: str = None,
        migration_err_help_doc_id: str = None,
        migration_err_help_doc_key: str = None,
        migration_err_msg: str = None,
        migration_err_type: str = None,
        migration_err_workaround: str = None,
        migration_mode: main_models.DescribeDtsJobsResponseBodyDtsJobListMigrationMode = None,
        min_du: float = None,
        origin_type: str = None,
        pay_type: str = None,
        performance: main_models.DescribeDtsJobsResponseBodyDtsJobListPerformance = None,
        precheck_status: main_models.DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus = None,
        reserved: str = None,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
        retry_state: main_models.DescribeDtsJobsResponseBodyDtsJobListRetryState = None,
        reverse_job: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJob = None,
        source_endpoint: main_models.DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint = None,
        status: str = None,
        structure_data_check_status: main_models.DescribeDtsJobsResponseBodyDtsJobListStructureDataCheckStatus = None,
        structure_initialization_status: main_models.DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus = None,
        tag_list: List[main_models.DescribeDtsJobsResponseBodyDtsJobListTagList] = None,
    ):
        # Indicates whether the **new** change tracking feature is used.
        # 
        # >  This parameter is returned only for change tracking instances of the new version.
        self.app_name = app_name
        # The start of the time range for change tracking. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.begin_timestamp = begin_timestamp
        # The start offset of incremental data synchronization. The value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.checkpoint = checkpoint
        # The consumption checkpoint of the change tracking instance. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.consumption_checkpoint = consumption_checkpoint
        # The downstream client information, in the following format: \\<IP address of the downstream client>:\\<Random ID generated by DTS>.
        self.consumption_client = consumption_client
        # The CPU utilization of the instance. Unit: percentage.
        self.cpu_usage = cpu_usage
        # The point in time when the task was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The state of the physical gateway-based migration task.
        self.data_cloud_status = data_cloud_status
        # The state of the extract, transform, and load (ETL) task. Valid values:
        # 
        # >  This parameter collection is returned only if an ETL task is configured.
        self.data_etl_status = data_etl_status
        # The state of full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The state of incremental data migration or synchronization.
        self.data_synchronization_status = data_synchronization_status
        # The objects that you want to synchronize. The value is a JSON string and can contain regular expressions. For more information, see "Objects of DTS tasks".
        self.db_object = db_object
        # The ID of the DTS dedicated cluster on which a DTS task runs.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The latency of incremental data synchronization. Unit: seconds.
        self.delay = delay
        # The connection settings of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The environment tag of the DTS instance. Valid values:
        # 
        # - **normal**
        # - **online**
        self.dts_bis_label = dts_bis_label
        # The ID of the data synchronization instance.
        self.dts_instance_id = dts_instance_id
        # The instance class.
        # 
        # >  For more information about the test performance of each instance class, see [Specifications of data synchronization instances](https://help.aliyun.com/document_detail/26605.html).
        self.dts_job_class = dts_job_class
        # The synchronization direction. The value is **Reverse**.
        self.dts_job_direction = dts_job_direction
        # The ID of the data synchronization task.
        self.dts_job_id = dts_job_id
        # The name of the data synchronization task.
        self.dts_job_name = dts_job_name
        # The DTS Units (DUs) usage of a task in a DTS dedicated cluster.
        self.du_real_usage = du_real_usage
        # The number of DUs that have been used.
        self.du_usage = du_usage
        # The end of the time range for change tracking. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_timestamp = end_timestamp
        # The error message returned.
        self.error_details = error_details
        # The error message returned if the task failed.
        self.error_message = error_message
        # The checkpoint of the ETL task.
        self.etl_safe_checkpoint = etl_safe_checkpoint
        # The point in time when the instance expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        # 
        # >  This parameter is returned only if the value of the **PayType** parameter is **PrePaid**.
        self.expire_time = expire_time
        # The state information about the full data verification task.
        self.full_data_check_status = full_data_check_status
        # The state information about the incremental data verification task.
        self.inc_data_check_status = inc_data_check_status
        self.insight_module = insight_module
        # The type of the DTS task. Valid values:
        # 
        # - **MIGRATION**: data migration task 
        # - **SYNC**: data synchronization task 
        # - **SUBSCRIBE**: change tracking task
        self.job_type = job_type
        # Upper limit of DU.
        # 
        # > Only supported by Serverless instances.
        self.max_du = max_du
        # The memory that has been used. Unit: MB.
        self.mem_usage = mem_usage
        # The error code.
        self.migration_err_code = migration_err_code
        # The ID of the error code-related documentation.
        self.migration_err_help_doc_id = migration_err_help_doc_id
        # The key of the error code-related documentation.
        self.migration_err_help_doc_key = migration_err_help_doc_key
        # The error message.
        self.migration_err_msg = migration_err_msg
        # The type of the error code.
        self.migration_err_type = migration_err_type
        # The solution to the error.
        self.migration_err_workaround = migration_err_workaround
        # The migration or synchronization modes.
        self.migration_mode = migration_mode
        # Lower limit of DU.
        # 
        # > Only supported by Serverless instances.
        self.min_du = min_du
        # The source of the task. Valid values:
        # 
        # *   **PTS**
        # *   **DMS**
        # *   **DTS**
        self.origin_type = origin_type
        # The billing method of the DTS instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.pay_type = pay_type
        # The performance of the data migration or synchronization instance.
        self.performance = performance
        # The precheck state.
        self.precheck_status = precheck_status
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, for example, whether to automatically start a precheck. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        self.reserved = reserved
        # The name of the resource group.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The information about the retries performed by DTS due to an exception.
        self.retry_state = retry_state
        # The details of the data synchronization task in the reverse direction. 
        # 
        # > This parameter is returned only for two-way data synchronization tasks.
        self.reverse_job = reverse_job
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The state of the DTS instance. For more information about the valid values, see the description of the request parameter **Status**.
        self.status = status
        self.structure_data_check_status = structure_data_check_status
        # The state of schema migration or initial schema synchronization.
        self.structure_initialization_status = structure_initialization_status
        # The tags of the task.
        self.tag_list = tag_list

    def validate(self):
        if self.data_cloud_status:
            self.data_cloud_status.validate()
        if self.data_etl_status:
            self.data_etl_status.validate()
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.error_details:
            for v1 in self.error_details:
                 if v1:
                    v1.validate()
        if self.full_data_check_status:
            self.full_data_check_status.validate()
        if self.inc_data_check_status:
            self.inc_data_check_status.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.retry_state:
            self.retry_state.validate()
        if self.reverse_job:
            self.reverse_job.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_data_check_status:
            self.structure_data_check_status.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp

        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint

        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client

        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_cloud_status is not None:
            result['DataCloudStatus'] = self.data_cloud_status.to_map()

        if self.data_etl_status is not None:
            result['DataEtlStatus'] = self.data_etl_status.to_map()

        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()

        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()

        if self.db_object is not None:
            result['DbObject'] = self.db_object

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.dts_bis_label is not None:
            result['DtsBisLabel'] = self.dts_bis_label

        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id

        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class

        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.du_real_usage is not None:
            result['DuRealUsage'] = self.du_real_usage

        if self.du_usage is not None:
            result['DuUsage'] = self.du_usage

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k1 in self.error_details:
                result['ErrorDetails'].append(k1.to_map() if k1 else None)

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.etl_safe_checkpoint is not None:
            result['EtlSafeCheckpoint'] = self.etl_safe_checkpoint

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.full_data_check_status is not None:
            result['FullDataCheckStatus'] = self.full_data_check_status.to_map()

        if self.inc_data_check_status is not None:
            result['IncDataCheckStatus'] = self.inc_data_check_status.to_map()

        if self.insight_module is not None:
            result['InsightModule'] = self.insight_module

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.max_du is not None:
            result['MaxDu'] = self.max_du

        if self.mem_usage is not None:
            result['MemUsage'] = self.mem_usage

        if self.migration_err_code is not None:
            result['MigrationErrCode'] = self.migration_err_code

        if self.migration_err_help_doc_id is not None:
            result['MigrationErrHelpDocId'] = self.migration_err_help_doc_id

        if self.migration_err_help_doc_key is not None:
            result['MigrationErrHelpDocKey'] = self.migration_err_help_doc_key

        if self.migration_err_msg is not None:
            result['MigrationErrMsg'] = self.migration_err_msg

        if self.migration_err_type is not None:
            result['MigrationErrType'] = self.migration_err_type

        if self.migration_err_workaround is not None:
            result['MigrationErrWorkaround'] = self.migration_err_workaround

        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()

        if self.min_du is not None:
            result['MinDu'] = self.min_du

        if self.origin_type is not None:
            result['OriginType'] = self.origin_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.performance is not None:
            result['Performance'] = self.performance.to_map()

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.resource_group_display_name is not None:
            result['ResourceGroupDisplayName'] = self.resource_group_display_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.retry_state is not None:
            result['RetryState'] = self.retry_state.to_map()

        if self.reverse_job is not None:
            result['ReverseJob'] = self.reverse_job.to_map()

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.structure_data_check_status is not None:
            result['StructureDataCheckStatus'] = self.structure_data_check_status.to_map()

        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')

        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')

        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')

        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataCloudStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListDataCloudStatus()
            self.data_cloud_status = temp_model.from_map(m.get('DataCloudStatus'))

        if m.get('DataEtlStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus()
            self.data_etl_status = temp_model.from_map(m.get('DataEtlStatus'))

        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('DtsBisLabel') is not None:
            self.dts_bis_label = m.get('DtsBisLabel')

        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')

        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')

        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('DuRealUsage') is not None:
            self.du_real_usage = m.get('DuRealUsage')

        if m.get('DuUsage') is not None:
            self.du_usage = m.get('DuUsage')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k1 in m.get('ErrorDetails'):
                temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListErrorDetails()
                self.error_details.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EtlSafeCheckpoint') is not None:
            self.etl_safe_checkpoint = m.get('EtlSafeCheckpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FullDataCheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListFullDataCheckStatus()
            self.full_data_check_status = temp_model.from_map(m.get('FullDataCheckStatus'))

        if m.get('IncDataCheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListIncDataCheckStatus()
            self.inc_data_check_status = temp_model.from_map(m.get('IncDataCheckStatus'))

        if m.get('InsightModule') is not None:
            self.insight_module = m.get('InsightModule')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MemUsage') is not None:
            self.mem_usage = m.get('MemUsage')

        if m.get('MigrationErrCode') is not None:
            self.migration_err_code = m.get('MigrationErrCode')

        if m.get('MigrationErrHelpDocId') is not None:
            self.migration_err_help_doc_id = m.get('MigrationErrHelpDocId')

        if m.get('MigrationErrHelpDocKey') is not None:
            self.migration_err_help_doc_key = m.get('MigrationErrHelpDocKey')

        if m.get('MigrationErrMsg') is not None:
            self.migration_err_msg = m.get('MigrationErrMsg')

        if m.get('MigrationErrType') is not None:
            self.migration_err_type = m.get('MigrationErrType')

        if m.get('MigrationErrWorkaround') is not None:
            self.migration_err_workaround = m.get('MigrationErrWorkaround')

        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('OriginType') is not None:
            self.origin_type = m.get('OriginType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetryState') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListRetryState()
            self.retry_state = temp_model.from_map(m.get('RetryState'))

        if m.get('ReverseJob') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJob()
            self.reverse_job = temp_model.from_map(m.get('ReverseJob'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureDataCheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListStructureDataCheckStatus()
            self.structure_data_check_status = temp_model.from_map(m.get('StructureDataCheckStatus'))

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListTagList()
                self.tag_list.append(temp_model.from_map(k1))

        return self

class DescribeDtsJobsResponseBodyDtsJobListTagList(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeDtsJobsResponseBodyDtsJobListStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if schema migration or initial schema synchronization failed.
        self.error_message = error_message
        # The progress of schema migration or initial schema synchronization. Unit: percentage.
        self.percent = percent
        # The number of tables that have been migrated or synchronized during schema migration or initial schema synchronization.
        self.progress = progress
        # The state of schema migration or initial schema synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyDtsJobListStructureDataCheckStatus(DaraModel):
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

class DescribeDtsJobsResponseBodyDtsJobListSourceEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database that contains the objects to be migrated from the source instance.
        self.database_name = database_name
        # The database engine of the source instance.
        self.engine_name = engine_name
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
        # The endpoint of the source instance.
        self.ip = ip
        # The SID of the Oracle database. 
        # 
        # > This parameter is returned only if the returned value of **EngineName** of the source instance is **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The port number of the source instance.
        self.port = port
        # The ID of the region in which the source instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **DISABLE**: SSL encryption is disabled. 
        # - **ENABLE_WITH_CERTIFICAT**E: SSL encryption is enabled and the CA certificate is uploaded. 
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection with an AWS MongoDB Altas database. 
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection with a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJob(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        cpu_usage: str = None,
        create_time: str = None,
        data_initialization_status: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus = None,
        db_object: str = None,
        dedicated_cluster_id: str = None,
        delay: int = None,
        destination_endpoint: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        du_usage: int = None,
        error_details: List[main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobErrorDetails] = None,
        error_message: str = None,
        etl_safe_checkpoint: str = None,
        expire_time: str = None,
        full_data_check_status: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobFullDataCheckStatus = None,
        inc_data_check_status: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobIncDataCheckStatus = None,
        max_du: float = None,
        mem_usage: str = None,
        migration_mode: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode = None,
        min_du: float = None,
        pay_type: str = None,
        performance: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance = None,
        precheck_status: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus = None,
        reserved: str = None,
        source_endpoint: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint = None,
        status: str = None,
        structure_data_check_status: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureDataCheckStatus = None,
        structure_initialization_status: main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus = None,
    ):
        # The start offset of incremental data synchronization. This value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.checkpoint = checkpoint
        # The CPU utilization of the instance. Unit: percentage.
        self.cpu_usage = cpu_usage
        # The time when the task was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The state of initial full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The state of incremental data synchronization.
        self.data_synchronization_status = data_synchronization_status
        # The schema of the objects that you want to synchronize. The value is a JSON string and can contain regular expressions. For more information, see Objects of DTS tasks.
        self.db_object = db_object
        # The ID of the DTS dedicated cluster on which a DTS task runs.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The latency of incremental data synchronization. Unit: seconds.
        self.delay = delay
        # The connection settings of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The ID of the data synchronization instance.
        self.dts_instance_id = dts_instance_id
        # The instance class. 
        # 
        # > For more information about the test performance of each instance class, see [Specifications of data synchronization instances](https://help.aliyun.com/document_detail/26605.html).
        self.dts_job_class = dts_job_class
        # The synchronization direction. **Reverse** is returned.
        self.dts_job_direction = dts_job_direction
        # The ID of the synchronization task.
        self.dts_job_id = dts_job_id
        # The name of the data synchronization task.
        self.dts_job_name = dts_job_name
        # The number of DUs that have been used.
        self.du_usage = du_usage
        # The error message returned.
        self.error_details = error_details
        # The error message returned if the task failed.
        self.error_message = error_message
        # The checkpoint of the ETL task.
        self.etl_safe_checkpoint = etl_safe_checkpoint
        # The time when the instance expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC. 
        # 
        # > This parameter is returned only if the returned value of **PayType** is **PrePaid**.
        self.expire_time = expire_time
        # The state information about the full data verification task.
        self.full_data_check_status = full_data_check_status
        # The state information about the incremental data verification task.
        self.inc_data_check_status = inc_data_check_status
        # Upper limit of DU.
        # 
        # > Only supported by Serverless instances.
        self.max_du = max_du
        # The memory that has been used. Unit: MB.
        self.mem_usage = mem_usage
        # The initial synchronization types.
        self.migration_mode = migration_mode
        # Lower limit of DU.
        # 
        # > Only supported by Serverless instances.
        self.min_du = min_du
        # The billing method of the DTS instance. Valid values:
        # 
        # - **PrePaid**: subscription
        # - **PostPaid**: pay-as-you-go
        self.pay_type = pay_type
        # The performance of the data synchronization instance.
        self.performance = performance
        # The precheck state.
        self.precheck_status = precheck_status
        # The reserved parameter of DTS. The value is a JSON string. You can specify this parameter to meet specific requirements, for example, whether to automatically start a precheck. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        self.reserved = reserved
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The state of the DTS instance. For more information about the valid values, see the description of the request parameter **Status**.
        self.status = status
        self.structure_data_check_status = structure_data_check_status
        # The state of initial schema synchronization.
        self.structure_initialization_status = structure_initialization_status

    def validate(self):
        if self.data_initialization_status:
            self.data_initialization_status.validate()
        if self.data_synchronization_status:
            self.data_synchronization_status.validate()
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.error_details:
            for v1 in self.error_details:
                 if v1:
                    v1.validate()
        if self.full_data_check_status:
            self.full_data_check_status.validate()
        if self.inc_data_check_status:
            self.inc_data_check_status.validate()
        if self.migration_mode:
            self.migration_mode.validate()
        if self.performance:
            self.performance.validate()
        if self.precheck_status:
            self.precheck_status.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.structure_data_check_status:
            self.structure_data_check_status.validate()
        if self.structure_initialization_status:
            self.structure_initialization_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_initialization_status is not None:
            result['DataInitializationStatus'] = self.data_initialization_status.to_map()

        if self.data_synchronization_status is not None:
            result['DataSynchronizationStatus'] = self.data_synchronization_status.to_map()

        if self.db_object is not None:
            result['DbObject'] = self.db_object

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.dts_instance_id is not None:
            result['DtsInstanceID'] = self.dts_instance_id

        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class

        if self.dts_job_direction is not None:
            result['DtsJobDirection'] = self.dts_job_direction

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.du_usage is not None:
            result['DuUsage'] = self.du_usage

        result['ErrorDetails'] = []
        if self.error_details is not None:
            for k1 in self.error_details:
                result['ErrorDetails'].append(k1.to_map() if k1 else None)

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.etl_safe_checkpoint is not None:
            result['EtlSafeCheckpoint'] = self.etl_safe_checkpoint

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.full_data_check_status is not None:
            result['FullDataCheckStatus'] = self.full_data_check_status.to_map()

        if self.inc_data_check_status is not None:
            result['IncDataCheckStatus'] = self.inc_data_check_status.to_map()

        if self.max_du is not None:
            result['MaxDu'] = self.max_du

        if self.mem_usage is not None:
            result['MemUsage'] = self.mem_usage

        if self.migration_mode is not None:
            result['MigrationMode'] = self.migration_mode.to_map()

        if self.min_du is not None:
            result['MinDu'] = self.min_du

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.performance is not None:
            result['Performance'] = self.performance.to_map()

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status.to_map()

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.structure_data_check_status is not None:
            result['StructureDataCheckStatus'] = self.structure_data_check_status.to_map()

        if self.structure_initialization_status is not None:
            result['StructureInitializationStatus'] = self.structure_initialization_status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('DtsInstanceID') is not None:
            self.dts_instance_id = m.get('DtsInstanceID')

        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')

        if m.get('DtsJobDirection') is not None:
            self.dts_job_direction = m.get('DtsJobDirection')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('DuUsage') is not None:
            self.du_usage = m.get('DuUsage')

        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k1 in m.get('ErrorDetails'):
                temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobErrorDetails()
                self.error_details.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EtlSafeCheckpoint') is not None:
            self.etl_safe_checkpoint = m.get('EtlSafeCheckpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FullDataCheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobFullDataCheckStatus()
            self.full_data_check_status = temp_model.from_map(m.get('FullDataCheckStatus'))

        if m.get('IncDataCheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobIncDataCheckStatus()
            self.inc_data_check_status = temp_model.from_map(m.get('IncDataCheckStatus'))

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MemUsage') is not None:
            self.mem_usage = m.get('MemUsage')

        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureDataCheckStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureDataCheckStatus()
            self.structure_data_check_status = temp_model.from_map(m.get('StructureDataCheckStatus'))

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if initial schema synchronization failed.
        self.error_message = error_message
        # The progress of initial schema synchronization. Unit: percentage.
        self.percent = percent
        # The number of tables that have been synchronized during initial schema synchronization.
        self.progress = progress
        # The state of initial schema synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyDtsJobListReverseJobStructureDataCheckStatus(DaraModel):
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

class DescribeDtsJobsResponseBodyDtsJobListReverseJobSourceEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database that contains the objects to be migrated from the source instance.
        self.database_name = database_name
        # The database engine of the source instance.
        self.engine_name = engine_name
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
        # The endpoint of the source instance.
        self.ip = ip
        # The SID of the Oracle database. 
        # 
        # > This parameter is returned only if the returned value of **EngineName** of the source instance is **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The port number of the source instance.
        self.port = port
        # The ID of the region in which the source instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **DISABLE**: SSL encryption is disabled. 
        # - **ENABLE_WITH_CERTIFICATE**: SSL encryption is enabled and the CA certificate is uploaded. 
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection with an AWS MongoDB Altas database. 
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection with a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The result of each precheck item.
        self.detail = detail
        # The error message returned if the precheck failed.
        self.error_message = error_message
        # The precheck progress. Unit: percentage.
        self.percent = percent
        # The precheck state. Valid values:
        # 
        # - **NotStarted**: The precheck is not started. 
        # - **Suspending**: The precheck is paused. 
        # - **Checking**: The precheck is in progress. 
        # - **Failed**: The precheck failed. 
        # - **Finished**: The precheck is complete.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
                temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        # The name of the precheck item.
        self.check_item = check_item
        # The description of the precheck item.
        self.check_item_description = check_item_description
        # The precheck result. Valid values:
        # 
        # - **Success**
        # - **Failed**
        self.check_result = check_result
        # The error message returned if the task failed to pass the precheck.
        self.failed_reason = failed_reason
        # The method to fix a precheck failure.
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description

        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

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

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The size of data that is synchronized per second. Unit: MB/s.
        self.flow = flow
        # The number of times that SQL statements are synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE.
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow is not None:
            result['Flow'] = self.flow

        if self.rps is not None:
            result['Rps'] = self.rps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('Rps') is not None:
            self.rps = m.get('Rps')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        full_data_check: bool = None,
        inc_data_check: bool = None,
        structure_data_check: bool = None,
        structure_initialization: bool = None,
    ):
        # Indicates whether initial full data synchronization is performed. Valid values:
        # 
        # -  **true**
        # -  **false**
        self.data_initialization = data_initialization
        # Indicates whether incremental data synchronization is performed. Valid values:
        # -  **true**
        # -  **false**
        self.data_synchronization = data_synchronization
        # Indicates whether full data verification is performed. Valid values:
        # -  **true**: yes
        # -  **false**: no
        self.full_data_check = full_data_check
        # Indicates whether incremental data verification is performed. Valid values:
        # -  **true**: yes
        # -  **false**: no
        self.inc_data_check = inc_data_check
        self.structure_data_check = structure_data_check
        # Indicates whether initial schema synchronization is performed. Valid values:
        # -  **true**
        # -  **false**
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

        if self.full_data_check is not None:
            result['FullDataCheck'] = self.full_data_check

        if self.inc_data_check is not None:
            result['IncDataCheck'] = self.inc_data_check

        if self.structure_data_check is not None:
            result['StructureDataCheck'] = self.structure_data_check

        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')

        if m.get('FullDataCheck') is not None:
            self.full_data_check = m.get('FullDataCheck')

        if m.get('IncDataCheck') is not None:
            self.inc_data_check = m.get('IncDataCheck')

        if m.get('StructureDataCheck') is not None:
            self.structure_data_check = m.get('StructureDataCheck')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobIncDataCheckStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if the task failed.
        self.error_message = error_message
        # The progress of the incremental data verification task. Unit: percentage.
        self.percent = percent
        # The progress of the incremental data verification task.
        self.progress = progress
        # The state of the incremental data verification task. Valid values:
        # 
        # - **Catched**: The verification is delayed. 
        # - **NotStarted**: The verification is not started. 
        # - **Checking**: The verification is in progress. 
        # - **Failed**: The verification failed.
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

class DescribeDtsJobsResponseBodyDtsJobListReverseJobFullDataCheckStatus(DaraModel):
    def __init__(
        self,
        can_switch: bool = None,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.can_switch = can_switch
        # The error message returned if the task failed.
        self.error_message = error_message
        # The progress of the full data verification task. Unit: percentage.
        self.percent = percent
        # The progress of the full data verification task.
        self.progress = progress
        # The state of the full data verification task. Valid values:
        # 
        # - **NotStarted**: The verification is not started. 
        # - **Checking**: The verification is in progress. 
        # - **Failed**: The verification failed. 
        # - **Finished**: The verification is complete.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_switch is not None:
            result['CanSwitch'] = self.can_switch

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
        if m.get('CanSwitch') is not None:
            self.can_switch = m.get('CanSwitch')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobErrorDetails(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        help_url: str = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The URL of the documentation.
        self.help_url = help_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.help_url is not None:
            result['HelpUrl'] = self.help_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobDestinationEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database that contains the synchronized objects in the destination instance.
        self.database_name = database_name
        # The database engine of the destination instance.
        self.engine_name = engine_name
        # The ID of the destination instance.
        self.instance_id = instance_id
        # The type of the destination instance.
        self.instance_type = instance_type
        # The endpoint of the destination instance.
        self.ip = ip
        # The SID of the Oracle database. 
        # 
        # > This parameter is returned only if the returned value of **EngineName** of the destination instance is **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The port number of the destination instance.
        self.port = port
        # The ID of the region in which the destination instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # - **DISABLE**: SSL encryption is disabled. 
        # - **ENABLE_WITH_CERTIFICATE**: SSL encryption is enabled and the CA certificate is uploaded. 
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection with an AWS MongoDB Altas database. 
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection with a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if incremental data synchronization failed.
        self.error_message = error_message
        # Indicates whether the instance needs to be upgraded. Valid values:
        # 
        # - **true**
        # - **false**
        # 
        # > To upgrade a DTS instance, call the [TransferInstanceClass](https://help.aliyun.com/document_detail/281093.html) operation.
        self.need_upgrade = need_upgrade
        # The progress of incremental data synchronization. Unit: percentage.
        self.percent = percent
        # The number of entries that have been migrated or synchronized during incremental data migration or synchronization.
        self.progress = progress
        # The state of incremental data synchronization.
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

        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade

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

        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyDtsJobListReverseJobDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if initial full data synchronization failed.
        self.error_message = error_message
        # The progress of initial full data synchronization. Unit: percentage.
        self.percent = percent
        # The number of entries that have been synchronized during initial full data synchronization.
        self.progress = progress
        # The state of initial full data synchronization. Valid values:
        # 
        # - **NotStarted**: The task is not started. 
        # - **Migrating**: The task is in progress. 
        # - **Failed**: The task failed. 
        # - **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyDtsJobListRetryState(DaraModel):
    def __init__(
        self,
        err_message: str = None,
        job_id: str = None,
        max_retry_time: int = None,
        migration_err_code: str = None,
        migration_err_help_doc_id: str = None,
        migration_err_help_doc_key: str = None,
        migration_err_msg: str = None,
        migration_err_type: str = None,
        migration_err_workaround: str = None,
        module: str = None,
        retry_count: int = None,
        retry_target: str = None,
        retry_time: int = None,
        retrying: bool = None,
    ):
        # The error message returned if these retries failed.
        self.err_message = err_message
        # The task ID.
        self.job_id = job_id
        # The maximum duration of a retry. Unit: seconds.
        self.max_retry_time = max_retry_time
        # The error code.
        self.migration_err_code = migration_err_code
        # The ID of the error code-related documentation.
        self.migration_err_help_doc_id = migration_err_help_doc_id
        # The key of the error code-related documentation.
        self.migration_err_help_doc_key = migration_err_help_doc_key
        # The error message.
        self.migration_err_msg = migration_err_msg
        # The type of the error code.
        self.migration_err_type = migration_err_type
        # The solution to the error.
        self.migration_err_workaround = migration_err_workaround
        # The progress of the instance when DTS retries.
        self.module = module
        # The number of retries that have been performed.
        self.retry_count = retry_count
        # The object on which these retries are performed. Valid values:
        # 
        # - **srcDB**: the source database 
        # - **destDB**: the destination database 
        # - **inner_module**: an internal module of DTS
        self.retry_target = retry_target
        # The time that has elapsed from the time when the first retry starts. Unit: seconds.
        self.retry_time = retry_time
        # Indicates whether the task is being retried. Valid values:
        # 
        # - **true**
        # - **false**
        self.retrying = retrying

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.max_retry_time is not None:
            result['MaxRetryTime'] = self.max_retry_time

        if self.migration_err_code is not None:
            result['MigrationErrCode'] = self.migration_err_code

        if self.migration_err_help_doc_id is not None:
            result['MigrationErrHelpDocId'] = self.migration_err_help_doc_id

        if self.migration_err_help_doc_key is not None:
            result['MigrationErrHelpDocKey'] = self.migration_err_help_doc_key

        if self.migration_err_msg is not None:
            result['MigrationErrMsg'] = self.migration_err_msg

        if self.migration_err_type is not None:
            result['MigrationErrType'] = self.migration_err_type

        if self.migration_err_workaround is not None:
            result['MigrationErrWorkaround'] = self.migration_err_workaround

        if self.module is not None:
            result['Module'] = self.module

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        if self.retry_target is not None:
            result['RetryTarget'] = self.retry_target

        if self.retry_time is not None:
            result['RetryTime'] = self.retry_time

        if self.retrying is not None:
            result['Retrying'] = self.retrying

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MaxRetryTime') is not None:
            self.max_retry_time = m.get('MaxRetryTime')

        if m.get('MigrationErrCode') is not None:
            self.migration_err_code = m.get('MigrationErrCode')

        if m.get('MigrationErrHelpDocId') is not None:
            self.migration_err_help_doc_id = m.get('MigrationErrHelpDocId')

        if m.get('MigrationErrHelpDocKey') is not None:
            self.migration_err_help_doc_key = m.get('MigrationErrHelpDocKey')

        if m.get('MigrationErrMsg') is not None:
            self.migration_err_msg = m.get('MigrationErrMsg')

        if m.get('MigrationErrType') is not None:
            self.migration_err_type = m.get('MigrationErrType')

        if m.get('MigrationErrWorkaround') is not None:
            self.migration_err_workaround = m.get('MigrationErrWorkaround')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        if m.get('RetryTarget') is not None:
            self.retry_target = m.get('RetryTarget')

        if m.get('RetryTime') is not None:
            self.retry_time = m.get('RetryTime')

        if m.get('Retrying') is not None:
            self.retrying = m.get('Retrying')

        return self

class DescribeDtsJobsResponseBodyDtsJobListPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The result of each precheck item.
        self.detail = detail
        # The cause of the precheck failure.
        self.error_message = error_message
        # The precheck progress. This is expressed as a percentage.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
                temp_model = main_models.DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyDtsJobListPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        # The name of the precheck item.
        self.check_item = check_item
        # The description of the precheck item.
        self.check_item_description = check_item_description
        # The precheck result. Valid values:
        # 
        # *   **Success**
        # *   **Failed**
        self.check_result = check_result
        # The error message returned if the task failed to pass the precheck.
        # 
        # >  This parameter is returned only if the value of the **CheckResult** parameter is **Failed**.
        self.failed_reason = failed_reason
        # The method to fix the precheck failure.
        # 
        # >  This parameter is returned only if the value of the **CheckResult** parameter is **Failed**.
        self.repair_method = repair_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        if self.check_item_description is not None:
            result['CheckItemDescription'] = self.check_item_description

        if self.check_result is not None:
            result['CheckResult'] = self.check_result

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

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

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('RepairMethod') is not None:
            self.repair_method = m.get('RepairMethod')

        return self

class DescribeDtsJobsResponseBodyDtsJobListPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The size of data that is migrated or synchronized per second. Unit: MB/s.
        self.flow = flow
        # The number of times that SQL statements are migrated or synchronized per second, including BEGIN, COMMIT, DML, and DDL statements. DML statements include INSERT, DELETE, and UPDATE.
        self.rps = rps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow is not None:
            result['Flow'] = self.flow

        if self.rps is not None:
            result['Rps'] = self.rps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flow') is not None:
            self.flow = m.get('Flow')

        if m.get('Rps') is not None:
            self.rps = m.get('Rps')

        return self

class DescribeDtsJobsResponseBodyDtsJobListMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        full_data_check: bool = None,
        inc_data_check: bool = None,
        structure_data_check: bool = None,
        structure_initialization: bool = None,
    ):
        # Indicates whether full data migration or synchronization is performed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.data_initialization = data_initialization
        # Indicates whether incremental data migration or synchronization is performed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.data_synchronization = data_synchronization
        # Indicates whether full data verification is performed. Valid values:
        # -  **true**: yes
        # -  **false**: no
        self.full_data_check = full_data_check
        # Indicates whether incremental data verification is performed. Valid values:
        # -  **true**: yes
        # -  **false**: no
        self.inc_data_check = inc_data_check
        self.structure_data_check = structure_data_check
        # Indicates whether schema migration or schema synchronization is performed. Valid values:
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

        if self.full_data_check is not None:
            result['FullDataCheck'] = self.full_data_check

        if self.inc_data_check is not None:
            result['IncDataCheck'] = self.inc_data_check

        if self.structure_data_check is not None:
            result['StructureDataCheck'] = self.structure_data_check

        if self.structure_initialization is not None:
            result['StructureInitialization'] = self.structure_initialization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInitialization') is not None:
            self.data_initialization = m.get('DataInitialization')

        if m.get('DataSynchronization') is not None:
            self.data_synchronization = m.get('DataSynchronization')

        if m.get('FullDataCheck') is not None:
            self.full_data_check = m.get('FullDataCheck')

        if m.get('IncDataCheck') is not None:
            self.inc_data_check = m.get('IncDataCheck')

        if m.get('StructureDataCheck') is not None:
            self.structure_data_check = m.get('StructureDataCheck')

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        return self

class DescribeDtsJobsResponseBodyDtsJobListIncDataCheckStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if the task failed.
        self.error_message = error_message
        # The progress of the incremental data verification task. Unit: percentage.
        self.percent = percent
        # The progress of the incremental data verification task.
        self.progress = progress
        # The state of the incremental data verification task. Valid values:
        # 
        # - **Catched**: The verification is delayed. 
        # - **NotStarted**: The verification is not started. 
        # - **Checking**: The verification is in progress. 
        # - **Failed**: The verification failed.
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

class DescribeDtsJobsResponseBodyDtsJobListFullDataCheckStatus(DaraModel):
    def __init__(
        self,
        can_switch: bool = None,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.can_switch = can_switch
        # The error message returned if the task failed.
        self.error_message = error_message
        # The progress of the full data verification task. Unit: percentage.
        self.percent = percent
        # The progress of the full data verification task.
        self.progress = progress
        # The state of the full data verification task. Valid values:
        # 
        # - **NotStarted**: The verification is not started. 
        # - **Checking**: The verification is in progress. 
        # - **Failed**: The verification failed. 
        # - **Finished**: The verification is complete.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_switch is not None:
            result['CanSwitch'] = self.can_switch

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
        if m.get('CanSwitch') is not None:
            self.can_switch = m.get('CanSwitch')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyDtsJobListErrorDetails(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        help_url: str = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The URL of the documentation.
        self.help_url = help_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.help_url is not None:
            result['HelpUrl'] = self.help_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')

        return self

class DescribeDtsJobsResponseBodyDtsJobListDestinationEndpoint(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        engine_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        oracle_sid: str = None,
        port: str = None,
        region: str = None,
        ssl_solution_enum: str = None,
        user_name: str = None,
    ):
        # The name of the database to which the migration object in the destination instance belongs.
        self.database_name = database_name
        # The database type of the destination instance.
        self.engine_name = engine_name
        # The ID of the destination instance.
        self.instance_id = instance_id
        # The type of the destination instance.
        self.instance_type = instance_type
        # The endpoint of the destination instance.
        self.ip = ip
        # The SID of the Oracle database.
        # 
        # >  This parameter is returned only if the **EngineName** parameter of the destination instance is set to **Oracle** and the Oracle database is deployed in a non-RAC architecture.
        self.oracle_sid = oracle_sid
        # The database service port of the destination instance.
        self.port = port
        # The ID of the region in which the destination instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether SSL encryption is enabled. Valid values:
        # 
        # *   **DISABLE**: SSL encryption is disabled.
        # *   **ENABLE_WITH_CERTIFICATE**: SSL encryption is enabled, and the CA certificate is uploaded.
        # *   **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL encryption is enabled for the connection to an AWS MongoDB Altas database.
        # *   **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to encrypt the connection to a Kafka cluster.
        self.ssl_solution_enum = ssl_solution_enum
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

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.oracle_sid is not None:
            result['OracleSID'] = self.oracle_sid

        if self.port is not None:
            result['Port'] = self.port

        if self.region is not None:
            result['Region'] = self.region

        if self.ssl_solution_enum is not None:
            result['SslSolutionEnum'] = self.ssl_solution_enum

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('OracleSID') is not None:
            self.oracle_sid = m.get('OracleSID')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SslSolutionEnum') is not None:
            self.ssl_solution_enum = m.get('SslSolutionEnum')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeDtsJobsResponseBodyDtsJobListDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if incremental data migration or synchronization failed.
        self.error_message = error_message
        # Indicates whether the instance needs to be upgraded. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        # 
        # >  To upgrade a DTS instance, call the [TransferInstanceClass](https://help.aliyun.com/document_detail/281093.html) operation.
        self.need_upgrade = need_upgrade
        # The progress of incremental data migration or synchronization.
        self.percent = percent
        # The number of records that have been migrated or synchronized during incremental data migration or synchronization.
        self.progress = progress
        # The state of incremental data migration or synchronization. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Migrating**: The task is in progress.
        # *   **Failed**: The task failed.
        # *   **Finished**: The task is complete.
        # *   **Catched**: The task is not delayed.
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

        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade

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

        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeDtsJobsResponseBodyDtsJobListDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if full data synchronization failed.
        self.error_message = error_message
        # The progress of full data synchronization. This is expressed as a percentage.
        self.percent = percent
        # The number of records that have been synchronized during full data synchronization.
        self.progress = progress
        # The state of full data synchronization. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Migrating**: The task is in progress.
        # *   **Failed**: The task failed.
        # *   **Finished**: The task is complete.
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

class DescribeDtsJobsResponseBodyDtsJobListDataEtlStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if the task failed.
        self.error_message = error_message
        # The progress of the ETL task.
        self.percent = percent
        # The number of records that have been processed by the ETL task.
        self.progress = progress
        # The state of the ETL task. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Migrating**: The task is in progress.
        # *   **Failed**: The task failed.
        # *   **Finished**: The task is complete.
        # *   **Catched**: The task is not delayed.
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

class DescribeDtsJobsResponseBodyDtsJobListDataCloudStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned if the task failed.
        self.error_message = error_message
        # Indicates whether the instance needs to be upgraded. Valid values:
        # 
        # - **true** 
        # - **false**
        self.need_upgrade = need_upgrade
        # The progress of the task. Unit: percentage.
        self.percent = percent
        # The number of tables that have been migrated.
        self.progress = progress
        # The state of the task. For more information about the valid values, see the description of the request parameter **Status**.
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

        if self.need_upgrade is not None:
            result['NeedUpgrade'] = self.need_upgrade

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

        if m.get('NeedUpgrade') is not None:
            self.need_upgrade = m.get('NeedUpgrade')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

