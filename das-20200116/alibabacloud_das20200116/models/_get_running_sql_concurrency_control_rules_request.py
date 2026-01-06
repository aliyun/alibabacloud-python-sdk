# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRunningSqlConcurrencyControlRulesRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The instance ID.
        # 
        # >  You must specify this parameter only if your database instance is an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. The value must be a positive integer. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. The value must be a positive integer. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

