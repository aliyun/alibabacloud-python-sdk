# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDataProcessJobTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeDataProcessJobTemplatesResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The list of data processing task templates.
        self.items = items
        # The current page number.
        self.page_number = page_number
        # The number of templates returned on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of templates that meet the specified conditions.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDataProcessJobTemplatesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDataProcessJobTemplatesResponseBodyItems(DaraModel):
    def __init__(
        self,
        captioning: bool = None,
        captioning_prompt: str = None,
        creation_time: str = None,
        embedding: bool = None,
        embedding_dimension: int = None,
        status: str = None,
        template_config: str = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # Specifies whether it is required to fetch the summary or video synopsis.
        self.captioning = captioning
        # The prompt used when extracting captions.
        self.captioning_prompt = captioning_prompt
        # The time when the task template was created, in RFC 3339 format.
        self.creation_time = creation_time
        # Specifies whether to convert content into vectors.
        self.embedding = embedding
        # The output dimension of the vector.
        self.embedding_dimension = embedding_dimension
        # The task template status.
        self.status = status
        # The JSON configuration string of the template.
        self.template_config = template_config
        # The task template ID.
        self.template_id = template_id
        # The task template name.
        self.template_name = template_name
        # The node templatetype. Valid value: image.
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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.embedding is not None:
            result['Embedding'] = self.embedding

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.status is not None:
            result['Status'] = self.status

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

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

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Embedding') is not None:
            self.embedding = m.get('Embedding')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

