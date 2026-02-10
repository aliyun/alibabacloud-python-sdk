# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageBuildRiskByKeyRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        image_uuid: str = None,
        lang: str = None,
        page_size: int = None,
        risk_key: str = None,
        status: int = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The key of the risk rule. 
        # > You can call the [DescribeImageBuildRiskList](~~DescribeImageBuildRiskList~~) operation to obtain the value of **RiskKey**.
        self.risk_key = risk_key
        # The status of the alert event. Valid values:
        # 
        # *   **0**: unhandled.
        # *   **1**: ignored.
        # *   **2**: false positive.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_key is not None:
            result['RiskKey'] = self.risk_key

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskKey') is not None:
            self.risk_key = m.get('RiskKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

