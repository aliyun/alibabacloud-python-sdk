# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchUpdateNoticeStatusRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        lang: str = None,
        notice_biz: str = None,
        notice_status: str = None,
        source_ip: str = None,
    ):
        # The list of primary key identifiers to be synchronized to Certificate Management Service. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.ids = ids
        # The language type for the request and the received message. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The business code of message notification. The value is fixed as ssl.
        self.notice_biz = notice_biz
        # Specifies whether to enable message notification.
        # \\--enable: enables message notification.
        # \\--disable: disables message notification.
        # 
        # This parameter is required.
        self.notice_status = notice_status
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.notice_biz is not None:
            result['NoticeBiz'] = self.notice_biz

        if self.notice_status is not None:
            result['NoticeStatus'] = self.notice_status

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NoticeBiz') is not None:
            self.notice_biz = m.get('NoticeBiz')

        if m.get('NoticeStatus') is not None:
            self.notice_status = m.get('NoticeStatus')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

