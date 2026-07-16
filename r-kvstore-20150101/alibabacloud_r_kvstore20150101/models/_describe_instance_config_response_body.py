# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceConfigResponseBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        param_no_loose_sentinel_enabled: str = None,
        param_no_loose_sentinel_password_free_access: str = None,
        param_no_loose_sentinel_password_free_commands: str = None,
        param_repl_mode: str = None,
        param_repl_timeout: str = None,
        param_sentinel_compat_enable: str = None,
        request_id: str = None,
    ):
        # The default configuration parameters of the instance. To view the full list of parameters, call the [DescribeParameters](https://help.aliyun.com/document_detail/473847.html) operation.
        self.config = config
        # Specifies whether to enable Sentinel compatibility mode. This parameter applies only to non-cluster instances. Valid values:
        # 
        # - **no** (default): Disabled
        # 
        # - **yes**: Enabled
        # 
        # > For more information, see [Sentinel compatibility mode](https://help.aliyun.com/document_detail/178911.html).
        self.param_no_loose_sentinel_enabled = param_no_loose_sentinel_enabled
        # Specifies whether to allow password-free execution of Sentinel commands when Sentinel compatibility mode is enabled. Valid values:
        # 
        # - **no** (default): Disabled.
        # 
        # - **yes**: Enabled. Allows you to run Sentinel commands on any connection without a password and use the `SENTINEL` command to subscribe to the `+switch-master` channel.
        self.param_no_loose_sentinel_password_free_access = param_no_loose_sentinel_password_free_access
        # Additional commands that can be run without a password. This parameter is valid only when Sentinel compatibility mode is enabled and `ParamNoLooseSentinelPasswordFreeAccess` is set to `yes`. By default, this parameter is empty.
        self.param_no_loose_sentinel_password_free_commands = param_no_loose_sentinel_password_free_commands
        # The replication mode. Valid values:
        # 
        # - **async** (default): asynchronous mode
        # 
        # - **semisync**: semi-synchronous mode
        self.param_repl_mode = param_repl_mode
        # The degradation threshold for the semi-synchronous mode. This parameter is valid only in semi-synchronous mode. Unit: milliseconds. Valid values: 10 to 60000. Default value: 500.
        # 
        # > If replication latency exceeds this threshold, the replication mode degrades to asynchronous mode. When the replication latency returns to normal, the mode reverts to semi-synchronous mode.
        self.param_repl_timeout = param_repl_timeout
        # Specifies whether to enable Sentinel compatibility mode. This parameter applies to instances that use the cluster architecture with proxy connection mode or the read/write splitting architecture. Valid values:
        # 
        # - **0** (default): Disabled
        # 
        # - **1**: Enabled
        # 
        # > For more information, see [Sentinel compatibility mode](https://help.aliyun.com/document_detail/178911.html).
        self.param_sentinel_compat_enable = param_sentinel_compat_enable
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.param_no_loose_sentinel_enabled is not None:
            result['ParamNoLooseSentinelEnabled'] = self.param_no_loose_sentinel_enabled

        if self.param_no_loose_sentinel_password_free_access is not None:
            result['ParamNoLooseSentinelPasswordFreeAccess'] = self.param_no_loose_sentinel_password_free_access

        if self.param_no_loose_sentinel_password_free_commands is not None:
            result['ParamNoLooseSentinelPasswordFreeCommands'] = self.param_no_loose_sentinel_password_free_commands

        if self.param_repl_mode is not None:
            result['ParamReplMode'] = self.param_repl_mode

        if self.param_repl_timeout is not None:
            result['ParamReplTimeout'] = self.param_repl_timeout

        if self.param_sentinel_compat_enable is not None:
            result['ParamSentinelCompatEnable'] = self.param_sentinel_compat_enable

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ParamNoLooseSentinelEnabled') is not None:
            self.param_no_loose_sentinel_enabled = m.get('ParamNoLooseSentinelEnabled')

        if m.get('ParamNoLooseSentinelPasswordFreeAccess') is not None:
            self.param_no_loose_sentinel_password_free_access = m.get('ParamNoLooseSentinelPasswordFreeAccess')

        if m.get('ParamNoLooseSentinelPasswordFreeCommands') is not None:
            self.param_no_loose_sentinel_password_free_commands = m.get('ParamNoLooseSentinelPasswordFreeCommands')

        if m.get('ParamReplMode') is not None:
            self.param_repl_mode = m.get('ParamReplMode')

        if m.get('ParamReplTimeout') is not None:
            self.param_repl_timeout = m.get('ParamReplTimeout')

        if m.get('ParamSentinelCompatEnable') is not None:
            self.param_sentinel_compat_enable = m.get('ParamSentinelCompatEnable')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

