# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveProducerUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        bill_producer_data: main_models.DescribeLiveProducerUsageDataResponseBodyBillProducerData = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The production studio usage data.
        self.bill_producer_data = bill_producer_data
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range for which the data was queried.
        self.start_time = start_time

    def validate(self):
        if self.bill_producer_data:
            self.bill_producer_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_producer_data is not None:
            result['BillProducerData'] = self.bill_producer_data.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillProducerData') is not None:
            temp_model = main_models.DescribeLiveProducerUsageDataResponseBodyBillProducerData()
            self.bill_producer_data = temp_model.from_map(m.get('BillProducerData'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLiveProducerUsageDataResponseBodyBillProducerData(DaraModel):
    def __init__(
        self,
        bill_producer_data_item: List[main_models.DescribeLiveProducerUsageDataResponseBodyBillProducerDataBillProducerDataItem] = None,
    ):
        self.bill_producer_data_item = bill_producer_data_item

    def validate(self):
        if self.bill_producer_data_item:
            for v1 in self.bill_producer_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BillProducerDataItem'] = []
        if self.bill_producer_data_item is not None:
            for k1 in self.bill_producer_data_item:
                result['BillProducerDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_producer_data_item = []
        if m.get('BillProducerDataItem') is not None:
            for k1 in m.get('BillProducerDataItem'):
                temp_model = main_models.DescribeLiveProducerUsageDataResponseBodyBillProducerDataBillProducerDataItem()
                self.bill_producer_data_item.append(temp_model.from_map(k1))

        return self

class DescribeLiveProducerUsageDataResponseBodyBillProducerDataBillProducerDataItem(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        instance: str = None,
        output_hd_duration: int = None,
        output_ld_duration: int = None,
        output_sd_duration: int = None,
        region: str = None,
        time_stamp: str = None,
        tran_hd_duration: int = None,
        tran_ld_duration: int = None,
        tran_sd_duration: int = None,
        type: str = None,
    ):
        # The domain name. If domain is specified by the SplitBy parameter, the usage data is returned based on different domain names.
        self.domain_name = domain_name
        # The production studio instance. If instance is specified by the SplitBy parameter, the usage data is returned based on different production studio instances.
        self.instance = instance
        # The duration of high definition streaming. Unit: minutes.
        self.output_hd_duration = output_hd_duration
        # The duration of low definition streaming. Unit: minutes.
        self.output_ld_duration = output_ld_duration
        # The duration of standard definition streaming. Unit: minutes.
        self.output_sd_duration = output_sd_duration
        # The region. If region is specified by the SplitBy parameter, the usage data is returned based on different regions.
        self.region = region
        # The timestamp of the returned data.
        self.time_stamp = time_stamp
        # The duration of high definition transcoding. Unit: minutes.
        self.tran_hd_duration = tran_hd_duration
        # The duration of low definition transcoding. Unit: minutes.
        self.tran_ld_duration = tran_ld_duration
        # The duration of standard definition transcoding. Unit: minutes.
        self.tran_sd_duration = tran_sd_duration
        # The type of the production studio. If type is specified by the SplitBy parameter, the usage data is returned based on different types of production studios.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.instance is not None:
            result['Instance'] = self.instance

        if self.output_hd_duration is not None:
            result['OutputHdDuration'] = self.output_hd_duration

        if self.output_ld_duration is not None:
            result['OutputLdDuration'] = self.output_ld_duration

        if self.output_sd_duration is not None:
            result['OutputSdDuration'] = self.output_sd_duration

        if self.region is not None:
            result['Region'] = self.region

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.tran_hd_duration is not None:
            result['TranHdDuration'] = self.tran_hd_duration

        if self.tran_ld_duration is not None:
            result['TranLdDuration'] = self.tran_ld_duration

        if self.tran_sd_duration is not None:
            result['TranSdDuration'] = self.tran_sd_duration

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Instance') is not None:
            self.instance = m.get('Instance')

        if m.get('OutputHdDuration') is not None:
            self.output_hd_duration = m.get('OutputHdDuration')

        if m.get('OutputLdDuration') is not None:
            self.output_ld_duration = m.get('OutputLdDuration')

        if m.get('OutputSdDuration') is not None:
            self.output_sd_duration = m.get('OutputSdDuration')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TranHdDuration') is not None:
            self.tran_hd_duration = m.get('TranHdDuration')

        if m.get('TranLdDuration') is not None:
            self.tran_ld_duration = m.get('TranLdDuration')

        if m.get('TranSdDuration') is not None:
            self.tran_sd_duration = m.get('TranSdDuration')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

