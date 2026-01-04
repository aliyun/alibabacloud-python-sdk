# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeOpEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        op_entities: List[main_models.DescribeOpEntitiesResponseBodyOpEntities] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The operation records.
        self.op_entities = op_entities
        # The request ID.
        self.request_id = request_id
        # The total number of returned operation records.
        self.total_count = total_count

    def validate(self):
        if self.op_entities:
            for v1 in self.op_entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OpEntities'] = []
        if self.op_entities is not None:
            for k1 in self.op_entities:
                result['OpEntities'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.op_entities = []
        if m.get('OpEntities') is not None:
            for k1 in m.get('OpEntities'):
                temp_model = main_models.DescribeOpEntitiesResponseBodyOpEntities()
                self.op_entities.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOpEntitiesResponseBodyOpEntities(DaraModel):
    def __init__(
        self,
        entity_object: str = None,
        entity_type: int = None,
        gmt_create: int = None,
        op_account: str = None,
        op_action: int = None,
        op_desc: str = None,
    ):
        # The operation object.
        self.entity_object = entity_object
        # The type of the operation object. Valid values:
        # 
        # *   **1**: the IP address of the Anti-DDoS Proxy instance.
        # *   **2**: Anti-DDoS plans.
        # *   **3**: ECS instances.
        # *   **4**: all logs.
        self.entity_type = entity_type
        # The time when the operation was performed. The value is a UNIX timestamp. Units: milliseconds.
        self.gmt_create = gmt_create
        # The ID of the Alibaba Cloud account that is used to perform the operation.
        self.op_account = op_account
        # The type of the operation. Valid values:
        # 
        # *   **1**: configuring burstable protection bandwidth.
        # *   **5**: using Anti-DDoS plans.
        # *   **8**: changing the IP addresses of ECS instances.
        # *   **9**: deactivating blackhole filtering.
        # *   **10**: configuring the near-origin traffic diversion feature.
        # *   **11**: clearing all logs.
        # *   **12**: downgrading the specifications of the Anti-DDoS Proxy instance. If the instance expires or the account has overdue payments, this operation is performed to downgrade the burstable protection bandwidth.
        # *   **13**: restoring the specifications of the Anti-DDoS Proxy instance. If the instance is renewed or you have paid the overdue payments within your account, this operation is performed to restore the burstable protection bandwidth.
        self.op_action = op_action
        # The details of the operation. This parameter is a JSON string. The string contains the following fields:
        # 
        # *   **newEntity**: the values of the parameters after the operation. This field is of the string type.
        # *   **oldEntity**: the values of the parameters before the operation. This field is of the string type.
        # 
        # Both **newEntity** and **oldEntity** are JSON strings. The returned parameters vary based on **OpAction**.
        # 
        # If the value of **OpAction** is **1**, **12**, or **13**, the following parameter is returned:
        # 
        # *   **elasticBandwidth**: the burstable protection bandwidth. This parameter is of the integer type. Unit: Gbit/s.
        # 
        #     Example: `{"newEntity":{"elasticBandwidth":300},"oldEntity":{"elasticBandwidth":300}}`
        # 
        # If the value of **OpAction** is **5**, the following parameters are returned:
        # 
        # *   **bandwidth**: the burstable protection bandwidth. The parameter is of the integer type. Unit: Gbit/s.
        # 
        # *   **count**: the number of Anti-DDoS plans. This parameter is of the integer type.
        # 
        # *   **deductCount**: the number of used Anti-DDoS plans. This parameter is of the integer type.
        # 
        # *   **expireTime**: the expiration time of the Anti-DDoS plans. This parameter is of the long type. The value is a UNIX timestamp. Units: milliseconds.
        # 
        # *   **instanceId**: the ID of the Anti-DDoS Proxy instance. This parameter is of the string type.
        # 
        # *   **peakFlow**: the peak throughput on the Anti-DDoS Proxy instance. This parameter is of the integer type. Unit: bit/s.
        # 
        #     Example: `{"newEntity":{"bandwidth":100,"count":4,"deductCount":1,"expireTime":1616299196000,"instanceId":"ddoscoo-cn-v641kpmq****","peakFlow":751427000}}`
        # 
        # If the value of **OpAction** is **8**, the following parameter is returned:
        # 
        # *   **instanceId**: the IDs of the ECS instances whose IP addresses are changed. This parameter is of the string type.
        # 
        #     Example: `{"newEntity":{"instanceId":"i-wz9h6nc313zptbqn****"}}`
        # 
        # If the value of **OpAction** is **9**, the following parameter is returned:
        # 
        # *   **actionMethod**: the operation method. This parameter is of the string type. Valid value: **undo**, which indicates that you deactivated blackhole filtering.
        # 
        #     Example: `{"newEntity":{"actionMethod":"undo"}}`
        # 
        # If the value of **OpAction** is **10**, the following parameters are returned:
        # 
        # *   **actionMethod**: the operation method. This parameter is of the string type. Valid values:
        # 
        #     *   **do**: The near-origin traffic diversion feature is enabled.
        #     *   **undo**: The near-origin traffic diversion feature is disabled.
        # 
        # *   **lines**: the Internet service provider (ISP) line from which the traffic is blocked. This parameter is of the array type. Valid values:
        # 
        #     *   **ct**: China Telecom (International).
        #     *   **cut**: China Unicom (International).
        # 
        #     Example: `{"newEntity":{"actionMethod":"undo","lines":["ct"]}}`
        # 
        # If the value of **OpAction** is **11**, no parameter is returned, and the description is empty.
        self.op_desc = op_desc

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

        if self.op_account is not None:
            result['OpAccount'] = self.op_account

        if self.op_action is not None:
            result['OpAction'] = self.op_action

        if self.op_desc is not None:
            result['OpDesc'] = self.op_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityObject') is not None:
            self.entity_object = m.get('EntityObject')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('OpAccount') is not None:
            self.op_account = m.get('OpAccount')

        if m.get('OpAction') is not None:
            self.op_action = m.get('OpAction')

        if m.get('OpDesc') is not None:
            self.op_desc = m.get('OpDesc')

        return self

