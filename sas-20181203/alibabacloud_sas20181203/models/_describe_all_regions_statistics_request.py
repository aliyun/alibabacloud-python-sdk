# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAllRegionsStatisticsRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        group_id: int = None,
        remark: str = None,
        source_ip: str = None,
    ):
        # The source of the request. Default value: **aqs**. Valid values:
        # 
        # *   **sas**: Security Center.
        # *   **aqs**: Server Guard.
        self.from_ = from_
        # The ID of the asset group that you want to query.
        # 
        # >  You can call the [DescribeAllGroups](https://help.aliyun.com/document_detail/130972.html) operation to query the ID.
        self.group_id = group_id
        # The name or public IP address of the asset.
        self.remark = remark
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

