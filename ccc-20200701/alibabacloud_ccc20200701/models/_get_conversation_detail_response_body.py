# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetConversationDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        phrases: List[main_models.GetConversationDetailResponseBodyPhrases] = None,
        request_id: str = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.phrases = phrases
        self.request_id = request_id

    def validate(self):
        if self.phrases:
            for v1 in self.phrases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        result['Phrases'] = []
        if self.phrases is not None:
            for k1 in self.phrases:
                result['Phrases'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.phrases = []
        if m.get('Phrases') is not None:
            for k1 in m.get('Phrases'):
                temp_model = main_models.GetConversationDetailResponseBodyPhrases()
                self.phrases.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConversationDetailResponseBodyPhrases(DaraModel):
    def __init__(
        self,
        begin: int = None,
        end: int = None,
        finished: bool = None,
        identity: str = None,
        role: str = None,
        words: str = None,
    ):
        self.begin = begin
        self.end = end
        self.finished = finished
        self.identity = identity
        self.role = role
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.end is not None:
            result['End'] = self.end

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.identity is not None:
            result['Identity'] = self.identity

        if self.role is not None:
            result['Role'] = self.role

        if self.words is not None:
            result['Words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Words') is not None:
            self.words = m.get('Words')

        return self

