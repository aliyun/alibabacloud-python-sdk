# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceRequest(DaraModel):
    def __init__(
        self,
        data_link_name: str = None,
        database_password: str = None,
        database_user: str = None,
        dba_id: int = None,
        ddl_online: int = None,
        ecs_instance_id: str = None,
        ecs_region: str = None,
        enable_sell_common: str = None,
        enable_sell_sitd: str = None,
        enable_sell_stable: str = None,
        enable_sell_trust: str = None,
        env_type: str = None,
        export_timeout: int = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_source: str = None,
        instance_type: str = None,
        network_type: str = None,
        port: int = None,
        query_timeout: int = None,
        safe_rule: str = None,
        sid: str = None,
        skip_test: bool = None,
        template_id: int = None,
        template_type: str = None,
        tid: int = None,
        use_dsql: int = None,
        use_ssl: int = None,
        vpc_id: str = None,
    ):
        # The name of the database link for cross-database queries.
        # 
        # > 
        # 
        # *   This property must be specified when UseDsql is set to 1.
        # 
        # *   The name can contain only lowercase letters and underscores (_).
        # 
        # *   The name must be unique within a tenant.
        self.data_link_name = data_link_name
        # The password of the account that is used to log on to the database instance.
        self.database_password = database_password
        # The account that is used to log on to the database instance.
        self.database_user = database_user
        # The ID of the user who assumes the database administrator (DBA) role. You can call the [ListUsers](https://help.aliyun.com/document_detail/141938.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to obtain the value of this parameter.
        self.dba_id = dba_id
        # Specifies whether to enable lock-free schema change. Valid values:
        # 
        # *   **0**: Disable Lock-free Schema Change.
        # *   **1**: MySQL native online DDL first.
        # *   **2**: DMS native online DDL first.
        # 
        # > Supported databases include ApsaraDB RDS for MySQL, PolarDB for MySQL, ApsaraDB MyBase for MySQL, and third-party MySQL databases.
        self.ddl_online = ddl_online
        # The ID of the ECS instance.
        # 
        # >  This parameter is required if InstanceSource is set to ECS_OWN.
        self.ecs_instance_id = ecs_instance_id
        # The region in which the ECS instance resides.
        # 
        # >  This parameter is required if InstanceSource is set to RDS, ECS_OWN, or VPC_IDC.
        self.ecs_region = ecs_region
        # Specifies whether to enable Security Collaboration for the database instance. Valid values:
        # 
        # *   Y: Enable.
        # *   N: Disable.
        self.enable_sell_common = enable_sell_common
        # Specifies whether to enable sensitive data protection. Valid values:
        # 
        # *   Y: Enable.
        # *   N: Disable.
        self.enable_sell_sitd = enable_sell_sitd
        # Specifies whether to enable Stable Change for the database instance. Valid values:
        # 
        # *   Y: Enable.
        # *   N: Disable.
        self.enable_sell_stable = enable_sell_stable
        # Specifies whether to enable the security hosting feature for the database instance. Valid values:
        # 
        # *   Y: Enable.
        # *   N: Disable.
        self.enable_sell_trust = enable_sell_trust
        # The type of the environment in which the database instance is deployed. Valid values:
        # 
        # *   **product**: production environment.
        # *   **dev**: development environment.
        # *   **pre**: pre-release environment.
        # *   **test**: test environment.
        # *   **sit**: system integration testing (SIT) environment.
        # *   **uat**: user acceptance testing (UAT) environment.
        # *   **pet**: stress testing environment.
        # *   **stag**: staging environment.
        self.env_type = env_type
        # The timeout period for exporting data from the database instance. Unit: seconds.
        self.export_timeout = export_timeout
        # The endpoint that is used to connect to the database instance.
        self.host = host
        # The alias of the database instance. Specify an alias that can help you quickly identify the database instance in Data Management (DMS).
        self.instance_alias = instance_alias
        # The ID of the instance. You can call the [ListInstances](https://help.aliyun.com/document_detail/141936.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The source of the database instance. Valid values:
        # 
        # *   **PUBLIC_OWN**: a self-managed database instance that is deployed on the Internet.
        # *   **RDS**: an ApsaraDB RDS instance.
        # *   **ECS_OWN**: a self-managed database instance that is deployed on an Elastic Compute Service (ECS) instance.
        # *   **VPC_IDC**: a self-managed database instance that is deployed in a data center connected over a virtual private cloud (VPC).
        self.instance_source = instance_source
        # The type of the database instance. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.instance_type = instance_type
        # The network type of the database instance. Valid values:
        # 
        # *   **CLASSIC**: the classic network.
        # *   **VPC**: VPC.
        self.network_type = network_type
        # The port that is used to connect to the database instance.
        self.port = port
        # The timeout period for querying data from the database instance. Unit: seconds.
        self.query_timeout = query_timeout
        # The name of the security rule set for the database instance. This parameter is required if Security Collaboration is enabled. You can call the[ListStandardGroups](https://help.aliyun.com/document_detail/465940.html) or [GetInstance](https://help.aliyun.com/document_detail/465826.html) operation to obtain the name of the security rule set from GroupName.
        self.safe_rule = safe_rule
        # The system ID (SID) of the database instance.
        # 
        # > This parameter is required if InstanceType is set to ORACLE.
        self.sid = sid
        # Specifies whether to skip the connectivity test. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.skip_test = skip_test
        # The ID of the classification and grading template. You can call the [ListClassificationTemplates](https://help.aliyun.com/document_detail/465947.html) operation to query the template ID.
        self.template_id = template_id
        # The type of the classification and grading template. You can call the [ListClassificationTemplates](https://help.aliyun.com/document_detail/465947.html) operation to query the template type.
        self.template_type = template_type
        # The ID of the tenant.
        # 
        # > You can move the pointer over the profile picture in the upper-right corner of the DMS console to obtain the tenant ID.
        self.tid = tid
        # Specifies whether to enable cross-instance query for the database instance. Valid values:
        # 
        # *   **0**: Disables cross-database query.
        # *   **1**: Enables cross-database query.
        # 
        # > Supported databases include MySQL, SQL Server, PostgreSQL, PolarDB for Oracle, and Redis.
        self.use_dsql = use_dsql
        # Specifies whether to allow Data Management Service (DMS) to connect to the database instance by using SSL connections. Before you use SSL connections, make sure that the SSL encryption feature is enabled for the database instance. Valid values:
        # 
        # *   **0** (default): DMS automatically checks whether self-negotiation is enabled for the database instance. DMS automatically checks whether the SSL encryption feature is enabled for the database instance. If the SSL encryption feature is enabled, DMS connects to the database instance by using SSL connections. Otherwise, DMS connects to the database instance without encryption.
        # *   **1**: DMS connects to the database instance by using SSL connections. This value is invalid if the SSL encryption feature is disabled for the database instance.
        # *   **-1**: DMS does not connect to the database instance by using SSL connections.
        # 
        # > 
        # 
        # *   This parameter is available only for a MySQL or Redis database instance.
        # 
        # *   SSL encrypts network connections at the transport layer to improve the security and integrity of data in transmission. However, SSL increases the response time of network connections.
        self.use_ssl = use_ssl
        # The VPC ID.
        # 
        # >  This parameter is required if InstanceSource is set to VPC_IDC.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_link_name is not None:
            result['DataLinkName'] = self.data_link_name

        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password

        if self.database_user is not None:
            result['DatabaseUser'] = self.database_user

        if self.dba_id is not None:
            result['DbaId'] = self.dba_id

        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region

        if self.enable_sell_common is not None:
            result['EnableSellCommon'] = self.enable_sell_common

        if self.enable_sell_sitd is not None:
            result['EnableSellSitd'] = self.enable_sell_sitd

        if self.enable_sell_stable is not None:
            result['EnableSellStable'] = self.enable_sell_stable

        if self.enable_sell_trust is not None:
            result['EnableSellTrust'] = self.enable_sell_trust

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.export_timeout is not None:
            result['ExportTimeout'] = self.export_timeout

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.port is not None:
            result['Port'] = self.port

        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout

        if self.safe_rule is not None:
            result['SafeRule'] = self.safe_rule

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.skip_test is not None:
            result['SkipTest'] = self.skip_test

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.use_dsql is not None:
            result['UseDsql'] = self.use_dsql

        if self.use_ssl is not None:
            result['UseSsl'] = self.use_ssl

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataLinkName') is not None:
            self.data_link_name = m.get('DataLinkName')

        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')

        if m.get('DatabaseUser') is not None:
            self.database_user = m.get('DatabaseUser')

        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')

        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')

        if m.get('EnableSellCommon') is not None:
            self.enable_sell_common = m.get('EnableSellCommon')

        if m.get('EnableSellSitd') is not None:
            self.enable_sell_sitd = m.get('EnableSellSitd')

        if m.get('EnableSellStable') is not None:
            self.enable_sell_stable = m.get('EnableSellStable')

        if m.get('EnableSellTrust') is not None:
            self.enable_sell_trust = m.get('EnableSellTrust')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('ExportTimeout') is not None:
            self.export_timeout = m.get('ExportTimeout')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')

        if m.get('SafeRule') is not None:
            self.safe_rule = m.get('SafeRule')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('SkipTest') is not None:
            self.skip_test = m.get('SkipTest')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')

        if m.get('UseSsl') is not None:
            self.use_ssl = m.get('UseSsl')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

