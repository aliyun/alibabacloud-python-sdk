# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class DescribeModelServiceResponseBody(DaraModel):
    def __init__(
        self,
        ai_nodes: List[str] = None,
        api_key: str = None,
        create_time: str = None,
        description: str = None,
        model_name: str = None,
        model_params: Dict[str, Any] = None,
        model_service_id: str = None,
        private_connect_url: str = None,
        public_connect_url: str = None,
        request_id: str = None,
        security_ip_list: str = None,
        status: str = None,
    ):
        # The list of AI nodes.
        self.ai_nodes = ai_nodes
        # The API key.
        self.api_key = api_key
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # The model name.
        self.model_name = model_name
        # Model parameters.
        self.model_params = model_params
        # The model service ID.
        self.model_service_id = model_service_id
        # The internal endpoint.
        self.private_connect_url = private_connect_url
        # The public endpoint.
        self.public_connect_url = public_connect_url
        # Request ID.
        self.request_id = request_id
        # A comma-separated list of IP addresses and CIDR blocks allowed to connect.
        self.security_ip_list = security_ip_list
        # The status of the model service.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_nodes is not None:
            result['AiNodes'] = self.ai_nodes

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_params is not None:
            result['ModelParams'] = self.model_params

        if self.model_service_id is not None:
            result['ModelServiceId'] = self.model_service_id

        if self.private_connect_url is not None:
            result['PrivateConnectUrl'] = self.private_connect_url

        if self.public_connect_url is not None:
            result['PublicConnectUrl'] = self.public_connect_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiNodes') is not None:
            self.ai_nodes = m.get('AiNodes')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelParams') is not None:
            self.model_params = m.get('ModelParams')

        if m.get('ModelServiceId') is not None:
            self.model_service_id = m.get('ModelServiceId')

        if m.get('PrivateConnectUrl') is not None:
            self.private_connect_url = m.get('PrivateConnectUrl')

        if m.get('PublicConnectUrl') is not None:
            self.public_connect_url = m.get('PublicConnectUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

