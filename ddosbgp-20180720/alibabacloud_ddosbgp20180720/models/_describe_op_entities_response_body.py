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
        # The list of Operation logs details.
        self.op_entities = op_entities
        # The ID of the request.
        self.request_id = request_id
        # The total number of queried operation logs.
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
        # The operation object, which is the ID of the Anti-DDoS Origin instance.
        self.entity_object = entity_object
        # The object type of the operation. The value is fixed as **1**, which indicates an Anti-DDoS Origin instance.
        self.entity_type = entity_type
        # The time when the log was created. The value is a UNIX timestamp in milliseconds.
        self.gmt_create = gmt_create
        # The Alibaba Cloud account ID used to execute the operation.
        # 
        # > If the value is **system**, the Anti-DDoS Origin service will automatically execute the operation.
        self.op_account = op_account
        # The operation type. Valid values:
        # 
        # - **3**: add protected IP addresses to the Anti-DDoS Origin instance
        # - **4**: unbind protected IP addresses from the Anti-DDoS Origin instance
        # - **5**: downgrade the Anti-DDoS Origin instance
        # - **6**: deactivate blackhole filtering
        # - **7**: reset the quota on blackhole filtering deactivation
        # - **8**: resume burstable protection
        self.op_action = op_action
        # The operation details. Use a JSON struct to transform the data into a character string representation. The JSON structure contains the following fields:
        # 
        # - **entity**: Object | The operation object. The fields contained in **entity** vary based on the operation type (**OpAction**). Details:
        # 
        #     - If **OpAction** is **3** (add protected IP addresses), **entity** contains the following fields:
        #         - **ips**: Array | The list of assets that are assigned public IP addresses that are attached to the Anti-DDoS Origin instance for protection.
        # 
        #     - If **OpAction** is **4** (unbind protected IP addresses), **entity** contains the following fields:
        #         - **ips**: Array | The list of assets that are assigned public IP addresses that are unbound from the Anti-DDoS Origin instance.
        # 
        #     - If **OpAction** is **5** (decrease the quota of the instance), **entity** contains the following fields:
        #         - **baseBandwidth**: Integer | The basic protection bandwidth. Unit: Gbit/s.
        #         - **elasticBandwidth**: Integer | The burstable protection bandwidth. Unit: Gbit/s.
        #         - **opSource**: Integer | The source of the operation. The value is fixed as **1**, which indicates that the Anti-DDoS Origin service will automatically execute the operation.
        # 
        #     - If **OpAction** is **6** (deactivate blackhole filtering), **entity** contains the following fields:
        #         - **ips**: Array | The list of assets that are assigned public IP addresses for which the blackhole filtering status is deactivated.
        # 
        #     - If **OpAction** is **7** (Reset quota on blackhole filtering deactivation), **entity** is empty.
        # 
        #     - If **OpAction** is **8** (recover burstable protection), **entity** contains the following fields:
        #         - **baseBandwidth**: Integer | The basic protection bandwidth. Unit: Gbit/s.
        #         - **elasticBandwidth**: Integer | The burstable protection bandwidth. Unit: Gbit/s.
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

