# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunDocWashingRequest(DaraModel):
    def __init__(
        self,
        model_id: str = None,
        prompt: str = None,
        reference_content: str = None,
        session_id: str = None,
        topic: str = None,
        word_number: int = None,
        workspace_id: str = None,
        writing_type_name: str = None,
        writing_type_ref_doc: str = None,
    ):
        self.model_id = model_id
        self.prompt = prompt
        # This parameter is required.
        self.reference_content = reference_content
        self.session_id = session_id
        self.topic = topic
        self.word_number = word_number
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_type_name = writing_type_name
        self.writing_type_ref_doc = writing_type_ref_doc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.reference_content is not None:
            result['ReferenceContent'] = self.reference_content

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.word_number is not None:
            result['WordNumber'] = self.word_number

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.writing_type_name is not None:
            result['WritingTypeName'] = self.writing_type_name

        if self.writing_type_ref_doc is not None:
            result['WritingTypeRefDoc'] = self.writing_type_ref_doc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ReferenceContent') is not None:
            self.reference_content = m.get('ReferenceContent')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('WordNumber') is not None:
            self.word_number = m.get('WordNumber')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WritingTypeName') is not None:
            self.writing_type_name = m.get('WritingTypeName')

        if m.get('WritingTypeRefDoc') is not None:
            self.writing_type_ref_doc = m.get('WritingTypeRefDoc')

        return self

