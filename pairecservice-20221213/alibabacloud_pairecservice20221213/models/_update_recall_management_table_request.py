# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecallManagementTableRequest(DaraModel):
    def __init__(
        self,
        enable_data_size_fluctuation_threshold: bool = None,
        enable_row_count_fluctuation_threshold: bool = None,
        index_version_id: str = None,
        instance_id: str = None,
        max_data_size_fluctuation_threshold: int = None,
        max_row_count_fluctuation_threshold: int = None,
        min_data_size_fluctuation_threshold: int = None,
        min_row_count_fluctuation_threshold: int = None,
    ):
        self.enable_data_size_fluctuation_threshold = enable_data_size_fluctuation_threshold
        self.enable_row_count_fluctuation_threshold = enable_row_count_fluctuation_threshold
        self.index_version_id = index_version_id
        # This parameter is required.
        self.instance_id = instance_id
        self.max_data_size_fluctuation_threshold = max_data_size_fluctuation_threshold
        self.max_row_count_fluctuation_threshold = max_row_count_fluctuation_threshold
        self.min_data_size_fluctuation_threshold = min_data_size_fluctuation_threshold
        self.min_row_count_fluctuation_threshold = min_row_count_fluctuation_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_data_size_fluctuation_threshold is not None:
            result['EnableDataSizeFluctuationThreshold'] = self.enable_data_size_fluctuation_threshold

        if self.enable_row_count_fluctuation_threshold is not None:
            result['EnableRowCountFluctuationThreshold'] = self.enable_row_count_fluctuation_threshold

        if self.index_version_id is not None:
            result['IndexVersionId'] = self.index_version_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_data_size_fluctuation_threshold is not None:
            result['MaxDataSizeFluctuationThreshold'] = self.max_data_size_fluctuation_threshold

        if self.max_row_count_fluctuation_threshold is not None:
            result['MaxRowCountFluctuationThreshold'] = self.max_row_count_fluctuation_threshold

        if self.min_data_size_fluctuation_threshold is not None:
            result['MinDataSizeFluctuationThreshold'] = self.min_data_size_fluctuation_threshold

        if self.min_row_count_fluctuation_threshold is not None:
            result['MinRowCountFluctuationThreshold'] = self.min_row_count_fluctuation_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableDataSizeFluctuationThreshold') is not None:
            self.enable_data_size_fluctuation_threshold = m.get('EnableDataSizeFluctuationThreshold')

        if m.get('EnableRowCountFluctuationThreshold') is not None:
            self.enable_row_count_fluctuation_threshold = m.get('EnableRowCountFluctuationThreshold')

        if m.get('IndexVersionId') is not None:
            self.index_version_id = m.get('IndexVersionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxDataSizeFluctuationThreshold') is not None:
            self.max_data_size_fluctuation_threshold = m.get('MaxDataSizeFluctuationThreshold')

        if m.get('MaxRowCountFluctuationThreshold') is not None:
            self.max_row_count_fluctuation_threshold = m.get('MaxRowCountFluctuationThreshold')

        if m.get('MinDataSizeFluctuationThreshold') is not None:
            self.min_data_size_fluctuation_threshold = m.get('MinDataSizeFluctuationThreshold')

        if m.get('MinRowCountFluctuationThreshold') is not None:
            self.min_row_count_fluctuation_threshold = m.get('MinRowCountFluctuationThreshold')

        return self

