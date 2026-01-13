# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BackflowFeatureConsistencyCheckJobDataRequest(DaraModel):
    def __init__(
        self,
        feature_consistency_check_job_config_id: str = None,
        instance_id: str = None,
        item_features: str = None,
        log_item_id: str = None,
        log_request_id: str = None,
        log_request_time: int = None,
        log_user_id: str = None,
        scene_name: str = None,
        scores: str = None,
        service_name: str = None,
        user_features: str = None,
    ):
        # This parameter is required.
        self.feature_consistency_check_job_config_id = feature_consistency_check_job_config_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.item_features = item_features
        # This parameter is required.
        self.log_item_id = log_item_id
        # This parameter is required.
        self.log_request_id = log_request_id
        # This parameter is required.
        self.log_request_time = log_request_time
        # This parameter is required.
        self.log_user_id = log_user_id
        # This parameter is required.
        self.scene_name = scene_name
        # This parameter is required.
        self.scores = scores
        self.service_name = service_name
        # This parameter is required.
        self.user_features = user_features

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature_consistency_check_job_config_id is not None:
            result['FeatureConsistencyCheckJobConfigId'] = self.feature_consistency_check_job_config_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.item_features is not None:
            result['ItemFeatures'] = self.item_features

        if self.log_item_id is not None:
            result['LogItemId'] = self.log_item_id

        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id

        if self.log_request_time is not None:
            result['LogRequestTime'] = self.log_request_time

        if self.log_user_id is not None:
            result['LogUserId'] = self.log_user_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.scores is not None:
            result['Scores'] = self.scores

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.user_features is not None:
            result['UserFeatures'] = self.user_features

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeatureConsistencyCheckJobConfigId') is not None:
            self.feature_consistency_check_job_config_id = m.get('FeatureConsistencyCheckJobConfigId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemFeatures') is not None:
            self.item_features = m.get('ItemFeatures')

        if m.get('LogItemId') is not None:
            self.log_item_id = m.get('LogItemId')

        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')

        if m.get('LogRequestTime') is not None:
            self.log_request_time = m.get('LogRequestTime')

        if m.get('LogUserId') is not None:
            self.log_user_id = m.get('LogUserId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('Scores') is not None:
            self.scores = m.get('Scores')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UserFeatures') is not None:
            self.user_features = m.get('UserFeatures')

        return self

