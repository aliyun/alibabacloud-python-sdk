# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        param_no_loose_sentinel_enabled: str = None,
        param_no_loose_sentinel_password_free_access: str = None,
        param_no_loose_sentinel_password_free_commands: str = None,
        param_repl_mode: str = None,
        param_semisync_repl_timeout: str = None,
        param_sentinel_compat_enable: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The instance parameters to modify, in JSON format. The new values overwrite the existing values. For example, if you want to set only the **maxmemory-policy** parameter to **noeviction**, pass in `{"maxmemory-policy":"noeviction"}`.
        # > For more information about each parameter, see [Metric description](https://help.aliyun.com/document_detail/259681.html).
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The Sentinel compatibility mode. This parameter applies to non-cluster instances. Valid values:
        # * **no** (default): disabled.
        # * **yes**: enabled.
        # > For more information, see [Sentinel compatibility mode](https://help.aliyun.com/document_detail/178911.html).
        self.param_no_loose_sentinel_enabled = param_no_loose_sentinel_enabled
        # Specifies whether to allow password-free execution of Sentinel-related commands when Sentinel mode is enabled. Valid values:
        # * **no** (default): disabled.
        # * **yes**: enabled. After this parameter is enabled, you can run Sentinel commands without a password on any connection and use the SENTINEL command to listen on the +switch-master channel.
        self.param_no_loose_sentinel_password_free_access = param_no_loose_sentinel_password_free_access
        # After Sentinel mode and the ParamNoLooseSentinelPasswordFreeAccess parameter are enabled, use this parameter to add additional password-free commands (empty by default).
        # > * After this parameter is set, the specified commands can be run without a password on any connection. Proceed with caution.
        # > * Commands must be in lowercase letters. Separate multiple commands with commas (,).
        self.param_no_loose_sentinel_password_free_commands = param_no_loose_sentinel_password_free_commands
        # The synchronization pattern. Valid values:
        # * **async** (default): asynchronous
        # * **semisync**: semi-synchronous.
        self.param_repl_mode = param_repl_mode
        # The degradation threshold for semi-synchronous mode. This parameter is supported only in semi-synchronous mode. Unit: ms. Valid values: 10 to 60000. Default value: 500.
        # > * When the synchronization latency exceeds this threshold, the synchronous mode automatically transforms to asynchronous. When the latency is eliminated, the synchronous mode automatically transforms back to semi-synchronous.
        # > * This parameter is supported only by Tair Enterprise instances. This feature is in public preview.
        self.param_semisync_repl_timeout = param_semisync_repl_timeout
        # The Sentinel compatibility mode. This parameter applies to instances that use the proxy connection mode in cluster architecture or instances that use the read/write splitting architecture. Valid values:
        # * **0** (default): disabled.
        # * **1**: enabled.
        # > For more information, see [Sentinel compatibility mode](https://help.aliyun.com/document_detail/178911.html).
        self.param_sentinel_compat_enable = param_sentinel_compat_enable
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
        if self.config is not None:
            result['Config'] = self.config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param_no_loose_sentinel_enabled is not None:
            result['ParamNoLooseSentinelEnabled'] = self.param_no_loose_sentinel_enabled

        if self.param_no_loose_sentinel_password_free_access is not None:
            result['ParamNoLooseSentinelPasswordFreeAccess'] = self.param_no_loose_sentinel_password_free_access

        if self.param_no_loose_sentinel_password_free_commands is not None:
            result['ParamNoLooseSentinelPasswordFreeCommands'] = self.param_no_loose_sentinel_password_free_commands

        if self.param_repl_mode is not None:
            result['ParamReplMode'] = self.param_repl_mode

        if self.param_semisync_repl_timeout is not None:
            result['ParamSemisyncReplTimeout'] = self.param_semisync_repl_timeout

        if self.param_sentinel_compat_enable is not None:
            result['ParamSentinelCompatEnable'] = self.param_sentinel_compat_enable

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParamNoLooseSentinelEnabled') is not None:
            self.param_no_loose_sentinel_enabled = m.get('ParamNoLooseSentinelEnabled')

        if m.get('ParamNoLooseSentinelPasswordFreeAccess') is not None:
            self.param_no_loose_sentinel_password_free_access = m.get('ParamNoLooseSentinelPasswordFreeAccess')

        if m.get('ParamNoLooseSentinelPasswordFreeCommands') is not None:
            self.param_no_loose_sentinel_password_free_commands = m.get('ParamNoLooseSentinelPasswordFreeCommands')

        if m.get('ParamReplMode') is not None:
            self.param_repl_mode = m.get('ParamReplMode')

        if m.get('ParamSemisyncReplTimeout') is not None:
            self.param_semisync_repl_timeout = m.get('ParamSemisyncReplTimeout')

        if m.get('ParamSentinelCompatEnable') is not None:
            self.param_sentinel_compat_enable = m.get('ParamSentinelCompatEnable')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

