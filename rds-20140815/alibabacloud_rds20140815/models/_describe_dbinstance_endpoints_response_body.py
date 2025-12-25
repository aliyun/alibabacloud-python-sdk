# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceEndpointsResponseBodyData = None,
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
            temp_model = main_models.DescribeDBInstanceEndpointsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceEndpointsResponseBodyData(DaraModel):
    def __init__(
        self,
        dbinstance_endpoints: main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpoints = None,
        dbinstance_name: str = None,
        ip_version: str = None,
    ):
        # The information of the endpoints of the instance.
        self.dbinstance_endpoints = dbinstance_endpoints
        # The name of the instance.
        self.dbinstance_name = dbinstance_name
        # The version of the IP protocol. Valid values:
        # 
        # *   **ipv4**
        # *   **ipv6**
        self.ip_version = ip_version

    def validate(self):
        if self.dbinstance_endpoints:
            self.dbinstance_endpoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_endpoints is not None:
            result['DBInstanceEndpoints'] = self.dbinstance_endpoints.to_map()

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceEndpoints') is not None:
            temp_model = main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpoints()
            self.dbinstance_endpoints = temp_model.from_map(m.get('DBInstanceEndpoints'))

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        return self

class DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpoints(DaraModel):
    def __init__(
        self,
        dbinstance_endpoint: List[main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpoint] = None,
    ):
        self.dbinstance_endpoint = dbinstance_endpoint

    def validate(self):
        if self.dbinstance_endpoint:
            for v1 in self.dbinstance_endpoint:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceEndpoint'] = []
        if self.dbinstance_endpoint is not None:
            for k1 in self.dbinstance_endpoint:
                result['DBInstanceEndpoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_endpoint = []
        if m.get('DBInstanceEndpoint') is not None:
            for k1 in m.get('DBInstanceEndpoint'):
                temp_model = main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpoint()
                self.dbinstance_endpoint.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpoint(DaraModel):
    def __init__(
        self,
        address_items: main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointAddressItems = None,
        endpoint_description: str = None,
        endpoint_id: str = None,
        endpoint_type: str = None,
        node_items: main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointNodeItems = None,
    ):
        # The information about the endpoint.
        self.address_items = address_items
        # The user-defined description of the endpoint.
        self.endpoint_description = endpoint_description
        # The endpoint ID of the instance.
        self.endpoint_id = endpoint_id
        # The type of the endpoint. Valid values:
        # 
        # *   **Primary**: the read/write endpoint of the instance
        # *   **Readonly**: the read-only endpoint of the instance
        self.endpoint_type = endpoint_type
        # The information about the node that is configured for the endpoint.
        self.node_items = node_items

    def validate(self):
        if self.address_items:
            self.address_items.validate()
        if self.node_items:
            self.node_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_items is not None:
            result['AddressItems'] = self.address_items.to_map()

        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.node_items is not None:
            result['NodeItems'] = self.node_items.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressItems') is not None:
            temp_model = main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointAddressItems()
            self.address_items = temp_model.from_map(m.get('AddressItems'))

        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('NodeItems') is not None:
            temp_model = main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointNodeItems()
            self.node_items = temp_model.from_map(m.get('NodeItems'))

        return self

class DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointNodeItems(DaraModel):
    def __init__(
        self,
        node_item: List[main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointNodeItemsNodeItem] = None,
    ):
        self.node_item = node_item

    def validate(self):
        if self.node_item:
            for v1 in self.node_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NodeItem'] = []
        if self.node_item is not None:
            for k1 in self.node_item:
                result['NodeItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_item = []
        if m.get('NodeItem') is not None:
            for k1 in m.get('NodeItem'):
                temp_model = main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointNodeItemsNodeItem()
                self.node_item.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointNodeItemsNodeItem(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        node_id: str = None,
        weight: int = None,
    ):
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The node ID.
        self.node_id = node_id
        # The weight of the node. Read requests are distributed based on the weight.
        # 
        # Valid values: 0 to 100.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointAddressItems(DaraModel):
    def __init__(
        self,
        address_item: List[main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointAddressItemsAddressItem] = None,
    ):
        self.address_item = address_item

    def validate(self):
        if self.address_item:
            for v1 in self.address_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddressItem'] = []
        if self.address_item is not None:
            for k1 in self.address_item:
                result['AddressItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.address_item = []
        if m.get('AddressItem') is not None:
            for k1 in m.get('AddressItem'):
                temp_model = main_models.DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointAddressItemsAddressItem()
                self.address_item.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceEndpointsResponseBodyDataDBInstanceEndpointsDBInstanceEndpointAddressItemsAddressItem(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        ip_address: str = None,
        ip_type: str = None,
        port: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The endpoints of the instance.
        self.connection_string = connection_string
        # The IP address.
        self.ip_address = ip_address
        # The type of the IP address. Valid values:
        # 
        # *   **Public**: Internet
        # *   **Private**: internal network
        self.ip_type = ip_type
        # The port number of the endpoint.
        self.port = port
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.port is not None:
            result['Port'] = self.port

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

