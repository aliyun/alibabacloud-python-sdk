# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageScanAuthCountResponseBody(DaraModel):
    def __init__(
        self,
        image_scan: main_models.DescribeImageScanAuthCountResponseBodyImageScan = None,
        request_id: str = None,
    ):
        # The authorization details of image security scanning.
        self.image_scan = image_scan
        # The ID of the request. The China Cloud generates a unique ID for each request. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_scan:
            self.image_scan.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_scan is not None:
            result['ImageScan'] = self.image_scan.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScan') is not None:
            temp_model = main_models.DescribeImageScanAuthCountResponseBodyImageScan()
            self.image_scan = temp_model.from_map(m.get('ImageScan'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageScanAuthCountResponseBodyImageScan(DaraModel):
    def __init__(
        self,
        image_scan_capacity: int = None,
        instance_id: str = None,
        scan_count: int = None,
    ):
        # The total number of authorization quotas.
        self.image_scan_capacity = image_scan_capacity
        # The instance ID of the purchased Security Center instance.
        self.instance_id = instance_id
        # The number of used authorization quotas.
        self.scan_count = scan_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_scan_capacity is not None:
            result['ImageScanCapacity'] = self.image_scan_capacity

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.scan_count is not None:
            result['ScanCount'] = self.scan_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageScanCapacity') is not None:
            self.image_scan_capacity = m.get('ImageScanCapacity')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ScanCount') is not None:
            self.scan_count = m.get('ScanCount')

        return self

