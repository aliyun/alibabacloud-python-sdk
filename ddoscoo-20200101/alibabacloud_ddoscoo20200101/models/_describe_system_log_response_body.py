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
        # An array that consists of details of the billing logs for the burstable clean bandwidth.
        self.system_log = system_log
        # The total number of billing logs for the burstable clean bandwidth.
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
        # The IP address of the instance.
        self.entity_object = entity_object
        # The type of the system log. The value is fixed as **20**, which indicates the billing logs for burstable clean bandwidth.
        self.entity_type = entity_type
        # The time when the bill was generated. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The time when the bill was last modified. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the Alibaba Cloud account to which the bill belongs.
        self.op_account = op_account
        # The operation type. The value is fixed as **100**, which indicates the billing logs for the burstable clean bandwidth that you increased.
        self.op_action = op_action
        # The details of the bill. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **newEntity**: the bill record, which contains the following fields. Data type: object.
        # 
        #     *   **billValue**: the usage of the burstable clean bandwidth within a month. Unit: Mbit/s. Data type: integer.
        #     *   **instanceId**: the ID of the instance. Data type: string.
        #     *   **ip**: the IP address of the instance. Data type: string.
        #     *   **maxBw**: the peak service traffic (monthly 95th percentile bandwidth) within a month. Unit: Mbit/s. Data type: string.
        #     *   **month**: the month in which the bill of the previous calendar month is issued. This value is a UNIX timestamp. Unit: milliseconds. Data type: long.
        #     *   **overBandwidth**: the peak service traffic minus the clean bandwidth of the instance. Unit: Mbit/s. Data type: integer.
        #     *   **peakTime**: the time in point of the peak service traffic that is measured for billing. This value is a UNIX timestamp. Unit: seconds. Data type: long.
        #     *   **startTimestamp**: the beginning of the time range for the peak service traffic range. This value is a UNIX timestamp. Unit: seconds. Data type: long.
        self.op_desc = op_desc
        # The status of the bill. Valid values:
        # 
        # *   **0**: to be billed
        # *   **1**: billed
        # *   **2**: terminated
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

