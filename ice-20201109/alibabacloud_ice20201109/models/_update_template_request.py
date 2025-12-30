# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTemplateRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        cover_url: str = None,
        name: str = None,
        preview_media: str = None,
        related_mediaids: str = None,
        source: str = None,
        status: str = None,
        template_id: str = None,
    ):
        self.config = config
        # The URL of the template thumbnail.
        self.cover_url = cover_url
        # The name of the online editing template.
        self.name = name
        # The ID of the preview video.
        self.preview_media = preview_media
        # The IDs of the materials associated with the template for use by the regular template editor.
        self.related_mediaids = related_mediaids
        # The source from which the template is modified. Default value: OpenAPI. Valid values:
        # 
        # *   AliyunConsole
        # *   OpenAPI
        # *   WebSDK
        self.source = source
        # The template state. Valid values:
        # 
        # *   Available: The template is available.
        # *   Created: The template is created but not ready for use.
        # *   Uploading: The video is being uploaded.
        # *   Processing: The advanced template is being processed.
        # *   UploadFailed: Failed to upload the video.
        # *   ProcessFailed: Failed to process the advanced template.
        # 
        # >  After an advanced template is created, it enters the Processing state. In this case, the template is unavailable. The template can be used only when it is in the Available state. The time required for template processing varies based on the size of the template file. Generally, it ranges from 10 seconds to 5 minutes.
        self.status = status
        # The ID of the online editing template. You can obtain the template ID in the [Intelligent Media Services (IMS) console](https://ice.console.aliyun.com/production/template/list/common) or the response parameters of the [AddTemplate](https://help.aliyun.com/document_detail/441161.html) operation.
        self.template_id = template_id

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

        if self.name is not None:
            result['Name'] = self.name

        if self.preview_media is not None:
            result['PreviewMedia'] = self.preview_media

        if self.related_mediaids is not None:
            result['RelatedMediaids'] = self.related_mediaids

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PreviewMedia') is not None:
            self.preview_media = m.get('PreviewMedia')

        if m.get('RelatedMediaids') is not None:
            self.related_mediaids = m.get('RelatedMediaids')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

