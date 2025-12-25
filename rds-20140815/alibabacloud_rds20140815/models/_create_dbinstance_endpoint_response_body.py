# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateDBInstanceEndpointResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateDBInstanceEndpointResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateDBInstanceEndpointResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateDBInstanceEndpointResponseBodyData(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_endpoint_id: str = None,
        dbinstance_name: str = None,
    ):
        # The internal endpoint.
        self.connection_string = connection_string
        # The endpoint ID of the instance.
        self.dbinstance_endpoint_id = dbinstance_endpoint_id
        # The ID of the instance.
        self.dbinstance_name = dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_endpoint_id is not None:
            result['DBInstanceEndpointId'] = self.dbinstance_endpoint_id

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceEndpointId') is not None:
            self.dbinstance_endpoint_id = m.get('DBInstanceEndpointId')

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        return self

