# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSuspiciousStatisticsRequest(DaraModel):
    def __init__(
        self,
        group_id_list: str = None,
        source_ip: str = None,
    ):
        # The IDs of the asset groups that you want to query. Separate multiple asset group IDs with commas (,).
        # > You can call the [DescribeAllGroups](~~DescribeAllGroups~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.group_id_list = group_id_list
        # The IP address of the access source.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id_list is not None:
            result['GroupIdList'] = self.group_id_list

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIdList') is not None:
            self.group_id_list = m.get('GroupIdList')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

