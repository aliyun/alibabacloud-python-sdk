# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyEventInfoRequest(DaraModel):
    def __init__(
        self,
        action_params: str = None,
        event_action: str = None,
        event_id: str = None,
        region_id: str = None,
        security_token: str = None,
    ):
        # The action-related parameters. You can add action-related parameters based on your business requirements. The parameter value varies with the value of the TaskAction parameter.
        self.action_params = action_params
        # The event handling action. Valid values:
        # 
        # *   **archive**
        # *   **undo**
        # 
        # >  This parameter is required.
        self.event_action = event_action
        # The event ID. You can call the DescribeEvents operation to obtain the IDs of the events. Separate multiple event IDs with commas (,). You can specify up to 20 event IDs.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/610399.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_params is not None:
            result['ActionParams'] = self.action_params

        if self.event_action is not None:
            result['EventAction'] = self.event_action

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')

        if m.get('EventAction') is not None:
            self.event_action = m.get('EventAction')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

