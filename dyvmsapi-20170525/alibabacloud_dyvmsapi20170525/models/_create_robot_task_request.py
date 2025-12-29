# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRobotTaskRequest(DaraModel):
    def __init__(
        self,
        caller: str = None,
        corp_name: str = None,
        dialog_id: int = None,
        is_self_line: bool = None,
        number_status_ident: bool = None,
        owner_id: int = None,
        recall_interval: int = None,
        recall_state_codes: str = None,
        recall_times: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retry_type: int = None,
        task_name: str = None,
    ):
        # The calling number.
        # 
        # You must use the phone numbers that you have purchased and separate multiple numbers with commas (,). You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Real Number Service** > **Real Number Management** to view the numbers you purchased.
        # 
        # This parameter is required.
        self.caller = caller
        # The company name, which must be the same as the **enterprise name** on the qualification management page.
        self.corp_name = corp_name
        # The ID of the robot or communication script that is used to initiate the call.
        # 
        # You can log on to the [Voice Messaging Service console](https://dyvms.console.aliyun.com/overview/home) and choose **Intelligent Voice Robot** > **Communication Script Management** to view the communication script ID.
        # 
        # This parameter is required.
        self.dialog_id = dialog_id
        # Specifies whether to call the self-managed line. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        # 
        # > If you set this parameter to **true**, calling numbers are not verified.
        self.is_self_line = is_self_line
        # Specifies whether to enable number status identification. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        # 
        # > If you set this parameter to **true**, the reason why a call is not answered is recorded.
        # 
        # This parameter is required.
        self.number_status_ident = number_status_ident
        self.owner_id = owner_id
        # The redial interval. Unit: minutes. The value must be greater than 1.
        # 
        # > The maximum redial interval is 30 minutes.
        self.recall_interval = recall_interval
        # The call state in which redial is required. Separate multiple call states with commas (,). Valid values:
        # 
        # *   **200010**: The phone of the called party is powered off.
        # *   **200011**: The number of the called party is out of service.
        # *   **200002**: The line is busy.
        # *   **200012**: The call is lost.
        # *   **200005**: The called party cannot be connected.
        # *   **200003**: The called party does not respond to the call.
        self.recall_state_codes = recall_state_codes
        # The number of redial times.
        self.recall_times = recall_times
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to enable auto-redial. Valid values:
        # 
        # *   **1**: enables auto-redial.
        # *   **0**: disables auto-redial.
        # 
        # This parameter is required.
        self.retry_type = retry_type
        # The task name. The task name can be up to 30 characters in length.
        # 
        # This parameter is required.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller is not None:
            result['Caller'] = self.caller

        if self.corp_name is not None:
            result['CorpName'] = self.corp_name

        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id

        if self.is_self_line is not None:
            result['IsSelfLine'] = self.is_self_line

        if self.number_status_ident is not None:
            result['NumberStatusIdent'] = self.number_status_ident

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.recall_interval is not None:
            result['RecallInterval'] = self.recall_interval

        if self.recall_state_codes is not None:
            result['RecallStateCodes'] = self.recall_state_codes

        if self.recall_times is not None:
            result['RecallTimes'] = self.recall_times

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retry_type is not None:
            result['RetryType'] = self.retry_type

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')

        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')

        if m.get('IsSelfLine') is not None:
            self.is_self_line = m.get('IsSelfLine')

        if m.get('NumberStatusIdent') is not None:
            self.number_status_ident = m.get('NumberStatusIdent')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RecallInterval') is not None:
            self.recall_interval = m.get('RecallInterval')

        if m.get('RecallStateCodes') is not None:
            self.recall_state_codes = m.get('RecallStateCodes')

        if m.get('RecallTimes') is not None:
            self.recall_times = m.get('RecallTimes')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetryType') is not None:
            self.retry_type = m.get('RetryType')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

