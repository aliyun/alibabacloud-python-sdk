# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class UpdateJobInfo(DaraModel):
    def __init__(
        self,
        import_qos: main_models.ImportQos = None,
        status: str = None,
    ):
        self.import_qos = import_qos
        self.status = status

    def validate(self):
        if self.import_qos:
            self.import_qos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.import_qos is not None:
            result['ImportQos'] = self.import_qos.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportQos') is not None:
            temp_model = main_models.ImportQos()
            self.import_qos = temp_model.from_map(m.get('ImportQos'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

