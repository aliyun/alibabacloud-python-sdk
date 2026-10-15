# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class ModifyInstanceRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        modify_type: str = None,
        owner_id: int = None,
        parameter: List[main_models.ModifyInstanceRequestParameter] = None,
        product_code: str = None,
        product_type: str = None,
        subscription_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request and prevent duplicate submissions.
        self.client_token = client_token
        # The instance ID of the instance whose configuration you want to modify.
        self.instance_id = instance_id
        # The type of configuration change. Valid values:
        # - Upgrade: upgrade.
        # - Downgrade: downgrade.
        # 
        # This parameter is required.
        self.modify_type = modify_type
        self.owner_id = owner_id
        # The list of parameters.
        self.parameter = parameter
        # The product code.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The product type.
        self.product_type = product_type
        # The billing method. Valid values:
        # - Subscription: subscription.
        # - PayAsYouGo: pay-as-you-go.
        # 
        # This parameter is required.
        self.subscription_type = subscription_type

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

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

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

        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.parameter = []
        if m.get('Parameter') is not None:
            for k1 in m.get('Parameter'):
                temp_model = main_models.ModifyInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k1))

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')

        return self

class ModifyInstanceRequestParameter(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The code of the nth module property. Valid values of n: 1 to 100. If multiple module properties exist, concatenate the parameters in the format of n=1,2,3…n.
        # 
        # > Specify only the module properties that need to be changed. For example, if only property A needs to be changed among properties A and B, pass only the information related to property A.
        # 
        # This parameter is required.
        self.code = code
        # The value of the nth module property. Valid values of n: 1 to 100.
        # 
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

