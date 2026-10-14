# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSystemLogResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        system_log: List[main_models.DescribeSystemLogResponseBodySystemLog] = None,
        total: int = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the billing logs for burstable clean bandwidth.
        self.system_log = system_log
        # The total number of billing logs for burstable clean bandwidth that are queried.
        self.total = total

    def validate(self):
        if self.system_log:
            for v1 in self.system_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SystemLog'] = []
        if self.system_log is not None:
            for k1 in self.system_log:
                result['SystemLog'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.system_log = []
        if m.get('SystemLog') is not None:
            for k1 in m.get('SystemLog'):
                temp_model = main_models.DescribeSystemLogResponseBodySystemLog()
                self.system_log.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeSystemLogResponseBodySystemLog(DaraModel):
    def __init__(
        self,
        entity_object: str = None,
        entity_type: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        op_account: str = None,
        op_action: int = None,
        op_desc: str = None,
        status: int = None,
    ):
        # The IP address of the Anti-DDoS instance.
        self.entity_object = entity_object
        # The type of the system log. The value is fixed at **20**, which indicates the billing log of burstable clean bandwidth.
        self.entity_type = entity_type
        # The time when the bill was created. This value is a timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The time when the bill was last modified. This value is a timestamp in milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the Alibaba Cloud account to which the bill belongs.
        self.op_account = op_account
        # The operation type. The value is fixed at **100**, which indicates that a billing record for burstable clean bandwidth is added.
        self.op_action = op_action
        # The details of the bill. This value is a string that is converted from a JSON struct. The JSON struct contains the following fields:
        # 
        # - **newEntity**: Object type, which indicates the bill record and contains the following fields:
        # 
        #   - **billValue**: Integer type | The usage of burstable clean bandwidth in the billing month. Unit: Mbit/s.
        #   - **instanceId**: String type | The ID of the Anti-DDoS instance.
        #   - **ip**: String type | The IP address of the Anti-DDoS instance.
        #   - **maxBw**: String type | The actual peak value of service traffic in the billing month (monthly 95th percentile). Unit: Mbit/s.
        #   - **month**: Long type | The month when the bill is generated (the billing month is the calendar month before the month when the bill is generated). This value is a timestamp in milliseconds.
        #   - **overBandwidth**: Integer type | The bandwidth that exceeds the clean bandwidth specification of the instance. Unit: Mbit/s.
        #   - **peakTime**: Long type | The time when the actual peak value of service traffic is measured. This value is a timestamp in seconds.
        #   - **startTimestamp**: Long type | The start time of the period when the peak value of instance service traffic is measured. This value is a timestamp in seconds.
        self.op_desc = op_desc
        # The status of the bill. Valid values:
        # 
        # - **0**: indicates that the bill is pending.
        # - **1**: indicates that the bill is generated.
        # - **2**: indicates that the bill is terminated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_object is not None:
            result['EntityObject'] = self.entity_object

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.op_account is not None:
            result['OpAccount'] = self.op_account

        if self.op_action is not None:
            result['OpAction'] = self.op_action

        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')

        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')

        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

