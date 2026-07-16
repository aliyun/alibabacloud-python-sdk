# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class SampleBase(DaraModel):
    def __init__(
        self,
        full_sample_device_ids: List[main_models.FullSampleItem] = None,
        full_sample_users: List[main_models.FullSampleItem] = None,
        sample_method: str = None,
        sample_rate: float = None,
    ):
        self.full_sample_device_ids = full_sample_device_ids
        self.full_sample_users = full_sample_users
        self.sample_method = sample_method
        self.sample_rate = sample_rate

    def validate(self):
        if self.full_sample_device_ids:
            for v1 in self.full_sample_device_ids:
                 if v1:
                    v1.validate()
        if self.full_sample_users:
            for v1 in self.full_sample_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FullSampleDeviceIds'] = []
        if self.full_sample_device_ids is not None:
            for k1 in self.full_sample_device_ids:
                result['FullSampleDeviceIds'].append(k1.to_map() if k1 else None)

        result['FullSampleUsers'] = []
        if self.full_sample_users is not None:
            for k1 in self.full_sample_users:
                result['FullSampleUsers'].append(k1.to_map() if k1 else None)

        if self.sample_method is not None:
            result['SampleMethod'] = self.sample_method

        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.full_sample_device_ids = []
        if m.get('FullSampleDeviceIds') is not None:
            for k1 in m.get('FullSampleDeviceIds'):
                temp_model = main_models.FullSampleItem()
                self.full_sample_device_ids.append(temp_model.from_map(k1))

        self.full_sample_users = []
        if m.get('FullSampleUsers') is not None:
            for k1 in m.get('FullSampleUsers'):
                temp_model = main_models.FullSampleItem()
                self.full_sample_users.append(temp_model.from_map(k1))

        if m.get('SampleMethod') is not None:
            self.sample_method = m.get('SampleMethod')

        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')

        return self

