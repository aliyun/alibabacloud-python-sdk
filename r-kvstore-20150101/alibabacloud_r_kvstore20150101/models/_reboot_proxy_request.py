# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootProxyRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        proxy_list: str = None,
        proxy_node_list: str = None,
        reboot_mode: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The IDs of the proxy nodes that you want to restart or rebuild. Separate multiple IDs with commas (,).
        self.proxy_list = proxy_list
        # The IDs of the hosts on which the proxy nodes are deployed. Separate multiple IDs with commas (,).
        self.proxy_node_list = proxy_node_list
        # The type of operation that you want to perform. Valid values:
        # 
        # *   **reboot**: restarts the proxy node.
        # *   **rebuild**: rebuilds the proxy node.
        self.reboot_mode = reboot_mode
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.proxy_list is not None:
            result['ProxyList'] = self.proxy_list

        if self.proxy_node_list is not None:
            result['ProxyNodeList'] = self.proxy_node_list

        if self.reboot_mode is not None:
            result['RebootMode'] = self.reboot_mode

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProxyList') is not None:
            self.proxy_list = m.get('ProxyList')

        if m.get('ProxyNodeList') is not None:
            self.proxy_node_list = m.get('ProxyNodeList')

        if m.get('RebootMode') is not None:
            self.reboot_mode = m.get('RebootMode')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

