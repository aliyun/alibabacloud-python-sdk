# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunEnterpriseVocAnalysisShrinkRequest(DaraModel):
    def __init__(
        self,
        ak_proxy: str = None,
        api_key: str = None,
        content: str = None,
        extra_info: str = None,
        filter_tags_shrink: str = None,
        model_id: str = None,
        output_format: str = None,
        source_trace: bool = None,
        tags_shrink: str = None,
        task_description: str = None,
    ):
        self.ak_proxy = ak_proxy
        self.api_key = api_key
        # 需要进行VOC分析的文本内容（content、contents、url、fileKey 四选一。优先级从小到大）
        self.content = content
        self.extra_info = extra_info
        # 过滤标签，用于筛选符合条件的内容。
        self.filter_tags_shrink = filter_tags_shrink
        self.model_id = model_id
        # 指定返回结果的格式，支持json或text
        self.output_format = output_format
        self.source_trace = source_trace
        # 业务标签体系，用于对文本内容进行分类和分析。
        self.tags_shrink = tags_shrink
        self.task_description = task_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak_proxy is not None:
            result['akProxy'] = self.ak_proxy

        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.content is not None:
            result['content'] = self.content

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('akProxy') is not None:
            self.ak_proxy = m.get('akProxy')

        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

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

        return self

