# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDPUtilizationDetailRequest(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        deducted_instance_id: str = None,
        end_time: str = None,
        include_share: bool = None,
        instance_id: str = None,
        instance_spec: str = None,
        last_token: str = None,
        limit: int = None,
        prod_code: str = None,
        start_time: str = None,
    ):
        # The code of the resource, such as ecsRi and scu_bag. If this parameter is specified, the ProdCode parameter does not take effect for the request.
        self.commodity_code = commodity_code
        # The ID of the deducted instance. If this parameter is not specified, the details of all instances are returned.
        self.deducted_instance_id = deducted_instance_id
        # The end of the time range to query. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies whether to query the resource plan usage of linked accounts. Valid values:
        # 
        # *   true: queries the resource plan usage of linked accounts.
        # *   false: does not query the resource plan usage of linked accounts.
        # 
        # This parameter is required.
        self.include_share = include_share
        # The ID of the instance to query. If this parameter is not specified, the details of all used instances are returned.
        self.instance_id = instance_id
        # The instance type of the instance.
        self.instance_spec = instance_spec
        # The token that is used to retrieve the next page of results. For the first query, set the value to null. For subsequent queries, set the value to the token that is obtained from the NextToken parameter.
        self.last_token = last_token
        # The number of entries to return on each page. Default value: 20. Maximum value: 300.
        self.limit = limit
        # The code of the service. Example: ecs.
        self.prod_code = prod_code
        # The beginning of the time range to query. Specify the time in the YYYY-MM-DD HH:mm:ss format.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.include_share is not None:
            result['IncludeShare'] = self.include_share

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.last_token is not None:
            result['LastToken'] = self.last_token

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IncludeShare') is not None:
            self.include_share = m.get('IncludeShare')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('LastToken') is not None:
            self.last_token = m.get('LastToken')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

