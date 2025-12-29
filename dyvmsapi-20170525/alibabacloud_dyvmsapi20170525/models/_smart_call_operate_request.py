# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SmartCallOperateRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        command: str = None,
        owner_id: int = None,
        param: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The unique receipt ID of the call. You can call the [SmartCall](https://help.aliyun.com/document_detail/393526.html) operation to obtain the receipt ID.
        # 
        # This parameter is required.
        self.call_id = call_id
        # The action that is initiated to the called number of an outbound robocall.
        # 
        # > Only the value **parallelBridge** is supported. This value indicates that a bridge action is initiated between a called number and an agent of the call center.
        # 
        # This parameter is required.
        self.command = command
        self.owner_id = owner_id
        # The extended field.
        self.param = param
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.command is not None:
            result['Command'] = self.command

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param is not None:
            result['Param'] = self.param

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

