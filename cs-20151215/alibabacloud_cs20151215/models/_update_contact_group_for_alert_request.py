# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateContactGroupForAlertRequest(DaraModel):
    def __init__(
        self,
        alert_rule_group_name: str = None,
        contact_group_ids: List[int] = None,
        cr_name: str = None,
        namespace: str = None,
    ):
        # The name of the alert contact group.
        self.alert_rule_group_name = alert_rule_group_name
        # The list of contact group IDs.
        self.contact_group_ids = contact_group_ids
        # The name of the container registry instance.
        self.cr_name = cr_name
        # The namespace in which the resource resides.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_rule_group_name is not None:
            result['alert_rule_group_name'] = self.alert_rule_group_name

        if self.contact_group_ids is not None:
            result['contact_group_ids'] = self.contact_group_ids

        if self.cr_name is not None:
            result['cr_name'] = self.cr_name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alert_rule_group_name') is not None:
            self.alert_rule_group_name = m.get('alert_rule_group_name')

        if m.get('contact_group_ids') is not None:
            self.contact_group_ids = m.get('contact_group_ids')

        if m.get('cr_name') is not None:
            self.cr_name = m.get('cr_name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        return self

