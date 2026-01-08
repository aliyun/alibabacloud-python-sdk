# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSdlEventListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sdl_event_detail_list: List[main_models.DescribeSdlEventListResponseBodySdlEventDetailList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.sdl_event_detail_list = sdl_event_detail_list
        self.total_count = total_count

    def validate(self):
        if self.sdl_event_detail_list:
            for v1 in self.sdl_event_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SdlEventDetailList'] = []
        if self.sdl_event_detail_list is not None:
            for k1 in self.sdl_event_detail_list:
                result['SdlEventDetailList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sdl_event_detail_list = []
        if m.get('SdlEventDetailList') is not None:
            for k1 in m.get('SdlEventDetailList'):
                temp_model = main_models.DescribeSdlEventListResponseBodySdlEventDetailList()
                self.sdl_event_detail_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSdlEventListResponseBodySdlEventDetailList(DaraModel):
    def __init__(
        self,
        asset_name: str = None,
        asset_private_ip: str = None,
        asset_type: str = None,
        category_class_id: str = None,
        category_name: str = None,
        city_id: str = None,
        country_id: str = None,
        dst_ip: str = None,
        dst_port_list: str = None,
        event_cnt: int = None,
        event_level: str = None,
        event_name: str = None,
        first_time: int = None,
        last_time: int = None,
        location_name: str = None,
        payload: str = None,
        proto_list: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_id_type: int = None,
        sensitive_data_cnt: int = None,
        sensitive_data_list: List[str] = None,
        sensitive_level: str = None,
        sensitive_type: str = None,
        src_ip: str = None,
        src_port_list: str = None,
        traffic_bytes: int = None,
        uuid: str = None,
    ):
        self.asset_name = asset_name
        self.asset_private_ip = asset_private_ip
        self.asset_type = asset_type
        self.category_class_id = category_class_id
        self.category_name = category_name
        self.city_id = city_id
        self.country_id = country_id
        self.dst_ip = dst_ip
        self.dst_port_list = dst_port_list
        self.event_cnt = event_cnt
        self.event_level = event_level
        self.event_name = event_name
        self.first_time = first_time
        self.last_time = last_time
        self.location_name = location_name
        self.payload = payload
        self.proto_list = proto_list
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_id_type = resource_id_type
        self.sensitive_data_cnt = sensitive_data_cnt
        self.sensitive_data_list = sensitive_data_list
        self.sensitive_level = sensitive_level
        self.sensitive_type = sensitive_type
        self.src_ip = src_ip
        self.src_port_list = src_port_list
        self.traffic_bytes = traffic_bytes
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_private_ip is not None:
            result['AssetPrivateIp'] = self.asset_private_ip

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.category_class_id is not None:
            result['CategoryClassId'] = self.category_class_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.city_id is not None:
            result['CityId'] = self.city_id

        if self.country_id is not None:
            result['CountryId'] = self.country_id

        if self.dst_ip is not None:
            result['DstIp'] = self.dst_ip

        if self.dst_port_list is not None:
            result['DstPortList'] = self.dst_port_list

        if self.event_cnt is not None:
            result['EventCnt'] = self.event_cnt

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.location_name is not None:
            result['LocationName'] = self.location_name

        if self.payload is not None:
            result['Payload'] = self.payload

        if self.proto_list is not None:
            result['ProtoList'] = self.proto_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_id_type is not None:
            result['ResourceIdType'] = self.resource_id_type

        if self.sensitive_data_cnt is not None:
            result['SensitiveDataCnt'] = self.sensitive_data_cnt

        if self.sensitive_data_list is not None:
            result['SensitiveDataList'] = self.sensitive_data_list

        if self.sensitive_level is not None:
            result['SensitiveLevel'] = self.sensitive_level

        if self.sensitive_type is not None:
            result['SensitiveType'] = self.sensitive_type

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.src_port_list is not None:
            result['SrcPortList'] = self.src_port_list

        if self.traffic_bytes is not None:
            result['TrafficBytes'] = self.traffic_bytes

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetPrivateIp') is not None:
            self.asset_private_ip = m.get('AssetPrivateIp')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CategoryClassId') is not None:
            self.category_class_id = m.get('CategoryClassId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')

        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')

        if m.get('DstIp') is not None:
            self.dst_ip = m.get('DstIp')

        if m.get('DstPortList') is not None:
            self.dst_port_list = m.get('DstPortList')

        if m.get('EventCnt') is not None:
            self.event_cnt = m.get('EventCnt')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        if m.get('ProtoList') is not None:
            self.proto_list = m.get('ProtoList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceIdType') is not None:
            self.resource_id_type = m.get('ResourceIdType')

        if m.get('SensitiveDataCnt') is not None:
            self.sensitive_data_cnt = m.get('SensitiveDataCnt')

        if m.get('SensitiveDataList') is not None:
            self.sensitive_data_list = m.get('SensitiveDataList')

        if m.get('SensitiveLevel') is not None:
            self.sensitive_level = m.get('SensitiveLevel')

        if m.get('SensitiveType') is not None:
            self.sensitive_type = m.get('SensitiveType')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('SrcPortList') is not None:
            self.src_port_list = m.get('SrcPortList')

        if m.get('TrafficBytes') is not None:
            self.traffic_bytes = m.get('TrafficBytes')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

