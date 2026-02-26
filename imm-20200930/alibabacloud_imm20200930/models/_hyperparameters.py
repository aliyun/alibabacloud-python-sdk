# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class Hyperparameters(DaraModel):
    def __init__(
        self,
        backup_interval: int = None,
        batch_size: int = None,
        data_loader_workers: int = None,
        evaluator: main_models.CustomParams = None,
        input_size: List[int] = None,
        max_epoch: int = None,
        optimization: main_models.Optimization = None,
        schedule: main_models.Schedule = None,
    ):
        # The frequency at which the model configuration is saved. If you set this parameter to 1, model configuration is saved every epoch.
        self.backup_interval = backup_interval
        # The batch size for model training.
        self.batch_size = batch_size
        # The number of threads used to read the training data.
        self.data_loader_workers = data_loader_workers
        # The custom parameters for model training.
        # 
        # This parameter is required.
        self.evaluator = evaluator
        # The image size. The array contains the width and height of the image.
        # 
        # This parameter is required.
        self.input_size = input_size
        # The number of epochs.
        self.max_epoch = max_epoch
        # The optimization algorithm.
        self.optimization = optimization
        # The learning rate scheduler.
        self.schedule = schedule

    def validate(self):
        if self.evaluator:
            self.evaluator.validate()
        if self.optimization:
            self.optimization.validate()
        if self.schedule:
            self.schedule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_interval is not None:
            result['BackupInterval'] = self.backup_interval

        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.data_loader_workers is not None:
            result['DataLoaderWorkers'] = self.data_loader_workers

        if self.evaluator is not None:
            result['Evaluator'] = self.evaluator.to_map()

        if self.input_size is not None:
            result['InputSize'] = self.input_size

        if self.max_epoch is not None:
            result['MaxEpoch'] = self.max_epoch

        if self.optimization is not None:
            result['Optimization'] = self.optimization.to_map()

        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupInterval') is not None:
            self.backup_interval = m.get('BackupInterval')

        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('DataLoaderWorkers') is not None:
            self.data_loader_workers = m.get('DataLoaderWorkers')

        if m.get('Evaluator') is not None:
            temp_model = main_models.CustomParams()
            self.evaluator = temp_model.from_map(m.get('Evaluator'))

        if m.get('InputSize') is not None:
            self.input_size = m.get('InputSize')

        if m.get('MaxEpoch') is not None:
            self.max_epoch = m.get('MaxEpoch')

        if m.get('Optimization') is not None:
            temp_model = main_models.Optimization()
            self.optimization = temp_model.from_map(m.get('Optimization'))

        if m.get('Schedule') is not None:
            temp_model = main_models.Schedule()
            self.schedule = temp_model.from_map(m.get('Schedule'))

        return self

