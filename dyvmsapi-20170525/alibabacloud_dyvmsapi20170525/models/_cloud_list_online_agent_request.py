# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudListOnlineAgentRequest(DaraModel):
    def __init__(
        self,
        cnos: str = None,
        enterprise_id: int = None,
        owner_id: int = None,
        pause_description: str = None,
        pause_type: str = None,
        qnos: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        state_code: str = None,
    ):
        # 坐席工号，指定座席工号则查询该工号座席的监控信息，可指定多个座席工号，指定多个座席工号使用英文逗号","分隔，不指定则查询所有队列监控信息，不指定则查询该账户下所有座席的监控信息
        self.cnos = cnos
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        self.owner_id = owner_id
        # 置忙原因，根据座席置忙原因过滤监控数据，可指定多个置忙原因，指定多个置忙原因使用英文逗号","分隔，不指定则默认查询所有设置状态的座席
        self.pause_description = pause_description
        # 置忙类型，根据座席置忙类型过滤监控数据，可指定多个置忙类型，指定多个置忙类型使用英文逗号","分隔，不指定则默认查询所有设置状态的座席。<br>取值说明1普通，2休息，3 IM，4 强制
        self.pause_type = pause_type
        # 队列号，指定队列号则查询该队列号所对应队列的监控信息，支持同时查询多个队列号对应队列的监控信息，多个队列号使用英文逗号","分隔，不指定则查询所有队列监控信息
        self.qnos = qnos
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 坐席状态，s1:空闲，s2:置忙，s3:整理，s4:呼叫中，s5:响铃，s6通话   可传多个状态码，多个值之间以","分隔
        self.state_code = state_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cnos is not None:
            result['Cnos'] = self.cnos

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pause_description is not None:
            result['PauseDescription'] = self.pause_description

        if self.pause_type is not None:
            result['PauseType'] = self.pause_type

        if self.qnos is not None:
            result['Qnos'] = self.qnos

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.state_code is not None:
            result['StateCode'] = self.state_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cnos') is not None:
            self.cnos = m.get('Cnos')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PauseDescription') is not None:
            self.pause_description = m.get('PauseDescription')

        if m.get('PauseType') is not None:
            self.pause_type = m.get('PauseType')

        if m.get('Qnos') is not None:
            self.qnos = m.get('Qnos')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StateCode') is not None:
            self.state_code = m.get('StateCode')

        return self

