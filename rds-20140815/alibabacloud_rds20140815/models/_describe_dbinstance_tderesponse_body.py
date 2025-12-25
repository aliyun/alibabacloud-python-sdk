# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceTDEResponseBody(DaraModel):
    def __init__(
        self,
        databases: main_models.DescribeDBInstanceTDEResponseBodyDatabases = None,
        encryption_key: str = None,
        request_id: str = None,
        tdemode: str = None,
        tdestatus: str = None,
    ):
        # The TDE status at the database level.
        # 
        # >  If your instance runs SQL Server 2019 SE or SQL Server EE, you can specify whether to enable TDE at the database level when you enable TDE at the instance level.
        self.databases = databases
        # The ID of the custom key.
        self.encryption_key = encryption_key
        # The ID of the request.
        self.request_id = request_id
        # The method that is used to generate the key for TDE at the instance level. Valid values:
        # 
        # *   **Aliyun_Generate_Key**
        # *   **Customer_Provided_Key**
        # *   **Unknown**
        self.tdemode = tdemode
        # The TDE status of the instance. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.tdestatus = tdestatus

    def validate(self):
        if self.databases:
            self.databases.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.databases is not None:
            result['Databases'] = self.databases.to_map()

        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tdemode is not None:
            result['TDEMode'] = self.tdemode

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Databases') is not None:
            temp_model = main_models.DescribeDBInstanceTDEResponseBodyDatabases()
            self.databases = temp_model.from_map(m.get('Databases'))

        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TDEMode') is not None:
            self.tdemode = m.get('TDEMode')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

class DescribeDBInstanceTDEResponseBodyDatabases(DaraModel):
    def __init__(
        self,
        database: List[main_models.DescribeDBInstanceTDEResponseBodyDatabasesDatabase] = None,
    ):
        self.database = database

    def validate(self):
        if self.database:
            for v1 in self.database:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Database'] = []
        if self.database is not None:
            for k1 in self.database:
                result['Database'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database = []
        if m.get('Database') is not None:
            for k1 in m.get('Database'):
                temp_model = main_models.DescribeDBInstanceTDEResponseBodyDatabasesDatabase()
                self.database.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceTDEResponseBodyDatabasesDatabase(DaraModel):
    def __init__(
        self,
        dbname: str = None,
        tdestatus: str = None,
    ):
        # The name of the database.
        self.dbname = dbname
        # The TDE status at the database level. Valid values:
        # 
        # *   **Enabled**
        # *   **Disabled**
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

