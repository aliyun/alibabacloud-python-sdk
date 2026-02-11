# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAlertRuleRequest(DaraModel):
    def __init__(
        self,
        alert_id: int = None,
        contact_group_ids: str = None,
        is_auto_start: bool = None,
        region_id: str = None,
        templage_alert_config: str = None,
    ):
        # This parameter is required.
        self.alert_id = alert_id
        self.contact_group_ids = contact_group_ids
        self.is_auto_start = is_auto_start
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.templage_alert_config = templage_alert_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id

        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids

        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')

        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')

        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')

        return self

