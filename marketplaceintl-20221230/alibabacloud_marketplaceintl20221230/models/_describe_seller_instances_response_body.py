# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_marketplaceintl20221230 import models as main_models
from darabonba.model import DaraModel

class DescribeSellerInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        fatal: bool = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[main_models.DescribeSellerInstancesResponseBodyResult] = None,
        success: bool = None,
        version: str = None,
    ):
        self.code = code
        self.count = count
        self.fatal = fatal
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result = result
        self.success = success
        self.version = version

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.fatal is not None:
            result['Fatal'] = self.fatal

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Fatal') is not None:
            self.fatal = m.get('Fatal')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeSellerInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeSellerInstancesResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_info: str = None,
        charge_type: int = None,
        commodity_code: str = None,
        created_on: int = None,
        host_info: str = None,
        info: str = None,
        instance_id: int = None,
        instance_status: str = None,
        user_id: int = None,
    ):
        self.app_info = app_info
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.created_on = created_on
        self.host_info = host_info
        self.info = info
        self.instance_id = instance_id
        self.instance_status = instance_status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_info is not None:
            result['AppInfo'] = self.app_info

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.created_on is not None:
            result['CreatedOn'] = self.created_on

        if self.host_info is not None:
            result['HostInfo'] = self.host_info

        if self.info is not None:
            result['Info'] = self.info

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfo') is not None:
            self.app_info = m.get('AppInfo')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreatedOn') is not None:
            self.created_on = m.get('CreatedOn')

        if m.get('HostInfo') is not None:
            self.host_info = m.get('HostInfo')

        if m.get('Info') is not None:
            self.info = m.get('Info')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

