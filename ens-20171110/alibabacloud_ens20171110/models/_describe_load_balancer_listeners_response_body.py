# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerListenersResponseBody(DaraModel):
    def __init__(
        self,
        listeners: main_models.DescribeLoadBalancerListenersResponseBodyListeners = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The listeners of the ELB instance.
        self.listeners = listeners
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            self.listeners.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListeners()
            self.listeners = temp_model.from_map(m.get('Listeners'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLoadBalancerListenersResponseBodyListeners(DaraModel):
    def __init__(
        self,
        listener: List[main_models.DescribeLoadBalancerListenersResponseBodyListenersListener] = None,
    ):
        self.listener = listener

    def validate(self):
        if self.listener:
            for v1 in self.listener:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listener'] = []
        if self.listener is not None:
            for k1 in self.listener:
                result['Listener'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listener = []
        if m.get('Listener') is not None:
            for k1 in m.get('Listener'):
                temp_model = main_models.DescribeLoadBalancerListenersResponseBodyListenersListener()
                self.listener.append(temp_model.from_map(k1))

        return self

class DescribeLoadBalancerListenersResponseBodyListenersListener(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        create_time: str = None,
        description: str = None,
        forward_port: str = None,
        listener_forward: str = None,
        listener_port: str = None,
        load_balancer_id: str = None,
        protocol: str = None,
        status: str = None,
    ):
        # The backend port that is used by the ELB instance. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The timestamp when the listener was created.
        self.create_time = create_time
        # The description of the listener.
        self.description = description
        # The listener port that is used for HTTP-to-HTTPS redirection.
        self.forward_port = forward_port
        # Indicates whether HTTP-to-HTTPS redirection is enabled for the listener. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.listener_forward = listener_forward
        # The listening port.
        self.listener_port = listener_port
        # The ID of the ELB instance.
        self.load_balancer_id = load_balancer_id
        # The network transmission protocol that is used by the listener.
        # 
        # *   **tcp**
        # *   **udp**
        # *   **http**
        # *   **https**
        self.protocol = protocol
        # The status of the listener. Valid values:
        # 
        # *   **running**
        # *   **stopped**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

