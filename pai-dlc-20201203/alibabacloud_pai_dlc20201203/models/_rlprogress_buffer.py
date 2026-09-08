# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class RLProgressBuffer(DaraModel):
    def __init__(
        self,
        consumed: int = None,
        detail: List[main_models.RLProgressBufferDetail] = None,
        eta_sec: int = None,
        fill_rate_per_min: float = None,
        finished: int = None,
        pct: float = None,
        ready: int = None,
        target: int = None,
        train_batch_size: int = None,
        training: bool = None,
    ):
        # The total number of consumed samples in incomplete buffers.
        self.consumed = consumed
        # The buffer details split by tag.
        self.detail = detail
        # The estimated number of remaining seconds to fill the buffer.
        self.eta_sec = eta_sec
        # The fill rate in entries per minute, estimated by using the rollout completion rate as a proxy.
        self.fill_rate_per_min = fill_rate_per_min
        # The total number of finished samples in incomplete buffers.
        self.finished = finished
        # The readiness percentage, which is the ratio of Ready to Target.
        self.pct = pct
        # The total number of ready samples in incomplete buffers.
        self.ready = ready
        # The total number of target samples in incomplete buffers.
        self.target = target
        # The configured training batch size.
        self.train_batch_size = train_batch_size
        # Indicates whether Consumed is greater than 0, which means the batch has been fetched and the trainer is updating.
        self.training = training

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumed is not None:
            result['Consumed'] = self.consumed

        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.eta_sec is not None:
            result['EtaSec'] = self.eta_sec

        if self.fill_rate_per_min is not None:
            result['FillRatePerMin'] = self.fill_rate_per_min

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.pct is not None:
            result['Pct'] = self.pct

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.target is not None:
            result['Target'] = self.target

        if self.train_batch_size is not None:
            result['TrainBatchSize'] = self.train_batch_size

        if self.training is not None:
            result['Training'] = self.training

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Consumed') is not None:
            self.consumed = m.get('Consumed')

        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.RLProgressBufferDetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('EtaSec') is not None:
            self.eta_sec = m.get('EtaSec')

        if m.get('FillRatePerMin') is not None:
            self.fill_rate_per_min = m.get('FillRatePerMin')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('Pct') is not None:
            self.pct = m.get('Pct')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TrainBatchSize') is not None:
            self.train_batch_size = m.get('TrainBatchSize')

        if m.get('Training') is not None:
            self.training = m.get('Training')

        return self

