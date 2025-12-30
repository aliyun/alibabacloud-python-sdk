# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteBizMetricRequest(DaraModel):
    def __init__(
        self,
        delete_biz_metric_command: main_models.DeleteBizMetricRequestDeleteBizMetricCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.delete_biz_metric_command = delete_biz_metric_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.delete_biz_metric_command:
            self.delete_biz_metric_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_biz_metric_command is not None:
            result['DeleteBizMetricCommand'] = self.delete_biz_metric_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteBizMetricCommand') is not None:
            temp_model = main_models.DeleteBizMetricRequestDeleteBizMetricCommand()
            self.delete_biz_metric_command = temp_model.from_map(m.get('DeleteBizMetricCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class DeleteBizMetricRequestDeleteBizMetricCommand(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

