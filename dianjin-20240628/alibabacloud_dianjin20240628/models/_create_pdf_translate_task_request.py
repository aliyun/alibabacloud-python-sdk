# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePdfTranslateTaskRequest(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        knowledge: str = None,
        library_id: str = None,
        model_id: str = None,
        translate_to: str = None,
    ):
        # Document ID
        # 
        # This parameter is required.
        self.doc_id = doc_id
        # Domain knowledge used as reference during translation
        self.knowledge = knowledge
        # Document library ID
        # 
        # This parameter is required.
        self.library_id = library_id
        # Model ID
        # 
        # This parameter is required.
        self.model_id = model_id
        # Target language. Default is Chinese
        self.translate_to = translate_to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.knowledge is not None:
            result['knowledge'] = self.knowledge

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.translate_to is not None:
            result['translateTo'] = self.translate_to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('knowledge') is not None:
            self.knowledge = m.get('knowledge')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('translateTo') is not None:
            self.translate_to = m.get('translateTo')

        return self

