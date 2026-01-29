# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class RenewChangeInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        owner_id: int = None,
        parameter: List[main_models.RenewChangeInstanceRequestParameter] = None,
        product_code: str = None,
        product_type: str = None,
        renew_period: int = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_id = owner_id
        self.parameter = parameter
        # This parameter is required.
        self.product_code = product_code
        self.product_type = product_type
        # This parameter is required.
        self.renew_period = renew_period

    def validate(self):
        if self.parameter:
            for v1 in self.parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['Parameter'] = []
        if self.parameter is not None:
            for k1 in self.parameter:
                result['Parameter'].append(k1.to_map() if k1 else None)

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.renew_period is not None:
            result['RenewPeriod'] = self.renew_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.parameter = []
        if m.get('Parameter') is not None:
            for k1 in m.get('Parameter'):
                temp_model = main_models.RenewChangeInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k1))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RenewPeriod') is not None:
            self.renew_period = m.get('RenewPeriod')

        return self

class RenewChangeInstanceRequestParameter(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

