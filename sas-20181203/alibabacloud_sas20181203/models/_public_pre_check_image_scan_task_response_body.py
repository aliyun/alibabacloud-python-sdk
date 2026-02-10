# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class PublicPreCheckImageScanTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.PublicPreCheckImageScanTaskResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned if the call is successful.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.PublicPreCheckImageScanTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class PublicPreCheckImageScanTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        need_auth_count: int = None,
        scan_image_count: int = None,
    ):
        # The number of images to scan in the task.
        self.need_auth_count = need_auth_count
        # The quota for container image scan to be consumed by the task.
        self.scan_image_count = scan_image_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_auth_count is not None:
            result['NeedAuthCount'] = self.need_auth_count

        if self.scan_image_count is not None:
            result['ScanImageCount'] = self.scan_image_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedAuthCount') is not None:
            self.need_auth_count = m.get('NeedAuthCount')

        if m.get('ScanImageCount') is not None:
            self.scan_image_count = m.get('ScanImageCount')

        return self

