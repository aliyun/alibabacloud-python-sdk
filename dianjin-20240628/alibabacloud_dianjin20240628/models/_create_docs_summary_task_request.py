# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class CreateDocsSummaryTaskRequest(DaraModel):
    def __init__(
        self,
        doc_infos: List[main_models.CreateDocsSummaryTaskRequestDocInfos] = None,
        enable_table: bool = None,
        instruction: str = None,
        model_id: str = None,
    ):
        # This parameter is required.
        self.doc_infos = doc_infos
        self.enable_table = enable_table
        self.instruction = instruction
        # This parameter is required.
        self.model_id = model_id

    def validate(self):
        if self.doc_infos:
            for v1 in self.doc_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['docInfos'] = []
        if self.doc_infos is not None:
            for k1 in self.doc_infos:
                result['docInfos'].append(k1.to_map() if k1 else None)

        if self.enable_table is not None:
            result['enableTable'] = self.enable_table

        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.model_id is not None:
            result['modelId'] = self.model_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_infos = []
        if m.get('docInfos') is not None:
            for k1 in m.get('docInfos'):
                temp_model = main_models.CreateDocsSummaryTaskRequestDocInfos()
                self.doc_infos.append(temp_model.from_map(k1))

        if m.get('enableTable') is not None:
            self.enable_table = m.get('enableTable')

        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        return self

class CreateDocsSummaryTaskRequestDocInfos(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        end_page: int = None,
        library_id: str = None,
        start_page: int = None,
    ):
        # This parameter is required.
        self.doc_id = doc_id
        self.end_page = end_page
        # This parameter is required.
        self.library_id = library_id
        self.start_page = start_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.end_page is not None:
            result['endPage'] = self.end_page

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.start_page is not None:
            result['startPage'] = self.start_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('endPage') is not None:
            self.end_page = m.get('endPage')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('startPage') is not None:
            self.start_page = m.get('startPage')

        return self

