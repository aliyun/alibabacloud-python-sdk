# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAgentRequest(DaraModel):
    def __init__(
        self,
        account: str = None,
        agent_tag: str = None,
        extension_pwd: str = None,
        name: str = None,
        owner_id: int = None,
        password: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # 坐席账号名(必须唯一)
        # 
        # This parameter is required.
        self.account = account
        # 合作方唯一标识
        self.agent_tag = agent_tag
        # 分机密码
        # 
        # This parameter is required.
        self.extension_pwd = extension_pwd
        # 坐席名称
        # 
        # This parameter is required.
        self.name = name
        self.owner_id = owner_id
        # 坐席账号密码 (可以跟分机密码一致)
        # 
        # This parameter is required.
        self.password = password
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.agent_tag is not None:
            result['AgentTag'] = self.agent_tag

        if self.extension_pwd is not None:
            result['ExtensionPwd'] = self.extension_pwd

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('AgentTag') is not None:
            self.agent_tag = m.get('AgentTag')

        if m.get('ExtensionPwd') is not None:
            self.extension_pwd = m.get('ExtensionPwd')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

