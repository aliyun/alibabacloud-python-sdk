# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeMeasurementDataResponseBody(DaraModel):
    def __init__(
        self,
        measurement_datas: main_models.DescribeMeasurementDataResponseBodyMeasurementDatas = None,
        request_id: str = None,
    ):
        # The metering data returned.
        self.measurement_datas = measurement_datas
        # The ID of the request.
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
            temp_model = main_models.DescribeMeasurementDataResponseBodyMeasurementDatas()
            self.measurement_datas = temp_model.from_map(m.get('MeasurementDatas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMeasurementDataResponseBodyMeasurementDatas(DaraModel):
    def __init__(
        self,
        measurement_data: List[main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData] = None,
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
                temp_model = main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k1))

        return self

class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementData(DaraModel):
    def __init__(
        self,
        band_width_fee_datas: main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas = None,
        charge_model: str = None,
        cost_cycle: str = None,
        cost_end_time: str = None,
        cost_start_time: str = None,
        resource_fee_data: main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData = None,
        resource_fee_data_details: main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails = None,
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
        # The information about computing resources.
        self.resource_fee_data = resource_fee_data
        # Details of the computing resources.
        self.resource_fee_data_details = resource_fee_data_details

    def validate(self):
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()
        if self.resource_fee_data:
            self.resource_fee_data.validate()
        if self.resource_fee_data_details:
            self.resource_fee_data_details.validate()

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

        if self.resource_fee_data is not None:
            result['ResourceFeeData'] = self.resource_fee_data.to_map()

        if self.resource_fee_data_details is not None:
            result['ResourceFeeDataDetails'] = self.resource_fee_data_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandWidthFeeDatas') is not None:
            temp_model = main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(m.get('BandWidthFeeDatas'))

        if m.get('ChargeModel') is not None:
            self.charge_model = m.get('ChargeModel')

        if m.get('CostCycle') is not None:
            self.cost_cycle = m.get('CostCycle')

        if m.get('CostEndTime') is not None:
            self.cost_end_time = m.get('CostEndTime')

        if m.get('CostStartTime') is not None:
            self.cost_start_time = m.get('CostStartTime')

        if m.get('ResourceFeeData') is not None:
            temp_model = main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData()
            self.resource_fee_data = temp_model.from_map(m.get('ResourceFeeData'))

        if m.get('ResourceFeeDataDetails') is not None:
            temp_model = main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails()
            self.resource_fee_data_details = temp_model.from_map(m.get('ResourceFeeDataDetails'))

        return self

class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetails(DaraModel):
    def __init__(
        self,
        resource_fee_data_detail: List[main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail] = None,
    ):
        self.resource_fee_data_detail = resource_fee_data_detail

    def validate(self):
        if self.resource_fee_data_detail:
            for v1 in self.resource_fee_data_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourceFeeDataDetail'] = []
        if self.resource_fee_data_detail is not None:
            for k1 in self.resource_fee_data_detail:
                result['ResourceFeeDataDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_fee_data_detail = []
        if m.get('ResourceFeeDataDetail') is not None:
            for k1 in m.get('ResourceFeeDataDetail'):
                temp_model = main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail()
                self.resource_fee_data_detail.append(temp_model.from_map(k1))

        return self

class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail(DaraModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_val: int = None,
        resource_type: str = None,
    ):
        # The code of the resource.
        self.cost_code = cost_code
        # The name of the resource.
        self.cost_name = cost_name
        # The consumption of the resource.
        # 
        # *   Memory unit: GB.
        # *   CPU unit: vCPU.
        # *   Storage unit: GB.
        self.cost_val = cost_val
        # The type of the resource.
        self.resource_type = resource_type

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

        if self.cost_val is not None:
            result['CostVal'] = self.cost_val

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')

        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')

        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataResourceFeeData(DaraModel):
    def __init__(
        self,
        memory: int = None,
        storage: int = None,
        vcpu: int = None,
    ):
        # The memory size. Unit: GB.
        self.memory = memory
        # The storage capacity. Unit: GB.
        self.storage = storage
        # The number of vCPUs.
        self.vcpu = vcpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory is not None:
            result['Memory'] = self.memory

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.vcpu is not None:
            result['Vcpu'] = self.vcpu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Vcpu') is not None:
            self.vcpu = m.get('Vcpu')

        return self

class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatas(DaraModel):
    def __init__(
        self,
        band_width_fee_data: List[main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData] = None,
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
                temp_model = main_models.DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k1))

        return self

class DescribeMeasurementDataResponseBodyMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(DaraModel):
    def __init__(
        self,
        cost_code: str = None,
        cost_name: str = None,
        cost_val: int = None,
    ):
        # The code of the bandwidth plan.
        self.cost_code = cost_code
        # The name of the bandwidth plan.
        self.cost_name = cost_name
        # The bandwidth consumption. Unit: bit/second.
        self.cost_val = cost_val

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

        if self.cost_val is not None:
            result['CostVal'] = self.cost_val

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostCode') is not None:
            self.cost_code = m.get('CostCode')

        if m.get('CostName') is not None:
            self.cost_name = m.get('CostName')

        if m.get('CostVal') is not None:
            self.cost_val = m.get('CostVal')

        return self

