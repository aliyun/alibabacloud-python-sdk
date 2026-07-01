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
        # The description of the job.
        # 
        # - Cannot exceed 1,024 bytes.
        # 
        # - Must be UTF-8 encoded.
        self.description = description
        # The audio production configuration:
        # 
        # - `voice`: The [voice type](https://help.aliyun.com/document_detail/449563.html).
        # 
        # - `customizedVoice`: The ID of the custom voice for voice cloning.
        # 
        # - `format`: The output file format. Supported formats: `PCM`, `WAV`, and `MP3`.
        # 
        # - `volume`: The volume. The value ranges from 0 to 100. Default: 50.
        # 
        # - `speech_rate`: The speech rate. The value ranges from -500 to 500. Default: 0.
        # 
        #   - Values of -500, 0, and 500 correspond to 0.5x, 1.0x, and 2.0x speed, respectively.
        # 
        #   - Calculation method:
        # 
        #     - For a 0.8x speed multiplier: (1 - 1/0.8) / 0.002 = -125.
        # 
        #     - For a 1.2x speed multiplier: (1 - 1/1.2) / 0.001 = 166.
        # 
        #     - For speed multipliers less than 1, use a factor of 0.002.
        # 
        #     - For speed multipliers greater than 1, use a factor of 0.001.
        # 
        # - `pitch_rate`: The pitch rate. The value ranges from -500 to 500. Default: 0.
        # 
        # 
        #   >Notice: 
        # 
        #   If you provide both `voice` and `customizedVoice`, `customizedVoice` takes precedence.
        # 
        # This parameter is required.
        self.editing_config = editing_config
        # The text to synthesize. The maximum length is 10,000 characters. Supports [SSML](https://help.aliyun.com/document_detail/2672807.html).
        # 
        # This parameter is required.
        self.input_config = input_config
        # The audio output configuration.
        # 
        # This parameter is required.
        self.output_config = output_config
        # Specifies whether to overwrite an existing OSS file.
        self.overwrite = overwrite
        # The title of the job. If you do not provide a title, the system automatically generates one based on the current date.
        # 
        # - Cannot exceed 128 bytes.
        # 
        # - Must be UTF-8 encoded.
        self.title = title
        # Custom settings in JSON format. The maximum length is 512 bytes. This parameter supports [custom callback address configuration](https://help.aliyun.com/document_detail/451631.html).
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

