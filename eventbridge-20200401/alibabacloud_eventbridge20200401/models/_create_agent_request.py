# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateAgentRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        metadata: main_models.CreateAgentRequestMetadata = None,
        name: str = None,
        prompt: str = None,
    ):
        self.description = description
        self.metadata = metadata
        self.name = name
        self.prompt = prompt

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Metadata') is not None:
            temp_model = main_models.CreateAgentRequestMetadata()
            self.metadata = temp_model.from_map(m.get('Metadata'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        return self

class CreateAgentRequestMetadata(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.CreateAgentRequestMetadataAttachments] = None,
    ):
        self.attachments = attachments

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['Attachments'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k1 in m.get('Attachments'):
                temp_model = main_models.CreateAgentRequestMetadataAttachments()
                self.attachments.append(temp_model.from_map(k1))

        return self

class CreateAgentRequestMetadataAttachments(DaraModel):
    def __init__(
        self,
        arn: str = None,
        mime_type: str = None,
    ):
        self.arn = arn
        self.mime_type = mime_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.mime_type is not None:
            result['MimeType'] = self.mime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')

        return self

