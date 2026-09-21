# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddPublishBatchRequest(DaraModel):
    def __init__(
        self,
        batch_name: str = None,
        interval: int = None,
        operation_base: int = None,
        upgrade_version: str = None,
    ):
        # The name of the release batch.
        # 
        # This parameter is required.
        self.batch_name = batch_name
        # The interval between release batches.
        # 
        # This parameter is required.
        self.interval = interval
        # The dimension for asset selection. Valid values:
        # 
        # - **0**: server instance
        # - **1**: server group
        # - **2**: VPC-connected instance ID
        self.operation_base = operation_base
        # The target version to which you want to upgrade.
        # 
        # This parameter is required.
        self.upgrade_version = upgrade_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_name is not None:
            result['BatchName'] = self.batch_name

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.operation_base is not None:
            result['OperationBase'] = self.operation_base

        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchName') is not None:
            self.batch_name = m.get('BatchName')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OperationBase') is not None:
            self.operation_base = m.get('OperationBase')

        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')

        return self

