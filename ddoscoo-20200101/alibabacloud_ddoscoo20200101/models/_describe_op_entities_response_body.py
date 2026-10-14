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
        # The operation log records.
        self.op_entities = op_entities
        # The ID of the request.
        self.request_id = request_id
        # The total number of operation records.
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
        # - **1**: IP Address of Anti-DDoS Proxy instance
        # - **2**: Anti-DDoS Pro and Anti-DDoS Premium mitigation plan
        # - **3**: ECS instance
        # - **4**: full logs
        self.entity_type = entity_type
        # The time when the operation was performed. This value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The Alibaba Cloud account ID that performed the operation.
        self.op_account = op_account
        # The type of the operation. Valid values:
        # - **1**: Settings for the burstable protection bandwidth.
        # - **5**: Offset with an anti-DDoS mitigation plan.
        # - **8**: Change an ECS IP address.
        # - **9**: Unblock (deactivation of blackhole filtering).
        # - **10**: Settings for near-origin traffic diversion.
        # - **11**: Clear full logs.
        # - **12**: Downgrade instance specifications. This indicates that the burstable protection bandwidth is reduced when the instance expires or the account has an overdue payment.
        # - **13**: Recover instance specifications. This indicates that the burstable protection bandwidth is recovered when the instance renewal is completed or the overdue payment is settled.
        self.op_action = op_action
        # The description of the operation, expressed as a JSON format character string with the following structure:
        # 
        # - **newEntity**: String. The parameters after the operation.
        # - **oldEntity**: String. The parameters before the operation.
        # 
        # Both **newEntity** and **oldEntity** are expressed as JSON format character strings. The operation parameters vary based on the operation type (**OpAction**).
        # 
        # When **OpAction** is **1**, **12**, or **13**, the operation parameters have the following structure:
        # - **elasticBandwidth**: Integer. The burstable protection bandwidth. Unit: Gbit/s.
        # 
        #     Example: `{"newEntity":{"elasticBandwidth":300},"oldEntity":{"elasticBandwidth":300}}`
        # 
        # 
        # When **OpAction** is **5**, the operation parameters have the following structure:
        # - **bandwidth**: Integer. The burstable protection bandwidth. Unit: Gbit/s.
        # - **count**: Integer. The number of anti-DDoS mitigation plans.
        # - **deductCount**: Integer. The number of offset anti-DDoS mitigation plans.
        # - **expireTime**: Long. The expiration time of the anti-DDoS mitigation plan. This value is a UNIX timestamp. Unit: milliseconds.
        # - **instanceId**: String. The instance ID of the Anti-DDoS Pro and Anti-DDoS Premium instance.
        # - **peakFlow**: Integer. The peak traffic. Unit: bit/s.
        # 
        #     Example: `{"newEntity":{"bandwidth":100,"count":4,"deductCount":1,"expireTime":1616299196000,"instanceId":"ddoscoo-cn-v641kpmq****","peakFlow":751427000}}`
        # 
        # 
        # When **OpAction** is **8**, the operation parameters have the following structure:
        # - **instanceId**: String. The instance ID of the ECS instance whose IP address is changed.
        # 
        #     Example: `{"newEntity":{"instanceId":"i-wz9h6nc313zptbqn****"}}`	
        # 	
        # 
        # When **OpAction** is **9**, the operation parameters have the following structure:
        # - **actionMethod**: String. The operation method. Value: **undo**, which indicates Unblock (deactivation of blackhole filtering).
        # 
        #     Example: `{"newEntity":{"actionMethod":"undo"}}`	
        # 	
        # 
        # When **OpAction** is **10**, the operation parameters have the following structure:
        # - **actionMethod**: String. The operation method. Valid values:
        #     - **do**: Enable near-origin traffic diversion.
        #     - **undo**: Disable near-origin traffic diversion.
        # - **lines**: Array. The line types. Valid values:
        #     - **ct**: China Telecom outside China line
        #     - **cut**: China Unicom outside China line
        # 
        #     Example: `{"newEntity":{"actionMethod":"undo","lines":["ct"]}}`
        # 
        # 
        # When **OpAction** is **11**, there are no operation parameters and the operation description is empty.
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

