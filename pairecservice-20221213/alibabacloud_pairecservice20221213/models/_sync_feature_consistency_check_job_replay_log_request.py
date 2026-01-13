# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncFeatureConsistencyCheckJobReplayLogRequest(DaraModel):
    def __init__(
        self,
        context_features: str = None,
        feature_consistency_check_job_config_id: str = None,
        generated_features: str = None,
        instance_id: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_request_time: int = None,
        log_user_id: str = None,
        raw_features: str = None,
        scene_name: str = None,
    ):
        # This parameter is required.
        self.context_features = context_features
        # This parameter is required.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # This parameter is required.
        self.generated_features = generated_features
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.log_item_id = log_item_id
        # This parameter is required.
        self.log_request_id = log_request_id
        # This parameter is required.
        self.log_request_time = log_request_time
        # This parameter is required.
        self.log_user_id = log_user_id
        # This parameter is required.
        self.raw_features = raw_features
        # This parameter is required.
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_features is not None:
            result['ContextFeatures'] = self.context_features

        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id

        if self.generated_features is not None:
            result['GeneratedFeatures'] = self.generated_features

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id

        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id

        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        if self.raw_features is not None:
            result['RawFeatures'] = self.raw_features

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContextFeatures') is not None:
            self.context_features = m.get('ContextFeatures')

        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')

        if m.get('GeneratedFeatures') is not None:
            self.generated_features = m.get('GeneratedFeatures')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')

        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')

        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('RawFeatures') is not None:
            self.raw_features = m.get('RawFeatures')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        return self

