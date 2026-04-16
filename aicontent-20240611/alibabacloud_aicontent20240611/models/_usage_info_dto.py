# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UsageInfoDTO(DaraModel):
    def __init__(
        self,
        completion_tokens: int = None,
        image_count: int = None,
        prompt_tokens: int = None,
        total_tokens: int = None,
        video_count: int = None,
        video_duration: int = None,
    ):
        self.completion_tokens = completion_tokens
        self.image_count = image_count
        self.prompt_tokens = prompt_tokens
        self.total_tokens = total_tokens
        self.video_count = video_count
        self.video_duration = video_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_tokens is not None:
            result['completionTokens'] = self.completion_tokens

        if self.image_count is not None:
            result['imageCount'] = self.image_count

        if self.prompt_tokens is not None:
            result['promptTokens'] = self.prompt_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        if self.video_count is not None:
            result['videoCount'] = self.video_count

        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTokens') is not None:
            self.completion_tokens = m.get('completionTokens')

        if m.get('imageCount') is not None:
            self.image_count = m.get('imageCount')

        if m.get('promptTokens') is not None:
            self.prompt_tokens = m.get('promptTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        if m.get('videoCount') is not None:
            self.video_count = m.get('videoCount')

        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')

        return self

