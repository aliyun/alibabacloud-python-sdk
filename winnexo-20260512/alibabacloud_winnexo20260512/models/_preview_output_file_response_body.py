# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class PreviewOutputFileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        degraded: bool = None,
        download_expires_at: str = None,
        download_url: str = None,
        file_ext: str = None,
        gmt_modified: str = None,
        item_name: str = None,
        item_type: str = None,
        message: str = None,
        output_item_id: str = None,
        preview_expires_at: str = None,
        preview_type: str = None,
        preview_url: str = None,
        read_state: str = None,
        request_id: str = None,
        slides: List[main_models.PreviewOutputFileResponseBodySlides] = None,
        unavailable_reason: str = None,
        version: main_models.PreviewOutputFileResponseBodyVersion = None,
    ):
        # The error code.
        self.code = code
        # The text content. This parameter is used for the CONTENT type.
        self.content = content
        # Indicates whether the preview is degraded to a download. A value of true indicates that the preview is degraded to a download and cannot be opened in an online previewer.
        self.degraded = degraded
        # The expiration time of the download ticket.
        self.download_expires_at = download_expires_at
        # The short-term signed download URL for the output. You can send a GET request to this URL before it expires.
        self.download_url = download_url
        # The file name extension. This parameter is used for the OSS_IMM type.
        self.file_ext = file_ext
        # The modification time in ISO8601 format.
        self.gmt_modified = gmt_modified
        # The output name.
        self.item_name = item_name
        # The output item type. Valid values: ppt, html, document, picture, slides, video, audio, email, and others.
        self.item_type = item_type
        # The message.
        self.message = message
        # The output item ID.
        self.output_item_id = output_item_id
        # The expiration time of the preview ticket.
        self.preview_expires_at = preview_expires_at
        # The preview type. Valid values: OSS_IMM, IMAGE, AUDIO, VIDEO, HTML, DING_TALK, VOICE_MEETING, and CONTENT.
        self.preview_type = preview_type
        # The preview URL. This parameter is used for OSS_IMM, DING_TALK, and VOICE_MEETING.
        self.preview_url = preview_url
        # The read state. Valid values: AVAILABLE, PRUNED, PENDING, and UNVERSIONED.
        self.read_state = read_state
        # The request ID.
        self.request_id = request_id
        # The list of slides for the slide deck output.
        self.slides = slides
        # The reason why the content is unavailable.
        self.unavailable_reason = unavailable_reason
        # The optimistic version number.
        self.version = version

    def validate(self):
        if self.slides:
            for v1 in self.slides:
                 if v1:
                    v1.validate()
        if self.version:
            self.version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content is not None:
            result['content'] = self.content

        if self.degraded is not None:
            result['degraded'] = self.degraded

        if self.download_expires_at is not None:
            result['downloadExpiresAt'] = self.download_expires_at

        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.file_ext is not None:
            result['fileExt'] = self.file_ext

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.item_name is not None:
            result['itemName'] = self.item_name

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.message is not None:
            result['message'] = self.message

        if self.output_item_id is not None:
            result['outputItemId'] = self.output_item_id

        if self.preview_expires_at is not None:
            result['previewExpiresAt'] = self.preview_expires_at

        if self.preview_type is not None:
            result['previewType'] = self.preview_type

        if self.preview_url is not None:
            result['previewUrl'] = self.preview_url

        if self.read_state is not None:
            result['readState'] = self.read_state

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['slides'] = []
        if self.slides is not None:
            for k1 in self.slides:
                result['slides'].append(k1.to_map() if k1 else None)

        if self.unavailable_reason is not None:
            result['unavailableReason'] = self.unavailable_reason

        if self.version is not None:
            result['version'] = self.version.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('degraded') is not None:
            self.degraded = m.get('degraded')

        if m.get('downloadExpiresAt') is not None:
            self.download_expires_at = m.get('downloadExpiresAt')

        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('fileExt') is not None:
            self.file_ext = m.get('fileExt')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('itemName') is not None:
            self.item_name = m.get('itemName')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('outputItemId') is not None:
            self.output_item_id = m.get('outputItemId')

        if m.get('previewExpiresAt') is not None:
            self.preview_expires_at = m.get('previewExpiresAt')

        if m.get('previewType') is not None:
            self.preview_type = m.get('previewType')

        if m.get('previewUrl') is not None:
            self.preview_url = m.get('previewUrl')

        if m.get('readState') is not None:
            self.read_state = m.get('readState')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.slides = []
        if m.get('slides') is not None:
            for k1 in m.get('slides'):
                temp_model = main_models.PreviewOutputFileResponseBodySlides()
                self.slides.append(temp_model.from_map(k1))

        if m.get('unavailableReason') is not None:
            self.unavailable_reason = m.get('unavailableReason')

        if m.get('version') is not None:
            temp_model = main_models.PreviewOutputFileResponseBodyVersion()
            self.version = temp_model.from_map(m.get('version'))

        return self

class PreviewOutputFileResponseBodyVersion(DaraModel):
    def __init__(
        self,
        availability: str = None,
        capabilities: main_models.PreviewOutputFileResponseBodyVersionCapabilities = None,
        content_revision: int = None,
        is_latest: bool = None,
        latest_version_id: str = None,
        read_state: str = None,
        selected_version_id: str = None,
        source_message_id: str = None,
        updated_at: str = None,
        version_no: int = None,
    ):
        # The number of remaining seats.
        self.availability = availability
        # Specifies whether the model supports multiple tool calls in a single response.
        self.capabilities = capabilities
        # The content revision number.
        self.content_revision = content_revision
        # Indicates whether the version is the latest version.
        self.is_latest = is_latest
        # The ID of the current latest version.
        self.latest_version_id = latest_version_id
        # The read state of the version.
        self.read_state = read_state
        # The ID of the version that is actually read.
        self.selected_version_id = selected_version_id
        # The ID of the message that generated this version.
        self.source_message_id = source_message_id
        # The update time.
        self.updated_at = updated_at
        # The version serial number.
        self.version_no = version_no

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availability is not None:
            result['availability'] = self.availability

        if self.capabilities is not None:
            result['capabilities'] = self.capabilities.to_map()

        if self.content_revision is not None:
            result['contentRevision'] = self.content_revision

        if self.is_latest is not None:
            result['isLatest'] = self.is_latest

        if self.latest_version_id is not None:
            result['latestVersionId'] = self.latest_version_id

        if self.read_state is not None:
            result['readState'] = self.read_state

        if self.selected_version_id is not None:
            result['selectedVersionId'] = self.selected_version_id

        if self.source_message_id is not None:
            result['sourceMessageId'] = self.source_message_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.version_no is not None:
            result['versionNo'] = self.version_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('availability') is not None:
            self.availability = m.get('availability')

        if m.get('capabilities') is not None:
            temp_model = main_models.PreviewOutputFileResponseBodyVersionCapabilities()
            self.capabilities = temp_model.from_map(m.get('capabilities'))

        if m.get('contentRevision') is not None:
            self.content_revision = m.get('contentRevision')

        if m.get('isLatest') is not None:
            self.is_latest = m.get('isLatest')

        if m.get('latestVersionId') is not None:
            self.latest_version_id = m.get('latestVersionId')

        if m.get('readState') is not None:
            self.read_state = m.get('readState')

        if m.get('selectedVersionId') is not None:
            self.selected_version_id = m.get('selectedVersionId')

        if m.get('sourceMessageId') is not None:
            self.source_message_id = m.get('sourceMessageId')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('versionNo') is not None:
            self.version_no = m.get('versionNo')

        return self

class PreviewOutputFileResponseBodyVersionCapabilities(DaraModel):
    def __init__(
        self,
        can_browser_open: bool = None,
        can_download: bool = None,
        can_edit: bool = None,
        can_restore: bool = None,
        can_save_as_knowledge: bool = None,
        can_share: bool = None,
    ):
        # Indicates whether the version can be opened in a browser.
        self.can_browser_open = can_browser_open
        # Indicates whether the version can be downloaded.
        self.can_download = can_download
        # Indicates whether the course can be edited or deleted.
        self.can_edit = can_edit
        # Indicates whether the version can be restored to the latest version.
        self.can_restore = can_restore
        # Indicates whether the version can be saved as knowledge.
        self.can_save_as_knowledge = can_save_as_knowledge
        # Indicates whether the version can be shared.
        self.can_share = can_share

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_browser_open is not None:
            result['canBrowserOpen'] = self.can_browser_open

        if self.can_download is not None:
            result['canDownload'] = self.can_download

        if self.can_edit is not None:
            result['canEdit'] = self.can_edit

        if self.can_restore is not None:
            result['canRestore'] = self.can_restore

        if self.can_save_as_knowledge is not None:
            result['canSaveAsKnowledge'] = self.can_save_as_knowledge

        if self.can_share is not None:
            result['canShare'] = self.can_share

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canBrowserOpen') is not None:
            self.can_browser_open = m.get('canBrowserOpen')

        if m.get('canDownload') is not None:
            self.can_download = m.get('canDownload')

        if m.get('canEdit') is not None:
            self.can_edit = m.get('canEdit')

        if m.get('canRestore') is not None:
            self.can_restore = m.get('canRestore')

        if m.get('canSaveAsKnowledge') is not None:
            self.can_save_as_knowledge = m.get('canSaveAsKnowledge')

        if m.get('canShare') is not None:
            self.can_share = m.get('canShare')

        return self

class PreviewOutputFileResponseBodySlides(DaraModel):
    def __init__(
        self,
        display_text: str = None,
        image_url: str = None,
        slide_id: str = None,
        slide_index: int = None,
        status: str = None,
    ):
        # The display text of the slide.
        self.display_text = display_text
        # Specifies the detail level of the image. Valid values: low, high, and auto. Default value: auto.
        self.image_url = image_url
        # The slide ID.
        self.slide_id = slide_id
        # The slide order.
        self.slide_index = slide_index
        # The signing status. Valid values:
        # - CREATED: created but not signed
        # - SUCCESS: signed successfully
        # - STOP: terminated
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_text is not None:
            result['displayText'] = self.display_text

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.slide_id is not None:
            result['slideId'] = self.slide_id

        if self.slide_index is not None:
            result['slideIndex'] = self.slide_index

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayText') is not None:
            self.display_text = m.get('displayText')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('slideId') is not None:
            self.slide_id = m.get('slideId')

        if m.get('slideIndex') is not None:
            self.slide_index = m.get('slideIndex')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

