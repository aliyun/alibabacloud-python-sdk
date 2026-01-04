# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceBandwidthDetailResponseBody(DaraModel):
    def __init__(
        self,
        bandwidths: List[main_models.DescribeInstanceBandwidthDetailResponseBodyBandwidths] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the maximum public bandwidth.
        self.bandwidths = bandwidths
        # The page number of the current page.
        self.page_number = page_number
        # The number of records per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.bandwidths:
            for v1 in self.bandwidths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bandwidths'] = []
        if self.bandwidths is not None:
            for k1 in self.bandwidths:
                result['Bandwidths'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bandwidths = []
        if m.get('Bandwidths') is not None:
            for k1 in m.get('Bandwidths'):
                temp_model = main_models.DescribeInstanceBandwidthDetailResponseBodyBandwidths()
                self.bandwidths.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceBandwidthDetailResponseBodyBandwidths(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        biz_time: str = None,
        ens_region_id: str = None,
        flow_type: int = None,
        instance_id: str = None,
        instance_type: str = None,
        ip: str = None,
        isp: str = None,
        rx_bw: int = None,
        service_type: str = None,
        tx_bw: int = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The bandwidth service time. The data granularity is 5 minutes.
        self.biz_time = biz_time
        # The node ID.
        self.ens_region_id = ens_region_id
        # The type of the bandwidth. Valid values: 1, which indicates public network bandwidth. 2, which indicates internal network bandwidth.
        self.flow_type = flow_type
        # The plan ID.
        self.instance_id = instance_id
        # The type of the instance, such as vm, eip, single_tenant, and nc.
        self.instance_type = instance_type
        # null
        self.ip = ip
        # The Internet service provider to which the IP address belongs.
        self.isp = isp
        # null
        self.rx_bw = rx_bw
        # The type of the service, such as vm, eip, esk, and meta.
        self.service_type = service_type
        # null
        self.tx_bw = tx_bw

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.biz_time is not None:
            result['BizTime'] = self.biz_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.rx_bw is not None:
            result['RxBw'] = self.rx_bw

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.tx_bw is not None:
            result['TxBw'] = self.tx_bw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('RxBw') is not None:
            self.rx_bw = m.get('RxBw')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('TxBw') is not None:
            self.tx_bw = m.get('TxBw')

        return self

