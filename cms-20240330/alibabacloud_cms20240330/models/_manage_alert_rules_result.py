# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ManageAlertRulesResult(DaraModel):
    def __init__(
        self,
        alert_rule: main_models.AlertRuleV2 = None,
        deleted_count: int = None,
        deleted_uuid_list: List[str] = None,
    ):
        self.alert_rule = alert_rule
        # 成功删除的规则数量
        self.deleted_count = deleted_count
        # 成功删除的规则 UUID 列表
        self.deleted_uuid_list = deleted_uuid_list

    def validate(self):
        if self.alert_rule:
            self.alert_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_rule is not None:
            result['alertRule'] = self.alert_rule.to_map()

        if self.deleted_count is not None:
            result['deletedCount'] = self.deleted_count

        if self.deleted_uuid_list is not None:
            result['deletedUuidList'] = self.deleted_uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertRule') is not None:
            temp_model = main_models.AlertRuleV2()
            self.alert_rule = temp_model.from_map(m.get('alertRule'))

        if m.get('deletedCount') is not None:
            self.deleted_count = m.get('deletedCount')

        if m.get('deletedUuidList') is not None:
            self.deleted_uuid_list = m.get('deletedUuidList')

        return self

