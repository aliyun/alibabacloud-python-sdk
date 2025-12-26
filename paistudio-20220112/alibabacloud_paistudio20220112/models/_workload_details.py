# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class WorkloadDetails(DaraModel):
    def __init__(
        self,
        dlc: main_models.QuotaJob = None,
        dsw: main_models.QuotaJob = None,
        eas: main_models.QuotaJob = None,
        summary: main_models.QuotaJob = None,
    ):
        self.dlc = dlc
        self.dsw = dsw
        self.eas = eas
        self.summary = summary

    def validate(self):
        if self.dlc:
            self.dlc.validate()
        if self.dsw:
            self.dsw.validate()
        if self.eas:
            self.eas.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dlc is not None:
            result['DLC'] = self.dlc.to_map()

        if self.dsw is not None:
            result['DSW'] = self.dsw.to_map()

        if self.eas is not None:
            result['EAS'] = self.eas.to_map()

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DLC') is not None:
            temp_model = main_models.QuotaJob()
            self.dlc = temp_model.from_map(m.get('DLC'))

        if m.get('DSW') is not None:
            temp_model = main_models.QuotaJob()
            self.dsw = temp_model.from_map(m.get('DSW'))

        if m.get('EAS') is not None:
            temp_model = main_models.QuotaJob()
            self.eas = temp_model.from_map(m.get('EAS'))

        if m.get('Summary') is not None:
            temp_model = main_models.QuotaJob()
            self.summary = temp_model.from_map(m.get('Summary'))

        return self

