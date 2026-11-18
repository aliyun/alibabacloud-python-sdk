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
        # The default configuration parameters of the instance. For more comprehensive parameter configurations, call the [Describeparamters](https://help.aliyun.com/document_detail/473847.html) operation.
        self.config = config
        # The Sentinel compatibility mode, which applies to non-cluster instances. Valid values:
        # * **no**: disabled. This is the default value.
        # * **yes**: enabled.
        # > For more information, see [Sentinel compatibility mode](https://help.aliyun.com/document_detail/178911.html).
        self.param_no_loose_sentinel_enabled = param_no_loose_sentinel_enabled
        # Specifies whether to allow password-free execution of Sentinel-related commands when the Sentinel mode is enabled. Valid values:
        # * **no**: disabled. This is the default value.
        # * **yes**: enabled. After this feature is enabled, you can execute Sentinel commands without a password on any connection and use the SENTINEL command to monitor the +switch-master channel.
        self.param_no_loose_sentinel_password_free_access = param_no_loose_sentinel_password_free_access
        # The list of additional password-free commands. After the Sentinel mode and the ParamNoLooseSentinelPasswordFreeAccess parameter are enabled, you can use this parameter to add extra password-free commands. Default value: empty.
        self.param_no_loose_sentinel_password_free_commands = param_no_loose_sentinel_password_free_commands
        # The synchronization mode. Valid values:
        # * **async**: asynchronous mode. This is the default value.
        # * **semisync**: semi-synchronous mode.
        self.param_repl_mode = param_repl_mode
        # The degradation threshold for the semi-synchronous mode. This parameter can be configured only when the semi-synchronous mode is used. Unit: milliseconds. Valid values: 10 to 60000. Default value: 500.
        # > When the synchronization latency exceeds this threshold, the synchronization mode automatically degrades to the asynchronous mode. After the synchronization latency is eliminated, the synchronization mode automatically switches back to the semi-synchronous mode.
        self.param_repl_timeout = param_repl_timeout
        # The Sentinel compatibility mode, which applies to instances in the cluster architecture proxy mode or read/write splitting architecture. Valid values:
        # * **0**: disabled. This is the default value.
        # * **1**: enabled.
        # > For more information, see [Sentinel compatibility mode](https://help.aliyun.com/document_detail/178911.html).
        self.param_sentinel_compat_enable = param_sentinel_compat_enable
        # The ID of the request.
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

