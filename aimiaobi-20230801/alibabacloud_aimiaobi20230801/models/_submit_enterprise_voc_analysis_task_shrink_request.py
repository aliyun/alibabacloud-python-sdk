# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitEnterpriseVocAnalysisTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        content_tags_shrink: str = None,
        contents_shrink: str = None,
        file_key: str = None,
        filter_tags_shrink: str = None,
        material_type: str = None,
        model_id: str = None,
        positive_sample: str = None,
        positive_sample_file_key: str = None,
        task_type: str = None,
        workspace_id: str = None,
    ):
        self.api_key = api_key
        # This parameter is required.
        self.content_tags_shrink = content_tags_shrink
        self.contents_shrink = contents_shrink
        self.file_key = file_key
        self.filter_tags_shrink = filter_tags_shrink
        self.material_type = material_type
        # This parameter is required.
        self.model_id = model_id
        self.positive_sample = positive_sample
        self.positive_sample_file_key = positive_sample_file_key
        self.task_type = task_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.content_tags_shrink is not None:
            result['ContentTags'] = self.content_tags_shrink

        if self.contents_shrink is not None:
            result['Contents'] = self.contents_shrink

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.filter_tags_shrink is not None:
            result['FilterTags'] = self.filter_tags_shrink

        if self.material_type is not None:
            result['MaterialType'] = self.material_type

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.positive_sample is not None:
            result['PositiveSample'] = self.positive_sample

        if self.positive_sample_file_key is not None:
            result['PositiveSampleFileKey'] = self.positive_sample_file_key

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ContentTags') is not None:
            self.content_tags_shrink = m.get('ContentTags')

        if m.get('Contents') is not None:
            self.contents_shrink = m.get('Contents')

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('FilterTags') is not None:
            self.filter_tags_shrink = m.get('FilterTags')

        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('PositiveSample') is not None:
            self.positive_sample = m.get('PositiveSample')

        if m.get('PositiveSampleFileKey') is not None:
            self.positive_sample_file_key = m.get('PositiveSampleFileKey')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

