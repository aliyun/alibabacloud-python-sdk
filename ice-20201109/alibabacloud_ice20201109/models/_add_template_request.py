# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTemplateRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        cover_url: str = None,
        name: str = None,
        preview_media: str = None,
        related_mediaids: str = None,
        source: str = None,
        status: str = None,
        type: str = None,
    ):
        self.config = config
        # The URL of the template thumbnail.
        self.cover_url = cover_url
        # The name of the custom template.
        self.name = name
        # The ID of the template preview video.
        self.preview_media = preview_media
        # The IDs of the materials associated with the template for use by the regular template editor.
        self.related_mediaids = related_mediaids
        # The source from which the template is created. Valid values:
        # 
        # *   OpenAPI
        # *   AliyunConsole
        # *   WebSDK
        # 
        # <!---->
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
        # <!---->
        self.status = status
        # The template type. Valid values:
        # 
        # *   Timeline: a regular template created based on the timeline of a video editing project, in which multiple materials are arranged in sequence across multiple layers. It can be used to convert text and images into videos, create photo albums, add opening and closing parts, and apply the default watermark.
        # *   VETemplate: an advanced template created using effects of Adobe After Effects (AE). It can be used to produce complex animations and advanced media effects.
        # 
        # <!---->
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

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

