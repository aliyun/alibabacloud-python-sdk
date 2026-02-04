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
        # The UNIX timestamp that represents the start time of change tracking. Unit: seconds.
        # 
        # >  You can use a search engine to obtain a UNIX timestamp converter.
        self.checkpoint = checkpoint
        # The objects for which you want to track data changes. The value must be a JSON string. For more information, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        # 
        # This parameter is required.
        self.db_list = db_list
        # The ID of the DTS dedicated cluster on which the change tracking task is scheduled to run.
        self.dedicated_cluster_id = dedicated_cluster_id
        # Specifies whether to monitor the task latency. Valid values:
        # 
        # *   **true**: monitors the task latency.
        # *   **false**: does not monitor the task latency.
        self.delay_notice = delay_notice
        # The mobile numbers to which latency-related alerts are sent. Separate multiple mobile numbers with commas (,).
        # 
        # > 
        # *   This parameter is available only for users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers.
        # *   Users of the international site (alibabacloud.com) cannot receive alerts by using mobile phones, but can [configure alert rules for DTS tasks in the CloudMonitor console](https://help.aliyun.com/document_detail/175876.html).
        self.delay_phone = delay_phone
        # The threshold for triggering latency-related alerts. Unit: seconds. The value must be an integer. You can set the threshold based on your business needs. To prevent jitters caused by network and database overloads, we recommend that you set the threshold to more than 10 seconds.
        # 
        # >  If the **DelayNotice** parameter is set to **true**, this parameter is required.
        self.delay_rule_time = delay_rule_time
        # Environment label of the DTS instance, with values:
        # - **normal**: **general** - **online**: **production**
        self.dts_bis_label = dts_bis_label
        # The ID of the change tracking instance. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        self.dts_instance_id = dts_instance_id
        # The ID of the change tracking task. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the task ID.
        self.dts_job_id = dts_job_id
        # The name of the change tracking task.
        # 
        # >  We recommend that you specify a descriptive name for easy identification. You do not need to use a unique name.
        # 
        # This parameter is required.
        self.dts_job_name = dts_job_name
        # Specifies whether to monitor the task status. Valid values:
        # 
        # *   **true**: monitors the task status.
        # *   **false**: does not monitor the task status.
        self.error_notice = error_notice
        # The mobile numbers to which status-related alerts are sent. Separate multiple mobile numbers with commas (,).
        # 
        # > 
        # *   This parameter is available only for users of the China site (aliyun.com). Only mobile numbers in the Chinese mainland are supported. You can specify up to 10 mobile numbers.
        # *   Users of the international site (alibabacloud.com) cannot receive alerts by using mobile phones, but can [configure alert rules for DTS tasks in the CloudMonitor console](https://help.aliyun.com/document_detail/175876.html).
        self.error_phone = error_phone
        # The DU upper limit of the Serverless instance, with values being: 2, 4, 8, 16. 
        # Currently, this feature is not supported, please do not pass in parameters.
        self.max_du = max_du
        # The lower limit of DU for Serverless instances, with values being: 1, 2, 4, 8, 16. 
        # This feature is currently not supported, please do not pass in parameters.
        self.min_du = min_du
        # The ID of the region in which the Data Transmission Service (DTS) instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The reserved parameter of DTS. The value must be a JSON string. You can specify this parameter to add more configurations of the source or destination database to the DTS task. For example, you can specify the data storage format of the destination Kafka database and the ID of the CEN instance. For more information, see [MigrationReserved](https://help.aliyun.com/document_detail/176470.html).
        self.reserve = reserve
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Name of the database to be subscribed.
        self.source_endpoint_database_name = source_endpoint_database_name
        # The engine of the source database. Valid values: **MySQL**, **PostgreSQL**, and **Oracle**.
        # 
        # >  If the source database is a self-managed database, you must specify this parameter.
        self.source_endpoint_engine_name = source_endpoint_engine_name
        # The endpoint of the source database.
        # 
        # >  This parameter is required only when the source database is a self-managed database.
        self.source_endpoint_ip = source_endpoint_ip
        # The ID of the source database.
        # 
        # >  This parameter is required only when the source database is an ApsaraDB RDS for MySQL instance, a PolarDB-X 1.0 instance, or a PolarDB for MySQL cluster.
        self.source_endpoint_instance_id = source_endpoint_instance_id
        # The type of the source database. Valid values:
        # 
        # *   **RDS**: ApsaraDB RDS for MySQL instance
        # *   **PolarDB**: PolarDB for MySQL cluster
        # *   **DRDS**: PolarDB-X 1.0 instance
        # *   **LocalInstance**: self-managed database with a public IP address
        # *   **ECS**: self-managed database hosted on an Elastic Compute Service (ECS) instance
        # *   **Express**: self-managed database connected over Express Connect
        # *   **CEN**: self-managed database connected over Cloud Enterprise Network (CEN)
        # *   **dg**: self-managed database connected over Database Gateway
        self.source_endpoint_instance_type = source_endpoint_instance_type
        # The system ID (SID) of the Oracle database.
        # 
        # >  This parameter is required only when the source database is a self-managed Oracle database and is not deployed in the Real Application Clusters (RAC) architecture.
        self.source_endpoint_oracle_sid = source_endpoint_oracle_sid
        # The ID of the Alibaba Cloud account to which the source database belongs.
        # 
        # >  This parameter is required only when you track data changes across different Alibaba Cloud accounts.
        self.source_endpoint_owner_id = source_endpoint_owner_id
        # The password of the account that is used to connect to the source database.
        self.source_endpoint_password = source_endpoint_password
        # The service port number of the source database.
        # 
        # >  This parameter is required only when the source database is a self-managed database.
        self.source_endpoint_port = source_endpoint_port
        # The ID of the region in which the source database resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # >  If the source database is a self-managed database with a public IP address, you can set the value of this parameter to **cn-hangzhou** or the ID of the region that is closest to the region in which the self-managed database resides.
        self.source_endpoint_region = source_endpoint_region
        # The RAM role that is authorized to access the source database. This parameter is required if the source database does not belong to the Alibaba Cloud account that you use to configure the change tracking task. In this case, you must authorize the Alibaba Cloud account to access the source database by using a RAM role.
        # 
        # >  For more information about the permissions that are required for the RAM role and how to grant the permissions to the RAM role, see [Configure RAM authorization for cross-account data migration and synchronization](https://help.aliyun.com/document_detail/48468.html).
        self.source_endpoint_role = source_endpoint_role
        # The username of the account that is used to connect to the source database.
        # 
        # >  The permissions that are required for the database account vary with the change tracking scenario. For more information, see [Prepare the source database account for change tracking](https://help.aliyun.com/document_detail/212653.html).
        self.source_endpoint_user_name = source_endpoint_user_name
        # The path of the certificate authority (CA) certificate that is used if the connection to the source database is encrypted by using the SSL protocol.
        # 
        # >  This feature is not supported. Do not specify this parameter.
        self.src_ca_certificate_oss_url = src_ca_certificate_oss_url
        # The key of the CA certificate that is used if the connection to the source database is encrypted by using the SSL protocol.
        # 
        # >  This feature is not supported. Do not specify this parameter.
        self.src_ca_certificate_password = src_ca_certificate_password
        # The path to the client certificate that is used if the connection to the source database is encrypted by using the SSL protocol.
        # 
        # >  This feature is not supported. Do not specify this parameter.
        self.src_client_cert_oss_url = src_client_cert_oss_url
        # The path to the private key of the client certificate that is used if the connection to the source database is encrypted by using the SSL protocol.
        # 
        # >  This feature is not supported. Do not specify this parameter.
        self.src_client_key_oss_url = src_client_key_oss_url
        # The password of the private key of the client certificate that is used if the connection to the source database is encrypted by using the SSL protocol.
        # 
        # >  This feature is not supported. Do not specify this parameter.
        self.src_client_password = src_client_password
        # Specifies whether to track DDL statements. Default value: true. Valid values:
        # 
        # *   **true**: tracks DDL statements.
        # *   **false**: does not track DDL statements.
        self.subscription_data_type_ddl = subscription_data_type_ddl
        # Specifies whether to track DML statements. Default value: true. Valid values:
        # 
        # *   **true**: tracks DML statements.
        # *   **false**: does not track DML statements.
        self.subscription_data_type_dml = subscription_data_type_dml
        # The network type of the change tracking task. Set the value to **vpc**. A value of vpc indicates the Virtual Private Cloud (VPC) network type.
        # 
        # > 
        # *   To use the new version of the change tracking feature, you must specify the SubscriptionInstanceNetworkType parameter. You must also specify the **SubscriptionInstanceVPCId** and **SubscriptionInstanceVSwitchID** parameters. If you do not specify the SubscriptionInstanceNetworkType parameter, the previous version of the change tracking feature is used.
        # *   The previous version of the change tracking feature supports self-managed MySQL databases, ApsaraDB RDS for MySQL instances, and PolarDB-X 1.0 instances. The new version of the change tracking feature supports self-managed MySQL databases, ApsaraDB RDS for MySQL instances, PolarDB for MySQL clusters, and Oracle databases.
        # 
        # This parameter is required.
        self.subscription_instance_network_type = subscription_instance_network_type
        # The ID of the VPC in which the change tracking instance is deployed.
        # 
        # >  This parameter is required only when the **SubscriptionInstanceNetworkType** parameter is set to **vpc**.
        self.subscription_instance_vpcid = subscription_instance_vpcid
        # The ID of the vSwitch in the specified VPC.
        # 
        # >  This parameter is required only when the **SubscriptionInstanceNetworkType** parameter is set to **vpc**.
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

