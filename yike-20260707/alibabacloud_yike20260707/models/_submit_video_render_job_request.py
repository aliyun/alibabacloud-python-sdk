# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoRenderJobRequest(DaraModel):
    def __init__(
        self,
        script: str = None,
        settings: str = None,
        user_data: str = None,
    ):
        # The complete creative script (JSON string) after user confirmation or editing. The structure aligns with the JSON content in the `Result` file returned by the `GetRemakeScriptJob` API.
        self.script = script
        # The rendering settings (JSON string).
        # 
        # - **Resolution** (String, required): The resolution. Valid values: `720P`, `1080P`.
        #   - **AspectRatio** (String, optional): The video aspect ratio. Valid values: `9:16`, `16:9`, `1:1`. Default value: `9:16`.
        #   - **VoiceoverLanguage** (String, optional): The voiceover language. Valid values: `zh` (Chinese), `en` (English), `es` (Spanish), `pt` (Portuguese), `fr` (French), `de` (German), `ja` (Japanese), `ko` (Korean), `ar` (Arabic). Default value: `zh`.
        #   - **WithSubtitles** (Bool, optional): Specifies whether to generate subtitles. Default value: `true`.
        #   - **TTS** (Object, optional): The TTS configuration. If not specified, the default voice is used. This parameter applies only to single-person scenarios with voiceover only.
        # 
        #     - **VoiceUrl** (String, optional): The URL of the voice file. The URL must be an HTTP or HTTPS address. If specified, the voiceover for the entire video uses this voice.
        # 
        #   - **Bgm** (String, optional): The URL or 32-character media asset ID of the background music.
        self.settings = settings
        # The custom user parameter in JSON format.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.script is not None:
            result['Script'] = self.script

        if self.settings is not None:
            result['Settings'] = self.settings

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('Settings') is not None:
            self.settings = m.get('Settings')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

