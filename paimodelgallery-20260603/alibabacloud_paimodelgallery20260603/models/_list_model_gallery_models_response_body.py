# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paimodelgallery20260603 import models as main_models
from darabonba.model import DaraModel

class ListModelGalleryModelsResponseBody(DaraModel):
    def __init__(
        self,
        models: main_models.ModelGalleryModel = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.models = models
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.models:
            self.models.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.models is not None:
            result['Models'] = self.models.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Models') is not None:
            temp_model = main_models.ModelGalleryModel()
            self.models = temp_model.from_map(m.get('Models'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

