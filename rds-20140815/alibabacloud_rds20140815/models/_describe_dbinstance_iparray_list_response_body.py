# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceIPArrayListResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstanceIPArrayListResponseBodyItems = None,
        request_id: str = None,
    ):
        # An array that consists of the details about the IP address whitelists.
        self.items = items
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstanceIPArrayListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceIPArrayListResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance_iparray: List[main_models.DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray] = None,
    ):
        self.dbinstance_iparray = dbinstance_iparray

    def validate(self):
        if self.dbinstance_iparray:
            for v1 in self.dbinstance_iparray:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceIPArray'] = []
        if self.dbinstance_iparray is not None:
            for k1 in self.dbinstance_iparray:
                result['DBInstanceIPArray'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_iparray = []
        if m.get('DBInstanceIPArray') is not None:
            for k1 in m.get('DBInstanceIPArray'):
                temp_model = main_models.DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray()
                self.dbinstance_iparray.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceIPArrayListResponseBodyItemsDBInstanceIPArray(DaraModel):
    def __init__(
        self,
        dbinstance_iparray_attribute: str = None,
        dbinstance_iparray_name: str = None,
        security_iplist: str = None,
        security_iptype: str = None,
    ):
        # The attribute of the IP address whitelist. By default, this parameter is empty.
        # 
        # >  A whitelist with the hidden attribute does not appear in the console. Such IP address whitelists are used to access Alibaba Cloud services, such as Data Transmission Service (DTS).
        self.dbinstance_iparray_attribute = dbinstance_iparray_attribute
        # The name of the IP address whitelist.
        self.dbinstance_iparray_name = dbinstance_iparray_name
        # The IP addresses in the IP address whitelist.
        self.security_iplist = security_iplist
        # The type of the IP address.
        self.security_iptype = security_iptype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_iparray_attribute is not None:
            result['DBInstanceIPArrayAttribute'] = self.dbinstance_iparray_attribute

        if self.dbinstance_iparray_name is not None:
            result['DBInstanceIPArrayName'] = self.dbinstance_iparray_name

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        if self.security_iptype is not None:
            result['SecurityIPType'] = self.security_iptype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceIPArrayAttribute') is not None:
            self.dbinstance_iparray_attribute = m.get('DBInstanceIPArrayAttribute')

        if m.get('DBInstanceIPArrayName') is not None:
            self.dbinstance_iparray_name = m.get('DBInstanceIPArrayName')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        if m.get('SecurityIPType') is not None:
            self.security_iptype = m.get('SecurityIPType')

        return self

