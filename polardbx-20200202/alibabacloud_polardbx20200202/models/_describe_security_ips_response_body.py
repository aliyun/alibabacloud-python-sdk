# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityIpsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeSecurityIpsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeSecurityIpsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSecurityIpsResponseBodyData(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        group_items: List[main_models.DescribeSecurityIpsResponseBodyDataGroupItems] = None,
    ):
        self.dbinstance_name = dbinstance_name
        self.group_items = group_items

    def validate(self):
        if self.group_items:
            for v1 in self.group_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        result['GroupItems'] = []
        if self.group_items is not None:
            for k1 in self.group_items:
                result['GroupItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        self.group_items = []
        if m.get('GroupItems') is not None:
            for k1 in m.get('GroupItems'):
                temp_model = main_models.DescribeSecurityIpsResponseBodyDataGroupItems()
                self.group_items.append(temp_model.from_map(k1))

        return self

class DescribeSecurityIpsResponseBodyDataGroupItems(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        security_iplist: str = None,
    ):
        self.group_name = group_name
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

