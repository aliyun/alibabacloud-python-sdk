# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadRobotTaskCalledFileRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        id: int = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tts_param: str = None,
        tts_param_head: str = None,
    ):
        # The called numbers. Separate multiple called numbers with commas (,).
        # 
        # > After you create a robocall task, you must upload called numbers in batches. You can upload up to 300,000 called numbers for each task.
        # 
        # This parameter is required.
        self.called_number = called_number
        # The unique ID of the robocall task. You can call the [CreateRobotTask](~~CreateRobotTask~~) operation to obtain the ID of the robocall task.
        # 
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The values of the variable in the text-to-speech (TTS) template, in the JSON format. The variable values specified by the TtsParam parameter must match the variable names specified by the TtsParamHead parameter.
        # 
        # *   If all the called numbers carry the same variable values, you can set the value of the number field to **all** and upload only one copy of the variable values.
        # *   If only some of the called numbers carry the same variable values, you can set the value of the number field to **all** for these called numbers and set the value of the number field and variable values for other called numbers based on your business requirements. The system preferentially selects the values that you set for the called numbers.
        self.tts_param = tts_param
        # The list of variable names carried in the robocall task, in the JSON format. The TtsParamHead parameter must be used together with the TtsParam parameter.
        self.tts_param_head = tts_param_head

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param

        if self.tts_param_head is not None:
            result['TtsParamHead'] = self.tts_param_head

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')

        if m.get('TtsParamHead') is not None:
            self.tts_param_head = m.get('TtsParamHead')

        return self

