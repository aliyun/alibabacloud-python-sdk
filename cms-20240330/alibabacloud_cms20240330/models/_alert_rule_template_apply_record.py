# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlertRuleTemplateApplyRecord(DaraModel):
    def __init__(
        self,
        apply_config: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        region_id: str = None,
        rule_id: str = None,
        status: str = None,
        template_uuid: str = None,
        user_id: str = None,
    ):
        # The effective configuration for the rule application.
        self.apply_config = apply_config
        # The time when the record was created.
        self.gmt_create = gmt_create
        # The time when the record was updated.
        self.gmt_modified = gmt_modified
        # The record ID.
        self.id = id
        # The region ID.
        self.region_id = region_id
        # The rule ID.
        self.rule_id = rule_id
        # The status.
        self.status = status
        # The UUID of the alert rule template.
        self.template_uuid = template_uuid
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_config is not None:
            result['applyConfig'] = self.apply_config

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.status is not None:
            result['status'] = self.status

        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applyConfig') is not None:
            self.apply_config = m.get('applyConfig')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

