# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
from darabonba.model import DaraModel

class GetListenerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        listener_description: str = None,
        listener_id: str = None,
        listener_status: str = None,
        load_balancer_id: str = None,
        region_id: str = None,
        request_id: str = None,
        server_group_id: str = None,
        tags: List[main_models.GetListenerAttributeResponseBodyTags] = None,
        tcp_idle_timeout: int = None,
    ):
        # The listener description.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (_), and hyphens (-).
        self.listener_description = listener_description
        # The listener ID.
        self.listener_id = listener_id
        # The listener status. Valid values:
        # 
        # *   **Provisioning**: The listener is being created.
        # *   **Running**: The listener is running.
        # *   **Configuring**: The listener is being configured.
        # *   **Deleting**: The listener is being deleted.
        self.listener_status = listener_status
        # The GWLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The region ID of the GWLB instance.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetListenerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TcpIdleTimeout') is not None:
            self.tcp_idle_timeout = m.get('TcpIdleTimeout')

        return self

class GetListenerAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key cannot be an empty string. The tag key can be up to 128 characters in length, and cannot start with `acs: `or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The tag value can be up to 256 characters in length and cannot contain `http://` or `https://`.
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

