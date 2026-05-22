# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        auth_conf_shrink: str = None,
        biz_name: str = None,
        comment: str = None,
        data_shrink: str = None,
        host_policy: str = None,
        proxied: bool = None,
        record_name: str = None,
        site_id: int = None,
        source_type: str = None,
        ttl: int = None,
        type: str = None,
    ):
        self.auth_conf_shrink = auth_conf_shrink
        # 业务场景
        self.biz_name = biz_name
        self.comment = comment
        # This parameter is required.
        self.data_shrink = data_shrink
        self.host_policy = host_policy
        # 是否代理加速
        self.proxied = proxied
        # 记录名称
        # 
        # This parameter is required.
        self.record_name = record_name
        # This parameter is required.
        self.site_id = site_id
        self.source_type = source_type
        # This parameter is required.
        self.ttl = ttl
        # 记录类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_conf_shrink is not None:
            result['AuthConf'] = self.auth_conf_shrink

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_shrink is not None:
            result['Data'] = self.data_shrink

        if self.host_policy is not None:
            result['HostPolicy'] = self.host_policy

        if self.proxied is not None:
            result['Proxied'] = self.proxied

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthConf') is not None:
            self.auth_conf_shrink = m.get('AuthConf')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Data') is not None:
            self.data_shrink = m.get('Data')

        if m.get('HostPolicy') is not None:
            self.host_policy = m.get('HostPolicy')

        if m.get('Proxied') is not None:
            self.proxied = m.get('Proxied')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

