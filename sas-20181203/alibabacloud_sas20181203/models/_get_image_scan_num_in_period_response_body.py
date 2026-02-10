# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetImageScanNumInPeriodResponseBody(DaraModel):
    def __init__(
        self,
        image_scan_data: main_models.GetImageScanNumInPeriodResponseBodyImageScanData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.image_scan_data = image_scan_data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_scan_data:
            self.image_scan_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_scan_data is not None:
            result['ImageScanData'] = self.image_scan_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScanData') is not None:
            temp_model = main_models.GetImageScanNumInPeriodResponseBodyImageScanData()
            self.image_scan_data = temp_model.from_map(m.get('ImageScanData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetImageScanNumInPeriodResponseBodyImageScanData(DaraModel):
    def __init__(
        self,
        image_scan_count: int = None,
    ):
        # The number of image scans.
        self.image_scan_count = image_scan_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_scan_count is not None:
            result['ImageScanCount'] = self.image_scan_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScanCount') is not None:
            self.image_scan_count = m.get('ImageScanCount')

        return self

