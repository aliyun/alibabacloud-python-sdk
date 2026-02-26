# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class GetBatchResponseBody(DaraModel):
    def __init__(
        self,
        batch: main_models.DataIngestion = None,
        request_id: str = None,
    ):
        # The information about the batch processing task.
        self.batch = batch
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.batch:
            self.batch.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch is not None:
            result['Batch'] = self.batch.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Batch') is not None:
            temp_model = main_models.DataIngestion()
            self.batch = temp_model.from_map(m.get('Batch'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

