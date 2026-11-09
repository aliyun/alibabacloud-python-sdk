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
        # The user-level idempotency token, which can be up to 40 characters in length. If the same user submits the request repeatedly with the same token, the original task is returned.
        self.client_token = client_token
        # The job description, which is used to record the business purpose or processing requirements.
        self.description = description
        # The input configuration JSON string. You must specify either Video or VideoMediaId, but not both. You can specify at most one of Audio and AudioMediaId. Subtitle is optional.
        # 
        # This parameter is required.
        self.input = input
        # The job parameters JSON string. It must include at least SourceLanguage and TargetLanguage. You can also configure primary subtitle erasure, voice translation, on-screen text translation, and final editing.
        # 
        # This parameter is required.
        self.job_parameters = job_parameters
        # The job type. SubtitleTranslate indicates subtitle translation, and VoiceTranslate indicates voice translation.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The output configuration JSON string. OssUri is the optional customer OSS output directory. If OssUri is not specified, a signed URL for the service-owned output is returned.
        self.output = output
        # The job title. If not specified, the service generates a default title.
        self.title = title
        # The user-defined data JSON string. When specifying an MNS queue to receive asynchronous notifications, set `NotifyAddress` to the pure queue name starting with `yike-callback-` instead of the full queue URL. You can optionally set `NotifyMnsEndpoint` to the MNS endpoint of the task account.
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

