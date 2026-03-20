# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        access_token: str = None,
        endpoints: List[main_models.DescribeGroupEndpointsResponseBodyEndpoints] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The service token.
        self.access_token = access_token
        # The endpoints of the service group.
        self.endpoints = endpoints
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_token is not None:
            result['AccessToken'] = self.access_token

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.DescribeGroupEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupEndpointsResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        backend_id: str = None,
        endpoint_type: str = None,
        internet_endpoints: List[str] = None,
        intranet_endpoints: List[str] = None,
        path_type: str = None,
        port: int = None,
    ):
        # The backend access ID, which varies based on the value of the EndpointType parameter.
        # 
        # *   If you set EndpointType to DefaultGateway, the value of this parameter is default.
        # *   If you set EndpointType to PrivateGateway, the value of this parameter is the ID of the dedicated gateway.
        # *   If you set EndpointType to Nlb, the value of this parameter is the ID of the NLB instance.
        # *   If you set EndpointType to Nacos, the value of this parameter is the ID of the Nacos instance.
        self.backend_id = backend_id
        # The service endpoint type. Valid values:
        # 
        # *   DefaultGateway: the shared gateway.
        # *   PrivateGateway: the dedicated gateway.
        # *   Nlb: Associate the service with the Network Load Balancer (NLB) instance.
        # *   Nacos: Associate the service with the Nacos instance.
        self.endpoint_type = endpoint_type
        # The full endpoint.
        self.internet_endpoints = internet_endpoints
        # The full endpoint.
        self.intranet_endpoints = intranet_endpoints
        # The path type. Valid values:
        # 
        # *   Group: the path of the service group.
        self.path_type = path_type
        # The port number. This parameter takes effect only when you associate the service with an NLB or Nacos instance.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_id is not None:
            result['BackendId'] = self.backend_id

        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type

        if self.internet_endpoints is not None:
            result['InternetEndpoints'] = self.internet_endpoints

        if self.intranet_endpoints is not None:
            result['IntranetEndpoints'] = self.intranet_endpoints

        if self.path_type is not None:
            result['PathType'] = self.path_type

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendId') is not None:
            self.backend_id = m.get('BackendId')

        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')

        if m.get('InternetEndpoints') is not None:
            self.internet_endpoints = m.get('InternetEndpoints')

        if m.get('IntranetEndpoints') is not None:
            self.intranet_endpoints = m.get('IntranetEndpoints')

        if m.get('PathType') is not None:
            self.path_type = m.get('PathType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

