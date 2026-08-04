# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class BatchOpResultDTO(DaraModel):
    def __init__(
        self,
        failed: List[main_models.BatchFailedItemDTO] = None,
        succeeded: List[int] = None,
    ):
        self.failed = failed
        self.succeeded = succeeded

    def validate(self):
        if self.failed:
            for v1 in self.failed:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['failed'] = []
        if self.failed is not None:
            for k1 in self.failed:
                result['failed'].append(k1.to_map() if k1 else None)

        if self.succeeded is not None:
            result['succeeded'] = self.succeeded

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed = []
        if m.get('failed') is not None:
            for k1 in m.get('failed'):
                temp_model = main_models.BatchFailedItemDTO()
                self.failed.append(temp_model.from_map(k1))

        if m.get('succeeded') is not None:
            self.succeeded = m.get('succeeded')

        return self

