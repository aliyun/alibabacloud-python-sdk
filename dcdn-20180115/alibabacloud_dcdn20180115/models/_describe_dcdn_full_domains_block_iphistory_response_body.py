# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnFullDomainsBlockIPHistoryResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        description: str = None,
        ipblock_info: List[main_models.DescribeDcdnFullDomainsBlockIPHistoryResponseBodyIPBlockInfo] = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # The value of Code is not 0 in the following scenarios:
        # 
        # *   The format of the IP address is invalid.
        # *   The format of the time is invalid.
        # *   Other abnormal scenarios
        self.code = code
        # The description of the status returned.
        self.description = description
        # The result of the operation.
        self.ipblock_info = ipblock_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ipblock_info:
            for v1 in self.ipblock_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        result['IPBlockInfo'] = []
        if self.ipblock_info is not None:
            for k1 in self.ipblock_info:
                result['IPBlockInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.ipblock_info = []
        if m.get('IPBlockInfo') is not None:
            for k1 in m.get('IPBlockInfo'):
                temp_model = main_models.DescribeDcdnFullDomainsBlockIPHistoryResponseBodyIPBlockInfo()
                self.ipblock_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnFullDomainsBlockIPHistoryResponseBodyIPBlockInfo(DaraModel):
    def __init__(
        self,
        block_ip: str = None,
        block_interval: str = None,
        deliver_time: str = None,
        operation_type: str = None,
        status: str = None,
        update_type: str = None,
    ):
        # The blocked IP address or CIDR block.
        self.block_ip = block_ip
        self.block_interval = block_interval
        # The delivery time.
        self.deliver_time = deliver_time
        self.operation_type = operation_type
        # The delivery status.
        # 
        # *   Success
        # *   Failed
        self.status = status
        self.update_type = update_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_ip is not None:
            result['BlockIP'] = self.block_ip

        if self.block_interval is not None:
            result['BlockInterval'] = self.block_interval

        if self.deliver_time is not None:
            result['DeliverTime'] = self.deliver_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.status is not None:
            result['Status'] = self.status

        if self.update_type is not None:
            result['UpdateType'] = self.update_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockIP') is not None:
            self.block_ip = m.get('BlockIP')

        if m.get('BlockInterval') is not None:
            self.block_interval = m.get('BlockInterval')

        if m.get('DeliverTime') is not None:
            self.deliver_time = m.get('DeliverTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')

        return self

