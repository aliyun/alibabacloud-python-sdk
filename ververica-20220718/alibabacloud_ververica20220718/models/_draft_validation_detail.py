# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class DraftValidationDetail(DaraModel):
    def __init__(
        self,
        draft_meta_info_error_details: List[main_models.DraftMetaInfoErrorDetail] = None,
        sql_error_detail: main_models.ValidationErrorDetails = None,
        sql_validation_result: str = None,
    ):
        self.draft_meta_info_error_details = draft_meta_info_error_details
        self.sql_error_detail = sql_error_detail
        self.sql_validation_result = sql_validation_result

    def validate(self):
        if self.draft_meta_info_error_details:
            for v1 in self.draft_meta_info_error_details:
                 if v1:
                    v1.validate()
        if self.sql_error_detail:
            self.sql_error_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['draftMetaInfoErrorDetails'] = []
        if self.draft_meta_info_error_details is not None:
            for k1 in self.draft_meta_info_error_details:
                result['draftMetaInfoErrorDetails'].append(k1.to_map() if k1 else None)

        if self.sql_error_detail is not None:
            result['sqlErrorDetail'] = self.sql_error_detail.to_map()

        if self.sql_validation_result is not None:
            result['sqlValidationResult'] = self.sql_validation_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.draft_meta_info_error_details = []
        if m.get('draftMetaInfoErrorDetails') is not None:
            for k1 in m.get('draftMetaInfoErrorDetails'):
                temp_model = main_models.DraftMetaInfoErrorDetail()
                self.draft_meta_info_error_details.append(temp_model.from_map(k1))

        if m.get('sqlErrorDetail') is not None:
            temp_model = main_models.ValidationErrorDetails()
            self.sql_error_detail = temp_model.from_map(m.get('sqlErrorDetail'))

        if m.get('sqlValidationResult') is not None:
            self.sql_validation_result = m.get('sqlValidationResult')

        return self

