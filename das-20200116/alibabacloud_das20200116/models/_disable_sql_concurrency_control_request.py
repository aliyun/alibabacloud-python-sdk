# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableSqlConcurrencyControlRequest(DaraModel):
    def __init__(
        self,
        console_context: str = None,
        instance_id: str = None,
        item_id: int = None,
    ):
        # The reserved parameter.
        self.console_context = console_context
        # The instance ID.
        # 
        # >  The database instance must be an ApsaraDB RDS for MySQL instance or a PolarDB for MySQL cluster.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the throttling rule that is applied to the instance. You can call the [GetRunningSqlConcurrencyControlRules](https://help.aliyun.com/document_detail/223538.html) operation to query the ID.
        # 
        # This parameter is required.
        self.item_id = item_id

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

        if self.item_id is not None:
            result['ItemId'] = self.item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        return self

