# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTableTopologyResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        table_topology: main_models.GetTableTopologyResponseBodyTableTopology = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The topology information.
        self.table_topology = table_topology

    def validate(self):
        if self.table_topology:
            self.table_topology.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.table_topology is not None:
            result['TableTopology'] = self.table_topology.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TableTopology') is not None:
            temp_model = main_models.GetTableTopologyResponseBodyTableTopology()
            self.table_topology = temp_model.from_map(m.get('TableTopology'))

        return self

class GetTableTopologyResponseBodyTableTopology(DaraModel):
    def __init__(
        self,
        logic: bool = None,
        table_guid: str = None,
        table_name: str = None,
        table_topology_info_list: List[main_models.GetTableTopologyResponseBodyTableTopologyTableTopologyInfoList] = None,
    ):
        # Indicates whether the table is a logical table. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.logic = logic
        # The GUID of the table in DMS.
        self.table_guid = table_guid
        # The name of the table.
        self.table_name = table_name
        # Information of the topology of the table.
        self.table_topology_info_list = table_topology_info_list

    def validate(self):
        if self.table_topology_info_list:
            for v1 in self.table_topology_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logic is not None:
            result['Logic'] = self.logic

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        result['TableTopologyInfoList'] = []
        if self.table_topology_info_list is not None:
            for k1 in self.table_topology_info_list:
                result['TableTopologyInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        self.table_topology_info_list = []
        if m.get('TableTopologyInfoList') is not None:
            for k1 in m.get('TableTopologyInfoList'):
                temp_model = main_models.GetTableTopologyResponseBodyTableTopologyTableTopologyInfoList()
                self.table_topology_info_list.append(temp_model.from_map(k1))

        return self

class GetTableTopologyResponseBodyTableTopologyTableTopologyInfoList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_name: str = None,
        db_search_name: str = None,
        db_type: str = None,
        instance_id: int = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        region_id: str = None,
        table_count: int = None,
        table_name_expr: str = None,
        table_name_list: str = None,
    ):
        # The ID of the physical database.
        self.db_id = db_id
        # The name of the database.
        self.db_name = db_name
        # The name that is used to search for the database.
        # > We recommend that you do not use this parameter for business development. The format of the parameter value may be modified in later versions.
        self.db_search_name = db_search_name
        # The database engine.
        self.db_type = db_type
        # The ID of the instance to which the physical database belongs.
        self.instance_id = instance_id
        # The ID of the resource related to the instance. The resource corresponds with the database instance type returned in the InstanceSource parameter.
        # 
        # *   **RDS**:The ID of the ApsaraDB RDS instance.
        # *   **ECS_OWN**: The ID of the Elastic Compute Service (ECS) instance.
        # *   **PUBLIC_OWN**: This parameter is left empty for self-managed database instances that are connected over the Internet.
        # *   **VPC_ID**:The ID of the virtual private cloud (VPC).
        # *   **GATEWAY**: The ID of the database gateway.
        self.instance_resource_id = instance_resource_id
        # The type of the database instance. Valid values:
        # 
        # *   **RDS**: an ApsaraDB RDS instance.
        # *   **ECS_OWN**: a self-managed database that is deployed on an ECS instance
        # *   **PUBLIC_OWN**: a self-managed database instance that is connected over the Internet.
        # *   **VPC_ID**: a self-managed database instance in a VPC that is connected over Express Connect circuits.
        # *   **GATEWAY**: a database instance connected by using a database gateway.
        self.instance_source = instance_source
        # The region ID of the instance.
        self.region_id = region_id
        # The number of tables.
        self.table_count = table_count
        # The expression of the names of logical tables.
        # 
        # **
        # 
        # **Description** This parameter is not returned for physical tables.
        self.table_name_expr = table_name_expr
        # The names of tables.
        # 
        # > The table names are separated by commas (,).
        self.table_name_list = table_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_resource_id is not None:
            result['InstanceResourceId'] = self.instance_resource_id

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.table_count is not None:
            result['TableCount'] = self.table_count

        if self.table_name_expr is not None:
            result['TableNameExpr'] = self.table_name_expr

        if self.table_name_list is not None:
            result['TableNameList'] = self.table_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceResourceId') is not None:
            self.instance_resource_id = m.get('InstanceResourceId')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')

        if m.get('TableNameExpr') is not None:
            self.table_name_expr = m.get('TableNameExpr')

        if m.get('TableNameList') is not None:
            self.table_name_list = m.get('TableNameList')

        return self

