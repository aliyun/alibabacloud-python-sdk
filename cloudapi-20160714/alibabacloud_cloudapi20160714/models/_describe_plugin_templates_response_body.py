# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribePluginTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        templates: main_models.DescribePluginTemplatesResponseBodyTemplates = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The templates.
        self.templates = templates

    def validate(self):
        if self.templates:
            self.templates.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.templates is not None:
            result['Templates'] = self.templates.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Templates') is not None:
            temp_model = main_models.DescribePluginTemplatesResponseBodyTemplates()
            self.templates = temp_model.from_map(m.get('Templates'))

        return self

class DescribePluginTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        template: List[main_models.DescribePluginTemplatesResponseBodyTemplatesTemplate] = None,
    ):
        self.template = template

    def validate(self):
        if self.template:
            for v1 in self.template:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Template'] = []
        if self.template is not None:
            for k1 in self.template:
                result['Template'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template = []
        if m.get('Template') is not None:
            for k1 in m.get('Template'):
                temp_model = main_models.DescribePluginTemplatesResponseBodyTemplatesTemplate()
                self.template.append(temp_model.from_map(k1))

        return self

class DescribePluginTemplatesResponseBodyTemplatesTemplate(DaraModel):
    def __init__(
        self,
        description: str = None,
        document_anchor: str = None,
        document_id: str = None,
        sample: str = None,
        title: str = None,
    ):
        # The description.
        self.description = description
        # The document anchor point.
        self.document_anchor = document_anchor
        # The ID of the document.
        self.document_id = document_id
        # The sample.
        self.sample = sample
        # The title of the plug-in template title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.document_anchor is not None:
            result['DocumentAnchor'] = self.document_anchor

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentAnchor') is not None:
            self.document_anchor = m.get('DocumentAnchor')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

