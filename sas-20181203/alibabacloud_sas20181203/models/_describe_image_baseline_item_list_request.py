# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageBaselineItemListRequest(DaraModel):
    def __init__(
        self,
        baseline_class_key: str = None,
        baseline_name_key: str = None,
        current_page: int = None,
        image_uuid: str = None,
        lang: str = None,
        page_size: int = None,
        scan_range: List[str] = None,
        status: str = None,
        uuids: List[str] = None,
    ):
        # The key of the baseline type.
        self.baseline_class_key = baseline_class_key
        # The key of the baseline name.
        self.baseline_name_key = baseline_name_key
        # The number of the page to return.
        self.current_page = current_page
        # The UUID of the image.
        # 
        # This parameter is required.
        self.image_uuid = image_uuid
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        self.page_size = page_size
        # The types of the assets that are scanned.
        self.scan_range = scan_range
        # The status of the baseline risk item. Valid values:
        # 
        # *   **0**: unfixed
        # *   **1**: fixed
        # *   **2**: pending verification
        # *   **3**: fixing failed
        self.status = status
        # The UUIDs of images.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_class_key is not None:
            result['BaselineClassKey'] = self.baseline_class_key

        if self.baseline_name_key is not None:
            result['BaselineNameKey'] = self.baseline_name_key

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.status is not None:
            result['Status'] = self.status

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineClassKey') is not None:
            self.baseline_class_key = m.get('BaselineClassKey')

        if m.get('BaselineNameKey') is not None:
            self.baseline_name_key = m.get('BaselineNameKey')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

