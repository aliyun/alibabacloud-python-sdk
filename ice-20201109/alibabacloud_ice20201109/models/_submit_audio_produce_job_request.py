# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAudioProduceJobRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        editing_config: str = None,
        input_config: str = None,
        output_config: str = None,
        overwrite: bool = None,
        title: str = None,
        user_data: str = None,
    ):
        # The job description.
        # 
        # *   The job description can be up to 1,024 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.description = description
        # The audio editing configurations.
        # 
        # *   voice: the [voice type](https://help.aliyun.com/document_detail/449563.html).
        # *   customizedVoice: the ID of the personalized human voice.
        # *   format: the format of the output file. Valid values: PCM, WAV, and MP3.
        # *   volume: the volume. Default value: 50. Valid values: 0 to 100.
        # *   speech_rate: the speech tempo. Default value: 0. Value range: -500 to 500.
        # *   pitch_rate: the intonation. Default value: 0. Value range: -500 to 500.
        # 
        # >  If you specify both voice and customizedVoice, customizedVoice takes precedence over voice.
        # 
        # This parameter is required.
        self.editing_config = editing_config
        # The text content. A maximum of 2,000 characters are supported. The [Speech Synthesis Markup Language (SSML)](https://help.aliyun.com/document_detail/2672807.html) is supported.
        # 
        # This parameter is required.
        self.input_config = input_config
        # The output audio configurations.
        # 
        # This parameter is required.
        self.output_config = output_config
        # Specifies whether to overwrite the existing Object Storage Service (OSS) object.
        self.overwrite = overwrite
        # The job title. If you do not specify this parameter, the system generates a title based on the current date.
        # 
        # *   The job title can be up to 128 bytes in length.
        # *   The value must be encoded in UTF-8.
        self.title = title
        # The user-defined data in the JSON format, which can be up to 512 bytes in length. You can specify a custom callback URL. For more information, see [Configure a callback upon editing completion](https://help.aliyun.com/document_detail/451631.html).
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

        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite

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

        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

