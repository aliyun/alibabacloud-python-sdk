# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class MonitorSlsAlert(DaraModel):
    def __init__(
        self,
        condition: str = None,
        env: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        monitor_notify_strategy: main_models.MonitorNotifyStrategy = None,
        monitor_sls_alert_rules: List[main_models.MonitorSlsAlertRule] = None,
        name: str = None,
        pbc_id: str = None,
        remark: str = None,
        service_group_id: str = None,
        type: str = None,
    ):
        self.condition = condition
        self.env = env
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        # This parameter is required.
        self.monitor_notify_strategy = monitor_notify_strategy
        self.monitor_sls_alert_rules = monitor_sls_alert_rules
        self.name = name
        self.pbc_id = pbc_id
        self.remark = remark
        self.service_group_id = service_group_id
        self.type = type

    def validate(self):
        if self.monitor_notify_strategy:
            self.monitor_notify_strategy.validate()
        if self.monitor_sls_alert_rules:
            for v1 in self.monitor_sls_alert_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['condition'] = self.condition

        if self.env is not None:
            result['env'] = self.env

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.monitor_notify_strategy is not None:
            result['monitorNotifyStrategy'] = self.monitor_notify_strategy.to_map()

        result['monitorSlsAlertRules'] = []
        if self.monitor_sls_alert_rules is not None:
            for k1 in self.monitor_sls_alert_rules:
                result['monitorSlsAlertRules'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.remark is not None:
            result['remark'] = self.remark

        if self.service_group_id is not None:
            result['serviceGroupId'] = self.service_group_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('monitorNotifyStrategy') is not None:
            temp_model = main_models.MonitorNotifyStrategy()
            self.monitor_notify_strategy = temp_model.from_map(m.get('monitorNotifyStrategy'))

        self.monitor_sls_alert_rules = []
        if m.get('monitorSlsAlertRules') is not None:
            for k1 in m.get('monitorSlsAlertRules'):
                temp_model = main_models.MonitorSlsAlertRule()
                self.monitor_sls_alert_rules.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('serviceGroupId') is not None:
            self.service_group_id = m.get('serviceGroupId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

