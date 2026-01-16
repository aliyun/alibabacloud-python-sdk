# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class CreateVpcEndpointResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateVpcEndpointResponseBodyResult = None,
    ):
        # The endpoint domain name, which is used to configure the connection.
        self.request_id = request_id
        # The ID of the endpoint on the service VPC side.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CreateVpcEndpointResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CreateVpcEndpointResponseBodyResult(DaraModel):
    def __init__(
        self,
        endpoint_domain: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        service_id: str = None,
    ):
        self.endpoint_domain = endpoint_domain
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        # The name of the service VPC-side endpoint.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_domain is not None:
            result['endpointDomain'] = self.endpoint_domain

        if self.endpoint_id is not None:
            result['endpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['endpointName'] = self.endpoint_name

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpointDomain') is not None:
            self.endpoint_domain = m.get('endpointDomain')

        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')

        if m.get('endpointName') is not None:
            self.endpoint_name = m.get('endpointName')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

