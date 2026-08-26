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
        # The list of endpoints.
        self.items = items
        # The request ID.
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
        address_items: List[main_models.DescribeAgenticDBBranchEndpointsResponseBodyItemsAddressItems] = None,
        connection_string: str = None,
        database: str = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        password: str = None,
        port: int = None,
    ):
        # The account name.
        self.account = account
        # The compatible connection address. The public endpoint is returned first. If no public endpoint is available, the private endpoint is returned.
        self.address = address
        # The list of public and private network endpoints.
        self.address_items = address_items
        # The compatible connection string. The public connection string is returned first. If no public connection string is available, the private connection string is returned.
        self.connection_string = connection_string
        # The database name.
        self.database = database
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The endpoint type.
        self.endpoint_type = endpoint_type
        # The password.
        self.password = password
        # The compatible connection port that corresponds to the Address parameter.
        self.port = port

    def validate(self):
        if self.address_items:
            for v1 in self.address_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.address is not None:
            result['Address'] = self.address

        result['AddressItems'] = []
        if self.address_items is not None:
            for k1 in self.address_items:
                result['AddressItems'].append(k1.to_map() if k1 else None)

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

        self.address_items = []
        if m.get('AddressItems') is not None:
            for k1 in m.get('AddressItems'):
                temp_model = main_models.DescribeAgenticDBBranchEndpointsResponseBodyItemsAddressItems()
                self.address_items.append(temp_model.from_map(k1))

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

class DescribeAgenticDBBranchEndpointsResponseBodyItemsAddressItems(DaraModel):
    def __init__(
        self,
        address: str = None,
        connection_string: str = None,
        net_type: str = None,
        port: int = None,
    ):
        # The endpoint.
        self.address = address
        # The full PostgreSQL connection string.
        self.connection_string = connection_string
        # The network type. Valid values: Private and Public.
        self.net_type = net_type
        # The port.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

