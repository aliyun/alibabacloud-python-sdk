# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetMultiModalRerankerResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetMultiModalRerankerResponseBodyResult = None,
        usage: main_models.GetMultiModalRerankerResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latency is not None:
            result['latency'] = self.latency

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('result') is not None:
            temp_model = main_models.GetMultiModalRerankerResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetMultiModalRerankerResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetMultiModalRerankerResponseBodyUsage(DaraModel):
    def __init__(
        self,
        image_token: int = None,
        text_token: int = None,
    ):
        self.image_token = image_token
        self.text_token = text_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_token is not None:
            result['image_token'] = self.image_token

        if self.text_token is not None:
            result['text_token'] = self.text_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_token') is not None:
            self.image_token = m.get('image_token')

        if m.get('text_token') is not None:
            self.text_token = m.get('text_token')

        return self

class GetMultiModalRerankerResponseBodyResult(DaraModel):
    def __init__(
        self,
        scores: List[main_models.GetMultiModalRerankerResponseBodyResultScores] = None,
    ):
        self.scores = scores

    def validate(self):
        if self.scores:
            for v1 in self.scores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['scores'] = []
        if self.scores is not None:
            for k1 in self.scores:
                result['scores'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scores = []
        if m.get('scores') is not None:
            for k1 in m.get('scores'):
                temp_model = main_models.GetMultiModalRerankerResponseBodyResultScores()
                self.scores.append(temp_model.from_map(k1))

        return self

class GetMultiModalRerankerResponseBodyResultScores(DaraModel):
    def __init__(
        self,
        index: int = None,
        score: float = None,
    ):
        self.index = index
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index

        if self.score is not None:
            result['score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('score') is not None:
            self.score = m.get('score')

        return self

