# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class EmbeddingTransformParameters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        embedding_data: main_models.EmbeddingTransformParametersEmbeddingData = None,
        embedding_model: str = None,
    ):
        self.api_key = api_key
        self.embedding_data = embedding_data
        self.embedding_model = embedding_model

    def validate(self):
        if self.embedding_data:
            self.embedding_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.embedding_data is not None:
            result['EmbeddingData'] = self.embedding_data.to_map()

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('EmbeddingData') is not None:
            temp_model = main_models.EmbeddingTransformParametersEmbeddingData()
            self.embedding_data = temp_model.from_map(m.get('EmbeddingData'))

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        return self

class EmbeddingTransformParametersEmbeddingData(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

