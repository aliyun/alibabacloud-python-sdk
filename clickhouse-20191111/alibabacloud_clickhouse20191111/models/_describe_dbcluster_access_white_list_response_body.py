# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20191111 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterAccessWhiteListResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_access_white_list: main_models.DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteList = None,
        request_id: str = None,
    ):
        # The details about the IP address whitelist.
        self.dbcluster_access_white_list = dbcluster_access_white_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbcluster_access_white_list:
            self.dbcluster_access_white_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_access_white_list is not None:
            result['DBClusterAccessWhiteList'] = self.dbcluster_access_white_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterAccessWhiteList') is not None:
            temp_model = main_models.DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteList()
            self.dbcluster_access_white_list = temp_model.from_map(m.get('DBClusterAccessWhiteList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteList(DaraModel):
    def __init__(
        self,
        iparray: List[main_models.DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteListIPArray] = None,
    ):
        self.iparray = iparray

    def validate(self):
        if self.iparray:
            for v1 in self.iparray:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IPArray'] = []
        if self.iparray is not None:
            for k1 in self.iparray:
                result['IPArray'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.iparray = []
        if m.get('IPArray') is not None:
            for k1 in m.get('IPArray'):
                temp_model = main_models.DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteListIPArray()
                self.iparray.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterAccessWhiteListResponseBodyDBClusterAccessWhiteListIPArray(DaraModel):
    def __init__(
        self,
        dbcluster_iparray_attribute: str = None,
        dbcluster_iparray_name: str = None,
        security_iplist: str = None,
    ):
        # The attribute of the IP address whitelist.
        self.dbcluster_iparray_attribute = dbcluster_iparray_attribute
        # The name of the IP address whitelist.
        self.dbcluster_iparray_name = dbcluster_iparray_name
        # The IP addresses in the IP address whitelist.
        self.security_iplist = security_iplist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_iparray_attribute is not None:
            result['DBClusterIPArrayAttribute'] = self.dbcluster_iparray_attribute

        if self.dbcluster_iparray_name is not None:
            result['DBClusterIPArrayName'] = self.dbcluster_iparray_name

        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterIPArrayAttribute') is not None:
            self.dbcluster_iparray_attribute = m.get('DBClusterIPArrayAttribute')

        if m.get('DBClusterIPArrayName') is not None:
            self.dbcluster_iparray_name = m.get('DBClusterIPArrayName')

        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')

        return self

