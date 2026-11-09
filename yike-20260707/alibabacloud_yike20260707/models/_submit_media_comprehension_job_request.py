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
        # The input material. It is a JSON string with the following structure:
        # 
        # - Medias (Array<Object>, required): The list of media assets. It contains 1 to 10 elements. Each element includes the following fields:
        #   - Type (String, required): The type of the media asset. Valid values: video and image. The value is not case-sensitive.
        #   - Url (String, mutually exclusive with MediaId): The URL of the media asset. It must start with http:// or https:// and be up to 2,048 characters in length. Unregistered URLs are automatically registered as media assets.
        #   - MediaId (String, mutually exclusive with Url): The ID of the registered media asset. If both Url and MediaId are specified, MediaId takes precedence.
        self.input = input
        # The analysis parameters. It is a JSON string with a maximum length of 65,536 characters and a maximum of 20 fields.
        self.job_params = job_params
        # The job type. Valid values:
        # 
        # - VideoBreakdown: viral video breakdown. The Medias array must contain exactly one element with Type set to video.
        # - ProductRecognition: product image information recognition. All elements in the Medias array must have Type set to image.
        self.job_type = job_type
        # The custom parameters. It is a JSON string that is returned as-is in the callback result, such as newsKey. NotifyAddress is a system-reserved field for the callback URL. A callback is triggered to this URL after the job is completed.
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

