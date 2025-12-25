# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTableDBTopologyResponseBody(DaraModel):
    def __init__(
        self,
        dbtopology: main_models.GetTableDBTopologyResponseBodyDBTopology = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The topology of the data table.
        self.dbtopology = dbtopology
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.GetTableDBTopologyResponseBodyDBTopology()
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

class GetTableDBTopologyResponseBodyDBTopology(DaraModel):
    def __init__(
        self,
        data_source_list: List[main_models.GetTableDBTopologyResponseBodyDBTopologyDataSourceList] = None,
        table_guid: str = None,
        table_name: str = None,
    ):
        # The data sources.
        self.data_source_list = data_source_list
        # The GUID of the table in DMS.
        self.table_guid = table_guid
        # The name of the table.
        # 
        # > 
        # 
        # *   If a logical table is queried, the name of the logical table is returned.
        # 
        # *   If a physical table is queried, the name of the physical table is returned.
        self.table_name = table_name

    def validate(self):
        if self.data_source_list:
            for v1 in self.data_source_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataSourceList'] = []
        if self.data_source_list is not None:
            for k1 in self.data_source_list:
                result['DataSourceList'].append(k1.to_map() if k1 else None)

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_list = []
        if m.get('DataSourceList') is not None:
            for k1 in m.get('DataSourceList'):
                temp_model = main_models.GetTableDBTopologyResponseBodyDBTopologyDataSourceList()
                self.data_source_list.append(temp_model.from_map(k1))

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetTableDBTopologyResponseBodyDBTopologyDataSourceList(DaraModel):
    def __init__(
        self,
        database_list: List[main_models.GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList] = None,
        db_type: str = None,
        host: str = None,
        port: int = None,
        sid: str = None,
    ):
        # The physical databases.
        self.database_list = database_list
        # The type of the database. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The endpoint of the data source.
        self.host = host
        # The port that is used to connect to the data source.
        self.port = port
        # The system ID (SID) of the data source.
        self.sid = sid

    def validate(self):
        if self.database_list:
            for v1 in self.database_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DatabaseList'] = []
        if self.database_list is not None:
            for k1 in self.database_list:
                result['DatabaseList'].append(k1.to_map() if k1 else None)

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.host is not None:
            result['Host'] = self.host

        if self.port is not None:
            result['Port'] = self.port

        if self.sid is not None:
            result['Sid'] = self.sid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database_list = []
        if m.get('DatabaseList') is not None:
            for k1 in m.get('DatabaseList'):
                temp_model = main_models.GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList()
                self.database_list.append(temp_model.from_map(k1))

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        return self

class GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseList(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        db_name: str = None,
        db_type: str = None,
        env_type: str = None,
        table_list: List[main_models.GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList] = None,
    ):
        # The ID of the database.
        self.db_id = db_id
        # The name of the database.
        self.db_name = db_name
        # The type of the database. For more information about the valid values of this parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The type of the environment to which the database belongs. Valid values:
        # 
        # *   **product**: production environment
        # *   **dev**: development environment
        # *   **pre**: pre-release environment
        # *   **test**: test environment
        # *   **sit**: system integration testing (SIT) environment
        # *   **uat**: user acceptance testing (UAT) environment
        # *   **pet**: stress testing environment
        # *   **stag**: staging environment
        # 
        # > For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # The physical tables.
        self.table_list = table_list

    def validate(self):
        if self.table_list:
            for v1 in self.table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        result['TableList'] = []
        if self.table_list is not None:
            for k1 in self.table_list:
                result['TableList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        self.table_list = []
        if m.get('TableList') is not None:
            for k1 in m.get('TableList'):
                temp_model = main_models.GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList()
                self.table_list.append(temp_model.from_map(k1))

        return self

class GetTableDBTopologyResponseBodyDBTopologyDataSourceListDatabaseListTableList(DaraModel):
    def __init__(
        self,
        table_id: str = None,
        table_name: str = None,
        table_type: str = None,
    ):
        # The ID of the table.
        self.table_id = table_id
        # The name of the physical table.
        self.table_name = table_name
        # The type of the table. This is a reserved parameter.
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_type is not None:
            result['TableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        return self

