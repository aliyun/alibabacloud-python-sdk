# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudbenchTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCloudbenchTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The returned status code.
        self.code = code
        # The detailed information, including the total number of entries and error codes.
        self.data = data
        # The returned message.
        # >If the request is successful, **Successful** is returned. If the request fails, an error message is returned, such as an error code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.
        # - **false**: The request fails.
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
            temp_model = main_models.DescribeCloudbenchTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudbenchTaskResponseBodyData(DaraModel):
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
        # The name of the archived OSS table.
        self.archive_oss_table_name = archive_oss_table_name
        # The SQL archiving state. Valid values:
        # 
        # - **0**: not started.
        # - **1**: completed.
        # - **2**: error.
        # - **3**: running.
        # - **4**: no download required.
        self.archive_state = archive_state
        # The backup set ID. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to obtain the backup set ID.
        self.backup_id = backup_id
        # The backup type. Valid values:
        # 
        # - **TIMESTAMP**: by backup time.
        # - **BACKUPID**: by backup set ID.
        self.backup_type = backup_type
        # The substep of the stress testing task. Valid values:
        # 
        # - **NEW**: task initialization.
        # - **WAIT_BUY_ECS**: purchasing an ECS instance.
        # - **WAIT_START_ECS**: starting the ECS instance.
        # - **WAIT_INSTALL_JDK**: installing JDK.
        # - **WAIT_INSTALL_DBGATEWAY**: installing DBGateway.
        # - **ADD_SECURITY_IPS_STEP**: configuring the security group whitelist.
        # - **ARCHIVE**: archiving full SQL.
        # - **DOWNLOAD**: downloading the full SQL file.
        # - **PROCEED**: preprocessing the full SQL file.
        # - **PRE_LOAD**: preloading the full SQL file.
        # - **VALIDATE**: functional verification.
        # - **PRESSURE**: performance stress testing.
        self.bench_step = bench_step
        # The status of the stress testing substep. Valid values:
        # 
        # - **NEW**: task initialization.
        # - **RUNNING**: running.
        # - **FAILED**: failed.
        # - **FINISHED**: completed.
        # - **Terminated**: terminated.
        # - **Deleted**: deleted.
        self.bench_step_status = bench_step_status
        # The database gateway ID of the stress testing machine.
        self.client_gateway_id = client_gateway_id
        # The type of the stress testing machine. Valid values:
        # 
        # - **ECS**: You need to prepare the [Database Gateway](https://help.aliyun.com/document_detail/64905.html) on your own.
        # - **DAS_ECS**: an ECS instance automatically purchased and deployed by DAS.
        self.client_type = client_type
        # The description of the stress testing task.
        self.description = description
        # The unique identity of the target instance.
        self.dst_instance_uuid = dst_instance_uuid
        # The reserved parameter.
        self.dst_ip = dst_ip
        # The port of the target instance.
        self.dst_port = dst_port
        # The type of the target instance. Valid values:
        # - **Instance** (default): instance ID.
        # - **ConnectionString**: endpoint of the instance.
        self.dst_type = dst_type
        # The DTS task specification.
        self.dts_job_class = dts_job_class
        # The ID of the DTS migration task.
        self.dts_job_id = dts_job_id
        # The name of the Data Transmission Service (DTS) task.
        self.dts_job_name = dts_job_name
        # The DTS task state. Valid values:
        # 
        # - **NOT_STARTED**: not started.
        # - **PRE_CHECKING**: precheck in progress.
        # - **PRE_CHECK_FAILED**: precheck failed.
        # - **CHECKING**: checking.
        # - **MIGRATING**: migrating.
        # - **CATCHED**: caught up.
        # - **SUSPENDING**: suspending.
        # - **MIGRATION_FAILED**: migration failed.
        # - **FINISHED**: completed.
        # - **INITIALIZING**: synchronization initializing.
        # - **INITIALIZE_FAILED**: synchronization initialization failed.
        # - **SYNCHRONIZING**: synchronizing.
        # - **MODIFYING**: modifying synchronization objects.
        # - **SWITCHING**: switching.
        # - **FAILED**: failed.
        self.dts_job_state = dts_job_state
        # The DTS task state. Valid values:
        # 
        # - **NOT_STARTED**: not started.
        # - **PRE_CHECKING**: precheck in progress.
        # - **PRE_CHECK_FAILED**: precheck failed.
        # - **CHECKING**: checking.
        # - **MIGRATING**: migrating.
        # - **CATCHED**: caught up.
        # - **SUSPENDING**: suspending.
        # - **MIGRATION_FAILED**: migration failed.
        # - **FINISHED**: completed.
        # - **INITIALIZING**: synchronization initializing.
        # - **INITIALIZE_FAILED**: synchronization initialization failed.
        # - **SYNCHRONIZING**: synchronizing.
        # - **MODIFYING**: modifying synchronization objects.
        # - **SWITCHING**: switching.
        # - **FAILED**: failed.
        self.dts_job_status = dts_job_status
        # The ECS instance ID.
        self.ecs_instance_id = ecs_instance_id
        # The state after the stress testing task ends. Valid values:
        # 
        # - **WAIT_TARGET**: preparing the target instance for stress testing.
        # - **WAIT_DBGATEWAY**: preparing the stress testing deployment.
        # - **WAIT_SQL**: preparing full SQL.
        # - **WAIT_LOGIC**: preparing to start traffic replay.
        # 
        # >After the stress testing task executes the state specified by EndState, the task directly reaches the completed state.
        self.end_state = end_state
        # The error code returned by the internal stress testing task.
        self.error_code = error_code
        # The error message returned when the task fails.
        self.error_message = error_message
        # The additional information.
        self.external = external
        # The stress testing rate multiplier. The replay rate must be a positive integer. Valid values: **0** to **30**. Default value: **1**.
        self.rate = rate
        # The duration of the stress testing task.
        self.request_duration = request_duration
        # The generated stress testing duration. Unit: milliseconds.
        self.smart_pressure_time = smart_pressure_time
        # The task source. Valid values:
        # 
        # - **DAS**.
        # - **OPEN_API**.
        self.source = source
        # The reuse information of the full SQL.
        self.sql_complete_reuse = sql_complete_reuse
        # The database type of the source instance.
        self.src_instance_area = src_instance_area
        # The UUID of the source instance.
        self.src_instance_uuid = src_instance_uuid
        # The reserved parameter.
        self.src_public_ip = src_public_ip
        # The current state of the stress testing task. Valid values:
        # 
        # - **WAIT_TARGET**: preparing the target instance for stress testing.
        # - **WAIT_DBGATEWAY**: preparing the stress testing deployment.
        # - **WAIT_SQL**: preparing full SQL.
        # - **WAIT_LOGIC**: preparing to start traffic replay.
        self.state = state
        # The running status of the stress testing task. Valid values:
        # 
        # - **SUCCESS**: successful.
        # - **IGNORED**: ignored.
        # - **RUNNING**: running.
        # - **EXCEPTION**: abnormal.
        self.status = status
        # The table names involved in the stress testing task.
        self.table_schema = table_schema
        # The task ID.
        self.task_id = task_id
        # The type of the stress testing task. Valid values:
        # - **pressure test** (default): intelligent stress testing. The traffic captured from the target instance is replayed on the destination instance at the maximum speed supported by the destination instance specifications.
        # - **smart pressure test**: generated stress testing. By analyzing and learning the traffic captured from the target instance within a short period of time, traffic that is consistent with the business model and traffic distribution of the original traffic is generated for continuous stress testing. This reduces the time required to collect data from the target instance and lowers storage costs and performance overhead.
        self.task_type = task_type
        # The Kafka consumption topic.
        self.topic = topic
        # The Alibaba Cloud account ID.
        self.user_id = user_id
        # The version of the stress testing task. Valid values:
        # 
        # - **V2.0**
        # - **V3.0**
        self.version = version
        # The temporary directory generated by the stress testing task.
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

