# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class RegisterLineageRelationRequest(DaraModel):
    def __init__(
        self,
        lineage_relation_register_vo: main_models.LineageRelationRegisterVO = None,
    ):
        # The structure whose lineage you want to register to DataWorks.
        # 
        # This parameter is required.
        self.lineage_relation_register_vo = lineage_relation_register_vo

    def validate(self):
        if self.lineage_relation_register_vo:
            self.lineage_relation_register_vo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lineage_relation_register_vo is not None:
            result['LineageRelationRegisterVO'] = self.lineage_relation_register_vo.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineageRelationRegisterVO') is not None:
            temp_model = main_models.LineageRelationRegisterVO()
            self.lineage_relation_register_vo = temp_model.from_map(m.get('LineageRelationRegisterVO'))

        return self

