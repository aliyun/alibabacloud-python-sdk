# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class PreviewDatasetVersionResponseBody(DaraModel):
    def __init__(
        self,
        preview_result: main_models.PreviewDatasetVersionResponseBodyPreviewResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Preview results
        self.preview_result = preview_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.preview_result:
            self.preview_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.preview_result is not None:
            result['PreviewResult'] = self.preview_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreviewResult') is not None:
            temp_model = main_models.PreviewDatasetVersionResponseBodyPreviewResult()
            self.preview_result = temp_model.from_map(m.get('PreviewResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PreviewDatasetVersionResponseBodyPreviewResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        file_name: str = None,
        mime_type: str = None,
        support_preview: bool = None,
    ):
        # Content
        self.content = content
        # File name
        self.file_name = file_name
        # The MIME type
        self.mime_type = mime_type
        # Preview availability
        self.support_preview = support_preview

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.mime_type is not None:
            result['MimeType'] = self.mime_type

        if self.support_preview is not None:
            result['SupportPreview'] = self.support_preview

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')

        if m.get('SupportPreview') is not None:
            self.support_preview = m.get('SupportPreview')

        return self

