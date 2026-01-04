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
        # The export status of the image. Valid values:
        # 
        # *   Exporting
        # *   Exported
        # *   ExportError
        # *   Unexported
        self.image_export_status = image_export_status
        # The ID of the request.
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

