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
        # The data struct.
        self.data = data
        # The request ID.
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
        # The configuration key.
        self.config_name = config_name
        # The configuration item. The following parameters are included:
        # 
        # - attendHtapList: the list of instances for which HTAP is enabled.
        # - autoAttendHtap: specifies whether to automatically add newly created read-only instances to the HTAP list.
        # - delayExecutionStrategy: when the read-only instance lag reaches the value specified by storageDelayThreshold, read-only traffic is routed back to the primary instance. Default value: 1. Valid values: 0 and 1.
        # - enableConsistentReplicaRead: specifies whether to enable consistent reads.
        # - storageDelayThreshold: the latency threshold for read-only instances. Default value: 3s. Valid values: 0 to 86400.
        # - enableHtap: specifies whether to enable HTAP.
        # - masterReadWeight: the read weight of the primary node. A value of 100 indicates that 100% of traffic is routed to the primary node. Valid values: 0 to 100.
        self.config_value = config_value
        # The instance ID.
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

