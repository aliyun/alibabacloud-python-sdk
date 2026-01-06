# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetRequestDiagnosisPageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRequestDiagnosisPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, Successful is returned. If the request failed, an error message that contains information such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetRequestDiagnosisPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRequestDiagnosisPageResponseBodyData(DaraModel):
    def __init__(
        self,
        extra: str = None,
        list: List[main_models.GetRequestDiagnosisPageResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # Additional information.
        self.extra = extra
        # The SQL diagnostics records returned.
        self.list = list
        # The page number. The value must be a positive integer. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. The value must be a positive integer. Default value: 10.
        self.page_size = page_size
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['extra'] = self.extra

        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['pageNo'] = self.page_no

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')

        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.GetRequestDiagnosisPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetRequestDiagnosisPageResponseBodyDataList(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        db_schema: str = None,
        engine: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        message_id: str = None,
        param: str = None,
        result: str = None,
        sql_id: str = None,
        state: int = None,
        uuid: str = None,
    ):
        # The user ID.
        self.account_id = account_id
        # The name of the database.
        self.db_schema = db_schema
        # The database engine. Valid values:
        # 
        # * **MySQL**
        # * **PostgreSQL**
        # * **SQLServer**
        # * **PolarDBMySQL**
        # * **PolarDBOracle**
        # * **MongoDB**
        self.engine = engine
        # The time when the SQL diagnostics task was created. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_create = gmt_create
        # The time when the SQL diagnostics task was modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.gmt_modified = gmt_modified
        # The unique ID of the diagnostics task.
        self.message_id = message_id
        # Additional information.
        self.param = param
        # The result of the SQL diagnostics task. The result includes the following information:
        # 
        # * **endTime**: the end time of the SQL diagnostics task.
        # * **errorCode**: indicates whether the SQL diagnostics task is complete. Valid values:
        #   * **0001**: The SQL diagnostics task is complete.
        #   * **0003**: The SQL diagnostics task failed.
        # 
        # * **errorMessage**: the error message.
        # * **estimateCost**: the estimated cost.
        #   * **cpu**: the estimated CPU utilization of the index.
        #   * **io**: the estimated I/O usage of the index.
        #   * **rows**: the estimated values of the rows returned for the index.
        # * **improvement**: the performance improvement ratio.
        # * **indexAdvices**: the index recommendations, which include the following information:
        #   * **columns**: the index columns.
        #   * **ddlAddIndex**: the DDL statement for the index.
        #   * **indexName**: the name of the index.
        #   * **schemaName**: the name of the database.
        #   * **tableName**: the name of the table.
        #   * **unique**: indicates whether the index is unique.
        # 
        # * **ip**: the IP address of the instance.
        # * **messageId**: the ID of the diagnostics task.
        # * **port**: the port used to connect to the instance.
        # * **sqlTag**: the SQL tag.
        # * **startTime**: the start time of the SQL diagnostics task.
        # * **success**: indicates whether the request was successful.
        # * **support**: indicates whether the SQL statement can be diagnosed. Valid values:
        #   * **true**: The SQL statement can be diagnosed.
        #   * **false**: The SQL statement cannot be diagnosed.
        # 
        # * **tuningAdvices**: the SQL rewrite suggestions.
        self.result = result
        # The SQL template ID.
        self.sql_id = sql_id
        # The status of the diagnostics task. Valid values:
        # 
        # * **0**: The diagnostics task is in progress.
        # 
        # * **1**: A diagnostics error occurred.
        # 
        # * **2**: The diagnostics task is complete.
        # 
        # * **3**: An SQL error occurred.
        # 
        # * **4**: An engine error occurred.
        self.state = state
        # The unique ID of the diagnostics instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.db_schema is not None:
            result['dbSchema'] = self.db_schema

        if self.engine is not None:
            result['engine'] = self.engine

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message_id is not None:
            result['messageId'] = self.message_id

        if self.param is not None:
            result['param'] = self.param

        if self.result is not None:
            result['result'] = self.result

        if self.sql_id is not None:
            result['sqlId'] = self.sql_id

        if self.state is not None:
            result['state'] = self.state

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('dbSchema') is not None:
            self.db_schema = m.get('dbSchema')

        if m.get('engine') is not None:
            self.engine = m.get('engine')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('messageId') is not None:
            self.message_id = m.get('messageId')

        if m.get('param') is not None:
            self.param = m.get('param')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('sqlId') is not None:
            self.sql_id = m.get('sqlId')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

