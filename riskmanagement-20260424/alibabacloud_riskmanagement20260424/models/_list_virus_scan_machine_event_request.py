# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVirusScanMachineEventRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        operate_task_id: str = None,
        page_size: int = None,
        region_id: str = None,
        uuid: str = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.operate_task_id = operate_task_id
        self.page_size = page_size
        self.region_id = region_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operate_task_id is not None:
            result['OperateTaskId'] = self.operate_task_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OperateTaskId') is not None:
            self.operate_task_id = m.get('OperateTaskId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

