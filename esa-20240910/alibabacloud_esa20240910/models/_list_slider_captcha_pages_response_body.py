# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListSliderCaptchaPagesResponseBody(DaraModel):
    def __init__(
        self,
        pages: List[main_models.ListSliderCaptchaPagesResponseBodyPages] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of custom slider CAPTCHA pages.
        self.pages = pages
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.pages:
            for v1 in self.pages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Pages'] = []
        if self.pages is not None:
            for k1 in self.pages:
                result['Pages'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pages = []
        if m.get('Pages') is not None:
            for k1 in m.get('Pages'):
                temp_model = main_models.ListSliderCaptchaPagesResponseBodyPages()
                self.pages.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSliderCaptchaPagesResponseBodyPages(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        site_ids: List[int] = None,
    ):
        # The ID of the custom slider CAPTCHA page.
        self.id = id
        # The name of the custom slider CAPTCHA page.
        self.name = name
        # The list of associated site IDs.
        self.site_ids = site_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.site_ids is not None:
            result['SiteIds'] = self.site_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SiteIds') is not None:
            self.site_ids = m.get('SiteIds')

        return self

