# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeReadDBInstanceDelayResponseBody(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        delay_time: int = None,
        items: main_models.DescribeReadDBInstanceDelayResponseBodyItems = None,
        read_dbinstance_id: str = None,
        request_id: str = None,
    ):
        # The primary instance ID.
        self.dbinstance_id = dbinstance_id
        # The latency of data replication. Unit: seconds.
        self.delay_time = delay_time
        # The latency information.
        self.items = items
        # The read-only instance ID.
        self.read_dbinstance_id = read_dbinstance_id
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.read_dbinstance_id is not None:
            result['ReadDBInstanceId'] = self.read_dbinstance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeReadDBInstanceDelayResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('ReadDBInstanceId') is not None:
            self.read_dbinstance_id = m.get('ReadDBInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeReadDBInstanceDelayResponseBodyItems(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeReadDBInstanceDelayResponseBodyItemsItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeReadDBInstanceDelayResponseBodyItemsItems()
                self.items.append(temp_model.from_map(k1))

        return self

class DescribeReadDBInstanceDelayResponseBodyItemsItems(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        read_dbinstance_names: main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadDBInstanceNames = None,
        read_delay_times: main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadDelayTimes = None,
        readonly_instance_delay: main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadonlyInstanceDelay = None,
    ):
        # The primary instance ID.
        self.dbinstance_id = dbinstance_id
        # An array that consists of information about the read-only instance.
        self.read_dbinstance_names = read_dbinstance_names
        # The latency of data replication.
        self.read_delay_times = read_delay_times
        # The information about the write-ahead log (WAL) latency.
        # 
        # >  This parameter is returned only when the primary instance runs PostgreSQL.
        self.readonly_instance_delay = readonly_instance_delay

    def validate(self):
        if self.read_dbinstance_names:
            self.read_dbinstance_names.validate()
        if self.read_delay_times:
            self.read_delay_times.validate()
        if self.readonly_instance_delay:
            self.readonly_instance_delay.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.read_dbinstance_names is not None:
            result['ReadDBInstanceNames'] = self.read_dbinstance_names.to_map()

        if self.read_delay_times is not None:
            result['ReadDelayTimes'] = self.read_delay_times.to_map()

        if self.readonly_instance_delay is not None:
            result['ReadonlyInstanceDelay'] = self.readonly_instance_delay.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ReadDBInstanceNames') is not None:
            temp_model = main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadDBInstanceNames()
            self.read_dbinstance_names = temp_model.from_map(m.get('ReadDBInstanceNames'))

        if m.get('ReadDelayTimes') is not None:
            temp_model = main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadDelayTimes()
            self.read_delay_times = temp_model.from_map(m.get('ReadDelayTimes'))

        if m.get('ReadonlyInstanceDelay') is not None:
            temp_model = main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadonlyInstanceDelay()
            self.readonly_instance_delay = temp_model.from_map(m.get('ReadonlyInstanceDelay'))

        return self

class DescribeReadDBInstanceDelayResponseBodyItemsItemsReadonlyInstanceDelay(DaraModel):
    def __init__(
        self,
        readonly_instance_delay: List[main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadonlyInstanceDelayReadonlyInstanceDelay] = None,
    ):
        self.readonly_instance_delay = readonly_instance_delay

    def validate(self):
        if self.readonly_instance_delay:
            for v1 in self.readonly_instance_delay:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReadonlyInstanceDelay'] = []
        if self.readonly_instance_delay is not None:
            for k1 in self.readonly_instance_delay:
                result['ReadonlyInstanceDelay'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.readonly_instance_delay = []
        if m.get('ReadonlyInstanceDelay') is not None:
            for k1 in m.get('ReadonlyInstanceDelay'):
                temp_model = main_models.DescribeReadDBInstanceDelayResponseBodyItemsItemsReadonlyInstanceDelayReadonlyInstanceDelay()
                self.readonly_instance_delay.append(temp_model.from_map(k1))

        return self

class DescribeReadDBInstanceDelayResponseBodyItemsItemsReadonlyInstanceDelayReadonlyInstanceDelay(DaraModel):
    def __init__(
        self,
        flush_lag: str = None,
        flush_latency: str = None,
        read_dbinstance_name: str = None,
        replay_lag: str = None,
        replay_latency: str = None,
        send_latency: str = None,
        write_lag: str = None,
        write_latency: str = None,
    ):
        # The duration that is allowed for the latency in the persistence of WAL data. Unit: seconds.
        self.flush_lag = flush_lag
        # The data size that is allowed for the latency in the persistence of WAL data. Unit: MB.
        self.flush_latency = flush_latency
        # The read-only instance ID.
        self.read_dbinstance_name = read_dbinstance_name
        # The duration that is allowed for the latency in the playback of WAL data. Unit: seconds.
        self.replay_lag = replay_lag
        # The data size that is allowed for the latency in the playback of WAL data. Unit: MB.
        self.replay_latency = replay_latency
        # The data size that is allowed for the latency in the sending of WAL data. Unit: MB.
        self.send_latency = send_latency
        # The duration that is allowed for the latency in the write-back of WAL data. Unit: seconds.
        self.write_lag = write_lag
        # The data size that is allowed for the latency in the write-back of WAL data. Unit: MB.
        self.write_latency = write_latency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flush_lag is not None:
            result['FlushLag'] = self.flush_lag

        if self.flush_latency is not None:
            result['FlushLatency'] = self.flush_latency

        if self.read_dbinstance_name is not None:
            result['ReadDBInstanceName'] = self.read_dbinstance_name

        if self.replay_lag is not None:
            result['ReplayLag'] = self.replay_lag

        if self.replay_latency is not None:
            result['ReplayLatency'] = self.replay_latency

        if self.send_latency is not None:
            result['SendLatency'] = self.send_latency

        if self.write_lag is not None:
            result['WriteLag'] = self.write_lag

        if self.write_latency is not None:
            result['WriteLatency'] = self.write_latency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlushLag') is not None:
            self.flush_lag = m.get('FlushLag')

        if m.get('FlushLatency') is not None:
            self.flush_latency = m.get('FlushLatency')

        if m.get('ReadDBInstanceName') is not None:
            self.read_dbinstance_name = m.get('ReadDBInstanceName')

        if m.get('ReplayLag') is not None:
            self.replay_lag = m.get('ReplayLag')

        if m.get('ReplayLatency') is not None:
            self.replay_latency = m.get('ReplayLatency')

        if m.get('SendLatency') is not None:
            self.send_latency = m.get('SendLatency')

        if m.get('WriteLag') is not None:
            self.write_lag = m.get('WriteLag')

        if m.get('WriteLatency') is not None:
            self.write_latency = m.get('WriteLatency')

        return self

class DescribeReadDBInstanceDelayResponseBodyItemsItemsReadDelayTimes(DaraModel):
    def __init__(
        self,
        read_delay_time: List[str] = None,
    ):
        self.read_delay_time = read_delay_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.read_delay_time is not None:
            result['ReadDelayTime'] = self.read_delay_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadDelayTime') is not None:
            self.read_delay_time = m.get('ReadDelayTime')

        return self

class DescribeReadDBInstanceDelayResponseBodyItemsItemsReadDBInstanceNames(DaraModel):
    def __init__(
        self,
        read_dbinstance_name: List[str] = None,
    ):
        self.read_dbinstance_name = read_dbinstance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.read_dbinstance_name is not None:
            result['ReadDBInstanceName'] = self.read_dbinstance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadDBInstanceName') is not None:
            self.read_dbinstance_name = m.get('ReadDBInstanceName')

        return self

