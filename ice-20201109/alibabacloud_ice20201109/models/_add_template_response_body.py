# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class AddTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template: main_models.AddTemplateResponseBodyTemplate = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The template information.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template is not None:
            result['Template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Template') is not None:
            temp_model = main_models.AddTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class AddTemplateResponseBodyTemplate(DaraModel):
    def __init__(
        self,
        config: str = None,
        cover_url: str = None,
        create_source: str = None,
        modified_source: str = None,
        name: str = None,
        preview_media: str = None,
        status: str = None,
        template_id: str = None,
        type: str = None,
    ):
        # The template configurations.
        self.config = config
        # The URL of the template thumbnail.
        self.cover_url = cover_url
        # The source from which the template was created.
        # 
        # Valid values:
        # 
        # *   AliyunConsole
        # *   WebSDK
        # *   OpenAPI
        self.create_source = create_source
        # The source from which the template was modified.
        # 
        # Valid values:
        # 
        # *   AliyunConsole
        # *   WebSDK
        # *   OpenAPI
        self.modified_source = modified_source
        # The template name.
        self.name = name
        # The ID of the preview video.
        self.preview_media = preview_media
        # The template state.
        # 
        # Valid values:
        # 
        # *   UploadFailed: Failed to upload the video.
        # *   ProcessFailed: Failed to process the advanced template.
        # *   Available: The template is available.
        # *   Uploading: The video is being uploaded.
        # *   Created: The template is created but not ready for use.
        # *   Processing: The advanced template is being processed.
        self.status = status
        # The template ID.
        self.template_id = template_id
        # The template type.
        # 
        # Valid values:
        # 
        # *   Timeline: regular template.
        # *   VETemplate: advanced template.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.create_source is not None:
            result['CreateSource'] = self.create_source

        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source

        if self.name is not None:
            result['Name'] = self.name

        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')

        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

