# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class AsyncCreateClipsTimeLineRequest(DaraModel):
    def __init__(
        self,
        additional_content: str = None,
        custom_content: str = None,
        high_light_config: main_models.AsyncCreateClipsTimeLineRequestHighLightConfig = None,
        no_ref_video: bool = None,
        process_prompt: str = None,
        recommend_audio: bool = None,
        task_id: str = None,
        timeline_scene: int = None,
        workspace_id: str = None,
    ):
        self.additional_content = additional_content
        self.custom_content = custom_content
        self.high_light_config = high_light_config
        self.no_ref_video = no_ref_video
        self.process_prompt = process_prompt
        self.recommend_audio = recommend_audio
        # This parameter is required.
        self.task_id = task_id
        self.timeline_scene = timeline_scene
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.high_light_config:
            self.high_light_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_content is not None:
            result['AdditionalContent'] = self.additional_content

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.high_light_config is not None:
            result['HighLightConfig'] = self.high_light_config.to_map()

        if self.no_ref_video is not None:
            result['NoRefVideo'] = self.no_ref_video

        if self.process_prompt is not None:
            result['ProcessPrompt'] = self.process_prompt

        if self.recommend_audio is not None:
            result['RecommendAudio'] = self.recommend_audio

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.timeline_scene is not None:
            result['TimelineScene'] = self.timeline_scene

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalContent') is not None:
            self.additional_content = m.get('AdditionalContent')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('HighLightConfig') is not None:
            temp_model = main_models.AsyncCreateClipsTimeLineRequestHighLightConfig()
            self.high_light_config = temp_model.from_map(m.get('HighLightConfig'))

        if m.get('NoRefVideo') is not None:
            self.no_ref_video = m.get('NoRefVideo')

        if m.get('ProcessPrompt') is not None:
            self.process_prompt = m.get('ProcessPrompt')

        if m.get('RecommendAudio') is not None:
            self.recommend_audio = m.get('RecommendAudio')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TimelineScene') is not None:
            self.timeline_scene = m.get('TimelineScene')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class AsyncCreateClipsTimeLineRequestHighLightConfig(DaraModel):
    def __init__(
        self,
        ht_analyze_rhythm: bool = None,
        ht_high_quality_label: List[str] = None,
        ht_low_quality_label: List[str] = None,
        ht_max_time_length: int = None,
        ht_min_time_length: int = None,
        ht_prompt: str = None,
        ht_single_shot_len: int = None,
    ):
        self.ht_analyze_rhythm = ht_analyze_rhythm
        self.ht_high_quality_label = ht_high_quality_label
        self.ht_low_quality_label = ht_low_quality_label
        self.ht_max_time_length = ht_max_time_length
        self.ht_min_time_length = ht_min_time_length
        self.ht_prompt = ht_prompt
        self.ht_single_shot_len = ht_single_shot_len

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ht_analyze_rhythm is not None:
            result['HtAnalyzeRhythm'] = self.ht_analyze_rhythm

        if self.ht_high_quality_label is not None:
            result['HtHighQualityLabel'] = self.ht_high_quality_label

        if self.ht_low_quality_label is not None:
            result['HtLowQualityLabel'] = self.ht_low_quality_label

        if self.ht_max_time_length is not None:
            result['HtMaxTimeLength'] = self.ht_max_time_length

        if self.ht_min_time_length is not None:
            result['HtMinTimeLength'] = self.ht_min_time_length

        if self.ht_prompt is not None:
            result['HtPrompt'] = self.ht_prompt

        if self.ht_single_shot_len is not None:
            result['HtSingleShotLen'] = self.ht_single_shot_len

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HtAnalyzeRhythm') is not None:
            self.ht_analyze_rhythm = m.get('HtAnalyzeRhythm')

        if m.get('HtHighQualityLabel') is not None:
            self.ht_high_quality_label = m.get('HtHighQualityLabel')

        if m.get('HtLowQualityLabel') is not None:
            self.ht_low_quality_label = m.get('HtLowQualityLabel')

        if m.get('HtMaxTimeLength') is not None:
            self.ht_max_time_length = m.get('HtMaxTimeLength')

        if m.get('HtMinTimeLength') is not None:
            self.ht_min_time_length = m.get('HtMinTimeLength')

        if m.get('HtPrompt') is not None:
            self.ht_prompt = m.get('HtPrompt')

        if m.get('HtSingleShotLen') is not None:
            self.ht_single_shot_len = m.get('HtSingleShotLen')

        return self

