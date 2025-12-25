# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetRealtimeDeliveryFieldResponseBody(DaraModel):
    def __init__(
        self,
        field_content: Dict[str, main_models.FieldContentValue] = None,
        request_id: str = None,
    ):
        # The fields returned.
        self.field_content = field_content
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.field_content:
            for v1 in self.field_content.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FieldContent'] = {}
        if self.field_content is not None:
            for k1, v1 in self.field_content.items():
                result['FieldContent'][k1] = v1.to_map() if v1 else None

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.field_content = {}
        if m.get('FieldContent') is not None:
            for k1, v1 in m.get('FieldContent').items():
                temp_model = main_models.FieldContentValue()
                self.field_content[k1] = temp_model.from_map(v1)

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

