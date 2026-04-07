# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateClusterConfigsShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: int = None,
        config_type: str = None,
        config_values_shrink: str = None,
        project_id: int = None,
    ):
        # The ID of the cluster associated with DataWorks.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The configuration type of the cluster. Valid values:
        # 
        # *   SPARK_CONF: SPARK parameters
        # 
        # This parameter is required.
        self.config_type = config_type
        # The configuration information of the cluster submodule.
        # 
        # This parameter is required.
        self.config_values_shrink = config_values_shrink
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.config_values_shrink is not None:
            result['ConfigValues'] = self.config_values_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('ConfigValues') is not None:
            self.config_values_shrink = m.get('ConfigValues')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

