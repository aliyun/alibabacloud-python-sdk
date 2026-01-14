# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class UpdateTaskCustomerRequest(DaraModel):
    def __init__(
        self,
        customers: List[main_models.UpdateTaskCustomerRequestCustomers] = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        # 外呼客户
        # 
        # This parameter is required.
        self.customers = customers
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 任务ID
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        if self.customers:
            for v1 in self.customers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Customers'] = []
        if self.customers is not None:
            for k1 in self.customers:
                result['Customers'].append(k1.to_map() if k1 else None)

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customers = []
        if m.get('Customers') is not None:
            for k1 in m.get('Customers'):
                temp_model = main_models.UpdateTaskCustomerRequestCustomers()
                self.customers.append(temp_model.from_map(k1))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class UpdateTaskCustomerRequestCustomers(DaraModel):
    def __init__(
        self,
        cancel: int = None,
        number: str = None,
        properties: Dict[str, Any] = None,
        tag: str = None,
    ):
        # 是否取消外呼 0否，1是
        self.cancel = cancel
        # 电话号码
        self.number = number
        # 需根据具体任务参数要求传输
        self.properties = properties
        # 用户自定义标签
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancel is not None:
            result['Cancel'] = self.cancel

        if self.number is not None:
            result['Number'] = self.number

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cancel') is not None:
            self.cancel = m.get('Cancel')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

