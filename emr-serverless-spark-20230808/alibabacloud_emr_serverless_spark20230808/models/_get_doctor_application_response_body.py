# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class GetDoctorApplicationResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDoctorApplicationResponseBodyData = None,
    ):
        # The data returned.
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetDoctorApplicationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        return self

class GetDoctorApplicationResponseBodyData(DaraModel):
    def __init__(
        self,
        suggestions: List[str] = None,
    ):
        # The diagnostics list.
        self.suggestions = suggestions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.suggestions is not None:
            result['suggestions'] = self.suggestions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('suggestions') is not None:
            self.suggestions = m.get('suggestions')

        return self

