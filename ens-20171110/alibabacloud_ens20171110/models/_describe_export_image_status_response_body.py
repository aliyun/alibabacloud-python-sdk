# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeExportImageStatusResponseBody(DaraModel):
    def __init__(
        self,
        image_export_status: str = None,
        request_id: str = None,
    ):
        # The image export status. Valid values:
        # - Exporting: The image is being exported.
        # - Exported: The image is exported.
        # - ExportError: An error occurred during the image export.
        # - Unexported: The image is not exported.
        self.image_export_status = image_export_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_export_status is not None:
            result['ImageExportStatus'] = self.image_export_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageExportStatus') is not None:
            self.image_export_status = m.get('ImageExportStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

