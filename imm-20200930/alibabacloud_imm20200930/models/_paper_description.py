# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class PaperDescription(DaraModel):
    def __init__(
        self,
        description: List[main_models.Summary] = None,
        title_id: List[str] = None,
    ):
        # The guide result.
        self.description = description
        # The section heading included in the guide result.
        self.title_id = title_id

    def validate(self):
        if self.description:
            for v1 in self.description:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Description'] = []
        if self.description is not None:
            for k1 in self.description:
                result['Description'].append(k1.to_map() if k1 else None)

        if self.title_id is not None:
            result['TitleID'] = self.title_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.description = []
        if m.get('Description') is not None:
            for k1 in m.get('Description'):
                temp_model = main_models.Summary()
                self.description.append(temp_model.from_map(k1))

        if m.get('TitleID') is not None:
            self.title_id = m.get('TitleID')

        return self

