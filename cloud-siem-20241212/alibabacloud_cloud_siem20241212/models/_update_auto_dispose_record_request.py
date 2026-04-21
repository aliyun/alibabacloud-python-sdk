# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutoDisposeRecordRequest(DaraModel):
    def __init__(
        self,
        auto_decision_conclusion: str = None,
        auto_decision_entity_list: str = None,
        auto_decision_result: str = None,
        auto_dispose_record_id: str = None,
        lang: str = None,
    ):
        self.auto_decision_conclusion = auto_decision_conclusion
        self.auto_decision_entity_list = auto_decision_entity_list
        self.auto_decision_result = auto_decision_result
        # This parameter is required.
        self.auto_dispose_record_id = auto_dispose_record_id
        # This parameter is required.
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_decision_conclusion is not None:
            result['AutoDecisionConclusion'] = self.auto_decision_conclusion

        if self.auto_decision_entity_list is not None:
            result['AutoDecisionEntityList'] = self.auto_decision_entity_list

        if self.auto_decision_result is not None:
            result['AutoDecisionResult'] = self.auto_decision_result

        if self.auto_dispose_record_id is not None:
            result['AutoDisposeRecordId'] = self.auto_dispose_record_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDecisionConclusion') is not None:
            self.auto_decision_conclusion = m.get('AutoDecisionConclusion')

        if m.get('AutoDecisionEntityList') is not None:
            self.auto_decision_entity_list = m.get('AutoDecisionEntityList')

        if m.get('AutoDecisionResult') is not None:
            self.auto_decision_result = m.get('AutoDecisionResult')

        if m.get('AutoDisposeRecordId') is not None:
            self.auto_dispose_record_id = m.get('AutoDisposeRecordId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

