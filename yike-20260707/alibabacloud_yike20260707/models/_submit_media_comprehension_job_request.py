# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaComprehensionJobRequest(DaraModel):
    def __init__(
        self,
        input: str = None,
        job_params: str = None,
        job_type: str = None,
        user_data: str = None,
    ):
        # The input material. JSON string with the following structure:
        # 
        # - Medias (Array<Object>, required): The list of media assets. Contains 1 to 10 elements. Each element includes the following fields:
        #   - Type (String, required): The media asset type. Valid values: video or image (case-insensitive).
        #   - Url (String, either Url or MediaId is required): The URL of the media asset. The URL must start with http:// or https:// and cannot exceed 2048 characters in length. Unregistered URLs are automatically registered as media assets.
        #   - MediaId (String, either Url or MediaId is required): The ID of a registered media asset. If both Url and MediaId are specified, MediaId takes precedence.
        self.input = input
        # The analysis parameters. JSON string. The total length cannot exceed 65536 characters, and the total number of fields cannot exceed 20.
        self.job_params = job_params
        # The job type.
        # 
        # - VideoBreakdown: viral video breakdown. Requires Medias to contain exactly 1 element with Type=video.
        # - ProductRecognition: product image information recognition. Requires all elements in Medias to have Type=image.
        self.job_type = job_type
        # The custom parameters. JSON string that is returned as-is in the callback result (for example, newsKey). The system reserved field NotifyAddress specifies the callback URL. The callback is triggered after the job is completed.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.job_params is not None:
            result['JobParams'] = self.job_params

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('JobParams') is not None:
            self.job_params = m.get('JobParams')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

