# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateJobTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        job_template_config_shrink: str = None,
        job_template_description: str = None,
        job_template_id: str = None,
        job_template_name: str = None,
    ):
        # The template configuration.
        self.job_template_config_shrink = job_template_config_shrink
        # The template description.
        self.job_template_description = job_template_description
        # The job template ID.
        # 
        # This parameter is required.
        self.job_template_id = job_template_id
        # The template name.
        self.job_template_name = job_template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_template_config_shrink is not None:
            result['JobTemplateConfig'] = self.job_template_config_shrink

        if self.job_template_description is not None:
            result['JobTemplateDescription'] = self.job_template_description

        if self.job_template_id is not None:
            result['JobTemplateId'] = self.job_template_id

        if self.job_template_name is not None:
            result['JobTemplateName'] = self.job_template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobTemplateConfig') is not None:
            self.job_template_config_shrink = m.get('JobTemplateConfig')

        if m.get('JobTemplateDescription') is not None:
            self.job_template_description = m.get('JobTemplateDescription')

        if m.get('JobTemplateId') is not None:
            self.job_template_id = m.get('JobTemplateId')

        if m.get('JobTemplateName') is not None:
            self.job_template_name = m.get('JobTemplateName')

        return self

