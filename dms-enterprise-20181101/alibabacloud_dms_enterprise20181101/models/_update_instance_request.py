# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceRequest(DaraModel):
    def __init__(
        self,
        data_link_name: str = None,
        database_password: str = None,
        database_user: str = None,
        dba_id: str = None,
        ddl_online: int = None,
        ecs_instance_id: str = None,
        ecs_region: str = None,
        enable_sell_sitd: str = None,
        env_type: str = None,
        export_timeout: int = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_source: str = None,
        instance_type: str = None,
        port: int = None,
        query_timeout: int = None,
        safe_rule_id: str = None,
        sid: str = None,
        skip_test: bool = None,
        template_id: int = None,
        template_type: str = None,
        tid: int = None,
        use_dsql: int = None,
        vpc_id: str = None,
    ):
        # The name of the database link for cross-database queries.
        # 
        # > 
        # 
        # *   This parameter is required if UseDsql is set to 1.
        # 
        # *   The name can contain only lowercase letters and underscores (_).
        # 
        # *   The name must be unique within a tenant.
        self.data_link_name = data_link_name
        # The password that is used to log on to the database.
        # 
        # This parameter is required.
        self.database_password = database_password
        # The account that is used to log on to the database.
        # 
        # This parameter is required.
        self.database_user = database_user
        # The ID of the user who assumes the database administrator (DBA) role of the database instance. You can call the [ListUsers](https://help.aliyun.com/document_detail/141938.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the user ID.
        # 
        # This parameter is required.
        self.dba_id = dba_id
        # Specifies whether to enable the lock-free schema change feature for the database instance. Valid values:
        # 
        # *   **0:** disables the lock-free schema change feature.
        # *   **1**: uses the online DDL of MySQL first.
        # *   **2**: uses the lock-free schema change feature of DMS first.
        self.ddl_online = ddl_online
        # The ID of the ECS instance on which the database instance is deployed.
        # 
        # > This parameter is required if the InstanceSource parameter is set to ECS_OWN.
        self.ecs_instance_id = ecs_instance_id
        # The ID of the region in which the database instance resides.
        # 
        # > This parameter is required if InstanceSource is set to RDS, ECS_OWN, and VPC_IDC.
        self.ecs_region = ecs_region
        # *   **Y:** enables the sensitive data protection feature
        # *   **N:** disables the sensitive data protection feature
        # *   **NULL or other:** does not update the status of the sensitive data protection feature
        self.enable_sell_sitd = enable_sell_sitd
        # The type of the environment in which the database instance is deployed. Valid values:
        # 
        # *   **product:** production environment
        # *   **dev:** development environment
        # *   **pre:** pre-release environment
        # *   **test:** test environment
        # *   **sit:** system integration testing (SIT) environment
        # *   **uat:** user acceptance testing (UAT) environment
        # *   **pet:** stress testing environment
        # *   **stag:** staging environment
        # 
        # This parameter is required.
        self.env_type = env_type
        # The timeout period for exporting data from the database instance.
        # 
        # This parameter is required.
        self.export_timeout = export_timeout
        # The host address that is used to connect to the database instance.
        # 
        # This parameter is required.
        self.host = host
        # The alias of the database instance. Specify an alias that can help you identify the database instance in DMS.
        # 
        # This parameter is required.
        self.instance_alias = instance_alias
        # The ID of the database instance. You can call the [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The source of the database instance. Valid values:
        # 
        # *   **PUBLIC_OWN:** a self-managed database instance that is deployed on the Internet
        # *   **RDS:** an ApsaraDB RDS instance
        # *   **ECS_OWN:** a self-managed database that is deployed on an Elastic Compute Service (ECS) instance
        # *   **VPC_IDC:** a self-managed database instance that is deployed in a data center connected over a virtual private cloud (VPC)
        # 
        # This parameter is required.
        self.instance_source = instance_source
        # The type of the database. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The port that is used to connect to the database instance.
        # 
        # This parameter is required.
        self.port = port
        # The timeout period for querying data in the database instance.
        # 
        # This parameter is required.
        self.query_timeout = query_timeout
        # The name of the security rule set (GroupName) for the instance. You can call the [ListStandardGroups](https://help.aliyun.com/document_detail/417891.html) or [GetInstance](https://help.aliyun.com/document_detail/141567.html) operation to query the name of the security rule set.
        # 
        # This parameter is required.
        self.safe_rule_id = safe_rule_id
        # The system ID (SID) of the database instance.
        # 
        # > This parameter is required if the InstanceType parameter is set to ORACLE.
        self.sid = sid
        # Specifies whether to skip the connectivity test. Valid values:
        # 
        # *   **true:** skips the connectivity test
        # *   **false:** does not skip the connectivity test
        self.skip_test = skip_test
        # The ID of the classification template. You can call the [ListClassificationTemplates](https://help.aliyun.com/document_detail/460613.html) operation to query the template ID.
        self.template_id = template_id
        # The type of the classification template. You can call the [ListClassificationTemplates](https://help.aliyun.com/document_detail/460613.html) operation to query the template type.
        self.template_type = template_type
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid
        # Specifies whether to enable the cross-database query feature for the database instance. Valid values:
        # 
        # *   **0**: disables the cross-database query feature.
        # *   **1**: enables the cross-database query feature.
        # 
        # > Supported database types: MySQL, SQL Server, PostgreSQL, PolarDB for PostgreSQL (compatible with Oracle), and ApsaraDB for Redis.
        self.use_dsql = use_dsql
        # The ID of the VPC to which the database instance belongs.
        # 
        # > This parameter is required if the InstanceSource parameter is set to VPC_IDC.
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

        if self.enable_sell_sitd is not None:
            result['EnableSellSitd'] = self.enable_sell_sitd

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

        if self.port is not None:
            result['Port'] = self.port

        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout

        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id

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

        if m.get('EnableSellSitd') is not None:
            self.enable_sell_sitd = m.get('EnableSellSitd')

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

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')

        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')

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

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

