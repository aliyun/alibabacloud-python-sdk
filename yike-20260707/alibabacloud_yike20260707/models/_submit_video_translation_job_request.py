# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoTranslationJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        input: str = None,
        job_parameters: str = None,
        job_type: str = None,
        output: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The user-level idempotency key.
        self.client_token = client_token
        # The job description.
        self.description = description
        # The input configuration JSON string:
        # - Video
        # - Audio
        # - Subtitle
        # 
        # <notice>Currently, only OSS addresses under the calling account are supported as input.</notice>
        # 
        # This parameter is required.
        self.input = input
        # The job parameters JSON string.
        # 
        # This parameter is required.
        self.job_parameters = job_parameters
        # The job type. Valid values:
        # - SubtitleTranslate
        # - VoiceTranslate
        # 
        # This parameter is required.
        self.job_type = job_type
        # The output configuration JSON string.
        # 
        # This parameter is required.
        self.output = output
        # If not specified, the service generates a default title.
        self.title = title
        # The custom user data JSON string.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.input is not None:
            result['Input'] = self.input

        if self.job_parameters is not None:
            result['JobParameters'] = self.job_parameters

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.output is not None:
            result['Output'] = self.output

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobParameters') is not None:
            self.job_parameters = m.get('JobParameters')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

