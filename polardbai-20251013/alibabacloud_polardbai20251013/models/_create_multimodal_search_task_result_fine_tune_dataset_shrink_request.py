# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMultimodalSearchTaskResultFineTuneDatasetShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dataset_description: str = None,
        dataset_name: str = None,
        result_index_shrink: str = None,
        result_mode: str = None,
        task_id: str = None,
        top_n: int = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dataset_description = dataset_description
        self.dataset_name = dataset_name
        self.result_index_shrink = result_index_shrink
        self.result_mode = result_mode
        # This parameter is required.
        self.task_id = task_id
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.result_index_shrink is not None:
            result['ResultIndex'] = self.result_index_shrink

        if self.result_mode is not None:
            result['ResultMode'] = self.result_mode

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.top_n is not None:
            result['TopN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('ResultIndex') is not None:
            self.result_index_shrink = m.get('ResultIndex')

        if m.get('ResultMode') is not None:
            self.result_mode = m.get('ResultMode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        return self

