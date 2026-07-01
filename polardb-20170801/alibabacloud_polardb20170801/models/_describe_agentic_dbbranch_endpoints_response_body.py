# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAgenticDBBranchEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAgenticDBBranchEndpointsResponseBodyItems] = None,
        request_id: str = None,
    ):
        self.items = items
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAgenticDBBranchEndpointsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAgenticDBBranchEndpointsResponseBodyItems(DaraModel):
    def __init__(
        self,
        account: str = None,
        address: str = None,
        connection_string: str = None,
        database: str = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        password: str = None,
        port: int = None,
    ):
        self.account = account
        self.address = address
        self.connection_string = connection_string
        self.database = database
        self.endpoint_id = endpoint_id
        self.endpoint_type = endpoint_type
        self.password = password
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.address is not None:
            result['Address'] = self.address

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.database is not None:
            result['Database'] = self.database

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.password is not None:
            result['Password'] = self.password

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

