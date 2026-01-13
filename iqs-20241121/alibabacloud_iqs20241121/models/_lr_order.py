# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iqs20241121 import models as main_models
from darabonba.model import DaraModel

class LrOrder(DaraModel):
    def __init__(
        self,
        account_credentials: List[main_models.AccountCredentialDTO] = None,
        ali_uid: str = None,
        commodity_code: str = None,
        commodity_id: str = None,
        commodity_spec: str = None,
        customer_name: str = None,
        event_time: str = None,
        expiration_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        order_category: str = None,
        order_id: int = None,
        qps: int = None,
        status: str = None,
    ):
        self.account_credentials = account_credentials
        self.ali_uid = ali_uid
        self.commodity_code = commodity_code
        self.commodity_id = commodity_id
        self.commodity_spec = commodity_spec
        self.customer_name = customer_name
        self.event_time = event_time
        self.expiration_time = expiration_time
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.instance_id = instance_id
        self.order_category = order_category
        self.order_id = order_id
        self.qps = qps
        self.status = status

    def validate(self):
        if self.account_credentials:
            for v1 in self.account_credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['accountCredentials'] = []
        if self.account_credentials is not None:
            for k1 in self.account_credentials:
                result['accountCredentials'].append(k1.to_map() if k1 else None)

        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid

        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code

        if self.commodity_id is not None:
            result['commodityId'] = self.commodity_id

        if self.commodity_spec is not None:
            result['commoditySpec'] = self.commodity_spec

        if self.customer_name is not None:
            result['customerName'] = self.customer_name

        if self.event_time is not None:
            result['eventTime'] = self.event_time

        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.order_category is not None:
            result['orderCategory'] = self.order_category

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.qps is not None:
            result['qps'] = self.qps

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_credentials = []
        if m.get('accountCredentials') is not None:
            for k1 in m.get('accountCredentials'):
                temp_model = main_models.AccountCredentialDTO()
                self.account_credentials.append(temp_model.from_map(k1))

        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')

        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')

        if m.get('commodityId') is not None:
            self.commodity_id = m.get('commodityId')

        if m.get('commoditySpec') is not None:
            self.commodity_spec = m.get('commoditySpec')

        if m.get('customerName') is not None:
            self.customer_name = m.get('customerName')

        if m.get('eventTime') is not None:
            self.event_time = m.get('eventTime')

        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('orderCategory') is not None:
            self.order_category = m.get('orderCategory')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('qps') is not None:
            self.qps = m.get('qps')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

