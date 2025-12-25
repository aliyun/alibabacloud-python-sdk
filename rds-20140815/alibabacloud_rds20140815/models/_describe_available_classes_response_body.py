# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableClassesResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_classes: List[main_models.DescribeAvailableClassesResponseBodyDBInstanceClasses] = None,
        request_id: str = None,
    ):
        # An array that consists of the instance types available for the instance.
        self.dbinstance_classes = dbinstance_classes
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dbinstance_classes:
            for v1 in self.dbinstance_classes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceClasses'] = []
        if self.dbinstance_classes is not None:
            for k1 in self.dbinstance_classes:
                result['DBInstanceClasses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_classes = []
        if m.get('DBInstanceClasses') is not None:
            for k1 in m.get('DBInstanceClasses'):
                temp_model = main_models.DescribeAvailableClassesResponseBodyDBInstanceClasses()
                self.dbinstance_classes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableClassesResponseBodyDBInstanceClasses(DaraModel):
    def __init__(
        self,
        dbinstance_class: str = None,
        dbinstance_storage_range: main_models.DescribeAvailableClassesResponseBodyDBInstanceClassesDBInstanceStorageRange = None,
    ):
        # The instance type of the instance.
        self.dbinstance_class = dbinstance_class
        # The storage capacity range that is supported for the instance.
        self.dbinstance_storage_range = dbinstance_storage_range

    def validate(self):
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceStorageRange') is not None:
            temp_model = main_models.DescribeAvailableClassesResponseBodyDBInstanceClassesDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m.get('DBInstanceStorageRange'))

        return self

class DescribeAvailableClassesResponseBodyDBInstanceClassesDBInstanceStorageRange(DaraModel):
    def __init__(
        self,
        max_value: int = None,
        min_value: int = None,
        step: int = None,
    ):
        # The maximum storage capacity that is supported for the instance. Unit: GB.
        self.max_value = max_value
        # The minimum storage capacity that is supported for the instance. Unit: GB.
        self.min_value = min_value
        # The minimum step size at which you can adjust the storage capacity of the instance. The minimum step size is 5 GB.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

