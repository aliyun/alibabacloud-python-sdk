# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCallOutboundInstantRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        caller_number: str = None,
        caller_uac_account_id: str = None,
        current_workspace_id: str = None,
        customer_line_code: str = None,
        customer_name: str = None,
        encrypt_call: bool = None,
        prompt_variables: str = None,
        task_id: int = None,
    ):
        self.called_number = called_number
        self.caller_number = caller_number
        self.caller_uac_account_id = caller_uac_account_id
        self.current_workspace_id = current_workspace_id
        self.customer_line_code = customer_line_code
        self.customer_name = customer_name
        self.encrypt_call = encrypt_call
        self.prompt_variables = prompt_variables
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.caller_uac_account_id is not None:
            result['CallerUacAccountId'] = self.caller_uac_account_id

        if self.current_workspace_id is not None:
            result['CurrentWorkspaceId'] = self.current_workspace_id

        if self.customer_line_code is not None:
            result['CustomerLineCode'] = self.customer_line_code

        if self.customer_name is not None:
            result['CustomerName'] = self.customer_name

        if self.encrypt_call is not None:
            result['EncryptCall'] = self.encrypt_call

        if self.prompt_variables is not None:
            result['PromptVariables'] = self.prompt_variables

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('CallerUacAccountId') is not None:
            self.caller_uac_account_id = m.get('CallerUacAccountId')

        if m.get('CurrentWorkspaceId') is not None:
            self.current_workspace_id = m.get('CurrentWorkspaceId')

        if m.get('CustomerLineCode') is not None:
            self.customer_line_code = m.get('CustomerLineCode')

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('EncryptCall') is not None:
            self.encrypt_call = m.get('EncryptCall')

        if m.get('PromptVariables') is not None:
            self.prompt_variables = m.get('PromptVariables')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

