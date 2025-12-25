# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDBTopologyResponseBody(DaraModel):
    def __init__(
        self,
        dbtopology: main_models.GetDBTopologyResponseBodyDBTopology = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The topology of the data table.
        self.dbtopology = dbtopology
        # The error code.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   **true**: The request is successful.
        # *   **false**: The request fails.
        self.success = success

    def validate(self):
        if self.dbtopology:
            self.dbtopology.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbtopology is not None:
            result['DBTopology'] = self.dbtopology.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTopology') is not None:
            temp_model = main_models.GetDBTopologyResponseBodyDBTopology()
            self.dbtopology = temp_model.from_map(m.get('DBTopology'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDBTopologyResponseBodyDBTopology(DaraModel):
    def __init__(
        self,
        alias: str = None,
        dbtopology_info_list: List[main_models.GetDBTopologyResponseBodyDBTopologyDBTopologyInfoList] = None,
        db_type: str = None,
        env_type: str = None,
        logic_db_id: int = None,
        logic_db_name: str = None,
        search_name: str = None,
    ):
        # The alias of the access point.
        self.alias = alias
        # The list of database splitting topology information.
        self.dbtopology_info_list = dbtopology_info_list
        # The type of the database engine.
        self.db_type = db_type
        # The type of the environment in which the database instance is deployed. Valid values:
        # 
        # *   product: production environment
        # *   dev: development environment
        # *   pre: pre-release environment
        # *   test: test environment
        # *   sit: system integration testing (SIT) environment
        # *   uat: user acceptance testing (UAT) environment
        # *   pet: stress testing environment
        # *   stag: staging environment
        self.env_type = env_type
        # The ID of the logical database.
        self.logic_db_id = logic_db_id
        # Logical database name.
        self.logic_db_name = logic_db_name
        # The name of the saved search.
        self.search_name = search_name

    def validate(self):
        if self.dbtopology_info_list:
            for v1 in self.dbtopology_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        result['DBTopologyInfoList'] = []
        if self.dbtopology_info_list is not None:
            for k1 in self.dbtopology_info_list:
                result['DBTopologyInfoList'].append(k1.to_map() if k1 else None)

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic_db_id is not None:
            result['LogicDbId'] = self.logic_db_id

        if self.logic_db_name is not None:
            result['LogicDbName'] = self.logic_db_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        self.dbtopology_info_list = []
        if m.get('DBTopologyInfoList') is not None:
            for k1 in m.get('DBTopologyInfoList'):
                temp_model = main_models.GetDBTopologyResponseBodyDBTopologyDBTopologyInfoList()
                self.dbtopology_info_list.append(temp_model.from_map(k1))

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('LogicDbId') is not None:
            self.logic_db_id = m.get('LogicDbId')

        if m.get('LogicDbName') is not None:
            self.logic_db_name = m.get('LogicDbName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class GetDBTopologyResponseBodyDBTopologyDBTopologyInfoList(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        instance_id: int = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        region_id: str = None,
        schema_name: str = None,
        search_name: str = None,
    ):
        # The name of the catalog to which the database belongs.
        # 
        # > If the database is a PostgreSQL database, the value of this parameter is the name of the database.
        self.catalog_name = catalog_name
        # The ID of the database for which the schema design is executed.
        self.db_id = db_id
        # The type of the database engine.
        self.db_type = db_type
        # The type of the environment to which the database belongs. Valid values:
        # 
        # *   product: production environment
        # *   dev: development environment
        # *   pre: staging environment
        # *   test: test environment
        # *   sit: SIT environment
        # *   uat: user acceptance testing (UAT) environment
        # *   pet: stress testing environment
        # *   stag: STAG environment
        self.env_type = env_type
        # The ID of the instance. The valid value is returned if you call the ListInstances operation. The instance ID is not the ID of the RDS instance.
        self.instance_id = instance_id
        # Instance resource ID.
        self.instance_resource_id = instance_resource_id
        # The source of the database instance. Valid values:
        # 
        # *   **PUBLIC_OWN:** a self-managed database instance that is deployed on the Internet
        # *   **RDS:** an ApsaraDB RDS instance
        # *   **ECS_OWN:** a self-managed database that is deployed on an Elastic Compute Service (ECS) instance
        # *   **VPC_IDC:** a self-managed database instance that is deployed in a data center connected over a virtual private cloud (VPC)
        self.instance_source = instance_source
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The name of the logical database.
        # 
        # > If the database is a PostgreSQL database, the value of this parameter is the name of the database schema.
        self.schema_name = schema_name
        # The name of the saved search.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_resource_id is not None:
            result['InstanceResourceId'] = self.instance_resource_id

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceResourceId') is not None:
            self.instance_resource_id = m.get('InstanceResourceId')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

