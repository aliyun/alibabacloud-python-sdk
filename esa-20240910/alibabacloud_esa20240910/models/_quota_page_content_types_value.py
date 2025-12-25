# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class QuotaPageContentTypesValue(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        content_length: main_models.WafQuotaInteger = None,
    ):
        # The switch for the Content-Type type in custom response pages.
        self.enable = enable
        # The content length quota for the Content-Type in custom response pages.
        self.content_length = content_length

    def validate(self):
        if self.content_length:
            self.content_length.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.content_length is not None:
            result['ContentLength'] = self.content_length.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('ContentLength') is not None:
            temp_model = main_models.WafQuotaInteger()
            self.content_length = temp_model.from_map(m.get('ContentLength'))

        return self

