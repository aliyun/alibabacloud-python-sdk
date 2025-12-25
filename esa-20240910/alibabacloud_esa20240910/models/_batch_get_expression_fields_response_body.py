# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class BatchGetExpressionFieldsResponseBody(DaraModel):
    def __init__(
        self,
        fields: List[main_models.BatchGetExpressionFieldsResponseBodyFields] = None,
        request_id: str = None,
    ):
        # List of match fields.
        self.fields = fields
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.BatchGetExpressionFieldsResponseBodyFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchGetExpressionFieldsResponseBodyFields(DaraModel):
    def __init__(
        self,
        fields: List[str] = None,
        id: str = None,
    ):
        # List of match fields for a single expression.
        self.fields = fields
        # ID of the expression, corresponding to the ID in the input parameters.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

