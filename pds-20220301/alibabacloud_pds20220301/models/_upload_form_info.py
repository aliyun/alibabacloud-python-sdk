# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UploadFormInfo(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        form_data: Dict[str, str] = None,
    ):
        self.endpoint = endpoint
        self.form_data = form_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.form_data is not None:
            result['form_data'] = self.form_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('form_data') is not None:
            self.form_data = m.get('form_data')

        return self

