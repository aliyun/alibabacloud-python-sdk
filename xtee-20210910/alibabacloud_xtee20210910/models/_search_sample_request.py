# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchSampleRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        lang: str = None,
        reg_id: str = None,
        tab: str = None,
        type: str = None,
        upload_time_end: str = None,
        upload_time_start: str = None,
    ):
        # The domain name keyword provided.
        self.keyword = keyword
        # The language of error messages returned by the API. Valid values: zh: Chinese. en: English. Default value: en.
        self.lang = lang
        # The area encoding.
        self.reg_id = reg_id
        # The scenario.
        self.tab = tab
        # The access type.
        self.type = type
        # The upload end time.
        self.upload_time_end = upload_time_end
        # The upload start time.
        self.upload_time_start = upload_time_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

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
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('Tab') is not None:
            self.tab = m.get('Tab')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UploadTimeEnd') is not None:
            self.upload_time_end = m.get('UploadTimeEnd')

        if m.get('UploadTimeStart') is not None:
            self.upload_time_start = m.get('UploadTimeStart')

        return self

