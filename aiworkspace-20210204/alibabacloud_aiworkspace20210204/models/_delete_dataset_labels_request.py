# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDatasetLabelsRequest(DaraModel):
    def __init__(
        self,
        label_keys: str = None,
    ):
        # The tag key. You can call [GetDataset](https://help.aliyun.com/document_detail/457218.html) to obtain the tag key. Multiple tag keys are separated by commas (,).
        self.label_keys = label_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_keys is not None:
            result['LabelKeys'] = self.label_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKeys') is not None:
            self.label_keys = m.get('LabelKeys')

        return self

