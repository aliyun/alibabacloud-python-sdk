# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSampleRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        reg_id: str = None,
        sample_name: str = None,
        tab: str = None,
        type: str = None,
        upload_time_end: str = None,
        upload_time_start: str = None,
    ):
        # Current page number.
        self.current_page = current_page
        # Language of error messages returned by the API. Valid values: zh: Chinese. en: English. Default value: en.
        self.lang = lang
        # Page size.
        self.page_size = page_size
        # Area code.
        self.reg_id = reg_id
        # Sample name.
        self.sample_name = sample_name
        # Scenario.
        self.tab = tab
        # Access type.
        self.type = type
        # Upload end time.
        self.upload_time_end = upload_time_end
        # Upload start time.
        self.upload_time_start = upload_time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.sample_name is not None:
            result['SampleName'] = self.sample_name

        if self.tab is not None:
            result['Tab'] = self.tab

        if self.type is not None:
            result['Type'] = self.type

        if self.upload_time_end is not None:
            result['UploadTimeEnd'] = self.upload_time_end

        if self.upload_time_start is not None:
            result['UploadTimeStart'] = self.upload_time_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('SampleName') is not None:
            self.sample_name = m.get('SampleName')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UploadTimeEnd') is not None:
            self.upload_time_end = m.get('UploadTimeEnd')

        if m.get('UploadTimeStart') is not None:
            self.upload_time_start = m.get('UploadTimeStart')

        return self

