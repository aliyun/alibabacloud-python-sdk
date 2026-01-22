# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBInstanceConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        config_value: str = None,
        db_instance_name: str = None,
    ):
        self.config_name = config_name
        self.config_value = config_value
        self.db_instance_name = db_instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.config_value is not None:
            result['ConfigValue'] = self.config_value

        if self.db_instance_name is not None:
            result['DbInstanceName'] = self.db_instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('ConfigValue') is not None:
            self.config_value = m.get('ConfigValue')

        if m.get('DbInstanceName') is not None:
            self.db_instance_name = m.get('DbInstanceName')

        return self

