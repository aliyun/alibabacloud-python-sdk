# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paimodelgallery20250630 import models as main_models
from darabonba.model import DaraModel

class GetDistillationTemplateResponseBody(DaraModel):
    def __init__(
        self,
        distillation_template: main_models.DistillationTemplate = None,
        request_id: str = None,
    ):
        # The distillation template details.
        self.distillation_template = distillation_template
        # **Request ID**
        self.request_id = request_id

    def validate(self):
        if self.distillation_template:
            self.distillation_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distillation_template is not None:
            result['DistillationTemplate'] = self.distillation_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistillationTemplate') is not None:
            temp_model = main_models.DistillationTemplate()
            self.distillation_template = temp_model.from_map(m.get('DistillationTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

