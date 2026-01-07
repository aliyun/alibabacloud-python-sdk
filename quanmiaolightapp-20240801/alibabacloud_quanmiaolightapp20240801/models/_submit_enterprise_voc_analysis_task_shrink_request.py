# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitEnterpriseVocAnalysisTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        contents_shrink: str = None,
        extra_info: str = None,
        file_key: str = None,
        filter_tags_shrink: str = None,
        model_id: str = None,
        output_format: str = None,
        source_trace: bool = None,
        tags_shrink: str = None,
        task_description: str = None,
        url: str = None,
    ):
        self.api_key = api_key
        self.contents_shrink = contents_shrink
        self.extra_info = extra_info
        self.file_key = file_key
        self.filter_tags_shrink = filter_tags_shrink
        self.model_id = model_id
        self.output_format = output_format
        self.source_trace = source_trace
        self.tags_shrink = tags_shrink
        self.task_description = task_description
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.contents_shrink is not None:
            result['contents'] = self.contents_shrink

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

        if self.file_key is not None:
            result['fileKey'] = self.file_key

        if self.filter_tags_shrink is not None:
            result['filterTags'] = self.filter_tags_shrink

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.output_format is not None:
            result['outputFormat'] = self.output_format

        if self.source_trace is not None:
            result['sourceTrace'] = self.source_trace

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        if self.task_description is not None:
            result['taskDescription'] = self.task_description

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('contents') is not None:
            self.contents_shrink = m.get('contents')

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

        if m.get('fileKey') is not None:
            self.file_key = m.get('fileKey')

        if m.get('filterTags') is not None:
            self.filter_tags_shrink = m.get('filterTags')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('outputFormat') is not None:
            self.output_format = m.get('outputFormat')

        if m.get('sourceTrace') is not None:
            self.source_trace = m.get('sourceTrace')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('taskDescription') is not None:
            self.task_description = m.get('taskDescription')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

