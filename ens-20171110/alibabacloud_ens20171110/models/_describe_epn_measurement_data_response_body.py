# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEpnMeasurementDataResponseBody(DaraModel):
    def __init__(
        self,
        measurement_datas: main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatas = None,
        request_id: str = None,
    ):
        # The metering data returned.
        self.measurement_datas = measurement_datas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.measurement_datas:
            self.measurement_datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.measurement_datas is not None:
            result['MeasurementDatas'] = self.measurement_datas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeasurementDatas') is not None:
            temp_model = main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatas()
            self.measurement_datas = temp_model.from_map(m.get('MeasurementDatas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEpnMeasurementDataResponseBodyMeasurementDatas(DaraModel):
    def __init__(
        self,
        measurement_data: List[main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData] = None,
    ):
        self.measurement_data = measurement_data

    def validate(self):
        if self.measurement_data:
            for v1 in self.measurement_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MeasurementData'] = []
        if self.measurement_data is not None:
            for k1 in self.measurement_data:
                result['MeasurementData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.measurement_data = []
        if m.get('MeasurementData') is not None:
            for k1 in m.get('MeasurementData'):
                temp_model = main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k1))

        return self

class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementData(DaraModel):
    def __init__(
        self,
        band_width_fee_datas: main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas = None,
        charge_model: str = None,
        cost_cycle: str = None,
        cost_end_time: str = None,
        cost_start_time: str = None,
    ):
        # The bandwidth data returned.
        self.band_width_fee_datas = band_width_fee_datas
        # The metering method. Valid values:
        # 
        # *   ChargeByUnified: unified metering.
        # *   ChargeByGrade: differential metering.
        self.charge_model = charge_model
        # The metering cycle.
        self.cost_cycle = cost_cycle
        # The end time of the metering cycle.
        self.cost_end_time = cost_end_time
        # The start time of the metering cycle.
        self.cost_start_time = cost_start_time

    def validate(self):
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.band_width_fee_datas is not None:
            result['BandWidthFeeDatas'] = self.band_width_fee_datas.to_map()

        if self.charge_model is not None:
            result['ChargeModel'] = self.charge_model

        if self.cost_cycle is not None:
            result['CostCycle'] = self.cost_cycle

        if self.cost_end_time is not None:
            result['CostEndTime'] = self.cost_end_time

        if self.cost_start_time is not None:
            result['CostStartTime'] = self.cost_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidthFeeDatas') is not None:
            temp_model = main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(m.get('BandWidthFeeDatas'))

        if m.get('ChargeModel') is not None:
            self.charge_model = m.get('ChargeModel')

        if m.get('CostCycle') is not None:
            self.cost_cycle = m.get('CostCycle')

        if m.get('CostEndTime') is not None:
            self.cost_end_time = m.get('CostEndTime')

        if m.get('CostStartTime') is not None:
            self.cost_start_time = m.get('CostStartTime')

        return self

class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas(DaraModel):
    def __init__(
        self,
        band_width_fee_data: List[main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData] = None,
    ):
        self.band_width_fee_data = band_width_fee_data

    def validate(self):
        if self.band_width_fee_data:
            for v1 in self.band_width_fee_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BandWidthFeeData'] = []
        if self.band_width_fee_data is not None:
            for k1 in self.band_width_fee_data:
                result['BandWidthFeeData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_fee_data = []
        if m.get('BandWidthFeeData') is not None:
            for k1 in m.get('BandWidthFeeData'):
                temp_model = main_models.DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k1))

        return self

class DescribeEpnMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(DaraModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_type: str = None,
        cost_val: int = None,
        isp_line: str = None,
    ):
        # The code of the billable item.
        self.cost_code = cost_code
        # The name of the billable item.
        self.cost_name = cost_name
        # Metering method
        # 
        # *   SpeedUp: bandwidth of intelligent acceleration
        # *   IntranetConnection: internal bandwidth
        self.cost_type = cost_type
        # The value of the billable item.
        self.cost_val = cost_val
        # This parameter is unavailable.
        self.isp_line = isp_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_code is not None:
            result['CostCode'] = self.cost_code

        if self.cost_name is not None:
            result['CostName'] = self.cost_name

        if self.cost_type is not None:
            result['CostType'] = self.cost_type

        if self.cost_val is not None:
            result['CostVal'] = self.cost_val

        if self.isp_line is not None:
            result['IspLine'] = self.isp_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')

        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')

        if m.get('CostType') is not None:
            self.cost_type = m.get('CostType')

        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')

        if m.get('IspLine') is not None:
            self.isp_line = m.get('IspLine')

        return self

