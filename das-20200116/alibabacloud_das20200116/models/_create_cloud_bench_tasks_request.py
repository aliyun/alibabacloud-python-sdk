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
        # The total number of stress testing tasks that you want to create. Valid values: **0** to **30**. Default value: **1**.
        self.amount = amount
        # The ID of the backup set. You can call the [DescribeBackups](https://help.aliyun.com/document_detail/26273.html) operation to query the ID of the backup set.
        self.backup_id = backup_id
        # The time when the backup starts. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.backup_time = backup_time
        # The type of the stress testing client. Valid values:
        # 
        # *   **ECS**: indicates that you must create the [DBGateway](https://help.aliyun.com/document_detail/64905.html).
        # *   **DAS_ECS**: indicates that DAS automatically purchases and deploys an Elastic Compute Service (ECS) instance for stress testing.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The description of the stress testing task.
        # 
        # This parameter is required.
        self.description = description
        # The endpoint of the destination instance. The specified endpoint must be the endpoint of an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance.
        # 
        # >  This parameter takes effect only if you set **DstType** to **ConnectionString**.
        self.dst_connection_string = dst_connection_string
        # The ID of the destination instance. The instance must be an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance. You can call the [GetInstanceInspections](https://help.aliyun.com/document_detail/202857.html) operation to query the ID.
        # 
        # >  This parameter must be specified if you set **DstType** to **Instance**.
        self.dst_instance_id = dst_instance_id
        # The port number of the instance that you want to access.
        # 
        # >  This parameter takes effect only if you set **DstType** to **ConnectionString**.
        self.dst_port = dst_port
        # The name of the privileged account for the destination instance.
        self.dst_super_account = dst_super_account
        # The password of the privileged account for the destination instance.
        self.dst_super_password = dst_super_password
        # The type of the identifier that is used to indicate the destination instance. Valid values:
        # 
        # *   **Instance**: the instance ID. This is the default value.
        # *   **ConnectionString**: the endpoint of the instance.
        self.dst_type = dst_type
        # The specification of the Data Transmission Service (DTS) migration task. You can call the [DescribeCloudbenchTask](https://help.aliyun.com/document_detail/230669.html) operation to query the specification.
        # 
        # >  You must migrate the basic data in the source instance to the destination instance before you start a stress testing task. When you create a DTS migration task, you must specify this parameter.
        self.dts_job_class = dts_job_class
        # The ID of the DTS migration task. You can call the [ConfigureDtsJob](https://help.aliyun.com/document_detail/208399.html) operation to query the ID.
        # 
        # >  After a DTS migration task is created in the DTS console, you must specify this parameter.
        self.dts_job_id = dts_job_id
        # The state that specifies the last operation that is performed for the stress testing task. Valid values:
        # 
        # *   **WAIT_TARGET**: prepares the destination instance
        # *   **WAIT_DBGATEWAY**: prepares the DBGateway
        # *   **WAIT_SQL**: prepares the full SQL statistics
        # *   **WAIT_LOGIC**: prepares to replay the traffic
        # 
        # >  When the state of a stress testing task changes to the state that is specified by the EndState parameter, the stress testing task becomes completed.
        self.end_state = end_state
        # The ID of the virtual private cloud (VPC) in which the database gateway (DBGateway) is deployed.
        # 
        # >  This parameter must be specified if you set **ClientType** to **ECS**.
        self.gateway_vpc_id = gateway_vpc_id
        # The IP address or domain name of the DBGateway.
        # 
        # >  This parameter must be specified if you set **ClientType** to **ECS**.
        self.gateway_vpc_ip = gateway_vpc_ip
        # The rate at which the traffic captured from the source instance is replayed on the destination instance. The value must be a positive integer. Valid values: **1** to **30**. Default value: **1**.
        self.rate = rate
        # The duration of the stress testing task for which the traffic is captured from the source instance. Unit: milliseconds.
        self.request_duration = request_duration
        # The time when the stress testing task ends. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.request_end_time = request_end_time
        # The time when the stress testing task starts. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.request_start_time = request_start_time
        # The duration within which the traffic generation stressing test takes effect. Unit: milliseconds.
        # 
        # >  This parameter must be specified if you set **TaskType** to **smart pressure test**.
        self.smart_pressure_time = smart_pressure_time
        # The ID of the source instance. The instance must be an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL instance. You can call the [GetInstanceInspections](https://help.aliyun.com/document_detail/202857.html) operation to query the ID.
        # 
        # >  This parameter must be specified if you set **DstType** to **Instance**.
        # 
        # This parameter is required.
        self.src_instance_id = src_instance_id
        # The reserved parameter.
        self.src_public_ip = src_public_ip
        # The name of the privileged account for the source instance. Set the value to **admin**.
        # 
        # >  This parameter must be specified if you set **DstType** to **Instance**.
        self.src_super_account = src_super_account
        # The password of the privileged account for the source instance.
        # 
        # >  This parameter must be specified if you set **DstType** to **Instance**.
        self.src_super_password = src_super_password
        # The type of the stress testing task. Valid values:
        # 
        # *   **pressure test** (default): A task of this type replays the traffic that is captured from the source instance on the destination instance at the maximum playback rate that is supported by the destination instance.
        # *   **smart pressure test**: A task of this type analyzes the traffic that is captured from the source instance over a short period of time and generates traffic on the destination instance for continuous stress testing. The business model based on which the traffic is generated on the destination instance and the traffic distribution are consistent with those on the source instance. Stress testing tasks of this type can help you reduce the amount of time that is consumed to collect data from the source instance and reduce storage costs and performance overheads.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The temporary directory generated for stress testing.
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

