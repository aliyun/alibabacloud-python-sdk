# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeHanaDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        hana_databases: main_models.DescribeHanaDatabasesResponseBodyHanaDatabases = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The response code. The status code 200 indicates that the request was successful.
        self.code = code
        # The information about SAP HANA databases.
        self.hana_databases = hana_databases
        # The returned message. If the request was successful, "successful" is returned. If the request failed, an error message is returned.
        self.message = message
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.hana_databases:
            self.hana_databases.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hana_databases is not None:
            result['HanaDatabases'] = self.hana_databases.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HanaDatabases') is not None:
            temp_model = main_models.DescribeHanaDatabasesResponseBodyHanaDatabases()
            self.hana_databases = temp_model.from_map(m.get('HanaDatabases'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHanaDatabasesResponseBodyHanaDatabases(DaraModel):
    def __init__(
        self,
        hana_database: List[main_models.DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase] = None,
    ):
        self.hana_database = hana_database

    def validate(self):
        if self.hana_database:
            for v1 in self.hana_database:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HanaDatabase'] = []
        if self.hana_database is not None:
            for k1 in self.hana_database:
                result['HanaDatabase'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hana_database = []
        if m.get('HanaDatabase') is not None:
            for k1 in m.get('HanaDatabase'):
                temp_model = main_models.DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase()
                self.hana_database.append(temp_model.from_map(k1))

        return self

class DescribeHanaDatabasesResponseBodyHanaDatabasesHanaDatabase(DaraModel):
    def __init__(
        self,
        active_status: str = None,
        database_name: str = None,
        detail: str = None,
        host: str = None,
        service_name: str = None,
        sql_port: int = None,
    ):
        # Indicates whether the database is started. Valid values:
        # 
        # *   **YES**: The database is started.
        # *   **NO**: The database is not started.
        self.active_status = active_status
        # The database name.
        self.database_name = database_name
        # The detailed information.
        self.detail = detail
        # The hostname.
        self.host = host
        # The service name.
        self.service_name = service_name
        # The port number.
        self.sql_port = sql_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_status is not None:
            result['ActiveStatus'] = self.active_status

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.host is not None:
            result['Host'] = self.host

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.sql_port is not None:
            result['SqlPort'] = self.sql_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveStatus') is not None:
            self.active_status = m.get('ActiveStatus')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SqlPort') is not None:
            self.sql_port = m.get('SqlPort')

        return self

