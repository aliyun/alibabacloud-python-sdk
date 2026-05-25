# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTlogCollectListRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        app_version: str = None,
        author: str = None,
        begin_date: int = None,
        city: str = None,
        create_begin_date: int = None,
        create_end_date: int = None,
        device_id: str = None,
        end_date: int = None,
        keyword: str = None,
        model: str = None,
        os: str = None,
        os_version: str = None,
        page_index: int = None,
        page_size: int = None,
        positive_comment: str = None,
        source_type: str = None,
        status: str = None,
        update_begin_date: int = None,
        update_end_date: int = None,
        user_nick: str = None,
        utdid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.app_version = app_version
        self.author = author
        self.begin_date = begin_date
        self.city = city
        self.create_begin_date = create_begin_date
        self.create_end_date = create_end_date
        self.device_id = device_id
        self.end_date = end_date
        self.keyword = keyword
        self.model = model
        # This parameter is required.
        self.os = os
        self.os_version = os_version
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        self.positive_comment = positive_comment
        self.source_type = source_type
        self.status = status
        self.update_begin_date = update_begin_date
        self.update_end_date = update_end_date
        self.user_nick = user_nick
        self.utdid = utdid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.author is not None:
            result['Author'] = self.author

        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date

        if self.city is not None:
            result['City'] = self.city

        if self.create_begin_date is not None:
            result['CreateBeginDate'] = self.create_begin_date

        if self.create_end_date is not None:
            result['CreateEndDate'] = self.create_end_date

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.model is not None:
            result['Model'] = self.model

        if self.os is not None:
            result['Os'] = self.os

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.positive_comment is not None:
            result['PositiveComment'] = self.positive_comment

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_begin_date is not None:
            result['UpdateBeginDate'] = self.update_begin_date

        if self.update_end_date is not None:
            result['UpdateEndDate'] = self.update_end_date

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        if self.utdid is not None:
            result['Utdid'] = self.utdid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CreateBeginDate') is not None:
            self.create_begin_date = m.get('CreateBeginDate')

        if m.get('CreateEndDate') is not None:
            self.create_end_date = m.get('CreateEndDate')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PositiveComment') is not None:
            self.positive_comment = m.get('PositiveComment')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateBeginDate') is not None:
            self.update_begin_date = m.get('UpdateBeginDate')

        if m.get('UpdateEndDate') is not None:
            self.update_end_date = m.get('UpdateEndDate')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')

        return self

