# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class UpdateMOQuotaAlertThresholdRequest(DaraModel):
    def __init__(
        self,
        apikey: List[main_models.UpdateMOQuotaAlertThresholdRequestApikey] = None,
        instance_id: str = None,
    ):
        # A list of API keys.
        # 
        # This parameter is required.
        self.apikey = apikey
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.apikey:
            for v1 in self.apikey:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Apikey'] = []
        if self.apikey is not None:
            for k1 in self.apikey:
                result['Apikey'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apikey = []
        if m.get('Apikey') is not None:
            for k1 in m.get('Apikey'):
                temp_model = main_models.UpdateMOQuotaAlertThresholdRequestApikey()
                self.apikey.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class UpdateMOQuotaAlertThresholdRequestApikey(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        threshold_percent: int = None,
    ):
        # The API key.
        self.apikey = apikey
        # The alert threshold percentage. For example, a value of 80 triggers an alert when usage reaches 80% of the usage quota. The alert is reset after the usage falls below this percentage.
        self.threshold_percent = threshold_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['Apikey'] = self.apikey

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apikey') is not None:
            self.apikey = m.get('Apikey')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        return self

