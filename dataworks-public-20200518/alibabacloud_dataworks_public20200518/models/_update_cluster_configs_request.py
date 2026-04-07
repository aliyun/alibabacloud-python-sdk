# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class UpdateClusterConfigsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: int = None,
        config_type: str = None,
        config_values: List[main_models.ClusterConfig] = None,
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
        self.config_values = config_values
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.config_values:
            for v1 in self.config_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        result['ConfigValues'] = []
        if self.config_values is not None:
            for k1 in self.config_values:
                result['ConfigValues'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        self.config_values = []
        if m.get('ConfigValues') is not None:
            for k1 in m.get('ConfigValues'):
                temp_model = main_models.ClusterConfig()
                self.config_values.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

