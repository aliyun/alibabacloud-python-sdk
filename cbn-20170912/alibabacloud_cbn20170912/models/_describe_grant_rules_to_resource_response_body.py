# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeGrantRulesToResourceResponseBody(DaraModel):
    def __init__(
        self,
        grant_rules: List[main_models.DescribeGrantRulesToResourceResponseBodyGrantRules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The permissions that are granted to the CEN instance.
        self.grant_rules = grant_rules
        # *   If no value is specified for **MaxResults**, query results are returned in one batch. The value of **MaxResults** indicates the total number of entries.
        # *   If a value is specified for **MaxResults**, query results are returned in batches. The value of **MaxResults** in the response indicates the number of entries in the current batch.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If the **NextToken** parameter is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.grant_rules:
            for v1 in self.grant_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GrantRules'] = []
        if self.grant_rules is not None:
            for k1 in self.grant_rules:
                result['GrantRules'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_rules = []
        if m.get('GrantRules') is not None:
            for k1 in m.get('GrantRules'):
                temp_model = main_models.DescribeGrantRulesToResourceResponseBodyGrantRules()
                self.grant_rules.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGrantRulesToResourceResponseBodyGrantRules(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_owner_id: int = None,
        create_time: str = None,
        effective_order_type: str = None,
        order_type: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The ID of the Alibaba Cloud account to which the CEN instance belongs.
        self.cen_owner_id = cen_owner_id
        # The timestamp when the permissions were granted. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        self.effective_order_type = effective_order_type
        # The entity that pays the fees of the network instance. Valid values: Valid values:
        # 
        # *   **PayByCenOwner**: The fees of the connections and data forwarding on the transit router are paid by the Alibaba Cloud account to which the CEN instance belongs.
        # *   **PayByResourceOwner**: The fees of the connections and data forwarding on the transit router are paid by the Alibaba Cloud account to which the network instance belongs.
        self.order_type = order_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.effective_order_type is not None:
            result['EffectiveOrderType'] = self.effective_order_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EffectiveOrderType') is not None:
            self.effective_order_type = m.get('EffectiveOrderType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        return self

