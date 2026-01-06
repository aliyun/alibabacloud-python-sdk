# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class Relation(DaraModel):
    def __init__(
        self,
        err_msg: str = None,
        lineage_relation: main_models.LineageRelation = None,
        result: bool = None,
    ):
        self.err_msg = err_msg
        self.lineage_relation = lineage_relation
        self.result = result

    def validate(self):
        if self.lineage_relation:
            self.lineage_relation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_msg is not None:
            result['ErrMsg'] = self.err_msg

        if self.lineage_relation is not None:
            result['LineageRelation'] = self.lineage_relation.to_map()

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMsg') is not None:
            self.err_msg = m.get('ErrMsg')

        if m.get('LineageRelation') is not None:
            temp_model = main_models.LineageRelation()
            self.lineage_relation = temp_model.from_map(m.get('LineageRelation'))

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

