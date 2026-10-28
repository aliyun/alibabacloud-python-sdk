# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeGadInstanceDtsMembersResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        db_engine_type: str = None,
        dts_job_list: List[main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobList] = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        instance_id: str = None,
        instance_name: str = None,
        page_number: int = None,
        page_record_count: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The database engine.
        self.db_engine_type = db_engine_type
        # The list of tasks and the execution details of each task.
        self.dts_job_list = dts_job_list
        # The dynamic error code. This parameter will be deprecated soon.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace the **%s** in the **ErrMessage** response parameter.
        # 
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, the specified request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned when the call fails.
        self.err_code = err_code
        # The error message returned when a call error occurs.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the active-active instance group.
        self.instance_id = instance_id
        # The name of the active-active instance group.
        self.instance_name = instance_name
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_record_count = page_record_count
        # The region ID of the instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The status of the active geo-redundancy instance group.
        self.status = status
        # Indicates whether the request is successful. Valid values:
        # - **true**: The request is successful.
        # - **false**: The request fails.
        self.success = success
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.dts_job_list:
            for v1 in self.dts_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_engine_type is not None:
            result['DbEngineType'] = self.db_engine_type

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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbEngineType') is not None:
            self.db_engine_type = m.get('DbEngineType')

        self.dts_job_list = []
        if m.get('DtsJobList') is not None:
            for k1 in m.get('DtsJobList'):
                temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobList()
                self.dts_job_list.append(temp_model.from_map(k1))

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeGadInstanceDtsMembersResponseBodyDtsJobList(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        begin_timestamp: str = None,
        checkpoint: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        cpu_usage: str = None,
        create_time: str = None,
        data_cloud_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataCloudStatus = None,
        data_etl_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataEtlStatus = None,
        data_initialization_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataSynchronizationStatus = None,
        db_object: str = None,
        dedicated_cluster_id: str = None,
        delay: int = None,
        destination_endpoint: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDestinationEndpoint = None,
        dts_bis_label: str = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        du_usage: int = None,
        end_timestamp: str = None,
        error_details: List[main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListErrorDetails] = None,
        error_message: str = None,
        etl_safe_checkpoint: str = None,
        expire_time: str = None,
        full_data_check_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListFullDataCheckStatus = None,
        inc_data_check_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListIncDataCheckStatus = None,
        job_type: str = None,
        max_du: float = None,
        mem_usage: str = None,
        migration_err_code: str = None,
        migration_err_help_doc_id: str = None,
        migration_err_help_doc_key: str = None,
        migration_err_msg: str = None,
        migration_err_type: str = None,
        migration_err_workaround: str = None,
        migration_mode: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListMigrationMode = None,
        min_du: float = None,
        origin_type: str = None,
        pay_type: str = None,
        performance: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListPerformance = None,
        precheck_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListPrecheckStatus = None,
        reserved: str = None,
        resource_group_display_name: str = None,
        resource_group_id: str = None,
        retry_state: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListRetryState = None,
        reverse_job: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJob = None,
        source_endpoint: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListStructureInitializationStatus = None,
        tag_list: List[main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListTagList] = None,
    ):
        # The application name.
        self.app_name = app_name
        # The start time of the timestamp range saved in the change tracking instance, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is in UTC.
        self.begin_timestamp = begin_timestamp
        # The checkpoint.
        self.checkpoint = checkpoint
        # The downstream consumption checkpoint of the change tracking instance, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is in UTC.
        self.consumption_checkpoint = consumption_checkpoint
        # The downstream consumption client information, which consists of the IP address and a random number generated by DTS.
        self.consumption_client = consumption_client
        # The current CPU utilization of the instance. Unit: %.
        self.cpu_usage = cpu_usage
        # The task creation time, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is in UTC.
        self.create_time = create_time
        # The status of the physical migration to the cloud task.
        self.data_cloud_status = data_cloud_status
        # The status of the ETL task.
        # > This parameter collection is returned only after an ETL task is configured.
        self.data_etl_status = data_etl_status
        # The status of full data migration or initial data synchronization.
        self.data_initialization_status = data_initialization_status
        # The status of incremental data migration or synchronization.
        self.data_synchronization_status = data_synchronization_status
        # The migration, synchronization, or change tracking objects. For more information about the definitions, see [Description of migration, synchronization, or change tracking objects](https://help.aliyun.com/document_detail/209545.html).
        self.db_object = db_object
        # The ID of the dedicated DTS cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The latency of incremental data migration or synchronization.
        # > If you query a data migration task, the unit of this parameter is milliseconds. If you query a data synchronization task, the unit of this parameter is seconds.
        self.delay = delay
        # The connection information of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The environment tag of the DTS instance. Valid values:
        # 
        # - **normal**: Normal.
        # - **online**: Online.
        self.dts_bis_label = dts_bis_label
        # The ID of the data migration, data synchronization, or subscribe instance.
        self.dts_instance_id = dts_instance_id
        # The link specifications.
        # > For more information about the specifications and performance tests of each link, see [Specifications for data migration links](https://help.aliyun.com/document_detail/26606.html) and [Specifications for data synchronization links](https://help.aliyun.com/document_detail/26605.html).
        self.dts_job_class = dts_job_class
        # The synchronization direction. Valid values:
        # - **Forward**: Forward.
        # - **Reverse**: Reverse.
        # 
        # > This parameter is returned only when the topology of the data synchronization instance is two-way synchronization.
        self.dts_job_direction = dts_job_direction
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The name of the DTS task.
        self.dts_job_name = dts_job_name
        # The used resources of the dedicated DTS cluster. Unit: DU.
        self.du_usage = du_usage
        # The end backup timestamp.
        self.end_timestamp = end_timestamp
        # The error details.
        self.error_details = error_details
        # The error message for a failed task.
        self.error_message = error_message
        # The safe checkpoint of the ETL task.
        self.etl_safe_checkpoint = etl_safe_checkpoint
        # The expiration time of the instance, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is in UTC.
        # > This parameter is returned only when the **PayType** parameter is set to **PrePaid**.
        self.expire_time = expire_time
        # The status information of full data verification.
        self.full_data_check_status = full_data_check_status
        # The status information of incremental data verification.
        self.inc_data_check_status = inc_data_check_status
        # The DTS task type.
        self.job_type = job_type
        # The DU upper limit of the serverless instance.
        self.max_du = max_du
        # The used memory. Unit: MB.
        self.mem_usage = mem_usage
        # The error code.
        self.migration_err_code = migration_err_code
        # The ID of the help document for the error code.
        self.migration_err_help_doc_id = migration_err_help_doc_id
        # The key of the help document for the error code.
        self.migration_err_help_doc_key = migration_err_help_doc_key
        # The error message.
        self.migration_err_msg = migration_err_msg
        # The type of the error code.
        self.migration_err_type = migration_err_type
        # The error workaround.
        self.migration_err_workaround = migration_err_workaround
        # The migration type or initial synchronization type.
        self.migration_mode = migration_mode
        # The minimum number of DUs for the serverless instance.
        self.min_du = min_du
        # The source of the task. Valid values:
        # 
        # - **PTS task**
        # - **DMS task**
        # - **DTS task**
        self.origin_type = origin_type
        # The billing method of the instance. Valid values:
        # 
        # - **PrePaid**: Subscription.
        # - **PostPaid**: Pay-as-you-go.
        self.pay_type = pay_type
        # The performance information of the migration or synchronization link.
        self.performance = performance
        # The precheck status.
        self.precheck_status = precheck_status
        # The reserved parameter for DTS. The value is a JSON string. You can specify this parameter to meet special requirements, such as whether to automatically start the precheck. For more information, see [MigrationReserved parameter description](https://help.aliyun.com/document_detail/176470.html).
        self.reserved = reserved
        # The name of the resource group.
        self.resource_group_display_name = resource_group_display_name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The retry state of DTS due to a task exception.
        self.retry_state = retry_state
        # The execution details of the reverse synchronization task.
        # > This parameter collection is returned only when the task is a data synchronization task and the topology type is two-way.
        self.reverse_job = reverse_job
        # The connection information of the source instance.
        self.source_endpoint = source_endpoint
        # The DTS instance status. Valid values:
        # 
        # Status of a data migration node:
        # - **NotStarted**: The node is not started.
        # - **Prechecking**: The precheck is in progress.
        # - **PrecheckFailed**: The precheck failed.
        # - **PreCheckPass**: The precheck passed.
        # - **NotConfigured**: The node is not configured.
        # - **Migrating**: The migration is in progress.
        # - **Suspending**: The node is being paused.
        # - **MigrationFailed**: The migration failed.
        # - **Finished**: The node is completed.
        # - **Retrying**: The node is being retried.
        # - **Upgrade**: The node is being upgraded.
        # - **Locked**: The node is locked.
        # - **Downgrade**: The node is being downgraded.
        # 
        # Status of a data synchronization node:
        # - **NotStarted**: The node is not started.
        # - **Prechecking**: The precheck is in progress.
        # - **PrecheckFailed**: The precheck failed.
        # - **PreCheckPass**: The precheck passed.
        # - **NotConfigured**: The node is not configured.
        # - **Initializing**: Initial synchronization is in progress.
        # - **InitializeFailed**: Initial synchronization failed.
        # - **Synchronizing**: Data synchronization is in progress.
        # - **Failed**: The synchronization failed.
        # - **Suspending**: The node is being paused.
        # - **Modifying**: The synchronization objects are being modified.
        # - **Finished**: The node is completed.
        # - **Retrying**: The node is being retried.
        # - **Upgrade**: The node is being upgraded.
        # - **Locked**: The node is locked.
        # - **Downgrade**: The node is being downgraded.
        # 
        # Status of a subscribe node:
        # - **NotConfigured**: The node is not configured.
        # - **NotStarted**: The node is not started.
        # - **Prechecking**: The precheck is in progress.
        # - **PrecheckFailed**: The precheck failed.
        # - **PreCheckPass**: The precheck passed.
        # - **Starting**: The node is being started.
        # - **Normal**: The node is running normally.
        # - **Retrying**: The node is being retried.
        # - **Abnormal**: The node is abnormal.
        # - **Upgrade**: The node is being upgraded.
        # - **Locked**: The node is locked.
        # - **Downgrade**: The node is being downgraded.
        self.status = status
        # The status of schema migration or initial schema synchronization.
        self.structure_initialization_status = structure_initialization_status
        # The list of tags.
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
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataCloudStatus()
            self.data_cloud_status = temp_model.from_map(m.get('DataCloudStatus'))

        if m.get('DataEtlStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataEtlStatus()
            self.data_etl_status = temp_model.from_map(m.get('DataEtlStatus'))

        if m.get('DataInitializationStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListDestinationEndpoint()
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

        if m.get('DuUsage') is not None:
            self.du_usage = m.get('DuUsage')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        self.error_details = []
        if m.get('ErrorDetails') is not None:
            for k1 in m.get('ErrorDetails'):
                temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListErrorDetails()
                self.error_details.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EtlSafeCheckpoint') is not None:
            self.etl_safe_checkpoint = m.get('EtlSafeCheckpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FullDataCheckStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListFullDataCheckStatus()
            self.full_data_check_status = temp_model.from_map(m.get('FullDataCheckStatus'))

        if m.get('IncDataCheckStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListIncDataCheckStatus()
            self.inc_data_check_status = temp_model.from_map(m.get('IncDataCheckStatus'))

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
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('OriginType') is not None:
            self.origin_type = m.get('OriginType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('ResourceGroupDisplayName') is not None:
            self.resource_group_display_name = m.get('ResourceGroupDisplayName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RetryState') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListRetryState()
            self.retry_state = temp_model.from_map(m.get('RetryState'))

        if m.get('ReverseJob') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJob()
            self.reverse_job = temp_model.from_map(m.get('ReverseJob'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListTagList()
                self.tag_list.append(temp_model.from_map(k1))

        return self

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListTagList(DaraModel):
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListStructureInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message returned when schema migration or initial schema synchronization fails.
        self.error_message = error_message
        # The progress of schema migration or initial schema synchronization, in percentage.
        self.percent = percent
        # The number of tables for which schema migration or initial schema synchronization is completed.
        self.progress = progress
        # The status of schema migration or initial schema synchronization.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListSourceEndpoint(DaraModel):
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
        # The name of the database to which the migration objects in the source instance belong.
        self.database_name = database_name
        # The database type of the source instance.
        self.engine_name = engine_name
        # The source instance ID.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
        # The endpoint of the source instance.
        self.ip = ip
        # The SID of the Oracle database.
        # > This parameter is returned only when the **EngineName** parameter of the source instance is set to **Oracle** and the Oracle database is a non-RAC instance.
        self.oracle_sid = oracle_sid
        # The database service port of the source instance.
        self.port = port
        # The region where the source instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether an SSL-secured connection is used. Valid values:
        # 
        # - **DISABLE**: SSL-secured connections are not used.
        # - **ENABLE_WITH_CERTIFICATE**: SSL-secured connections are used, and a CA certificate is uploaded.
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL-secured connections to AWS MongoDB Atlas are used.
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to connect to Kafka.
        self.ssl_solution_enum = ssl_solution_enum
        # The username.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJob(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        cpu_usage: str = None,
        create_time: str = None,
        data_initialization_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDataInitializationStatus = None,
        data_synchronization_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDataSynchronizationStatus = None,
        db_object: str = None,
        dedicated_cluster_id: str = None,
        delay: int = None,
        destination_endpoint: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDestinationEndpoint = None,
        dts_instance_id: str = None,
        dts_job_class: str = None,
        dts_job_direction: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        du_usage: int = None,
        error_details: List[main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobErrorDetails] = None,
        error_message: str = None,
        etl_safe_checkpoint: str = None,
        expire_time: str = None,
        full_data_check_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobFullDataCheckStatus = None,
        inc_data_check_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobIncDataCheckStatus = None,
        max_du: float = None,
        mem_usage: str = None,
        migration_mode: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobMigrationMode = None,
        min_du: float = None,
        pay_type: str = None,
        performance: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPerformance = None,
        precheck_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPrecheckStatus = None,
        reserved: str = None,
        source_endpoint: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobSourceEndpoint = None,
        status: str = None,
        structure_initialization_status: main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobStructureInitializationStatus = None,
    ):
        # The checkpoint for incremental data synchronization. The value is a UNIX timestamp, in seconds.
        self.checkpoint = checkpoint
        # The current CPU utilization of the instance. Unit: %.
        self.cpu_usage = cpu_usage
        # The task creation time, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is in UTC.
        self.create_time = create_time
        # The status of initial full data synchronization.
        self.data_initialization_status = data_initialization_status
        # The status of incremental data synchronization.
        self.data_synchronization_status = data_synchronization_status
        # The schema definition of the synchronized objects. The value is a JSON string and supports specific regular expressions. For more information and examples, see the object configuration instructions for migration, synchronization, or change tracking.
        self.db_object = db_object
        # The ID of the dedicated DTS cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The latency, in seconds.
        self.delay = delay
        # The connection information of the destination instance.
        self.destination_endpoint = destination_endpoint
        # The instance ID of the data synchronization instance.
        self.dts_instance_id = dts_instance_id
        # The specifications of the synchronization link.
        # > For more information about the specifications and performance test results of each link, see [Specifications of data synchronization links](https://help.aliyun.com/document_detail/26605.html).
        self.dts_job_class = dts_job_class
        # The description of the DTS task.
        self.dts_job_direction = dts_job_direction
        # The ID of the synchronization task.
        self.dts_job_id = dts_job_id
        # The name of the DTS task.
        self.dts_job_name = dts_job_name
        # The used resources of the dedicated DTS cluster. Unit: DU.
        self.du_usage = du_usage
        # The error details.
        self.error_details = error_details
        # The error message for a failed task.
        self.error_message = error_message
        # The safe checkpoint of the ETL task.
        self.etl_safe_checkpoint = etl_safe_checkpoint
        # The expiration time of the instance, in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format. The time is in UTC.
        # > This parameter is returned only when the **PayType** parameter is set to **PrePaid**.
        self.expire_time = expire_time
        # The status information of full data verification.
        self.full_data_check_status = full_data_check_status
        # The status information of incremental data verification.
        self.inc_data_check_status = inc_data_check_status
        # The DU upper limit of the serverless instance.
        self.max_du = max_du
        # The amount of used memory, in MB.
        self.mem_usage = mem_usage
        # The type of initial synchronization.
        self.migration_mode = migration_mode
        # The minimum number of DUs for the serverless instance.
        self.min_du = min_du
        # The billing method of the instance. Valid values:
        # 
        # - **PrePaid**: Subscription.
        # - **PostPaid**: Pay-as-you-go.
        self.pay_type = pay_type
        # The performance information of the synchronization link.
        self.performance = performance
        # The precheck status.
        self.precheck_status = precheck_status
        # The reserved parameters of DTS. The value is a JSON string. You can specify this parameter to meet special requirements, such as specifying whether to automatically start the precheck. For more information, see [MigrationReserved parameter description](https://help.aliyun.com/document_detail/176470.html).
        self.reserved = reserved
        # The connection information of the source instance.
        self.source_endpoint = source_endpoint
        # The status of the reverse synchronization task.
        self.status = status
        # The status of initial schema synchronization.
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
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDataInitializationStatus()
            self.data_initialization_status = temp_model.from_map(m.get('DataInitializationStatus'))

        if m.get('DataSynchronizationStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDataSynchronizationStatus()
            self.data_synchronization_status = temp_model.from_map(m.get('DataSynchronizationStatus'))

        if m.get('DbObject') is not None:
            self.db_object = m.get('DbObject')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDestinationEndpoint()
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
                temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobErrorDetails()
                self.error_details.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EtlSafeCheckpoint') is not None:
            self.etl_safe_checkpoint = m.get('EtlSafeCheckpoint')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FullDataCheckStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobFullDataCheckStatus()
            self.full_data_check_status = temp_model.from_map(m.get('FullDataCheckStatus'))

        if m.get('IncDataCheckStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobIncDataCheckStatus()
            self.inc_data_check_status = temp_model.from_map(m.get('IncDataCheckStatus'))

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MemUsage') is not None:
            self.mem_usage = m.get('MemUsage')

        if m.get('MigrationMode') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobMigrationMode()
            self.migration_mode = temp_model.from_map(m.get('MigrationMode'))

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Performance') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPerformance()
            self.performance = temp_model.from_map(m.get('Performance'))

        if m.get('PrecheckStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPrecheckStatus()
            self.precheck_status = temp_model.from_map(m.get('PrecheckStatus'))

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StructureInitializationStatus') is not None:
            temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobStructureInitializationStatus()
            self.structure_initialization_status = temp_model.from_map(m.get('StructureInitializationStatus'))

        return self

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobStructureInitializationStatus(DaraModel):
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
        # The number of tables for which initial schema synchronization is completed.
        self.progress = progress
        # The status of initial schema synchronization.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobSourceEndpoint(DaraModel):
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
        # The name of the database to which the migration objects in the instance belong.
        self.database_name = database_name
        # The database type of the source instance.
        self.engine_name = engine_name
        # The source instance ID.
        self.instance_id = instance_id
        # The type of the source instance.
        self.instance_type = instance_type
        # The endpoint of the instance.
        self.ip = ip
        # The SID of the Oracle database.
        # > This parameter is returned only when the **EngineName** parameter of the source instance is set to **Oracle** and the Oracle database is a non-RAC instance.
        self.oracle_sid = oracle_sid
        # The database service port of the source instance.
        self.port = port
        # The region where the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether an SSL-secured connection is used. Valid values:
        # 
        # - **DISABLE**: SSL-secured connections are not used.
        # - **ENABLE_WITH_CERTIFICATE**: SSL-secured connections are used, and a CA certificate is uploaded.
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL-secured connections to AWS MongoDB Atlas are used.
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to connect to Kafka.
        self.ssl_solution_enum = ssl_solution_enum
        # The username.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The execution status of each precheck item.
        self.detail = detail
        # The error message for the precheck failure.
        self.error_message = error_message
        # The overall progress of the precheck, in percentage.
        self.percent = percent
        # The precheck status.
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
                temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        # The precheck item.
        self.check_item = check_item
        # The description of the precheck item.
        self.check_item_description = check_item_description
        # The precheck result. Valid values:
        # - **Success**: The item passed the precheck.
        # - **Failed**: The item failed the precheck.
        self.check_result = check_result
        # The error message returned when the precheck fails.
        self.failed_reason = failed_reason
        # The solution provided when the precheck fails.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The data synchronization traffic per second, in MB/s.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        full_data_check: bool = None,
        inc_data_check: bool = None,
        structure_initialization: bool = None,
    ):
        # Specifies whether to perform initial full data synchronization. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.data_initialization = data_initialization
        # Specifies whether to perform incremental data synchronization. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.data_synchronization = data_synchronization
        # Indicates whether full data validation is performed. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.full_data_check = full_data_check
        # Indicates whether incremental data validation is performed. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.inc_data_check = inc_data_check
        # Specifies whether to perform initial schema synchronization. Valid values:
        # - **true**: Yes.
        # - **false**: No.
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

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        return self

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobIncDataCheckStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for a failed task.
        self.error_message = error_message
        # The progress of the incremental data verification task. Unit: %.
        self.percent = percent
        # The completion progress of the incremental data verification task.
        self.progress = progress
        # The status information of incremental data verification.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobFullDataCheckStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for a failed task.
        self.error_message = error_message
        # The progress of the full data verification task. Unit: %.
        self.percent = percent
        # The completion progress of the full data verification task.
        self.progress = progress
        # The status information of full data verification.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobErrorDetails(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        help_url: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The URL of the help document.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDestinationEndpoint(DaraModel):
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
        # The name of the database to which the synchronized objects belong in the instance.
        self.database_name = database_name
        # The database engine type of the instance.
        self.engine_name = engine_name
        # The instance ID.
        self.instance_id = instance_id
        # The instance type.
        self.instance_type = instance_type
        # The endpoint of the instance.
        self.ip = ip
        # The SID of the Oracle database.
        # > This parameter is returned only when the **EngineName** parameter of the destination instance is set to **Oracle** and the Oracle database is a non-RAC instance.
        self.oracle_sid = oracle_sid
        # The database service port of the instance.
        self.port = port
        # The region where the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether an SSL-secured connection is used. Valid values:
        # 
        # - **DISABLE**: SSL-secured connections are not used.
        # - **ENABLE_WITH_CERTIFICATE**: SSL-secured connections are used, and a CA certificate is uploaded.
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL-secured connections to AWS MongoDB Atlas are used.
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to connect to Kafka.
        self.ssl_solution_enum = ssl_solution_enum
        # The username.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for the incremental data synchronization failure.
        self.error_message = error_message
        # Indicates whether the instance specifications need to be upgraded. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > To upgrade the instance specifications, call the [TransferInstanceClass](https://help.aliyun.com/document_detail/281093.html) operation.
        self.need_upgrade = need_upgrade
        # The progress of incremental data synchronization, in percentage.
        self.percent = percent
        # The number of records for which incremental data migration or synchronization is completed.
        self.progress = progress
        # The status of incremental data synchronization.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListReverseJobDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for the initial full data synchronization failure.
        self.error_message = error_message
        # The progress of initial full data synchronization, in percentage.
        self.percent = percent
        # The number of records for which initial full data synchronization is completed.
        self.progress = progress
        # The status of initial full data synchronization.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListRetryState(DaraModel):
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
        # The error message returned when a call error occurs.
        self.err_message = err_message
        # The task ID.
        self.job_id = job_id
        # The maximum retry time, in seconds.
        self.max_retry_time = max_retry_time
        # The error code.
        self.migration_err_code = migration_err_code
        # The ID of the help document for the error code.
        self.migration_err_help_doc_id = migration_err_help_doc_id
        # The key of the help document for the error code.
        self.migration_err_help_doc_key = migration_err_help_doc_key
        # The error message.
        self.migration_err_msg = migration_err_msg
        # The type of the error code.
        self.migration_err_type = migration_err_type
        # The error workaround.
        self.migration_err_workaround = migration_err_workaround
        # The instance progress.
        self.module = module
        # The number of retries.
        self.retry_count = retry_count
        # The retry target. Valid values:
        # 
        # - **srcDB**: The source database.
        # - **destDB**: The destination database.
        # - **inner_module**: The internal module of DTS.
        self.retry_target = retry_target
        # The elapsed retry time, in seconds.
        self.retry_time = retry_time
        # Indicates whether the task is being retried. Valid values:
        # - **true**: Yes.
        # - **false**: No.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListPrecheckStatus(DaraModel):
    def __init__(
        self,
        detail: List[main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListPrecheckStatusDetail] = None,
        error_message: str = None,
        percent: str = None,
        status: str = None,
    ):
        # The execution status of each precheck item.
        self.detail = detail
        # The error message for the precheck failure.
        self.error_message = error_message
        # The overall progress of the precheck, in percentage.
        self.percent = percent
        # The precheck status.
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
                temp_model = main_models.DescribeGadInstanceDtsMembersResponseBodyDtsJobListPrecheckStatusDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListPrecheckStatusDetail(DaraModel):
    def __init__(
        self,
        check_item: str = None,
        check_item_description: str = None,
        check_result: str = None,
        failed_reason: str = None,
        repair_method: str = None,
    ):
        # The precheck item.
        self.check_item = check_item
        # The description of the precheck item.
        self.check_item_description = check_item_description
        # The check result. Valid values:
        # - **Success**: The item passed the check.
        # - **Failed**: The item failed the check.
        self.check_result = check_result
        # The error message for the failed precheck.
        # > This parameter is returned only when the **CheckResult** parameter is set to **Failed**.
        self.failed_reason = failed_reason
        # The solution for the failed precheck.
        # > This parameter is returned only when the **CheckResult** parameter is set to **Failed**.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListPerformance(DaraModel):
    def __init__(
        self,
        flow: str = None,
        rps: str = None,
    ):
        # The data migration or synchronization traffic per second, in MB/s.
        self.flow = flow
        # The number of SQL statements migrated or synchronized per second, including BEGIN, COMMIT, DML statements (INSERT, DELETE, and UPDATE), and DDL statements.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListMigrationMode(DaraModel):
    def __init__(
        self,
        data_initialization: bool = None,
        data_synchronization: bool = None,
        full_data_check: bool = None,
        inc_data_check: bool = None,
        structure_initialization: bool = None,
    ):
        # Indicates whether full data migration or initial full data synchronization is performed. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.data_initialization = data_initialization
        # Indicates whether incremental data migration or synchronization is performed. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.data_synchronization = data_synchronization
        # Indicates whether full data validation is performed. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.full_data_check = full_data_check
        # Indicates whether incremental data validation is performed. Valid values:
        # - **true**: Yes.
        # - **false**: No.
        self.inc_data_check = inc_data_check
        # Indicates whether schema migration or initial schema synchronization is performed. Valid values:
        # - **true**: Yes.
        # - **false**: No.
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

        if m.get('StructureInitialization') is not None:
            self.structure_initialization = m.get('StructureInitialization')

        return self

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListIncDataCheckStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for a failed task.
        self.error_message = error_message
        # The progress of the incremental data verification task. Unit: %.
        self.percent = percent
        # The completion progress of the incremental data verification task.
        self.progress = progress
        # The status information of incremental data verification.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListFullDataCheckStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for a failed task.
        self.error_message = error_message
        # The progress of the full data verification task. Unit: %.
        self.percent = percent
        # The completion progress of the full data verification task.
        self.progress = progress
        # The status information of full data verification.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListErrorDetails(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        help_url: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The URL of the help document.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListDestinationEndpoint(DaraModel):
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
        # The name of the database to which the migration objects in the instance belong.
        self.database_name = database_name
        # The database engine type of the instance.
        self.engine_name = engine_name
        # The instance ID.
        self.instance_id = instance_id
        # The instance type.
        self.instance_type = instance_type
        # The endpoint of the instance.
        self.ip = ip
        # The SID of the Oracle database.
        # > This parameter is returned only when the **EngineName** parameter of the destination instance is set to **Oracle** and the Oracle database is a non-RAC instance.
        self.oracle_sid = oracle_sid
        # The database service port of the instance.
        self.port = port
        # The region where the instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Indicates whether an SSL-secured connection is used. Valid values:
        # 
        # - **DISABLE**: SSL-secured connections are not used.
        # - **ENABLE_WITH_CERTIFICATE**: SSL-secured connections are used, and a CA certificate is uploaded.
        # - **ENABLE_ONLY_4_MONGODB_ALTAS**: SSL-secured connections to AWS MongoDB Atlas are used.
        # - **ENABLE_ONLY_4_KAFKA_SCRAM_SHA_256**: SCRAM-SHA-256 is used to connect to Kafka.
        self.ssl_solution_enum = ssl_solution_enum
        # The username.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataSynchronizationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for failed incremental data migration or synchronization.
        self.error_message = error_message
        # Indicates whether the instance specifications need to be upgraded. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        # 
        # > To upgrade the instance specifications, call the [TransferInstanceClass](https://help.aliyun.com/document_detail/281093.html) operation.
        self.need_upgrade = need_upgrade
        # The progress of incremental data migration or synchronization. Unit: %.
        self.percent = percent
        # The number of records for which incremental data migration or synchronization is completed.
        self.progress = progress
        # The log level of the log information. Multiple statuses are separated by commas (,). Valid values:
        # 
        # - **NORMAL**: Normal.
        # - **WARN**: Warning.
        # - **ERROR**: Error.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataInitializationStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for failed full data migration or initial data synchronization.
        self.error_message = error_message
        # The progress of full data migration or initial data synchronization. Unit: %.
        self.percent = percent
        # The number of records for which full data migration or initial data synchronization is completed.
        self.progress = progress
        # The status of full data migration or initial data synchronization.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataEtlStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for a failed ETL task.
        self.error_message = error_message
        # The ETL task progress. Unit: %.
        self.percent = percent
        # The number of records for which the ETL task is completed.
        self.progress = progress
        # The log level of the log information. Multiple statuses are separated by commas (,). Valid values:
        # 
        # - **NORMAL**: Normal.
        # - **WARN**: Warning.
        # - **ERROR**: Error.
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

class DescribeGadInstanceDtsMembersResponseBodyDtsJobListDataCloudStatus(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        need_upgrade: bool = None,
        percent: str = None,
        progress: str = None,
        status: str = None,
    ):
        # The error message for a failed task.
        self.error_message = error_message
        # Indicates whether the instance specifications need to be upgraded. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.need_upgrade = need_upgrade
        # The task progress. Unit: %.
        self.percent = percent
        # The number of tables that have been migrated.
        self.progress = progress
        # The status of the physical migration to the cloud task.
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

