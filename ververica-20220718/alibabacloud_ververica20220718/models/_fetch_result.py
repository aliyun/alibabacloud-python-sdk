# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class FetchResult(DaraModel):
    def __init__(
        self,
        result_message: str = None,
        result_type: str = None,
        table_results: List[main_models.TableResult] = None,
    ):
        self.result_message = result_message
        self.result_type = result_type
        self.table_results = table_results

    def validate(self):
        if self.table_results:
            for v1 in self.table_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result_message is not None:
            result['resultMessage'] = self.result_message

        if self.result_type is not None:
            result['resultType'] = self.result_type

        result['tableResults'] = []
        if self.table_results is not None:
            for k1 in self.table_results:
                result['tableResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resultMessage') is not None:
            self.result_message = m.get('resultMessage')

        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')

        self.table_results = []
        if m.get('tableResults') is not None:
            for k1 in m.get('tableResults'):
                temp_model = main_models.TableResult()
                self.table_results.append(temp_model.from_map(k1))

        return self

