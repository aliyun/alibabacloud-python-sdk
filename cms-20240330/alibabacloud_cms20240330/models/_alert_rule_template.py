# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlertRuleTemplate(DaraModel):
    def __init__(
        self,
        alert_type: str = None,
        apply_count: int = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        is_system: int = None,
        labels: str = None,
        rule_configs: str = None,
        status: int = None,
        sub_type: str = None,
        template_name: str = None,
        user_id: str = None,
        uuid: str = None,
    ):
        # The type of the alert.
        self.alert_type = alert_type
        # The number of alert rules created from this template.
        self.apply_count = apply_count
        # The description of the template.
        self.description = description
        # The creation time of the template, as a UNIX timestamp.
        self.gmt_create = gmt_create
        # The time the template was last modified, as a UNIX timestamp.
        self.gmt_modified = gmt_modified
        # The ID of the alert rule template.
        self.id = id
        # Indicates whether the template is system-defined. Valid values: `0` (user-defined) and `1` (system-defined).
        self.is_system = is_system
        # The labels associated with the template, formatted as a JSON string.
        self.labels = labels
        # The rule configuration, formatted as a JSON string.
        self.rule_configs = rule_configs
        # The status of the template.
        self.status = status
        # The subtype of the alert.
        self.sub_type = sub_type
        # The name of the alert rule template.
        self.template_name = template_name
        # The ID of the user who owns the template.
        self.user_id = user_id
        # The universally unique identifier (UUID) of the template.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_type is not None:
            result['alertType'] = self.alert_type

        if self.apply_count is not None:
            result['applyCount'] = self.apply_count

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.is_system is not None:
            result['isSystem'] = self.is_system

        if self.labels is not None:
            result['labels'] = self.labels

        if self.rule_configs is not None:
            result['ruleConfigs'] = self.rule_configs

        if self.status is not None:
            result['status'] = self.status

        if self.sub_type is not None:
            result['subType'] = self.sub_type

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertType') is not None:
            self.alert_type = m.get('alertType')

        if m.get('applyCount') is not None:
            self.apply_count = m.get('applyCount')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isSystem') is not None:
            self.is_system = m.get('isSystem')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('ruleConfigs') is not None:
            self.rule_configs = m.get('ruleConfigs')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('subType') is not None:
            self.sub_type = m.get('subType')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

