# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitASRJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        duration: str = None,
        editing_config: str = None,
        input_file: str = None,
        start_time: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The job description, which can up to 128 bytes in length.
        self.description = description
        # The speech duration.
        self.duration = duration
        self.editing_config = editing_config
        # The input file. You can specify an Object Storage Service (OSS) URL or the ID of a media asset in the media asset library.
        self.input_file = input_file
        # The start time of the speech to recognize.
        self.start_time = start_time
        # The job title, which can be up to 128 bytes in length.
        self.title = title
        # The user-defined data in the JSON format. You can specify your business information, such as the business environment and job information.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.input_file is not None:
            result['InputFile'] = self.input_file

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('InputFile') is not None:
            self.input_file = m.get('InputFile')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

