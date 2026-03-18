# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeOpEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        op_entities: List[main_models.DescribeOpEntitiesResponseBodyOpEntities] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the operation log.
        self.op_entities = op_entities
        # The ID of the request.
        self.request_id = request_id
        # The total number of operation logs.
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
        # The operation object, which is the ID of the instance.
        self.entity_object = entity_object
        # The type of the operation object. The value is fixed as **1**, which indicates Anti-DDoS Origin instances.
        self.entity_type = entity_type
        # The time when the log was generated. The value is a UNIX timestamp. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The ID of the Alibaba Cloud account that performs the operation.
        # 
        # > If the value is **system**, the operation is performed by Anti-DDoS Origin.
        self.op_account = op_account
        # The type of operation. Valid values:
        # 
        # *   **3**: indicates an operation to add an IP address to the Anti-DDoS Origin instance for protection.
        # *   **4**: indicates an operation to remove a protected IP address from the Anti-DDoS Origin instance.
        # *   **5**: indicates an operation to downgrade the Anti-DDoS Origin instance.
        # *   **6**: indicates an operation to deactivate blackhole filtering for an IP address.
        # *   **7**: indicates an operation to reset the number of times that you can deactivate blackhole filtering.
        # *   **8**: indicates an operation to enable burstable protection.
        self.op_action = op_action
        # The details of the operation. The value is a string that consists of a JSON struct. The JSON struct contains the following fields:
        # 
        # *   **entity**: the operation object. Data type: object. The fields that are included in the value of the **entity** parameter vary based on the value of the **OpAction** parameter. Valid values:
        # 
        #     *   If the value of the **OpAction** parameter is **3**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses that are protected by the Anti-DDoS Origin instance. Data type: array
        # 
        #     *   If the value of the **OpAction** parameter is **4**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses that are no longer protected by the Anti-DDoS Origin instance. Data type: array.
        # 
        #     *   If the value of the **OpAction** parameter is **5**, the value of the **entity** parameter consists of the following fields:
        # 
        #         *   **baseBandwidth**: the basic protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **elasticBandwidth**: the burstable protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **opSource**: the source of the operation. The value is fixed as **1**, indicating that the operation is performed by Anti-DDoS Origin. Data type: integer.
        # 
        #     *   If the value of the **OpAction** parameter is **6**, the value of the **entity** parameter consists of the following field:
        # 
        #         *   **ips**: the public IP addresses for which to deactivate blackhole filtering. Data type: array.
        # 
        #     *   If the value of the **OpAction** parameter is **7**, the **entity** parameter is not returned.
        # 
        #     *   If the value of the **OpAction** parameter is **8**, the value of the **entity** parameter consists of the following fields:
        # 
        #         *   **baseBandwidth**: the basic protection bandwidth. Unit: Gbit/s. Data type: integer.
        #         *   **elasticBandwidth**: the burstable protection bandwidth. Unit: Gbit/s. Data type: integer.
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

