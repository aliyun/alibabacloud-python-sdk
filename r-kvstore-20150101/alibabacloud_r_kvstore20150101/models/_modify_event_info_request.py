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
        # The parameters related to the action in JSON format.
        # When **TaskAction** is set to **modifySwitchTime**, set this parameter to `{"recoverMode": "xxx", "recoverTime": "xxx"}`.
        # * **recoverMode**: the task recovery mode. Valid values:
        #   * **imePoint**: executes the task at a specified point in time.
        #   * **immediate**: executes the task immediately.
        #   * **maintainTime**: executes the task during the O&M window.
        # * **recoverTime**: the specified point in time in UTC. The format is yyyy-MM-ddTHH:mm:ssZ. This parameter is required when **recoverMode** is set to **timePoint**.
        self.action_params = action_params
        # The action to process the event. Valid values:
        # - **archive**: Archives the event.
        # - **undo**: Does not process the event.
        self.event_action = event_action
        # The event IDs. Separate multiple IDs with commas. A maximum of 20 IDs are supported.
        # 
        # This parameter is required.
        self.event_id = event_id
        # The region ID.
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

