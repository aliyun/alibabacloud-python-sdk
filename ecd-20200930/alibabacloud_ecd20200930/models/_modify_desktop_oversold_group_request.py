# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDesktopOversoldGroupRequest(DaraModel):
    def __init__(
        self,
        concurrence_count: int = None,
        description: str = None,
        idle_disconnect_duration: int = None,
        image_id: str = None,
        keep_duration: int = None,
        name: str = None,
        oversold_group_id: str = None,
        oversold_user_count: int = None,
        oversold_warn: int = None,
        policy_group_id: str = None,
        stop_duration: int = None,
    ):
        self.concurrence_count = concurrence_count
        self.description = description
        self.idle_disconnect_duration = idle_disconnect_duration
        self.image_id = image_id
        self.keep_duration = keep_duration
        self.name = name
        self.oversold_group_id = oversold_group_id
        self.oversold_user_count = oversold_user_count
        self.oversold_warn = oversold_warn
        self.policy_group_id = policy_group_id
        self.stop_duration = stop_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrence_count is not None:
            result['ConcurrenceCount'] = self.concurrence_count

        if self.description is not None:
            result['Description'] = self.description

        if self.idle_disconnect_duration is not None:
            result['IdleDisconnectDuration'] = self.idle_disconnect_duration

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.keep_duration is not None:
            result['KeepDuration'] = self.keep_duration

        if self.name is not None:
            result['Name'] = self.name

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.oversold_user_count is not None:
            result['OversoldUserCount'] = self.oversold_user_count

        if self.oversold_warn is not None:
            result['OversoldWarn'] = self.oversold_warn

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.stop_duration is not None:
            result['StopDuration'] = self.stop_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrenceCount') is not None:
            self.concurrence_count = m.get('ConcurrenceCount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IdleDisconnectDuration') is not None:
            self.idle_disconnect_duration = m.get('IdleDisconnectDuration')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeepDuration') is not None:
            self.keep_duration = m.get('KeepDuration')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('OversoldUserCount') is not None:
            self.oversold_user_count = m.get('OversoldUserCount')

        if m.get('OversoldWarn') is not None:
            self.oversold_warn = m.get('OversoldWarn')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('StopDuration') is not None:
            self.stop_duration = m.get('StopDuration')

        return self

