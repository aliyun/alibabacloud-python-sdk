# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ExportModelFeatureTrainingSetTableRequest(DaraModel):
    def __init__(
        self,
        feature_view_config: Dict[str, main_models.FeatureViewConfigValue] = None,
        label_input_config: main_models.ExportModelFeatureTrainingSetTableRequestLabelInputConfig = None,
        real_time_iterate_interval: int = None,
        real_time_partition_count_value: int = None,
        training_set_config: main_models.ExportModelFeatureTrainingSetTableRequestTrainingSetConfig = None,
    ):
        self.feature_view_config = feature_view_config
        self.label_input_config = label_input_config
        self.real_time_iterate_interval = real_time_iterate_interval
        self.real_time_partition_count_value = real_time_partition_count_value
        self.training_set_config = training_set_config

    def validate(self):
        if self.feature_view_config:
            for v1 in self.feature_view_config.values():
                 if v1:
                    v1.validate()
        if self.label_input_config:
            self.label_input_config.validate()
        if self.training_set_config:
            self.training_set_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeatureViewConfig'] = {}
        if self.feature_view_config is not None:
            for k1, v1 in self.feature_view_config.items():
                result['FeatureViewConfig'][k1] = v1.to_map() if v1 else None

        if self.label_input_config is not None:
            result['LabelInputConfig'] = self.label_input_config.to_map()

        if self.real_time_iterate_interval is not None:
            result['RealTimeIterateInterval'] = self.real_time_iterate_interval

        if self.real_time_partition_count_value is not None:
            result['RealTimePartitionCountValue'] = self.real_time_partition_count_value

        if self.training_set_config is not None:
            result['TrainingSetConfig'] = self.training_set_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_view_config = {}
        if m.get('FeatureViewConfig') is not None:
            for k1, v1 in m.get('FeatureViewConfig').items():
                temp_model = main_models.FeatureViewConfigValue()
                self.feature_view_config[k1] = temp_model.from_map(v1)

        if m.get('LabelInputConfig') is not None:
            temp_model = main_models.ExportModelFeatureTrainingSetTableRequestLabelInputConfig()
            self.label_input_config = temp_model.from_map(m.get('LabelInputConfig'))

        if m.get('RealTimeIterateInterval') is not None:
            self.real_time_iterate_interval = m.get('RealTimeIterateInterval')

        if m.get('RealTimePartitionCountValue') is not None:
            self.real_time_partition_count_value = m.get('RealTimePartitionCountValue')

        if m.get('TrainingSetConfig') is not None:
            temp_model = main_models.ExportModelFeatureTrainingSetTableRequestTrainingSetConfig()
            self.training_set_config = temp_model.from_map(m.get('TrainingSetConfig'))

        return self

class ExportModelFeatureTrainingSetTableRequestTrainingSetConfig(DaraModel):
    def __init__(
        self,
        partitions: Dict[str, dict] = None,
    ):
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.partitions is not None:
            result['Partitions'] = self.partitions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')

        return self

class ExportModelFeatureTrainingSetTableRequestLabelInputConfig(DaraModel):
    def __init__(
        self,
        event_time: str = None,
        partitions: Dict[str, dict] = None,
    ):
        self.event_time = event_time
        self.partitions = partitions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.partitions is not None:
            result['Partitions'] = self.partitions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('Partitions') is not None:
            self.partitions = m.get('Partitions')

        return self

