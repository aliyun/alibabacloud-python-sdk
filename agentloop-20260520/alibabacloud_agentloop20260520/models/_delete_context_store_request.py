# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteContextStoreRequest(DaraModel):
    def __init__(
        self,
        delete_output_dataset: bool = None,
    ):
        # Specifies whether to simultaneously delete the memory output dataset (memory type). Default value: false.
        self.delete_output_dataset = delete_output_dataset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_output_dataset is not None:
            result['deleteOutputDataset'] = self.delete_output_dataset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleteOutputDataset') is not None:
            self.delete_output_dataset = m.get('deleteOutputDataset')

        return self

