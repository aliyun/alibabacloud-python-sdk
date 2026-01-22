# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class ModifyDBInstanceConnectionStringResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ModifyDBInstanceConnectionStringResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ModifyDBInstanceConnectionStringResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ModifyDBInstanceConnectionStringResponseBodyData(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_name: str = None,
        dbinstance_net_type: str = None,
        port: str = None,
    ):
        self.connection_string = connection_string
        self.dbinstance_name = dbinstance_name
        self.dbinstance_net_type = dbinstance_net_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

