# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class DqlResult(DaraModel):
    def __init__(
        self,
        statement_index: int = None,
        submit_preview_result: main_models.SubmitPreviewResult = None,
        table_results: List[main_models.TableResult] = None,
    ):
        self.statement_index = statement_index
        self.submit_preview_result = submit_preview_result
        self.table_results = table_results

    def validate(self):
        if self.submit_preview_result:
            self.submit_preview_result.validate()
        if self.table_results:
            for v1 in self.table_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.statement_index is not None:
            result['statementIndex'] = self.statement_index

        if self.submit_preview_result is not None:
            result['submitPreviewResult'] = self.submit_preview_result.to_map()

        result['tableResults'] = []
        if self.table_results is not None:
            for k1 in self.table_results:
                result['tableResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statementIndex') is not None:
            self.statement_index = m.get('statementIndex')

        if m.get('submitPreviewResult') is not None:
            temp_model = main_models.SubmitPreviewResult()
            self.submit_preview_result = temp_model.from_map(m.get('submitPreviewResult'))

        self.table_results = []
        if m.get('tableResults') is not None:
            for k1 in m.get('tableResults'):
                temp_model = main_models.TableResult()
                self.table_results.append(temp_model.from_map(k1))

        return self

