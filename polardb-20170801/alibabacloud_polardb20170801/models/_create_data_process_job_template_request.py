# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataProcessJobTemplateRequest(DaraModel):
    def __init__(
        self,
        captioning: bool = None,
        captioning_prompt: str = None,
        embedding: bool = None,
        embedding_dimension: int = None,
        region_id: str = None,
        template_config: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # Specifies whether to fetch the image summary or video synopsis. When Settings is true, CaptioningPrompt must be provided.
        self.captioning = captioning
        # The prompt used for extracting captions. This parameter takes effect only when Captioning is set to true.
        self.captioning_prompt = captioning_prompt
        # Specifies whether to convert the content into vectors.
        self.embedding = embedding
        # The output dimension of the vector. Valid values when Embedding is set to true: 512, 768, 1024, and 2048.
        self.embedding_dimension = embedding_dimension
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The JSON string for additional template configurations.
        # 
        # This parameter is required.
        self.template_config = template_config
        # The name of the task template.
        self.template_name = template_name
        # The templatetype of the node template. Valid value: image.
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.captioning is not None:
            result['Captioning'] = self.captioning

        if self.captioning_prompt is not None:
            result['CaptioningPrompt'] = self.captioning_prompt

        if self.embedding is not None:
            result['Embedding'] = self.embedding

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Captioning') is not None:
            self.captioning = m.get('Captioning')

        if m.get('CaptioningPrompt') is not None:
            self.captioning_prompt = m.get('CaptioningPrompt')

        if m.get('Embedding') is not None:
            self.embedding = m.get('Embedding')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

