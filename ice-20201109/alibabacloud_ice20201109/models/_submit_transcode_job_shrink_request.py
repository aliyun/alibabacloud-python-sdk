# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitTranscodeJobShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        input_group_shrink: str = None,
        name: str = None,
        output_group_shrink: str = None,
        schedule_config_shrink: str = None,
        user_data: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The input group of the job. An input of a single file indicates a transcoding job. An input of multiple files indicates an audio and video stream merge job.
        # 
        # This parameter is required.
        self.input_group_shrink = input_group_shrink
        # The job name.
        self.name = name
        # The output group of the job.
        # 
        # This parameter is required.
        self.output_group_shrink = output_group_shrink
        # The scheduling information about the job.
        self.schedule_config_shrink = schedule_config_shrink
        # The custom settings. The value must be in the JSON format and can be up to 512 bytes in length. You can specify a [custom callback URL](https://help.aliyun.com/document_detail/451631.html).
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

        if self.input_group_shrink is not None:
            result['InputGroup'] = self.input_group_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.output_group_shrink is not None:
            result['OutputGroup'] = self.output_group_shrink

        if self.schedule_config_shrink is not None:
            result['ScheduleConfig'] = self.schedule_config_shrink

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InputGroup') is not None:
            self.input_group_shrink = m.get('InputGroup')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputGroup') is not None:
            self.output_group_shrink = m.get('OutputGroup')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config_shrink = m.get('ScheduleConfig')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

