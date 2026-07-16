# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class GetExecutorConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetExecutorConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned for the request.
        self.code = code
        # The configuration data for the Executor.
        self.data = data
        # The error message returned if the request fails.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.GetExecutorConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetExecutorConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        config: str = None,
        executor_type: str = None,
    ):
        # The default global configuration for Data Integration tasks. This configuration specifies the default handling policies for different types of DDL messages. Example:
        # `{"RENAMECOLUMN":"WARNING","DROPTABLE":"WARNING","CREATETABLE":"WARNING","MODIFYCOLUMN":"WARNING","TRUNCATETABLE":"WARNING","DROPCOLUMN":"WARNING","ADDCOLUMN":"WARNING","RENAMETABLE":"WARNING"}`
        # 
        # The DDL message types are as follows:
        # 
        # - RENAMECOLUMN: `RENAME COLUMN`
        # 
        # - DROPTABLE: `DROP TABLE`
        # 
        # - CREATETABLE: `CREATE TABLE`
        # 
        # - MODIFYCOLUMN: `MODIFY COLUMN`
        # 
        # - TRUNCATETABLE: `TRUNCATE TABLE`
        # 
        # - DROPCOLUMN: `DROP COLUMN`
        # 
        # - ADDCOLUMN: `ADD COLUMN`
        # 
        # - RENAMETABLE: `RENAME TABLE`
        # 
        # When DataWorks receives a DDL message, it applies one of the following handling policies:
        # 
        # - WARNING: Discards the message and logs a warning in the Real-time Synchronization Task log.
        # 
        # - IGNORE: Discards the message without sending it to the Destination Data Source.
        # 
        # - CRITICAL: Causes the Real-time Synchronization Task to fail.
        # 
        # - NORMAL: Forwards the message to the Destination Data Source. Because handling of DDL messages can vary by Destination Data Source, DataWorks only forwards the message.
        self.config = config
        # The type of the Executor.
        self.executor_type = executor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.executor_type is not None:
            result['ExecutorType'] = self.executor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ExecutorType') is not None:
            self.executor_type = m.get('ExecutorType')

        return self

