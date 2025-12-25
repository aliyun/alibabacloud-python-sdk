# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        instance_list: main_models.ListInstancesResponseBodyInstanceList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code that is returned.
        self.error_code = error_code
        # The error message that is returned.
        self.error_message = error_message
        # The information about the database instances that are returned.
        self.instance_list = instance_list
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of database instances that are returned.
        self.total_count = total_count

    def validate(self):
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceList') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m.get('InstanceList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstancesResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        instance: List[main_models.ListInstancesResponseBodyInstanceListInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.ListInstancesResponseBodyInstanceListInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class ListInstancesResponseBodyInstanceListInstance(DaraModel):
    def __init__(
        self,
        data_link_name: str = None,
        database_password: str = None,
        database_user: str = None,
        dba_id: str = None,
        dba_nick_name: str = None,
        ddl_online: int = None,
        ecs_instance_id: str = None,
        ecs_region: str = None,
        env_type: str = None,
        export_timeout: int = None,
        host: str = None,
        instance_alias: str = None,
        instance_id: str = None,
        instance_source: str = None,
        instance_type: str = None,
        owner_id_list: main_models.ListInstancesResponseBodyInstanceListInstanceOwnerIdList = None,
        owner_name_list: main_models.ListInstancesResponseBodyInstanceListInstanceOwnerNameList = None,
        port: int = None,
        query_timeout: int = None,
        safe_rule_id: str = None,
        sell_sitd: bool = None,
        sell_trust: str = None,
        sid: str = None,
        standard_group: main_models.ListInstancesResponseBodyInstanceListInstanceStandardGroup = None,
        state: str = None,
        use_dsql: int = None,
        vpc_id: str = None,
    ):
        # The name of the database link for the database instance.
        self.data_link_name = data_link_name
        # The password that is used to log on to the database instance.
        self.database_password = database_password
        # The account that is used to log on to the database.
        self.database_user = database_user
        # The ID of the database administrator (DBA) of the database instance.
        self.dba_id = dba_id
        # The nickname of the DBA of the instance.
        self.dba_nick_name = dba_nick_name
        # Indicates whether the lock-free schema change feature is enabled for the database instance.
        self.ddl_online = ddl_online
        # The ID of the ECS instance on which the database instance is deployed.
        self.ecs_instance_id = ecs_instance_id
        # The ID of the region in which the database instance resides.
        self.ecs_region = ecs_region
        # The type of the environment to which the database instance belongs. Valid values:
        # 
        # *   **product:** production environment
        # *   **dev**: development environment
        # *   **pre**: pre-release environment
        # *   **test**: test environment
        # *   **sit**: SIT environment
        # *   **uat**: UAT environment
        # *   **pet**: stress testing environment
        # *   **stag:** staging environment
        self.env_type = env_type
        # The timeout period for exporting data from the database instance.
        self.export_timeout = export_timeout
        # The host address that is used to connect to the database instance.
        self.host = host
        # The alias of the database instance.
        self.instance_alias = instance_alias
        # The ID of the instance.
        self.instance_id = instance_id
        # The source of the database instance.
        self.instance_source = instance_source
        # The type of the database instance.
        self.instance_type = instance_type
        # The IDs of the owners of the database instance.
        self.owner_id_list = owner_id_list
        # The nicknames of the owners of the database instance.
        self.owner_name_list = owner_name_list
        # The port number that is used to connect to the database instance.
        self.port = port
        # The timeout period for querying data in the database instance.
        self.query_timeout = query_timeout
        # The ID of the security rule set of the database instance.
        self.safe_rule_id = safe_rule_id
        # Indicates whether the sensitive data protection feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.sell_sitd = sell_sitd
        self.sell_trust = sell_trust
        # The system ID (SID) of the database instance.
        self.sid = sid
        # The control mode of the database instance.
        self.standard_group = standard_group
        # The status of the database instance.
        self.state = state
        # Indicates whether the cross-database query feature is enabled for the database instance. Valid values:
        # 
        # *   **0**: disabled
        # *   **1:**: enabled
        self.use_dsql = use_dsql
        # The ID of the VPC to which the database instance belongs.
        self.vpc_id = vpc_id

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()
        if self.standard_group:
            self.standard_group.validate()

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

        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name

        if self.ddl_online is not None:
            result['DdlOnline'] = self.ddl_online

        if self.ecs_instance_id is not None:
            result['EcsInstanceId'] = self.ecs_instance_id

        if self.ecs_region is not None:
            result['EcsRegion'] = self.ecs_region

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

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()

        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()

        if self.port is not None:
            result['Port'] = self.port

        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout

        if self.safe_rule_id is not None:
            result['SafeRuleId'] = self.safe_rule_id

        if self.sell_sitd is not None:
            result['SellSitd'] = self.sell_sitd

        if self.sell_trust is not None:
            result['SellTrust'] = self.sell_trust

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.standard_group is not None:
            result['StandardGroup'] = self.standard_group.to_map()

        if self.state is not None:
            result['State'] = self.state

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

        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')

        if m.get('DdlOnline') is not None:
            self.ddl_online = m.get('DdlOnline')

        if m.get('EcsInstanceId') is not None:
            self.ecs_instance_id = m.get('EcsInstanceId')

        if m.get('EcsRegion') is not None:
            self.ecs_region = m.get('EcsRegion')

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

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstanceListInstanceOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstanceListInstanceOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')

        if m.get('SafeRuleId') is not None:
            self.safe_rule_id = m.get('SafeRuleId')

        if m.get('SellSitd') is not None:
            self.sell_sitd = m.get('SellSitd')

        if m.get('SellTrust') is not None:
            self.sell_trust = m.get('SellTrust')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('StandardGroup') is not None:
            temp_model = main_models.ListInstancesResponseBodyInstanceListInstanceStandardGroup()
            self.standard_group = temp_model.from_map(m.get('StandardGroup'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('UseDsql') is not None:
            self.use_dsql = m.get('UseDsql')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListInstancesResponseBodyInstanceListInstanceStandardGroup(DaraModel):
    def __init__(
        self,
        group_mode: str = None,
        group_name: str = None,
    ):
        # The type of the control mode. Valid values:
        # 
        # *   **COMMON**: Security Collaboration
        # *   **NONE_CONTROL**: Flexible Management
        # *   **STABLE**: Stable Change
        self.group_mode = group_mode
        # The name of the security rule corresponding to the control mode.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_mode is not None:
            result['GroupMode'] = self.group_mode

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupMode') is not None:
            self.group_mode = m.get('GroupMode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

class ListInstancesResponseBodyInstanceListInstanceOwnerNameList(DaraModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')

        return self

class ListInstancesResponseBodyInstanceListInstanceOwnerIdList(DaraModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        return self

