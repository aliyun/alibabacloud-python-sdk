# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateARMServerInstancesRequest(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_renew: bool = None,
        auto_use_coupon: bool = None,
        cidr: str = None,
        ens_region_id: str = None,
        environment_var: str = None,
        frequency: int = None,
        image_id: str = None,
        instance_billing_cycle: str = None,
        instance_type: str = None,
        key_pair_name: str = None,
        name_space: str = None,
        pay_type: str = None,
        period: int = None,
        period_unit: str = None,
        resolution: str = None,
        server_name: str = None,
        server_type: str = None,
        tag: List[main_models.CreateARMServerInstancesRequestTag] = None,
    ):
        # The number of instances to create. Minimum value: **1**. Maximum value: **100**.
        # 
        # This parameter is required.
        self.amount = amount
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # Specifies whether to use coupons. Valid values:
        self.auto_use_coupon = auto_use_coupon
        # The IPv4 CIDR block used by the instance, in CIDR notation.
        self.cidr = cidr
        # The ENS edge zone ID.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # One or more environment variables to set during EAIS instance initialization.
        self.environment_var = environment_var
        # The refresh rate, in Hz. Valid values: 30 and 60.
        self.frequency = frequency
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The instance billing cycle. Valid values:
        # - Hour
        # - Day
        self.instance_billing_cycle = instance_billing_cycle
        # The instance type of the AIC container instance. Valid values:
        # 
        # - aic.cf52r.c1.np
        # 
        # - aic.cf52r.c2.np
        # 
        # - aic.cf53r.c2.np
        # 
        # - aic.cf52r.c4.np
        # 
        # - aic.cf53r.c3.np
        # 
        # - aic.cf52r.c3.np
        # 
        # - aic.cf53r.c1.np
        # 
        # - aic.cf53r.c5.np
        # 
        # - aic.cf53r.c6
        # 
        # - aic.cf53r.c4.np
        # 
        # - aic.cf53r.c6.np
        # 
        # - aic.cf53r.c7.np
        # 
        # - aic.cf52m1r.c5.np
        # 
        # - aic.cf53r.c8.np
        # 
        # - aic.cf53r.c7
        # 
        # - aic.cf52m1r.c2.np
        # 
        # - aic.cf52m1r.c1.np
        # 
        # - aic.cf52m1r.c3.np
        # 
        # - aic.cf52m1r.c4.np
        # 
        # - aic.cf52m1r.c6
        # 
        # - ens.a6c2
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The key pair name.
        self.key_pair_name = key_pair_name
        # The namespace.
        self.name_space = name_space
        # The billing type. Valid values: **PrePaid** (subscription).
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The duration for which you want to purchase the resource.
        # 
        # - If you do not specify PeriodUnit, the resource is purchased on a monthly basis by default. Currently, only Days and Month are supported.
        # - If PeriodUnit is set to Day, Period can only be set to 3.
        # - If PeriodUnit is set to Month, Period can be set to 1 to 9 or 12.
        self.period = period
        # The unit of the purchase duration.
        self.period_unit = period_unit
        # The resolution. Valid values:
        # 
        # - 1920*864
        # 
        # - 1080*1920
        # 
        # - 1920*1080
        # 
        # - 720*1280
        # 
        # - 2400*1080
        # 
        # - 1080*2400
        # 
        # - 1280*720
        # 
        # - 864*1920
        # 
        # This parameter is required.
        self.resolution = resolution
        # The service name.
        self.server_name = server_name
        # The ARM board specification. Valid values:
        # 
        # - cas.cf53r
        # - cas.cf52r
        # - cas.cf52m1r
        # - cas.tg52g2
        # - ens.afq-c2m3i.medium
        # 
        # This parameter is required.
        self.server_type = server_type
        # The list of tags bound to the instance.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.environment_var is not None:
            result['EnvironmentVar'] = self.environment_var

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.name_space is not None:
            result['NameSpace'] = self.name_space

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnvironmentVar') is not None:
            self.environment_var = m.get('EnvironmentVar')

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateARMServerInstancesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateARMServerInstancesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

