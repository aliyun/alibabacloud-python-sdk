# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SlotStatusDetail(DaraModel):
    def __init__(
        self,
        loaded_file_num: int = None,
        loaded_file_size: str = None,
        loading_time_cost: int = None,
    ):
        self.loaded_file_num = loaded_file_num
        self.loaded_file_size = loaded_file_size
        self.loading_time_cost = loading_time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.loaded_file_num is not None:
            result['LoadedFileNum'] = self.loaded_file_num

        if self.loaded_file_size is not None:
            result['LoadedFileSize'] = self.loaded_file_size

        if self.loading_time_cost is not None:
            result['LoadingTimeCost'] = self.loading_time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadedFileNum') is not None:
            self.loaded_file_num = m.get('LoadedFileNum')

        if m.get('LoadedFileSize') is not None:
            self.loaded_file_size = m.get('LoadedFileSize')

        if m.get('LoadingTimeCost') is not None:
            self.loading_time_cost = m.get('LoadingTimeCost')

        return self

