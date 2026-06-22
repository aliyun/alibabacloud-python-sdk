# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAttackCountRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        lang: str = None,
        source_ip: str = None,
        uuids: str = None,
    ):
        # The source identifier of the request. Set this parameter to sas.
        self.from_ = from_
        # The language of the request and response. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The IP address of the access source.
        self.source_ip = source_ip
        # The UUID of the server. Separate multiple UUIDs with commas (,).
        # > Call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to obtain this parameter.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

