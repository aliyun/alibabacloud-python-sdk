# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTotalStatisticsRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
        group_id: int = None,
        remark: str = None,
    ):
        # The source of data. Default value: **aqs**. Valid values:
        # 
        # *   **sas**: Security Center
        # *   **aqs**: Server Guard
        self.from_ = from_
        # The ID of the asset group.
        # 
        # > You can call the [DescribeAllGroups](https://help.aliyun.com/document_detail/130972.html) operation to query the IDs of asset groups.
        self.group_id = group_id
        # The name or public IP address of the asset.
        self.remark = remark

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

