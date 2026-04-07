# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDataSourceMetaResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDataSourceMetaResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned result.
        self.data = data
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDataSourceMetaResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataSourceMetaResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        meta: str = None,
        status: str = None,
    ):
        # The reason why the metadata of the data source fails to be obtained. If the metadata of the data source is obtained, no value is returned for this parameter.
        self.message = message
        # The returned metadata of the data source. The returned metadata is in the JSON format.
        # 
        # `{"dbTables":[{"dbName":"testdb","schema":[{"tableInfos":[{"dbName":"testdb","enable":true,"table":"table1","tableName":"table1"}]},{"tableInfos":[{"dbName":"testdb","enable":true,"table":"table2","tableName":"table2"}]}]}]}`
        # 
        # Parameter description:
        # 
        # *   dbName: the name of the database in which the data source resides.
        # *   schema: the schema of the database.
        # *   enable: indicates whether the database is available. The valid values are true and false. The value true indicates that the database is available. The value false indicates that the database is unavailable.
        # *   tableName: the name of the table in the database.
        # *   tableInfos: the information about the table in the database.
        self.meta = meta
        # Indicates whether the metadata of the data source is obtained. Valid values:
        # 
        # *   success: The metadata of the data source is obtained.
        # *   fail: The metadata of the data source failed to be obtained. You can troubleshoot issues based on the Message parameter.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.meta is not None:
            result['Meta'] = self.meta

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Meta') is not None:
            self.meta = m.get('Meta')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

