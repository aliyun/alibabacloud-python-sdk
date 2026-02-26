# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Message(DaraModel):
    def __init__(
        self,
        assistant_type: str = None,
        content: str = None,
        create_time: str = None,
        dataset_name: str = None,
        language: str = None,
        regenerate: bool = None,
        reply: str = None,
        score: float = None,
        source_uri: str = None,
        suggestion: str = None,
        tone: str = None,
        topic: str = None,
    ):
        # Assistant type.
        self.assistant_type = assistant_type
        # The content of the question.
        self.content = content
        # The time when the message was created.
        self.create_time = create_time
        # The dataset that the answer references to.
        self.dataset_name = dataset_name
        # The language of the answer.
        self.language = language
        # Indicates whether the message is a regenerated answer.
        self.regenerate = regenerate
        # The answer.
        self.reply = reply
        # Rate
        self.score = score
        # The URI of the source file from which the answer was generated.
        self.source_uri = source_uri
        # The compliance check results. Valid values: pass block
        self.suggestion = suggestion
        # The tone of the answer.
        self.tone = tone
        # The topic in the question.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assistant_type is not None:
            result['AssistantType'] = self.assistant_type

        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.language is not None:
            result['Language'] = self.language

        if self.regenerate is not None:
            result['Regenerate'] = self.regenerate

        if self.reply is not None:
            result['Reply'] = self.reply

        if self.score is not None:
            result['Score'] = self.score

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        if self.tone is not None:
            result['Tone'] = self.tone

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssistantType') is not None:
            self.assistant_type = m.get('AssistantType')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Regenerate') is not None:
            self.regenerate = m.get('Regenerate')

        if m.get('Reply') is not None:
            self.reply = m.get('Reply')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        if m.get('Tone') is not None:
            self.tone = m.get('Tone')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

