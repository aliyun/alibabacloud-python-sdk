# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDesktopIdsByVulNamesResponseBody(DaraModel):
    def __init__(
        self,
        desktop_items: List[main_models.DescribeDesktopIdsByVulNamesResponseBodyDesktopItems] = None,
        request_id: str = None,
    ):
        # The array of cloud desktop information.
        self.desktop_items = desktop_items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.desktop_items:
            for v1 in self.desktop_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DesktopItems'] = []
        if self.desktop_items is not None:
            for k1 in self.desktop_items:
                result['DesktopItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_items = []
        if m.get('DesktopItems') is not None:
            for k1 in m.get('DesktopItems'):
                temp_model = main_models.DescribeDesktopIdsByVulNamesResponseBodyDesktopItems()
                self.desktop_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDesktopIdsByVulNamesResponseBodyDesktopItems(DaraModel):
    def __init__(
        self,
        desktop_id: str = None,
        desktop_name: str = None,
    ):
        # The cloud desktop ID.
        self.desktop_id = desktop_id
        # The cloud desktop name.
        self.desktop_name = desktop_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        return self

