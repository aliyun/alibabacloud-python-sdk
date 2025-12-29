# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRobotTaskCallListRequest(DaraModel):
    def __init__(
        self,
        call_result: str = None,
        called: str = None,
        dialog_count_from: str = None,
        dialog_count_to: str = None,
        duration_from: str = None,
        duration_to: str = None,
        hangup_direction: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        task_id: str = None,
    ):
        # The call result. Valid values:
        # 
        # *   **200002**: The line is busy.
        # *   **200005**: The called party cannot be connected.
        # *   **200010**: The phone of the called party is powered off.
        # *   **200011**: The called party is out of service.
        # *   **200012**: The call is lost.
        self.call_result = call_result
        # The called number.
        self.called = called
        # The minimum number of conversation rounds in the call.
        self.dialog_count_from = dialog_count_from
        # The maximum number of conversation rounds in the call.
        self.dialog_count_to = dialog_count_to
        # The minimum call duration.
        self.duration_from = duration_from
        # The maximum call duration.
        self.duration_to = duration_to
        # The party who hangs up. Valid values:
        # 
        # *   **0**: the called party.
        # *   **1**: the robot.
        self.hangup_direction = hangup_direction
        self.owner_id = owner_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The unique ID of the robocall task. You can call the [CreateRobotTask](https://help.aliyun.com/document_detail/393531.html) operation to obtain the task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_result is not None:
            result['CallResult'] = self.call_result

        if self.called is not None:
            result['Called'] = self.called

        if self.dialog_count_from is not None:
            result['DialogCountFrom'] = self.dialog_count_from

        if self.dialog_count_to is not None:
            result['DialogCountTo'] = self.dialog_count_to

        if self.duration_from is not None:
            result['DurationFrom'] = self.duration_from

        if self.duration_to is not None:
            result['DurationTo'] = self.duration_to

        if self.hangup_direction is not None:
            result['HangupDirection'] = self.hangup_direction

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')

        if m.get('Called') is not None:
            self.called = m.get('Called')

        if m.get('DialogCountFrom') is not None:
            self.dialog_count_from = m.get('DialogCountFrom')

        if m.get('DialogCountTo') is not None:
            self.dialog_count_to = m.get('DialogCountTo')

        if m.get('DurationFrom') is not None:
            self.duration_from = m.get('DurationFrom')

        if m.get('DurationTo') is not None:
            self.duration_to = m.get('DurationTo')

        if m.get('HangupDirection') is not None:
            self.hangup_direction = m.get('HangupDirection')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

