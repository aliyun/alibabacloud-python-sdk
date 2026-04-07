# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunTriggerNodeRequest(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        biz_date: int = None,
        cycle_time: int = None,
        node_id: int = None,
    ):
        # The ID of the DataWorks workspace to which the manually triggered node belongs. You can call the [ListProjects](https://help.aliyun.com/document_detail/178393.html) operation to query the ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The data timestamp of the instance that is generated for the manually triggered node.
        # 
        # This parameter is required.
        self.biz_date = biz_date
        # The scheduling time to run the manually triggered node. Set the value to a 13-digit timestamp in milliseconds.
        # 
        # This parameter is required.
        self.cycle_time = cycle_time
        # The ID of the manually triggered node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the ID.
        # 
        # This parameter is required.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.cycle_time is not None:
            result['CycleTime'] = self.cycle_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('CycleTime') is not None:
            self.cycle_time = m.get('CycleTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

