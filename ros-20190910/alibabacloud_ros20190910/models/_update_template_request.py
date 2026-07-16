# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateTemplateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        is_draft: bool = None,
        rotate_strategy: str = None,
        template_body: str = None,
        template_id: str = None,
        template_name: str = None,
        template_url: str = None,
        validation_options: List[str] = None,
    ):
        # The description of the template. The maximum length is 256 characters.
        self.description = description
        # Whether to update the Draft (draft) version. Values:
        # - false (default): If template content is provided, a new version is created, and the Draft version is cleared. Otherwise, the current latest version is modified.
        # - true: Modifies the Draft version. The Draft version can only be retrieved via the GetTemplate interface. The ListTemplateVersions interface will not return it. The TemplateVersion parameter in other interfaces cannot specify Draft.
        self.is_draft = is_draft
        # Template version rotation strategy. Values:
        # - None (default): No rotation. An error occurs when the version limit is reached.
        # - DeleteOldestNonSharedVersionWhenLimitExceeded: Rotates and deletes non-shared template versions.
        # > 
        # > - If all versions of the template are shared, they cannot be rotated and deleted.
        # > - The current latest version will not be rotated and deleted.
        # > - Regardless of whether rotation deletion is used, the template version number cannot exceed v65000.
        self.rotate_strategy = rotate_strategy
        # The structure of the template body. The length should be between 1 and 524,288 bytes. If the content is long, it is recommended to use HTTP POST + Body Param to pass the parameter in the request body to avoid request failure due to an overly long URL.
        # 
        # > You must and can only specify one of `TemplateBody`, `TemplateURL`, `TemplateId`, or `TemplateScratchId`.
        self.template_body = template_body
        # The template ID. Supports both shared and private templates.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The name of the template.  
        # The length should not exceed 255 characters (utf-8 encoding), and it must start with a number, letter, or Chinese character. It can include numbers, letters, Chinese characters, hyphens (-), and underscores (_).
        self.template_name = template_name
        # The location of the file containing the template body. The URL must point to a template located on a web server (HTTP or HTTPS) or in an Alibaba Cloud OSS bucket (e.g., oss://ros/template/demo, oss://ros/template/demo?RegionId=cn-hangzhou), with a maximum size of 524,288 bytes.   
        # 
        # > If the OSS region is not specified, it defaults to the same as the `RegionId` parameter in the request.
        #    
        # You can only specify one of `TemplateBody` or `TemplateURL`.   
        # The maximum length of the URL is 1,024 bytes.
        self.template_url = template_url
        # Validation options.
        # 
        # By default, no options are enabled, and strict validation is performed.
        self.validation_options = validation_options

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.is_draft is not None:
            result['IsDraft'] = self.is_draft

        if self.rotate_strategy is not None:
            result['RotateStrategy'] = self.rotate_strategy

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_url is not None:
            result['TemplateURL'] = self.template_url

        if self.validation_options is not None:
            result['ValidationOptions'] = self.validation_options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDraft') is not None:
            self.is_draft = m.get('IsDraft')

        if m.get('RotateStrategy') is not None:
            self.rotate_strategy = m.get('RotateStrategy')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')

        if m.get('ValidationOptions') is not None:
            self.validation_options = m.get('ValidationOptions')

        return self

