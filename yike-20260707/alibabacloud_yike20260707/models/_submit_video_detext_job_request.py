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
        # The user-level idempotency token. The token can be up to 40 characters in length. If the same user submits the request repeatedly with the same token, the original task is returned.
        self.client_token = client_token
        # The input configuration JSON string. You must specify either VideoUrl or VideoMediaId, but not both.
        # 
        # This parameter is required.
        self.input = input
        # The text erasure parameters JSON string. TextTargets is used to detect and erase text. FullEraseTargets is used to inpaint entire regions. EraseAllText only controls text filtering and does not expand the region. For parameters, default behaviors, and combination examples, see the supplementary description of request parameters.
        self.job_parameters = job_parameters
        # The output configuration JSON string. You can use OssUri to specify an OSS directory or an MP4 file path. The path cannot contain query parameters or fragments. If a directory is specified, detext.mp4 is automatically appended. If the path ends with .mp4 and has no trailing slash, it is used directly as the destination file. If OssUri is not specified, a signed URL for the processing result is returned in the query result.
        self.output = output
        # The custom data JSON string used for pass-through in final state notifications. For Message Service (MNS) callbacks, use NotifyAddress to specify the queue name prefixed with yike-callback, and use NotifyMnsEndpoint to specify the MNS endpoint of the same account. For HTTP or HTTPS callbacks, use NotifyAddress to specify the complete URL.
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

