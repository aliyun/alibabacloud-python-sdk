# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LlmSmartCallEncryptShrinkRequest(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        caller_number: str = None,
        encrypt_called_number: str = None,
        out_id: str = None,
        owner_id: int = None,
        prompt_param_shrink: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_word_param_shrink: str = None,
    ):
        # This parameter is required.
        self.application_code = application_code
        # This parameter is required.
        self.caller_number = caller_number
        # This parameter is required.
        self.encrypt_called_number = encrypt_called_number
        self.out_id = out_id
        self.owner_id = owner_id
        self.prompt_param_shrink = prompt_param_shrink
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_word_param_shrink = start_word_param_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.encrypt_called_number is not None:
            result['EncryptCalledNumber'] = self.encrypt_called_number

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prompt_param_shrink is not None:
            result['PromptParam'] = self.prompt_param_shrink

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_word_param_shrink is not None:
            result['StartWordParam'] = self.start_word_param_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('EncryptCalledNumber') is not None:
            self.encrypt_called_number = m.get('EncryptCalledNumber')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PromptParam') is not None:
            self.prompt_param_shrink = m.get('PromptParam')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartWordParam') is not None:
            self.start_word_param_shrink = m.get('StartWordParam')

        return self

