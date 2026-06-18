# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchAssignSeatsRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        account_ids_str: str = None,
        caller_uac_account_id: str = None,
        locale: str = None,
        namespace_id: str = None,
        seat_type: str = None,
        workspace_id: str = None,
    ):
        # The list of target member IDs.
        self.account_ids = account_ids
        # The AccountIds in string format.
        self.account_ids_str = account_ids_str
        # The account ID of the caller that identifies the initiator of this call.
        self.caller_uac_account_id = caller_uac_account_id
        # The language setting. Valid values: zh-CN and en-US.
        self.locale = locale
        # The product namespace ID. For the TokenPlan product, this field is fixed to namespace-1.
        self.namespace_id = namespace_id
        # The seat type. Valid values: standard, pro, and max.
        # 
        # This parameter is required.
        self.seat_type = seat_type
        # The ID of the target workspace.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.account_ids_str is not None:
            result['AccountIdsStr'] = self.account_ids_str

        if self.caller_uac_account_id is not None:
            result['CallerUacAccountId'] = self.caller_uac_account_id

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.seat_type is not None:
            result['SeatType'] = self.seat_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('AccountIdsStr') is not None:
            self.account_ids_str = m.get('AccountIdsStr')

        if m.get('CallerUacAccountId') is not None:
            self.caller_uac_account_id = m.get('CallerUacAccountId')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('SeatType') is not None:
            self.seat_type = m.get('SeatType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

