# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class UpdateDatasetResponseBody(DaraModel):
    def __init__(
        self,
        dataset: main_models.Dataset = None,
        request_id: str = None,
    ):
        # 数据集。
        self.dataset = dataset
        # 请求ID。
        self.request_id = request_id

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset is not None:
            result['Dataset'] = self.dataset.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dataset') is not None:
            temp_model = main_models.Dataset()
            self.dataset = temp_model.from_map(m.get('Dataset'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

