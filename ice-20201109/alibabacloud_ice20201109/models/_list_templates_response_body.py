# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        templates: List[main_models.ListTemplatesResponseBodyTemplates] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The queried templates.
        self.templates = templates
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.templates:
            for v1 in self.templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Templates'] = []
        if self.templates is not None:
            for k1 in self.templates:
                result['Templates'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.templates = []
        if m.get('Templates') is not None:
            for k1 in m.get('Templates'):
                temp_model = main_models.ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTemplatesResponseBodyTemplates(DaraModel):
    def __init__(
        self,
        clips_param: str = None,
        config: str = None,
        cover_url: str = None,
        create_source: str = None,
        creation_time: str = None,
        modified_source: str = None,
        modified_time: str = None,
        name: str = None,
        preview_media: str = None,
        preview_media_status: str = None,
        status: str = None,
        template_id: str = None,
        type: str = None,
    ):
        # The clip parameters.
        self.clips_param = clips_param
        # The template configurations.
        self.config = config
        # The thumbnail URL.
        self.cover_url = cover_url
        # The source from which the template was created.
        # 
        # Valid values:
        # 
        # *   AliyunConsole
        # *   WebSDK
        # *   OpenAPI
        self.create_source = create_source
        # The time when the template was created.
        self.creation_time = creation_time
        # The source from which the template was modified.
        # 
        # Valid values:
        # 
        # *   AliyunConsole
        # *   WebSDK
        # *   OpenAPI
        self.modified_source = modified_source
        # The time when the template was last modified.
        self.modified_time = modified_time
        # The template name.
        self.name = name
        # The preview media asset.
        self.preview_media = preview_media
        # The state of the preview media asset.
        # 
        # Valid values:
        # 
        # *   PrepareFail
        # *   Init
        # *   Normal
        # *   Preparing
        self.preview_media_status = preview_media_status
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
        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param

        if self.config is not None:
            result['Config'] = self.config

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.create_source is not None:
            result['CreateSource'] = self.create_source

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media

        if self.preview_media_status is not None:
            result['PreviewMediaStatus'] = self.preview_media_status

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')

        if m.get('PreviewMediaStatus') is not None:
            self.preview_media_status = m.get('PreviewMediaStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

