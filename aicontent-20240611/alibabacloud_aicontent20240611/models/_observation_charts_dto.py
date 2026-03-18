# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ObservationChartsDTO(DaraModel):
    def __init__(
        self,
        call_volume: List[main_models.TimeSeriesPointDTO] = None,
        concurrency: List[main_models.TimeSeriesPointDTO] = None,
        qpm: List[main_models.TimeSeriesPointDTO] = None,
        response_time: List[main_models.TimeSeriesPointDTO] = None,
        success_rate: List[main_models.TimeSeriesPointDTO] = None,
        tpm: List[main_models.TimeSeriesPointDTO] = None,
    ):
        self.call_volume = call_volume
        self.concurrency = concurrency
        self.qpm = qpm
        self.response_time = response_time
        self.success_rate = success_rate
        self.tpm = tpm

    def validate(self):
        if self.call_volume:
            for v1 in self.call_volume:
                 if v1:
                    v1.validate()
        if self.concurrency:
            for v1 in self.concurrency:
                 if v1:
                    v1.validate()
        if self.qpm:
            for v1 in self.qpm:
                 if v1:
                    v1.validate()
        if self.response_time:
            for v1 in self.response_time:
                 if v1:
                    v1.validate()
        if self.success_rate:
            for v1 in self.success_rate:
                 if v1:
                    v1.validate()
        if self.tpm:
            for v1 in self.tpm:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['callVolume'] = []
        if self.call_volume is not None:
            for k1 in self.call_volume:
                result['callVolume'].append(k1.to_map() if k1 else None)

        result['concurrency'] = []
        if self.concurrency is not None:
            for k1 in self.concurrency:
                result['concurrency'].append(k1.to_map() if k1 else None)

        result['qpm'] = []
        if self.qpm is not None:
            for k1 in self.qpm:
                result['qpm'].append(k1.to_map() if k1 else None)

        result['responseTime'] = []
        if self.response_time is not None:
            for k1 in self.response_time:
                result['responseTime'].append(k1.to_map() if k1 else None)

        result['successRate'] = []
        if self.success_rate is not None:
            for k1 in self.success_rate:
                result['successRate'].append(k1.to_map() if k1 else None)

        result['tpm'] = []
        if self.tpm is not None:
            for k1 in self.tpm:
                result['tpm'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_volume = []
        if m.get('callVolume') is not None:
            for k1 in m.get('callVolume'):
                temp_model = main_models.TimeSeriesPointDTO()
                self.call_volume.append(temp_model.from_map(k1))

        self.concurrency = []
        if m.get('concurrency') is not None:
            for k1 in m.get('concurrency'):
                temp_model = main_models.TimeSeriesPointDTO()
                self.concurrency.append(temp_model.from_map(k1))

        self.qpm = []
        if m.get('qpm') is not None:
            for k1 in m.get('qpm'):
                temp_model = main_models.TimeSeriesPointDTO()
                self.qpm.append(temp_model.from_map(k1))

        self.response_time = []
        if m.get('responseTime') is not None:
            for k1 in m.get('responseTime'):
                temp_model = main_models.TimeSeriesPointDTO()
                self.response_time.append(temp_model.from_map(k1))

        self.success_rate = []
        if m.get('successRate') is not None:
            for k1 in m.get('successRate'):
                temp_model = main_models.TimeSeriesPointDTO()
                self.success_rate.append(temp_model.from_map(k1))

        self.tpm = []
        if m.get('tpm') is not None:
            for k1 in m.get('tpm'):
                temp_model = main_models.TimeSeriesPointDTO()
                self.tpm.append(temp_model.from_map(k1))

        return self

