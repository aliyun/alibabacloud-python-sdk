# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class ListJobTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        job_templates: List[main_models.ListJobTemplatesResponseBodyJobTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The job templates.
        self.job_templates = job_templates
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of templates.
        self.total_count = total_count

    def validate(self):
        if self.job_templates:
            for v1 in self.job_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobTemplates'] = []
        if self.job_templates is not None:
            for k1 in self.job_templates:
                result['JobTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_templates = []
        if m.get('JobTemplates') is not None:
            for k1 in m.get('JobTemplates'):
                temp_model = main_models.ListJobTemplatesResponseBodyJobTemplates()
                self.job_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListJobTemplatesResponseBodyJobTemplates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        job_template_description: str = None,
        job_template_id: str = None,
        job_template_name: str = None,
        status: str = None,
        tags: List[main_models.ListJobTemplatesResponseBodyJobTemplatesTags] = None,
        update_time: str = None,
    ):
        # The creation time. The example uses the YYYY-MM-DD HH:mm:ss format.
        self.create_time = create_time
        # The template description.
        self.job_template_description = job_template_description
        # The job template ID.
        self.job_template_id = job_template_id
        # The template name.
        self.job_template_name = job_template_name
        # The job template status.
        self.status = status
        # The job tags.
        self.tags = tags
        # The update time. The example uses the YYYY-MM-DD HH:mm:ss format.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_template_description is not None:
            result['JobTemplateDescription'] = self.job_template_description

        if self.job_template_id is not None:
            result['JobTemplateId'] = self.job_template_id

        if self.job_template_name is not None:
            result['JobTemplateName'] = self.job_template_name

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobTemplateDescription') is not None:
            self.job_template_description = m.get('JobTemplateDescription')

        if m.get('JobTemplateId') is not None:
            self.job_template_id = m.get('JobTemplateId')

        if m.get('JobTemplateName') is not None:
            self.job_template_name = m.get('JobTemplateName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListJobTemplatesResponseBodyJobTemplatesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListJobTemplatesResponseBodyJobTemplatesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The job tag key.
        self.key = key
        # The job tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

