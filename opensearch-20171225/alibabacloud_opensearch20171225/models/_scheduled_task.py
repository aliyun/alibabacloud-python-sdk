# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class ScheduledTask(DaraModel):
    def __init__(
        self,
        auto_switch: bool = None,
        cron: str = None,
        enabled: bool = None,
        filter: main_models.ScheduledTaskFilter = None,
        forked_app_id: str = None,
        permanent: bool = None,
        run_now: bool = None,
        type: str = None,
        version: str = None,
    ):
        self.auto_switch = auto_switch
        self.cron = cron
        self.enabled = enabled
        self.filter = filter
        self.forked_app_id = forked_app_id
        self.permanent = permanent
        self.run_now = run_now
        self.type = type
        self.version = version

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_switch is not None:
            result['autoSwitch'] = self.auto_switch

        if self.cron is not None:
            result['cron'] = self.cron

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.filter is not None:
            result['filter'] = self.filter.to_map()

        if self.forked_app_id is not None:
            result['forkedAppId'] = self.forked_app_id

        if self.permanent is not None:
            result['permanent'] = self.permanent

        if self.run_now is not None:
            result['runNow'] = self.run_now

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoSwitch') is not None:
            self.auto_switch = m.get('autoSwitch')

        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('filter') is not None:
            temp_model = main_models.ScheduledTaskFilter()
            self.filter = temp_model.from_map(m.get('filter'))

        if m.get('forkedAppId') is not None:
            self.forked_app_id = m.get('forkedAppId')

        if m.get('permanent') is not None:
            self.permanent = m.get('permanent')

        if m.get('runNow') is not None:
            self.run_now = m.get('runNow')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ScheduledTaskFilter(DaraModel):
    def __init__(
        self,
        days: int = None,
        expression: str = None,
        field: str = None,
        unit: str = None,
    ):
        self.days = days
        self.expression = expression
        self.field = field
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days is not None:
            result['days'] = self.days

        if self.expression is not None:
            result['expression'] = self.expression

        if self.field is not None:
            result['field'] = self.field

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('days') is not None:
            self.days = m.get('days')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

