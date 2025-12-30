# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFinReportSummaryTaskRequest(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        enable_table: bool = None,
        end_page: int = None,
        instruction: str = None,
        library_id: str = None,
        model_id: str = None,
        start_page: int = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        # This parameter is required.
        self.enable_table = enable_table
        self.end_page = end_page
        self.instruction = instruction
        # This parameter is required.
        self.library_id = library_id
        # This parameter is required.
        self.model_id = model_id
        self.start_page = start_page
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.enable_table is not None:
            result['enableTable'] = self.enable_table

        if self.end_page is not None:
            result['endPage'] = self.end_page

        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.start_page is not None:
            result['startPage'] = self.start_page

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('enableTable') is not None:
            self.enable_table = m.get('enableTable')

        if m.get('endPage') is not None:
            self.end_page = m.get('endPage')

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('startPage') is not None:
            self.start_page = m.get('startPage')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

