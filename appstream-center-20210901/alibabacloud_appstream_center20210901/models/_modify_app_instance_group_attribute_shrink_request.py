# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppInstanceGroupAttributeShrinkRequest(DaraModel):
    def __init__(
        self,
        app_instance_group_id: str = None,
        app_instance_group_name: str = None,
        network_shrink: str = None,
        node_pool_shrink: str = None,
        per_session_per_app: bool = None,
        pre_open_app_id: str = None,
        pre_open_mode: str = None,
        product_type: str = None,
        security_policy_shrink: str = None,
        session_timeout: int = None,
        storage_policy_shrink: str = None,
    ):
        # The delivery group ID.
        # 
        # This parameter is required.
        self.app_instance_group_id = app_instance_group_id
        # The delivery group name.
        self.app_instance_group_name = app_instance_group_name
        # The network configuration.
        # 
        # > To use this parameter, submit a ticket.
        self.network_shrink = network_shrink
        # The resource group object.
        self.node_pool_shrink = node_pool_shrink
        # Specifies whether to allow only one application per session.
        # - If enabled, opening multiple applications within a delivery group allocates a separate session for each application, consuming more sessions.
        self.per_session_per_app = per_session_per_app
        # The AppId of the pre-open application. If the PreOpenMode parameter is set to `SINGLE_APP`, PreOpenAppId cannot be an empty string.
        self.pre_open_app_id = pre_open_app_id
        # The pre-open mode.
        self.pre_open_mode = pre_open_mode
        # The product type.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The security policy.
        self.security_policy_shrink = security_policy_shrink
        # The session retention duration after disconnection, in minutes. After an end user session is disconnected, the session is retained for the specified duration before being logged off. Set this parameter to `-1` to retain the session indefinitely. Valid values: -1 and 3 to 300. Default value: `15`.
        self.session_timeout = session_timeout
        # The storage policy.
        self.storage_policy_shrink = storage_policy_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id

        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name

        if self.network_shrink is not None:
            result['Network'] = self.network_shrink

        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink

        if self.per_session_per_app is not None:
            result['PerSessionPerApp'] = self.per_session_per_app

        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id

        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')

        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')

        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')

        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')

        if m.get('PerSessionPerApp') is not None:
            self.per_session_per_app = m.get('PerSessionPerApp')

        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')

        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')

        return self

