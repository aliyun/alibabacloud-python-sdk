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
        # 需修改的实例参数，格式为JSON，修改后的值会覆盖原来的值。例如您只希望修改**maxmemory-policy**参数为**noeviction**，您可以传入`{"maxmemory-policy":"noeviction"}`。
        # > 关于各参数的详细说明，请参见[参数说明](https://help.aliyun.com/document_detail/259681.html)。
        self.config = config
        # 实例ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # 哨兵兼容模式，适用于非集群实例。取值说明：
        # * **no**（默认）：未开启
        # * **yes**：开启
        # > 更多信息请参见[Sentinel兼容模式](https://help.aliyun.com/document_detail/178911.html)。
        self.param_no_loose_sentinel_enabled = param_no_loose_sentinel_enabled
        # 开启哨兵模式时，是否允许免密执行Sentinel相关命令，取值说明：
        # * **no**（默认）：关闭。
        # * **yes**：开启。开启后，可以在任意连接上免密执行Sentinel命令以及使用SENTINEL命令监听+switch-master通道。
        self.param_no_loose_sentinel_password_free_access = param_no_loose_sentinel_password_free_access
        # 启用哨兵模式及ParamNoLooseSentinelPasswordFreeAccess参数后，可通过本参数添加额外的免密命令列表（默认为空）。
        # > * 设置后可在任意连接上无需密码执行对应命令，请谨慎操作。
        # > * 命令需使用小写字母，多个命令以英文逗号(,)分隔。
        self.param_no_loose_sentinel_password_free_commands = param_no_loose_sentinel_password_free_commands
        # 同步模式：
        # * **async**（默认）：异步
        # * **semisync**：半同步
        self.param_repl_mode = param_repl_mode
        # 半同步模式的降级阈值。仅半同步支持配置该参数，单位为ms，取值范围为10~60000，默认为500。
        # > * 当同步延迟超出该阈值时，同步模式会自动转为异步，当同步延迟消除后，同步模式会自动转换为半同步。
        # > * 仅Tair企业版实例支持，该功能公测中。
        self.param_semisync_repl_timeout = param_semisync_repl_timeout
        # 哨兵兼容模式，适用于集群架构代理连接模式或读写分离架构的实例，取值说明：
        # * **0**（默认）：未开启
        # * **1**：开启
        # > 更多信息请参见[Sentinel兼容模式](https://help.aliyun.com/document_detail/178911.html)。
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

