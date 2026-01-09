# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransferCallToSkillGroupRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        call_id: str = None,
        client_token: str = None,
        connection_id: str = None,
        hold_connection_id: str = None,
        instance_id: str = None,
        is_single_transfer: bool = None,
        job_id: str = None,
        skill_group_id: int = None,
        type: int = None,
    ):
        # This parameter is required.
        self.account_name = account_name
        self.call_id = call_id
        self.client_token = client_token
        self.connection_id = connection_id
        self.hold_connection_id = hold_connection_id
        # This parameter is required.
        self.instance_id = instance_id
        self.is_single_transfer = is_single_transfer
        self.job_id = job_id
        # This parameter is required.
        self.skill_group_id = skill_group_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.hold_connection_id is not None:
            result['HoldConnectionId'] = self.hold_connection_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_single_transfer is not None:
            result['IsSingleTransfer'] = self.is_single_transfer

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('HoldConnectionId') is not None:
            self.hold_connection_id = m.get('HoldConnectionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSingleTransfer') is not None:
            self.is_single_transfer = m.get('IsSingleTransfer')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

