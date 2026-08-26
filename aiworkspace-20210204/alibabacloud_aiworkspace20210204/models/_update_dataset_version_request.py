# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class UpdateDatasetVersionRequest(DaraModel):
    def __init__(
        self,
        data_count: int = None,
        data_size: int = None,
        dataset_task_ram_role: str = None,
        description: str = None,
        options: str = None,
        user_metrics_endpoints: List[main_models.UserMetricsEndpoint] = None,
    ):
        # The number of dataset files.
        self.data_count = data_count
        # The size of the space occupied by dataset files. Unit: bytes.
        self.data_size = data_size
        # DatasetTaskRamRole
        self.dataset_task_ram_role = dataset_task_ram_role
        # The custom description of the dataset, which is used to distinguish different datasets.
        self.description = description
        # The extended field in JsonString format. When DLC uses the dataset, you can specify the default mount path of the dataset by configuring the mountPath field.
        self.options = options
        self.user_metrics_endpoints = user_metrics_endpoints

    def validate(self):
        if self.user_metrics_endpoints:
            for v1 in self.user_metrics_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_count is not None:
            result['DataCount'] = self.data_count

        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.dataset_task_ram_role is not None:
            result['DatasetTaskRamRole'] = self.dataset_task_ram_role

        if self.description is not None:
            result['Description'] = self.description

        if self.options is not None:
            result['Options'] = self.options

        result['UserMetricsEndpoints'] = []
        if self.user_metrics_endpoints is not None:
            for k1 in self.user_metrics_endpoints:
                result['UserMetricsEndpoints'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCount') is not None:
            self.data_count = m.get('DataCount')

        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('DatasetTaskRamRole') is not None:
            self.dataset_task_ram_role = m.get('DatasetTaskRamRole')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        self.user_metrics_endpoints = []
        if m.get('UserMetricsEndpoints') is not None:
            for k1 in m.get('UserMetricsEndpoints'):
                temp_model = main_models.UserMetricsEndpoint()
                self.user_metrics_endpoints.append(temp_model.from_map(k1))

        return self

