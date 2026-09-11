# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureSubscriptionRequest(DaraModel):
    def __init__(
        self,
        checkpoint: str = None,
        db_list: str = None,
        dedicated_cluster_id: str = None,
        delay_notice: bool = None,
        delay_phone: str = None,
        delay_rule_time: int = None,
        dts_bis_label: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        dts_job_name: str = None,
        error_notice: bool = None,
        error_phone: str = None,
        max_du: float = None,
        min_du: float = None,
        region_id: str = None,
        reserve: str = None,
        resource_group_id: str = None,
        source_endpoint_database_name: str = None,
        source_endpoint_engine_name: str = None,
        source_endpoint_ip: str = None,
        source_endpoint_instance_id: str = None,
        source_endpoint_instance_type: str = None,
        source_endpoint_oracle_sid: str = None,
        source_endpoint_owner_id: str = None,
        source_endpoint_password: str = None,
        source_endpoint_port: str = None,
        source_endpoint_region: str = None,
        source_endpoint_role: str = None,
        source_endpoint_user_name: str = None,
        src_ca_certificate_oss_url: str = None,
        src_ca_certificate_password: str = None,
        src_client_cert_oss_url: str = None,
        src_client_key_oss_url: str = None,
        src_client_password: str = None,
        subscription_data_type_ddl: bool = None,
        subscription_data_type_dml: bool = None,
        subscription_instance_network_type: str = None,
        subscription_instance_vpcid: str = None,
        subscription_instance_vswitch_id: str = None,
    ):
        # The start time of change tracking, in the format of a UNIX timestamp. Unit: seconds.
        # > You can use a search engine to find a UNIX timestamp converter.
        self.checkpoint = checkpoint
        # The objects to be tracked, in JSON format. For more information, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        # 
        # This parameter is required.
        self.db_list = db_list
        # The ID of the DTS dedicated cluster. This parameter is used to schedule the change tracking task to the specified DTS dedicated cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # Specifies whether to monitor the latency status. Valid values:
        # 
        # - **true**: monitors the latency status.
        # - **false**: does not monitor the latency status.
        self.delay_notice = delay_notice
        # The mobile phone numbers for receiving latency alerts. Separate multiple phone numbers with commas (,).
        # > - This parameter is supported only on the China site (aliyun.com). Only Chinese mainland phone numbers are supported, and you can specify up to 10 phone numbers.
        # - The China site (Chinese mainland) does not support phone alerts. You can only [configure alert rules for DTS tasks in CloudMonitor](https://help.aliyun.com/document_detail/175876.html).
        self.delay_phone = delay_phone
        # The threshold for triggering latency alerts. Unit: seconds. The value must be an integer. Set the threshold based on your business requirements. To avoid alert fluctuations caused by network conditions or database loads, set the threshold to 10 seconds or more.
        # > This parameter is required when **DelayNotice** is set to **true**.
        self.delay_rule_time = delay_rule_time
        # The environment tag of the DTS instance. Valid values:
        # 
        # - **normal**: normal
        # - **online**: online.
        self.dts_bis_label = dts_bis_label
        # The ID of the change tracking instance. You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to query the instance ID.
        self.dts_instance_id = dts_instance_id
        # The ID of the change tracking task. You can call [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) to query the task ID.
        self.dts_job_id = dts_job_id
        # The name of the change tracking task.
        # > Specify a descriptive name that makes it easy to identify the task. The name does not need to be unique.
        # 
        # This parameter is required.
        self.dts_job_name = dts_job_name
        # Specifies whether to monitor the error status. Valid values:
        # 
        # - **true**: monitors the error status.
        # - **false**: does not monitor the error status.
        self.error_notice = error_notice
        # The mobile phone numbers for receiving error alerts. Separate multiple phone numbers with commas (,).
        # > - This parameter is supported only on the China site (aliyun.com). Only Chinese mainland phone numbers are supported, and you can specify up to 10 phone numbers.
        # - The China site (Chinese mainland) does not support phone alerts. You can only [configure alert rules for DTS tasks in CloudMonitor](https://help.aliyun.com/document_detail/175876.html).
        self.error_phone = error_phone
        # The maximum number of DUs for a serverless instance. Valid values: 2, 4, 8, and 16.
        # <props="intl">
        # > This feature is currently not supported. Do not specify this parameter..
        self.max_du = max_du
        # The minimum number of DTS Units (DUs) for a serverless instance. Valid values: 1, 2, 4, 8, and 16.
        # <props="intl">
        # > This feature is currently not supported. Do not specify this parameter..
        self.min_du = min_du
        # The region in which the change tracking instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The reserved parameter of DTS, in JSON format. You can specify this parameter to add information about the source and destination databases, such as the data storage format of the destination Kafka database or the CEN instance ID. For more information, see the [Reserve metric description](https://help.aliyun.com/document_detail/176470.html).
        self.reserve = reserve
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The name of the database to be tracked.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The engine type of the source database. Valid values: **MySQL**, **PostgreSQL**, and **Oracle**.
        # 
        # > This parameter is required if the source database is a self-managed database.
        self.source_endpoint_engine_name = source_endpoint_engine_name
        # The endpoint of the source database.
        # > This parameter is available and required only when the source database is a self-managed database.
        self.source_endpoint_ip = source_endpoint_ip
        # The instance ID of the source instance.
        # > This parameter is active and required only when the source database is an ApsaraDB RDS for MySQL instance, a PolarDB-X 1.0 instance, or a PolarDB for MySQL cluster.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The instance type of the source database. Valid values:
        # 
        # - **RDS**: ApsaraDB RDS instance.
        # - **PolarDB**: PolarDB for MySQL cluster.
        # - **DRDS**: PolarDB-X 1.0 instance.
        # - **LocalInstance**: self-managed database with a public IP address.
        # - **ECS**: self-managed database hosted on an ECS instance.
        # - **Express**: self-managed database connected over Express Connect.
        # - **CEN**: self-managed database connected over Cloud Enterprise Network (CEN).
        # - **dg**: self-managed database connected over Database Gateway.
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The SID of the Oracle database.
        # > This parameter is available and required only when the source database is a self-managed Oracle database that is not a Real Application Cluster (RAC) instance.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The Alibaba Cloud account ID of the account to which the source instance belongs.
        # > This parameter is active and required only when you configure cross-Alibaba Cloud account change tracking. You must subscribe to the task.
        self.source_endpoint_owner_id = source_endpoint_owner_id
        # The password of the database account for the source instance.
        self.source_endpoint_password = source_endpoint_password
        # The service port of the source database.
        # > This parameter is available and required only when the source database is a self-managed database.
        self.source_endpoint_port = source_endpoint_port
        # The region of the source instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the source instance is a self-managed database with a public IP address, you can set this parameter to **cn-hangzhou** or the region ID closest to the self-managed database.
        self.source_endpoint_region = source_endpoint_region
        # The authorized role of the source instance. If the source instance and the change tracking task belong to different Alibaba Cloud accounts, specify this parameter to allow the Alibaba Cloud account that owns the change tracking task to access the source instance.
        # > For more information about the permissions and authorization methods required for the role, see [Configure RAM authorization for cross-account data migration or synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.source_endpoint_role = source_endpoint_role
        # The database account of the source instance.
        # > The permissions required for change tracking vary depending on the database type. For more information, see the account permissions section in [Prepare database accounts for change tracking](https://help.aliyun.com/document_detail/212653.html).
        self.source_endpoint_user_name = source_endpoint_user_name
        # The path of the CA certificate when the source database uses an SSL connection.
        # 
        # > This feature is currently not supported. Do not specify this parameter.
        self.src_ca_certificate_oss_url = src_ca_certificate_oss_url
        # The key of the CA certificate when the source database uses an SSL connection.
        # 
        # > This feature is currently not supported. Do not specify this parameter.
        self.src_ca_certificate_password = src_ca_certificate_password
        # The path of the client certificate when the source database uses an SSL connection.
        # 
        # > This feature is currently not supported. Do not specify this parameter.
        self.src_client_cert_oss_url = src_client_cert_oss_url
        # The path of the client certificate private key when the source database uses an SSL connection.
        # 
        # > This feature is currently not supported. Do not specify this parameter.
        self.src_client_key_oss_url = src_client_key_oss_url
        # The password of the client certificate private key when the source database uses an SSL connection.
        # 
        # > This feature is currently not supported. Do not specify this parameter.
        self.src_client_password = src_client_password
        # Specifies whether to track DDL data. Valid values:
        # 
        # - **true** (default): tracks DDL data.
        # - **false**: does not track DDL data.
        self.subscription_data_type_ddl = subscription_data_type_ddl
        # Specifies whether to track DML data. Valid values:
        # - **true** (default): tracks DML data.
        # - **false**: does not track DML data.
        self.subscription_data_type_dml = subscription_data_type_dml
        # The network type of the change tracking task. The only valid value is **vpc**, which indicates virtual private cloud (VPC).
        # 
        # > - If you specify this parameter, the change tracking task is defined as the new version. You must also correctly set the **SubscriptionInstanceVPCId** and **SubscriptionInstanceVSwitchID** parameters. If you do not specify this parameter, the change tracking task is defined as the legacy version.
        # - Legacy change tracking tasks support tracking data from self-managed MySQL, ApsaraDB RDS for MySQL, and PolarDB-X 1.0. New-version change tracking tasks support tracking data from self-managed MySQL, ApsaraDB RDS for MySQL, PolarDB for MySQL, and Oracle.
        # 
        # This parameter is required.
        self.subscription_instance_network_type = subscription_instance_network_type
        # The VPC ID of the change tracking instance.
        # > This parameter is available and required only when **SubscriptionInstanceNetworkType** is set to **vpc**.
        self.subscription_instance_vpcid = subscription_instance_vpcid
        # The vSwitch ID of the change tracking instance.
        # > This parameter is available and required only when **SubscriptionInstanceNetworkType** is set to **vpc**.
        self.subscription_instance_vswitch_id = subscription_instance_vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.db_list is not None:
            result['DbList'] = self.db_list

        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.delay_notice is not None:
            result['DelayNotice'] = self.delay_notice

        if self.delay_phone is not None:
            result['DelayPhone'] = self.delay_phone

        if self.delay_rule_time is not None:
            result['DelayRuleTime'] = self.delay_rule_time

        if self.dts_bis_label is not None:
            result['DtsBisLabel'] = self.dts_bis_label

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.dts_job_name is not None:
            result['DtsJobName'] = self.dts_job_name

        if self.error_notice is not None:
            result['ErrorNotice'] = self.error_notice

        if self.error_phone is not None:
            result['ErrorPhone'] = self.error_phone

        if self.max_du is not None:
            result['MaxDu'] = self.max_du

        if self.min_du is not None:
            result['MinDu'] = self.min_du

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reserve is not None:
            result['Reserve'] = self.reserve

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_endpoint_database_name is not None:
            result['SourceEndpointDatabaseName'] = self.source_endpoint_database_name

        if self.source_endpoint_engine_name is not None:
            result['SourceEndpointEngineName'] = self.source_endpoint_engine_name

        if self.source_endpoint_ip is not None:
            result['SourceEndpointIP'] = self.source_endpoint_ip

        if self.source_endpoint_instance_id is not None:
            result['SourceEndpointInstanceID'] = self.source_endpoint_instance_id

        if self.source_endpoint_instance_type is not None:
            result['SourceEndpointInstanceType'] = self.source_endpoint_instance_type

        if self.source_endpoint_oracle_sid is not None:
            result['SourceEndpointOracleSID'] = self.source_endpoint_oracle_sid

        if self.source_endpoint_owner_id is not None:
            result['SourceEndpointOwnerID'] = self.source_endpoint_owner_id

        if self.source_endpoint_password is not None:
            result['SourceEndpointPassword'] = self.source_endpoint_password

        if self.source_endpoint_port is not None:
            result['SourceEndpointPort'] = self.source_endpoint_port

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        if self.source_endpoint_role is not None:
            result['SourceEndpointRole'] = self.source_endpoint_role

        if self.source_endpoint_user_name is not None:
            result['SourceEndpointUserName'] = self.source_endpoint_user_name

        if self.src_ca_certificate_oss_url is not None:
            result['SrcCaCertificateOssUrl'] = self.src_ca_certificate_oss_url

        if self.src_ca_certificate_password is not None:
            result['SrcCaCertificatePassword'] = self.src_ca_certificate_password

        if self.src_client_cert_oss_url is not None:
            result['SrcClientCertOssUrl'] = self.src_client_cert_oss_url

        if self.src_client_key_oss_url is not None:
            result['SrcClientKeyOssUrl'] = self.src_client_key_oss_url

        if self.src_client_password is not None:
            result['SrcClientPassword'] = self.src_client_password

        if self.subscription_data_type_ddl is not None:
            result['SubscriptionDataTypeDDL'] = self.subscription_data_type_ddl

        if self.subscription_data_type_dml is not None:
            result['SubscriptionDataTypeDML'] = self.subscription_data_type_dml

        if self.subscription_instance_network_type is not None:
            result['SubscriptionInstanceNetworkType'] = self.subscription_instance_network_type

        if self.subscription_instance_vpcid is not None:
            result['SubscriptionInstanceVPCId'] = self.subscription_instance_vpcid

        if self.subscription_instance_vswitch_id is not None:
            result['SubscriptionInstanceVSwitchId'] = self.subscription_instance_vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('DbList') is not None:
            self.db_list = m.get('DbList')

        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DelayNotice') is not None:
            self.delay_notice = m.get('DelayNotice')

        if m.get('DelayPhone') is not None:
            self.delay_phone = m.get('DelayPhone')

        if m.get('DelayRuleTime') is not None:
            self.delay_rule_time = m.get('DelayRuleTime')

        if m.get('DtsBisLabel') is not None:
            self.dts_bis_label = m.get('DtsBisLabel')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('DtsJobName') is not None:
            self.dts_job_name = m.get('DtsJobName')

        if m.get('ErrorNotice') is not None:
            self.error_notice = m.get('ErrorNotice')

        if m.get('ErrorPhone') is not None:
            self.error_phone = m.get('ErrorPhone')

        if m.get('MaxDu') is not None:
            self.max_du = m.get('MaxDu')

        if m.get('MinDu') is not None:
            self.min_du = m.get('MinDu')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reserve') is not None:
            self.reserve = m.get('Reserve')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceEndpointDatabaseName') is not None:
            self.source_endpoint_database_name = m.get('SourceEndpointDatabaseName')

        if m.get('SourceEndpointEngineName') is not None:
            self.source_endpoint_engine_name = m.get('SourceEndpointEngineName')

        if m.get('SourceEndpointIP') is not None:
            self.source_endpoint_ip = m.get('SourceEndpointIP')

        if m.get('SourceEndpointInstanceID') is not None:
            self.source_endpoint_instance_id = m.get('SourceEndpointInstanceID')

        if m.get('SourceEndpointInstanceType') is not None:
            self.source_endpoint_instance_type = m.get('SourceEndpointInstanceType')

        if m.get('SourceEndpointOracleSID') is not None:
            self.source_endpoint_oracle_sid = m.get('SourceEndpointOracleSID')

        if m.get('SourceEndpointOwnerID') is not None:
            self.source_endpoint_owner_id = m.get('SourceEndpointOwnerID')

        if m.get('SourceEndpointPassword') is not None:
            self.source_endpoint_password = m.get('SourceEndpointPassword')

        if m.get('SourceEndpointPort') is not None:
            self.source_endpoint_port = m.get('SourceEndpointPort')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        if m.get('SourceEndpointRole') is not None:
            self.source_endpoint_role = m.get('SourceEndpointRole')

        if m.get('SourceEndpointUserName') is not None:
            self.source_endpoint_user_name = m.get('SourceEndpointUserName')

        if m.get('SrcCaCertificateOssUrl') is not None:
            self.src_ca_certificate_oss_url = m.get('SrcCaCertificateOssUrl')

        if m.get('SrcCaCertificatePassword') is not None:
            self.src_ca_certificate_password = m.get('SrcCaCertificatePassword')

        if m.get('SrcClientCertOssUrl') is not None:
            self.src_client_cert_oss_url = m.get('SrcClientCertOssUrl')

        if m.get('SrcClientKeyOssUrl') is not None:
            self.src_client_key_oss_url = m.get('SrcClientKeyOssUrl')

        if m.get('SrcClientPassword') is not None:
            self.src_client_password = m.get('SrcClientPassword')

        if m.get('SubscriptionDataTypeDDL') is not None:
            self.subscription_data_type_ddl = m.get('SubscriptionDataTypeDDL')

        if m.get('SubscriptionDataTypeDML') is not None:
            self.subscription_data_type_dml = m.get('SubscriptionDataTypeDML')

        if m.get('SubscriptionInstanceNetworkType') is not None:
            self.subscription_instance_network_type = m.get('SubscriptionInstanceNetworkType')

        if m.get('SubscriptionInstanceVPCId') is not None:
            self.subscription_instance_vpcid = m.get('SubscriptionInstanceVPCId')

        if m.get('SubscriptionInstanceVSwitchId') is not None:
            self.subscription_instance_vswitch_id = m.get('SubscriptionInstanceVSwitchId')

        return self

