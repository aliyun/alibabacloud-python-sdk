# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class Features(DaraModel):
    def __init__(
        self,
        quota: main_models.FeaturesQuota = None,
    ):
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            temp_model = main_models.FeaturesQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        return self

class FeaturesQuota(DaraModel):
    def __init__(
        self,
        is_enabled: bool = None,
    ):
        self.is_enabled = is_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_enabled is not None:
            result['IsEnabled'] = self.is_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEnabled') is not None:
            self.is_enabled = m.get('IsEnabled')

        return self

