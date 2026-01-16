# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListVpcEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListVpcEndpointsResponseBodyResult] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The details of the endpoints.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListVpcEndpointsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListVpcEndpointsResponseBodyResult(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        create_time: str = None,
        endpoint_business_status: str = None,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        endpoint_status: str = None,
        service_id: str = None,
        service_name: str = None,
    ):
        # The status of the endpoint connection. Valid values:
        # 
        # *   Pending
        # *   Connecting
        # *   Connected
        # *   Disconnecting
        # *   Disconnected
        # *   Deleting
        # *   ServiceDeleted
        self.connection_status = connection_status
        # The time when the endpoint was created.
        self.create_time = create_time
        # The business status of the endpoint. Valid values:
        # 
        # *   Normal
        # *   FinancialLocked
        self.endpoint_business_status = endpoint_business_status
        # The domain name of the endpoint. The domain name is used for connection configuration.
        self.endpoint_domain = endpoint_domain
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The name of the endpoint.
        self.endpoint_name = endpoint_name
        # The status of the endpoint. Valid values:
        # 
        # *   Creating
        # *   Active
        # *   Pending
        # *   Deleting
        self.endpoint_status = endpoint_status
        # The ID of the endpoint service with which the endpoint is associated.
        self.service_id = service_id
        # The name of the endpoint service with which the endpoint is associated.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['connectionStatus'] = self.connection_status

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.endpoint_business_status is not None:
            result['endpointBusinessStatus'] = self.endpoint_business_status

        if self.endpoint_domain is not None:
            result['endpointDomain'] = self.endpoint_domain

        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name

        if self.endpoint_status is not None:
            result['endpointStatus'] = self.endpoint_status

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionStatus') is not None:
            self.connection_status = m.get('connectionStatus')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('endpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('endpointBusinessStatus')

        if m.get('endpointDomain') is not None:
            self.endpoint_domain = m.get('endpointDomain')

        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')

        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')

        if m.get('endpointStatus') is not None:
            self.endpoint_status = m.get('endpointStatus')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

