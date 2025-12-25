# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunTitleGenerationShrinkRequest(DaraModel):
    def __init__(
        self,
        deduplicated_titles_shrink: str = None,
        reference_data_shrink: str = None,
        task_id: str = None,
        title_count: str = None,
        workspace_id: str = None,
    ):
        self.deduplicated_titles_shrink = deduplicated_titles_shrink
        # This parameter is required.
        self.reference_data_shrink = reference_data_shrink
        self.task_id = task_id
        self.title_count = title_count
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deduplicated_titles_shrink is not None:
            result['DeduplicatedTitles'] = self.deduplicated_titles_shrink

        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.title_count is not None:
            result['TitleCount'] = self.title_count

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeduplicatedTitles') is not None:
            self.deduplicated_titles_shrink = m.get('DeduplicatedTitles')

        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TitleCount') is not None:
            self.title_count = m.get('TitleCount')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

