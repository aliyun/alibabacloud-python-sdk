# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCallOutboundInstantRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        customer_name: str = None,
        encrypt_call: bool = None,
        prompt_variables: str = None,
        task_id: int = None,
    ):
        self.called_number = called_number
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

        if m.get('CustomerName') is not None:
            self.customer_name = m.get('CustomerName')

        if m.get('EncryptCall') is not None:
            self.encrypt_call = m.get('EncryptCall')

        if m.get('PromptVariables') is not None:
            self.prompt_variables = m.get('PromptVariables')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

