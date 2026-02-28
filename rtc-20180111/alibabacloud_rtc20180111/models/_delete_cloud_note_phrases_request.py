# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DeleteCloudNotePhrasesRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        phrase: main_models.DeleteCloudNotePhrasesRequestPhrase = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.phrase = phrase

    def validate(self):
        if self.phrase:
            self.phrase.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.phrase is not None:
            result['Phrase'] = self.phrase.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Phrase') is not None:
            temp_model = main_models.DeleteCloudNotePhrasesRequestPhrase()
            self.phrase = temp_model.from_map(m.get('Phrase'))

        return self

class DeleteCloudNotePhrasesRequestPhrase(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

