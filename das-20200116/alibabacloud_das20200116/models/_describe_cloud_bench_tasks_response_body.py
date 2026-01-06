# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudBenchTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCloudBenchTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The detailed information, including the error codes and the number of entries that are returned.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeCloudBenchTasksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudBenchTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: str = None,
        list: main_models.DescribeCloudBenchTasksResponseBodyDataList = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The reserved parameter.
        self.extra = extra
        # The detailed information of the stress testing task.
        self.list = list
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.list:
            self.list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

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
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('List') is not None:
            temp_model = main_models.DescribeCloudBenchTasksResponseBodyDataList()
            self.list = temp_model.from_map(m.get('List'))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCloudBenchTasksResponseBodyDataList(DaraModel):
    def __init__(
        self,
        cloudbench_tasks: List[main_models.DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks] = None,
    ):
        self.cloudbench_tasks = cloudbench_tasks

    def validate(self):
        if self.cloudbench_tasks:
            for v1 in self.cloudbench_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cloudbenchTasks'] = []
        if self.cloudbench_tasks is not None:
            for k1 in self.cloudbench_tasks:
                result['cloudbenchTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloudbench_tasks = []
        if m.get('cloudbenchTasks') is not None:
            for k1 in m.get('cloudbenchTasks'):
                temp_model = main_models.DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks()
                self.cloudbench_tasks.append(temp_model.from_map(k1))

        return self

class DescribeCloudBenchTasksResponseBodyDataListCloudbenchTasks(DaraModel):
    def __init__(
        self,
        archive_job_id: str = None,
        archive_oss_table_name: str = None,
        archive_state: int = None,
        backup_id: str = None,
        backup_type: str = None,
        bench_step: str = None,
        bench_step_status: str = None,
        client_gateway_id: str = None,
        client_type: str = None,
        description: str = None,
        dst_instance_uuid: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        dts_job_state: int = None,
        dts_job_status: str = None,
        ecs_instance_id: str = None,
        end_state: str = None,
        error_code: str = None,
        error_message: str = None,
        external: str = None,
        rate: int = None,
        request_duration: int = None,
        smart_pressure_time: int = None,
        source: str = None,
        sql_complete_reuse: str = None,
        src_instance_area: str = None,
        src_instance_uuid: str = None,
        src_public_ip: str = None,
        state: str = None,
        status: str = None,
        table_schema: str = None,
        task_id: str = None,
        task_type: str = None,
        topic: str = None,
        user_id: str = None,
        version: str = None,
        work_dir: str = None,
    ):
        # The archiving task ID.
        self.archive_job_id = archive_job_id
        # The name of the table that was archived to Object Storage Service (OSS).
        self.archive_oss_table_name = archive_oss_table_name
        # The archiving status of the file that stores the analysis result of full SQL statistics. Valid values:
        # 
        # * **0**: The file archiving is not started.
        # * **1**: The file is archived.
        # * **2**: An error occurred.
        # * **3**: The file is being archived.
        # * **4**: The archived file does not need to be downloaded.
        self.archive_state = archive_state
        # The ID of the backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the ID of the backup set.
        self.backup_id = backup_id
        # The backup type. Valid values:
        # 
        # * **TIMESTAMP**: Data is restored to the state at a specific point in time.
        # * **BACKUPID**: Data is restored from a backup set that is identified by an ID.
        self.backup_type = backup_type
        # The substep in the stress testing task. Valid values:
        # 
        # * **NEW**: Initialize the stress testing task.
        # * **WAIT_BUY_ECS**: Purchase an ECS instance.
        # * **WAIT_START_ECS**: Start the ECS instance.
        # * **WAIT_INSTALL_JDK**: Install the Java Development Kit (JDK).
        # * **WAIT_INSTALL_DBGATEWAY**: Install the database gateway (DBGateway).
        # * **ADD_SECURITY_IPS_STEP**: Configure the whitelist of the security group.
        # * **ARCHIVE**: Archive the file that stores the analysis results of full SQL statistics.
        # * **DOWNLOAD**: Download the file that stores the analysis result of full SQL statistics.
        # * **PROCEED**: Preprocess the file that stores the analysis result of full SQL statistics.
        # * **PRE_LOAD**: Preload the file that stores the analysis result of full SQL statistics.
        # * **VALIDATE**: Verify the functionality of stress testing.
        # * **PRESSURE**: Start the stress testing task.
        self.bench_step = bench_step
        # The status that indicates the substep performed for the stress testing task. Valid values:
        # 
        # * **NEW**: The task is being initialized.
        # * **RUNNING**: The task is running.
        # * **FAILED**: The task failed.
        # * **FINISHED**: The task is complete.
        # * **Terminated**: The task is terminated.
        # * **Deleted**: The task is deleted.
        self.bench_step_status = bench_step_status
        # The DBGateway ID of the stress testing client.
        self.client_gateway_id = client_gateway_id
        # The type of the stress testing client. Valid values:
        # 
        # * **ECS**: indicates that you must prepare the DBGateway.
        # * **DAS_ECS**: indicates that DAS automatically purchases and deploys an ECS instance for stress testing.
        self.client_type = client_type
        # The description of the stress testing task.
        self.description = description
        # The UUID of the destination instance.
        self.dst_instance_uuid = dst_instance_uuid
        # The reserved parameter.
        self.dst_ip = dst_ip
        # The port number of the destination instance.
        self.dst_port = dst_port
        # The type of the identifier that is used to indicate the destination instance. Valid values:
        # 
        # * **Instance** (default): the instance ID.
        # * **ConnectionString**: the endpoint of the instance.
        self.dst_type = dst_type
        # The specification of the DTS instance.
        # 
        # > For more information about the specifications of DTS instances and the test performance of each instance, see [Specifications of data migration instances](https://help.aliyun.com/document_detail/26606.html).
        self.dts_job_class = dts_job_class
        # The ID of the DTS migration task.
        self.dts_job_id = dts_job_id
        # The name of the Data Transmission Service (DTS) migration task.
        self.dts_job_name = dts_job_name
        # The status of the DTS migration task. Valid values:
        # 
        # * **NOT_STARTED**: The task is not started.
        # * **PRE_CHECKING**: The task is in precheck.
        # * **PRE_CHECK_FAILED**: The precheck failed.
        # * **CHECKING**: The task is being checked.
        # * **MIGRATING**: The data is being migrated.
        # * **CATCHED**: The data is migrated from the source instance to the destination instance.
        # * **SUSPENDING**: The task is suspended.
        # * **MIGRATION_FAILED**: The data failed to be migrated.
        # * **FINISHED**: The task is complete.
        # * **INITIALIZING**: The synchronization is being initialized.
        # * **INITIALIZE_FAILED**: The synchronization failed to be initialized.
        # * **SYNCHRONIZING**: The data is being synchronized.
        # * **MODIFYING**: The roles of the instances are being changed.
        # * **SWITCHING**: The roles of the instances are being switched.
        # * **FAILED**: The task failed.
        self.dts_job_state = dts_job_state
        # The status of the DTS migration task. Valid values:
        # 
        # * **NOT_STARTED**: The task is not started.
        # * **PRE_CHECKING**: The task is in precheck.
        # * **PRE_CHECK_FAILED**: The precheck failed.
        # * **CHECKING**: The task is being checked.
        # * **MIGRATING**: The data is being migrated.
        # * **CATCHED**: The data is migrated from the source instance to the destination instance.
        # * **SUSPENDING**: The task is suspended.
        # * **MIGRATION_FAILED**: The data failed to be migrated.
        # * **FINISHED**: The task is complete.
        # * **INITIALIZING**: The synchronization is being initialized.
        # * **INITIALIZE_FAILED**: The synchronization failed to be initialized.
        # * **SYNCHRONIZING**: The data is being synchronized.
        # * **MODIFYING**: The roles of the instances are being changed.
        # * **SWITCHING**: The roles of the instances are being switched.
        # * **FAILED**: The task failed.
        self.dts_job_status = dts_job_status
        # The ID of the Elastic Compute Service (ECS) instance.
        self.ecs_instance_id = ecs_instance_id
        # The state that indicates the last operation performed for the stress testing task. Valid values:
        # 
        # * **WAIT_TARGET**: prepares the destination instance.
        # * **WAIT_DBGATEWAY**: prepares the DBGateway.
        # * **WAIT_SQL**: prepares the full SQL statistics.
        # * **WAIT_LOGIC**: prepares to replay the traffic.
        # 
        # > When the state of a stress testing task changes to the state that is specified by the EndState parameter, the stress testing task is complete.
        self.end_state = end_state
        # The error code returned for the substep of the stress testing task.
        self.error_code = error_code
        # The error message returned if the task failed.
        self.error_message = error_message
        # The additional information.
        self.external = external
        # The rate at which the stress testing task replayed the traffic. This value is a positive integer. Valid values: **0** to **30**. Default value: **1**.
        self.rate = rate
        # The duration of the stress testing task. Unit: millisecond.
        self.request_duration = request_duration
        # The duration of the stress testing task of the smart pressure test type. Unit: millisecond.
        self.smart_pressure_time = smart_pressure_time
        # The source of the task. Valid values:
        # 
        # * **DAS**
        # * **OPEN_API**
        self.source = source
        # The reused information about the analysis result of full SQL statistics.
        self.sql_complete_reuse = sql_complete_reuse
        # The database engine of the source instance. Valid values:
        self.src_instance_area = src_instance_area
        # The UUID of the source instance.
        self.src_instance_uuid = src_instance_uuid
        # The reserved parameter.
        self.src_public_ip = src_public_ip
        # The state that indicates the operation performed for the stress testing task. Valid values:
        # 
        # * **WAIT_TARGET**: prepares the destination instance.
        # * **WAIT_DBGATEWAY**: prepares the DBGateway.
        # * **WAIT_SQL**: prepares the full SQL statistics.
        # * **WAIT_LOGIC**: prepares to replay the traffic.
        self.state = state
        # The status of the stress testing task. Valid values:
        # 
        # * **SUCCESS**: The task was successful.
        # * **IGNORED**: The task was ignored.
        # * **RUNNING**: The task is running.
        # * **EXCEPTION**: The task is abnormal.
        self.status = status
        # The name of the table that is used for stress testing.
        self.table_schema = table_schema
        # The task ID.
        self.task_id = task_id
        # The type of the stress testing task. Valid values:
        # 
        # * **pressure test** (default): A task of this type replays the traffic that is captured from the source instance on the destination instance at the maximum playback rate that is supported by the destination instance.
        # * **smart pressure test**: A task of this type analyzes the traffic that is captured from the source instance over a short period of time and generates traffic on the destination instance for continuous stress testing. The business model based on which the traffic is generated on the destination instance and the traffic distribution are consistent with those on the source instance. Stress testing tasks of this type can help you reduce the amount of time that is consumed to collect data from the source instance and reduce storage costs and performance overheads.
        self.task_type = task_type
        # The topic that contains the consumed data. This topic is a topic in Message Queue for Apache Kafka.
        self.topic = topic
        # The Alibaba Cloud account ID.
        self.user_id = user_id
        # The version of the stress testing task. Valid values:
        # 
        # * **V2.0**
        # * **V3.0**
        self.version = version
        # The path of the temporary directory that is generated for stress testing.
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.archive_job_id is not None:
            result['ArchiveJobId'] = self.archive_job_id

        if self.archive_oss_table_name is not None:
            result['ArchiveOssTableName'] = self.archive_oss_table_name

        if self.archive_state is not None:
            result['ArchiveState'] = self.archive_state

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bench_step is not None:
            result['BenchStep'] = self.bench_step

        if self.bench_step_status is not None:
            result['BenchStepStatus'] = self.bench_step_status

        if self.client_gateway_id is not None:
            result['ClientGatewayId'] = self.client_gateway_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.description is not None:
            result['Description'] = self.description

        if self.dst_instance_uuid is not None:
            result['DstInstanceUuid'] = self.dst_instance_uuid

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.dts_job_state is not None:
            result['DtsJobState'] = self.dts_job_state

        if self.dts_job_status is not None:
            result['DtsJobStatus'] = self.dts_job_status

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.end_state is not None:
            result['EndState'] = self.end_state

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.external is not None:
            result['External'] = self.external

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration

        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time

        if self.source is not None:
            result['Source'] = self.source

        if self.sql_complete_reuse is not None:
            result['SqlCompleteReuse'] = self.sql_complete_reuse

        if self.src_instance_area is not None:
            result['SrcInstanceArea'] = self.src_instance_area

        if self.src_instance_uuid is not None:
            result['SrcInstanceUuid'] = self.src_instance_uuid

        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.version is not None:
            result['Version'] = self.version

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArchiveJobId') is not None:
            self.archive_job_id = m.get('ArchiveJobId')

        if m.get('ArchiveOssTableName') is not None:
            self.archive_oss_table_name = m.get('ArchiveOssTableName')

        if m.get('ArchiveState') is not None:
            self.archive_state = m.get('ArchiveState')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('BenchStep') is not None:
            self.bench_step = m.get('BenchStep')

        if m.get('BenchStepStatus') is not None:
            self.bench_step_status = m.get('BenchStepStatus')

        if m.get('ClientGatewayId') is not None:
            self.client_gateway_id = m.get('ClientGatewayId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DstInstanceUuid') is not None:
            self.dst_instance_uuid = m.get('DstInstanceUuid')

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('DtsJobState') is not None:
            self.dts_job_state = m.get('DtsJobState')

        if m.get('DtsJobStatus') is not None:
            self.dts_job_status = m.get('DtsJobStatus')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('External') is not None:
            self.external = m.get('External')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')

        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SqlCompleteReuse') is not None:
            self.sql_complete_reuse = m.get('SqlCompleteReuse')

        if m.get('SrcInstanceArea') is not None:
            self.src_instance_area = m.get('SrcInstanceArea')

        if m.get('SrcInstanceUuid') is not None:
            self.src_instance_uuid = m.get('SrcInstanceUuid')

        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TableSchema') is not None:
            self.table_schema = m.get('TableSchema')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        return self

