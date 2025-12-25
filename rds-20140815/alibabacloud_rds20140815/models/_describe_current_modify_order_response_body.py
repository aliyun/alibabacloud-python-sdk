# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeCurrentModifyOrderResponseBody(DaraModel):
    def __init__(
        self,
        modify_order: List[main_models.DescribeCurrentModifyOrderResponseBodyModifyOrder] = None,
        request_id: str = None,
    ):
        # The specification change order.
        self.modify_order = modify_order
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.modify_order:
            for v1 in self.modify_order:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModifyOrder'] = []
        if self.modify_order is not None:
            for k1 in self.modify_order:
                result['ModifyOrder'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modify_order = []
        if m.get('ModifyOrder') is not None:
            for k1 in m.get('ModifyOrder'):
                temp_model = main_models.DescribeCurrentModifyOrderResponseBodyModifyOrder()
                self.modify_order.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCurrentModifyOrderResponseBodyModifyOrder(DaraModel):
    def __init__(
        self,
        class_group: str = None,
        cpu: str = None,
        db_instance_id: str = None,
        effective_time: str = None,
        mark: str = None,
        memory_class: str = None,
        status: str = None,
        storage: str = None,
        target_dbinstance_class: str = None,
    ):
        # The instance family of the instance.
        self.class_group = class_group
        # The number of CPU cores that are supported by the instance type. Unit: cores.
        self.cpu = cpu
        # The instance ID.
        self.db_instance_id = db_instance_id
        # The effective time. Valid values:
        # 
        # *   **Immediate**: This is the default value.
        # *   **MaintainTime**: The effective time is within the maintenance window. For more information, see [ModifyDBInstanceMaintainTime](https://help.aliyun.com/document_detail/610402.html).
        self.effective_time = effective_time
        # The description of the instance.
        self.mark = mark
        # The memory capacity that is supported by the instance type. Unit: GB.
        self.memory_class = memory_class
        # The status of the task.
        self.status = status
        # The storage capacity of the instance.
        self.storage = storage
        # The new instance type of the instance. Valid values:
        self.target_dbinstance_class = target_dbinstance_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_group is not None:
            result['ClassGroup'] = self.class_group

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.mark is not None:
            result['Mark'] = self.mark

        if self.memory_class is not None:
            result['MemoryClass'] = self.memory_class

        if self.status is not None:
            result['Status'] = self.status

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.target_dbinstance_class is not None:
            result['TargetDBInstanceClass'] = self.target_dbinstance_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassGroup') is not None:
            self.class_group = m.get('ClassGroup')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('Mark') is not None:
            self.mark = m.get('Mark')

        if m.get('MemoryClass') is not None:
            self.memory_class = m.get('MemoryClass')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('TargetDBInstanceClass') is not None:
            self.target_dbinstance_class = m.get('TargetDBInstanceClass')

        return self

