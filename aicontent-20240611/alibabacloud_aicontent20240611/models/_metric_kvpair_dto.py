# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetricKVPairDTO(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: float = None,
    ):
        # Metric Name.  
        # 
        # **Chat**  
        # - `total_calls`: Number Of Calls, integer, Count  
        # - `input_tokens`: Total input tokens, integer  
        # - `output_tokens`: Total output tokens, integer  
        # - `reasoning_tokens`: Reasoning tokens, integer  
        # - `cached_tokens`: Cached input tokens (hit), integer  
        # 
        # **Vision**  
        # - `total_calls`: Number Of Calls, integer, Count  
        # - `image_count`: Number of generated images, integer  
        # - `video_duration`: Generated video duration, rounded to 3 decimal places, seconds  
        # 
        # **Embedding**  
        # - `total_calls`: Number Of Calls, integer, Count  
        # - `embedding_output_tokens`: Embedding output tokens, integer  
        # - `billing_tokens`: Total billing tokens, integer  
        # - `image_tokens`: Image tokens (multimodal embedding), integer  
        # 
        # **Omni-modal (ChatFullmodal / ChatMultimodal)**  
        # - `total_calls`: Number Of Calls, integer, Count  
        # - `input_text_tokens`: Input text tokens, integer  
        # - `input_audio_tokens`: Input audio tokens, integer  
        # - `input_image_tokens`: Input image tokens, integer  
        # - `input_video_tokens`: Input video tokens, integer  
        # - `output_text_tokens`: Output text tokens, integer  
        # - `output_audio_tokens`: Output audio tokens, integer  
        # 
        # **Speech (TTS / ASR)**  
        # - `total_calls`: Number Of Calls, integer, Count  
        # - `characters`: Characters converted to speech, integer  
        # - `asr_duration`: Speech recognition duration, rounded to 3 decimal places, seconds
        self.key = key
        # Metric value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

