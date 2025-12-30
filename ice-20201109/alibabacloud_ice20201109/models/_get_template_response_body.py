# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template: main_models.GetTemplateResponseBodyTemplate = None,
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
            temp_model = main_models.GetTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m.get('Template'))

        return self

class GetTemplateResponseBodyTemplate(DaraModel):
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
        related_mediaids: str = None,
        status: str = None,
        template_id: str = None,
        type: str = None,
    ):
        # The clip parameters for submitting a video production job. You can replace mediaId and text with real values to submit a job. References:
        # 
        # *   [Create and use a regular template](https://help.aliyun.com/document_detail/445399.html)
        # *   [Create and use advanced templates](https://help.aliyun.com/document_detail/445389.html)
        self.clips_param = clips_param
        # The template configurations.
        # 
        # *   For more information about the configurations of a regular template, see [Config object of a regular template](https://help.aliyun.com/document_detail/456193.html).
        # *   For more information about the configurations of an advanced template, see [Create and use advanced templates](https://help.aliyun.com/document_detail/445389.html).
        self.config = config
        # The thumbnail URL.
        self.cover_url = cover_url
        # The source from which the template was created. Valid values:
        # 
        # *   AliyunConsole
        # *   OpenAPI
        # *   WebSDK
        self.create_source = create_source
        # The time when the template was created.
        self.creation_time = creation_time
        # The source from which the template was modified. Valid values:
        # 
        # *   AliyunConsole
        # *   OpenAPI
        # *   WebSDK
        self.modified_source = modified_source
        # The time when the template was last modified.
        self.modified_time = modified_time
        # The template name.
        self.name = name
        # The preview media asset.
        self.preview_media = preview_media
        # The state of the preview media asset. Valid values:
        # 
        # *   Init: the initial state, which indicates that the source file is not ready.
        # *   Preparing: The source file is being prepared. For example, the file is being uploaded or edited.
        # *   PrepareFail: The source file failed to be prepared. For example, the information about the source file failed to be obtained.
        # *   Normal: The source file is ready.
        self.preview_media_status = preview_media_status
        # The IDs of the materials associated with the template for use by the regular template editor.
        self.related_mediaids = related_mediaids
        # The template state. Valid values:
        # 
        # *   Available
        # *   Created
        # *   Uploading
        # *   Processing
        # *   UploadFailed
        # *   ProcessFailed
        self.status = status
        # The template ID.
        self.template_id = template_id
        # The template type. Valid values:
        # 
        # *   Timeline
        # *   VETemplate
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

        if self.related_mediaids is not None:
            result['RelatedMediaids'] = self.related_mediaids

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

        if m.get('RelatedMediaids') is not None:
            self.related_mediaids = m.get('RelatedMediaids')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

