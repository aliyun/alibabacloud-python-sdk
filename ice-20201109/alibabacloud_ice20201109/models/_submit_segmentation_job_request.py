# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitSegmentationJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        input_config: str = None,
        job_params: str = None,
        output_config: str = None,
        user_data: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The input configuration. For detailed parameters, see [InputConfig](~~2874121#cc59ad3082jbx~~).
        self.input_config = input_config
        # The task parameters. For details, see [JobParams](~~2874121#a60357f2d5iix~~).
        self.job_params = job_params
        # The output configuration. For detailed parameters, see [OutputConfig](~~2874121#cef23186a8d6w~~).
        self.output_config = output_config
        # The user-defined data in the JSON format, which can be up to 512 bytes in length.
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

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

