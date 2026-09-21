# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetRequestDiagnosisResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetRequestDiagnosisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The response message.
        # 
        # > This parameter returns `Successful` if the request succeeds. If the request fails, it returns an error message, which may include an error code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request succeeded.
        # 
        # - **false**: The request failed.
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
            temp_model = main_models.GetRequestDiagnosisResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRequestDiagnosisResultResponseBodyData(DaraModel):
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
        # The database name.
        self.db_schema = db_schema
        # The database engine. Valid values:
        # 
        # - **MySQL**
        # 
        # - **PostgreSQL**
        # 
        # - **SQL Server**
        # 
        # - **PolarDB-X**
        # 
        # - **PolarDB for Oracle**
        # 
        # - **MongoDB**
        self.engine = engine
        # The creation time of the SQL diagnosis, provided as a Unix timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The last modification time of the SQL diagnosis, provided as a Unix timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The unique ID of the diagnosis.
        self.message_id = message_id
        # Additional information.
        self.param = param
        # The details of the SQL diagnosis result, returned as a JSON-formatted string.
        # 
        # - **endTime**: The end time of the SQL diagnosis.
        # 
        # - **errorCode**: The error code.
        # 
        #   - **0001**: The diagnosis was successful.
        # 
        #   - **0003**: The diagnosis failed.
        # 
        # - **errorMessage**: The error message.
        # 
        # - **estimateCost**: The estimated cost.
        # 
        #   - **cpu**: The estimated CPU cost of the query.
        # 
        #   - **io**: The estimated I/O cost of the query.
        # 
        #   - **rows**: The estimated number of rows returned by the query.
        # 
        # - **improvement**: The performance improvement ratio.
        # 
        # - **indexAdvices**: The index suggestions.
        # 
        #   - **columns**: The index columns.
        # 
        #   - **ddlAddIndex**: The DDL statement for creating the index.
        # 
        #   - **indexName**: The index name.
        # 
        #   - **schemaName**: The schema name.
        # 
        #   - **tableName**: The table name.
        # 
        #   - **unique**: Indicates whether the index is a unique index.
        # 
        # - **ip**: The instance IP address.
        # 
        # - **messageId**: The diagnosis ID.
        # 
        # - **port**: The instance port.
        # 
        # - **sqlTag**: The SQL tags.
        # 
        #   - **PRED_EQUAL**: Equality predicate.
        # 
        #   - **CNT_QB**: Number of query blocks.
        # 
        #   - **CNT_TB**: Number of tables.
        # 
        #   - **JOIN_LEFT**: Left join.
        # 
        #   - **SEL_SMALL**: Small result set selection.
        # 
        #   - **AGGR_SEL**: Aggregate selection.
        # 
        #   - **PRED_LT_EQ / PRED_GT_EQ**: Less-than-or-equal-to / greater-than-or-equal-to predicate.
        # 
        #   - **PRED_LIKE_PREFIX**: LIKE prefix match.
        # 
        #   - **ORDER_BY**: Contains an ORDER BY clause.
        # 
        #   - **LIMIT**: Contains a LIMIT clause.
        # 
        #   - **GROUP_BY**: Contains a GROUP BY clause.
        # 
        #   - **JOIN_INNER**: Inner join.
        # 
        #   - **JOIN_RIGHT**: Right join.
        # 
        #   - **HAVING**: Contains a HAVING clause.
        # 
        #   - **UNION**: Contains a UNION operation.
        # 
        # - **startTime**: The start time of the SQL diagnosis.
        # 
        # - **success**: Indicates whether the diagnosis was successful.
        # 
        # - **support**: Indicates whether the SQL statement can be diagnosed.
        # 
        #   - **true**: Supported.
        # 
        #   - **false**: Not supported.
        # 
        # - **tuningAdvices**: The SQL rewrite suggestions.
        self.result = result
        # The SQL template ID.
        self.sql_id = sql_id
        # The diagnosis status. Valid values:
        # 
        # - **0**: In progress.
        # 
        # - **1**: Diagnosis error.
        # 
        # - **2**: Completed.
        # 
        # - **3**: SQL error.
        # 
        # - **4**: Engine error.
        self.state = state
        # The unique identifier of the diagnosed instance.
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

