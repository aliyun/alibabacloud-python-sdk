# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePublishGroupTaskRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        order_id: int = None,
        plan_time: str = None,
        publish_strategy: str = None,
        tid: int = None,
    ):
        # The ID of the database for which the schema design is executed.
        # 
        # This parameter is required.
        self.db_id = db_id
        # Indicates whether the database is a logical database.
        # 
        # This parameter is required.
        self.logic = logic
        # The ID of the ticket.
        # 
        # > : You can create a schema design ticket in the DMS console. For more information, see [Design schemas](https://help.aliyun.com/document_detail/69711.html). You can also create a schema design ticket by calling the [CreateOrder](https://help.aliyun.com/document_detail/144649.html) operation and obtain the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The time to execute the schema design ticket.
        self.plan_time = plan_time
        # The policy to execute the schema design ticket. Valid values:
        # 
        # *   IMMEDIATELY: immediately executes the schema design ticket.
        # *   REGULARLY: executes the schema design ticket at a scheduled time.
        # 
        # This parameter is required.
        self.publish_strategy = publish_strategy
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, log on to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time

        if self.publish_strategy is not None:
            result['PublishStrategy'] = self.publish_strategy

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')

        if m.get('PublishStrategy') is not None:
            self.publish_strategy = m.get('PublishStrategy')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

