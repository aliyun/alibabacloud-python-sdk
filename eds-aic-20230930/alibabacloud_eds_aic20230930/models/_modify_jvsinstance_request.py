# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class ModifyJVSInstanceRequest(DaraModel):
    def __init__(
        self,
        apply_to_all: bool = None,
        credit_config: List[main_models.ModifyJVSInstanceRequestCreditConfig] = None,
        instance_ids: List[str] = None,
        instance_name: str = None,
    ):
        self.apply_to_all = apply_to_all
        self.credit_config = credit_config
        self.instance_ids = instance_ids
        self.instance_name = instance_name

    def validate(self):
        if self.credit_config:
            for v1 in self.credit_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_to_all is not None:
            result['ApplyToAll'] = self.apply_to_all

        result['CreditConfig'] = []
        if self.credit_config is not None:
            for k1 in self.credit_config:
                result['CreditConfig'].append(k1.to_map() if k1 else None)

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyToAll') is not None:
            self.apply_to_all = m.get('ApplyToAll')

        self.credit_config = []
        if m.get('CreditConfig') is not None:
            for k1 in m.get('CreditConfig'):
                temp_model = main_models.ModifyJVSInstanceRequestCreditConfig()
                self.credit_config.append(temp_model.from_map(k1))

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

class ModifyJVSInstanceRequestCreditConfig(DaraModel):
    def __init__(
        self,
        credit_limit: int = None,
        limit_period: str = None,
    ):
        self.credit_limit = credit_limit
        self.limit_period = limit_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_limit is not None:
            result['CreditLimit'] = self.credit_limit

        if self.limit_period is not None:
            result['LimitPeriod'] = self.limit_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditLimit') is not None:
            self.credit_limit = m.get('CreditLimit')

        if m.get('LimitPeriod') is not None:
            self.limit_period = m.get('LimitPeriod')

        return self

