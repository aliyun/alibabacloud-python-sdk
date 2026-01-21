# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListOperationDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        databases: List[main_models.ListOperationDatabasesResponseBodyDatabases] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The databases returned.
        self.databases = databases
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.databases:
            for v1 in self.databases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Databases'] = []
        if self.databases is not None:
            for k1 in self.databases:
                result['Databases'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.databases = []
        if m.get('Databases') is not None:
            for k1 in m.get('Databases'):
                temp_model = main_models.ListOperationDatabasesResponseBodyDatabases()
                self.databases.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOperationDatabasesResponseBodyDatabases(DaraModel):
    def __init__(
        self,
        active_address_type: str = None,
        comment: str = None,
        database_id: str = None,
        database_name: str = None,
        database_port: int = None,
        database_private_address: str = None,
        database_public_address: str = None,
        database_type: str = None,
        source: str = None,
        source_instance_id: str = None,
        source_instance_region_id: str = None,
        source_instance_state: str = None,
    ):
        # The address type of the database. Valid values:
        # 
        # *   **Public**
        # *   **Private**
        self.active_address_type = active_address_type
        # The remarks of the database.
        self.comment = comment
        # The database ID.
        self.database_id = database_id
        # The database name.
        self.database_name = database_name
        # The port of the database.
        self.database_port = database_port
        # The private address of the database.
        self.database_private_address = database_private_address
        # The public address of the database.
        self.database_public_address = database_public_address
        # The database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **PostgreSQL**
        # *   **Oracle**
        # *   **SQLServer**
        self.database_type = database_type
        # The database type. Valid values:
        # 
        # *   **Local**: on-premises database.
        # *   **Rds**: ApsaraDB RDS instance.
        # *   **PolarDB**: PolarDB cluster.
        self.source = source
        # The ID of the ApsaraDB RDS instance.
        self.source_instance_id = source_instance_id
        # The region ID of the ApsaraDB RDS instance.
        self.source_instance_region_id = source_instance_region_id
        # The database status. Valid values:
        # 
        # *   **Normal**
        # *   **Release**
        self.source_instance_state = source_instance_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.database_port is not None:
            result['DatabasePort'] = self.database_port

        if self.database_private_address is not None:
            result['DatabasePrivateAddress'] = self.database_private_address

        if self.database_public_address is not None:
            result['DatabasePublicAddress'] = self.database_public_address

        if self.database_type is not None:
            result['DatabaseType'] = self.database_type

        if self.source is not None:
            result['Source'] = self.source

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_instance_region_id is not None:
            result['SourceInstanceRegionId'] = self.source_instance_region_id

        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('DatabasePort') is not None:
            self.database_port = m.get('DatabasePort')

        if m.get('DatabasePrivateAddress') is not None:
            self.database_private_address = m.get('DatabasePrivateAddress')

        if m.get('DatabasePublicAddress') is not None:
            self.database_public_address = m.get('DatabasePublicAddress')

        if m.get('DatabaseType') is not None:
            self.database_type = m.get('DatabaseType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceInstanceRegionId') is not None:
            self.source_instance_region_id = m.get('SourceInstanceRegionId')

        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')

        return self

