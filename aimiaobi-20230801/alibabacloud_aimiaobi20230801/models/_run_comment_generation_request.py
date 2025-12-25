# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class RunCommentGenerationRequest(DaraModel):
    def __init__(
        self,
        allow_emoji: bool = None,
        extra_info: str = None,
        length: str = None,
        length_range: Dict[str, Any] = None,
        model_id: str = None,
        num_comments: str = None,
        sentiment: Dict[str, Any] = None,
        session_id: str = None,
        source_material: str = None,
        style: str = None,
        type: Dict[str, Any] = None,
        workspace_id: str = None,
    ):
        self.allow_emoji = allow_emoji
        self.extra_info = extra_info
        self.length = length
        # This parameter is required.
        self.length_range = length_range
        self.model_id = model_id
        # This parameter is required.
        self.num_comments = num_comments
        # This parameter is required.
        self.sentiment = sentiment
        self.session_id = session_id
        # This parameter is required.
        self.source_material = source_material
        self.style = style
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_emoji is not None:
            result['AllowEmoji'] = self.allow_emoji

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.length is not None:
            result['Length'] = self.length

        if self.length_range is not None:
            result['LengthRange'] = self.length_range

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.num_comments is not None:
            result['NumComments'] = self.num_comments

        if self.sentiment is not None:
            result['Sentiment'] = self.sentiment

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.source_material is not None:
            result['SourceMaterial'] = self.source_material

        if self.style is not None:
            result['Style'] = self.style

        if self.type is not None:
            result['Type'] = self.type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowEmoji') is not None:
            self.allow_emoji = m.get('AllowEmoji')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('LengthRange') is not None:
            self.length_range = m.get('LengthRange')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('NumComments') is not None:
            self.num_comments = m.get('NumComments')

        if m.get('Sentiment') is not None:
            self.sentiment = m.get('Sentiment')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SourceMaterial') is not None:
            self.source_material = m.get('SourceMaterial')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

