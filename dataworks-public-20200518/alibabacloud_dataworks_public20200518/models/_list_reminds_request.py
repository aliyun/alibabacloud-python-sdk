# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRemindsRequest(DaraModel):
    def __init__(
        self,
        alert_target: str = None,
        founder: str = None,
        node_id: int = None,
        page_number: int = None,
        page_size: int = None,
        remind_types: str = None,
        search_text: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to receive alert notifications.
        self.alert_target = alert_target
        # The ID of the Alibaba Cloud account that is used to create the custom alert rules.
        self.founder = founder
        # The ID of the node to which the custom alert rules are applied. You can use the ID to search for the custom alert rules that are applied to the node.
        self.node_id = node_id
        # The number of the page to return. Valid values: 1 to 30. Default value: 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The conditions that trigger an alert for the node. Valid values: FINISHED, UNFINISHED, ERROR, CYCLE_UNFINISHED, and TIMEOUT. The value FINISHED indicates that the node finishes running. The value UNFINISHED indicates that the node is still running at the specified point in time. The value ERROR indicates that an error occurs when the node is running. The value CYCLE_UNFINISHED indicates that the node does not finish running in the specified scheduling cycle. The value TIMEOUT indicates that the node times out. You can specify multiple conditions for a custom alert rule. If you specify multiple condition, separate them with commas (,).
        self.remind_types = remind_types
        # The keyword in a rule name that is used to search for the rule. Fuzzy search is supported.
        self.search_text = search_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_target is not None:
            result['AlertTarget'] = self.alert_target

        if self.founder is not None:
            result['Founder'] = self.founder

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remind_types is not None:
            result['RemindTypes'] = self.remind_types

        if self.search_text is not None:
            result['SearchText'] = self.search_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertTarget') is not None:
            self.alert_target = m.get('AlertTarget')

        if m.get('Founder') is not None:
            self.founder = m.get('Founder')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RemindTypes') is not None:
            self.remind_types = m.get('RemindTypes')

        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')

        return self

