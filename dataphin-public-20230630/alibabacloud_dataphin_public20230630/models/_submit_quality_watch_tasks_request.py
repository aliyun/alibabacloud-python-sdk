# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SubmitQualityWatchTasksRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        submit_command: main_models.SubmitQualityWatchTasksRequestSubmitCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.submit_command = submit_command

    def validate(self):
        if self.submit_command:
            self.submit_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.submit_command is not None:
            result['SubmitCommand'] = self.submit_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('SubmitCommand') is not None:
            temp_model = main_models.SubmitQualityWatchTasksRequestSubmitCommand()
            self.submit_command = temp_model.from_map(m.get('SubmitCommand'))

        return self

class SubmitQualityWatchTasksRequestSubmitCommand(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        partition_expression: str = None,
        watch_id_list: List[int] = None,
    ):
        self.biz_date = biz_date
        self.partition_expression = partition_expression
        # This parameter is required.
        self.watch_id_list = watch_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.partition_expression is not None:
            result['PartitionExpression'] = self.partition_expression

        if self.watch_id_list is not None:
            result['WatchIdList'] = self.watch_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('PartitionExpression') is not None:
            self.partition_expression = m.get('PartitionExpression')

        if m.get('WatchIdList') is not None:
            self.watch_id_list = m.get('WatchIdList')

        return self

