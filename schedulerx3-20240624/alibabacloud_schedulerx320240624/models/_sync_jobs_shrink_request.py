# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncJobsShrinkRequest(DaraModel):
    def __init__(
        self,
        job_ids_shrink: str = None,
        original_app_name: str = None,
        original_cluster_id: str = None,
        target_app_name: str = None,
        target_cluster_id: str = None,
    ):
        # This parameter is required.
        self.job_ids_shrink = job_ids_shrink
        # This parameter is required.
        self.original_app_name = original_app_name
        # This parameter is required.
        self.original_cluster_id = original_cluster_id
        # This parameter is required.
        self.target_app_name = target_app_name
        # This parameter is required.
        self.target_cluster_id = target_cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_ids_shrink is not None:
            result['JobIds'] = self.job_ids_shrink

        if self.original_app_name is not None:
            result['OriginalAppName'] = self.original_app_name

        if self.original_cluster_id is not None:
            result['OriginalClusterId'] = self.original_cluster_id

        if self.target_app_name is not None:
            result['TargetAppName'] = self.target_app_name

        if self.target_cluster_id is not None:
            result['TargetClusterId'] = self.target_cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobIds') is not None:
            self.job_ids_shrink = m.get('JobIds')

        if m.get('OriginalAppName') is not None:
            self.original_app_name = m.get('OriginalAppName')

        if m.get('OriginalClusterId') is not None:
            self.original_cluster_id = m.get('OriginalClusterId')

        if m.get('TargetAppName') is not None:
            self.target_app_name = m.get('TargetAppName')

        if m.get('TargetClusterId') is not None:
            self.target_cluster_id = m.get('TargetClusterId')

        return self

