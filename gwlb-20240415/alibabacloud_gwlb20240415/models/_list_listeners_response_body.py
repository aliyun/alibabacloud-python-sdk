# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
from darabonba.model import DaraModel

class ListListenersResponseBody(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.ListListenersResponseBodyListeners] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The GWLB listeners.
        self.listeners = listeners
        # The maximum number of results to be returned from a single query when the NextToken parameter is used in the query. Valid values: 1 to 1000. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['Listeners'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('Listeners') is not None:
            for k1 in m.get('Listeners'):
                temp_model = main_models.ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListListenersResponseBodyListeners(DaraModel):
    def __init__(
        self,
        listener_description: str = None,
        listener_id: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        server_group_id: str = None,
        tags: List[main_models.ListListenersResponseBodyListenersTags] = None,
        tcp_idle_timeout: int = None,
    ):
        # The description of the listener.
        self.listener_description = listener_description
        # The listener ID.
        self.listener_id = listener_id
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**: The listener is being created.
        # *   **Running**: The listener is running.
        # *   **Configuring**: The listener is being configured.
        # *   **Deleting**: The listener is being deleted.
        self.listener_status = listener_status
        # The GWLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The server group ID.
        self.server_group_id = server_group_id
        # The tags.
        self.tags = tags
        # The timeout period of an idle TCP connection. Unit: seconds.
        self.tcp_idle_timeout = tcp_idle_timeout

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tcp_idle_timeout is not None:
            result['TcpIdleTimeout'] = self.tcp_idle_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListListenersResponseBodyListenersTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TcpIdleTimeout') is not None:
            self.tcp_idle_timeout = m.get('TcpIdleTimeout')

        return self

class ListListenersResponseBodyListenersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

