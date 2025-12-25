# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CalculateDBInstanceWeightResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.CalculateDBInstanceWeightResponseBodyItems = None,
        request_id: str = None,
    ):
        # An array that consists of information about the system-assigned read weight.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.CalculateDBInstanceWeightResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CalculateDBInstanceWeightResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance_weight: List[main_models.CalculateDBInstanceWeightResponseBodyItemsDBInstanceWeight] = None,
    ):
        self.dbinstance_weight = dbinstance_weight

    def validate(self):
        if self.dbinstance_weight:
            for v1 in self.dbinstance_weight:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceWeight'] = []
        if self.dbinstance_weight is not None:
            for k1 in self.dbinstance_weight:
                result['DBInstanceWeight'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_weight = []
        if m.get('DBInstanceWeight') is not None:
            for k1 in m.get('DBInstanceWeight'):
                temp_model = main_models.CalculateDBInstanceWeightResponseBodyItemsDBInstanceWeight()
                self.dbinstance_weight.append(temp_model.from_map(k1))

        return self

class CalculateDBInstanceWeightResponseBodyItemsDBInstanceWeight(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbinstance_type: str = None,
        readonly_instance_sqldelayed_time: str = None,
        weight: str = None,
    ):
        # The instance ID
        self.dbinstance_id = dbinstance_id
        # The type of the instance. Valid values:
        # 
        # *   **Master**: primary instance
        # *   **Readonly**: read-only instance
        self.dbinstance_type = dbinstance_type
        # The latency at which the read-only instances replicate data. The read-only instances replicate data from the primary instance at the latency that is specified by the **ReadonlyInstanceSQLDelayedTime** parameter. Unit: seconds.
        self.readonly_instance_sqldelayed_time = readonly_instance_sqldelayed_time
        # The read weight that the system calculates in real time for the instance.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.readonly_instance_sqldelayed_time is not None:
            result['ReadonlyInstanceSQLDelayedTime'] = self.readonly_instance_sqldelayed_time

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('ReadonlyInstanceSQLDelayedTime') is not None:
            self.readonly_instance_sqldelayed_time = m.get('ReadonlyInstanceSQLDelayedTime')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

