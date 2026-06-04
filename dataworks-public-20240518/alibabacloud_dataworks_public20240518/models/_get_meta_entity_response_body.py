# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetMetaEntityResponseBody(DaraModel):
    def __init__(
        self,
        meta_entity: main_models.MetaEntity = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.meta_entity = meta_entity
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.meta_entity:
            self.meta_entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_entity is not None:
            result['MetaEntity'] = self.meta_entity.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaEntity') is not None:
            temp_model = main_models.MetaEntity()
            self.meta_entity = temp_model.from_map(m.get('MetaEntity'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

