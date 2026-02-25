# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListCustomViewsResponseBody(DaraModel):
    def __init__(
        self,
        custom_views: main_models.ListCustomViewsResponseBodyCustomViews = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.custom_views = custom_views
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.custom_views:
            self.custom_views.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_views is not None:
            result['CustomViews'] = self.custom_views.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomViews') is not None:
            temp_model = main_models.ListCustomViewsResponseBodyCustomViews()
            self.custom_views = temp_model.from_map(m.get('CustomViews'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomViewsResponseBodyCustomViews(DaraModel):
    def __init__(
        self,
        custom_view: List[main_models.ListCustomViewsResponseBodyCustomViewsCustomView] = None,
    ):
        self.custom_view = custom_view

    def validate(self):
        if self.custom_view:
            for v1 in self.custom_view:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomView'] = []
        if self.custom_view is not None:
            for k1 in self.custom_view:
                result['CustomView'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_view = []
        if m.get('CustomView') is not None:
            for k1 in m.get('CustomView'):
                temp_model = main_models.ListCustomViewsResponseBodyCustomViewsCustomView()
                self.custom_view.append(temp_model.from_map(k1))

        return self

class ListCustomViewsResponseBodyCustomViewsCustomView(DaraModel):
    def __init__(
        self,
        custom_view_id: str = None,
        image_url: str = None,
    ):
        self.custom_view_id = custom_view_id
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_view_id is not None:
            result['CustomViewId'] = self.custom_view_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomViewId') is not None:
            self.custom_view_id = m.get('CustomViewId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

