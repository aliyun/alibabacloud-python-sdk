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
        # The parameter settings of the instance. For more information, see [Parameter overview and configuration guide](https://help.aliyun.com/document_detail/43885.html).
        self.config = config
        # The Sentinel-compatible mode, which is applicable to non-cluster instances. For more information about the parameter, see the relevant documentation.
        self.param_no_loose_sentinel_enabled = param_no_loose_sentinel_enabled
        # Indicates whether Sentinel commands can be run without requiring a password when the Sentinel mode is enabled. Valid values: Valid values: yes and no. Default value: no. After you set this parameter to yes, you can run Sentinel commands in a virtual private cloud (VPC) without the need to enable the password-free access feature.
        self.param_no_loose_sentinel_password_free_access = param_no_loose_sentinel_password_free_access
        # After you enable the Sentinel mode and set the ParamNoLooseSentinelPasswordFreeAccess parameter to yes, you can use this parameter to specify an additional list of commands that can be run without requiring a password. By default, this parameter is empty. After you configure this parameter, you can run the specified commands without a password on any connection. Proceed with caution. The commands must be written in lowercase letters. Multiple commands are separated by commas (,).
        self.param_no_loose_sentinel_password_free_commands = param_no_loose_sentinel_password_free_commands
        # The synchronization mode.
        # 
        # *   **semisync**
        # *   **async**
        self.param_repl_mode = param_repl_mode
        # The degradation threshold time of the semi-synchronous replication mode. This parameter is required only when semi-synchronous replication is enabled. Unit: milliseconds. Valid values: 10 to 60000.
        self.param_repl_timeout = param_repl_timeout
        # The Sentinel-compatible mode, which is applicable to cluster instances in proxy mode or read/write splitting instances. For more information about the parameter, see the relevant documentation.
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

