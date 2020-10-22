# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class DescribeEpnBandwitdhByInternetChargeTypeRequest(TeaModel):
    def __init__(self, version=None, start_time=None, end_time=None, isp=None, ens_region_id=None,
                 networking_model=None):
        self.version = version          # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.isp = isp                  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.networking_model = networking_model  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Isp'] = self.isp
        result['EnsRegionId'] = self.ens_region_id
        result['NetworkingModel'] = self.networking_model
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.isp = map.get('Isp')
        self.ens_region_id = map.get('EnsRegionId')
        self.networking_model = map.get('NetworkingModel')
        return self


class DescribeEpnBandwitdhByInternetChargeTypeResponse(TeaModel):
    def __init__(self, request_id=None, internet_charge_type=None, bandwidth_value=None, time_stamp=None):
        self.request_id = request_id    # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.bandwidth_value = bandwidth_value  # type: int
        self.time_stamp = time_stamp    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.bandwidth_value, 'bandwidth_value')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InternetChargeType'] = self.internet_charge_type
        result['BandwidthValue'] = self.bandwidth_value
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.internet_charge_type = map.get('InternetChargeType')
        self.bandwidth_value = map.get('BandwidthValue')
        self.time_stamp = map.get('TimeStamp')
        return self


class DescribeEpnBandWidthDataRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, instance_id=None, start_time=None, end_time=None,
                 period=None, isp=None, networking_model=None, epninstance_id=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.period = period            # type: str
        self.isp = isp                  # type: str
        self.networking_model = networking_model  # type: str
        self.epninstance_id = epninstance_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.period, 'period')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['InstanceId'] = self.instance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Period'] = self.period
        result['Isp'] = self.isp
        result['NetworkingModel'] = self.networking_model
        result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.instance_id = map.get('InstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.period = map.get('Period')
        self.isp = map.get('Isp')
        self.networking_model = map.get('NetworkingModel')
        self.epninstance_id = map.get('EPNInstanceId')
        return self


class DescribeEpnBandWidthDataResponse(TeaModel):
    def __init__(self, request_id=None, monitor_data=None):
        self.request_id = request_id    # type: str
        self.monitor_data = monitor_data  # type: DescribeEpnBandWidthDataResponseMonitorData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.monitor_data, 'monitor_data')
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        else:
            result['MonitorData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('MonitorData') is not None:
            temp_model = DescribeEpnBandWidthDataResponseMonitorData()
            self.monitor_data = temp_model.from_map(map['MonitorData'])
        else:
            self.monitor_data = None
        return self


class DescribeEpnBandWidthDataResponseMonitorDataBandWidthMonitorData(TeaModel):
    def __init__(self, up_band_width=None, down_band_width=None, internet_tx=None, internet_rx=None,
                 time_stamp=None):
        self.up_band_width = up_band_width  # type: int
        self.down_band_width = down_band_width  # type: int
        self.internet_tx = internet_tx  # type: int
        self.internet_rx = internet_rx  # type: int
        self.time_stamp = time_stamp    # type: str

    def validate(self):
        self.validate_required(self.up_band_width, 'up_band_width')
        self.validate_required(self.down_band_width, 'down_band_width')
        self.validate_required(self.internet_tx, 'internet_tx')
        self.validate_required(self.internet_rx, 'internet_rx')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['UpBandWidth'] = self.up_band_width
        result['DownBandWidth'] = self.down_band_width
        result['InternetTX'] = self.internet_tx
        result['InternetRX'] = self.internet_rx
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.up_band_width = map.get('UpBandWidth')
        self.down_band_width = map.get('DownBandWidth')
        self.internet_tx = map.get('InternetTX')
        self.internet_rx = map.get('InternetRX')
        self.time_stamp = map.get('TimeStamp')
        return self


class DescribeEpnBandWidthDataResponseMonitorData(TeaModel):
    def __init__(self, max_down_band_width=None, max_up_band_width=None, band_width_monitor_data=None):
        self.max_down_band_width = max_down_band_width  # type: int
        self.max_up_band_width = max_up_band_width  # type: int
        self.band_width_monitor_data = band_width_monitor_data  # type: List[DescribeEpnBandWidthDataResponseMonitorDataBandWidthMonitorData]

    def validate(self):
        self.validate_required(self.max_down_band_width, 'max_down_band_width')
        self.validate_required(self.max_up_band_width, 'max_up_band_width')
        self.validate_required(self.band_width_monitor_data, 'band_width_monitor_data')
        if self.band_width_monitor_data:
            for k in self.band_width_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MaxDownBandWidth'] = self.max_down_band_width
        result['MaxUpBandWidth'] = self.max_up_band_width
        result['BandWidthMonitorData'] = []
        if self.band_width_monitor_data is not None:
            for k in self.band_width_monitor_data:
                result['BandWidthMonitorData'].append(k.to_map() if k else None)
        else:
            result['BandWidthMonitorData'] = None
        return result

    def from_map(self, map={}):
        self.max_down_band_width = map.get('MaxDownBandWidth')
        self.max_up_band_width = map.get('MaxUpBandWidth')
        self.band_width_monitor_data = []
        if map.get('BandWidthMonitorData') is not None:
            for k in map.get('BandWidthMonitorData'):
                temp_model = DescribeEpnBandWidthDataResponseMonitorDataBandWidthMonitorData()
                self.band_width_monitor_data.append(temp_model.from_map(k))
        else:
            self.band_width_monitor_data = None
        return self


class DescribeEpnMeasurementDataRequest(TeaModel):
    def __init__(self, version=None, start_date=None, end_date=None):
        self.version = version          # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class DescribeEpnMeasurementDataResponse(TeaModel):
    def __init__(self, request_id=None, measurement_datas=None):
        self.request_id = request_id    # type: str
        self.measurement_datas = measurement_datas  # type: DescribeEpnMeasurementDataResponseMeasurementDatas

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.measurement_datas, 'measurement_datas')
        if self.measurement_datas:
            self.measurement_datas.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.measurement_datas is not None:
            result['MeasurementDatas'] = self.measurement_datas.to_map()
        else:
            result['MeasurementDatas'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('MeasurementDatas') is not None:
            temp_model = DescribeEpnMeasurementDataResponseMeasurementDatas()
            self.measurement_datas = temp_model.from_map(map['MeasurementDatas'])
        else:
            self.measurement_datas = None
        return self


class DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(TeaModel):
    def __init__(self, cost_val=None, cost_code=None, cost_name=None, cost_type=None, isp_line=None):
        self.cost_val = cost_val        # type: int
        self.cost_code = cost_code      # type: str
        self.cost_name = cost_name      # type: str
        self.cost_type = cost_type      # type: str
        self.isp_line = isp_line        # type: str

    def validate(self):
        self.validate_required(self.cost_val, 'cost_val')
        self.validate_required(self.cost_code, 'cost_code')
        self.validate_required(self.cost_name, 'cost_name')
        self.validate_required(self.cost_type, 'cost_type')
        self.validate_required(self.isp_line, 'isp_line')

    def to_map(self):
        result = {}
        result['CostVal'] = self.cost_val
        result['CostCode'] = self.cost_code
        result['CostName'] = self.cost_name
        result['CostType'] = self.cost_type
        result['IspLine'] = self.isp_line
        return result

    def from_map(self, map={}):
        self.cost_val = map.get('CostVal')
        self.cost_code = map.get('CostCode')
        self.cost_name = map.get('CostName')
        self.cost_type = map.get('CostType')
        self.isp_line = map.get('IspLine')
        return self


class DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatas(TeaModel):
    def __init__(self, band_width_fee_data=None):
        self.band_width_fee_data = band_width_fee_data  # type: List[DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData]

    def validate(self):
        self.validate_required(self.band_width_fee_data, 'band_width_fee_data')
        if self.band_width_fee_data:
            for k in self.band_width_fee_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BandWidthFeeData'] = []
        if self.band_width_fee_data is not None:
            for k in self.band_width_fee_data:
                result['BandWidthFeeData'].append(k.to_map() if k else None)
        else:
            result['BandWidthFeeData'] = None
        return result

    def from_map(self, map={}):
        self.band_width_fee_data = []
        if map.get('BandWidthFeeData') is not None:
            for k in map.get('BandWidthFeeData'):
                temp_model = DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k))
        else:
            self.band_width_fee_data = None
        return self


class DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementData(TeaModel):
    def __init__(self, charge_model=None, cost_cycle=None, cost_start_time=None, cost_end_time=None,
                 band_width_fee_datas=None):
        self.charge_model = charge_model  # type: str
        self.cost_cycle = cost_cycle    # type: str
        self.cost_start_time = cost_start_time  # type: str
        self.cost_end_time = cost_end_time  # type: str
        self.band_width_fee_datas = band_width_fee_datas  # type: DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatas

    def validate(self):
        self.validate_required(self.charge_model, 'charge_model')
        self.validate_required(self.cost_cycle, 'cost_cycle')
        self.validate_required(self.cost_start_time, 'cost_start_time')
        self.validate_required(self.cost_end_time, 'cost_end_time')
        self.validate_required(self.band_width_fee_datas, 'band_width_fee_datas')
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()

    def to_map(self):
        result = {}
        result['ChargeModel'] = self.charge_model
        result['CostCycle'] = self.cost_cycle
        result['CostStartTime'] = self.cost_start_time
        result['CostEndTime'] = self.cost_end_time
        if self.band_width_fee_datas is not None:
            result['BandWidthFeeDatas'] = self.band_width_fee_datas.to_map()
        else:
            result['BandWidthFeeDatas'] = None
        return result

    def from_map(self, map={}):
        self.charge_model = map.get('ChargeModel')
        self.cost_cycle = map.get('CostCycle')
        self.cost_start_time = map.get('CostStartTime')
        self.cost_end_time = map.get('CostEndTime')
        if map.get('BandWidthFeeDatas') is not None:
            temp_model = DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(map['BandWidthFeeDatas'])
        else:
            self.band_width_fee_datas = None
        return self


class DescribeEpnMeasurementDataResponseMeasurementDatas(TeaModel):
    def __init__(self, measurement_data=None):
        self.measurement_data = measurement_data  # type: List[DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementData]

    def validate(self):
        self.validate_required(self.measurement_data, 'measurement_data')
        if self.measurement_data:
            for k in self.measurement_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MeasurementData'] = []
        if self.measurement_data is not None:
            for k in self.measurement_data:
                result['MeasurementData'].append(k.to_map() if k else None)
        else:
            result['MeasurementData'] = None
        return result

    def from_map(self, map={}):
        self.measurement_data = []
        if map.get('MeasurementData') is not None:
            for k in map.get('MeasurementData'):
                temp_model = DescribeEpnMeasurementDataResponseMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k))
        else:
            self.measurement_data = None
        return self


class DescribeNetworkInterfacesRequest(TeaModel):
    def __init__(self, instance_id=None, v_switch_id=None, ens_region_id=None, primary_ip_address=None,
                 page_number=None, page_size=None):
        self.instance_id = instance_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.primary_ip_address = primary_ip_address  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['VSwitchId'] = self.v_switch_id
        result['EnsRegionId'] = self.ens_region_id
        result['PrimaryIpAddress'] = self.primary_ip_address
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.v_switch_id = map.get('VSwitchId')
        self.ens_region_id = map.get('EnsRegionId')
        self.primary_ip_address = map.get('PrimaryIpAddress')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeNetworkInterfacesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 network_interface_sets=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.network_interface_sets = network_interface_sets  # type: DescribeNetworkInterfacesResponseNetworkInterfaceSets

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.network_interface_sets, 'network_interface_sets')
        if self.network_interface_sets:
            self.network_interface_sets.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.network_interface_sets is not None:
            result['NetworkInterfaceSets'] = self.network_interface_sets.to_map()
        else:
            result['NetworkInterfaceSets'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('NetworkInterfaceSets') is not None:
            temp_model = DescribeNetworkInterfacesResponseNetworkInterfaceSets()
            self.network_interface_sets = temp_model.from_map(map['NetworkInterfaceSets'])
        else:
            self.network_interface_sets = None
        return self


class DescribeNetworkInterfacesResponseNetworkInterfaceSetsNetworkInterfaceSet(TeaModel):
    def __init__(self, status=None, primary_ip=None, ens_region_id=None, instance_id=None, v_switch_id=None,
                 network_interface_id=None, mac_address=None, creation_time=None, primary_ip_type=None):
        self.status = status            # type: str
        self.primary_ip = primary_ip    # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.network_interface_id = network_interface_id  # type: str
        self.mac_address = mac_address  # type: str
        self.creation_time = creation_time  # type: str
        self.primary_ip_type = primary_ip_type  # type: str

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.primary_ip, 'primary_ip')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.network_interface_id, 'network_interface_id')
        self.validate_required(self.mac_address, 'mac_address')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.primary_ip_type, 'primary_ip_type')

    def to_map(self):
        result = {}
        result['Status'] = self.status
        result['PrimaryIp'] = self.primary_ip
        result['EnsRegionId'] = self.ens_region_id
        result['InstanceId'] = self.instance_id
        result['VSwitchId'] = self.v_switch_id
        result['NetworkInterfaceId'] = self.network_interface_id
        result['MacAddress'] = self.mac_address
        result['CreationTime'] = self.creation_time
        result['PrimaryIpType'] = self.primary_ip_type
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        self.primary_ip = map.get('PrimaryIp')
        self.ens_region_id = map.get('EnsRegionId')
        self.instance_id = map.get('InstanceId')
        self.v_switch_id = map.get('VSwitchId')
        self.network_interface_id = map.get('NetworkInterfaceId')
        self.mac_address = map.get('MacAddress')
        self.creation_time = map.get('CreationTime')
        self.primary_ip_type = map.get('PrimaryIpType')
        return self


class DescribeNetworkInterfacesResponseNetworkInterfaceSets(TeaModel):
    def __init__(self, network_interface_set=None):
        self.network_interface_set = network_interface_set  # type: List[DescribeNetworkInterfacesResponseNetworkInterfaceSetsNetworkInterfaceSet]

    def validate(self):
        self.validate_required(self.network_interface_set, 'network_interface_set')
        if self.network_interface_set:
            for k in self.network_interface_set:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['NetworkInterfaceSet'] = []
        if self.network_interface_set is not None:
            for k in self.network_interface_set:
                result['NetworkInterfaceSet'].append(k.to_map() if k else None)
        else:
            result['NetworkInterfaceSet'] = None
        return result

    def from_map(self, map={}):
        self.network_interface_set = []
        if map.get('NetworkInterfaceSet') is not None:
            for k in map.get('NetworkInterfaceSet'):
                temp_model = DescribeNetworkInterfacesResponseNetworkInterfaceSetsNetworkInterfaceSet()
                self.network_interface_set.append(temp_model.from_map(k))
        else:
            self.network_interface_set = None
        return self


class CreateEPInstanceRequest(TeaModel):
    def __init__(self, epninstance_type=None, epninstance_name=None, internet_charge_type=None,
                 networking_model=None, internet_max_bandwidth_out=None):
        self.epninstance_type = epninstance_type  # type: str
        self.epninstance_name = epninstance_name  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.networking_model = networking_model  # type: str
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int

    def validate(self):
        self.validate_required(self.epninstance_type, 'epninstance_type')
        self.validate_required(self.epninstance_name, 'epninstance_name')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.networking_model, 'networking_model')
        self.validate_required(self.internet_max_bandwidth_out, 'internet_max_bandwidth_out')

    def to_map(self):
        result = {}
        result['EPNInstanceType'] = self.epninstance_type
        result['EPNInstanceName'] = self.epninstance_name
        result['InternetChargeType'] = self.internet_charge_type
        result['NetworkingModel'] = self.networking_model
        result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        return result

    def from_map(self, map={}):
        self.epninstance_type = map.get('EPNInstanceType')
        self.epninstance_name = map.get('EPNInstanceName')
        self.internet_charge_type = map.get('InternetChargeType')
        self.networking_model = map.get('NetworkingModel')
        self.internet_max_bandwidth_out = map.get('InternetMaxBandwidthOut')
        return self


class CreateEPInstanceResponse(TeaModel):
    def __init__(self, request_id=None, epninstance_id=None):
        self.request_id = request_id    # type: str
        self.epninstance_id = epninstance_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.epninstance_id, 'epninstance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.epninstance_id = map.get('EPNInstanceId')
        return self


class ModifyImageSharePermissionRequest(TeaModel):
    def __init__(self, image_id=None, add_accounts=None, remove_accounts=None):
        self.image_id = image_id        # type: str
        self.add_accounts = add_accounts  # type: str
        self.remove_accounts = remove_accounts  # type: str

    def validate(self):
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['AddAccounts'] = self.add_accounts
        result['RemoveAccounts'] = self.remove_accounts
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.add_accounts = map.get('AddAccounts')
        self.remove_accounts = map.get('RemoveAccounts')
        return self


class ModifyImageSharePermissionResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddNetworkInterfaceToInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, networks=None):
        self.instance_id = instance_id  # type: str
        self.networks = networks        # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.networks, 'networks')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Networks'] = self.networks
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.networks = map.get('Networks')
        return self


class AddNetworkInterfaceToInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeImageSharePermissionRequest(TeaModel):
    def __init__(self, image_id=None, page_number=None, page_size=None, aliyun_id=None):
        self.image_id = image_id        # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str
        self.aliyun_id = aliyun_id      # type: int

    def validate(self):
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['AliyunId'] = self.aliyun_id
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.aliyun_id = map.get('AliyunId')
        return self


class DescribeImageSharePermissionResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, image_id=None,
                 accounts=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.image_id = image_id        # type: str
        self.accounts = accounts        # type: DescribeImageSharePermissionResponseAccounts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.accounts, 'accounts')
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['ImageId'] = self.image_id
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        else:
            result['Accounts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.image_id = map.get('ImageId')
        if map.get('Accounts') is not None:
            temp_model = DescribeImageSharePermissionResponseAccounts()
            self.accounts = temp_model.from_map(map['Accounts'])
        else:
            self.accounts = None
        return self


class DescribeImageSharePermissionResponseAccounts(TeaModel):
    def __init__(self, account=None):
        self.account = account          # type: List[str]

    def validate(self):
        self.validate_required(self.account, 'account')

    def to_map(self):
        result = {}
        result['Account'] = self.account
        return result

    def from_map(self, map={}):
        self.account = map.get('Account')
        return self


class RemoveVSwitchesFromEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None, v_switches_info=None):
        self.epninstance_id = epninstance_id  # type: str
        self.v_switches_info = v_switches_info  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')
        self.validate_required(self.v_switches_info, 'v_switches_info')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        result['VSwitchesInfo'] = self.v_switches_info
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        self.v_switches_info = map.get('VSwitchesInfo')
        return self


class RemoveVSwitchesFromEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DistApplicationDataRequest(TeaModel):
    def __init__(self, app_id=None, data=None, dist_strategy=None):
        self.app_id = app_id            # type: str
        self.data = data                # type: str
        self.dist_strategy = dist_strategy  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['Data'] = self.data
        result['DistStrategy'] = self.dist_strategy
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.data = map.get('Data')
        self.dist_strategy = map.get('DistStrategy')
        return self


class DistApplicationDataResponse(TeaModel):
    def __init__(self, request_id=None, dist_instance_total_count=None, dist_results=None, dist_instance_ids=None):
        self.request_id = request_id    # type: str
        self.dist_instance_total_count = dist_instance_total_count  # type: int
        self.dist_results = dist_results  # type: DistApplicationDataResponseDistResults
        self.dist_instance_ids = dist_instance_ids  # type: DistApplicationDataResponseDistInstanceIds

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.dist_instance_total_count, 'dist_instance_total_count')
        self.validate_required(self.dist_results, 'dist_results')
        if self.dist_results:
            self.dist_results.validate()
        self.validate_required(self.dist_instance_ids, 'dist_instance_ids')
        if self.dist_instance_ids:
            self.dist_instance_ids.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DistInstanceTotalCount'] = self.dist_instance_total_count
        if self.dist_results is not None:
            result['DistResults'] = self.dist_results.to_map()
        else:
            result['DistResults'] = None
        if self.dist_instance_ids is not None:
            result['DistInstanceIds'] = self.dist_instance_ids.to_map()
        else:
            result['DistInstanceIds'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.dist_instance_total_count = map.get('DistInstanceTotalCount')
        if map.get('DistResults') is not None:
            temp_model = DistApplicationDataResponseDistResults()
            self.dist_results = temp_model.from_map(map['DistResults'])
        else:
            self.dist_results = None
        if map.get('DistInstanceIds') is not None:
            temp_model = DistApplicationDataResponseDistInstanceIds()
            self.dist_instance_ids = temp_model.from_map(map['DistInstanceIds'])
        else:
            self.dist_instance_ids = None
        return self


class DistApplicationDataResponseDistResultsDistResult(TeaModel):
    def __init__(self, version=None, result_descrip=None, result_code=None, name=None):
        self.version = version          # type: str
        self.result_descrip = result_descrip  # type: str
        self.result_code = result_code  # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.result_descrip, 'result_descrip')
        self.validate_required(self.result_code, 'result_code')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['ResultDescrip'] = self.result_descrip
        result['ResultCode'] = self.result_code
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.result_descrip = map.get('ResultDescrip')
        self.result_code = map.get('ResultCode')
        self.name = map.get('Name')
        return self


class DistApplicationDataResponseDistResults(TeaModel):
    def __init__(self, dist_result=None):
        self.dist_result = dist_result  # type: List[DistApplicationDataResponseDistResultsDistResult]

    def validate(self):
        self.validate_required(self.dist_result, 'dist_result')
        if self.dist_result:
            for k in self.dist_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DistResult'] = []
        if self.dist_result is not None:
            for k in self.dist_result:
                result['DistResult'].append(k.to_map() if k else None)
        else:
            result['DistResult'] = None
        return result

    def from_map(self, map={}):
        self.dist_result = []
        if map.get('DistResult') is not None:
            for k in map.get('DistResult'):
                temp_model = DistApplicationDataResponseDistResultsDistResult()
                self.dist_result.append(temp_model.from_map(k))
        else:
            self.dist_result = None
        return self


class DistApplicationDataResponseDistInstanceIds(TeaModel):
    def __init__(self, dist_instance_id=None):
        self.dist_instance_id = dist_instance_id  # type: List[str]

    def validate(self):
        self.validate_required(self.dist_instance_id, 'dist_instance_id')

    def to_map(self):
        result = {}
        result['DistInstanceId'] = self.dist_instance_id
        return result

    def from_map(self, map={}):
        self.dist_instance_id = map.get('DistInstanceId')
        return self


class JoinVSwitchesToEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None, v_switches_info=None):
        self.epninstance_id = epninstance_id  # type: str
        self.v_switches_info = v_switches_info  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')
        self.validate_required(self.v_switches_info, 'v_switches_info')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        result['VSwitchesInfo'] = self.v_switches_info
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        self.v_switches_info = map.get('VSwitchesInfo')
        return self


class JoinVSwitchesToEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeApplicationRequest(TeaModel):
    def __init__(self, app_id=None, app_versions=None, level=None, out_detail_stat_params=None):
        self.app_id = app_id            # type: str
        self.app_versions = app_versions  # type: str
        self.level = level              # type: str
        self.out_detail_stat_params = out_detail_stat_params  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['AppVersions'] = self.app_versions
        result['Level'] = self.level
        result['OutDetailStatParams'] = self.out_detail_stat_params
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.app_versions = map.get('AppVersions')
        self.level = map.get('Level')
        self.out_detail_stat_params = map.get('OutDetailStatParams')
        return self


class DescribeApplicationResponse(TeaModel):
    def __init__(self, request_id=None, application=None):
        self.request_id = request_id    # type: str
        self.application = application  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application, 'application')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Application'] = self.application
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.application = map.get('Application')
        return self


class DescribeDataPushResultRequest(TeaModel):
    def __init__(self, app_id=None, data_names=None, data_versions=None, min_date=None, max_date=None,
                 page_number=None, page_size=None, region_ids=None):
        self.app_id = app_id            # type: str
        self.data_names = data_names    # type: str
        self.data_versions = data_versions  # type: str
        self.min_date = min_date        # type: str
        self.max_date = max_date        # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.region_ids = region_ids    # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['DataNames'] = self.data_names
        result['DataVersions'] = self.data_versions
        result['MinDate'] = self.min_date
        result['MaxDate'] = self.max_date
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['RegionIds'] = self.region_ids
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.data_names = map.get('DataNames')
        self.data_versions = map.get('DataVersions')
        self.min_date = map.get('MinDate')
        self.max_date = map.get('MaxDate')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.region_ids = map.get('RegionIds')
        return self


class DescribeDataPushResultResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, push_results=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.push_results = push_results  # type: DescribeDataPushResultResponsePushResults

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.push_results, 'push_results')
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()
        else:
            result['PushResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('PushResults') is not None:
            temp_model = DescribeDataPushResultResponsePushResults()
            self.push_results = temp_model.from_map(map['PushResults'])
        else:
            self.push_results = None
        return self


class DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStatRegionIdsRegionId(TeaModel):
    def __init__(self, start_time=None, update_time=None, region_id=None, status_descrip=None):
        self.start_time = start_time    # type: str
        self.update_time = update_time  # type: str
        self.region_id = region_id      # type: str
        self.status_descrip = status_descrip  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.region_id, 'region_id')
        self.validate_required(self.status_descrip, 'status_descrip')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['UpdateTime'] = self.update_time
        result['RegionId'] = self.region_id
        result['StatusDescrip'] = self.status_descrip
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.update_time = map.get('UpdateTime')
        self.region_id = map.get('RegionId')
        self.status_descrip = map.get('StatusDescrip')
        return self


class DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStatRegionIds(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id      # type: List[DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStatRegionIdsRegionId]

    def validate(self):
        self.validate_required(self.region_id, 'region_id')
        if self.region_id:
            for k in self.region_id:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RegionId'] = []
        if self.region_id is not None:
            for k in self.region_id:
                result['RegionId'].append(k.to_map() if k else None)
        else:
            result['RegionId'] = None
        return result

    def from_map(self, map={}):
        self.region_id = []
        if map.get('RegionId') is not None:
            for k in map.get('RegionId'):
                temp_model = DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStatRegionIdsRegionId()
                self.region_id.append(temp_model.from_map(k))
        else:
            self.region_id = None
        return self


class DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStat(TeaModel):
    def __init__(self, status=None, region_id_count=None, region_ids=None):
        self.status = status            # type: str
        self.region_id_count = region_id_count  # type: int
        self.region_ids = region_ids    # type: DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStatRegionIds

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.region_id_count, 'region_id_count')
        self.validate_required(self.region_ids, 'region_ids')
        if self.region_ids:
            self.region_ids.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        result['RegionIdCount'] = self.region_id_count
        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids.to_map()
        else:
            result['RegionIds'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        self.region_id_count = map.get('RegionIdCount')
        if map.get('RegionIds') is not None:
            temp_model = DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStatRegionIds()
            self.region_ids = temp_model.from_map(map['RegionIds'])
        else:
            self.region_ids = None
        return self


class DescribeDataPushResultResponsePushResultsPushResultStatusStatS(TeaModel):
    def __init__(self, status_stat=None):
        self.status_stat = status_stat  # type: List[DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStat]

    def validate(self):
        self.validate_required(self.status_stat, 'status_stat')
        if self.status_stat:
            for k in self.status_stat:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StatusStat'] = []
        if self.status_stat is not None:
            for k in self.status_stat:
                result['StatusStat'].append(k.to_map() if k else None)
        else:
            result['StatusStat'] = None
        return result

    def from_map(self, map={}):
        self.status_stat = []
        if map.get('StatusStat') is not None:
            for k in map.get('StatusStat'):
                temp_model = DescribeDataPushResultResponsePushResultsPushResultStatusStatSStatusStat()
                self.status_stat.append(temp_model.from_map(k))
        else:
            self.status_stat = None
        return self


class DescribeDataPushResultResponsePushResultsPushResult(TeaModel):
    def __init__(self, name=None, version=None, status_stat_s=None):
        self.name = name                # type: str
        self.version = version          # type: str
        self.status_stat_s = status_stat_s  # type: DescribeDataPushResultResponsePushResultsPushResultStatusStatS

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.version, 'version')
        self.validate_required(self.status_stat_s, 'status_stat_s')
        if self.status_stat_s:
            self.status_stat_s.validate()

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['Version'] = self.version
        if self.status_stat_s is not None:
            result['StatusStatS'] = self.status_stat_s.to_map()
        else:
            result['StatusStatS'] = None
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.version = map.get('Version')
        if map.get('StatusStatS') is not None:
            temp_model = DescribeDataPushResultResponsePushResultsPushResultStatusStatS()
            self.status_stat_s = temp_model.from_map(map['StatusStatS'])
        else:
            self.status_stat_s = None
        return self


class DescribeDataPushResultResponsePushResults(TeaModel):
    def __init__(self, push_result=None):
        self.push_result = push_result  # type: List[DescribeDataPushResultResponsePushResultsPushResult]

    def validate(self):
        self.validate_required(self.push_result, 'push_result')
        if self.push_result:
            for k in self.push_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PushResult'] = []
        if self.push_result is not None:
            for k in self.push_result:
                result['PushResult'].append(k.to_map() if k else None)
        else:
            result['PushResult'] = None
        return result

    def from_map(self, map={}):
        self.push_result = []
        if map.get('PushResult') is not None:
            for k in map.get('PushResult'):
                temp_model = DescribeDataPushResultResponsePushResultsPushResult()
                self.push_result.append(temp_model.from_map(k))
        else:
            self.push_result = None
        return self


class PushApplicationDataRequest(TeaModel):
    def __init__(self, data=None, app_id=None, timeout=None, push_strategy=None):
        self.data = data                # type: str
        self.app_id = app_id            # type: str
        self.timeout = timeout          # type: int
        self.push_strategy = push_strategy  # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['Data'] = self.data
        result['AppId'] = self.app_id
        result['Timeout'] = self.timeout
        result['PushStrategy'] = self.push_strategy
        return result

    def from_map(self, map={}):
        self.data = map.get('Data')
        self.app_id = map.get('AppId')
        self.timeout = map.get('Timeout')
        self.push_strategy = map.get('PushStrategy')
        return self


class PushApplicationDataResponse(TeaModel):
    def __init__(self, request_id=None, push_results=None):
        self.request_id = request_id    # type: str
        self.push_results = push_results  # type: PushApplicationDataResponsePushResults

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.push_results, 'push_results')
        if self.push_results:
            self.push_results.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.push_results is not None:
            result['PushResults'] = self.push_results.to_map()
        else:
            result['PushResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('PushResults') is not None:
            temp_model = PushApplicationDataResponsePushResults()
            self.push_results = temp_model.from_map(map['PushResults'])
        else:
            self.push_results = None
        return self


class PushApplicationDataResponsePushResultsPushResult(TeaModel):
    def __init__(self, version=None, result_descrip=None, result_code=None, name=None):
        self.version = version          # type: str
        self.result_descrip = result_descrip  # type: str
        self.result_code = result_code  # type: int
        self.name = name                # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.result_descrip, 'result_descrip')
        self.validate_required(self.result_code, 'result_code')
        self.validate_required(self.name, 'name')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['ResultDescrip'] = self.result_descrip
        result['ResultCode'] = self.result_code
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.result_descrip = map.get('ResultDescrip')
        self.result_code = map.get('ResultCode')
        self.name = map.get('Name')
        return self


class PushApplicationDataResponsePushResults(TeaModel):
    def __init__(self, push_result=None):
        self.push_result = push_result  # type: List[PushApplicationDataResponsePushResultsPushResult]

    def validate(self):
        self.validate_required(self.push_result, 'push_result')
        if self.push_result:
            for k in self.push_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PushResult'] = []
        if self.push_result is not None:
            for k in self.push_result:
                result['PushResult'].append(k.to_map() if k else None)
        else:
            result['PushResult'] = None
        return result

    def from_map(self, map={}):
        self.push_result = []
        if map.get('PushResult') is not None:
            for k in map.get('PushResult'):
                temp_model = PushApplicationDataResponsePushResultsPushResult()
                self.push_result.append(temp_model.from_map(k))
        else:
            self.push_result = None
        return self


class UpgradeApplicationRequest(TeaModel):
    def __init__(self, app_id=None, template=None, timeout=None):
        self.app_id = app_id            # type: str
        self.template = template        # type: str
        self.timeout = timeout          # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.template, 'template')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['Template'] = self.template
        result['Timeout'] = self.timeout
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.template = map.get('Template')
        self.timeout = map.get('Timeout')
        return self


class UpgradeApplicationResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RescaleApplicationRequest(TeaModel):
    def __init__(self, app_id=None, rescale_type=None, rescale_level=None, resource_selector=None,
                 to_app_version=None, timeout=None):
        self.app_id = app_id            # type: str
        self.rescale_type = rescale_type  # type: str
        self.rescale_level = rescale_level  # type: str
        self.resource_selector = resource_selector  # type: str
        self.to_app_version = to_app_version  # type: str
        self.timeout = timeout          # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.rescale_type, 'rescale_type')
        self.validate_required(self.resource_selector, 'resource_selector')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RescaleType'] = self.rescale_type
        result['RescaleLevel'] = self.rescale_level
        result['ResourceSelector'] = self.resource_selector
        result['ToAppVersion'] = self.to_app_version
        result['Timeout'] = self.timeout
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.rescale_type = map.get('RescaleType')
        self.rescale_level = map.get('RescaleLevel')
        self.resource_selector = map.get('ResourceSelector')
        self.to_app_version = map.get('ToAppVersion')
        self.timeout = map.get('Timeout')
        return self


class RescaleApplicationResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None):
        self.epninstance_id = epninstance_id  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        return self


class DeleteEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(self, cluster_names=None, app_versions=None, level=None, out_app_info_params=None,
                 page_number=None, page_size=None, min_date=None, max_date=None):
        self.cluster_names = cluster_names  # type: str
        self.app_versions = app_versions  # type: str
        self.level = level              # type: str
        self.out_app_info_params = out_app_info_params  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.min_date = min_date        # type: str
        self.max_date = max_date        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ClusterNames'] = self.cluster_names
        result['AppVersions'] = self.app_versions
        result['Level'] = self.level
        result['OutAppInfoParams'] = self.out_app_info_params
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['MinDate'] = self.min_date
        result['MaxDate'] = self.max_date
        return result

    def from_map(self, map={}):
        self.cluster_names = map.get('ClusterNames')
        self.app_versions = map.get('AppVersions')
        self.level = map.get('Level')
        self.out_app_info_params = map.get('OutAppInfoParams')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.min_date = map.get('MinDate')
        self.max_date = map.get('MaxDate')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, applications=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.applications = applications  # type: ListApplicationsResponseApplications

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.applications, 'applications')
        if self.applications:
            self.applications.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.applications is not None:
            result['Applications'] = self.applications.to_map()
        else:
            result['Applications'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Applications') is not None:
            temp_model = ListApplicationsResponseApplications()
            self.applications = temp_model.from_map(map['Applications'])
        else:
            self.applications = None
        return self


class ListApplicationsResponseApplicationsApplicationAppListApp(TeaModel):
    def __init__(self, app_id=None, app_info=None):
        self.app_id = app_id            # type: str
        self.app_info = app_info        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_info, 'app_info')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['AppInfo'] = self.app_info
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.app_info = map.get('AppInfo')
        return self


class ListApplicationsResponseApplicationsApplicationAppList(TeaModel):
    def __init__(self, app=None):
        self.app = app                  # type: List[ListApplicationsResponseApplicationsApplicationAppListApp]

    def validate(self):
        self.validate_required(self.app, 'app')
        if self.app:
            for k in self.app:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['App'] = []
        if self.app is not None:
            for k in self.app:
                result['App'].append(k.to_map() if k else None)
        else:
            result['App'] = None
        return result

    def from_map(self, map={}):
        self.app = []
        if map.get('App') is not None:
            for k in map.get('App'):
                temp_model = ListApplicationsResponseApplicationsApplicationAppListApp()
                self.app.append(temp_model.from_map(k))
        else:
            self.app = None
        return self


class ListApplicationsResponseApplicationsApplication(TeaModel):
    def __init__(self, cluster_name=None, app_list=None):
        self.cluster_name = cluster_name  # type: str
        self.app_list = app_list        # type: ListApplicationsResponseApplicationsApplicationAppList

    def validate(self):
        self.validate_required(self.cluster_name, 'cluster_name')
        self.validate_required(self.app_list, 'app_list')
        if self.app_list:
            self.app_list.validate()

    def to_map(self):
        result = {}
        result['ClusterName'] = self.cluster_name
        if self.app_list is not None:
            result['AppList'] = self.app_list.to_map()
        else:
            result['AppList'] = None
        return result

    def from_map(self, map={}):
        self.cluster_name = map.get('ClusterName')
        if map.get('AppList') is not None:
            temp_model = ListApplicationsResponseApplicationsApplicationAppList()
            self.app_list = temp_model.from_map(map['AppList'])
        else:
            self.app_list = None
        return self


class ListApplicationsResponseApplications(TeaModel):
    def __init__(self, application=None):
        self.application = application  # type: List[ListApplicationsResponseApplicationsApplication]

    def validate(self):
        self.validate_required(self.application, 'application')
        if self.application:
            for k in self.application:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Application'] = []
        if self.application is not None:
            for k in self.application:
                result['Application'].append(k.to_map() if k else None)
        else:
            result['Application'] = None
        return result

    def from_map(self, map={}):
        self.application = []
        if map.get('Application') is not None:
            for k in map.get('Application'):
                temp_model = ListApplicationsResponseApplicationsApplication()
                self.application.append(temp_model.from_map(k))
        else:
            self.application = None
        return self


class DescribeServcieScheduleRequest(TeaModel):
    def __init__(self, app_id=None, uuid=None, pod_config_name=None):
        self.app_id = app_id            # type: str
        self.uuid = uuid                # type: str
        self.pod_config_name = pod_config_name  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.uuid, 'uuid')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['Uuid'] = self.uuid
        result['PodConfigName'] = self.pod_config_name
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.uuid = map.get('Uuid')
        self.pod_config_name = map.get('PodConfigName')
        return self


class DescribeServcieScheduleResponse(TeaModel):
    def __init__(self, request_id=None, instance_id=None, instance_ip=None, instance_port=None, index=None,
                 tcp_ports=None, request_repeated=None, pod_abstract_info=None):
        self.request_id = request_id    # type: str
        self.instance_id = instance_id  # type: str
        self.instance_ip = instance_ip  # type: str
        self.instance_port = instance_port  # type: int
        self.index = index              # type: int
        self.tcp_ports = tcp_ports      # type: str
        self.request_repeated = request_repeated  # type: bool
        self.pod_abstract_info = pod_abstract_info  # type: DescribeServcieScheduleResponsePodAbstractInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_ip, 'instance_ip')
        self.validate_required(self.instance_port, 'instance_port')
        self.validate_required(self.index, 'index')
        self.validate_required(self.tcp_ports, 'tcp_ports')
        self.validate_required(self.request_repeated, 'request_repeated')
        self.validate_required(self.pod_abstract_info, 'pod_abstract_info')
        if self.pod_abstract_info:
            self.pod_abstract_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InstanceId'] = self.instance_id
        result['InstanceIp'] = self.instance_ip
        result['InstancePort'] = self.instance_port
        result['Index'] = self.index
        result['TcpPorts'] = self.tcp_ports
        result['RequestRepeated'] = self.request_repeated
        if self.pod_abstract_info is not None:
            result['PodAbstractInfo'] = self.pod_abstract_info.to_map()
        else:
            result['PodAbstractInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.instance_id = map.get('InstanceId')
        self.instance_ip = map.get('InstanceIp')
        self.instance_port = map.get('InstancePort')
        self.index = map.get('Index')
        self.tcp_ports = map.get('TcpPorts')
        self.request_repeated = map.get('RequestRepeated')
        if map.get('PodAbstractInfo') is not None:
            temp_model = DescribeServcieScheduleResponsePodAbstractInfo()
            self.pod_abstract_info = temp_model.from_map(map['PodAbstractInfo'])
        else:
            self.pod_abstract_info = None
        return self


class DescribeServcieScheduleResponsePodAbstractInfoContainerStatusesContainerStatus(TeaModel):
    def __init__(self, name=None, container_id=None):
        self.name = name                # type: str
        self.container_id = container_id  # type: str

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.container_id, 'container_id')

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['ContainerId'] = self.container_id
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.container_id = map.get('ContainerId')
        return self


class DescribeServcieScheduleResponsePodAbstractInfoContainerStatuses(TeaModel):
    def __init__(self, container_status=None):
        self.container_status = container_status  # type: List[DescribeServcieScheduleResponsePodAbstractInfoContainerStatusesContainerStatus]

    def validate(self):
        self.validate_required(self.container_status, 'container_status')
        if self.container_status:
            for k in self.container_status:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ContainerStatus'] = []
        if self.container_status is not None:
            for k in self.container_status:
                result['ContainerStatus'].append(k.to_map() if k else None)
        else:
            result['ContainerStatus'] = None
        return result

    def from_map(self, map={}):
        self.container_status = []
        if map.get('ContainerStatus') is not None:
            for k in map.get('ContainerStatus'):
                temp_model = DescribeServcieScheduleResponsePodAbstractInfoContainerStatusesContainerStatus()
                self.container_status.append(temp_model.from_map(k))
        else:
            self.container_status = None
        return self


class DescribeServcieScheduleResponsePodAbstractInfo(TeaModel):
    def __init__(self, name=None, resource_scope=None, container_service=None, namespace=None, status=None,
                 container_statuses=None):
        self.name = name                # type: bool
        self.resource_scope = resource_scope  # type: bool
        self.container_service = container_service  # type: bool
        self.namespace = namespace      # type: bool
        self.status = status            # type: bool
        self.container_statuses = container_statuses  # type: DescribeServcieScheduleResponsePodAbstractInfoContainerStatuses

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.resource_scope, 'resource_scope')
        self.validate_required(self.container_service, 'container_service')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.status, 'status')
        self.validate_required(self.container_statuses, 'container_statuses')
        if self.container_statuses:
            self.container_statuses.validate()

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['ResourceScope'] = self.resource_scope
        result['ContainerService'] = self.container_service
        result['Namespace'] = self.namespace
        result['Status'] = self.status
        if self.container_statuses is not None:
            result['ContainerStatuses'] = self.container_statuses.to_map()
        else:
            result['ContainerStatuses'] = None
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.resource_scope = map.get('ResourceScope')
        self.container_service = map.get('ContainerService')
        self.namespace = map.get('Namespace')
        self.status = map.get('Status')
        if map.get('ContainerStatuses') is not None:
            temp_model = DescribeServcieScheduleResponsePodAbstractInfoContainerStatuses()
            self.container_statuses = temp_model.from_map(map['ContainerStatuses'])
        else:
            self.container_statuses = None
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(self, app_id=None, timeout=None):
        self.app_id = app_id            # type: str
        self.timeout = timeout          # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['Timeout'] = self.timeout
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.timeout = map.get('Timeout')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None, epninstance_name=None, networking_model=None,
                 internet_max_bandwidth_out=None):
        self.epninstance_id = epninstance_id  # type: str
        self.epninstance_name = epninstance_name  # type: str
        self.networking_model = networking_model  # type: str
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        result['EPNInstanceName'] = self.epninstance_name
        result['NetworkingModel'] = self.networking_model
        result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        self.epninstance_name = map.get('EPNInstanceName')
        self.networking_model = map.get('NetworkingModel')
        self.internet_max_bandwidth_out = map.get('InternetMaxBandwidthOut')
        return self


class ModifyEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RollbackApplicationRequest(TeaModel):
    def __init__(self, app_id=None, from_app_version=None, to_app_version=None, timeout=None):
        self.app_id = app_id            # type: str
        self.from_app_version = from_app_version  # type: str
        self.to_app_version = to_app_version  # type: str
        self.timeout = timeout          # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.from_app_version, 'from_app_version')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['FromAppVersion'] = self.from_app_version
        result['ToAppVersion'] = self.to_app_version
        result['Timeout'] = self.timeout
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.from_app_version = map.get('FromAppVersion')
        self.to_app_version = map.get('ToAppVersion')
        self.timeout = map.get('Timeout')
        return self


class RollbackApplicationResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeEpnInstanceAttributeRequest(TeaModel):
    def __init__(self, epninstance_id=None):
        self.epninstance_id = epninstance_id  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        return self


class DescribeEpnInstanceAttributeResponse(TeaModel):
    def __init__(self, request_id=None, epninstance_id=None, epninstance_name=None, networking_model=None,
                 v_switches=None, instances=None, conf_versions=None):
        self.request_id = request_id    # type: str
        self.epninstance_id = epninstance_id  # type: str
        self.epninstance_name = epninstance_name  # type: str
        self.networking_model = networking_model  # type: str
        self.v_switches = v_switches    # type: List[DescribeEpnInstanceAttributeResponseVSwitches]
        self.instances = instances      # type: List[DescribeEpnInstanceAttributeResponseInstances]
        self.conf_versions = conf_versions  # type: List[DescribeEpnInstanceAttributeResponseConfVersions]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.epninstance_id, 'epninstance_id')
        self.validate_required(self.epninstance_name, 'epninstance_name')
        self.validate_required(self.networking_model, 'networking_model')
        self.validate_required(self.v_switches, 'v_switches')
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()
        self.validate_required(self.instances, 'instances')
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()
        self.validate_required(self.conf_versions, 'conf_versions')
        if self.conf_versions:
            for k in self.conf_versions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['EPNInstanceId'] = self.epninstance_id
        result['EPNInstanceName'] = self.epninstance_name
        result['NetworkingModel'] = self.networking_model
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        else:
            result['VSwitches'] = None
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        else:
            result['Instances'] = None
        result['ConfVersions'] = []
        if self.conf_versions is not None:
            for k in self.conf_versions:
                result['ConfVersions'].append(k.to_map() if k else None)
        else:
            result['ConfVersions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.epninstance_id = map.get('EPNInstanceId')
        self.epninstance_name = map.get('EPNInstanceName')
        self.networking_model = map.get('NetworkingModel')
        self.v_switches = []
        if map.get('VSwitches') is not None:
            for k in map.get('VSwitches'):
                temp_model = DescribeEpnInstanceAttributeResponseVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        else:
            self.v_switches = None
        self.instances = []
        if map.get('Instances') is not None:
            for k in map.get('Instances'):
                temp_model = DescribeEpnInstanceAttributeResponseInstances()
                self.instances.append(temp_model.from_map(k))
        else:
            self.instances = None
        self.conf_versions = []
        if map.get('ConfVersions') is not None:
            for k in map.get('ConfVersions'):
                temp_model = DescribeEpnInstanceAttributeResponseConfVersions()
                self.conf_versions.append(temp_model.from_map(k))
        else:
            self.conf_versions = None
        return self


class DescribeEpnInstanceAttributeResponseVSwitches(TeaModel):
    def __init__(self, v_switch_id=None, ens_region_id=None, cidr_block=None, v_switch_name=None):
        self.v_switch_id = v_switch_id  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.cidr_block = cidr_block    # type: str
        self.v_switch_name = v_switch_name  # type: str

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.cidr_block, 'cidr_block')
        self.validate_required(self.v_switch_name, 'v_switch_name')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        result['EnsRegionId'] = self.ens_region_id
        result['CidrBlock'] = self.cidr_block
        result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        self.ens_region_id = map.get('EnsRegionId')
        self.cidr_block = map.get('CidrBlock')
        self.v_switch_name = map.get('VSwitchName')
        return self


class DescribeEpnInstanceAttributeResponseInstances(TeaModel):
    def __init__(self, instance_id=None, public_ip_address=None, ens_region_id=None, isp=None, instance_name=None,
                 private_ip_address=None, status=None):
        self.instance_id = instance_id  # type: str
        self.public_ip_address = public_ip_address  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.isp = isp                  # type: str
        self.instance_name = instance_name  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.public_ip_address, 'public_ip_address')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.private_ip_address, 'private_ip_address')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['PublicIpAddress'] = self.public_ip_address
        result['EnsRegionId'] = self.ens_region_id
        result['Isp'] = self.isp
        result['InstanceName'] = self.instance_name
        result['PrivateIpAddress'] = self.private_ip_address
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.public_ip_address = map.get('PublicIpAddress')
        self.ens_region_id = map.get('EnsRegionId')
        self.isp = map.get('Isp')
        self.instance_name = map.get('InstanceName')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.status = map.get('Status')
        return self


class DescribeEpnInstanceAttributeResponseConfVersions(TeaModel):
    def __init__(self, ens_region_id=None, conf_version=None):
        self.ens_region_id = ens_region_id  # type: str
        self.conf_version = conf_version  # type: str

    def validate(self):
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.conf_version, 'conf_version')

    def to_map(self):
        result = {}
        result['EnsRegionId'] = self.ens_region_id
        result['ConfVersion'] = self.conf_version
        return result

    def from_map(self, map={}):
        self.ens_region_id = map.get('EnsRegionId')
        self.conf_version = map.get('ConfVersion')
        return self


class RunServiceScheduleRequest(TeaModel):
    def __init__(self, app_id=None, uuid=None, client_ip=None, service_action=None, pod_config_name=None,
                 pre_locked_timeout=None, directorys=None, service_commands=None, schedule_strategy=None):
        self.app_id = app_id            # type: str
        self.uuid = uuid                # type: str
        self.client_ip = client_ip      # type: str
        self.service_action = service_action  # type: str
        self.pod_config_name = pod_config_name  # type: str
        self.pre_locked_timeout = pre_locked_timeout  # type: int
        self.directorys = directorys    # type: str
        self.service_commands = service_commands  # type: str
        self.schedule_strategy = schedule_strategy  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.service_action, 'service_action')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['Uuid'] = self.uuid
        result['ClientIp'] = self.client_ip
        result['ServiceAction'] = self.service_action
        result['PodConfigName'] = self.pod_config_name
        result['PreLockedTimeout'] = self.pre_locked_timeout
        result['Directorys'] = self.directorys
        result['ServiceCommands'] = self.service_commands
        result['ScheduleStrategy'] = self.schedule_strategy
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.uuid = map.get('Uuid')
        self.client_ip = map.get('ClientIp')
        self.service_action = map.get('ServiceAction')
        self.pod_config_name = map.get('PodConfigName')
        self.pre_locked_timeout = map.get('PreLockedTimeout')
        self.directorys = map.get('Directorys')
        self.service_commands = map.get('ServiceCommands')
        self.schedule_strategy = map.get('ScheduleStrategy')
        return self


class RunServiceScheduleResponse(TeaModel):
    def __init__(self, request_id=None, request_repeated=None, tcp_ports=None, instance_id=None, instance_port=None,
                 instance_ip=None, index=None, command_results=None):
        self.request_id = request_id    # type: str
        self.request_repeated = request_repeated  # type: str
        self.tcp_ports = tcp_ports      # type: bool
        self.instance_id = instance_id  # type: str
        self.instance_port = instance_port  # type: int
        self.instance_ip = instance_ip  # type: str
        self.index = index              # type: int
        self.command_results = command_results  # type: RunServiceScheduleResponseCommandResults

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.request_repeated, 'request_repeated')
        self.validate_required(self.tcp_ports, 'tcp_ports')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_port, 'instance_port')
        self.validate_required(self.instance_ip, 'instance_ip')
        self.validate_required(self.index, 'index')
        self.validate_required(self.command_results, 'command_results')
        if self.command_results:
            self.command_results.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RequestRepeated'] = self.request_repeated
        result['TcpPorts'] = self.tcp_ports
        result['InstanceId'] = self.instance_id
        result['InstancePort'] = self.instance_port
        result['InstanceIp'] = self.instance_ip
        result['Index'] = self.index
        if self.command_results is not None:
            result['CommandResults'] = self.command_results.to_map()
        else:
            result['CommandResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.request_repeated = map.get('RequestRepeated')
        self.tcp_ports = map.get('TcpPorts')
        self.instance_id = map.get('InstanceId')
        self.instance_port = map.get('InstancePort')
        self.instance_ip = map.get('InstanceIp')
        self.index = map.get('Index')
        if map.get('CommandResults') is not None:
            temp_model = RunServiceScheduleResponseCommandResults()
            self.command_results = temp_model.from_map(map['CommandResults'])
        else:
            self.command_results = None
        return self


class RunServiceScheduleResponseCommandResultsCommandResult(TeaModel):
    def __init__(self, container_name=None, command=None, result_msg=None):
        self.container_name = container_name  # type: str
        self.command = command          # type: str
        self.result_msg = result_msg    # type: str

    def validate(self):
        self.validate_required(self.container_name, 'container_name')
        self.validate_required(self.command, 'command')
        self.validate_required(self.result_msg, 'result_msg')

    def to_map(self):
        result = {}
        result['ContainerName'] = self.container_name
        result['Command'] = self.command
        result['ResultMsg'] = self.result_msg
        return result

    def from_map(self, map={}):
        self.container_name = map.get('ContainerName')
        self.command = map.get('Command')
        self.result_msg = map.get('ResultMsg')
        return self


class RunServiceScheduleResponseCommandResults(TeaModel):
    def __init__(self, command_result=None):
        self.command_result = command_result  # type: List[RunServiceScheduleResponseCommandResultsCommandResult]

    def validate(self):
        self.validate_required(self.command_result, 'command_result')
        if self.command_result:
            for k in self.command_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CommandResult'] = []
        if self.command_result is not None:
            for k in self.command_result:
                result['CommandResult'].append(k.to_map() if k else None)
        else:
            result['CommandResult'] = None
        return result

    def from_map(self, map={}):
        self.command_result = []
        if map.get('CommandResult') is not None:
            for k in map.get('CommandResult'):
                temp_model = RunServiceScheduleResponseCommandResultsCommandResult()
                self.command_result.append(temp_model.from_map(k))
        else:
            self.command_result = None
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, template=None, timeout=None):
        self.template = template        # type: str
        self.timeout = timeout          # type: int

    def validate(self):
        self.validate_required(self.template, 'template')

    def to_map(self):
        result = {}
        result['Template'] = self.template
        result['Timeout'] = self.timeout
        return result

    def from_map(self, map={}):
        self.template = map.get('Template')
        self.timeout = map.get('Timeout')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, request_id=None, app_id=None):
        self.request_id = request_id    # type: str
        self.app_id = app_id            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AppId'] = self.app_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.app_id = map.get('AppId')
        return self


class CreateEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_type=None, epninstance_name=None, internet_charge_type=None,
                 networking_model=None, internet_max_bandwidth_out=None):
        self.epninstance_type = epninstance_type  # type: str
        self.epninstance_name = epninstance_name  # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.networking_model = networking_model  # type: str
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int

    def validate(self):
        self.validate_required(self.epninstance_type, 'epninstance_type')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.networking_model, 'networking_model')
        self.validate_required(self.internet_max_bandwidth_out, 'internet_max_bandwidth_out')

    def to_map(self):
        result = {}
        result['EPNInstanceType'] = self.epninstance_type
        result['EPNInstanceName'] = self.epninstance_name
        result['InternetChargeType'] = self.internet_charge_type
        result['NetworkingModel'] = self.networking_model
        result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        return result

    def from_map(self, map={}):
        self.epninstance_type = map.get('EPNInstanceType')
        self.epninstance_name = map.get('EPNInstanceName')
        self.internet_charge_type = map.get('InternetChargeType')
        self.networking_model = map.get('NetworkingModel')
        self.internet_max_bandwidth_out = map.get('InternetMaxBandwidthOut')
        return self


class CreateEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None, epninstance_id=None):
        self.request_id = request_id    # type: str
        self.epninstance_id = epninstance_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.epninstance_id, 'epninstance_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.epninstance_id = map.get('EPNInstanceId')
        return self


class StopEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None):
        self.epninstance_id = epninstance_id  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        return self


class StopEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeDataDistResultRequest(TeaModel):
    def __init__(self, app_id=None, data_names=None, data_versions=None, instance_ids=None, min_date=None,
                 max_date=None, page_number=None, page_size=None):
        self.app_id = app_id            # type: str
        self.data_names = data_names    # type: str
        self.data_versions = data_versions  # type: str
        self.instance_ids = instance_ids  # type: str
        self.min_date = min_date        # type: str
        self.max_date = max_date        # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['DataNames'] = self.data_names
        result['DataVersions'] = self.data_versions
        result['InstanceIds'] = self.instance_ids
        result['MinDate'] = self.min_date
        result['MaxDate'] = self.max_date
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.data_names = map.get('DataNames')
        self.data_versions = map.get('DataVersions')
        self.instance_ids = map.get('InstanceIds')
        self.min_date = map.get('MinDate')
        self.max_date = map.get('MaxDate')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeDataDistResultResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, dist_results=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.dist_results = dist_results  # type: DescribeDataDistResultResponseDistResults

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.dist_results, 'dist_results')
        if self.dist_results:
            self.dist_results.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.dist_results is not None:
            result['DistResults'] = self.dist_results.to_map()
        else:
            result['DistResults'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('DistResults') is not None:
            temp_model = DescribeDataDistResultResponseDistResults()
            self.dist_results = temp_model.from_map(map['DistResults'])
        else:
            self.dist_results = None
        return self


class DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStatInstancesInstance(TeaModel):
    def __init__(self, instance_id=None, start_time=None, update_time=None, status_descrip=None):
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: str
        self.update_time = update_time  # type: str
        self.status_descrip = status_descrip  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.status_descrip, 'status_descrip')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['StartTime'] = self.start_time
        result['UpdateTime'] = self.update_time
        result['StatusDescrip'] = self.status_descrip
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.start_time = map.get('StartTime')
        self.update_time = map.get('UpdateTime')
        self.status_descrip = map.get('StatusDescrip')
        return self


class DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStatInstances(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance        # type: List[DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStatInstancesInstance]

    def validate(self):
        self.validate_required(self.instance, 'instance')
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        else:
            result['Instance'] = None
        return result

    def from_map(self, map={}):
        self.instance = []
        if map.get('Instance') is not None:
            for k in map.get('Instance'):
                temp_model = DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStatInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        else:
            self.instance = None
        return self


class DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStat(TeaModel):
    def __init__(self, status=None, instance_count=None, instances=None):
        self.status = status            # type: str
        self.instance_count = instance_count  # type: str
        self.instances = instances      # type: DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStatInstances

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.instance_count, 'instance_count')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = {}
        result['Status'] = self.status
        result['InstanceCount'] = self.instance_count
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        else:
            result['Instances'] = None
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        self.instance_count = map.get('InstanceCount')
        if map.get('Instances') is not None:
            temp_model = DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStatInstances()
            self.instances = temp_model.from_map(map['Instances'])
        else:
            self.instances = None
        return self


class DescribeDataDistResultResponseDistResultsDistResultStatusStats(TeaModel):
    def __init__(self, status_stat=None):
        self.status_stat = status_stat  # type: List[DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStat]

    def validate(self):
        self.validate_required(self.status_stat, 'status_stat')
        if self.status_stat:
            for k in self.status_stat:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StatusStat'] = []
        if self.status_stat is not None:
            for k in self.status_stat:
                result['StatusStat'].append(k.to_map() if k else None)
        else:
            result['StatusStat'] = None
        return result

    def from_map(self, map={}):
        self.status_stat = []
        if map.get('StatusStat') is not None:
            for k in map.get('StatusStat'):
                temp_model = DescribeDataDistResultResponseDistResultsDistResultStatusStatsStatusStat()
                self.status_stat.append(temp_model.from_map(k))
        else:
            self.status_stat = None
        return self


class DescribeDataDistResultResponseDistResultsDistResult(TeaModel):
    def __init__(self, version=None, name=None, status_stats=None):
        self.version = version          # type: str
        self.name = name                # type: str
        self.status_stats = status_stats  # type: DescribeDataDistResultResponseDistResultsDistResultStatusStats

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.name, 'name')
        self.validate_required(self.status_stats, 'status_stats')
        if self.status_stats:
            self.status_stats.validate()

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['Name'] = self.name
        if self.status_stats is not None:
            result['StatusStats'] = self.status_stats.to_map()
        else:
            result['StatusStats'] = None
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.name = map.get('Name')
        if map.get('StatusStats') is not None:
            temp_model = DescribeDataDistResultResponseDistResultsDistResultStatusStats()
            self.status_stats = temp_model.from_map(map['StatusStats'])
        else:
            self.status_stats = None
        return self


class DescribeDataDistResultResponseDistResults(TeaModel):
    def __init__(self, dist_result=None):
        self.dist_result = dist_result  # type: List[DescribeDataDistResultResponseDistResultsDistResult]

    def validate(self):
        self.validate_required(self.dist_result, 'dist_result')
        if self.dist_result:
            for k in self.dist_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DistResult'] = []
        if self.dist_result is not None:
            for k in self.dist_result:
                result['DistResult'].append(k.to_map() if k else None)
        else:
            result['DistResult'] = None
        return result

    def from_map(self, map={}):
        self.dist_result = []
        if map.get('DistResult') is not None:
            for k in map.get('DistResult'):
                temp_model = DescribeDataDistResultResponseDistResultsDistResult()
                self.dist_result.append(temp_model.from_map(k))
        else:
            self.dist_result = None
        return self


class DescribeEpnInstancesRequest(TeaModel):
    def __init__(self, epninstance_id=None, epninstance_name=None, page_number=None, page_size=None):
        self.epninstance_id = epninstance_id  # type: str
        self.epninstance_name = epninstance_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        result['EPNInstanceName'] = self.epninstance_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        self.epninstance_name = map.get('EPNInstanceName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeEpnInstancesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, epninstances=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.epninstances = epninstances  # type: DescribeEpnInstancesResponseEPNInstances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.epninstances, 'epninstances')
        if self.epninstances:
            self.epninstances.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.epninstances is not None:
            result['EPNInstances'] = self.epninstances.to_map()
        else:
            result['EPNInstances'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('EPNInstances') is not None:
            temp_model = DescribeEpnInstancesResponseEPNInstances()
            self.epninstances = temp_model.from_map(map['EPNInstances'])
        else:
            self.epninstances = None
        return self


class DescribeEpnInstancesResponseEPNInstancesEPNInstance(TeaModel):
    def __init__(self, epninstance_id=None, epninstance_name=None, networking_model=None, modify_time=None,
                 epninstance_type=None, status=None, internet_max_bandwidth_out=None, creation_time=None, start_time=None,
                 end_time=None):
        self.epninstance_id = epninstance_id  # type: str
        self.epninstance_name = epninstance_name  # type: str
        self.networking_model = networking_model  # type: str
        self.modify_time = modify_time  # type: str
        self.epninstance_type = epninstance_type  # type: str
        self.status = status            # type: str
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.creation_time = creation_time  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')
        self.validate_required(self.epninstance_name, 'epninstance_name')
        self.validate_required(self.networking_model, 'networking_model')
        self.validate_required(self.modify_time, 'modify_time')
        self.validate_required(self.epninstance_type, 'epninstance_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.internet_max_bandwidth_out, 'internet_max_bandwidth_out')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        result['EPNInstanceName'] = self.epninstance_name
        result['NetworkingModel'] = self.networking_model
        result['ModifyTime'] = self.modify_time
        result['EPNInstanceType'] = self.epninstance_type
        result['Status'] = self.status
        result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        result['CreationTime'] = self.creation_time
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        self.epninstance_name = map.get('EPNInstanceName')
        self.networking_model = map.get('NetworkingModel')
        self.modify_time = map.get('ModifyTime')
        self.epninstance_type = map.get('EPNInstanceType')
        self.status = map.get('Status')
        self.internet_max_bandwidth_out = map.get('InternetMaxBandwidthOut')
        self.creation_time = map.get('CreationTime')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeEpnInstancesResponseEPNInstances(TeaModel):
    def __init__(self, epninstance=None):
        self.epninstance = epninstance  # type: List[DescribeEpnInstancesResponseEPNInstancesEPNInstance]

    def validate(self):
        self.validate_required(self.epninstance, 'epninstance')
        if self.epninstance:
            for k in self.epninstance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EPNInstance'] = []
        if self.epninstance is not None:
            for k in self.epninstance:
                result['EPNInstance'].append(k.to_map() if k else None)
        else:
            result['EPNInstance'] = None
        return result

    def from_map(self, map={}):
        self.epninstance = []
        if map.get('EPNInstance') is not None:
            for k in map.get('EPNInstance'):
                temp_model = DescribeEpnInstancesResponseEPNInstancesEPNInstance()
                self.epninstance.append(temp_model.from_map(k))
        else:
            self.epninstance = None
        return self


class RemovePublicIpsFromEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None, instance_infos=None):
        self.epninstance_id = epninstance_id  # type: str
        self.instance_infos = instance_infos  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')
        self.validate_required(self.instance_infos, 'instance_infos')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        self.instance_infos = map.get('InstanceInfos')
        return self


class RemovePublicIpsFromEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class JoinPublicIpsToEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None, instance_infos=None):
        self.epninstance_id = epninstance_id  # type: str
        self.instance_infos = instance_infos  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')
        self.validate_required(self.instance_infos, 'instance_infos')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        result['InstanceInfos'] = self.instance_infos
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        self.instance_infos = map.get('InstanceInfos')
        return self


class JoinPublicIpsToEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeApplicationResourceSummaryRequest(TeaModel):
    def __init__(self, level=None, resource_type=None):
        self.level = level              # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Level'] = self.level
        result['ResourceType'] = self.resource_type
        return result

    def from_map(self, map={}):
        self.level = map.get('Level')
        self.resource_type = map.get('ResourceType')
        return self


class DescribeApplicationResourceSummaryResponse(TeaModel):
    def __init__(self, request_id=None, application_resource=None):
        self.request_id = request_id    # type: str
        self.application_resource = application_resource  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.application_resource, 'application_resource')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ApplicationResource'] = self.application_resource
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.application_resource = map.get('ApplicationResource')
        return self


class StartEpnInstanceRequest(TeaModel):
    def __init__(self, epninstance_id=None):
        self.epninstance_id = epninstance_id  # type: str

    def validate(self):
        self.validate_required(self.epninstance_id, 'epninstance_id')

    def to_map(self):
        result = {}
        result['EPNInstanceId'] = self.epninstance_id
        return result

    def from_map(self, map={}):
        self.epninstance_id = map.get('EPNInstanceId')
        return self


class StartEpnInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeExportImageInfoRequest(TeaModel):
    def __init__(self, image_id=None, image_name=None, page_number=None, page_size=None):
        self.image_id = image_id        # type: str
        self.image_name = image_name    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['ImageName'] = self.image_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.image_name = map.get('ImageName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeExportImageInfoResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, images=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.images = images            # type: DescribeExportImageInfoResponseImages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.images, 'images')
        if self.images:
            self.images.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.images is not None:
            result['Images'] = self.images.to_map()
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Images') is not None:
            temp_model = DescribeExportImageInfoResponseImages()
            self.images = temp_model.from_map(map['Images'])
        else:
            self.images = None
        return self


class DescribeExportImageInfoResponseImagesImage(TeaModel):
    def __init__(self, creation_time=None, image_id=None, image_name=None, architecture=None,
                 image_owner_alias=None, platform=None, image_export_status=None, exported_image_url=None):
        self.creation_time = creation_time  # type: str
        self.image_id = image_id        # type: str
        self.image_name = image_name    # type: str
        self.architecture = architecture  # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.platform = platform        # type: str
        self.image_export_status = image_export_status  # type: str
        self.exported_image_url = exported_image_url  # type: str

    def validate(self):
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_name, 'image_name')
        self.validate_required(self.architecture, 'architecture')
        self.validate_required(self.image_owner_alias, 'image_owner_alias')
        self.validate_required(self.platform, 'platform')
        self.validate_required(self.image_export_status, 'image_export_status')
        self.validate_required(self.exported_image_url, 'exported_image_url')

    def to_map(self):
        result = {}
        result['CreationTime'] = self.creation_time
        result['ImageId'] = self.image_id
        result['ImageName'] = self.image_name
        result['Architecture'] = self.architecture
        result['ImageOwnerAlias'] = self.image_owner_alias
        result['Platform'] = self.platform
        result['ImageExportStatus'] = self.image_export_status
        result['ExportedImageURL'] = self.exported_image_url
        return result

    def from_map(self, map={}):
        self.creation_time = map.get('CreationTime')
        self.image_id = map.get('ImageId')
        self.image_name = map.get('ImageName')
        self.architecture = map.get('Architecture')
        self.image_owner_alias = map.get('ImageOwnerAlias')
        self.platform = map.get('Platform')
        self.image_export_status = map.get('ImageExportStatus')
        self.exported_image_url = map.get('ExportedImageURL')
        return self


class DescribeExportImageInfoResponseImages(TeaModel):
    def __init__(self, image=None):
        self.image = image              # type: List[DescribeExportImageInfoResponseImagesImage]

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        else:
            result['Image'] = None
        return result

    def from_map(self, map={}):
        self.image = []
        if map.get('Image') is not None:
            for k in map.get('Image'):
                temp_model = DescribeExportImageInfoResponseImagesImage()
                self.image.append(temp_model.from_map(k))
        else:
            self.image = None
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, v_switch_id=None, v_switch_name=None, page_number=None,
                 page_size=None, order_by_params=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.v_switch_name = v_switch_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.order_by_params = order_by_params  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['VSwitchId'] = self.v_switch_id
        result['VSwitchName'] = self.v_switch_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['OrderByParams'] = self.order_by_params
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.v_switch_id = map.get('VSwitchId')
        self.v_switch_name = map.get('VSwitchName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.order_by_params = map.get('OrderByParams')
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, v_switches=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.v_switches = v_switches    # type: DescribeVSwitchesResponseVSwitches

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.v_switches, 'v_switches')
        if self.v_switches:
            self.v_switches.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches.to_map()
        else:
            result['VSwitches'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('VSwitches') is not None:
            temp_model = DescribeVSwitchesResponseVSwitches()
            self.v_switches = temp_model.from_map(map['VSwitches'])
        else:
            self.v_switches = None
        return self


class DescribeVSwitchesResponseVSwitchesVSwitch(TeaModel):
    def __init__(self, v_switch_id=None, v_switch_name=None, status=None, cidr_block=None, ens_region_id=None,
                 free_ip_count=None, created_time=None):
        self.v_switch_id = v_switch_id  # type: str
        self.v_switch_name = v_switch_name  # type: str
        self.status = status            # type: str
        self.cidr_block = cidr_block    # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.free_ip_count = free_ip_count  # type: int
        self.created_time = created_time  # type: str

    def validate(self):
        self.validate_required(self.v_switch_id, 'v_switch_id')
        self.validate_required(self.v_switch_name, 'v_switch_name')
        self.validate_required(self.status, 'status')
        self.validate_required(self.cidr_block, 'cidr_block')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.free_ip_count, 'free_ip_count')
        self.validate_required(self.created_time, 'created_time')

    def to_map(self):
        result = {}
        result['VSwitchId'] = self.v_switch_id
        result['VSwitchName'] = self.v_switch_name
        result['Status'] = self.status
        result['CidrBlock'] = self.cidr_block
        result['EnsRegionId'] = self.ens_region_id
        result['FreeIpCount'] = self.free_ip_count
        result['CreatedTime'] = self.created_time
        return result

    def from_map(self, map={}):
        self.v_switch_id = map.get('VSwitchId')
        self.v_switch_name = map.get('VSwitchName')
        self.status = map.get('Status')
        self.cidr_block = map.get('CidrBlock')
        self.ens_region_id = map.get('EnsRegionId')
        self.free_ip_count = map.get('FreeIpCount')
        self.created_time = map.get('CreatedTime')
        return self


class DescribeVSwitchesResponseVSwitches(TeaModel):
    def __init__(self, v_switch=None):
        self.v_switch = v_switch        # type: List[DescribeVSwitchesResponseVSwitchesVSwitch]

    def validate(self):
        self.validate_required(self.v_switch, 'v_switch')
        if self.v_switch:
            for k in self.v_switch:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VSwitch'] = []
        if self.v_switch is not None:
            for k in self.v_switch:
                result['VSwitch'].append(k.to_map() if k else None)
        else:
            result['VSwitch'] = None
        return result

    def from_map(self, map={}):
        self.v_switch = []
        if map.get('VSwitch') is not None:
            for k in map.get('VSwitch'):
                temp_model = DescribeVSwitchesResponseVSwitchesVSwitch()
                self.v_switch.append(temp_model.from_map(k))
        else:
            self.v_switch = None
        return self


class DeleteVSwitchRequest(TeaModel):
    def __init__(self, version=None, v_switch_id=None):
        self.version = version          # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.v_switch_id = map.get('VSwitchId')
        return self


class DeleteVSwitchResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateVSwitchRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, cidr_block=None, v_switch_name=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.cidr_block = cidr_block    # type: str
        self.v_switch_name = v_switch_name  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.cidr_block, 'cidr_block')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['CidrBlock'] = self.cidr_block
        result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.cidr_block = map.get('CidrBlock')
        self.v_switch_name = map.get('VSwitchName')
        return self


class CreateVSwitchResponse(TeaModel):
    def __init__(self, request_id=None, v_switch_id=None):
        self.request_id = request_id    # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.v_switch_id, 'v_switch_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.v_switch_id = map.get('VSwitchId')
        return self


class DescribeExportImageStatusRequest(TeaModel):
    def __init__(self, version=None, image_id=None):
        self.version = version          # type: str
        self.image_id = image_id        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['ImageId'] = self.image_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.image_id = map.get('ImageId')
        return self


class DescribeExportImageStatusResponse(TeaModel):
    def __init__(self, request_id=None, image_export_status=None):
        self.request_id = request_id    # type: str
        self.image_export_status = image_export_status  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.image_export_status, 'image_export_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ImageExportStatus'] = self.image_export_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.image_export_status = map.get('ImageExportStatus')
        return self


class ExportImageRequest(TeaModel):
    def __init__(self, version=None, image_id=None, ossbucket=None, ossregion_id=None, ossprefix=None,
                 role_name=None):
        self.version = version          # type: str
        self.image_id = image_id        # type: str
        self.ossbucket = ossbucket      # type: str
        self.ossregion_id = ossregion_id  # type: str
        self.ossprefix = ossprefix      # type: str
        self.role_name = role_name      # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.ossbucket, 'ossbucket')
        self.validate_required(self.ossregion_id, 'ossregion_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['ImageId'] = self.image_id
        result['OSSBucket'] = self.ossbucket
        result['OSSRegionId'] = self.ossregion_id
        result['OSSPrefix'] = self.ossprefix
        result['RoleName'] = self.role_name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.image_id = map.get('ImageId')
        self.ossbucket = map.get('OSSBucket')
        self.ossregion_id = map.get('OSSRegionId')
        self.ossprefix = map.get('OSSPrefix')
        self.role_name = map.get('RoleName')
        return self


class ExportImageResponse(TeaModel):
    def __init__(self, request_id=None, exported_image_url=None):
        self.request_id = request_id    # type: str
        self.exported_image_url = exported_image_url  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.exported_image_url, 'exported_image_url')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ExportedImageURL'] = self.exported_image_url
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.exported_image_url = map.get('ExportedImageURL')
        return self


class ImportKeyPairRequest(TeaModel):
    def __init__(self, version=None, key_pair_name=None, public_key_body=None):
        self.version = version          # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.public_key_body = public_key_body  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.key_pair_name, 'key_pair_name')
        self.validate_required(self.public_key_body, 'public_key_body')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['KeyPairName'] = self.key_pair_name
        result['PublicKeyBody'] = self.public_key_body
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.key_pair_name = map.get('KeyPairName')
        self.public_key_body = map.get('PublicKeyBody')
        return self


class ImportKeyPairResponse(TeaModel):
    def __init__(self, request_id=None, key_pair_name=None, key_pair_finger_print=None):
        self.request_id = request_id    # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.key_pair_finger_print = key_pair_finger_print  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.key_pair_name, 'key_pair_name')
        self.validate_required(self.key_pair_finger_print, 'key_pair_finger_print')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['KeyPairName'] = self.key_pair_name
        result['KeyPairFingerPrint'] = self.key_pair_finger_print
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.key_pair_name = map.get('KeyPairName')
        self.key_pair_finger_print = map.get('KeyPairFingerPrint')
        return self


class DescribeKeyPairsRequest(TeaModel):
    def __init__(self, version=None, key_pair_name=None, page_number=None, page_size=None):
        self.version = version          # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['KeyPairName'] = self.key_pair_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.key_pair_name = map.get('KeyPairName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeKeyPairsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, key_pairs=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.key_pairs = key_pairs      # type: DescribeKeyPairsResponseKeyPairs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.key_pairs, 'key_pairs')
        if self.key_pairs:
            self.key_pairs.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.key_pairs is not None:
            result['KeyPairs'] = self.key_pairs.to_map()
        else:
            result['KeyPairs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('KeyPairs') is not None:
            temp_model = DescribeKeyPairsResponseKeyPairs()
            self.key_pairs = temp_model.from_map(map['KeyPairs'])
        else:
            self.key_pairs = None
        return self


class DescribeKeyPairsResponseKeyPairsKeyPair(TeaModel):
    def __init__(self, creation_time=None, key_pair_name=None, key_pair_finger_print=None):
        self.creation_time = creation_time  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.key_pair_finger_print = key_pair_finger_print  # type: str

    def validate(self):
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.key_pair_name, 'key_pair_name')
        self.validate_required(self.key_pair_finger_print, 'key_pair_finger_print')

    def to_map(self):
        result = {}
        result['CreationTime'] = self.creation_time
        result['KeyPairName'] = self.key_pair_name
        result['KeyPairFingerPrint'] = self.key_pair_finger_print
        return result

    def from_map(self, map={}):
        self.creation_time = map.get('CreationTime')
        self.key_pair_name = map.get('KeyPairName')
        self.key_pair_finger_print = map.get('KeyPairFingerPrint')
        return self


class DescribeKeyPairsResponseKeyPairs(TeaModel):
    def __init__(self, key_pair=None):
        self.key_pair = key_pair        # type: List[DescribeKeyPairsResponseKeyPairsKeyPair]

    def validate(self):
        self.validate_required(self.key_pair, 'key_pair')
        if self.key_pair:
            for k in self.key_pair:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['KeyPair'] = []
        if self.key_pair is not None:
            for k in self.key_pair:
                result['KeyPair'].append(k.to_map() if k else None)
        else:
            result['KeyPair'] = None
        return result

    def from_map(self, map={}):
        self.key_pair = []
        if map.get('KeyPair') is not None:
            for k in map.get('KeyPair'):
                temp_model = DescribeKeyPairsResponseKeyPairsKeyPair()
                self.key_pair.append(temp_model.from_map(k))
        else:
            self.key_pair = None
        return self


class DeleteKeyPairsRequest(TeaModel):
    def __init__(self, version=None, key_pair_name=None):
        self.version = version          # type: str
        self.key_pair_name = key_pair_name  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.key_pair_name, 'key_pair_name')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.key_pair_name = map.get('KeyPairName')
        return self


class DeleteKeyPairsResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateKeyPairRequest(TeaModel):
    def __init__(self, version=None, key_pair_name=None):
        self.version = version          # type: str
        self.key_pair_name = key_pair_name  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.key_pair_name, 'key_pair_name')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['KeyPairName'] = self.key_pair_name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.key_pair_name = map.get('KeyPairName')
        return self


class CreateKeyPairResponse(TeaModel):
    def __init__(self, request_id=None, key_pair_id=None, private_key_body=None, key_pair_name=None,
                 key_pair_finger_print=None):
        self.request_id = request_id    # type: str
        self.key_pair_id = key_pair_id  # type: str
        self.private_key_body = private_key_body  # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.key_pair_finger_print = key_pair_finger_print  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.key_pair_id, 'key_pair_id')
        self.validate_required(self.private_key_body, 'private_key_body')
        self.validate_required(self.key_pair_name, 'key_pair_name')
        self.validate_required(self.key_pair_finger_print, 'key_pair_finger_print')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['KeyPairId'] = self.key_pair_id
        result['PrivateKeyBody'] = self.private_key_body
        result['KeyPairName'] = self.key_pair_name
        result['KeyPairFingerPrint'] = self.key_pair_finger_print
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.key_pair_id = map.get('KeyPairId')
        self.private_key_body = map.get('PrivateKeyBody')
        self.key_pair_name = map.get('KeyPairName')
        self.key_pair_finger_print = map.get('KeyPairFingerPrint')
        return self


class ExportBillDetailDataRequest(TeaModel):
    def __init__(self, version=None, start_date=None, end_date=None):
        self.version = version          # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class ExportBillDetailDataResponse(TeaModel):
    def __init__(self, request_id=None, file_path=None):
        self.request_id = request_id    # type: str
        self.file_path = file_path      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.file_path, 'file_path')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['FilePath'] = self.file_path
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.file_path = map.get('FilePath')
        return self


class DescribeEnsRegionIdResourceRequest(TeaModel):
    def __init__(self, version=None, start_time=None, end_time=None, order_by_params=None, page_number=None,
                 page_size=None, isp=None):
        self.version = version          # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.order_by_params = order_by_params  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: str
        self.isp = isp                  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['OrderByParams'] = self.order_by_params
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Isp'] = self.isp
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.order_by_params = map.get('OrderByParams')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.isp = map.get('Isp')
        return self


class DescribeEnsRegionIdResourceResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None,
                 ens_region_id_resources=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.ens_region_id_resources = ens_region_id_resources  # type: DescribeEnsRegionIdResourceResponseEnsRegionIdResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.ens_region_id_resources, 'ens_region_id_resources')
        if self.ens_region_id_resources:
            self.ens_region_id_resources.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.ens_region_id_resources is not None:
            result['EnsRegionIdResources'] = self.ens_region_id_resources.to_map()
        else:
            result['EnsRegionIdResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('EnsRegionIdResources') is not None:
            temp_model = DescribeEnsRegionIdResourceResponseEnsRegionIdResources()
            self.ens_region_id_resources = temp_model.from_map(map['EnsRegionIdResources'])
        else:
            self.ens_region_id_resources = None
        return self


class DescribeEnsRegionIdResourceResponseEnsRegionIdResourcesEnsRegionIdResource(TeaModel):
    def __init__(self, area=None, area_code=None, ens_region_id=None, ens_region_id_name=None, vcpu=None,
                 internet_bandwidth=None, isp=None, biz_date=None, instance_count=None):
        self.area = area                # type: str
        self.area_code = area_code      # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.ens_region_id_name = ens_region_id_name  # type: str
        self.vcpu = vcpu                # type: int
        self.internet_bandwidth = internet_bandwidth  # type: int
        self.isp = isp                  # type: str
        self.biz_date = biz_date        # type: str
        self.instance_count = instance_count  # type: int

    def validate(self):
        self.validate_required(self.area, 'area')
        self.validate_required(self.area_code, 'area_code')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.ens_region_id_name, 'ens_region_id_name')
        self.validate_required(self.vcpu, 'vcpu')
        self.validate_required(self.internet_bandwidth, 'internet_bandwidth')
        self.validate_required(self.isp, 'isp')
        self.validate_required(self.biz_date, 'biz_date')
        self.validate_required(self.instance_count, 'instance_count')

    def to_map(self):
        result = {}
        result['Area'] = self.area
        result['AreaCode'] = self.area_code
        result['EnsRegionId'] = self.ens_region_id
        result['EnsRegionIdName'] = self.ens_region_id_name
        result['VCpu'] = self.vcpu
        result['InternetBandwidth'] = self.internet_bandwidth
        result['Isp'] = self.isp
        result['BizDate'] = self.biz_date
        result['InstanceCount'] = self.instance_count
        return result

    def from_map(self, map={}):
        self.area = map.get('Area')
        self.area_code = map.get('AreaCode')
        self.ens_region_id = map.get('EnsRegionId')
        self.ens_region_id_name = map.get('EnsRegionIdName')
        self.vcpu = map.get('VCpu')
        self.internet_bandwidth = map.get('InternetBandwidth')
        self.isp = map.get('Isp')
        self.biz_date = map.get('BizDate')
        self.instance_count = map.get('InstanceCount')
        return self


class DescribeEnsRegionIdResourceResponseEnsRegionIdResources(TeaModel):
    def __init__(self, ens_region_id_resource=None):
        self.ens_region_id_resource = ens_region_id_resource  # type: List[DescribeEnsRegionIdResourceResponseEnsRegionIdResourcesEnsRegionIdResource]

    def validate(self):
        self.validate_required(self.ens_region_id_resource, 'ens_region_id_resource')
        if self.ens_region_id_resource:
            for k in self.ens_region_id_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EnsRegionIdResource'] = []
        if self.ens_region_id_resource is not None:
            for k in self.ens_region_id_resource:
                result['EnsRegionIdResource'].append(k.to_map() if k else None)
        else:
            result['EnsRegionIdResource'] = None
        return result

    def from_map(self, map={}):
        self.ens_region_id_resource = []
        if map.get('EnsRegionIdResource') is not None:
            for k in map.get('EnsRegionIdResource'):
                temp_model = DescribeEnsRegionIdResourceResponseEnsRegionIdResourcesEnsRegionIdResource()
                self.ens_region_id_resource.append(temp_model.from_map(k))
        else:
            self.ens_region_id_resource = None
        return self


class DescribeBandwitdhByInternetChargeTypeRequest(TeaModel):
    def __init__(self, version=None, start_time=None, end_time=None, isp=None, ens_region_id=None):
        self.version = version          # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.isp = isp                  # type: str
        self.ens_region_id = ens_region_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Isp'] = self.isp
        result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.isp = map.get('Isp')
        self.ens_region_id = map.get('EnsRegionId')
        return self


class DescribeBandwitdhByInternetChargeTypeResponse(TeaModel):
    def __init__(self, request_id=None, internet_charge_type=None, bandwidth_value=None, time_stamp=None):
        self.request_id = request_id    # type: str
        self.internet_charge_type = internet_charge_type  # type: str
        self.bandwidth_value = bandwidth_value  # type: int
        self.time_stamp = time_stamp    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.internet_charge_type, 'internet_charge_type')
        self.validate_required(self.bandwidth_value, 'bandwidth_value')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['InternetChargeType'] = self.internet_charge_type
        result['BandwidthValue'] = self.bandwidth_value
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.internet_charge_type = map.get('InternetChargeType')
        self.bandwidth_value = map.get('BandwidthValue')
        self.time_stamp = map.get('TimeStamp')
        return self


class AuthorizeSecurityGroupRequest(TeaModel):
    def __init__(self, version=None, ip_protocol=None, port_range=None, security_group_id=None, policy=None,
                 priority=None, source_cidr_ip=None, source_port_range=None):
        self.version = version          # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.port_range = port_range    # type: str
        self.security_group_id = security_group_id  # type: str
        self.policy = policy            # type: str
        self.priority = priority        # type: int
        self.source_cidr_ip = source_cidr_ip  # type: str
        self.source_port_range = source_port_range  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ip_protocol, 'ip_protocol')
        self.validate_required(self.port_range, 'port_range')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.source_cidr_ip, 'source_cidr_ip')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['IpProtocol'] = self.ip_protocol
        result['PortRange'] = self.port_range
        result['SecurityGroupId'] = self.security_group_id
        result['Policy'] = self.policy
        result['Priority'] = self.priority
        result['SourceCidrIp'] = self.source_cidr_ip
        result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ip_protocol = map.get('IpProtocol')
        self.port_range = map.get('PortRange')
        self.security_group_id = map.get('SecurityGroupId')
        self.policy = map.get('Policy')
        self.priority = map.get('Priority')
        self.source_cidr_ip = map.get('SourceCidrIp')
        self.source_port_range = map.get('SourcePortRange')
        return self


class AuthorizeSecurityGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RevokeSecurityGroupRequest(TeaModel):
    def __init__(self, version=None, ip_protocol=None, port_range=None, security_group_id=None, policy=None,
                 priority=None, source_cidr_ip=None, source_port_range=None):
        self.version = version          # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.port_range = port_range    # type: str
        self.security_group_id = security_group_id  # type: str
        self.policy = policy            # type: str
        self.priority = priority        # type: int
        self.source_cidr_ip = source_cidr_ip  # type: str
        self.source_port_range = source_port_range  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ip_protocol, 'ip_protocol')
        self.validate_required(self.port_range, 'port_range')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.source_cidr_ip, 'source_cidr_ip')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['IpProtocol'] = self.ip_protocol
        result['PortRange'] = self.port_range
        result['SecurityGroupId'] = self.security_group_id
        result['Policy'] = self.policy
        result['Priority'] = self.priority
        result['SourceCidrIp'] = self.source_cidr_ip
        result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ip_protocol = map.get('IpProtocol')
        self.port_range = map.get('PortRange')
        self.security_group_id = map.get('SecurityGroupId')
        self.policy = map.get('Policy')
        self.priority = map.get('Priority')
        self.source_cidr_ip = map.get('SourceCidrIp')
        self.source_port_range = map.get('SourcePortRange')
        return self


class RevokeSecurityGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteSecurityGroupRequest(TeaModel):
    def __init__(self, version=None, security_group_id=None):
        self.version = version          # type: str
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.security_group_id, 'security_group_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.security_group_id = map.get('SecurityGroupId')
        return self


class DeleteSecurityGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeSecurityGroupAttributeRequest(TeaModel):
    def __init__(self, version=None, security_group_id=None):
        self.version = version          # type: str
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.security_group_id, 'security_group_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.security_group_id = map.get('SecurityGroupId')
        return self


class DescribeSecurityGroupAttributeResponse(TeaModel):
    def __init__(self, request_id=None, security_group_id=None, permissions=None):
        self.request_id = request_id    # type: str
        self.security_group_id = security_group_id  # type: str
        self.permissions = permissions  # type: DescribeSecurityGroupAttributeResponsePermissions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.permissions, 'permissions')
        if self.permissions:
            self.permissions.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SecurityGroupId'] = self.security_group_id
        if self.permissions is not None:
            result['Permissions'] = self.permissions.to_map()
        else:
            result['Permissions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.security_group_id = map.get('SecurityGroupId')
        if map.get('Permissions') is not None:
            temp_model = DescribeSecurityGroupAttributeResponsePermissions()
            self.permissions = temp_model.from_map(map['Permissions'])
        else:
            self.permissions = None
        return self


class DescribeSecurityGroupAttributeResponsePermissionsPermission(TeaModel):
    def __init__(self, dest_cidr_ip=None, source_cidr_ip=None, ip_protocol=None, priority=None, policy=None,
                 direction=None, creation_time=None, port_range=None, source_port_range=None):
        self.dest_cidr_ip = dest_cidr_ip  # type: str
        self.source_cidr_ip = source_cidr_ip  # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.priority = priority        # type: int
        self.policy = policy            # type: str
        self.direction = direction      # type: str
        self.creation_time = creation_time  # type: str
        self.port_range = port_range    # type: str
        self.source_port_range = source_port_range  # type: str

    def validate(self):
        self.validate_required(self.dest_cidr_ip, 'dest_cidr_ip')
        self.validate_required(self.source_cidr_ip, 'source_cidr_ip')
        self.validate_required(self.ip_protocol, 'ip_protocol')
        self.validate_required(self.priority, 'priority')
        self.validate_required(self.policy, 'policy')
        self.validate_required(self.direction, 'direction')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.port_range, 'port_range')
        self.validate_required(self.source_port_range, 'source_port_range')

    def to_map(self):
        result = {}
        result['DestCidrIp'] = self.dest_cidr_ip
        result['SourceCidrIp'] = self.source_cidr_ip
        result['IpProtocol'] = self.ip_protocol
        result['Priority'] = self.priority
        result['Policy'] = self.policy
        result['Direction'] = self.direction
        result['CreationTime'] = self.creation_time
        result['PortRange'] = self.port_range
        result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, map={}):
        self.dest_cidr_ip = map.get('DestCidrIp')
        self.source_cidr_ip = map.get('SourceCidrIp')
        self.ip_protocol = map.get('IpProtocol')
        self.priority = map.get('Priority')
        self.policy = map.get('Policy')
        self.direction = map.get('Direction')
        self.creation_time = map.get('CreationTime')
        self.port_range = map.get('PortRange')
        self.source_port_range = map.get('SourcePortRange')
        return self


class DescribeSecurityGroupAttributeResponsePermissions(TeaModel):
    def __init__(self, permission=None):
        self.permission = permission    # type: List[DescribeSecurityGroupAttributeResponsePermissionsPermission]

    def validate(self):
        self.validate_required(self.permission, 'permission')
        if self.permission:
            for k in self.permission:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Permission'] = []
        if self.permission is not None:
            for k in self.permission:
                result['Permission'].append(k.to_map() if k else None)
        else:
            result['Permission'] = None
        return result

    def from_map(self, map={}):
        self.permission = []
        if map.get('Permission') is not None:
            for k in map.get('Permission'):
                temp_model = DescribeSecurityGroupAttributeResponsePermissionsPermission()
                self.permission.append(temp_model.from_map(k))
        else:
            self.permission = None
        return self


class LeaveSecurityGroupRequest(TeaModel):
    def __init__(self, version=None, security_group_id=None, instance_id=None):
        self.version = version          # type: str
        self.security_group_id = security_group_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['SecurityGroupId'] = self.security_group_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.security_group_id = map.get('SecurityGroupId')
        self.instance_id = map.get('InstanceId')
        return self


class LeaveSecurityGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class JoinSecurityGroupRequest(TeaModel):
    def __init__(self, version=None, security_group_id=None, instance_id=None):
        self.version = version          # type: str
        self.security_group_id = security_group_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['SecurityGroupId'] = self.security_group_id
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.security_group_id = map.get('SecurityGroupId')
        self.instance_id = map.get('InstanceId')
        return self


class JoinSecurityGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AuthorizeSecurityGroupEgressRequest(TeaModel):
    def __init__(self, version=None, ip_protocol=None, port_range=None, security_group_id=None, policy=None,
                 priority=None, dest_cidr_ip=None, source_port_range=None):
        self.version = version          # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.port_range = port_range    # type: str
        self.security_group_id = security_group_id  # type: str
        self.policy = policy            # type: str
        self.priority = priority        # type: int
        self.dest_cidr_ip = dest_cidr_ip  # type: str
        self.source_port_range = source_port_range  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ip_protocol, 'ip_protocol')
        self.validate_required(self.port_range, 'port_range')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.dest_cidr_ip, 'dest_cidr_ip')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['IpProtocol'] = self.ip_protocol
        result['PortRange'] = self.port_range
        result['SecurityGroupId'] = self.security_group_id
        result['Policy'] = self.policy
        result['Priority'] = self.priority
        result['DestCidrIp'] = self.dest_cidr_ip
        result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ip_protocol = map.get('IpProtocol')
        self.port_range = map.get('PortRange')
        self.security_group_id = map.get('SecurityGroupId')
        self.policy = map.get('Policy')
        self.priority = map.get('Priority')
        self.dest_cidr_ip = map.get('DestCidrIp')
        self.source_port_range = map.get('SourcePortRange')
        return self


class AuthorizeSecurityGroupEgressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class RevokeSecurityGroupEgressRequest(TeaModel):
    def __init__(self, version=None, ip_protocol=None, port_range=None, security_group_id=None, policy=None,
                 priority=None, dest_cidr_ip=None, source_port_range=None):
        self.version = version          # type: str
        self.ip_protocol = ip_protocol  # type: str
        self.port_range = port_range    # type: str
        self.security_group_id = security_group_id  # type: str
        self.policy = policy            # type: str
        self.priority = priority        # type: int
        self.dest_cidr_ip = dest_cidr_ip  # type: str
        self.source_port_range = source_port_range  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ip_protocol, 'ip_protocol')
        self.validate_required(self.port_range, 'port_range')
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.dest_cidr_ip, 'dest_cidr_ip')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['IpProtocol'] = self.ip_protocol
        result['PortRange'] = self.port_range
        result['SecurityGroupId'] = self.security_group_id
        result['Policy'] = self.policy
        result['Priority'] = self.priority
        result['DestCidrIp'] = self.dest_cidr_ip
        result['SourcePortRange'] = self.source_port_range
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ip_protocol = map.get('IpProtocol')
        self.port_range = map.get('PortRange')
        self.security_group_id = map.get('SecurityGroupId')
        self.policy = map.get('Policy')
        self.priority = map.get('Priority')
        self.dest_cidr_ip = map.get('DestCidrIp')
        self.source_port_range = map.get('SourcePortRange')
        return self


class RevokeSecurityGroupEgressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeSecurityGroupsRequest(TeaModel):
    def __init__(self, version=None, security_group_id=None, page_number=None, page_size=None,
                 security_group_name=None):
        self.version = version          # type: str
        self.security_group_id = security_group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['SecurityGroupId'] = self.security_group_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.security_group_id = map.get('SecurityGroupId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.security_group_name = map.get('SecurityGroupName')
        return self


class DescribeSecurityGroupsResponse(TeaModel):
    def __init__(self, request_id=None, total_count=None, page_number=None, page_size=None, security_groups=None):
        self.request_id = request_id    # type: str
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.security_groups = security_groups  # type: DescribeSecurityGroupsResponseSecurityGroups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.security_groups, 'security_groups')
        if self.security_groups:
            self.security_groups.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups.to_map()
        else:
            result['SecurityGroups'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('SecurityGroups') is not None:
            temp_model = DescribeSecurityGroupsResponseSecurityGroups()
            self.security_groups = temp_model.from_map(map['SecurityGroups'])
        else:
            self.security_groups = None
        return self


class DescribeSecurityGroupsResponseSecurityGroupsSecurityGroup(TeaModel):
    def __init__(self, security_group_id=None, creation_time=None, security_group_name=None):
        self.security_group_id = security_group_id  # type: str
        self.creation_time = creation_time  # type: str
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.security_group_name, 'security_group_name')

    def to_map(self):
        result = {}
        result['SecurityGroupId'] = self.security_group_id
        result['CreationTime'] = self.creation_time
        result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, map={}):
        self.security_group_id = map.get('SecurityGroupId')
        self.creation_time = map.get('CreationTime')
        self.security_group_name = map.get('SecurityGroupName')
        return self


class DescribeSecurityGroupsResponseSecurityGroups(TeaModel):
    def __init__(self, security_group=None):
        self.security_group = security_group  # type: List[DescribeSecurityGroupsResponseSecurityGroupsSecurityGroup]

    def validate(self):
        self.validate_required(self.security_group, 'security_group')
        if self.security_group:
            for k in self.security_group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SecurityGroup'] = []
        if self.security_group is not None:
            for k in self.security_group:
                result['SecurityGroup'].append(k.to_map() if k else None)
        else:
            result['SecurityGroup'] = None
        return result

    def from_map(self, map={}):
        self.security_group = []
        if map.get('SecurityGroup') is not None:
            for k in map.get('SecurityGroup'):
                temp_model = DescribeSecurityGroupsResponseSecurityGroupsSecurityGroup()
                self.security_group.append(temp_model.from_map(k))
        else:
            self.security_group = None
        return self


class CreateSecurityGroupRequest(TeaModel):
    def __init__(self, version=None, security_group_name=None):
        self.version = version          # type: str
        self.security_group_name = security_group_name  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['SecurityGroupName'] = self.security_group_name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.security_group_name = map.get('SecurityGroupName')
        return self


class CreateSecurityGroupResponse(TeaModel):
    def __init__(self, request_id=None, security_group_id=None):
        self.request_id = request_id    # type: str
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.security_group_id, 'security_group_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.security_group_id = map.get('SecurityGroupId')
        return self


class DescribeEnsRegionIdIpv6InfoRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        return self


class DescribeEnsRegionIdIpv6InfoResponse(TeaModel):
    def __init__(self, request_id=None, support_ipv_6info=None):
        self.request_id = request_id    # type: str
        self.support_ipv_6info = support_ipv_6info  # type: DescribeEnsRegionIdIpv6InfoResponseSupportIpv6Info

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.support_ipv_6info, 'support_ipv_6info')
        if self.support_ipv_6info:
            self.support_ipv_6info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.support_ipv_6info is not None:
            result['SupportIpv6Info'] = self.support_ipv_6info.to_map()
        else:
            result['SupportIpv6Info'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('SupportIpv6Info') is not None:
            temp_model = DescribeEnsRegionIdIpv6InfoResponseSupportIpv6Info()
            self.support_ipv_6info = temp_model.from_map(map['SupportIpv6Info'])
        else:
            self.support_ipv_6info = None
        return self


class DescribeEnsRegionIdIpv6InfoResponseSupportIpv6Info(TeaModel):
    def __init__(self, support_ipv_6=None, ens_region_id=None):
        self.support_ipv_6 = support_ipv_6  # type: bool
        self.ens_region_id = ens_region_id  # type: str

    def validate(self):
        self.validate_required(self.support_ipv_6, 'support_ipv_6')
        self.validate_required(self.ens_region_id, 'ens_region_id')

    def to_map(self):
        result = {}
        result['SupportIpv6'] = self.support_ipv_6
        result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, map={}):
        self.support_ipv_6 = map.get('SupportIpv6')
        self.ens_region_id = map.get('EnsRegionId')
        return self


class DescribeCreatePrePaidInstanceResultRequest(TeaModel):
    def __init__(self, version=None, instance_id=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        return self


class DescribeCreatePrePaidInstanceResultResponse(TeaModel):
    def __init__(self, request_id=None, instance_create_result=None):
        self.request_id = request_id    # type: str
        self.instance_create_result = instance_create_result  # type: DescribeCreatePrePaidInstanceResultResponseInstanceCreateResult

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.instance_create_result, 'instance_create_result')
        if self.instance_create_result:
            self.instance_create_result.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.instance_create_result is not None:
            result['InstanceCreateResult'] = self.instance_create_result.to_map()
        else:
            result['InstanceCreateResult'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('InstanceCreateResult') is not None:
            temp_model = DescribeCreatePrePaidInstanceResultResponseInstanceCreateResult()
            self.instance_create_result = temp_model.from_map(map['InstanceCreateResult'])
        else:
            self.instance_create_result = None
        return self


class DescribeCreatePrePaidInstanceResultResponseInstanceCreateResult(TeaModel):
    def __init__(self, instance_create_status=None, instance_id=None):
        self.instance_create_status = instance_create_status  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.instance_create_status, 'instance_create_status')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceCreateStatus'] = self.instance_create_status
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.instance_create_status = map.get('InstanceCreateStatus')
        self.instance_id = map.get('InstanceId')
        return self


class DescribePriceRequest(TeaModel):
    def __init__(self, version=None, instance_type=None, ens_region_id=None, period=None, system_disk=None,
                 quantity=None, data_disk=None, internet_charge_type=None):
        self.version = version          # type: str
        self.instance_type = instance_type  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.period = period            # type: int
        self.system_disk = system_disk  # type: DescribePriceRequestSystemDisk
        self.quantity = quantity        # type: int
        self.data_disk = data_disk      # type: List[DescribePriceRequestDataDisk]
        self.internet_charge_type = internet_charge_type  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.period, 'period')
        if self.system_disk:
            self.system_disk.validate()
        self.validate_required(self.quantity, 'quantity')
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()
        self.validate_required(self.internet_charge_type, 'internet_charge_type')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceType'] = self.instance_type
        result['EnsRegionId'] = self.ens_region_id
        result['Period'] = self.period
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        else:
            result['SystemDisk'] = None
        result['Quantity'] = self.quantity
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        else:
            result['DataDisk'] = None
        result['InternetChargeType'] = self.internet_charge_type
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_type = map.get('InstanceType')
        self.ens_region_id = map.get('EnsRegionId')
        self.period = map.get('Period')
        if map.get('SystemDisk') is not None:
            temp_model = DescribePriceRequestSystemDisk()
            self.system_disk = temp_model.from_map(map['SystemDisk'])
        else:
            self.system_disk = None
        self.quantity = map.get('Quantity')
        self.data_disk = []
        if map.get('DataDisk') is not None:
            for k in map.get('DataDisk'):
                temp_model = DescribePriceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        else:
            self.data_disk = None
        self.internet_charge_type = map.get('InternetChargeType')
        return self


class DescribePriceRequestSystemDisk(TeaModel):
    def __init__(self, size=None):
        self.size = size                # type: int

    def validate(self):
        self.validate_required(self.size, 'size')

    def to_map(self):
        result = {}
        result['Size'] = self.size
        return result

    def from_map(self, map={}):
        self.size = map.get('Size')
        return self


class DescribePriceRequestDataDisk(TeaModel):
    def __init__(self, size=None):
        self.size = size                # type: int

    def validate(self):
        self.validate_required(self.size, 'size')

    def to_map(self):
        result = {}
        result['Size'] = self.size
        return result

    def from_map(self, map={}):
        self.size = map.get('Size')
        return self


class DescribePriceResponse(TeaModel):
    def __init__(self, request_id=None, price_info=None):
        self.request_id = request_id    # type: str
        self.price_info = price_info    # type: DescribePriceResponsePriceInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.price_info, 'price_info')
        if self.price_info:
            self.price_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.price_info is not None:
            result['PriceInfo'] = self.price_info.to_map()
        else:
            result['PriceInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('PriceInfo') is not None:
            temp_model = DescribePriceResponsePriceInfo()
            self.price_info = temp_model.from_map(map['PriceInfo'])
        else:
            self.price_info = None
        return self


class DescribePriceResponsePriceInfoPrice(TeaModel):
    def __init__(self, discount_price=None, original_price=None, trade_price=None, currency=None):
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float
        self.currency = currency        # type: str

    def validate(self):
        self.validate_required(self.discount_price, 'discount_price')
        self.validate_required(self.original_price, 'original_price')
        self.validate_required(self.trade_price, 'trade_price')
        self.validate_required(self.currency, 'currency')

    def to_map(self):
        result = {}
        result['DiscountPrice'] = self.discount_price
        result['OriginalPrice'] = self.original_price
        result['TradePrice'] = self.trade_price
        result['Currency'] = self.currency
        return result

    def from_map(self, map={}):
        self.discount_price = map.get('DiscountPrice')
        self.original_price = map.get('OriginalPrice')
        self.trade_price = map.get('TradePrice')
        self.currency = map.get('Currency')
        return self


class DescribePriceResponsePriceInfo(TeaModel):
    def __init__(self, price=None):
        self.price = price              # type: DescribePriceResponsePriceInfoPrice

    def validate(self):
        self.validate_required(self.price, 'price')
        if self.price:
            self.price.validate()

    def to_map(self):
        result = {}
        if self.price is not None:
            result['Price'] = self.price.to_map()
        else:
            result['Price'] = None
        return result

    def from_map(self, map={}):
        if map.get('Price') is not None:
            temp_model = DescribePriceResponsePriceInfoPrice()
            self.price = temp_model.from_map(map['Price'])
        else:
            self.price = None
        return self


class ExportMeasurementDataRequest(TeaModel):
    def __init__(self, version=None, start_date=None, end_date=None):
        self.version = version          # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class ExportMeasurementDataResponse(TeaModel):
    def __init__(self, request_id=None, file_path=None):
        self.request_id = request_id    # type: str
        self.file_path = file_path      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.file_path, 'file_path')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['FilePath'] = self.file_path
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.file_path = map.get('FilePath')
        return self


class DescribeMeasurementDataRequest(TeaModel):
    def __init__(self, version=None, start_date=None, end_date=None):
        self.version = version          # type: str
        self.start_date = start_date    # type: str
        self.end_date = end_date        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_date, 'start_date')
        self.validate_required(self.end_date, 'end_date')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['StartDate'] = self.start_date
        result['EndDate'] = self.end_date
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.start_date = map.get('StartDate')
        self.end_date = map.get('EndDate')
        return self


class DescribeMeasurementDataResponse(TeaModel):
    def __init__(self, request_id=None, measurement_datas=None):
        self.request_id = request_id    # type: str
        self.measurement_datas = measurement_datas  # type: DescribeMeasurementDataResponseMeasurementDatas

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.measurement_datas, 'measurement_datas')
        if self.measurement_datas:
            self.measurement_datas.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.measurement_datas is not None:
            result['MeasurementDatas'] = self.measurement_datas.to_map()
        else:
            result['MeasurementDatas'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('MeasurementDatas') is not None:
            temp_model = DescribeMeasurementDataResponseMeasurementDatas()
            self.measurement_datas = temp_model.from_map(map['MeasurementDatas'])
        else:
            self.measurement_datas = None
        return self


class DescribeMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData(TeaModel):
    def __init__(self, cost_val=None, cost_code=None, cost_name=None):
        self.cost_val = cost_val        # type: int
        self.cost_code = cost_code      # type: str
        self.cost_name = cost_name      # type: str

    def validate(self):
        self.validate_required(self.cost_val, 'cost_val')
        self.validate_required(self.cost_code, 'cost_code')
        self.validate_required(self.cost_name, 'cost_name')

    def to_map(self):
        result = {}
        result['CostVal'] = self.cost_val
        result['CostCode'] = self.cost_code
        result['CostName'] = self.cost_name
        return result

    def from_map(self, map={}):
        self.cost_val = map.get('CostVal')
        self.cost_code = map.get('CostCode')
        self.cost_name = map.get('CostName')
        return self


class DescribeMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatas(TeaModel):
    def __init__(self, band_width_fee_data=None):
        self.band_width_fee_data = band_width_fee_data  # type: List[DescribeMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData]

    def validate(self):
        self.validate_required(self.band_width_fee_data, 'band_width_fee_data')
        if self.band_width_fee_data:
            for k in self.band_width_fee_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BandWidthFeeData'] = []
        if self.band_width_fee_data is not None:
            for k in self.band_width_fee_data:
                result['BandWidthFeeData'].append(k.to_map() if k else None)
        else:
            result['BandWidthFeeData'] = None
        return result

    def from_map(self, map={}):
        self.band_width_fee_data = []
        if map.get('BandWidthFeeData') is not None:
            for k in map.get('BandWidthFeeData'):
                temp_model = DescribeMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatasBandWidthFeeData()
                self.band_width_fee_data.append(temp_model.from_map(k))
        else:
            self.band_width_fee_data = None
        return self


class DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail(TeaModel):
    def __init__(self, cost_val=None, cost_code=None, cost_name=None, resource_type=None):
        self.cost_val = cost_val        # type: int
        self.cost_code = cost_code      # type: str
        self.cost_name = cost_name      # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        self.validate_required(self.cost_val, 'cost_val')
        self.validate_required(self.cost_code, 'cost_code')
        self.validate_required(self.cost_name, 'cost_name')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        result['CostVal'] = self.cost_val
        result['CostCode'] = self.cost_code
        result['CostName'] = self.cost_name
        result['ResourceType'] = self.resource_type
        return result

    def from_map(self, map={}):
        self.cost_val = map.get('CostVal')
        self.cost_code = map.get('CostCode')
        self.cost_name = map.get('CostName')
        self.resource_type = map.get('ResourceType')
        return self


class DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeDataDetails(TeaModel):
    def __init__(self, resource_fee_data_detail=None):
        self.resource_fee_data_detail = resource_fee_data_detail  # type: List[DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail]

    def validate(self):
        self.validate_required(self.resource_fee_data_detail, 'resource_fee_data_detail')
        if self.resource_fee_data_detail:
            for k in self.resource_fee_data_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceFeeDataDetail'] = []
        if self.resource_fee_data_detail is not None:
            for k in self.resource_fee_data_detail:
                result['ResourceFeeDataDetail'].append(k.to_map() if k else None)
        else:
            result['ResourceFeeDataDetail'] = None
        return result

    def from_map(self, map={}):
        self.resource_fee_data_detail = []
        if map.get('ResourceFeeDataDetail') is not None:
            for k in map.get('ResourceFeeDataDetail'):
                temp_model = DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeDataDetailsResourceFeeDataDetail()
                self.resource_fee_data_detail.append(temp_model.from_map(k))
        else:
            self.resource_fee_data_detail = None
        return self


class DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeData(TeaModel):
    def __init__(self, storage=None, memory=None, vcpu=None):
        self.storage = storage          # type: int
        self.memory = memory            # type: int
        self.vcpu = vcpu                # type: int

    def validate(self):
        self.validate_required(self.storage, 'storage')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.vcpu, 'vcpu')

    def to_map(self):
        result = {}
        result['Storage'] = self.storage
        result['Memory'] = self.memory
        result['Vcpu'] = self.vcpu
        return result

    def from_map(self, map={}):
        self.storage = map.get('Storage')
        self.memory = map.get('Memory')
        self.vcpu = map.get('Vcpu')
        return self


class DescribeMeasurementDataResponseMeasurementDatasMeasurementData(TeaModel):
    def __init__(self, charge_model=None, cost_cycle=None, cost_start_time=None, cost_end_time=None,
                 band_width_fee_datas=None, resource_fee_data_details=None, resource_fee_data=None):
        self.charge_model = charge_model  # type: str
        self.cost_cycle = cost_cycle    # type: str
        self.cost_start_time = cost_start_time  # type: str
        self.cost_end_time = cost_end_time  # type: str
        self.band_width_fee_datas = band_width_fee_datas  # type: DescribeMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatas
        self.resource_fee_data_details = resource_fee_data_details  # type: DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeDataDetails
        self.resource_fee_data = resource_fee_data  # type: DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeData

    def validate(self):
        self.validate_required(self.charge_model, 'charge_model')
        self.validate_required(self.cost_cycle, 'cost_cycle')
        self.validate_required(self.cost_start_time, 'cost_start_time')
        self.validate_required(self.cost_end_time, 'cost_end_time')
        self.validate_required(self.band_width_fee_datas, 'band_width_fee_datas')
        if self.band_width_fee_datas:
            self.band_width_fee_datas.validate()
        self.validate_required(self.resource_fee_data_details, 'resource_fee_data_details')
        if self.resource_fee_data_details:
            self.resource_fee_data_details.validate()
        self.validate_required(self.resource_fee_data, 'resource_fee_data')
        if self.resource_fee_data:
            self.resource_fee_data.validate()

    def to_map(self):
        result = {}
        result['ChargeModel'] = self.charge_model
        result['CostCycle'] = self.cost_cycle
        result['CostStartTime'] = self.cost_start_time
        result['CostEndTime'] = self.cost_end_time
        if self.band_width_fee_datas is not None:
            result['BandWidthFeeDatas'] = self.band_width_fee_datas.to_map()
        else:
            result['BandWidthFeeDatas'] = None
        if self.resource_fee_data_details is not None:
            result['ResourceFeeDataDetails'] = self.resource_fee_data_details.to_map()
        else:
            result['ResourceFeeDataDetails'] = None
        if self.resource_fee_data is not None:
            result['ResourceFeeData'] = self.resource_fee_data.to_map()
        else:
            result['ResourceFeeData'] = None
        return result

    def from_map(self, map={}):
        self.charge_model = map.get('ChargeModel')
        self.cost_cycle = map.get('CostCycle')
        self.cost_start_time = map.get('CostStartTime')
        self.cost_end_time = map.get('CostEndTime')
        if map.get('BandWidthFeeDatas') is not None:
            temp_model = DescribeMeasurementDataResponseMeasurementDatasMeasurementDataBandWidthFeeDatas()
            self.band_width_fee_datas = temp_model.from_map(map['BandWidthFeeDatas'])
        else:
            self.band_width_fee_datas = None
        if map.get('ResourceFeeDataDetails') is not None:
            temp_model = DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeDataDetails()
            self.resource_fee_data_details = temp_model.from_map(map['ResourceFeeDataDetails'])
        else:
            self.resource_fee_data_details = None
        if map.get('ResourceFeeData') is not None:
            temp_model = DescribeMeasurementDataResponseMeasurementDatasMeasurementDataResourceFeeData()
            self.resource_fee_data = temp_model.from_map(map['ResourceFeeData'])
        else:
            self.resource_fee_data = None
        return self


class DescribeMeasurementDataResponseMeasurementDatas(TeaModel):
    def __init__(self, measurement_data=None):
        self.measurement_data = measurement_data  # type: List[DescribeMeasurementDataResponseMeasurementDatasMeasurementData]

    def validate(self):
        self.validate_required(self.measurement_data, 'measurement_data')
        if self.measurement_data:
            for k in self.measurement_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MeasurementData'] = []
        if self.measurement_data is not None:
            for k in self.measurement_data:
                result['MeasurementData'].append(k.to_map() if k else None)
        else:
            result['MeasurementData'] = None
        return result

    def from_map(self, map={}):
        self.measurement_data = []
        if map.get('MeasurementData') is not None:
            for k in map.get('MeasurementData'):
                temp_model = DescribeMeasurementDataResponseMeasurementDatasMeasurementData()
                self.measurement_data.append(temp_model.from_map(k))
        else:
            self.measurement_data = None
        return self


class DescribeAvailableResourceInfoRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeAvailableResourceInfoResponse(TeaModel):
    def __init__(self, request_id=None, support_resources=None, images=None):
        self.request_id = request_id    # type: str
        self.support_resources = support_resources  # type: DescribeAvailableResourceInfoResponseSupportResources
        self.images = images            # type: DescribeAvailableResourceInfoResponseImages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.support_resources, 'support_resources')
        if self.support_resources:
            self.support_resources.validate()
        self.validate_required(self.images, 'images')
        if self.images:
            self.images.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        else:
            result['SupportResources'] = None
        if self.images is not None:
            result['Images'] = self.images.to_map()
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('SupportResources') is not None:
            temp_model = DescribeAvailableResourceInfoResponseSupportResources()
            self.support_resources = temp_model.from_map(map['SupportResources'])
        else:
            self.support_resources = None
        if map.get('Images') is not None:
            temp_model = DescribeAvailableResourceInfoResponseImages()
            self.images = temp_model.from_map(map['Images'])
        else:
            self.images = None
        return self


class DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId(TeaModel):
    def __init__(self, ens_region_id=None, name=None, en_name=None, area=None, province=None):
        self.ens_region_id = ens_region_id  # type: str
        self.name = name                # type: str
        self.en_name = en_name          # type: str
        self.area = area                # type: str
        self.province = province        # type: str

    def validate(self):
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.en_name, 'en_name')
        self.validate_required(self.area, 'area')
        self.validate_required(self.province, 'province')

    def to_map(self):
        result = {}
        result['EnsRegionId'] = self.ens_region_id
        result['Name'] = self.name
        result['EnName'] = self.en_name
        result['Area'] = self.area
        result['Province'] = self.province
        return result

    def from_map(self, map={}):
        self.ens_region_id = map.get('EnsRegionId')
        self.name = map.get('Name')
        self.en_name = map.get('EnName')
        self.area = map.get('Area')
        self.province = map.get('Province')
        return self


class DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIdsExtends(TeaModel):
    def __init__(self, ens_region_id=None):
        self.ens_region_id = ens_region_id  # type: List[DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId]

    def validate(self):
        self.validate_required(self.ens_region_id, 'ens_region_id')
        if self.ens_region_id:
            for k in self.ens_region_id:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EnsRegionId'] = []
        if self.ens_region_id is not None:
            for k in self.ens_region_id:
                result['EnsRegionId'].append(k.to_map() if k else None)
        else:
            result['EnsRegionId'] = None
        return result

    def from_map(self, map={}):
        self.ens_region_id = []
        if map.get('EnsRegionId') is not None:
            for k in map.get('EnsRegionId'):
                temp_model = DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIdsExtendsEnsRegionId()
                self.ens_region_id.append(temp_model.from_map(k))
        else:
            self.ens_region_id = None
        return self


class DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIds(TeaModel):
    def __init__(self, ens_region_id=None):
        # EnsRegionId
        self.ens_region_id = ens_region_id  # type: List[str]

    def validate(self):
        self.validate_required(self.ens_region_id, 'ens_region_id')

    def to_map(self):
        result = {}
        result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, map={}):
        self.ens_region_id = map.get('EnsRegionId')
        return self


class DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceInstanceSpeces(TeaModel):
    def __init__(self, instance_spec=None):
        # InstanceSpec
        self.instance_spec = instance_spec  # type: List[str]

    def validate(self):
        self.validate_required(self.instance_spec, 'instance_spec')

    def to_map(self):
        result = {}
        result['InstanceSpec'] = self.instance_spec
        return result

    def from_map(self, map={}):
        self.instance_spec = map.get('InstanceSpec')
        return self


class DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceBandwidthTypes(TeaModel):
    def __init__(self, bandwidth_type=None):
        # BandwidthType
        self.bandwidth_type = bandwidth_type  # type: List[str]

    def validate(self):
        self.validate_required(self.bandwidth_type, 'bandwidth_type')

    def to_map(self):
        result = {}
        result['BandwidthType'] = self.bandwidth_type
        return result

    def from_map(self, map={}):
        self.bandwidth_type = map.get('BandwidthType')
        return self


class DescribeAvailableResourceInfoResponseSupportResourcesSupportResource(TeaModel):
    def __init__(self, data_disk_min_size=None, data_disk_max_size=None, system_disk_min_size=None,
                 system_disk_max_size=None, ens_region_ids_extends=None, ens_region_ids=None, instance_speces=None,
                 bandwidth_types=None):
        self.data_disk_min_size = data_disk_min_size  # type: int
        self.data_disk_max_size = data_disk_max_size  # type: int
        self.system_disk_min_size = system_disk_min_size  # type: int
        self.system_disk_max_size = system_disk_max_size  # type: int
        self.ens_region_ids_extends = ens_region_ids_extends  # type: DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIdsExtends
        self.ens_region_ids = ens_region_ids  # type: DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIds
        self.instance_speces = instance_speces  # type: DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceInstanceSpeces
        self.bandwidth_types = bandwidth_types  # type: DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceBandwidthTypes

    def validate(self):
        self.validate_required(self.data_disk_min_size, 'data_disk_min_size')
        self.validate_required(self.data_disk_max_size, 'data_disk_max_size')
        self.validate_required(self.system_disk_min_size, 'system_disk_min_size')
        self.validate_required(self.system_disk_max_size, 'system_disk_max_size')
        self.validate_required(self.ens_region_ids_extends, 'ens_region_ids_extends')
        if self.ens_region_ids_extends:
            self.ens_region_ids_extends.validate()
        self.validate_required(self.ens_region_ids, 'ens_region_ids')
        if self.ens_region_ids:
            self.ens_region_ids.validate()
        self.validate_required(self.instance_speces, 'instance_speces')
        if self.instance_speces:
            self.instance_speces.validate()
        self.validate_required(self.bandwidth_types, 'bandwidth_types')
        if self.bandwidth_types:
            self.bandwidth_types.validate()

    def to_map(self):
        result = {}
        result['DataDiskMinSize'] = self.data_disk_min_size
        result['DataDiskMaxSize'] = self.data_disk_max_size
        result['SystemDiskMinSize'] = self.system_disk_min_size
        result['SystemDiskMaxSize'] = self.system_disk_max_size
        if self.ens_region_ids_extends is not None:
            result['EnsRegionIdsExtends'] = self.ens_region_ids_extends.to_map()
        else:
            result['EnsRegionIdsExtends'] = None
        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids.to_map()
        else:
            result['EnsRegionIds'] = None
        if self.instance_speces is not None:
            result['InstanceSpeces'] = self.instance_speces.to_map()
        else:
            result['InstanceSpeces'] = None
        if self.bandwidth_types is not None:
            result['BandwidthTypes'] = self.bandwidth_types.to_map()
        else:
            result['BandwidthTypes'] = None
        return result

    def from_map(self, map={}):
        self.data_disk_min_size = map.get('DataDiskMinSize')
        self.data_disk_max_size = map.get('DataDiskMaxSize')
        self.system_disk_min_size = map.get('SystemDiskMinSize')
        self.system_disk_max_size = map.get('SystemDiskMaxSize')
        if map.get('EnsRegionIdsExtends') is not None:
            temp_model = DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIdsExtends()
            self.ens_region_ids_extends = temp_model.from_map(map['EnsRegionIdsExtends'])
        else:
            self.ens_region_ids_extends = None
        if map.get('EnsRegionIds') is not None:
            temp_model = DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceEnsRegionIds()
            self.ens_region_ids = temp_model.from_map(map['EnsRegionIds'])
        else:
            self.ens_region_ids = None
        if map.get('InstanceSpeces') is not None:
            temp_model = DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceInstanceSpeces()
            self.instance_speces = temp_model.from_map(map['InstanceSpeces'])
        else:
            self.instance_speces = None
        if map.get('BandwidthTypes') is not None:
            temp_model = DescribeAvailableResourceInfoResponseSupportResourcesSupportResourceBandwidthTypes()
            self.bandwidth_types = temp_model.from_map(map['BandwidthTypes'])
        else:
            self.bandwidth_types = None
        return self


class DescribeAvailableResourceInfoResponseSupportResources(TeaModel):
    def __init__(self, support_resource=None):
        self.support_resource = support_resource  # type: List[DescribeAvailableResourceInfoResponseSupportResourcesSupportResource]

    def validate(self):
        self.validate_required(self.support_resource, 'support_resource')
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        else:
            result['SupportResource'] = None
        return result

    def from_map(self, map={}):
        self.support_resource = []
        if map.get('SupportResource') is not None:
            for k in map.get('SupportResource'):
                temp_model = DescribeAvailableResourceInfoResponseSupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        else:
            self.support_resource = None
        return self


class DescribeAvailableResourceInfoResponseImagesImage(TeaModel):
    def __init__(self, image_id=None, image_name=None, image_size=None):
        self.image_id = image_id        # type: str
        self.image_name = image_name    # type: str
        self.image_size = image_size    # type: int

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_name, 'image_name')
        self.validate_required(self.image_size, 'image_size')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['ImageName'] = self.image_name
        result['ImageSize'] = self.image_size
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.image_name = map.get('ImageName')
        self.image_size = map.get('ImageSize')
        return self


class DescribeAvailableResourceInfoResponseImages(TeaModel):
    def __init__(self, image=None):
        self.image = image              # type: List[DescribeAvailableResourceInfoResponseImagesImage]

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        else:
            result['Image'] = None
        return result

    def from_map(self, map={}):
        self.image = []
        if map.get('Image') is not None:
            for k in map.get('Image'):
                temp_model = DescribeAvailableResourceInfoResponseImagesImage()
                self.image.append(temp_model.from_map(k))
        else:
            self.image = None
        return self


class DescribePrePaidInstanceStockRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, system_disk_size=None, data_disk_size=None,
                 instance_spec=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.system_disk_size = system_disk_size  # type: int
        self.data_disk_size = data_disk_size  # type: int
        self.instance_spec = instance_spec  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.data_disk_size, 'data_disk_size')
        self.validate_required(self.instance_spec, 'instance_spec')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['SystemDiskSize'] = self.system_disk_size
        result['DataDiskSize'] = self.data_disk_size
        result['InstanceSpec'] = self.instance_spec
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.system_disk_size = map.get('SystemDiskSize')
        self.data_disk_size = map.get('DataDiskSize')
        self.instance_spec = map.get('InstanceSpec')
        return self


class DescribePrePaidInstanceStockResponse(TeaModel):
    def __init__(self, request_id=None, data_disk_size=None, ens_region_id=None, cores=None, memory=None,
                 avaliable_count=None, instance_spec=None, system_disk_size=None):
        self.request_id = request_id    # type: str
        self.data_disk_size = data_disk_size  # type: int
        self.ens_region_id = ens_region_id  # type: str
        self.cores = cores              # type: int
        self.memory = memory            # type: int
        self.avaliable_count = avaliable_count  # type: int
        self.instance_spec = instance_spec  # type: str
        self.system_disk_size = system_disk_size  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data_disk_size, 'data_disk_size')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.cores, 'cores')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.avaliable_count, 'avaliable_count')
        self.validate_required(self.instance_spec, 'instance_spec')
        self.validate_required(self.system_disk_size, 'system_disk_size')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DataDiskSize'] = self.data_disk_size
        result['EnsRegionId'] = self.ens_region_id
        result['Cores'] = self.cores
        result['Memory'] = self.memory
        result['AvaliableCount'] = self.avaliable_count
        result['InstanceSpec'] = self.instance_spec
        result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.data_disk_size = map.get('DataDiskSize')
        self.ens_region_id = map.get('EnsRegionId')
        self.cores = map.get('Cores')
        self.memory = map.get('Memory')
        self.avaliable_count = map.get('AvaliableCount')
        self.instance_spec = map.get('InstanceSpec')
        self.system_disk_size = map.get('SystemDiskSize')
        return self


class UnassociateEipAddressRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, eip=None, instance_id_internet_ip=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.eip = eip                  # type: str
        self.instance_id_internet_ip = instance_id_internet_ip  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.eip, 'eip')
        self.validate_required(self.instance_id_internet_ip, 'instance_id_internet_ip')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['Eip'] = self.eip
        result['InstanceIdInternetIp'] = self.instance_id_internet_ip
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.eip = map.get('Eip')
        self.instance_id_internet_ip = map.get('InstanceIdInternetIp')
        return self


class UnassociateEipAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ReleaseEipAddressRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, eips=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.eips = eips                # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.eips, 'eips')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['Eips'] = self.eips
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.eips = map.get('Eips')
        return self


class ReleaseEipAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeEipAddressesRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, eips=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.eips = eips                # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['Eips'] = self.eips
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.eips = map.get('Eips')
        return self


class DescribeEipAddressesResponse(TeaModel):
    def __init__(self, request_id=None, eip_addresses=None):
        self.request_id = request_id    # type: str
        self.eip_addresses = eip_addresses  # type: DescribeEipAddressesResponseEipAddresses

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.eip_addresses, 'eip_addresses')
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()
        else:
            result['EipAddresses'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('EipAddresses') is not None:
            temp_model = DescribeEipAddressesResponseEipAddresses()
            self.eip_addresses = temp_model.from_map(map['EipAddresses'])
        else:
            self.eip_addresses = None
        return self


class DescribeEipAddressesResponseEipAddressesEipAddress(TeaModel):
    def __init__(self, eip=None, instance_id_internet_ip=None):
        self.eip = eip                  # type: str
        self.instance_id_internet_ip = instance_id_internet_ip  # type: str

    def validate(self):
        self.validate_required(self.eip, 'eip')
        self.validate_required(self.instance_id_internet_ip, 'instance_id_internet_ip')

    def to_map(self):
        result = {}
        result['Eip'] = self.eip
        result['InstanceIdInternetIp'] = self.instance_id_internet_ip
        return result

    def from_map(self, map={}):
        self.eip = map.get('Eip')
        self.instance_id_internet_ip = map.get('InstanceIdInternetIp')
        return self


class DescribeEipAddressesResponseEipAddresses(TeaModel):
    def __init__(self, eip_address=None):
        self.eip_address = eip_address  # type: List[DescribeEipAddressesResponseEipAddressesEipAddress]

    def validate(self):
        self.validate_required(self.eip_address, 'eip_address')
        if self.eip_address:
            for k in self.eip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k in self.eip_address:
                result['EipAddress'].append(k.to_map() if k else None)
        else:
            result['EipAddress'] = None
        return result

    def from_map(self, map={}):
        self.eip_address = []
        if map.get('EipAddress') is not None:
            for k in map.get('EipAddress'):
                temp_model = DescribeEipAddressesResponseEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k))
        else:
            self.eip_address = None
        return self


class AssociateEipAddressRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, eip=None, instance_id_internet_ip=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.eip = eip                  # type: str
        self.instance_id_internet_ip = instance_id_internet_ip  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.eip, 'eip')
        self.validate_required(self.instance_id_internet_ip, 'instance_id_internet_ip')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['Eip'] = self.eip
        result['InstanceIdInternetIp'] = self.instance_id_internet_ip
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.eip = map.get('Eip')
        self.instance_id_internet_ip = map.get('InstanceIdInternetIp')
        return self


class AssociateEipAddressResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AllocateEipAddressRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, count=None, min_count=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.count = count              # type: int
        self.min_count = min_count      # type: int

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['Count'] = self.count
        result['MinCount'] = self.min_count
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.count = map.get('Count')
        self.min_count = map.get('MinCount')
        return self


class AllocateEipAddressResponse(TeaModel):
    def __init__(self, request_id=None, biz_status_code=None, eip_addresses=None):
        self.request_id = request_id    # type: str
        self.biz_status_code = biz_status_code  # type: str
        self.eip_addresses = eip_addresses  # type: AllocateEipAddressResponseEipAddresses

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.biz_status_code, 'biz_status_code')
        self.validate_required(self.eip_addresses, 'eip_addresses')
        if self.eip_addresses:
            self.eip_addresses.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BizStatusCode'] = self.biz_status_code
        if self.eip_addresses is not None:
            result['EipAddresses'] = self.eip_addresses.to_map()
        else:
            result['EipAddresses'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.biz_status_code = map.get('BizStatusCode')
        if map.get('EipAddresses') is not None:
            temp_model = AllocateEipAddressResponseEipAddresses()
            self.eip_addresses = temp_model.from_map(map['EipAddresses'])
        else:
            self.eip_addresses = None
        return self


class AllocateEipAddressResponseEipAddressesEipAddress(TeaModel):
    def __init__(self, eip=None):
        self.eip = eip                  # type: str

    def validate(self):
        self.validate_required(self.eip, 'eip')

    def to_map(self):
        result = {}
        result['Eip'] = self.eip
        return result

    def from_map(self, map={}):
        self.eip = map.get('Eip')
        return self


class AllocateEipAddressResponseEipAddresses(TeaModel):
    def __init__(self, eip_address=None):
        self.eip_address = eip_address  # type: List[AllocateEipAddressResponseEipAddressesEipAddress]

    def validate(self):
        self.validate_required(self.eip_address, 'eip_address')
        if self.eip_address:
            for k in self.eip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EipAddress'] = []
        if self.eip_address is not None:
            for k in self.eip_address:
                result['EipAddress'].append(k.to_map() if k else None)
        else:
            result['EipAddress'] = None
        return result

    def from_map(self, map={}):
        self.eip_address = []
        if map.get('EipAddress') is not None:
            for k in map.get('EipAddress'):
                temp_model = AllocateEipAddressResponseEipAddressesEipAddress()
                self.eip_address.append(temp_model.from_map(k))
        else:
            self.eip_address = None
        return self


class ReleasePostPaidInstanceRequest(TeaModel):
    def __init__(self, version=None, instance_id=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        return self


class ReleasePostPaidInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ReleasePrePaidInstanceRequest(TeaModel):
    def __init__(self, version=None, instance_id=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        return self


class ReleasePrePaidInstanceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AttachEnsInstancesRequest(TeaModel):
    def __init__(self, version=None, instance_id=None, scripts=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str
        self.scripts = scripts          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.scripts, 'scripts')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        result['Scripts'] = self.scripts
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        self.scripts = map.get('Scripts')
        return self


class AttachEnsInstancesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeReservedResourceRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeReservedResourceResponse(TeaModel):
    def __init__(self, request_id=None, code=None, images=None, support_resources=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.images = images            # type: DescribeReservedResourceResponseImages
        self.support_resources = support_resources  # type: DescribeReservedResourceResponseSupportResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.images, 'images')
        if self.images:
            self.images.validate()
        self.validate_required(self.support_resources, 'support_resources')
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        else:
            result['Images'] = None
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        else:
            result['SupportResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('Images') is not None:
            temp_model = DescribeReservedResourceResponseImages()
            self.images = temp_model.from_map(map['Images'])
        else:
            self.images = None
        if map.get('SupportResources') is not None:
            temp_model = DescribeReservedResourceResponseSupportResources()
            self.support_resources = temp_model.from_map(map['SupportResources'])
        else:
            self.support_resources = None
        return self


class DescribeReservedResourceResponseImagesImage(TeaModel):
    def __init__(self, image_id=None, image_name=None):
        self.image_id = image_id        # type: str
        self.image_name = image_name    # type: str

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_name, 'image_name')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['ImageName'] = self.image_name
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.image_name = map.get('ImageName')
        return self


class DescribeReservedResourceResponseImages(TeaModel):
    def __init__(self, image=None):
        self.image = image              # type: List[DescribeReservedResourceResponseImagesImage]

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        else:
            result['Image'] = None
        return result

    def from_map(self, map={}):
        self.image = []
        if map.get('Image') is not None:
            for k in map.get('Image'):
                temp_model = DescribeReservedResourceResponseImagesImage()
                self.image.append(temp_model.from_map(k))
        else:
            self.image = None
        return self


class DescribeReservedResourceResponseSupportResourcesSupportResourceSystemDiskSizes(TeaModel):
    def __init__(self, system_disk_size=None):
        # SystemDiskSize
        self.system_disk_size = system_disk_size  # type: List[str]

    def validate(self):
        self.validate_required(self.system_disk_size, 'system_disk_size')

    def to_map(self):
        result = {}
        result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, map={}):
        self.system_disk_size = map.get('SystemDiskSize')
        return self


class DescribeReservedResourceResponseSupportResourcesSupportResourceDataDiskSizes(TeaModel):
    def __init__(self, data_disk_size=None):
        # DataDiskSize
        self.data_disk_size = data_disk_size  # type: List[str]

    def validate(self):
        self.validate_required(self.data_disk_size, 'data_disk_size')

    def to_map(self):
        result = {}
        result['DataDiskSize'] = self.data_disk_size
        return result

    def from_map(self, map={}):
        self.data_disk_size = map.get('DataDiskSize')
        return self


class DescribeReservedResourceResponseSupportResourcesSupportResource(TeaModel):
    def __init__(self, ens_region_id=None, support_resources_count=None, instance_spec=None,
                 system_disk_sizes=None, data_disk_sizes=None):
        self.ens_region_id = ens_region_id  # type: str
        self.support_resources_count = support_resources_count  # type: str
        self.instance_spec = instance_spec  # type: str
        self.system_disk_sizes = system_disk_sizes  # type: DescribeReservedResourceResponseSupportResourcesSupportResourceSystemDiskSizes
        self.data_disk_sizes = data_disk_sizes  # type: DescribeReservedResourceResponseSupportResourcesSupportResourceDataDiskSizes

    def validate(self):
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.support_resources_count, 'support_resources_count')
        self.validate_required(self.instance_spec, 'instance_spec')
        self.validate_required(self.system_disk_sizes, 'system_disk_sizes')
        if self.system_disk_sizes:
            self.system_disk_sizes.validate()
        self.validate_required(self.data_disk_sizes, 'data_disk_sizes')
        if self.data_disk_sizes:
            self.data_disk_sizes.validate()

    def to_map(self):
        result = {}
        result['EnsRegionId'] = self.ens_region_id
        result['SupportResourcesCount'] = self.support_resources_count
        result['InstanceSpec'] = self.instance_spec
        if self.system_disk_sizes is not None:
            result['SystemDiskSizes'] = self.system_disk_sizes.to_map()
        else:
            result['SystemDiskSizes'] = None
        if self.data_disk_sizes is not None:
            result['DataDiskSizes'] = self.data_disk_sizes.to_map()
        else:
            result['DataDiskSizes'] = None
        return result

    def from_map(self, map={}):
        self.ens_region_id = map.get('EnsRegionId')
        self.support_resources_count = map.get('SupportResourcesCount')
        self.instance_spec = map.get('InstanceSpec')
        if map.get('SystemDiskSizes') is not None:
            temp_model = DescribeReservedResourceResponseSupportResourcesSupportResourceSystemDiskSizes()
            self.system_disk_sizes = temp_model.from_map(map['SystemDiskSizes'])
        else:
            self.system_disk_sizes = None
        if map.get('DataDiskSizes') is not None:
            temp_model = DescribeReservedResourceResponseSupportResourcesSupportResourceDataDiskSizes()
            self.data_disk_sizes = temp_model.from_map(map['DataDiskSizes'])
        else:
            self.data_disk_sizes = None
        return self


class DescribeReservedResourceResponseSupportResources(TeaModel):
    def __init__(self, support_resource=None):
        self.support_resource = support_resource  # type: List[DescribeReservedResourceResponseSupportResourcesSupportResource]

    def validate(self):
        self.validate_required(self.support_resource, 'support_resource')
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        else:
            result['SupportResource'] = None
        return result

    def from_map(self, map={}):
        self.support_resource = []
        if map.get('SupportResource') is not None:
            for k in map.get('SupportResource'):
                temp_model = DescribeReservedResourceResponseSupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        else:
            self.support_resource = None
        return self


class DescribeInstanceTypesRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeInstanceTypesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, instance_types=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.instance_types = instance_types  # type: DescribeInstanceTypesResponseInstanceTypes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.instance_types, 'instance_types')
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        else:
            result['InstanceTypes'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('InstanceTypes') is not None:
            temp_model = DescribeInstanceTypesResponseInstanceTypes()
            self.instance_types = temp_model.from_map(map['InstanceTypes'])
        else:
            self.instance_types = None
        return self


class DescribeInstanceTypesResponseInstanceTypesInstanceType(TeaModel):
    def __init__(self, cpu_core_count=None, memory_size=None, instance_type_id=None, instance_type_name=None):
        self.cpu_core_count = cpu_core_count  # type: int
        self.memory_size = memory_size  # type: int
        self.instance_type_id = instance_type_id  # type: str
        self.instance_type_name = instance_type_name  # type: str

    def validate(self):
        self.validate_required(self.cpu_core_count, 'cpu_core_count')
        self.validate_required(self.memory_size, 'memory_size')
        self.validate_required(self.instance_type_id, 'instance_type_id')
        self.validate_required(self.instance_type_name, 'instance_type_name')

    def to_map(self):
        result = {}
        result['CpuCoreCount'] = self.cpu_core_count
        result['MemorySize'] = self.memory_size
        result['InstanceTypeId'] = self.instance_type_id
        result['InstanceTypeName'] = self.instance_type_name
        return result

    def from_map(self, map={}):
        self.cpu_core_count = map.get('CpuCoreCount')
        self.memory_size = map.get('MemorySize')
        self.instance_type_id = map.get('InstanceTypeId')
        self.instance_type_name = map.get('InstanceTypeName')
        return self


class DescribeInstanceTypesResponseInstanceTypes(TeaModel):
    def __init__(self, instance_type=None):
        self.instance_type = instance_type  # type: List[DescribeInstanceTypesResponseInstanceTypesInstanceType]

    def validate(self):
        self.validate_required(self.instance_type, 'instance_type')
        if self.instance_type:
            for k in self.instance_type:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceType'] = []
        if self.instance_type is not None:
            for k in self.instance_type:
                result['InstanceType'].append(k.to_map() if k else None)
        else:
            result['InstanceType'] = None
        return result

    def from_map(self, map={}):
        self.instance_type = []
        if map.get('InstanceType') is not None:
            for k in map.get('InstanceType'):
                temp_model = DescribeInstanceTypesResponseInstanceTypesInstanceType()
                self.instance_type.append(temp_model.from_map(k))
        else:
            self.instance_type = None
        return self


class CreateImageRequest(TeaModel):
    def __init__(self, product=None, version=None, instance_id=None, image_name=None,
                 delete_after_image_upload=None):
        self.product = product          # type: str
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str
        self.image_name = image_name    # type: str
        self.delete_after_image_upload = delete_after_image_upload  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.image_name, 'image_name')

    def to_map(self):
        result = {}
        result['product'] = self.product
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        result['ImageName'] = self.image_name
        result['DeleteAfterImageUpload'] = self.delete_after_image_upload
        return result

    def from_map(self, map={}):
        self.product = map.get('product')
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        self.image_name = map.get('ImageName')
        self.delete_after_image_upload = map.get('DeleteAfterImageUpload')
        return self


class CreateImageResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class DescribeEnsNetSaleDistrictRequest(TeaModel):
    def __init__(self, version=None, net_level_code=None, net_district_code=None):
        self.version = version          # type: str
        self.net_level_code = net_level_code  # type: str
        self.net_district_code = net_district_code  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.net_level_code, 'net_level_code')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['NetLevelCode'] = self.net_level_code
        result['NetDistrictCode'] = self.net_district_code
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.net_level_code = map.get('NetLevelCode')
        self.net_district_code = map.get('NetDistrictCode')
        return self


class DescribeEnsNetSaleDistrictResponse(TeaModel):
    def __init__(self, request_id=None, code=None, ens_net_districts=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.ens_net_districts = ens_net_districts  # type: DescribeEnsNetSaleDistrictResponseEnsNetDistricts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.ens_net_districts, 'ens_net_districts')
        if self.ens_net_districts:
            self.ens_net_districts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.ens_net_districts is not None:
            result['EnsNetDistricts'] = self.ens_net_districts.to_map()
        else:
            result['EnsNetDistricts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('EnsNetDistricts') is not None:
            temp_model = DescribeEnsNetSaleDistrictResponseEnsNetDistricts()
            self.ens_net_districts = temp_model.from_map(map['EnsNetDistricts'])
        else:
            self.ens_net_districts = None
        return self


class DescribeEnsNetSaleDistrictResponseEnsNetDistrictsEnsNetDistrict(TeaModel):
    def __init__(self, net_district_code=None, net_district_name=None, ens_region_id_count=None,
                 net_district_level=None, net_district_father_code=None, net_district_en_name=None, instance_count=None):
        self.net_district_code = net_district_code  # type: str
        self.net_district_name = net_district_name  # type: str
        self.ens_region_id_count = ens_region_id_count  # type: str
        self.net_district_level = net_district_level  # type: str
        self.net_district_father_code = net_district_father_code  # type: str
        self.net_district_en_name = net_district_en_name  # type: str
        self.instance_count = instance_count  # type: str

    def validate(self):
        self.validate_required(self.net_district_code, 'net_district_code')
        self.validate_required(self.net_district_name, 'net_district_name')
        self.validate_required(self.ens_region_id_count, 'ens_region_id_count')
        self.validate_required(self.net_district_level, 'net_district_level')
        self.validate_required(self.net_district_father_code, 'net_district_father_code')
        self.validate_required(self.net_district_en_name, 'net_district_en_name')
        self.validate_required(self.instance_count, 'instance_count')

    def to_map(self):
        result = {}
        result['NetDistrictCode'] = self.net_district_code
        result['NetDistrictName'] = self.net_district_name
        result['EnsRegionIdCount'] = self.ens_region_id_count
        result['NetDistrictLevel'] = self.net_district_level
        result['NetDistrictFatherCode'] = self.net_district_father_code
        result['NetDistrictEnName'] = self.net_district_en_name
        result['InstanceCount'] = self.instance_count
        return result

    def from_map(self, map={}):
        self.net_district_code = map.get('NetDistrictCode')
        self.net_district_name = map.get('NetDistrictName')
        self.ens_region_id_count = map.get('EnsRegionIdCount')
        self.net_district_level = map.get('NetDistrictLevel')
        self.net_district_father_code = map.get('NetDistrictFatherCode')
        self.net_district_en_name = map.get('NetDistrictEnName')
        self.instance_count = map.get('InstanceCount')
        return self


class DescribeEnsNetSaleDistrictResponseEnsNetDistricts(TeaModel):
    def __init__(self, ens_net_district=None):
        self.ens_net_district = ens_net_district  # type: List[DescribeEnsNetSaleDistrictResponseEnsNetDistrictsEnsNetDistrict]

    def validate(self):
        self.validate_required(self.ens_net_district, 'ens_net_district')
        if self.ens_net_district:
            for k in self.ens_net_district:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EnsNetDistrict'] = []
        if self.ens_net_district is not None:
            for k in self.ens_net_district:
                result['EnsNetDistrict'].append(k.to_map() if k else None)
        else:
            result['EnsNetDistrict'] = None
        return result

    def from_map(self, map={}):
        self.ens_net_district = []
        if map.get('EnsNetDistrict') is not None:
            for k in map.get('EnsNetDistrict'):
                temp_model = DescribeEnsNetSaleDistrictResponseEnsNetDistrictsEnsNetDistrict()
                self.ens_net_district.append(temp_model.from_map(k))
        else:
            self.ens_net_district = None
        return self


class DescribeEnsNetDistrictRequest(TeaModel):
    def __init__(self, version=None, net_level_code=None, net_district_code=None):
        self.version = version          # type: str
        self.net_level_code = net_level_code  # type: str
        self.net_district_code = net_district_code  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.net_level_code, 'net_level_code')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['NetLevelCode'] = self.net_level_code
        result['NetDistrictCode'] = self.net_district_code
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.net_level_code = map.get('NetLevelCode')
        self.net_district_code = map.get('NetDistrictCode')
        return self


class DescribeEnsNetDistrictResponse(TeaModel):
    def __init__(self, request_id=None, code=None, ens_net_districts=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.ens_net_districts = ens_net_districts  # type: DescribeEnsNetDistrictResponseEnsNetDistricts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.ens_net_districts, 'ens_net_districts')
        if self.ens_net_districts:
            self.ens_net_districts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.ens_net_districts is not None:
            result['EnsNetDistricts'] = self.ens_net_districts.to_map()
        else:
            result['EnsNetDistricts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('EnsNetDistricts') is not None:
            temp_model = DescribeEnsNetDistrictResponseEnsNetDistricts()
            self.ens_net_districts = temp_model.from_map(map['EnsNetDistricts'])
        else:
            self.ens_net_districts = None
        return self


class DescribeEnsNetDistrictResponseEnsNetDistrictsEnsNetDistrict(TeaModel):
    def __init__(self, net_district_code=None, net_district_name=None, net_district_father_code=None,
                 ens_region_id_count=None, net_district_level=None, net_district_en_name=None):
        self.net_district_code = net_district_code  # type: str
        self.net_district_name = net_district_name  # type: str
        self.net_district_father_code = net_district_father_code  # type: str
        self.ens_region_id_count = ens_region_id_count  # type: str
        self.net_district_level = net_district_level  # type: str
        self.net_district_en_name = net_district_en_name  # type: str

    def validate(self):
        self.validate_required(self.net_district_code, 'net_district_code')
        self.validate_required(self.net_district_name, 'net_district_name')
        self.validate_required(self.net_district_father_code, 'net_district_father_code')
        self.validate_required(self.ens_region_id_count, 'ens_region_id_count')
        self.validate_required(self.net_district_level, 'net_district_level')
        self.validate_required(self.net_district_en_name, 'net_district_en_name')

    def to_map(self):
        result = {}
        result['NetDistrictCode'] = self.net_district_code
        result['NetDistrictName'] = self.net_district_name
        result['NetDistrictFatherCode'] = self.net_district_father_code
        result['EnsRegionIdCount'] = self.ens_region_id_count
        result['NetDistrictLevel'] = self.net_district_level
        result['NetDistrictEnName'] = self.net_district_en_name
        return result

    def from_map(self, map={}):
        self.net_district_code = map.get('NetDistrictCode')
        self.net_district_name = map.get('NetDistrictName')
        self.net_district_father_code = map.get('NetDistrictFatherCode')
        self.ens_region_id_count = map.get('EnsRegionIdCount')
        self.net_district_level = map.get('NetDistrictLevel')
        self.net_district_en_name = map.get('NetDistrictEnName')
        return self


class DescribeEnsNetDistrictResponseEnsNetDistricts(TeaModel):
    def __init__(self, ens_net_district=None):
        self.ens_net_district = ens_net_district  # type: List[DescribeEnsNetDistrictResponseEnsNetDistrictsEnsNetDistrict]

    def validate(self):
        self.validate_required(self.ens_net_district, 'ens_net_district')
        if self.ens_net_district:
            for k in self.ens_net_district:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EnsNetDistrict'] = []
        if self.ens_net_district is not None:
            for k in self.ens_net_district:
                result['EnsNetDistrict'].append(k.to_map() if k else None)
        else:
            result['EnsNetDistrict'] = None
        return result

    def from_map(self, map={}):
        self.ens_net_district = []
        if map.get('EnsNetDistrict') is not None:
            for k in map.get('EnsNetDistrict'):
                temp_model = DescribeEnsNetDistrictResponseEnsNetDistrictsEnsNetDistrict()
                self.ens_net_district.append(temp_model.from_map(k))
        else:
            self.ens_net_district = None
        return self


class PreCreateEnsServiceRequest(TeaModel):
    def __init__(self, version=None, ens_service_name=None, image_id=None, instance_spec=None,
                 system_disk_size=None, data_disk_size=None, bandwidth_type=None, instance_bandwithd_limit=None, password=None,
                 key_pair_name=None, user_data=None, net_level=None, scheduling_strategy=None, scheduling_price_strategy=None,
                 buy_resources_detail=None):
        self.version = version          # type: str
        self.ens_service_name = ens_service_name  # type: str
        self.image_id = image_id        # type: str
        self.instance_spec = instance_spec  # type: str
        self.system_disk_size = system_disk_size  # type: str
        self.data_disk_size = data_disk_size  # type: str
        self.bandwidth_type = bandwidth_type  # type: str
        self.instance_bandwithd_limit = instance_bandwithd_limit  # type: str
        self.password = password        # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.user_data = user_data      # type: str
        self.net_level = net_level      # type: str
        self.scheduling_strategy = scheduling_strategy  # type: str
        self.scheduling_price_strategy = scheduling_price_strategy  # type: str
        self.buy_resources_detail = buy_resources_detail  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_service_name, 'ens_service_name')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.instance_spec, 'instance_spec')
        self.validate_required(self.system_disk_size, 'system_disk_size')
        self.validate_required(self.bandwidth_type, 'bandwidth_type')
        self.validate_required(self.instance_bandwithd_limit, 'instance_bandwithd_limit')
        self.validate_required(self.net_level, 'net_level')
        self.validate_required(self.scheduling_strategy, 'scheduling_strategy')
        self.validate_required(self.buy_resources_detail, 'buy_resources_detail')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsServiceName'] = self.ens_service_name
        result['ImageId'] = self.image_id
        result['InstanceSpec'] = self.instance_spec
        result['SystemDiskSize'] = self.system_disk_size
        result['DataDiskSize'] = self.data_disk_size
        result['BandwidthType'] = self.bandwidth_type
        result['InstanceBandwithdLimit'] = self.instance_bandwithd_limit
        result['Password'] = self.password
        result['KeyPairName'] = self.key_pair_name
        result['UserData'] = self.user_data
        result['NetLevel'] = self.net_level
        result['SchedulingStrategy'] = self.scheduling_strategy
        result['SchedulingPriceStrategy'] = self.scheduling_price_strategy
        result['BuyResourcesDetail'] = self.buy_resources_detail
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_service_name = map.get('EnsServiceName')
        self.image_id = map.get('ImageId')
        self.instance_spec = map.get('InstanceSpec')
        self.system_disk_size = map.get('SystemDiskSize')
        self.data_disk_size = map.get('DataDiskSize')
        self.bandwidth_type = map.get('BandwidthType')
        self.instance_bandwithd_limit = map.get('InstanceBandwithdLimit')
        self.password = map.get('Password')
        self.key_pair_name = map.get('KeyPairName')
        self.user_data = map.get('UserData')
        self.net_level = map.get('NetLevel')
        self.scheduling_strategy = map.get('SchedulingStrategy')
        self.scheduling_price_strategy = map.get('SchedulingPriceStrategy')
        self.buy_resources_detail = map.get('BuyResourcesDetail')
        return self


class PreCreateEnsServiceResponse(TeaModel):
    def __init__(self, request_id=None, code=None, ens_service_id=None, net_level=None, buy_resources_detail=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.ens_service_id = ens_service_id  # type: str
        self.net_level = net_level      # type: str
        self.buy_resources_detail = buy_resources_detail  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.ens_service_id, 'ens_service_id')
        self.validate_required(self.net_level, 'net_level')
        self.validate_required(self.buy_resources_detail, 'buy_resources_detail')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['EnsServiceId'] = self.ens_service_id
        result['NetLevel'] = self.net_level
        result['BuyResourcesDetail'] = self.buy_resources_detail
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.ens_service_id = map.get('EnsServiceId')
        self.net_level = map.get('NetLevel')
        self.buy_resources_detail = map.get('BuyResourcesDetail')
        return self


class DescribeBandWithdChargeTypeRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeBandWithdChargeTypeResponse(TeaModel):
    def __init__(self, request_id=None, code=None, band_with_type_info=None, charge_cycle_info=None,
                 charge_contract_type=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.band_with_type_info = band_with_type_info  # type: str
        self.charge_cycle_info = charge_cycle_info  # type: str
        self.charge_contract_type = charge_contract_type  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.band_with_type_info, 'band_with_type_info')
        self.validate_required(self.charge_cycle_info, 'charge_cycle_info')
        self.validate_required(self.charge_contract_type, 'charge_contract_type')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['BandWithTypeInfo'] = self.band_with_type_info
        result['ChargeCycleInfo'] = self.charge_cycle_info
        result['ChargeContractType'] = self.charge_contract_type
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.band_with_type_info = map.get('BandWithTypeInfo')
        self.charge_cycle_info = map.get('ChargeCycleInfo')
        self.charge_contract_type = map.get('ChargeContractType')
        return self


class ModifyImageAttributeRequest(TeaModel):
    def __init__(self, product=None, version=None, image_id=None, image_name=None):
        self.product = product          # type: str
        self.version = version          # type: str
        self.image_id = image_id        # type: str
        self.image_name = image_name    # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_name, 'image_name')

    def to_map(self):
        result = {}
        result['product'] = self.product
        result['Version'] = self.version
        result['ImageId'] = self.image_id
        result['ImageName'] = self.image_name
        return result

    def from_map(self, map={}):
        self.product = map.get('product')
        self.version = map.get('Version')
        self.image_id = map.get('ImageId')
        self.image_name = map.get('ImageName')
        return self


class ModifyImageAttributeResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class CreateEnsServiceRequest(TeaModel):
    def __init__(self, version=None, ens_service_id=None, order_type=None):
        self.version = version          # type: str
        self.ens_service_id = ens_service_id  # type: str
        self.order_type = order_type    # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.ens_service_id, 'ens_service_id')
        self.validate_required(self.order_type, 'order_type')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsServiceId'] = self.ens_service_id
        result['OrderType'] = self.order_type
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_service_id = map.get('EnsServiceId')
        self.order_type = map.get('OrderType')
        return self


class CreateEnsServiceResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class DescribeEnsNetLevelRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeEnsNetLevelResponse(TeaModel):
    def __init__(self, request_id=None, code=None, ens_net_levels=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.ens_net_levels = ens_net_levels  # type: DescribeEnsNetLevelResponseEnsNetLevels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.ens_net_levels, 'ens_net_levels')
        if self.ens_net_levels:
            self.ens_net_levels.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.ens_net_levels is not None:
            result['EnsNetLevels'] = self.ens_net_levels.to_map()
        else:
            result['EnsNetLevels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('EnsNetLevels') is not None:
            temp_model = DescribeEnsNetLevelResponseEnsNetLevels()
            self.ens_net_levels = temp_model.from_map(map['EnsNetLevels'])
        else:
            self.ens_net_levels = None
        return self


class DescribeEnsNetLevelResponseEnsNetLevelsEnsNetLevel(TeaModel):
    def __init__(self, ens_net_level_code=None):
        self.ens_net_level_code = ens_net_level_code  # type: str

    def validate(self):
        self.validate_required(self.ens_net_level_code, 'ens_net_level_code')

    def to_map(self):
        result = {}
        result['EnsNetLevelCode'] = self.ens_net_level_code
        return result

    def from_map(self, map={}):
        self.ens_net_level_code = map.get('EnsNetLevelCode')
        return self


class DescribeEnsNetLevelResponseEnsNetLevels(TeaModel):
    def __init__(self, ens_net_level=None):
        self.ens_net_level = ens_net_level  # type: List[DescribeEnsNetLevelResponseEnsNetLevelsEnsNetLevel]

    def validate(self):
        self.validate_required(self.ens_net_level, 'ens_net_level')
        if self.ens_net_level:
            for k in self.ens_net_level:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EnsNetLevel'] = []
        if self.ens_net_level is not None:
            for k in self.ens_net_level:
                result['EnsNetLevel'].append(k.to_map() if k else None)
        else:
            result['EnsNetLevel'] = None
        return result

    def from_map(self, map={}):
        self.ens_net_level = []
        if map.get('EnsNetLevel') is not None:
            for k in map.get('EnsNetLevel'):
                temp_model = DescribeEnsNetLevelResponseEnsNetLevelsEnsNetLevel()
                self.ens_net_level.append(temp_model.from_map(k))
        else:
            self.ens_net_level = None
        return self


class DescribeInstanceSpecRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeInstanceSpecResponse(TeaModel):
    def __init__(self, request_id=None, code=None, data_disk_min_size=None, data_disk_max_size=None,
                 system_disk_max_size=None, bandwidth_limit=None, instance_specs=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.data_disk_min_size = data_disk_min_size  # type: int
        self.data_disk_max_size = data_disk_max_size  # type: int
        self.system_disk_max_size = system_disk_max_size  # type: int
        self.bandwidth_limit = bandwidth_limit  # type: int
        self.instance_specs = instance_specs  # type: DescribeInstanceSpecResponseInstanceSpecs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data_disk_min_size, 'data_disk_min_size')
        self.validate_required(self.data_disk_max_size, 'data_disk_max_size')
        self.validate_required(self.system_disk_max_size, 'system_disk_max_size')
        self.validate_required(self.bandwidth_limit, 'bandwidth_limit')
        self.validate_required(self.instance_specs, 'instance_specs')
        if self.instance_specs:
            self.instance_specs.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['DataDiskMinSize'] = self.data_disk_min_size
        result['DataDiskMaxSize'] = self.data_disk_max_size
        result['SystemDiskMaxSize'] = self.system_disk_max_size
        result['BandwidthLimit'] = self.bandwidth_limit
        if self.instance_specs is not None:
            result['InstanceSpecs'] = self.instance_specs.to_map()
        else:
            result['InstanceSpecs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.data_disk_min_size = map.get('DataDiskMinSize')
        self.data_disk_max_size = map.get('DataDiskMaxSize')
        self.system_disk_max_size = map.get('SystemDiskMaxSize')
        self.bandwidth_limit = map.get('BandwidthLimit')
        if map.get('InstanceSpecs') is not None:
            temp_model = DescribeInstanceSpecResponseInstanceSpecs()
            self.instance_specs = temp_model.from_map(map['InstanceSpecs'])
        else:
            self.instance_specs = None
        return self


class DescribeInstanceSpecResponseInstanceSpecsInstanceSpec(TeaModel):
    def __init__(self, instance_type=None, core=None, memory=None, display_name=None):
        self.instance_type = instance_type  # type: str
        self.core = core                # type: str
        self.memory = memory            # type: str
        self.display_name = display_name  # type: str

    def validate(self):
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.core, 'core')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.display_name, 'display_name')

    def to_map(self):
        result = {}
        result['InstanceType'] = self.instance_type
        result['Core'] = self.core
        result['Memory'] = self.memory
        result['DisplayName'] = self.display_name
        return result

    def from_map(self, map={}):
        self.instance_type = map.get('InstanceType')
        self.core = map.get('Core')
        self.memory = map.get('Memory')
        self.display_name = map.get('DisplayName')
        return self


class DescribeInstanceSpecResponseInstanceSpecs(TeaModel):
    def __init__(self, instance_spec=None):
        self.instance_spec = instance_spec  # type: List[DescribeInstanceSpecResponseInstanceSpecsInstanceSpec]

    def validate(self):
        self.validate_required(self.instance_spec, 'instance_spec')
        if self.instance_spec:
            for k in self.instance_spec:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceSpec'] = []
        if self.instance_spec is not None:
            for k in self.instance_spec:
                result['InstanceSpec'].append(k.to_map() if k else None)
        else:
            result['InstanceSpec'] = None
        return result

    def from_map(self, map={}):
        self.instance_spec = []
        if map.get('InstanceSpec') is not None:
            for k in map.get('InstanceSpec'):
                temp_model = DescribeInstanceSpecResponseInstanceSpecsInstanceSpec()
                self.instance_spec.append(temp_model.from_map(k))
        else:
            self.instance_spec = None
        return self


class DescribeInstanceAutoRenewAttributeRequest(TeaModel):
    def __init__(self, version=None, instance_ids=None):
        self.version = version          # type: str
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_ids, 'instance_ids')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_ids = map.get('InstanceIds')
        return self


class DescribeInstanceAutoRenewAttributeResponse(TeaModel):
    def __init__(self, request_id=None, code=None, instance_renew_attributes=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.instance_renew_attributes = instance_renew_attributes  # type: DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.instance_renew_attributes, 'instance_renew_attributes')
        if self.instance_renew_attributes:
            self.instance_renew_attributes.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.instance_renew_attributes is not None:
            result['InstanceRenewAttributes'] = self.instance_renew_attributes.to_map()
        else:
            result['InstanceRenewAttributes'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('InstanceRenewAttributes') is not None:
            temp_model = DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributes()
            self.instance_renew_attributes = temp_model.from_map(map['InstanceRenewAttributes'])
        else:
            self.instance_renew_attributes = None
        return self


class DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributesInstanceRenewAttribute(TeaModel):
    def __init__(self, instance_id=None, auto_renewal=None, duration=None):
        self.instance_id = instance_id  # type: str
        self.auto_renewal = auto_renewal  # type: bool
        self.duration = duration        # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.auto_renewal, 'auto_renewal')
        self.validate_required(self.duration, 'duration')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['AutoRenewal'] = self.auto_renewal
        result['Duration'] = self.duration
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.auto_renewal = map.get('AutoRenewal')
        self.duration = map.get('Duration')
        return self


class DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributes(TeaModel):
    def __init__(self, instance_renew_attribute=None):
        self.instance_renew_attribute = instance_renew_attribute  # type: List[DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributesInstanceRenewAttribute]

    def validate(self):
        self.validate_required(self.instance_renew_attribute, 'instance_renew_attribute')
        if self.instance_renew_attribute:
            for k in self.instance_renew_attribute:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceRenewAttribute'] = []
        if self.instance_renew_attribute is not None:
            for k in self.instance_renew_attribute:
                result['InstanceRenewAttribute'].append(k.to_map() if k else None)
        else:
            result['InstanceRenewAttribute'] = None
        return result

    def from_map(self, map={}):
        self.instance_renew_attribute = []
        if map.get('InstanceRenewAttribute') is not None:
            for k in map.get('InstanceRenewAttribute'):
                temp_model = DescribeInstanceAutoRenewAttributeResponseInstanceRenewAttributesInstanceRenewAttribute()
                self.instance_renew_attribute.append(temp_model.from_map(k))
        else:
            self.instance_renew_attribute = None
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(self, version=None):
        self.version = version          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(self, request_id=None, code=None, images=None, support_resources=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.images = images            # type: DescribeAvailableResourceResponseImages
        self.support_resources = support_resources  # type: DescribeAvailableResourceResponseSupportResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.images, 'images')
        if self.images:
            self.images.validate()
        self.validate_required(self.support_resources, 'support_resources')
        if self.support_resources:
            self.support_resources.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        else:
            result['Images'] = None
        if self.support_resources is not None:
            result['SupportResources'] = self.support_resources.to_map()
        else:
            result['SupportResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('Images') is not None:
            temp_model = DescribeAvailableResourceResponseImages()
            self.images = temp_model.from_map(map['Images'])
        else:
            self.images = None
        if map.get('SupportResources') is not None:
            temp_model = DescribeAvailableResourceResponseSupportResources()
            self.support_resources = temp_model.from_map(map['SupportResources'])
        else:
            self.support_resources = None
        return self


class DescribeAvailableResourceResponseImagesImage(TeaModel):
    def __init__(self, image_id=None, image_name=None):
        self.image_id = image_id        # type: str
        self.image_name = image_name    # type: str

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_name, 'image_name')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['ImageName'] = self.image_name
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.image_name = map.get('ImageName')
        return self


class DescribeAvailableResourceResponseImages(TeaModel):
    def __init__(self, image=None):
        self.image = image              # type: List[DescribeAvailableResourceResponseImagesImage]

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        else:
            result['Image'] = None
        return result

    def from_map(self, map={}):
        self.image = []
        if map.get('Image') is not None:
            for k in map.get('Image'):
                temp_model = DescribeAvailableResourceResponseImagesImage()
                self.image.append(temp_model.from_map(k))
        else:
            self.image = None
        return self


class DescribeAvailableResourceResponseSupportResourcesSupportResource(TeaModel):
    def __init__(self, data_disk_size=None, ens_region_id=None, support_resources_count=None, instance_spec=None,
                 system_disk_size=None):
        self.data_disk_size = data_disk_size  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.support_resources_count = support_resources_count  # type: str
        self.instance_spec = instance_spec  # type: str
        self.system_disk_size = system_disk_size  # type: str

    def validate(self):
        self.validate_required(self.data_disk_size, 'data_disk_size')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.support_resources_count, 'support_resources_count')
        self.validate_required(self.instance_spec, 'instance_spec')
        self.validate_required(self.system_disk_size, 'system_disk_size')

    def to_map(self):
        result = {}
        result['DataDiskSize'] = self.data_disk_size
        result['EnsRegionId'] = self.ens_region_id
        result['SupportResourcesCount'] = self.support_resources_count
        result['InstanceSpec'] = self.instance_spec
        result['SystemDiskSize'] = self.system_disk_size
        return result

    def from_map(self, map={}):
        self.data_disk_size = map.get('DataDiskSize')
        self.ens_region_id = map.get('EnsRegionId')
        self.support_resources_count = map.get('SupportResourcesCount')
        self.instance_spec = map.get('InstanceSpec')
        self.system_disk_size = map.get('SystemDiskSize')
        return self


class DescribeAvailableResourceResponseSupportResources(TeaModel):
    def __init__(self, support_resource=None):
        self.support_resource = support_resource  # type: List[DescribeAvailableResourceResponseSupportResourcesSupportResource]

    def validate(self):
        self.validate_required(self.support_resource, 'support_resource')
        if self.support_resource:
            for k in self.support_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SupportResource'] = []
        if self.support_resource is not None:
            for k in self.support_resource:
                result['SupportResource'].append(k.to_map() if k else None)
        else:
            result['SupportResource'] = None
        return result

    def from_map(self, map={}):
        self.support_resource = []
        if map.get('SupportResource') is not None:
            for k in map.get('SupportResource'):
                temp_model = DescribeAvailableResourceResponseSupportResourcesSupportResource()
                self.support_resource.append(temp_model.from_map(k))
        else:
            self.support_resource = None
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, instance_type=None, ens_region_id=None, password=None, period=None, image_id=None,
                 system_disk=None, quantity=None, data_disk=None, internet_charge_type=None, auto_renew_period=None,
                 auto_renew=None, ip_type=None, key_pair_name=None, user_data=None, v_switch_id=None, private_ip_address=None,
                 payment_type=None, instance_name=None, host_name=None, unique_suffix=None):
        self.instance_type = instance_type  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.password = password        # type: str
        self.period = period            # type: str
        self.image_id = image_id        # type: str
        self.system_disk = system_disk  # type: CreateInstanceRequestSystemDisk
        self.quantity = quantity        # type: str
        self.data_disk = data_disk      # type: List[CreateInstanceRequestDataDisk]
        self.internet_charge_type = internet_charge_type  # type: str
        self.auto_renew_period = auto_renew_period  # type: str
        self.auto_renew = auto_renew    # type: str
        self.ip_type = ip_type          # type: str
        self.key_pair_name = key_pair_name  # type: str
        self.user_data = user_data      # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.private_ip_address = private_ip_address  # type: str
        self.payment_type = payment_type  # type: str
        self.instance_name = instance_name  # type: str
        self.host_name = host_name      # type: str
        self.unique_suffix = unique_suffix  # type: bool

    def validate(self):
        self.validate_required(self.instance_type, 'instance_type')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.period, 'period')
        self.validate_required(self.image_id, 'image_id')
        if self.system_disk:
            self.system_disk.validate()
        self.validate_required(self.quantity, 'quantity')
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceType'] = self.instance_type
        result['EnsRegionId'] = self.ens_region_id
        result['Password'] = self.password
        result['Period'] = self.period
        result['ImageId'] = self.image_id
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        else:
            result['SystemDisk'] = None
        result['Quantity'] = self.quantity
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        else:
            result['DataDisk'] = None
        result['InternetChargeType'] = self.internet_charge_type
        result['AutoRenewPeriod'] = self.auto_renew_period
        result['AutoRenew'] = self.auto_renew
        result['IpType'] = self.ip_type
        result['KeyPairName'] = self.key_pair_name
        result['UserData'] = self.user_data
        result['VSwitchId'] = self.v_switch_id
        result['PrivateIpAddress'] = self.private_ip_address
        result['PaymentType'] = self.payment_type
        result['InstanceName'] = self.instance_name
        result['HostName'] = self.host_name
        result['UniqueSuffix'] = self.unique_suffix
        return result

    def from_map(self, map={}):
        self.instance_type = map.get('InstanceType')
        self.ens_region_id = map.get('EnsRegionId')
        self.password = map.get('Password')
        self.period = map.get('Period')
        self.image_id = map.get('ImageId')
        if map.get('SystemDisk') is not None:
            temp_model = CreateInstanceRequestSystemDisk()
            self.system_disk = temp_model.from_map(map['SystemDisk'])
        else:
            self.system_disk = None
        self.quantity = map.get('Quantity')
        self.data_disk = []
        if map.get('DataDisk') is not None:
            for k in map.get('DataDisk'):
                temp_model = CreateInstanceRequestDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        else:
            self.data_disk = None
        self.internet_charge_type = map.get('InternetChargeType')
        self.auto_renew_period = map.get('AutoRenewPeriod')
        self.auto_renew = map.get('AutoRenew')
        self.ip_type = map.get('IpType')
        self.key_pair_name = map.get('KeyPairName')
        self.user_data = map.get('UserData')
        self.v_switch_id = map.get('VSwitchId')
        self.private_ip_address = map.get('PrivateIpAddress')
        self.payment_type = map.get('PaymentType')
        self.instance_name = map.get('InstanceName')
        self.host_name = map.get('HostName')
        self.unique_suffix = map.get('UniqueSuffix')
        return self


class CreateInstanceRequestSystemDisk(TeaModel):
    def __init__(self, size=None):
        self.size = size                # type: str

    def validate(self):
        self.validate_required(self.size, 'size')

    def to_map(self):
        result = {}
        result['Size'] = self.size
        return result

    def from_map(self, map={}):
        self.size = map.get('Size')
        return self


class CreateInstanceRequestDataDisk(TeaModel):
    def __init__(self, size=None):
        self.size = size                # type: str

    def validate(self):
        self.validate_required(self.size, 'size')

    def to_map(self):
        result = {}
        result['Size'] = self.size
        return result

    def from_map(self, map={}):
        self.size = map.get('Size')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, request_id=None, code=None, instance_ids=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.instance_ids = instance_ids  # type: CreateInstanceResponseInstanceIds

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.instance_ids, 'instance_ids')
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        else:
            result['InstanceIds'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('InstanceIds') is not None:
            temp_model = CreateInstanceResponseInstanceIds()
            self.instance_ids = temp_model.from_map(map['InstanceIds'])
        else:
            self.instance_ids = None
        return self


class CreateInstanceResponseInstanceIds(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: List[str]

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        return self


class ReInitDiskRequest(TeaModel):
    def __init__(self, version=None, disk_id=None, image_id=None):
        self.version = version          # type: str
        self.disk_id = disk_id          # type: str
        self.image_id = image_id        # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.disk_id, 'disk_id')
        self.validate_required(self.image_id, 'image_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['DiskId'] = self.disk_id
        result['ImageId'] = self.image_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.disk_id = map.get('DiskId')
        self.image_id = map.get('ImageId')
        return self


class ReInitDiskResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class DescribeImageInfosRequest(TeaModel):
    def __init__(self, version=None, os_type=None):
        self.version = version          # type: str
        self.os_type = os_type          # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['OsType'] = self.os_type
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.os_type = map.get('OsType')
        return self


class DescribeImageInfosResponse(TeaModel):
    def __init__(self, request_id=None, code=None, images=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.images = images            # type: DescribeImageInfosResponseImages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.images, 'images')
        if self.images:
            self.images.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.images is not None:
            result['Images'] = self.images.to_map()
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('Images') is not None:
            temp_model = DescribeImageInfosResponseImages()
            self.images = temp_model.from_map(map['Images'])
        else:
            self.images = None
        return self


class DescribeImageInfosResponseImagesImage(TeaModel):
    def __init__(self, image_id=None, description=None, image_version=None, ostype=None, osname=None,
                 image_size=None):
        self.image_id = image_id        # type: str
        self.description = description  # type: str
        self.image_version = image_version  # type: str
        self.ostype = ostype            # type: str
        self.osname = osname            # type: str
        self.image_size = image_size    # type: str

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.description, 'description')
        self.validate_required(self.image_version, 'image_version')
        self.validate_required(self.ostype, 'ostype')
        self.validate_required(self.osname, 'osname')
        self.validate_required(self.image_size, 'image_size')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['Description'] = self.description
        result['ImageVersion'] = self.image_version
        result['OSType'] = self.ostype
        result['OSName'] = self.osname
        result['ImageSize'] = self.image_size
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.description = map.get('Description')
        self.image_version = map.get('ImageVersion')
        self.ostype = map.get('OSType')
        self.osname = map.get('OSName')
        self.image_size = map.get('ImageSize')
        return self


class DescribeImageInfosResponseImages(TeaModel):
    def __init__(self, image=None):
        self.image = image              # type: List[DescribeImageInfosResponseImagesImage]

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        else:
            result['Image'] = None
        return result

    def from_map(self, map={}):
        self.image = []
        if map.get('Image') is not None:
            for k in map.get('Image'):
                temp_model = DescribeImageInfosResponseImagesImage()
                self.image.append(temp_model.from_map(k))
        else:
            self.image = None
        return self


class DescribeUserBandWidthDataRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, instance_id=None, start_time=None, end_time=None,
                 period=None, isp=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.period = period            # type: str
        self.isp = isp                  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.period, 'period')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['InstanceId'] = self.instance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Period'] = self.period
        result['Isp'] = self.isp
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.instance_id = map.get('InstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.period = map.get('Period')
        self.isp = map.get('Isp')
        return self


class DescribeUserBandWidthDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, monitor_data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.monitor_data = monitor_data  # type: DescribeUserBandWidthDataResponseMonitorData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.monitor_data, 'monitor_data')
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        else:
            result['MonitorData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('MonitorData') is not None:
            temp_model = DescribeUserBandWidthDataResponseMonitorData()
            self.monitor_data = temp_model.from_map(map['MonitorData'])
        else:
            self.monitor_data = None
        return self


class DescribeUserBandWidthDataResponseMonitorDataBandWidthMonitorData(TeaModel):
    def __init__(self, up_band_width=None, down_band_width=None, internet_tx=None, internet_rx=None,
                 time_stamp=None):
        self.up_band_width = up_band_width  # type: int
        self.down_band_width = down_band_width  # type: int
        self.internet_tx = internet_tx  # type: int
        self.internet_rx = internet_rx  # type: int
        self.time_stamp = time_stamp    # type: str

    def validate(self):
        self.validate_required(self.up_band_width, 'up_band_width')
        self.validate_required(self.down_band_width, 'down_band_width')
        self.validate_required(self.internet_tx, 'internet_tx')
        self.validate_required(self.internet_rx, 'internet_rx')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['UpBandWidth'] = self.up_band_width
        result['DownBandWidth'] = self.down_band_width
        result['InternetTX'] = self.internet_tx
        result['InternetRX'] = self.internet_rx
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.up_band_width = map.get('UpBandWidth')
        self.down_band_width = map.get('DownBandWidth')
        self.internet_tx = map.get('InternetTX')
        self.internet_rx = map.get('InternetRX')
        self.time_stamp = map.get('TimeStamp')
        return self


class DescribeUserBandWidthDataResponseMonitorData(TeaModel):
    def __init__(self, max_down_band_width=None, max_up_band_width=None, band_width_monitor_data=None):
        self.max_down_band_width = max_down_band_width  # type: str
        self.max_up_band_width = max_up_band_width  # type: str
        self.band_width_monitor_data = band_width_monitor_data  # type: List[DescribeUserBandWidthDataResponseMonitorDataBandWidthMonitorData]

    def validate(self):
        self.validate_required(self.max_down_band_width, 'max_down_band_width')
        self.validate_required(self.max_up_band_width, 'max_up_band_width')
        self.validate_required(self.band_width_monitor_data, 'band_width_monitor_data')
        if self.band_width_monitor_data:
            for k in self.band_width_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['MaxDownBandWidth'] = self.max_down_band_width
        result['MaxUpBandWidth'] = self.max_up_band_width
        result['BandWidthMonitorData'] = []
        if self.band_width_monitor_data is not None:
            for k in self.band_width_monitor_data:
                result['BandWidthMonitorData'].append(k.to_map() if k else None)
        else:
            result['BandWidthMonitorData'] = None
        return result

    def from_map(self, map={}):
        self.max_down_band_width = map.get('MaxDownBandWidth')
        self.max_up_band_width = map.get('MaxUpBandWidth')
        self.band_width_monitor_data = []
        if map.get('BandWidthMonitorData') is not None:
            for k in map.get('BandWidthMonitorData'):
                temp_model = DescribeUserBandWidthDataResponseMonitorDataBandWidthMonitorData()
                self.band_width_monitor_data.append(temp_model.from_map(k))
        else:
            self.band_width_monitor_data = None
        return self


class RebootInstanceRequest(TeaModel):
    def __init__(self, version=None, instance_id=None, force_stop=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str
        self.force_stop = force_stop    # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        result['ForceStop'] = self.force_stop
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        self.force_stop = map.get('ForceStop')
        return self


class RebootInstanceResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class DescribeEnsRegionsRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        return self


class DescribeEnsRegionsResponse(TeaModel):
    def __init__(self, request_id=None, code=None, ens_regions=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.ens_regions = ens_regions  # type: DescribeEnsRegionsResponseEnsRegions

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.ens_regions, 'ens_regions')
        if self.ens_regions:
            self.ens_regions.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.ens_regions is not None:
            result['EnsRegions'] = self.ens_regions.to_map()
        else:
            result['EnsRegions'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('EnsRegions') is not None:
            temp_model = DescribeEnsRegionsResponseEnsRegions()
            self.ens_regions = temp_model.from_map(map['EnsRegions'])
        else:
            self.ens_regions = None
        return self


class DescribeEnsRegionsResponseEnsRegionsEnsRegions(TeaModel):
    def __init__(self, ens_region_id=None, name=None, en_name=None, area=None, province=None):
        self.ens_region_id = ens_region_id  # type: str
        self.name = name                # type: str
        self.en_name = en_name          # type: str
        self.area = area                # type: str
        self.province = province        # type: str

    def validate(self):
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.en_name, 'en_name')
        self.validate_required(self.area, 'area')
        self.validate_required(self.province, 'province')

    def to_map(self):
        result = {}
        result['EnsRegionId'] = self.ens_region_id
        result['Name'] = self.name
        result['EnName'] = self.en_name
        result['Area'] = self.area
        result['Province'] = self.province
        return result

    def from_map(self, map={}):
        self.ens_region_id = map.get('EnsRegionId')
        self.name = map.get('Name')
        self.en_name = map.get('EnName')
        self.area = map.get('Area')
        self.province = map.get('Province')
        return self


class DescribeEnsRegionsResponseEnsRegions(TeaModel):
    def __init__(self, ens_regions=None):
        self.ens_regions = ens_regions  # type: List[DescribeEnsRegionsResponseEnsRegionsEnsRegions]

    def validate(self):
        self.validate_required(self.ens_regions, 'ens_regions')
        if self.ens_regions:
            for k in self.ens_regions:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EnsRegions'] = []
        if self.ens_regions is not None:
            for k in self.ens_regions:
                result['EnsRegions'].append(k.to_map() if k else None)
        else:
            result['EnsRegions'] = None
        return result

    def from_map(self, map={}):
        self.ens_regions = []
        if map.get('EnsRegions') is not None:
            for k in map.get('EnsRegions'):
                temp_model = DescribeEnsRegionsResponseEnsRegionsEnsRegions()
                self.ens_regions.append(temp_model.from_map(k))
        else:
            self.ens_regions = None
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, version=None, instance_id=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class DescribeInstanceMonitorDataRequest(TeaModel):
    def __init__(self, version=None, instance_id=None, start_time=None, end_time=None, period=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.period = period            # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Period'] = self.period
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.period = map.get('Period')
        return self


class DescribeInstanceMonitorDataResponse(TeaModel):
    def __init__(self, request_id=None, code=None, monitor_data=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.monitor_data = monitor_data  # type: DescribeInstanceMonitorDataResponseMonitorData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.monitor_data, 'monitor_data')
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()
        else:
            result['MonitorData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        if map.get('MonitorData') is not None:
            temp_model = DescribeInstanceMonitorDataResponseMonitorData()
            self.monitor_data = temp_model.from_map(map['MonitorData'])
        else:
            self.monitor_data = None
        return self


class DescribeInstanceMonitorDataResponseMonitorDataInstanceMonitorData(TeaModel):
    def __init__(self, instance_id=None, memory=None, cpu=None):
        self.instance_id = instance_id  # type: str
        self.memory = memory            # type: str
        self.cpu = cpu                  # type: str

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.cpu, 'cpu')

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['Memory'] = self.memory
        result['CPU'] = self.cpu
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.memory = map.get('Memory')
        self.cpu = map.get('CPU')
        return self


class DescribeInstanceMonitorDataResponseMonitorData(TeaModel):
    def __init__(self, instance_monitor_data=None):
        self.instance_monitor_data = instance_monitor_data  # type: List[DescribeInstanceMonitorDataResponseMonitorDataInstanceMonitorData]

    def validate(self):
        self.validate_required(self.instance_monitor_data, 'instance_monitor_data')
        if self.instance_monitor_data:
            for k in self.instance_monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['InstanceMonitorData'] = []
        if self.instance_monitor_data is not None:
            for k in self.instance_monitor_data:
                result['InstanceMonitorData'].append(k.to_map() if k else None)
        else:
            result['InstanceMonitorData'] = None
        return result

    def from_map(self, map={}):
        self.instance_monitor_data = []
        if map.get('InstanceMonitorData') is not None:
            for k in map.get('InstanceMonitorData'):
                temp_model = DescribeInstanceMonitorDataResponseMonitorDataInstanceMonitorData()
                self.instance_monitor_data.append(temp_model.from_map(k))
        else:
            self.instance_monitor_data = None
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, version=None, ens_region_id=None, instance_id=None, ens_region_ids=None, instance_ids=None,
                 instance_name=None, image_id=None, page_number=None, page_size=None, status=None, order_by_params=None,
                 ens_service_id=None, instance_resource_type=None, search_key=None):
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.ens_region_ids = ens_region_ids  # type: str
        self.instance_ids = instance_ids  # type: str
        self.instance_name = instance_name  # type: str
        self.image_id = image_id        # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: str
        self.status = status            # type: str
        self.order_by_params = order_by_params  # type: str
        self.ens_service_id = ens_service_id  # type: str
        self.instance_resource_type = instance_resource_type  # type: str
        self.search_key = search_key    # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['InstanceId'] = self.instance_id
        result['EnsRegionIds'] = self.ens_region_ids
        result['InstanceIds'] = self.instance_ids
        result['InstanceName'] = self.instance_name
        result['ImageId'] = self.image_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['Status'] = self.status
        result['OrderByParams'] = self.order_by_params
        result['EnsServiceId'] = self.ens_service_id
        result['InstanceResourceType'] = self.instance_resource_type
        result['SearchKey'] = self.search_key
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.instance_id = map.get('InstanceId')
        self.ens_region_ids = map.get('EnsRegionIds')
        self.instance_ids = map.get('InstanceIds')
        self.instance_name = map.get('InstanceName')
        self.image_id = map.get('ImageId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.status = map.get('Status')
        self.order_by_params = map.get('OrderByParams')
        self.ens_service_id = map.get('EnsServiceId')
        self.instance_resource_type = map.get('InstanceResourceType')
        self.search_key = map.get('SearchKey')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, total_count=None, page_number=None, page_size=None,
                 instances=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.instances = instances      # type: DescribeInstancesResponseInstances

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.instances, 'instances')
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        else:
            result['Instances'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Instances') is not None:
            temp_model = DescribeInstancesResponseInstances()
            self.instances = temp_model.from_map(map['Instances'])
        else:
            self.instances = None
        return self


class DescribeInstancesResponseInstancesInstanceDataDiskDataDisk(TeaModel):
    def __init__(self, device_type=None, storage=None, uuid=None, disk_type=None, name=None, category=None, size=None,
                 disk_id=None, disk_name=None):
        self.device_type = device_type  # type: str
        self.storage = storage          # type: int
        self.uuid = uuid                # type: str
        self.disk_type = disk_type      # type: str
        self.name = name                # type: str
        self.category = category        # type: str
        self.size = size                # type: int
        self.disk_id = disk_id          # type: str
        self.disk_name = disk_name      # type: str

    def validate(self):
        self.validate_required(self.device_type, 'device_type')
        self.validate_required(self.storage, 'storage')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.disk_type, 'disk_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.category, 'category')
        self.validate_required(self.size, 'size')
        self.validate_required(self.disk_id, 'disk_id')
        self.validate_required(self.disk_name, 'disk_name')

    def to_map(self):
        result = {}
        result['device_type'] = self.device_type
        result['storage'] = self.storage
        result['uuid'] = self.uuid
        result['disk_type'] = self.disk_type
        result['name'] = self.name
        result['Category'] = self.category
        result['Size'] = self.size
        result['DiskId'] = self.disk_id
        result['DiskName'] = self.disk_name
        return result

    def from_map(self, map={}):
        self.device_type = map.get('device_type')
        self.storage = map.get('storage')
        self.uuid = map.get('uuid')
        self.disk_type = map.get('disk_type')
        self.name = map.get('name')
        self.category = map.get('Category')
        self.size = map.get('Size')
        self.disk_id = map.get('DiskId')
        self.disk_name = map.get('DiskName')
        return self


class DescribeInstancesResponseInstancesInstanceDataDisk(TeaModel):
    def __init__(self, data_disk=None):
        self.data_disk = data_disk      # type: List[DescribeInstancesResponseInstancesInstanceDataDiskDataDisk]

    def validate(self):
        self.validate_required(self.data_disk, 'data_disk')
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
        else:
            result['DataDisk'] = None
        return result

    def from_map(self, map={}):
        self.data_disk = []
        if map.get('DataDisk') is not None:
            for k in map.get('DataDisk'):
                temp_model = DescribeInstancesResponseInstancesInstanceDataDiskDataDisk()
                self.data_disk.append(temp_model.from_map(k))
        else:
            self.data_disk = None
        return self


class DescribeInstancesResponseInstancesInstancePublicIpAddressesPublicIpAddress(TeaModel):
    def __init__(self, ip=None, gate_way=None, isp=None):
        self.ip = ip                    # type: str
        self.gate_way = gate_way        # type: str
        self.isp = isp                  # type: str

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.gate_way, 'gate_way')
        self.validate_required(self.isp, 'isp')

    def to_map(self):
        result = {}
        result['Ip'] = self.ip
        result['GateWay'] = self.gate_way
        result['Isp'] = self.isp
        return result

    def from_map(self, map={}):
        self.ip = map.get('Ip')
        self.gate_way = map.get('GateWay')
        self.isp = map.get('Isp')
        return self


class DescribeInstancesResponseInstancesInstancePublicIpAddresses(TeaModel):
    def __init__(self, public_ip_address=None):
        self.public_ip_address = public_ip_address  # type: List[DescribeInstancesResponseInstancesInstancePublicIpAddressesPublicIpAddress]

    def validate(self):
        self.validate_required(self.public_ip_address, 'public_ip_address')
        if self.public_ip_address:
            for k in self.public_ip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PublicIpAddress'] = []
        if self.public_ip_address is not None:
            for k in self.public_ip_address:
                result['PublicIpAddress'].append(k.to_map() if k else None)
        else:
            result['PublicIpAddress'] = None
        return result

    def from_map(self, map={}):
        self.public_ip_address = []
        if map.get('PublicIpAddress') is not None:
            for k in map.get('PublicIpAddress'):
                temp_model = DescribeInstancesResponseInstancesInstancePublicIpAddressesPublicIpAddress()
                self.public_ip_address.append(temp_model.from_map(k))
        else:
            self.public_ip_address = None
        return self


class DescribeInstancesResponseInstancesInstancePrivateIpAddressesPrivateIpAddress(TeaModel):
    def __init__(self, ip=None, gate_way=None, isp=None):
        self.ip = ip                    # type: str
        self.gate_way = gate_way        # type: str
        self.isp = isp                  # type: str

    def validate(self):
        self.validate_required(self.ip, 'ip')
        self.validate_required(self.gate_way, 'gate_way')
        self.validate_required(self.isp, 'isp')

    def to_map(self):
        result = {}
        result['Ip'] = self.ip
        result['GateWay'] = self.gate_way
        result['Isp'] = self.isp
        return result

    def from_map(self, map={}):
        self.ip = map.get('Ip')
        self.gate_way = map.get('GateWay')
        self.isp = map.get('Isp')
        return self


class DescribeInstancesResponseInstancesInstancePrivateIpAddresses(TeaModel):
    def __init__(self, private_ip_address=None):
        self.private_ip_address = private_ip_address  # type: List[DescribeInstancesResponseInstancesInstancePrivateIpAddressesPrivateIpAddress]

    def validate(self):
        self.validate_required(self.private_ip_address, 'private_ip_address')
        if self.private_ip_address:
            for k in self.private_ip_address:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PrivateIpAddress'] = []
        if self.private_ip_address is not None:
            for k in self.private_ip_address:
                result['PrivateIpAddress'].append(k.to_map() if k else None)
        else:
            result['PrivateIpAddress'] = None
        return result

    def from_map(self, map={}):
        self.private_ip_address = []
        if map.get('PrivateIpAddress') is not None:
            for k in map.get('PrivateIpAddress'):
                temp_model = DescribeInstancesResponseInstancesInstancePrivateIpAddressesPrivateIpAddress()
                self.private_ip_address.append(temp_model.from_map(k))
        else:
            self.private_ip_address = None
        return self


class DescribeInstancesResponseInstancesInstanceSystemDisk(TeaModel):
    def __init__(self, device_type=None, storage=None, uuid=None, disk_type=None, name=None, category=None, size=None,
                 disk_id=None, disk_name=None):
        self.device_type = device_type  # type: str
        self.storage = storage          # type: int
        self.uuid = uuid                # type: str
        self.disk_type = disk_type      # type: str
        self.name = name                # type: str
        self.category = category        # type: str
        self.size = size                # type: int
        self.disk_id = disk_id          # type: str
        self.disk_name = disk_name      # type: str

    def validate(self):
        self.validate_required(self.device_type, 'device_type')
        self.validate_required(self.storage, 'storage')
        self.validate_required(self.uuid, 'uuid')
        self.validate_required(self.disk_type, 'disk_type')
        self.validate_required(self.name, 'name')
        self.validate_required(self.category, 'category')
        self.validate_required(self.size, 'size')
        self.validate_required(self.disk_id, 'disk_id')
        self.validate_required(self.disk_name, 'disk_name')

    def to_map(self):
        result = {}
        result['device_type'] = self.device_type
        result['storage'] = self.storage
        result['uuid'] = self.uuid
        result['disk_type'] = self.disk_type
        result['name'] = self.name
        result['Category'] = self.category
        result['Size'] = self.size
        result['DiskId'] = self.disk_id
        result['DiskName'] = self.disk_name
        return result

    def from_map(self, map={}):
        self.device_type = map.get('device_type')
        self.storage = map.get('storage')
        self.uuid = map.get('uuid')
        self.disk_type = map.get('disk_type')
        self.name = map.get('name')
        self.category = map.get('Category')
        self.size = map.get('Size')
        self.disk_id = map.get('DiskId')
        self.disk_name = map.get('DiskName')
        return self


class DescribeInstancesResponseInstancesInstanceSecurityGroupIds(TeaModel):
    def __init__(self, security_group_id=None):
        # SecurityGroupId
        self.security_group_id = security_group_id  # type: List[str]

    def validate(self):
        self.validate_required(self.security_group_id, 'security_group_id')

    def to_map(self):
        result = {}
        result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, map={}):
        self.security_group_id = map.get('SecurityGroupId')
        return self


class DescribeInstancesResponseInstancesInstanceInnerIpAddress(TeaModel):
    def __init__(self, ip_address=None):
        # IpAddress
        self.ip_address = ip_address    # type: List[str]

    def validate(self):
        self.validate_required(self.ip_address, 'ip_address')

    def to_map(self):
        result = {}
        result['IpAddress'] = self.ip_address
        return result

    def from_map(self, map={}):
        self.ip_address = map.get('IpAddress')
        return self


class DescribeInstancesResponseInstancesInstancePublicIpAddress(TeaModel):
    def __init__(self, ip_address=None):
        # IpAddress
        self.ip_address = ip_address    # type: List[str]

    def validate(self):
        self.validate_required(self.ip_address, 'ip_address')

    def to_map(self):
        result = {}
        result['IpAddress'] = self.ip_address
        return result

    def from_map(self, map={}):
        self.ip_address = map.get('IpAddress')
        return self


class DescribeInstancesResponseInstancesInstance(TeaModel):
    def __init__(self, instance_id=None, instance_name=None, ens_region_id=None, cpu=None, memory=None, disk=None,
                 internet_max_bandwidth_in=None, internet_max_bandwidth_out=None, creation_time=None, status=None, host_name=None,
                 image_id=None, expired_time=None, instance_resource_type=None, spec_name=None, osname=None, data_disk=None,
                 public_ip_addresses=None, private_ip_addresses=None, system_disk=None, security_group_ids=None, inner_ip_address=None,
                 public_ip_address=None):
        self.instance_id = instance_id  # type: str
        self.instance_name = instance_name  # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.cpu = cpu                  # type: str
        self.memory = memory            # type: int
        self.disk = disk                # type: int
        self.internet_max_bandwidth_in = internet_max_bandwidth_in  # type: int
        self.internet_max_bandwidth_out = internet_max_bandwidth_out  # type: int
        self.creation_time = creation_time  # type: str
        self.status = status            # type: str
        self.host_name = host_name      # type: str
        self.image_id = image_id        # type: str
        self.expired_time = expired_time  # type: str
        self.instance_resource_type = instance_resource_type  # type: str
        self.spec_name = spec_name      # type: str
        self.osname = osname            # type: str
        self.data_disk = data_disk      # type: DescribeInstancesResponseInstancesInstanceDataDisk
        self.public_ip_addresses = public_ip_addresses  # type: DescribeInstancesResponseInstancesInstancePublicIpAddresses
        self.private_ip_addresses = private_ip_addresses  # type: DescribeInstancesResponseInstancesInstancePrivateIpAddresses
        self.system_disk = system_disk  # type: DescribeInstancesResponseInstancesInstanceSystemDisk
        self.security_group_ids = security_group_ids  # type: DescribeInstancesResponseInstancesInstanceSecurityGroupIds
        self.inner_ip_address = inner_ip_address  # type: DescribeInstancesResponseInstancesInstanceInnerIpAddress
        self.public_ip_address = public_ip_address  # type: DescribeInstancesResponseInstancesInstancePublicIpAddress

    def validate(self):
        self.validate_required(self.instance_id, 'instance_id')
        self.validate_required(self.instance_name, 'instance_name')
        self.validate_required(self.ens_region_id, 'ens_region_id')
        self.validate_required(self.cpu, 'cpu')
        self.validate_required(self.memory, 'memory')
        self.validate_required(self.disk, 'disk')
        self.validate_required(self.internet_max_bandwidth_in, 'internet_max_bandwidth_in')
        self.validate_required(self.internet_max_bandwidth_out, 'internet_max_bandwidth_out')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.status, 'status')
        self.validate_required(self.host_name, 'host_name')
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.expired_time, 'expired_time')
        self.validate_required(self.instance_resource_type, 'instance_resource_type')
        self.validate_required(self.spec_name, 'spec_name')
        self.validate_required(self.osname, 'osname')
        self.validate_required(self.data_disk, 'data_disk')
        if self.data_disk:
            self.data_disk.validate()
        self.validate_required(self.public_ip_addresses, 'public_ip_addresses')
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()
        self.validate_required(self.private_ip_addresses, 'private_ip_addresses')
        if self.private_ip_addresses:
            self.private_ip_addresses.validate()
        self.validate_required(self.system_disk, 'system_disk')
        if self.system_disk:
            self.system_disk.validate()
        self.validate_required(self.security_group_ids, 'security_group_ids')
        if self.security_group_ids:
            self.security_group_ids.validate()
        self.validate_required(self.inner_ip_address, 'inner_ip_address')
        if self.inner_ip_address:
            self.inner_ip_address.validate()
        self.validate_required(self.public_ip_address, 'public_ip_address')
        if self.public_ip_address:
            self.public_ip_address.validate()

    def to_map(self):
        result = {}
        result['InstanceId'] = self.instance_id
        result['InstanceName'] = self.instance_name
        result['EnsRegionId'] = self.ens_region_id
        result['Cpu'] = self.cpu
        result['Memory'] = self.memory
        result['Disk'] = self.disk
        result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        result['CreationTime'] = self.creation_time
        result['Status'] = self.status
        result['HostName'] = self.host_name
        result['ImageId'] = self.image_id
        result['ExpiredTime'] = self.expired_time
        result['InstanceResourceType'] = self.instance_resource_type
        result['SpecName'] = self.spec_name
        result['OSName'] = self.osname
        if self.data_disk is not None:
            result['DataDisk'] = self.data_disk.to_map()
        else:
            result['DataDisk'] = None
        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()
        else:
            result['PublicIpAddresses'] = None
        if self.private_ip_addresses is not None:
            result['PrivateIpAddresses'] = self.private_ip_addresses.to_map()
        else:
            result['PrivateIpAddresses'] = None
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        else:
            result['SystemDisk'] = None
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()
        else:
            result['SecurityGroupIds'] = None
        if self.inner_ip_address is not None:
            result['InnerIpAddress'] = self.inner_ip_address.to_map()
        else:
            result['InnerIpAddress'] = None
        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address.to_map()
        else:
            result['PublicIpAddress'] = None
        return result

    def from_map(self, map={}):
        self.instance_id = map.get('InstanceId')
        self.instance_name = map.get('InstanceName')
        self.ens_region_id = map.get('EnsRegionId')
        self.cpu = map.get('Cpu')
        self.memory = map.get('Memory')
        self.disk = map.get('Disk')
        self.internet_max_bandwidth_in = map.get('InternetMaxBandwidthIn')
        self.internet_max_bandwidth_out = map.get('InternetMaxBandwidthOut')
        self.creation_time = map.get('CreationTime')
        self.status = map.get('Status')
        self.host_name = map.get('HostName')
        self.image_id = map.get('ImageId')
        self.expired_time = map.get('ExpiredTime')
        self.instance_resource_type = map.get('InstanceResourceType')
        self.spec_name = map.get('SpecName')
        self.osname = map.get('OSName')
        if map.get('DataDisk') is not None:
            temp_model = DescribeInstancesResponseInstancesInstanceDataDisk()
            self.data_disk = temp_model.from_map(map['DataDisk'])
        else:
            self.data_disk = None
        if map.get('PublicIpAddresses') is not None:
            temp_model = DescribeInstancesResponseInstancesInstancePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(map['PublicIpAddresses'])
        else:
            self.public_ip_addresses = None
        if map.get('PrivateIpAddresses') is not None:
            temp_model = DescribeInstancesResponseInstancesInstancePrivateIpAddresses()
            self.private_ip_addresses = temp_model.from_map(map['PrivateIpAddresses'])
        else:
            self.private_ip_addresses = None
        if map.get('SystemDisk') is not None:
            temp_model = DescribeInstancesResponseInstancesInstanceSystemDisk()
            self.system_disk = temp_model.from_map(map['SystemDisk'])
        else:
            self.system_disk = None
        if map.get('SecurityGroupIds') is not None:
            temp_model = DescribeInstancesResponseInstancesInstanceSecurityGroupIds()
            self.security_group_ids = temp_model.from_map(map['SecurityGroupIds'])
        else:
            self.security_group_ids = None
        if map.get('InnerIpAddress') is not None:
            temp_model = DescribeInstancesResponseInstancesInstanceInnerIpAddress()
            self.inner_ip_address = temp_model.from_map(map['InnerIpAddress'])
        else:
            self.inner_ip_address = None
        if map.get('PublicIpAddress') is not None:
            temp_model = DescribeInstancesResponseInstancesInstancePublicIpAddress()
            self.public_ip_address = temp_model.from_map(map['PublicIpAddress'])
        else:
            self.public_ip_address = None
        return self


class DescribeInstancesResponseInstances(TeaModel):
    def __init__(self, instance=None):
        self.instance = instance        # type: List[DescribeInstancesResponseInstancesInstance]

    def validate(self):
        self.validate_required(self.instance, 'instance')
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        else:
            result['Instance'] = None
        return result

    def from_map(self, map={}):
        self.instance = []
        if map.get('Instance') is not None:
            for k in map.get('Instance'):
                temp_model = DescribeInstancesResponseInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        else:
            self.instance = None
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(self, product=None, version=None, ens_region_id=None, image_id=None, status=None, image_name=None,
                 page_number=None, page_size=None):
        self.product = product          # type: str
        self.version = version          # type: str
        self.ens_region_id = ens_region_id  # type: str
        self.image_id = image_id        # type: str
        self.status = status            # type: str
        self.image_name = image_name    # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size      # type: str

    def validate(self):
        self.validate_required(self.version, 'version')

    def to_map(self):
        result = {}
        result['product'] = self.product
        result['Version'] = self.version
        result['EnsRegionId'] = self.ens_region_id
        result['ImageId'] = self.image_id
        result['Status'] = self.status
        result['ImageName'] = self.image_name
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.product = map.get('product')
        self.version = map.get('Version')
        self.ens_region_id = map.get('EnsRegionId')
        self.image_id = map.get('ImageId')
        self.status = map.get('Status')
        self.image_name = map.get('ImageName')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(self, request_id=None, code=None, total_count=None, page_number=None, page_size=None, images=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int
        self.total_count = total_count  # type: int
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.images = images            # type: DescribeImagesResponseImages

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.images, 'images')
        if self.images:
            self.images.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        result['TotalCount'] = self.total_count
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        if self.images is not None:
            result['Images'] = self.images.to_map()
        else:
            result['Images'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        self.total_count = map.get('TotalCount')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        if map.get('Images') is not None:
            temp_model = DescribeImagesResponseImages()
            self.images = temp_model.from_map(map['Images'])
        else:
            self.images = None
        return self


class DescribeImagesResponseImagesImage(TeaModel):
    def __init__(self, image_id=None, image_name=None, image_owner_alias=None, platform=None, architecture=None,
                 creation_time=None, image_size=None):
        self.image_id = image_id        # type: str
        self.image_name = image_name    # type: str
        self.image_owner_alias = image_owner_alias  # type: str
        self.platform = platform        # type: str
        self.architecture = architecture  # type: str
        self.creation_time = creation_time  # type: str
        self.image_size = image_size    # type: str

    def validate(self):
        self.validate_required(self.image_id, 'image_id')
        self.validate_required(self.image_name, 'image_name')
        self.validate_required(self.image_owner_alias, 'image_owner_alias')
        self.validate_required(self.platform, 'platform')
        self.validate_required(self.architecture, 'architecture')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.image_size, 'image_size')

    def to_map(self):
        result = {}
        result['ImageId'] = self.image_id
        result['ImageName'] = self.image_name
        result['ImageOwnerAlias'] = self.image_owner_alias
        result['Platform'] = self.platform
        result['Architecture'] = self.architecture
        result['CreationTime'] = self.creation_time
        result['ImageSize'] = self.image_size
        return result

    def from_map(self, map={}):
        self.image_id = map.get('ImageId')
        self.image_name = map.get('ImageName')
        self.image_owner_alias = map.get('ImageOwnerAlias')
        self.platform = map.get('Platform')
        self.architecture = map.get('Architecture')
        self.creation_time = map.get('CreationTime')
        self.image_size = map.get('ImageSize')
        return self


class DescribeImagesResponseImages(TeaModel):
    def __init__(self, image=None):
        self.image = image              # type: List[DescribeImagesResponseImagesImage]

    def validate(self):
        self.validate_required(self.image, 'image')
        if self.image:
            for k in self.image:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Image'] = []
        if self.image is not None:
            for k in self.image:
                result['Image'].append(k.to_map() if k else None)
        else:
            result['Image'] = None
        return result

    def from_map(self, map={}):
        self.image = []
        if map.get('Image') is not None:
            for k in map.get('Image'):
                temp_model = DescribeImagesResponseImagesImage()
                self.image.append(temp_model.from_map(k))
        else:
            self.image = None
        return self


class StopInstanceRequest(TeaModel):
    def __init__(self, version=None, instance_id=None, force_stop=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str
        self.force_stop = force_stop    # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        result['ForceStop'] = self.force_stop
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        self.force_stop = map.get('ForceStop')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, version=None, instance_id=None, password=None, instance_name=None):
        self.version = version          # type: str
        self.instance_id = instance_id  # type: str
        self.password = password        # type: str
        self.instance_name = instance_name  # type: str

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.instance_id, 'instance_id')

    def to_map(self):
        result = {}
        result['Version'] = self.version
        result['InstanceId'] = self.instance_id
        result['Password'] = self.password
        result['InstanceName'] = self.instance_name
        return result

    def from_map(self, map={}):
        self.version = map.get('Version')
        self.instance_id = map.get('InstanceId')
        self.password = map.get('Password')
        self.instance_name = map.get('InstanceName')
        return self


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(self, request_id=None, code=None):
        self.request_id = request_id    # type: str
        self.code = code                # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.code, 'code')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Code'] = self.code
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.code = map.get('Code')
        return self
