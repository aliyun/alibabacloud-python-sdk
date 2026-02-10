# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class OperateImageBaselineWhitelistRequest(DaraModel):
    def __init__(
        self,
        baseline_item_key_list: str = None,
        image_uuid: str = None,
        lang: str = None,
        operation: str = None,
        scan_range: List[str] = None,
    ):
        # The keys of baseline check items.
        # 
        # This parameter is required.
        self.baseline_item_key_list = baseline_item_key_list
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The operation that you want to perform on the check items. Valid values:
        # 
        # *   **add**: adds the check items to the whitelist
        # *   **del**: removes the check items from the whitelist
        # 
        # This parameter is required.
        self.operation = operation
        # The types of the assets that you want to scan.
        self.scan_range = scan_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_item_key_list is not None:
            result['BaselineItemKeyList'] = self.baseline_item_key_list

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineItemKeyList') is not None:
            self.baseline_item_key_list = m.get('BaselineItemKeyList')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        return self

