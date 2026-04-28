# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class CsiGetFileInfoResponseBody(DaraModel):
    def __init__(
        self,
        investigation_info: main_models.InvestigationInfo = None,
        url: str = None,
    ):
        self.investigation_info = investigation_info
        self.url = url

    def validate(self):
        if self.investigation_info:
            self.investigation_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.investigation_info is not None:
            result['investigation_info'] = self.investigation_info.to_map()

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('investigation_info') is not None:
            temp_model = main_models.InvestigationInfo()
            self.investigation_info = temp_model.from_map(m.get('investigation_info'))

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

