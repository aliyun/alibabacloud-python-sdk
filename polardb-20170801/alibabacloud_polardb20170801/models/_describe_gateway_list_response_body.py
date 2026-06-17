# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeGatewayListResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeGatewayListResponseBodyItems] = None,
        page_number: str = None,
        page_record_count: str = None,
        page_size: str = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # A list of gateway instances.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The number of entries per page.
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        # 
        # Default value: 30.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeGatewayListResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeGatewayListResponseBodyItems(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        db_type: str = None,
        expire_time: str = None,
        expired: bool = None,
        gw_cluster_id: str = None,
        gw_description: str = None,
        modify_time: str = None,
        pay_type: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The time when the gateway instance was created.
        self.create_time = create_time
        # The database type.
        self.db_type = db_type
        # The expiration time of the gateway instance.
        # 
        # - For subscription instances, this parameter indicates the expiration time.
        # 
        # - This parameter is empty for pay-as-you-go instances.
        self.expire_time = expire_time
        # Indicates whether the gateway instance has expired. Valid values:
        # 
        # - **true**
        # 
        # - **false**
        self.expired = expired
        # The gateway instance ID.
        self.gw_cluster_id = gw_cluster_id
        # The description of the gateway instance.
        self.gw_description = gw_description
        # The time when the gateway instance was last modified.
        self.modify_time = modify_time
        # The billing method. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go
        # 
        # - **Prepaid**: subscription
        self.pay_type = pay_type
        # The region ID.
        self.region_id = region_id
        # The status of the gateway instance. Valid values:
        # 
        # - **CREATE**: creating
        # 
        # - **ACTIVATION**: running
        self.status = status
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.gw_description is not None:
            result['GwDescription'] = self.gw_description

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('GwDescription') is not None:
            self.gw_description = m.get('GwDescription')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

