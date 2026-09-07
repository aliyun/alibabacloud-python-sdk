# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListNetBandwidthResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        net_bandwidth_list: List[main_models.ListNetBandwidthResponseBodyNetBandwidthList] = None,
        page_size: int = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The list of bandwidth configurations.
        self.net_bandwidth_list = net_bandwidth_list
        # The number of entries per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of entries returned.
        self.total_num = total_num

    def validate(self):
        if self.net_bandwidth_list:
            for v1 in self.net_bandwidth_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['NetBandwidthList'] = []
        if self.net_bandwidth_list is not None:
            for k1 in self.net_bandwidth_list:
                result['NetBandwidthList'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.net_bandwidth_list = []
        if m.get('NetBandwidthList') is not None:
            for k1 in m.get('NetBandwidthList'):
                temp_model = main_models.ListNetBandwidthResponseBodyNetBandwidthList()
                self.net_bandwidth_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListNetBandwidthResponseBodyNetBandwidthList(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        instance_id: str = None,
        instance_name: str = None,
        net_type: str = None,
        region: str = None,
    ):
        # The bandwidth value, in Mbps.
        self.bandwidth = bandwidth
        # The time when the instance was created.
        self.gmt_create = gmt_create
        # The time when the instance was last modified.
        self.gmt_modified = gmt_modified
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The network type.
        self.net_type = net_type
        # The region ID.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

