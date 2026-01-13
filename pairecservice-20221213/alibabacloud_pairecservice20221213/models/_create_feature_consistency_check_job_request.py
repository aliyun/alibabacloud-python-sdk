# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFeatureConsistencyCheckJobRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        feature_consistency_check_job_config_id: str = None,
        instance_id: str = None,
        sampling_duration: int = None,
    ):
        # This parameter is required.
        self.environment = environment
        # This parameter is required.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.sampling_duration = sampling_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sampling_duration is not None:
            result['SamplingDuration'] = self.sampling_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SamplingDuration') is not None:
            self.sampling_duration = m.get('SamplingDuration')

        return self

