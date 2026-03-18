# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class QueryEnableMultiAzPriceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        observers: List[main_models.QueryEnableMultiAzPriceRequestObservers] = None,
        promotion_option_no: str = None,
    ):
        self.instance_id = instance_id
        self.observers = observers
        self.promotion_option_no = promotion_option_no

    def validate(self):
        if self.observers:
            for v1 in self.observers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        result['observers'] = []
        if self.observers is not None:
            for k1 in self.observers:
                result['observers'].append(k1.to_map() if k1 else None)

        if self.promotion_option_no is not None:
            result['promotionOptionNo'] = self.promotion_option_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        self.observers = []
        if m.get('observers') is not None:
            for k1 in m.get('observers'):
                temp_model = main_models.QueryEnableMultiAzPriceRequestObservers()
                self.observers.append(temp_model.from_map(k1))

        if m.get('promotionOptionNo') is not None:
            self.promotion_option_no = m.get('promotionOptionNo')

        return self

class QueryEnableMultiAzPriceRequestObservers(DaraModel):
    def __init__(
        self,
        vsw_id: str = None,
        zone_id: str = None,
    ):
        self.vsw_id = vsw_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vsw_id is not None:
            result['vswId'] = self.vsw_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vswId') is not None:
            self.vsw_id = m.get('vswId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

