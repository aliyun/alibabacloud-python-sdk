# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoDetextJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        input: str = None,
        job_parameters: str = None,
        output: str = None,
        user_data: str = None,
    ):
        # The user-level idempotency token. The token can be up to 40 characters in length. If the same user submits a request with the same token, the original task is returned.
        self.client_token = client_token
        # The input configuration JSON string. You must specify either VideoUrl or VideoMediaId, but not both.
        # 
        # This parameter is required.
        self.input = input
        # The text erasure parameter JSON string. This parameter can contain EraseAllText, TimeRanges, TextTargets, FullEraseTargets, and Config.
        self.job_parameters = job_parameters
        # The output configuration JSON string. You can use OssUri to specify the customer\\"s OSS bucket. If a directory is specified, the output file is named detext.mp4.
        self.output = output
        # The custom user data JSON string. This parameter can contain the asynchronous notification address NotifyAddress.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.input is not None:
            result['Input'] = self.input

        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters

        if self.output is not None:
            result['Output'] = self.output

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

