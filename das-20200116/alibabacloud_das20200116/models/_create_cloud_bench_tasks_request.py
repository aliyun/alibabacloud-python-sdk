# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudBenchTasksRequest(DaraModel):
    def __init__(
        self,
        amount: str = None,
        backup_id: str = None,
        backup_time: str = None,
        client_type: str = None,
        description: str = None,
        dst_connection_string: str = None,
        dst_instance_id: str = None,
        dst_port: str = None,
        dst_super_account: str = None,
        dst_super_password: str = None,
        dst_type: str = None,
        dts_job_class: str = None,
        dts_job_id: str = None,
        end_state: str = None,
        gateway_vpc_id: str = None,
        gateway_vpc_ip: str = None,
        rate: str = None,
        request_duration: str = None,
        request_end_time: str = None,
        request_start_time: str = None,
        smart_pressure_time: str = None,
        src_instance_id: str = None,
        src_public_ip: str = None,
        src_super_account: str = None,
        src_super_password: str = None,
        task_type: str = None,
        work_dir: str = None,
    ):
        # The total number of stress testing tasks to create. Valid values: **0** to **30**. Default value: **1**.
        self.amount = amount
        # The ID of the backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the backup list and obtain the ID.
        self.backup_id = backup_id
        # The time of the backup. Format: yyyy-MM-ddTHH:mm:ssZ (UTC time).
        self.backup_time = backup_time
        # The type of stress testing machine. Valid values:
        # 
        # - **ECS**: You need to prepare a [Database Gateway](https://help.aliyun.com/document_detail/64905.html) yourself.
        # 
        # - **DAS_ECS**: An ECS instance that is automatically purchased and deployed by DAS.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The description of the stress testing task.
        # 
        # This parameter is required.
        self.description = description
        # The connection address of the target instance. Only RDS MySQL and PolarDB MySQL instances are supported.
        # 
        # > This parameter takes effect when **DstType** is set to **ConnectionString**.
        self.dst_connection_string = dst_connection_string
        # The ID of the target instance. Only RDS MySQL and PolarDB MySQL instances are supported. You can call the [GetInstanceInspections](https://help.aliyun.com/document_detail/202857.html) operation to obtain the ID.
        # 
        # > This parameter is required when **DstType** is set to **Instance**.
        self.dst_instance_id = dst_instance_id
        # The port of the target instance.
        # 
        # > This parameter takes effect when **DstType** is set to **ConnectionString**.
        self.dst_port = dst_port
        # The privileged account of the target instance.
        self.dst_super_account = dst_super_account
        # The password of the privileged account of the target instance.
        self.dst_super_password = dst_super_password
        # The type of the target instance. Valid values:
        # 
        # - **Instance** (default): instance ID.
        # 
        # - **ConnectionString**: connection address of the instance.
        self.dst_type = dst_type
        # The specification of the DTS migration task. You can call the [DescribeCloudbenchTask](https://help.aliyun.com/document_detail/230669.html) operation to obtain the specification.
        # 
        # > The stress testing task needs to migrate the baseline data from the source instance to the target instance. This parameter is required when you create a new DTS task.
        self.dts_job_class = dts_job_class
        # The ID of the DTS migration task. You can call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation to obtain the ID.
        # 
        # > This parameter is required when a DTS task has been created in the DTS console.
        self.dts_job_id = dts_job_id
        # The status after the stress testing task ends. Valid values:
        # 
        # - **WAIT_TARGET**: Prepare the target instance for stress testing.
        # 
        # - **WAIT_DBGATEWAY**: Prepare the stress testing deployment.
        # 
        # - **WAIT_SQL**: Prepare the full SQL statements.
        # 
        # - **WAIT_LOGIC**: Prepare to start replaying the traffic.
        # 
        # > When the stress testing task completes the status set by EndState, the task directly reaches the completed status.
        self.end_state = end_state
        # The virtual private cloud (VPC) ID of the Database Gateway.
        # 
        # > This parameter is required when **ClientType** is set to **ECS**.
        self.gateway_vpc_id = gateway_vpc_id
        # The IP address or domain name of the Database Gateway.
        # 
        # > This parameter is required when **ClientType** is set to **ECS**.
        self.gateway_vpc_ip = gateway_vpc_ip
        # The replay speed of the source instance traffic on the target instance. The replay speed must be a positive integer. Valid values: **1** to **30**. Default value: **1**.
        self.rate = rate
        # The duration of the stress testing task. Unit: milliseconds.
        self.request_duration = request_duration
        # The end time of the stress testing task. The time is in the UNIX timestamp format. Unit: milliseconds.
        self.request_end_time = request_end_time
        # The start time of the stress testing task. The time is in the UNIX timestamp format. Unit: milliseconds.
        self.request_start_time = request_start_time
        # The duration of the generated stress testing. Unit: milliseconds.
        # 
        # > This parameter is required when **TaskType** is set to **smart pressure test**.
        self.smart_pressure_time = smart_pressure_time
        # The ID of the source instance. Only RDS MySQL and PolarDB MySQL instances are supported. You can call the [GetInstanceInspections](https://help.aliyun.com/document_detail/202857.html) operation to obtain the ID.
        # 
        # > This parameter is required when **DstType** is set to **Instance**.
        # 
        # This parameter is required.
        self.src_instance_id = src_instance_id
        # Reserved parameter.
        self.src_public_ip = src_public_ip
        # The privileged account of the source instance. Value: **admin**.
        # 
        # > This parameter is required when **DstType** is set to **Instance**.
        self.src_super_account = src_super_account
        # The password of the privileged account of the source instance.
        # 
        # > This parameter is required when **DstType** is set to **Instance**.
        self.src_super_password = src_super_password
        # The type of stress testing task. Valid values:
        # 
        # - **pressure test** (default): Intelligent stress testing, which replays the traffic captured from the source instance on the target instance at the maximum speed supported by the target instance type.
        # 
        # - **smart pressure test**: Generated stress testing, which analyzes and learns from the traffic captured from the source instance in a short period of time, generates traffic that is consistent with the business model and traffic distribution of the original traffic for continuous stress testing, reduces the time for collecting data from the source instance, and reduces storage costs and performance overhead.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The temporary directory generated by the stress testing.
        self.work_dir = work_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.backup_id is not None:
            result['BackupId'] = self.backup_id

        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.description is not None:
            result['Description'] = self.description

        if self.dst_connection_string is not None:
            result['DstConnectionString'] = self.dst_connection_string

        if self.dst_instance_id is not None:
            result['DstInstanceId'] = self.dst_instance_id

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.dst_super_account is not None:
            result['DstSuperAccount'] = self.dst_super_account

        if self.dst_super_password is not None:
            result['DstSuperPassword'] = self.dst_super_password

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.dts_job_class is not None:
            result['DtsJobClass'] = self.dts_job_class

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.end_state is not None:
            result['EndState'] = self.end_state

        if self.gateway_vpc_id is not None:
            result['GatewayVpcId'] = self.gateway_vpc_id

        if self.gateway_vpc_ip is not None:
            result['GatewayVpcIp'] = self.gateway_vpc_ip

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.request_duration is not None:
            result['RequestDuration'] = self.request_duration

        if self.request_end_time is not None:
            result['RequestEndTime'] = self.request_end_time

        if self.request_start_time is not None:
            result['RequestStartTime'] = self.request_start_time

        if self.smart_pressure_time is not None:
            result['SmartPressureTime'] = self.smart_pressure_time

        if self.src_instance_id is not None:
            result['SrcInstanceId'] = self.src_instance_id

        if self.src_public_ip is not None:
            result['SrcPublicIp'] = self.src_public_ip

        if self.src_super_account is not None:
            result['SrcSuperAccount'] = self.src_super_account

        if self.src_super_password is not None:
            result['SrcSuperPassword'] = self.src_super_password

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')

        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DstConnectionString') is not None:
            self.dst_connection_string = m.get('DstConnectionString')

        if m.get('DstInstanceId') is not None:
            self.dst_instance_id = m.get('DstInstanceId')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('DstSuperAccount') is not None:
            self.dst_super_account = m.get('DstSuperAccount')

        if m.get('DstSuperPassword') is not None:
            self.dst_super_password = m.get('DstSuperPassword')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('DtsJobClass') is not None:
            self.dts_job_class = m.get('DtsJobClass')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('EndState') is not None:
            self.end_state = m.get('EndState')

        if m.get('GatewayVpcId') is not None:
            self.gateway_vpc_id = m.get('GatewayVpcId')

        if m.get('GatewayVpcIp') is not None:
            self.gateway_vpc_ip = m.get('GatewayVpcIp')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('RequestDuration') is not None:
            self.request_duration = m.get('RequestDuration')

        if m.get('RequestEndTime') is not None:
            self.request_end_time = m.get('RequestEndTime')

        if m.get('RequestStartTime') is not None:
            self.request_start_time = m.get('RequestStartTime')

        if m.get('SmartPressureTime') is not None:
            self.smart_pressure_time = m.get('SmartPressureTime')

        if m.get('SrcInstanceId') is not None:
            self.src_instance_id = m.get('SrcInstanceId')

        if m.get('SrcPublicIp') is not None:
            self.src_public_ip = m.get('SrcPublicIp')

        if m.get('SrcSuperAccount') is not None:
            self.src_super_account = m.get('SrcSuperAccount')

        if m.get('SrcSuperPassword') is not None:
            self.src_super_password = m.get('SrcSuperPassword')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        return self

