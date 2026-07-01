# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAvatarVideoJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        editing_config: str = None,
        input_config: str = None,
        output_config: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The description of the job. The description can be up to 128 bytes in length.
        self.description = description
        # The configurations for the avatar job, such as the avatar ID, voice, and speech rate.
        self.editing_config = editing_config
        # Input can be text, an audio file from Object Storage Service (OSS), or a [media asset](). Only MP3 and WAV audio formats are supported.>Notice:  The value of the `Text` parameter must contain at least five characters.
        self.input_config = input_config
        # Specifies the output configuration, including the destination URL for the rendered video.
        self.output_config = output_config
        # The title of the job. The title can be up to 128 bytes in length.
        self.title = title
        # A user-defined JSON string for passing custom business information, such as environment details or job metadata.
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

        if self.editing_config is not None:
            result['EditingConfig'] = self.editing_config

        if self.input_config is not None:
            result['InputConfig'] = self.input_config

        if self.output_config is not None:
            result['OutputConfig'] = self.output_config

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EditingConfig') is not None:
            self.editing_config = m.get('EditingConfig')

        if m.get('InputConfig') is not None:
            self.input_config = m.get('InputConfig')

        if m.get('OutputConfig') is not None:
            self.output_config = m.get('OutputConfig')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

