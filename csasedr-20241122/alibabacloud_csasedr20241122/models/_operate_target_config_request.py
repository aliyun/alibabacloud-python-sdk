# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateTargetConfigRequest(DaraModel):
    def __init__(
        self,
        selection_key: str = None,
        status: str = None,
        switch_id_list: List[str] = None,
    ):
        # The key of the rule switch configuration associated with the policy. It must be the same as the key used in the ListSystemConfigRules query.
        # 
        # This parameter is required.
        self.selection_key = selection_key
        # The status of the rule switch. Valid values:
        # - **add**: Enabled.
        # - **del**: Disabled.
        # 
        # This parameter is required.
        self.status = status
        # The list of system rule switch identifiers whose status is to be updated. The elements are obtained from the SwitchId returned by ListSystemConfigRules. A maximum of 100 items are supported. The backend updates the items one by one based on the list. The request is rejected if the list is not provided.
        self.switch_id_list = switch_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_id_list is not None:
            result['SwitchIdList'] = self.switch_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchIdList') is not None:
            self.switch_id_list = m.get('SwitchIdList')

        return self

