# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        dbinstance_endpoints: List[main_models.DescribeInstanceEndpointsResponseBodyDBInstanceEndpoints] = None,
        instance_endpoints: List[main_models.DescribeInstanceEndpointsResponseBodyInstanceEndpoints] = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.branch_name = branch_name
        # The endpoints of the database instance.
        self.dbinstance_endpoints = dbinstance_endpoints
        # The endpoints of the AI application instance.
        self.instance_endpoints = instance_endpoints
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbinstance_endpoints:
            for v1 in self.dbinstance_endpoints:
                 if v1:
                    v1.validate()
        if self.instance_endpoints:
            for v1 in self.instance_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        result['DBInstanceEndpoints'] = []
        if self.dbinstance_endpoints is not None:
            for k1 in self.dbinstance_endpoints:
                result['DBInstanceEndpoints'].append(k1.to_map() if k1 else None)

        result['InstanceEndpoints'] = []
        if self.instance_endpoints is not None:
            for k1 in self.instance_endpoints:
                result['InstanceEndpoints'].append(k1.to_map() if k1 else None)

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        self.dbinstance_endpoints = []
        if m.get('DBInstanceEndpoints') is not None:
            for k1 in m.get('DBInstanceEndpoints'):
                temp_model = main_models.DescribeInstanceEndpointsResponseBodyDBInstanceEndpoints()
                self.dbinstance_endpoints.append(temp_model.from_map(k1))

        self.instance_endpoints = []
        if m.get('InstanceEndpoints') is not None:
            for k1 in m.get('InstanceEndpoints'):
                temp_model = main_models.DescribeInstanceEndpointsResponseBodyInstanceEndpoints()
                self.instance_endpoints.append(temp_model.from_map(k1))

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceEndpointsResponseBodyInstanceEndpoints(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        domain: str = None,
        ip: str = None,
        ip_type: str = None,
        port: str = None,
    ):
        # The endpoint.
        self.connection_string = connection_string
        self.domain = domain
        # The IP address.
        self.ip = ip
        # The network type. Valid values:
        # 
        # - **public**: Internet.
        # - **vpc**: private network.
        self.ip_type = ip_type
        # The connection port.
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

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.ip is not None:
            result['IP'] = self.ip

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class DescribeInstanceEndpointsResponseBodyDBInstanceEndpoints(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        ip_type: str = None,
        port: str = None,
    ):
        # The endpoint.
        self.connection_string = connection_string
        # The network type. Valid values:
        # 
        # - **public**: Internet.
        # - **vpc**: private network.
        self.ip_type = ip_type
        # The connection port.
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

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

