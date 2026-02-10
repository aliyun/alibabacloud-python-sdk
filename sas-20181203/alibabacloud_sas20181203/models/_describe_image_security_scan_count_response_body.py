# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageSecurityScanCountResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeImageSecurityScanCountResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
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
            temp_model = main_models.DescribeImageSecurityScanCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageSecurityScanCountResponseBodyData(DaraModel):
    def __init__(
        self,
        image_baseline_count: int = None,
        image_cve_vul_count: int = None,
        image_malicious_file_count: int = None,
        image_sca_vul_count: int = None,
    ):
        # The number of image baseline risks detected on the current asset.
        self.image_baseline_count = image_baseline_count
        # The number of image system vulnerabilities returned on the current page.
        self.image_cve_vul_count = image_cve_vul_count
        # The number of malicious image samples returned on the current page.
        self.image_malicious_file_count = image_malicious_file_count
        # The number of image application vulnerabilities returned on the current page.
        self.image_sca_vul_count = image_sca_vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_baseline_count is not None:
            result['ImageBaselineCount'] = self.image_baseline_count

        if self.image_cve_vul_count is not None:
            result['ImageCveVulCount'] = self.image_cve_vul_count

        if self.image_malicious_file_count is not None:
            result['ImageMaliciousFileCount'] = self.image_malicious_file_count

        if self.image_sca_vul_count is not None:
            result['ImageScaVulCount'] = self.image_sca_vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageBaselineCount') is not None:
            self.image_baseline_count = m.get('ImageBaselineCount')

        if m.get('ImageCveVulCount') is not None:
            self.image_cve_vul_count = m.get('ImageCveVulCount')

        if m.get('ImageMaliciousFileCount') is not None:
            self.image_malicious_file_count = m.get('ImageMaliciousFileCount')

        if m.get('ImageScaVulCount') is not None:
            self.image_sca_vul_count = m.get('ImageScaVulCount')

        return self

