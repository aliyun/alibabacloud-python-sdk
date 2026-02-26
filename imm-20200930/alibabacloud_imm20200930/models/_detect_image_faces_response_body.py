# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DetectImageFacesResponseBody(DaraModel):
    def __init__(
        self,
        faces: List[main_models.Figure] = None,
        request_id: str = None,
    ):
        # The faces.
        self.faces = faces
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.faces:
            for v1 in self.faces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Faces'] = []
        if self.faces is not None:
            for k1 in self.faces:
                result['Faces'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.faces = []
        if m.get('Faces') is not None:
            for k1 in m.get('Faces'):
                temp_model = main_models.Figure()
                self.faces.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

