# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_aiccs20230516 import models as main_models
from darabonba.model import DaraModel

class ImportNumberRequest(DaraModel):
    def __init__(
        self,
        customers: List[main_models.ImportNumberRequestCustomers] = None,
        fail_return: int = None,
        out_id: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: int = None,
    ):
        # This parameter is required.
        self.customers = customers
        self.fail_return = fail_return
        # This parameter is required.
        self.out_id = out_id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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

        if self.fail_return is not None:
            result['FailReturn'] = self.fail_return

        if self.out_id is not None:
            result['OutId'] = self.out_id

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
                temp_model = main_models.ImportNumberRequestCustomers()
                self.customers.append(temp_model.from_map(k1))

        if m.get('FailReturn') is not None:
            self.fail_return = m.get('FailReturn')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class ImportNumberRequestCustomers(DaraModel):
    def __init__(
        self,
        client_url: str = None,
        number: str = None,
        number_md5: str = None,
        properties: Dict[str, Any] = None,
        tag: str = None,
    ):
        self.client_url = client_url
        self.number = number
        self.number_md5 = number_md5
        self.properties = properties
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_url is not None:
            result['ClientUrl'] = self.client_url

        if self.number is not None:
            result['Number'] = self.number

        if self.number_md5 is not None:
            result['NumberMD5'] = self.number_md5

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientUrl') is not None:
            self.client_url = m.get('ClientUrl')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('NumberMD5') is not None:
            self.number_md5 = m.get('NumberMD5')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

