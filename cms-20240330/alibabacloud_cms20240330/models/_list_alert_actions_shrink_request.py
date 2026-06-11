# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertActionsShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_action_ids_shrink: str = None,
        alert_action_name: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The unique IDs of the alert action integrations.
        self.alert_action_ids_shrink = alert_action_ids_shrink
        # The name of the alert action integration.
        self.alert_action_name = alert_action_name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 100.
        self.page_size = page_size
        # The type of the alert action integration.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_ids_shrink is not None:
            result['alertActionIds'] = self.alert_action_ids_shrink

        if self.alert_action_name is not None:
            result['alertActionName'] = self.alert_action_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids_shrink = m.get('alertActionIds')

        if m.get('alertActionName') is not None:
            self.alert_action_name = m.get('alertActionName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

