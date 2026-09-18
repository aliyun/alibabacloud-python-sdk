# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paimodelgallery20250630 import models as main_models
from darabonba.model import DaraModel

class ListDistillationTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        distillation_templates: List[main_models.DistillationTemplateSummary] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of distillation template summaries, sorted by OrderNumber in ascending order.
        self.distillation_templates = distillation_templates
        # The page number, which echoes the PageNumber value in the request.
        self.page_number = page_number
        # The number of entries per page, which echoes the PageSize value in the request.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of templates that match the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.distillation_templates:
            for v1 in self.distillation_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DistillationTemplates'] = []
        if self.distillation_templates is not None:
            for k1 in self.distillation_templates:
                result['DistillationTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.distillation_templates = []
        if m.get('DistillationTemplates') is not None:
            for k1 in m.get('DistillationTemplates'):
                temp_model = main_models.DistillationTemplateSummary()
                self.distillation_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

