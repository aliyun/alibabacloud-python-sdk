# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListDIProjectConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDIProjectConfigResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the query.
        self.data = data
        # The request ID.
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
            temp_model = main_models.ListDIProjectConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDIProjectConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        config: str = None,
    ):
        # The default global configuration of synchronization solutions. The value indicates the processing rules of different types of DDL messages. Example: {"RENAMECOLUMN":"WARNING","DROPTABLE":"WARNING","CREATETABLE":"WARNING","MODIFYCOLUMN":"WARNING","TRUNCATETABLE":"WARNING","DROPCOLUMN":"WARNING","ADDCOLUMN":"WARNING","RENAMETABLE":"WARNING"}
        # 
        # Field description:
        # 
        # *   RENAMECOLUMN: renames a column.
        # *   DROPTABLE: deletes a table.
        # *   CREATETABLE: creates a table.
        # *   MODIFYCOLUMN: changes the data type of a column.
        # *   TRUNCATETABLE: clears a table.
        # *   DROPCOLUMN: deletes a column.
        # *   ADDCOLUMN: creates a column.
        # *   RENAMETABLE: renames a table.
        # 
        # DataWorks processes a DDL message of a specific type based on the following rules:
        # 
        # *   WARNING: ignores the message and records an alert in real-time synchronization logs. The alert contains information about the situation that the message is ignored because of an execution error.
        # *   IGNORE: discards the message and does not send it to the destination.
        # *   CRITICAL: terminates the real-time synchronization node and sets the node status to Failed.
        # *   NORMAL: sends the message to the destination to process the message. Each destination processes DDL messages based on its own business logic. If DataWorks adopts the NORMAL policy, DataWorks only forwards DDL messages.
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        return self

