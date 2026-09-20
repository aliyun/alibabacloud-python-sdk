# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceMaintainTimeRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
    ):
        # The ID of the instance for which you want to modify the O&M window. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The end time of the instance O&M window. Specify the time in the HH:mmZ format in UTC.
        # 
        # This parameter is required.
        self.maintain_end_time = maintain_end_time
        # The start time of the instance O&M window. Specify the time in the HH:mmZ format in UTC.
        # 
        # This parameter is required.
        self.maintain_start_time = maintain_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        return self

